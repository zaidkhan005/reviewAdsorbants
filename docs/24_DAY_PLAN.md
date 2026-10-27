# 24-day review-paper sprint

The original sprint rule remains: every workday ends with a visible deliverable; do not polish sentences while a section is incomplete. This plan tracks completed artifacts—not work that merely appears in a conversation.

## Current restart checkpoint (2026-10-27)

The intake stage has advanced substantially beyond the earlier 2026-10-24 checkpoint.

- **20 documented PDF-processing batches**, with detailed extraction notes through Batch 20.
- **310 source-linked evidence records** in `data/corpus-evidence.csv`. These are findings, not distinct papers.
- **62 candidate/screening records** in `data/corpus-screening-register.csv`.
- **61 of 62** candidates have completed full-text screening; `DISC-022` is **deferred** until the user supplies its full-text PDF. It is not screened or excluded and is temporarily outside the active queue. `CORP-025` was screened using its open-access PubMed Central full text; a dose/capacity inconsistency is recorded.
- **64 source-caveat entries** in `data/source-caveats.csv`.
- The evidence CSV contains records for **59 distinct candidate IDs**; evidence records include primary studies and reviews, so this does not equal the final bibliography.
- The downloaded-PDF intake is complete for the files supplied through Batch 20. Do not assume additional user-held PDFs remain to be uploaded.
- **Journal-quartile audit now covers all 34 unique journals** in `data/journal-quartile-audit.csv`, with results copied to the 62-row screening register. Latest available 2025 SCImago/SJR profiles were used where found; Arabian Journal of Chemistry has a historical 2024 Q1 entry but Scopus coverage was discontinued, and Iraqi Journal of Agricultural Sciences is flagged as discontinued with no current quartile assigned. Category-level confirmation remains limited for Environmental Research, Journal of Engineering and Carbon Research. Secondary profile displays were used rather than direct canonical SCImago verification for every title.
- A **provisional candidate-role audit** now covers all 62 rows in `data/candidate-decision-audit.csv`; it separates primary-study candidates, background-only reviews, adjacent technology, deferred and out-of-scope records. **Final retain/exclude decisions, normalized cross-paper comparisons and substantive manuscript section drafts remain incomplete.** The new comparison matrix is a structured extraction workspace, not a completed review manuscript.

Current repository references:
- [Working manuscript outline](../manuscript/REVIEW_OUTLINE.md)
- [Master evidence register](../data/corpus-evidence.csv)
- [Screening register](../data/corpus-screening-register.csv)
- [Source-caveat register](../data/source-caveats.csv)
- [Candidate decision audit](../data/candidate-decision-audit.csv)
- [Primary-study comparison matrix (v1)](../data/primary-study-comparison-matrix.csv)
- [Journal-quartile audit](../data/journal-quartile-audit.csv)
- [Research workflow](RESEARCH_WORKFLOW.md)
- [Current project checkpoint log](../logs/2026-10-27-project-checkpoint.md)

## Sprint status table

| Day | Planned work | End-of-day deliverable | Status in this workspace |
|---|---|---|---|
| 1 | Full-corpus intake, reference deduplication, and evidence system | Unified screening register plus a source-linked evidence record | **Substantially complete for supplied corpus:** 62 candidates, 20 batch reports, 310 evidence records. `DISC-022` remains deferred until the user supplies its PDF; journal quartiles have been first-pass audited for all 34 unique journal titles, with exceptions logged. |
| 2 | Section 2.1 raw biomass literature | Evidence-screened subsection draft | Not complete; no verified finished section draft recorded. |
| 3 | Finish Section 2.1 | Complete rough draft of 2.1 | Not complete/verified. |
| 4 | Section 2.2: natural clays & biopolymers | 8–15 screened papers, evidence notes and rough draft | Taxonomy and evidence exist; final screening/Q1 check and full draft remain. |
| 5 | Finish/complete Section 2.2 biopolymer evidence | Complete rough draft of 2.2 | Not complete/verified. |
| 6 | Biochar and modified biochar | Evidence set and rough draft of 2.3 | Evidence set is growing; Q1 screen and draft remain. |
| 7 | Synthesize processing and modification comparisons | Comparative table and draft synthesis | **Version 1 evidence matrix created:** 208 target/material/stage group rows drawn from 43 primary-study candidates. Normalization, same-target comparisons and synthesis narrative remain pending. |
| 8 | Engineered/nano-carbon adsorbents | Evidence set and rough draft of 2.4 | Evidence set is growing; final Q1 shortlist and draft remain. |
| 9 | Complete Section 2 and compare material classes | Integrated classification/synthesis | Pending. |
| 10 | Processing–cost–performance continuum | Core framework figure/table and narrative | Pending. |
| 11 | Kinetics | Kinetic-model analysis | Individual records extracted; integrated cross-paper analysis pending. |
| 12 | Isotherms | Isotherm analysis | Individual records extracted; integrated cross-paper analysis pending. |
| 13 | pH, speciation and mechanisms | Mechanism/speciation synthesis | Individual records extracted; evidence-weighted synthesis pending. |
| 14 | Techno-economics and energy | Cost/energy comparison | Data are uneven; comparative synthesis pending. |
| 15 | Regeneration and spent adsorbent | Regeneration/end-of-life synthesis | Individual caveats recorded; integrated synthesis pending. |
| 16 | Real-water matrix effects | Matrix-effects synthesis | Individual records extracted; integrated synthesis pending. |
| 17 | Practical applications, batch/fixed-bed/MBR/polishing | Application section | Column and adjacent-technology evidence exists; section draft pending. |
| 18 | Challenges | Evidence-backed challenges | Some gaps are documented; final synthesis pending. |
| 19 | Future perspectives | Prioritized future directions | Pending. |
| 20 | Introduction and conclusions | Rough drafts | Pending. |
| 21 | Figures and tables | Complete visual set | Pending; no final integrated figure/table set verified. |
| 22 | Citation audit | Verified reference list and in-text links | Pending; Q1 and citation-to-primary-source checks remain. |
| 23 | Scientific editing | Revised complete manuscript | Pending. |
| 24 | Final quality assurance | Submission-ready manuscript package | Pending. |

## Next execution sequence after intake

Do not continue routine batch intake unless a specific evidence gap requires a targeted source. The next workstream is:

1. Keep `DISC-022` **deferred** until the user supplies its PDF; do not count it as screened or excluded.
2. Resolve the journal-quartile exceptions listed in `data/journal-quartile-audit.csv` if a strict Q1-only rule will determine final eligibility; use the institution's required ranking source and keep SJR/JCR and publication-year distinctions explicit.
3. Review `data/candidate-decision-audit.csv` and convert provisional working roles into final retain / exclude / background-only decisions; it is a triage aid, not a final screening decision.
4. Audit `data/primary-study-comparison-matrix.csv` for condition/unit consistency and identify defensible same-target/same-metric comparisons before treating values as comparative rankings.
5. Draft material-class sections from those checked comparisons; use `manuscript/CONTINUUM_SYNTHESIS_V1.md` as a structural working draft, not as a final section.

This is a planning record, not a claim that prior deliverables are fully finished. Mark a section complete only when the actual draft/artifact has been checked.
