# Project checkpoint — 2026-10-27

## Verified current state

- Completed intake of the PDFs supplied through **Batch 20**; no further user-held PDF batch is assumed.
- **20 batch evidence notes** are documented for the supplied PDFs; missing session logs for Batches 13–20 were added to the logs directory.
- **312 source-linked evidence records** are in `data/corpus-evidence.csv` (305 from batch intake, five CORP-025 full-text audit records, one published-abstract check for CORP-023, and one subsequent source/caption audit record).
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
9. Audited the comparison-matrix crosswalk: 208 rows reference 249 unique evidence IDs, with no duplicate or orphan IDs; 62 other evidence IDs are background/review or adjacent-technology evidence outside the core matrix.
10. Created `logs/2026-10-27-comparison-readiness-audit-01.md` with condition-matched within-study comparison candidates, separate endpoint rules and a quarantine list for capacity/model contradictions.
11. Created `manuscript/COMPARATIVE_TABLES_V1.md` with five endpoint-separated comparison panels and source/evidence IDs. These remain working tables pending source-PDF recheck, citation formatting and final quartile/inclusion decisions.
12. Created and validated `data/screening-decision-adjudication-v1.csv`: 62 unique candidate IDs, 18 columns, no blanks. It separates provisional scope decisions from ranking eligibility and preserves `DISC-022` as deferred/not screened/not excluded.
13. Cross-checked CORP-023's published journal abstract: its headline pH-4 capacities match the uploaded preprint (alginate 74.2±0.3 mg/g; chitosan 80.4±0.2 mg/g), while detailed published methods/tables remain unverified. Added `EV-AUD-006` and a dedicated source log.
9. Created `data/primary-study-comparison-matrix.csv`, with 208 target/material/stage groupings from source-linked evidence for 43 primary-study candidates. The matrix separates observed outcomes, model-derived capacities, kinetics, matrices, regeneration, continuous-flow, cost/LCA and mechanisms while retaining evidence IDs and source locations.
10. Validated CSV structure and counts: 62 candidate rows with consistent fields, 34 journal audit entries, 312 evidence records with no duplicate evidence IDs, and 64 source caveats. DISC-022 remains deferred and un-screened.
11. Drafted `manuscript/CONTINUUM_SYNTHESIS_V1.md` across the eight working material classes, with source-linked examples, quality caveats and a minimum normalization schema. Checked all 29 internal candidate DOI links against the screening register; no mismatches remain.
12. Drafted `manuscript/SECTION_2_1_RAW_BIOMASS_V1.md` for seven candidate studies (CORP-004, -005, -006, -010, -016, -017 and -019), including a small source-linked comparison table and explicit capacity/mass-balance caveats. Validated 16 in-text DOI links against the register; no mismatches remain.

## Current work sequence

1. Keep `DISC-022` deferred until the user supplies its full-text PDF; do not treat it as screened or excluded.
2. Resolve ranking exceptions against the institution's preferred source if strict Q1 eligibility is required; do not conflate 2025 SJR profile data with publication-year quartiles or JCR results.
3. Review `data/screening-decision-adjudication-v1.csv` and the candidate-role audit to make final retain / exclude / background-only decisions, with source/endpoint checks and the required ranking system/year/category kept explicit.
4. Recheck `manuscript/COMPARATIVE_TABLES_V1.md` against the source PDFs/supplements, apply the agreed ranking-year/category rule, and expand the tables only with validated like-for-like data; keep observed uptake, fitted qmax, removal percentage, Kp, column metrics, regeneration and degradation distinct.
5. Section 2.2 natural-clays/biopolymers v1 is now available at `manuscript/SECTION_2_2_CLAYS_BIOPOLYMERS_V1.md`; continue with Section 2.3 (biochar/modified biochar) using the checked evidence and comparison matrix. Treat all drafts as provisional until source checks, Zotero citation insertion and editorial revision are complete.

## Key files

- [24-day plan](../docs/24_DAY_PLAN.md)
- [Screening register](../data/corpus-screening-register.csv)
- [Master evidence register](../data/corpus-evidence.csv)
- [Source-caveat register](../data/source-caveats.csv)
- [Journal-quartile audit](../data/journal-quartile-audit.csv)
- [Candidate decision audit](../data/candidate-decision-audit.csv)
- [Scope/ranking adjudication v1](../data/screening-decision-adjudication-v1.csv)
- [CORP-023 published abstract check](2026-10-27-corp-023-published-abstract-check.md)
- [Primary-study comparison matrix](../data/primary-study-comparison-matrix.csv)
- [Quantitative-comparison readiness audit](2026-10-27-comparison-readiness-audit-01.md)
- [Comparative evidence tables v1](../manuscript/COMPARATIVE_TABLES_V1.md)
- [Continuum synthesis draft v1](../manuscript/CONTINUUM_SYNTHESIS_V1.md)
- [Section 2.1 raw-biomass draft v1](../manuscript/SECTION_2_1_RAW_BIOMASS_V1.md)
- [Section 2.2 natural clays and biopolymers draft v1](../manuscript/SECTION_2_2_CLAYS_BIOPOLYMERS_V1.md)
- [Section 2.2 draft log](2026-10-27-section-2-2-batch-01.md)
- [Section 2.1 draft log](2026-10-27-section-2-1-batch-01.md)
- [Quartile audit batch log](2026-10-27-q1-audit-batch-01.md)
- [Continuum synthesis log](2026-10-27-continuum-synthesis-batch-01.md)
- [Screening and synthesis setup log](2026-10-27-screening-synthesis-batch-01.md)
- [Screening and Q1 checkpoint](2026-10-27-screening-q1-start.md)

## Post-checkpoint update — targeted literature discovery pass 01 (2026-10-27)

The first gap-led discovery pass is now logged at `logs/2026-10-27-targeted-discovery-pass-01.md`. Six new primary-study candidate leads (DISC-031–DISC-036) were identified after title/DOI comparison with the prior 62-row register. The canonical register, candidate-decision audit and provisional adjudication file now contain **68 rows**; the evidence register was not changed because the six new candidates have not yet had page/table/figure-level evidence extracted. The journal quartile audit now has **38 rows**; four new journal titles are explicitly marked not yet audited. The reference-acquisition tracker now contains 21 discovery/query records; per-query hit counts were not exposed by the search interface, so no returned-hit count was invented.

New candidates cover (i) amoxicillin adsorption on chitosan beads, (ii) alginate/carboxymethyl-chitosan hydrogel beads for single/binary feeds, (iii) self-templated biochar from anaerobic-digestion residue, (iv) sawdust vs sawdust/plastic co-pyrolysis biochar, (v) KOH-activated biochar from antibiotic fermentation residue, and (vi) a 2026 garden-waste biochar study. These remain provisional. In the open-access fermentation-residue article DISC-035, printed qe/removal equations appear to use a reversed concentration-difference sign; this must be checked before quantitative use.

Current acquisition state: 68 candidates; 61 previously completed full-text screens plus six new leads awaiting source review, with DISC-022 separately deferred. The rough 220–250 candidate-pool plan therefore now implies around **152–182 additional candidate leads** to discover before deduplication/screening; this is a planning estimate, not a bibliography count. The final cited-reference count remains unaudited. See `docs/REFERENCE_TARGET_PLAN.md`, `data/reference-acquisition-tracker.csv`, and the discovery-pass log.