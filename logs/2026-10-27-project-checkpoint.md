# Project checkpoint — 2026-10-27

## Verified current state

- Completed intake of the PDFs supplied through **Batch 20**; no further user-held PDF batch is assumed.
- **20 batch evidence notes** are documented for the supplied PDFs; missing session logs for Batches 13–20 were added to the logs directory.
- **310 source-linked evidence records** are in `data/corpus-evidence.csv` (305 from batch intake plus five records from the subsequent full-text audit of CORP-025).
- **62 candidate/screening rows** are in `data/corpus-screening-register.csv`.
- **61 of 62** candidates have completed full-text screening. `DISC-022`, the 2022 *Journal of Hazardous Materials* critical review, is **deferred until the user supplies the full-text PDF**; it is neither screened nor excluded and is temporarily outside the active queue.
- **64 source-caveat entries** are recorded.
- The evidence file contains findings for distinct candidate IDs; it includes primary-study records and secondary review-derived evidence, so the record count is not a paper count or final bibliography count.
- **First-pass journal-level quartile audit completed for all 34 unique journal titles.** `data/journal-quartile-audit.csv` is the dedicated one-row-per-journal record, and the current results are populated in `data/corpus-screening-register.csv`. Latest available 2025 SJR profile data were used where found; Arabian Journal of Chemistry uses historical 2024 SJR Q1 data with a Scopus-discontinuation caveat. Iraqi Journal of Agricultural Sciences is flagged as discontinued and has no current quartile assigned. Follow-up verification now confirms current 2025 SJR Q2 across six categories for Journal of Engineering and Q1 across three categories for Carbon Research; iScience Q1 is corroborated for 2025 and the 2024 SJR snapshot. Environmental Research remains provisional for the exact 2025 Environmental Science category. Arabian Journal of Chemistry and Iraqi Journal of Agricultural Sciences retain discontinued-status caveats. Most records rely on secondary profiles displaying SJR data, so institutional Q1-only decisions should be checked against the institution's required ranking source.
- The manuscript outline exists. A provisional candidate-role audit, source-linked primary-study comparison matrix v1, continuum synthesis v1 and Section 2.1 raw-biomass draft v1 now exist. Final include/exclude decisions, normalized same-target comparisons, author–date citation conversion and editorial completion remain.

## Consolidation work completed

1. Added missing session logs for Batches 13–20 with links to the detailed extraction notes.
2. Updated `docs/24_DAY_PLAN.md` to replace the stale 31-record checkpoint with the verified Batch 20 state and the post-intake sequence.
3. Screened CORP-025 using the open-access PubMed Central full text and added five audit evidence records (EV-AUD-001–EV-AUD-005).
4. Recorded a high-priority mismatch in the montmorillonite study: the methods specify 0.03 g in 50 mL while the conclusion calls the optimum dosage 0.03 g/L; if the stated 120 mg/L initial concentration and 0.03 g/50 mL refer to the headline capacity/removal, the mass-balance ceiling is 200 mg/g, inconsistent with the 500–526 mg/g statements.
5. Checked the publisher preview/abstract and metadata for DISC-022, but did **not** mark the review full-text checked because the full text/tables were not accessible from the public pages inspected.
6. Recorded first-pass journal-quartile source fields for iScience and Journal of Hazardous Materials while keeping quartile verification separate from full-text screening.
7. Audited latest available SJR metrics across all 34 unique journals and updated the dedicated audit. Follow-up checks then resolved the current-category questions for Journal of Engineering and Carbon Research, corroborated iScience, and recorded the remaining Environmental Research/discontinuation caveats.
8. Created `data/candidate-decision-audit.csv`, assigning a provisional working role and quantitative-use guardrail to each of 62 candidates (not final inclusion/exclusion decisions).
9. Audited the comparison-matrix crosswalk: 208 rows reference 248 unique evidence IDs, with no duplicate or orphan IDs; 62 other evidence IDs are background/review or adjacent-technology evidence outside the core matrix.
10. Created `logs/2026-10-27-comparison-readiness-audit-01.md` with condition-matched within-study comparison candidates, separate endpoint rules and a quarantine list for capacity/model contradictions.
9. Created `data/primary-study-comparison-matrix.csv`, with 208 target/material/stage groupings from source-linked evidence for 43 primary-study candidates. The matrix separates observed outcomes, model-derived capacities, kinetics, matrices, regeneration, continuous-flow, cost/LCA and mechanisms while retaining evidence IDs and source locations.
10. Validated CSV structure and counts: 62 candidate rows with consistent fields, 34 journal audit entries, 310 evidence records with no duplicate evidence IDs, and 64 source caveats. DISC-022 remains deferred and un-screened.
11. Drafted `manuscript/CONTINUUM_SYNTHESIS_V1.md` across the eight working material classes, with source-linked examples, quality caveats and a minimum normalization schema. Checked all 29 internal candidate DOI links against the screening register; no mismatches remain.
12. Drafted `manuscript/SECTION_2_1_RAW_BIOMASS_V1.md` for seven candidate studies (CORP-004, -005, -006, -010, -016, -017 and -019), including a small source-linked comparison table and explicit capacity/mass-balance caveats. Validated 16 in-text DOI links against the register; no mismatches remain.

## Current work sequence

1. Keep `DISC-022` deferred until the user supplies its full-text PDF; do not treat it as screened or excluded.
2. Resolve ranking exceptions against the institution's preferred source if strict Q1 eligibility is required; do not conflate 2025 SJR profile data with publication-year quartiles or JCR results.
3. Review the provisional candidate-role audit and make final retain / exclude / background-only decisions.
4. Build the first condition-matched comparison tables from the Tier A candidates in `logs/2026-10-27-comparison-readiness-audit-01.md`; keep observed uptake, fitted qmax, removal percentage, Kp, column metrics, regeneration and degradation distinct.
5. Draft and cite material-class sections from the checked comparisons.

## Key files

- [24-day plan](../docs/24_DAY_PLAN.md)
- [Screening register](../data/corpus-screening-register.csv)
- [Master evidence register](../data/corpus-evidence.csv)
- [Source-caveat register](../data/source-caveats.csv)
- [Journal-quartile audit](../data/journal-quartile-audit.csv)
- [Candidate decision audit](../data/candidate-decision-audit.csv)
- [Primary-study comparison matrix](../data/primary-study-comparison-matrix.csv)
- [Quantitative-comparison readiness audit](2026-10-27-comparison-readiness-audit-01.md)
- [Continuum synthesis draft v1](../manuscript/CONTINUUM_SYNTHESIS_V1.md)
- [Section 2.1 raw-biomass draft v1](../manuscript/SECTION_2_1_RAW_BIOMASS_V1.md)
- [Section 2.1 draft log](2026-10-27-section-2-1-batch-01.md)
- [Quartile audit batch log](2026-10-27-q1-audit-batch-01.md)
- [Continuum synthesis log](2026-10-27-continuum-synthesis-batch-01.md)
- [Screening and synthesis setup log](2026-10-27-screening-synthesis-batch-01.md)
- [Screening and Q1 checkpoint](2026-10-27-screening-q1-start.md)
