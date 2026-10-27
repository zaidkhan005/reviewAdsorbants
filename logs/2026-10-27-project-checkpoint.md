# Project checkpoint — 2026-10-27

## Verified current state

- Completed intake of the PDFs supplied through **Batch 20**; no further user-held PDF batch is assumed.
- **20 batch evidence notes** are documented for the supplied PDFs; missing session logs for Batches 13–20 were added to the logs directory.
- **310 source-linked evidence records** are in `data/corpus-evidence.csv` (305 from batch intake plus five records from the subsequent full-text audit of CORP-025).
- **62 candidate/screening rows** are in `data/corpus-screening-register.csv`.
- **61 of 62** records are marked full-text checked. One remains pending: `DISC-022`, the 2022 *Journal of Hazardous Materials* critical review.
- **64 source-caveat entries** are recorded.
- The evidence file contains findings for distinct candidate IDs; it includes primary-study records and secondary review-derived evidence, so the record count is not a paper count or final bibliography count.
- **Quartile verification has started** for two journals. CORP-025/iScience has a 2024 SJR Q1 first-pass entry in Multidisciplinary, but direct SCImago profile confirmation remains pending because the canonical page was inaccessible in this session. DISC-022/Journal of Hazardous Materials has a 2024 Scopus/SJR Q1 source record in Environmental Engineering, Waste Management and Disposal, Pollution and Environmental Chemistry, citing a WUR Library display of Scopus metrics. The other candidates remain pending.
- The manuscript outline exists, but the substantive section drafts and integrated comparative evidence tables have not been verified as complete.

## Consolidation work completed

1. Added missing session logs for Batches 13–20 with links to the detailed extraction notes.
2. Updated `docs/24_DAY_PLAN.md` to replace the stale 31-record checkpoint with the verified Batch 20 state and the post-intake sequence.
3. Screened CORP-025 using the open-access PubMed Central full text and added five audit evidence records (EV-AUD-001–EV-AUD-005).
4. Recorded a high-priority mismatch in the montmorillonite study: the methods specify 0.03 g in 50 mL while the conclusion calls the optimum dosage 0.03 g/L; if the stated 120 mg/L initial concentration and 0.03 g/50 mL refer to the headline capacity/removal, the mass-balance ceiling is 200 mg/g, inconsistent with the 500–526 mg/g statements.
5. Checked the publisher preview/abstract and metadata for DISC-022, but did **not** mark the review full-text checked because the full text/tables were not accessible from the public pages inspected.
6. Recorded first-pass journal-quartile source fields for iScience and Journal of Hazardous Materials while keeping quartile verification separate from full-text screening.

## Current work sequence

1. Obtain legitimate access to the full text of DISC-022 and screen it; keep it FULLTEXT-NEEDED until then.
2. Continue quartile verification for the remaining candidate journals with ranking provider, year, category, quartile and source URL recorded.
3. Make final retain / exclude / background-only decisions after screening and ranking checks.
4. Build comparison tables from checked primary studies, keeping observed uptake, fitted (q_{\max}), removal percentage, column metrics, regeneration and degradation distinct.
5. Draft and cite manuscript sections from the checked comparisons.

## Key files

- [24-day plan](../docs/24_DAY_PLAN.md)
- [Screening register](../data/corpus-screening-register.csv)
- [Master evidence register](../data/corpus-evidence.csv)
- [Source-caveat register](../data/source-caveats.csv)
- [Screening and Q1 checkpoint](2026-10-27-screening-q1-start.md)
