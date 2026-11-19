---
name: technical-reviewer
description: Review a scientific manuscript, method, experiment plan, results, or rebuttal for technical correctness, claim-evidence support, methodology, baselines, metrics, statistics, assumptions, interpretation, reproducibility, and reviewer-critical rigor issues. Do not use for grammar-only editing or bibliography metadata checks.
---

# Technical Reviewer

## Review Position

Use this skill after the scientific structure is roughly clear and before prose polishing. This skill evaluates scientific truth and rigor, not grammar-only editing or bibliography metadata.

If available, apply the shared protocol in `../_shared/scientific-paper-common.md`.

## Review Workflow

1. Determine the paper type: empirical, theoretical, systems, algorithmic, dataset, benchmark, survey/review, position, or mixed.
2. Inspect all available manuscript files, result tables, figures, logs, notebooks, scripts, datasets, configuration files, and supplementary artifacts relevant to the claims.
3. Extract the central claims, contributions, assumptions, methodology, evidence, stated limitations, and reproducibility claims.
4. Build a claim-evidence map with exact manuscript and evidence locations.
5. Check whether each claim is supported by method, experiment, derivation, citation, implementation artifact, dataset, benchmark, or clearly stated reasoning.
6. Evaluate whether the methodology can answer the research questions and whether the results justify the conclusions.
7. Separate fatal flaws from fixable presentation gaps. Do not overstate a concern when the available manuscript simply lacks detail.

## Claim-Evidence Map Requirements

For each major claim, include:

- exact manuscript location;
- claim type: novelty, correctness, performance, generality, causal, empirical, theoretical, usability, safety, or reproducibility;
- support type: experiment, proof, derivation, citation, implementation artifact, dataset, benchmark, expert judgment, or unsupported;
- evidence location: table, figure, equation, section, log file, script, dataset, or reference;
- verdict: supported, partially supported, unsupported, contradicted, or unverifiable.

Do not accept `better`, `robust`, `efficient`, `scalable`, `state of the art`, `significant`, `first`, or `novel` without a defined comparison, metric, baseline, scope, and evidence.

## Core Checks

Assess:

- Problem formulation: precise objective, assumptions, scope, constraints, and definitions.
- Related work positioning: fair comparison, correct distinction from prior work, and no unsupported novelty claims.
- Methodology: valid design choices, reproducibility details, algorithmic clarity, theoretical soundness, and implementation assumptions.
- Experimental design: appropriate datasets, sampling, train/test separation, baselines, ablations, controls, statistical analysis, and sensitivity analysis.
- Metrics: correct metric definitions, suitable metrics for the research question, uncertainty reporting, and avoidance of misleading aggregate results.
- Results: consistency between tables, figures, logs, artifacts, narrative, and conclusions.
- Interpretation: no causal claims from correlational evidence, no generalization beyond tested settings, and no selective reporting.
- Threats to validity: internal, external, construct, and conclusion validity where appropriate.
- Reproducibility: parameters, hardware/software, random seeds, data availability, code availability, and enough detail to repeat the study.
- Ethical, safety, privacy, or deployment risks if relevant to the work.

## Paper-Type Specific Checks

For empirical papers, verify coherence among research questions, hypotheses, methodology, experiments, results, discussion, limitations, and conclusion.

For theoretical or algorithmic papers, verify definitions, assumptions, theorem statements, proof sketches, complexity analysis, edge cases, and comparison with known results.

For systems papers, verify architecture rationale, workload realism, implementation detail, performance evaluation, scalability, fault tolerance, and operational constraints.

For dataset or benchmark papers, verify data provenance, collection protocol, splits, licensing, leakage controls, baseline tasks, quality checks, and artifact availability.

For survey or review papers, verify literature search scope, inclusion/exclusion criteria, taxonomy quality, comparative synthesis, and whether open challenges follow from the reviewed literature.

## Uncertainty Rule

If a claim, result, artifact, or interpretation cannot be verified from supplied files or authoritative external sources, mark it as unresolved or unverifiable. Do not silently repair missing evidence by inventing experiments, assumptions, or citations.

## Output Format

Return the review in this order:

1. `Technical verdict`: concise assessment of current scientific soundness and main risks.
2. `Claim-evidence map`: claim-by-claim table using the required fields above.
3. `Major technical issues`: numbered findings with location, issue, consequence, and recommended fix.
4. `Methodology and experiment review`: specific recommendations for design, baselines, ablations, metrics, statistics, and reproducibility.
5. `Artifact and result-file review`: artifacts inspected, commands or checks run if any, and gaps that prevent verification.
6. `Interpretation risks`: overclaims, missing limitations, alternative explanations, and places where conclusions exceed evidence.
7. `Unresolved technical issues`: claims or evidence gaps that must be resolved to establish rigor.
8. `Suggested additions`: concrete experiments, analyses, proofs, figures, tables, logs, scripts, or artifact changes that would improve technical quality.
