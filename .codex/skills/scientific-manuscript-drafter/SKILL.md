---
name: scientific-manuscript-drafter
description: Draft or revise a peer-review-ready scientific manuscript from provided evidence, experiments, notes, code outputs, figures, tables, and verified references. Use when Codex must turn research artifacts into a paper while preserving claim-evidence traceability. Do not use for independent literature invention, citation fabrication, or unsupported claim generation.
---

# Scientific Manuscript Drafter

## Core Rule

Write only claims supported by supplied evidence, verified references, derivations, experiments, figures, tables, code outputs, or clearly marked author-provided assumptions. Do not invent results, citations, datasets, baselines, limitations, or novelty claims.

If available, apply the shared protocol in `../_shared/scientific-paper-common.md`.

## Workflow

1. Inventory available evidence:
   - manuscript drafts,
   - research notes,
   - hypotheses or research questions,
   - experiment logs,
   - tables and figures,
   - code outputs,
   - data descriptions,
   - verified bibliography files.
2. Build a claim-evidence table before drafting:
   - claim,
   - evidence source,
   - manuscript location or intended location,
   - confidence,
   - missing support.
3. Select the paper type: empirical, theoretical, systems, dataset, benchmark, survey/review, position, or mixed.
4. Draft in this order:
   - contribution statement,
   - outline,
   - method, theory, system, dataset, or evaluation sections,
   - results or formal findings,
   - discussion and limitations,
   - introduction,
   - abstract,
   - conclusion.
5. Preserve traceability while drafting. Each major claim must point to a result, derivation, artifact, figure, table, citation, or stated assumption.
6. Invoke or recommend the reviewer skills in this order:
   - `scientific-structure-reviewer`,
   - `technical-reviewer`,
   - `citation-reference-reviewer`,
   - `writing-reviewer`.

## Peer-Review-Ready Manuscript Expectations

Draft papers with the usual scientific article elements when appropriate:

- title that matches the actual contribution and evidence,
- abstract summarizing problem, method, main result, conclusion, and implication,
- introduction with motivation, gap, research question, and contributions,
- related work that positions the contribution rather than listing background,
- reproducible method, theory, system, dataset, or review protocol,
- evaluation, results, or formal findings that answer the research question,
- discussion that interprets results and limitations,
- conclusion that states what was established without adding new evidence,
- references that directly support the work.

Do not add sections merely to match a template. Use sections that make the scientific argument verifiable.

## Claim Safety

Do not write or strengthen claims such as `novel`, `first`, `state of the art`, `robust`, `significant`, `efficient`, `scalable`, or `superior` unless the supplied evidence defines the comparison, metric, baseline, scope, and uncertainty.

Mark unsupported or weakly supported claims as unresolved instead of making them sound polished.

## Output Format

Return drafting work in this order:

1. `Evidence inventory`
2. `Claim-evidence table`
3. `Proposed paper type and publication fit`
4. `Draft outline`
5. `Draft manuscript text`
6. `Unsupported or unresolved claims`
7. `Reviewer-skill handoff plan`
