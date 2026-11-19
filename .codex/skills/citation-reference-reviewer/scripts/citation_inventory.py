#!/usr/bin/env python3
"""Build a deterministic LaTeX/BibTeX citation inventory."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


CITE_COMMANDS = (
    "cite",
    "citep",
    "citet",
    "citeauthor",
    "citealp",
    "parencite",
    "textcite",
)

BIB_ENTRY_RE = re.compile(r"@(?P<type>[A-Za-z]+)\s*\{\s*(?P<key>[^,\s]+)\s*,", re.MULTILINE)
FIELD_RE = re.compile(
    r"(?P<field>[A-Za-z][A-Za-z0-9_-]*)\s*=\s*(?P<value>\{(?:[^{}]|\{[^{}]*\})*\}|\"[^\"]*\"|[^,\n]+)",
    re.MULTILINE,
)
DOI_SHAPE_RE = re.compile(r"^10\.\d{4,9}/\S+$", re.IGNORECASE)


def strip_comments(text: str) -> str:
    lines = []
    for line in text.splitlines():
        escaped = False
        out = []
        for ch in line:
            if ch == "%" and not escaped:
                break
            out.append(ch)
            escaped = ch == "\\" and not escaped
            if ch != "\\":
                escaped = False
        lines.append("".join(out))
    return "\n".join(lines)


def clean_value(value: str) -> str:
    value = value.strip().rstrip(",").strip()
    if len(value) >= 2 and ((value[0] == "{" and value[-1] == "}") or (value[0] == '"' and value[-1] == '"')):
        value = value[1:-1]
    return re.sub(r"\s+", " ", value.strip())


def citation_regex(extra_commands: list[str]) -> re.Pattern[str]:
    commands = sorted(set(CITE_COMMANDS).union(c.strip().lstrip("\\") for c in extra_commands if c.strip()))
    return re.compile(
        r"\\(?P<cmd>" + "|".join(re.escape(c) for c in commands) + r")\*?"
        r"(?:\[[^\]]*\]){0,2}\{(?P<keys>[^{}]+)\}"
    )


def read_tex_citations(tex_files: list[Path], cite_re: re.Pattern[str]) -> tuple[list[dict], Counter]:
    occurrences = []
    counts: Counter[str] = Counter()
    for path in tex_files:
        text = strip_comments(path.read_text(errors="replace"))
        for match in cite_re.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            keys = [k.strip() for k in match.group("keys").split(",") if k.strip()]
            for key in keys:
                counts[key] += 1
                occurrences.append(
                    {
                        "key": key,
                        "command": match.group("cmd"),
                        "file": str(path),
                        "line": line,
                    }
                )
    return occurrences, counts


def entry_blocks(text: str) -> list[tuple[str, str, str]]:
    matches = list(BIB_ENTRY_RE.finditer(text))
    blocks = []
    for i, match in enumerate(matches):
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        blocks.append((match.group("type"), match.group("key"), text[start:end]))
    return blocks


def read_bib_entries(bib_files: list[Path]) -> tuple[list[dict], Counter]:
    entries = []
    key_counts: Counter[str] = Counter()
    for path in bib_files:
        text = path.read_text(errors="replace")
        for entry_type, key, block in entry_blocks(text):
            key_counts[key] += 1
            fields = {m.group("field").lower(): clean_value(m.group("value")) for m in FIELD_RE.finditer(block)}
            entries.append(
                {
                    "key": key,
                    "type": entry_type.lower(),
                    "file": str(path),
                    "title": fields.get("title", ""),
                    "year": fields.get("year", ""),
                    "doi": fields.get("doi", ""),
                    "url": fields.get("url", ""),
                    "author": fields.get("author", ""),
                }
            )
    return entries, key_counts


def normalize_title(title: str) -> str:
    title = re.sub(r"[{}\\]", "", title).lower()
    title = re.sub(r"[^a-z0-9]+", " ", title)
    return re.sub(r"\s+", " ", title).strip()


def build_inventory(root: Path, extra_commands: list[str]) -> dict:
    tex_files = sorted(p for p in root.rglob("*.tex") if ".git" not in p.parts)
    bib_files = sorted(p for p in root.rglob("*.bib") if ".git" not in p.parts)
    occurrences, citation_counts = read_tex_citations(tex_files, citation_regex(extra_commands))
    entries, bib_key_counts = read_bib_entries(bib_files)
    bib_keys = {e["key"] for e in entries}
    cited_keys = set(citation_counts)

    doi_to_keys: dict[str, list[str]] = defaultdict(list)
    title_to_keys: dict[str, list[str]] = defaultdict(list)
    malformed_doi = []
    doi_url_fields = []
    for entry in entries:
        doi = entry.get("doi", "").strip()
        if doi:
            doi_lower = doi.lower()
            normalized_doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi_lower).strip()
            doi_to_keys[normalized_doi].append(entry["key"])
            if doi_lower.startswith(("http://doi.org/", "https://doi.org/", "http://dx.doi.org/", "https://dx.doi.org/")):
                doi_url_fields.append({"key": entry["key"], "doi": doi})
            if not DOI_SHAPE_RE.match(normalized_doi):
                malformed_doi.append({"key": entry["key"], "doi": doi})
        title_norm = normalize_title(entry.get("title", ""))
        if title_norm:
            title_to_keys[title_norm].append(entry["key"])

    duplicate_dois = {doi: keys for doi, keys in doi_to_keys.items() if len(set(keys)) > 1}
    duplicate_titles = {title: keys for title, keys in title_to_keys.items() if len(set(keys)) > 1}

    return {
        "root": str(root),
        "tex_files": [str(p) for p in tex_files],
        "bib_files": [str(p) for p in bib_files],
        "citation_commands": sorted(set(CITE_COMMANDS).union(c.strip().lstrip("\\") for c in extra_commands if c.strip())),
        "citation_occurrences": occurrences,
        "citation_counts": dict(sorted(citation_counts.items())),
        "bib_entries": entries,
        "missing_bib_entries": sorted(cited_keys - bib_keys),
        "uncited_bib_entries": sorted(bib_keys - cited_keys),
        "duplicate_bib_keys": sorted(k for k, count in bib_key_counts.items() if count > 1),
        "doi_url_fields": doi_url_fields,
        "malformed_doi_fields": malformed_doi,
        "duplicate_dois": duplicate_dois,
        "likely_duplicate_titles": duplicate_titles,
        "summary": {
            "tex_file_count": len(tex_files),
            "bib_file_count": len(bib_files),
            "citation_occurrence_count": len(occurrences),
            "cited_key_count": len(cited_keys),
            "bib_entry_count": len(entries),
            "missing_bib_entry_count": len(cited_keys - bib_keys),
            "uncited_bib_entry_count": len(bib_keys - cited_keys),
            "duplicate_bib_key_count": sum(1 for count in bib_key_counts.values() if count > 1),
            "malformed_doi_count": len(malformed_doi),
            "doi_url_field_count": len(doi_url_fields),
            "duplicate_doi_count": len(duplicate_dois),
            "likely_duplicate_title_count": len(duplicate_titles),
        },
    }


def write_markdown(inventory: dict, path: Path) -> None:
    summary = inventory["summary"]
    lines = [
        "# Citation Audit",
        "",
        "## Summary",
        "",
    ]
    for key, value in summary.items():
        lines.append(f"- `{key}`: {value}")
    sections = [
        ("Missing BibTeX Entries", inventory["missing_bib_entries"]),
        ("Uncited BibTeX Entries", inventory["uncited_bib_entries"]),
        ("Duplicate BibTeX Keys", inventory["duplicate_bib_keys"]),
        ("Malformed DOI Fields", inventory["malformed_doi_fields"]),
        ("DOI URL Fields", inventory["doi_url_fields"]),
        ("Duplicate DOIs", inventory["duplicate_dois"]),
        ("Likely Duplicate Titles", inventory["likely_duplicate_titles"]),
    ]
    for title, data in sections:
        lines.extend(["", f"## {title}", ""])
        if not data:
            lines.append("None detected.")
        elif isinstance(data, dict):
            for item, keys in sorted(data.items()):
                lines.append(f"- `{item}`: {', '.join(f'`{k}`' for k in keys)}")
        else:
            for item in data:
                if isinstance(item, dict):
                    lines.append("- " + ", ".join(f"`{k}`: {v}" for k, v in item.items()))
                else:
                    lines.append(f"- `{item}`")
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Project root to scan")
    parser.add_argument("--out", default="citation_inventory.json", help="JSON inventory path")
    parser.add_argument("--md", default="citation_audit.md", help="Markdown audit path")
    parser.add_argument(
        "--extra-command",
        action="append",
        default=[],
        help="Additional citation command name to parse, for example mycite or \\mycite",
    )
    args = parser.parse_args()

    inventory = build_inventory(Path(args.root).resolve(), args.extra_command)
    Path(args.out).write_text(json.dumps(inventory, indent=2, sort_keys=True) + "\n")
    write_markdown(inventory, Path(args.md))
    print(json.dumps(inventory["summary"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
