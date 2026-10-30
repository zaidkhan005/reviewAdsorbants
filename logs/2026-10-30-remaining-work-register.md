# Semester-paper remaining-work register — 30 October 2026

Project source of truth: `zaidkhan005/reviewAdsorbants`.

## Purpose and counting rules

This register reconciles the existing candidate register, semester evidence extraction, evidence-readiness audit, inclusion shortlist, condition-labelled comparison, claim-evidence audit and citation-linkage audit. It is a continuation checkpoint, not a new literature search and not a restart.

The machine-readable, candidate-by-candidate file is:
- `data/semester-remaining-work-register.csv`

Do not count evidence rows, candidate IDs, distinct studies, comparison rows and manuscript claims as interchangeable units.

## Snapshot

| Item | Current count | Meaning |
|---|---:|---|
| Candidate records | 44 | IDs SEM-001 through SEM-044 |
| Distinct study candidates | 43 | One record, SEM-041, is a duplicate alias of SEM-026 |
| Dedicated semester evidence-extraction rows | 39 | One row each for the current 39 extracted candidate IDs |
| Evidence-readiness rows | 39 | Matched to the 39 extraction rows |
| Candidates without a dedicated semester extraction row | 5 | See breakdown below; several deliberately do not need a new row |
| Condition-labelled comparison rows | 24 | Condition/metric comparison entries, not all 44 candidates |
| Results/discussion claim-evidence audits | 22 | RD-001 through RD-022; these are claims, not 22 unique papers |
| Existing Results & Discussion draft | V1, sections 3.1–3.6 | Evidence-led working draft; explicitly not submission-ready |
| Citations in that draft | 15 | Their citation keys were reconciled against the user-supplied 173-entry export in the existing citation checkpoint |

The 38 evidence rows do not mean 38 fully verified empirical papers. They include different source access levels, provisional empirical entries, condition-specific caveats and the theory-only SEM-013 record.

## The five candidates without a dedicated semester extraction row

| Candidate | Current decision | Further work |
|---|---|---|
| SEM-022 | Review article; background/context only | No empirical extraction row required. Use only to trace original primary papers; do not count it as a primary study. |
| SEM-035 | Needs clarification | Resolve tetracycline species, bibliographic identity and primary experimental method before deciding inclusion. |
| SEM-036 | Material identity unresolved | Check characterization to decide whether “graphene-oxide-like carbon nanosheets” meet the review's defined graphene-based scope. Waste origin alone is not sufficient. |
| SEM-038 | Reuses existing broad-corpus evidence | Link EV-B10-004–EV-B10-009 via `data/semester-main-corpus-crosswalk.csv`; do not create duplicate semester evidence rows. Preserve the dose/concentration mass-balance warning. |
| SEM-041 | Duplicate alias of SEM-026 | No further study extraction. Keep alias for traceability only; cite/count the canonical study once. |

Therefore there are **two genuinely open candidate identity/scope items** (SEM-035 and SEM-036). SEM-023's identity and proceedings publication type are resolved; its full-text evidence is extracted and its numerical claims are held under explicit source-quality caveats. SEM-021's identity is resolved and it now has an abstract-level evidence row; its remaining full-text parameter validation is tracked as source-strengthening work, not metadata resolution.

Namespace warning: **SEM-035** is a candidate ID for the “Adsorption Characteristics of Modified Graphene Oxide on Tetracycline Antibiotics in Water” lead. **EV-SEM-035** is an evidence ID attached to candidate **SEM-013**, the 2024 theoretical DFT paper. These identifiers refer to different records.

## Existing evidence needing attention

- **39/44 candidates** already have dedicated semester extraction and readiness rows.
- **17 evidence records** are still at publisher-abstract, indexed-snippet or preview access level. One of these is SEM-013, which is theory-only; the other 16 are provisional empirical candidates, including SEM-021 (EV-SEM-038). The candidate-level CSV specifies which records need source strengthening and which metrics must remain held.
- Other extracted candidates have primary full text or accepted-manuscript text, but still carry targeted caveats: missing conditions, uncertain figure readings, fitted-vs-observed metric separation, source-internal discrepancies, impossible column mass, or absent supplementary tables. Do not reopen completed extraction wholesale; follow the row-specific next action.
- The condition-labelled comparison has **24 entries**. Expand it only where the source provides enough conditions and metric identity. Do not force every candidate into it, and do not make an unqualified capacity leaderboard.
- The claim-evidence audit has **22 claims**. It must be reconciled against the final text after synthesis; do not treat the count as 22 studies.

