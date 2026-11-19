---
name: writing-reviewer
description: Review or rewrite scientific manuscript prose for peer-review-ready clarity, concision, paragraph flow, terminology consistency, grammar, tone, and professional wording while preserving technical meaning. Use after structure and technical claims are stable. Do not strengthen unsupported claims.
---

# Writing Reviewer

## Review Position

Use this skill after the manuscript's structure, technical claims, and citations are reasonably stable. If the prose is polished but the claim is unsupported, flag the support problem instead of making the sentence more persuasive.

If available, apply the shared protocol in `../_shared/scientific-paper-common.md`.

## Review Workflow

1. Identify the manuscript type, publication context if stated, paper stage, and the sections provided. If only a partial draft is available, review the visible text without inventing missing content.
2. Read for the scientific claim path: motivation, gap, contribution, method, evidence, interpretation, and conclusion. Flag places where the prose obscures that path.
3. Review at three levels: paper/section flow, paragraph logic, and sentence-level clarity.
4. Preserve the author's technical meaning. Do not rewrite claims to be stronger than the evidence supports.
5. Prefer direct, precise, formal scientific prose. Remove promotional language, vague intensifiers, excessive hedging, and conversational phrasing.

## Rewrite Safety

When rewriting, preserve:

- claim strength,
- uncertainty level,
- causal vs. correlational wording,
- scope conditions,
- limitations,
- metric names and values,
- dataset and baseline names,
- citation placement.

Use bracketed placeholders such as `[metric]`, `[dataset]`, or `[result]` when information is missing. Do not fill placeholders with invented details.

## Peer-Review-Ready Writing Checks

Check for:

- Clear problem framing and contribution statements in the abstract and introduction.
- Concise abstract with motivation, method, main result, and significance, without citations unless unavoidable.
- Introduction that moves from broad context to specific gap and contributions.
- Paragraphs with one main point, topic sentence, evidence or explanation, and transition.
- Consistent terminology for methods, datasets, variables, baselines, metrics, and contributions.
- Appropriate tense: present for general truths and paper structure, past for completed experiments, present perfect for prior work when relevant.
- Objective tone: avoid `novel`, `significant`, `superior`, `robust`, or `state of the art` unless substantiated.
- Formal scientific phrasing: avoid first-person overuse, contractions, rhetorical questions, bullet-heavy argumentation in the main text, and informal transitions.
- Figures and tables introduced before interpretation and discussed with specific takeaways.
- Acronyms defined on first use and used consistently afterward.
- Grammar, punctuation, hyphenation, capitalization, and notation consistency.
- Artifact-language leaks: main manuscript prose must not contain local file paths, source filenames, shell commands, build-system details, repository-relative paths, internal audit filenames, raw result filenames, or implementation-only terms unless they are explicitly required in an artifact availability statement, appendix, supplementary-material section, or reproducibility checklist.
- Deliverable-format mismatch: if the requested paper format is Markdown, Word, plain text, journal LaTeX, or another format, flag any manuscript or generated output that uses a different primary format or leaks syntax from another format, such as LaTeX commands in Markdown or Markdown table syntax in LaTeX.

## Uncertainty Rule

If a sentence depends on a claim, citation, result, or interpretation that cannot be verified from the supplied material, mark it as unresolved. Do not make unresolved claims sound more certain, general, causal, or important.

## Output Format

Return the review in this order:

1. `Overall assessment`: 3-6 sentences on readiness and the most important writing risks.
2. `Truth-preservation risks`: polished or persuasive wording that may overstate evidence, causality, novelty, or scope.
3. `High-priority revisions`: numbered issues that materially affect clarity, flow, or peer-review-ready scientific professionalism. Include location, problem, why it matters, and concrete fix.
4. `Section-level comments`: concise notes by section, including missing transitions, redundant content, misplaced background, or unclear paragraph purpose.
5. `Line-level or sentence-level suggestions`: rewrite candidates for awkward, verbose, ambiguous, or non-peer-review-ready sentences.
6. `Terminology and style consistency`: inconsistent terms, acronyms, tense shifts, and notation style issues.
7. `Artifact-language and format issues`: local paths, source/build filenames, commands, internal artifact references, or wrong-format syntax that should be removed from the main paper or moved to supplementary material.
8. `Suggested rewrites`: polished alternatives for the abstract, contribution paragraph, topic sentences, or transitions when useful.
9. `Unresolved support problems`: prose that cannot be safely rewritten until evidence or citations are clarified.

## Rewrite Rules

- Keep rewrites technically faithful to the supplied manuscript.
- Prefer compact scientific sentences over elaborate phrasing.
- When suggesting a rewrite, explain the intended improvement briefly.
- If the manuscript is very rough, prioritize structural prose fixes before grammar polish.
