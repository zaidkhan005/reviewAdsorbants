# Project checkpoint — 2026-10-27

## Verified state

- Completed intake of the PDFs supplied through **Batch 20**; no further user-held PDF batch is assumed.
- **20** batch evidence notes are documented.
- **305** source-linked evidence records are in `data/corpus-evidence.csv`.
- **62** candidate/screening rows are in `data/corpus-screening-register.csv`.
- **60/62** records are marked full-text checked; two remain pending: `CORP-025` and `DISC-022`.
- **62** source-caveat entries are recorded.
- The evidence file contains entries for 59 distinct candidate IDs. Primary-study findings and review-derived secondary values are mixed in the evidence register but labelled by source type/role; they must not be pooled without screening.
- Q1 verification is not complete: 61 candidate records are marked pending and no verified Q1 record contains the required provider, year, category, quartile and source URL.
- The manuscript outline exists, but the substantive section drafts and integrated comparative evidence tables have not been verified as complete.

## Work consolidated in this checkpoint

Created missing session logs for Batches 13–20 to match the detailed extraction reports. Updated the 24-day plan to replace the outdated 31-record intake checkpoint with current counts and a realistic post-intake work sequence. The plan keeps manuscript sections pending unless a completed draft is actually present.

## Next sequence

1. Screen the two remaining full-text candidates: `CORP-025` and `DISC-022`.
2. Begin source-documented Q1 verification; keep provider, year, subject category, quartile and verification URL as separate fields.
3. Make retain/exclude/background-only decisions after considering relevance and evidence role.
4. Build comparative tables from checked primary studies, keeping observed uptake, fitted (q_{\max}\), removal, column metrics, regeneration and degradation distinct.
5. Draft and cite the manuscript sections from those comparisons.

Key files: [24-day plan](../docs/24_DAY_PLAN.md), [screening register](../data/corpus-screening-register.csv), [master evidence register](../data/corpus-evidence.csv), [source caveats](../data/source-caveats.csv).