## Journal quartile / ranking work

Current candidate-register status:
- 42 candidate records explicitly say quartile not checked for this semester screen.
- SEM-021 and SEM-023 have verified identity; both still lack a semester-specific journal-quartile audit.
- SEM-038 has an existing main-corpus signal of Q2 across five 2025 SJR categories, but publication-year/category and JCR eligibility have not been re-audited for this semester paper.
- SEM-041 is a duplicate alias; ranking should be assigned once to canonical SEM-026.

That means journal-rank verification remains open for **42 candidate records or canonical study decisions**, while SEM-038 has a provisional existing signal and SEM-041 inherits the canonical record. A quartile audit must record database (e.g. SJR or JCR), journal, category, quartile, ranking year and verification date. Do not use a generic current Q1/Q2 label without its category and year. Whether Q1 is a hard inclusion rule must be taken from the actual semester-paper requirements, not assumed from earlier category-specific literature searches.

## Citation and manuscript status

The existing 15 in-text citation keys in the current Results & Discussion V1 were reconciled to the supplied 173-entry Better BibTeX export in the earlier citation checkpoint. This does **not** mean all 44 candidate records need a key now. Candidate-level citation readiness remains mixed; only obtain/repair keys for studies actually selected for the manuscript, using Zotero/Better BibTeX and exact DOI matching. Never invent a key.

The inspected manuscript artifact is `manuscript/SEMESTER_RESULTS_AND_DISCUSSION_V1.md`, covering sections 3.1–3.6. It is an evidence-led working draft, not a submission-ready full manuscript. Final work includes any missing manuscript sections required by the agreed outline, integrating selected studies, revising the synthesis and claim audit, reconciling bibliography keys, applying the required citation style, and final consistency/format checks. This status note does not assume the state of other manuscript files that were not audited here.

## Recommended remaining sequence

1. **Close the four candidate decisions:** SEM-021 (metadata/identity), SEM-036 (material classification), SEM-035 (target/species and paper identity), and SEM-023 (publication type and primary-data eligibility). Do not create evidence rows unless a distinct eligible primary study is verified.
2. **Strengthen source-level evidence:** work through the 15 provisional empirical abstract/indexed/preview candidates where full primary text can be accessed. Keep SEM-013 in a theory-only lane.
3. **Complete the journal-ranking audit:** verify journal, category, year and database for candidates being considered for inclusion; only apply a Q1 cutoff if it is a confirmed requirement.
4. **Harmonize comparison data:** expand the 23-row condition-labelled table only with condition-complete, metric-defined evidence; preserve separate observed (q_e), fitted kinetic (q_e), fitted (q_{max}/q_m), removal and column metrics.
5. **Finalize manuscript synthesis:** integrate the strongest, scope-eligible studies into Results & Discussion, audit every numerical/interpretive claim against its source, and preserve known inconsistencies.
6. **Close citation and submission QA:** reconcile keys only for selected cited studies, validate every in-text citation against the final bibliography, and apply the required institutional/journal style.

## What is not needed now

- Do not repeat the earlier evidence extraction batches.
- Do not ask the user for another PDF batch by default; prior instructions said no additional batch was assumed waiting.
- Do not re-extract SEM-038 into a duplicate evidence row.
- Do not count SEM-022 as an empirical paper or SEM-041 as a second distinct study.
- Do not rank theory-only SEM-013 as an adsorption-performance experiment.
- Do not silently resolve source inconsistencies or invent missing concentrations, doses, energies, cost values, journal quartiles or citation keys.

## State of this checkpoint

This file and `data/semester-remaining-work-register.csv` are planning/reconciliation artifacts. They do not mark the remaining scientific and ranking work as complete.
