---
name: scientific-structure-reviewer
description: Review a scientific manuscript outline or draft for peer-review-ready structure, scientific story, contribution framing, section order, paper-type fit, motivation, gap, and narrative coherence. Use before detailed technical or prose review. Do not use for citation verification or line editing.
---

# Scientific Structure and Outline Reviewer

## Boundary

Evaluate whether the manuscript structure supports the scientific argument. Identify missing evidence at a high level, but leave detailed validity of methods, experiments, proofs, metrics, artifacts, and claims to `technical-reviewer`. Do not perform citation verification or line editing.

If available, apply the shared protocol in `../_shared/scientific-paper-common.md`.

## Recommended Review Order

When multiple manuscript-review skills are relevant, use this order:

1. `scientific-structure-reviewer` - decide whether the paper shape works.
2. `technical-reviewer` - verify claims, methods, experiments, and interpretation.
3. `citation-reference-reviewer` - verify references and citation consistency.
4. `writing-reviewer` - polish prose without changing scientific meaning.

Do not perform line editing before structural, technical, or citation problems are identified.

## Review Workflow

1. Identify the intended paper type, audience, publication context if known, and current writing stage.
2. Extract the manuscript's scientific story: context, problem, gap, objective, contribution, method or review approach, evidence, insight, limitations, and conclusion.
3. State the reader promise: what the title, abstract, and introduction promise the reader.
4. Check whether the rest of the outline fulfills that reader promise without overclaiming.
5. Evaluate whether the outline lets a reader understand why the work matters, what is new, how it was validated, and what can be concluded.
6. Check section order and section purpose before sentence-level issues.
7. Recommend concrete restructuring steps that can be applied before or during writing.

## Peer-Review-Ready Structure Checks

Assess whether the manuscript has:

- A title and abstract that match the actual contribution and evidence.
- An introduction with motivation, precise problem statement, gap in prior work, contributions, and paper organization.
- Related work that positions the paper rather than becoming a generic background section.
- A method, theory, framework, system, or review methodology section with enough structure to support later claims.
- Experiments, evaluation, analysis, or synthesis sections that map directly to research questions or contributions.
- A discussion that interprets findings, limitations, and implications rather than repeating results.
- A conclusion that states what was established and what remains open without introducing new evidence.
- Section headings that communicate scientific function, not only implementation chronology.
- Balanced coverage: no excessive background, underdeveloped method, thin evaluation, or missing discussion.

## Paper-Type Specific Structure

For empirical papers, check coherence among introduction, related work, methodology, experiments, results, discussion, threats to validity, and conclusion.

For theoretical or algorithmic papers, check flow from definitions and assumptions to proposed result, proof or analysis, comparison, implications, and limitations.

For systems papers, check flow from requirements and design goals to architecture, implementation, evaluation methodology, results, operational lessons, and limitations.

For dataset or benchmark papers, check flow from motivation and scope to construction protocol, quality controls, metadata, access, baselines, tasks, limitations, and intended use.

For review or survey papers, check coherence among introduction, review scope, literature search methodology, inclusion/exclusion criteria, taxonomy or classification framework, comparative synthesis, open challenges, future research directions, and conclusion.

## Section Purpose Checks

For each section, determine:

- What question this section answers for the reader.
- Which contribution or claim it supports.
- Whether it appears at the right point in the argument.
- Whether it repeats another section or contains content that belongs elsewhere.
- What evidence, figure, table, definition, or transition is missing.

## Uncertainty Rule

If the outline promises a claim that cannot be verified from supplied manuscript material, mark the support as unresolved. Do not invent missing experiments, citations, results, or contributions to repair the structure.

## Output Format

Return the review in this order:

1. `Structural verdict`: concise assessment of whether the current outline can support a peer-review-ready scientific manuscript.
2. `Reader promise`: what the title, abstract, and introduction promise, and whether the manuscript fulfills that promise.
3. `Scientific story map`: one-paragraph reconstruction of the intended narrative and where it currently breaks down.
4. `Outline assessment`: section-by-section evaluation of purpose, order, missing content, redundant content, and balance.
5. `Major restructuring recommendations`: concrete section moves, merges, splits, additions, or deletions.
6. `Paper-type fit`: assess whether the structure matches the manuscript type and list missing paper-type-specific elements.
7. `Contribution and motivation review`: evaluate problem statement, research gap, contribution framing, and novelty positioning.
8. `Proposed revised outline`: provide section titles and 1-2 sentence purpose statements.
9. `Unresolved structural support`: claims, sections, or promises that need evidence before drafting or polishing.

## Recommendation Rules

- Keep recommendations actionable and tied to specific sections.
- Prefer outline changes that improve reader comprehension and evidentiary logic.
- Do not add sections merely because a template includes them; explain why each section is needed.
- If the paper type is ambiguous, state the plausible types and how the outline would differ for each.
