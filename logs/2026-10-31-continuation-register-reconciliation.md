# Continuation register reconciliation — 31 October 2026

## Source-of-truth checkpoint

Repository: `zaidkhan005/reviewAdsorbants`  
Branch: `main`  
Baseline commit inspected: `17473b8ac31cb268b388f4a219e9442373f06071`  
This is a continuation and consistency repair, not a new literature search or a restart.

## Reconciled counts

| Dataset | Verified count | Counting rule |
|---|---:|---|
| Semester candidate register | 51 rows | Includes SEM-041 as a historical duplicate alias |
| Distinct DOI-defined candidate works | 50 | SEM-041 aliases SEM-026 and is counted once |
| Dedicated semester evidence | 46 rows | Evidence records, not necessarily accepted/cited papers |
| Condition-labelled comparison | 28 rows | Condition/metric entries; not one row per candidate |
| Manuscript claim-evidence audit | 19 rows | Claim-level audit records |
| Distinct works currently cited | 19 | 15 target-material primary-study works plus four contextual sources |
| Zotero DOI intake queue | 21 unique DOI entries | Metadata intake only; not counted as cited works |

## Consistency issue repaired

Before this update, `data/semester-remaining-work-register.csv` contained 44 candidate rows (SEM-001–SEM-044), while the current candidate register and README already contained SEM-045–SEM-051. The remaining-work register has now been extended with seven candidate-specific rows, bringing it to 51 rows. Existing SEM-001–SEM-044 entries were retained without rewriting.

The new rows were populated by cross-referencing the current candidate register, evidence-readiness audit, study-inclusion shortlist, citation-linkage audit and condition-labelled comparison. They preserve the source-access level, study disposition, comparison membership, citation readiness, priority and next QA action.

## Important status distinctions

- SEM-045, SEM-046, SEM-049, SEM-050 and SEM-051 have primary full-text or indexed full-article evidence, but each retains explicit metric, condition or cost caveats.
- SEM-047 and SEM-048 remain abstract/preview-level; neither is promoted to a condition-matched capacity comparison.
- Of SEM-045–SEM-051, only SEM-051 currently has an entry in the 28-row condition-labelled comparison. This is a table-membership fact, not an exclusion decision for the other six.
- None of SEM-045–SEM-051 has a verified Better BibTeX key in the five mounted exports checked on 31 October. Their DOI rows remain not citation-ready until Zotero is searched and a fresh Better BibTeX export supplies actual keys.
- No manuscript text, existing 19 verified citation keys, or cited-reference bibliography records were changed in this repair.

## Next work

1. Add condition-labelled comparison rows only where a candidate's reported condition and metric identity can be stated without mixing observed uptake, fitted kinetic qe, fitted qmax, removal percentage or column metrics.
2. Strengthen SEM-047 and SEM-048 only if complete primary full text becomes accessible; keep their abstract/preview evidence tier visible otherwise.
3. Continue journal-ranking verification with provider, ranking year and subject category recorded separately. Do not assume a Q1-only semester rule.
4. Complete the 21-DOI Zotero metadata reconciliation after searching the user's existing library to avoid duplicates; export fresh Better BibTeX and update keys by exact DOI before adding citations.
5. Re-run the manuscript claim-to-source audit after selective citation expansion. The 19 currently verified cited works remain unchanged.

## Files updated

- `data/semester-remaining-work-register.csv` — extended from 44 to 51 candidate rows.
- `README.md` — repository continuation date and register navigation updated.

No new papers were requested or downloaded in this checkpoint.
