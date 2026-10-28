# Full-text extraction — Upload batches from 2026-10-28

## What was processed

Today’s uploaded PDFs were grouped into 11 staging sets under `data/batch-extractions/`. Source-pinpoint extraction records were created for each paper and then consolidated into the project’s master evidence database. The original staging CSVs are retained unchanged so that all batch-level IDs and review notes remain auditable.

- **32 paper records** were registered with central candidate IDs **DISC-037–DISC-068**.
- **177 source-linked evidence rows** were consolidated into `data/corpus-evidence.csv`.
- The master screening, candidate-decision audit, adjudication and journal-quartile tables were updated in parallel.
- The staging-to-master mapping is preserved in `data/batch-extractions/consolidation-crosswalk-2026-10-28.csv`.

## Batch mapping

| Staging set | Master candidate IDs | Evidence rows |
|---|---:|---:|
| Clay batch | DISC-037–DISC-039 | 10 |
| Batch 01 | DISC-040–DISC-042 | 15 |
| Batch 02 | DISC-043–DISC-045 | 8 |
| Batch 03 | DISC-046–DISC-047 | 15 |
| Batch 04 | DISC-048–DISC-050 | 15 |
| Batch 05 | DISC-051–DISC-053 | 15 |
| Batch 06 | DISC-054–DISC-056 | 18 |
| Chemosphere upload set | DISC-057–DISC-059 | 31 |
| Upload set A | DISC-060–DISC-062 | 16 |
| Upload set B | DISC-063–DISC-065 | 16 |
| JEnvMan upload set | DISC-066–DISC-068 | 18 |
| **Total** | **32 candidates** | **177** |

## Where the evidence lives

- **Structured record (for filtering, synthesis, and tables):** [`data/corpus-evidence.csv`](../data/corpus-evidence.csv)
- **Candidate metadata, provisional screening decisions and DOI mapping:** [`data/corpus-screening-register.csv`](../data/corpus-screening-register.csv)
- **Candidate audit / quantitative-use guardrails:** [`data/candidate-decision-audit.csv`](../data/candidate-decision-audit.csv)
- **Provisional scope and eligibility adjudication:** [`data/screening-decision-adjudication-v1.csv`](../data/screening-decision-adjudication-v1.csv)
- **Journal-ranking checks:** [`data/journal-quartile-audit.csv`](../data/journal-quartile-audit.csv)
- **Batch-level CSVs and full crosswalk:** [`data/batch-extractions/`](../data/batch-extractions/)

## Interpretation and safeguards

This is an **evidence extraction and consolidation record, not final inclusion approval**. Candidate records remain provisional. Journal Q1 eligibility is not inferred from journal prestige or a current quartile alone; it must match the requested ranking system, publication year and subject category.

Review articles are marked as background/citation-discovery sources and their reported tables are not treated as primary experimental measurements. Context-specific endpoints are kept separate: fitted isotherm (q_{max}), observed kinetic/equilibrium uptake, removal percentage, dose required for a target removal, column breakthrough/bed-volume results, and soil or other non-wastewater systems are not interchangeable. When a paper reports conflicting equations, conditions, captions, model fits or arithmetic, the source caveat is preserved rather than silently “corrected”. Missing supplementary information is not assumed available.

## Important correction to the repository layout

The evidence **was initially left only in the CSV staging directory**, which made it appear absent from the project’s main `evidence/` folder. This note fixes that discoverability gap. The evidence folder contains narrative, human-readable batch reports; `data/corpus-evidence.csv` remains the structured master database. Future PDF batches should update both: one narrative Markdown report under `evidence/` plus the corresponding source-pinned rows and crosswalk in `data/`.

## Status

- Structured rows merged: **177 / 177** (per the staged crosswalk).
- Candidate IDs assigned: **DISC-037–DISC-068**.
- Original staging records retained: **yes**.
- Final Q1 eligibility and manuscript inclusion decisions: **pending separate adjudication**.
