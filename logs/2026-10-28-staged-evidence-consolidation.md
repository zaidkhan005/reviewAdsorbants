# Staged evidence consolidation — 2026-10-28

## Result

All source-pinned evidence in `data/batch-extractions/` from the 11 dated/identified staging evidence files has been reconciled against the current master evidence database.

- Staging inputs: **11 evidence CSVs**.
- Staged evidence rows: **177**.
- Distinct DOIs: **32**.
- Staged rows with missing source pinpoints: **0**.
- Exact evidence tuples not represented in the master: **0**.
- Unknown candidate IDs referenced by master evidence: **0**.
- Master evidence count after reconciliation: **489**.
- Master screening register count after reconciliation: **100 candidates**.
- Candidate decision audit and adjudication rows: **100** each.
- Journal-level quartile audit rows: **41**. Ranking eligibility remains separate and pending where required.

## Merge decisions

- The staging CSVs were preserved unchanged as the branch-level audit trail.
- Batch-local IDs such as `PROPOSED-BATCH-01-PAPER-01` and `STAGE-BATCH-06-P1-E01` remain in the staging files only. The canonical evidence table uses stable master candidate IDs and unique master evidence IDs.
- All 177 staged evidence records match a master evidence row by DOI plus target, material, evidence domain, source page/table/figure, metric/value and reported result. This prevents double-counting identical rows while preserving multiple distinct observations from the same paper.
- Candidate IDs resolve to rows in the canonical screening register; no `PROPOSED-...` IDs remain in the master evidence table.
- The crosswalk at `data/batch-extractions/consolidation-crosswalk-2026-10-28.csv` links every staging evidence ID and local candidate ID to its master candidate ID, master evidence ID(s), source location and metric/value.

## Sources covered by the staging merge

| Staging set | Evidence rows | Papers / DOI identities |
|---|---:|---:|
| 2026-10-28 clay batch | 10 | 3 |
| Batch 01 | 15 | 3 |
| Batch 02 | 8 | 3 |
| Batch 03 | 15 | 2 |
| Batch 04 | 15 | 3 |
| Batch 05 | 15 | 3 |
| Batch 06 | 18 | 3 |
| CS 2006/2022/2025 set | 31 | 3 |
| Upload set A | 16 | 3 |
| Upload set B | 16 | 3 |
| JEnvMan upload set | 18 | 3 |
| **Total** | **177** | **32** |

## Scientific caveats

- The merge did not erase or harmonize conflicting values. Paper-specific caveats, unit conflicts, mass-balance issues, fitted-versus-observed metrics, mixed matrices, possible biodegradation, missing supplementary information, and source-equation problems remain in the master evidence caveat column.
- Reviews are retained as background / citation-chasing sources where appropriate; review-level values are not recast as original experimental data.
- No new source was automatically classified as Q1 based on journal reputation or current ranking alone. The 41-row journal audit includes pending status where the publication-year/provider/category rule has not been established.
- Better BibTeX citation keys are not created by this merge. They remain pending verification against a real current Zotero export.
- DISC-022 remains deferred until the user provides the full-text PDF; it has not been screened or excluded.

## Validation links

- `data/corpus-evidence.csv` — canonical 489-row evidence table.
- `data/corpus-screening-register.csv` — canonical 100-candidate register.
- `data/candidate-decision-audit.csv` and `data/screening-decision-adjudication-v1.csv` — decision and adjudication records.
- `data/journal-quartile-audit.csv` — 41 journal rows with pending checks preserved.
- `data/batch-extractions/consolidation-crosswalk-2026-10-28.csv` — row-level staging-to-master crosswalk.

## Important limitation

This consolidation verifies that the staging extractions have been propagated into the canonical tables. It does not mean all 100 candidates are accepted, all journal quartiles have been verified, or that either manuscript reference-count target (approximately 60 and 150 distinct works actually cited) is achieved. All new/staged papers must still undergo final scope adjudication, publication-year ranking checks where required, and Zotero/Better BibTeX citation conversion before the bibliography is final.