---
name: citation-reference-reviewer
description: Audit LaTeX/BibTeX references and IEEE-style citations for real-source existence, metadata correctness, DOI/URL validity, fabricated citations, missing keys, uncited entries, duplicate sources, and in-text/bibliography consistency. Use for citation verification, bibliography repair, DOI checks, and reference-list audits. Do not use for general prose review.
---

# Citation and Reference Reviewer

## Non-Negotiable Verification Rule

Verify every reference against authoritative external sources before declaring it correct. Do not assume that titles, author lists, venues, years, DOIs, arXiv IDs, URLs, or BibTeX fields are accurate because they look plausible.

If available, apply the shared protocol in `../_shared/scientific-paper-common.md`.

## Source Priority

Use this source priority:

1. Publisher or official proceedings page.
2. DOI registration metadata: Crossref, DataCite, DOI.org resolver.
3. Indexing databases: IEEE Xplore, ACM Digital Library, SpringerLink, ScienceDirect, Wiley, PubMed, DBLP, OpenReview, arXiv.
4. Author or institutional repository.
5. General web search only to locate one of the above.

If sources disagree, report the disagreement and prefer publisher or proceedings metadata unless there is evidence of publisher metadata error.

## Inputs to Inspect

Inspect all available manuscript and bibliography files:

- LaTeX source files: `.tex`, included sections, appendices, and supplementary material.
- Bibliography files: `.bib`, generated `.bbl`, or reference lists if BibTeX is not yet available.
- Citation commands: `\cite`, `\citep`, `\citet`, `\citeauthor`, `\citealp`, `\parencite`, `\textcite`, and custom citation macros.
- URLs, DOIs, arXiv IDs, standards identifiers, dataset references, software references, and online documentation references.

All maintained references must remain in BibTeX format unless the user explicitly asks for another format.

## Deterministic Inventory Step

Before external verification, generate a machine-readable citation inventory when possible.

Use `scripts/citation_inventory.py` when available:

```bash
python .codex/skills/citation-reference-reviewer/scripts/citation_inventory.py --root . --out citation_inventory.json --md citation_audit.md
```

Required checks:

- all `\cite`, `\citep`, `\citet`, `\citeauthor`, `\citealp`, `\parencite`, `\textcite`, and custom citation commands;
- citation keys used in `.tex` but missing from `.bib`;
- `.bib` entries never cited;
- duplicate BibTeX keys;
- likely duplicate sources with different keys;
- DOI strings that are malformed, duplicated, or represented as URLs in the `doi` field;
- URLs without access dates if the project style requires them.

When writing inventory outputs, use:

- `citation_inventory.json`
- `citation_audit.md`

## Verification Workflow

1. Build or read the citation inventory: all in-text citation keys, all BibTeX keys, uncited entries, missing entries, duplicate entries, malformed DOI fields, and repeated sources under different keys.
2. For each BibTeX entry, verify existence and metadata from authoritative sources:
   - authors and author order,
   - title and capitalization,
   - venue or publisher,
   - year, volume, number, pages, article number, edition, or version,
   - DOI, ISBN, ISSN, arXiv ID, standard number, dataset/software version, and URL.
3. Test DOI format and resolution using `https://doi.org/<doi>` or an authoritative metadata source.
4. Check URL accessibility and whether the URL is stable enough for a formal paper. Prefer DOI, publisher, standard, repository, or archival URLs over unstable web pages.
5. Detect suspicious entries: missing venue, improbable venue/year combinations, fake-looking DOIs, non-resolving DOI links, title mismatch, author mismatch, fabricated proceedings, or citation keys without matching source records.
6. Check IEEE practice: numeric citation style, citation placement, no author-year phrasing unless textually necessary, no citation clusters used as vague evidence, no unsupported statements hidden behind broad citation groups, and no numbered reference entry representing a group of sources.
7. Produce corrected BibTeX entries for every fix. Preserve citation keys unless renaming is clearly beneficial and all in-text uses can be updated.

## Common Fabrication or Metadata Error Patterns

Flag entries with:

- plausible title but no authoritative record;
- DOI prefix that belongs to a different publisher or venue;
- conference year that does not match the proceedings;
- arXiv title that differs from the published title without explanation;
- workshop papers cited as full conference papers;
- preprints cited as peer-reviewed publications;
- missing pages or article numbers where the publisher record has them;
- Google Scholar-only metadata with no authoritative source.

## BibTeX Quality Rules

- Use canonical BibTeX entry types: `@article`, `@inproceedings`, `@book`, `@incollection`, `@techreport`, `@misc`, `@standard`, `@manual`, `@phdthesis`, `@mastersthesis`, or toolchain-supported alternatives.
- For BibTeX `doi` fields, prefer bare DOI strings unless the project style requires DOI URLs. For displayed reference text or publisher-facing links, prefer the canonical `https://doi.org/...` form.
- Use `url` for stable non-DOI resources and include `urldate` only if the bibliography style supports it or the project already uses it.
- Preserve proper nouns and acronyms with braces in titles, such as `{IEEE}`, `{GPU}`, or method names.
- Do not invent missing page numbers, issue numbers, DOIs, or venues.
- For arXiv-only works, include `eprint`, `archivePrefix = {arXiv}`, and `primaryClass` when available.
- For standards, include issuing organization, standard number, title, year, and DOI or stable URL when available.
- For datasets and software, include version, repository or archive, DOI if available, and access information only when required by the bibliography style.
- IEEE reference-list rule: do not use one numbered reference entry to represent a group of sources. Each source must have its own reference number.

## Uncertainty Rule

If a citation, source record, DOI, URL, or metadata field cannot be verified from supplied files or authoritative external sources, mark it as unresolved. Do not silently repair it by inventing missing information.

## Output Format

Return the audit in this order:

1. `Verification summary`: counts of citations, BibTeX entries, verified entries, corrected entries, unresolved entries, uncited entries, and missing entries.
2. `Inventory results`: citation inventory path if generated, missing keys, uncited keys, duplicate keys, duplicate DOI/source candidates, and malformed DOI fields.
3. `Critical reference problems`: fabricated, non-resolving, mismatched, duplicate, or missing sources that must be fixed.
4. `Citation consistency`: missing keys, uncited references, duplicate keys, citation clusters that need explanation, and IEEE style issues.
5. `Per-reference audit table`: key, source status, metadata status, DOI/URL status, authoritative source used, and required action.
6. `Corrected BibTeX`: provide complete replacement entries for entries that need correction.
7. `Unresolved items`: list sources that could not be verified and the exact authoritative searches attempted.

## Evidence Discipline

When reporting verification, cite or name the authoritative source used for each correction. If external access is unavailable, mark entries as `not externally verified` and explain that final authenticity checks remain pending.
