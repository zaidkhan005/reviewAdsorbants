# Semester manuscript inclusion-set and cross-file reconciliation (2026-10-31)

## Scope

Reconcile the current manuscript's cited sources to the semester candidate register, condition-labelled comparison matrix, evidence-readiness audit and Better BibTeX linkage ledger. This is a repository-structure and citation traceability audit; it does not independently re-read all 15 primary studies.

## Result

The manuscript's 19 cited references resolve by exact DOI as follows:

- **15 primary-study candidates** map to SEM-004, SEM-010, SEM-016, SEM-017, SEM-018, SEM-020, SEM-029, SEM-031, SEM-032, SEM-033, SEM-034, SEM-037, SEM-038, SEM-039 and SEM-040.
- **4 contextual references** remain outside the semester candidate register by design: Ahmed et al. (2015) and Jiao et al. (2025) are reviews; Wang et al. (2010) is a CIP–montmorillonite comparator; Gu et al. (2007) is a TC–humic-acid dissolved-organic-matter comparator.

Cross-file coverage after this pass:

| Register / file | Current records | Coverage of the 15 cited primary studies |
|---|---:|---:|
| Semester candidate register | 51 | 15/15 present |
| Condition-labelled comparison matrix | 28 | 15/15 present |
| Evidence-readiness audit | 47 | 15/15 present |
| BibTeX/citation linkage ledger | 51 | 15/15 current manuscript citekeys populated |
| Curated cited-reference bibliography | 19 | 15 primary + 4 contextual |

No cited primary study is missing from the candidate register, comparison matrix, readiness audit or citation-linkage ledger. The four contextual references are not expected to have SEM candidate IDs.

## Consolidation and corrections

1. **SEM-038 / Zhang & Wu (2022):** Added a semester readiness-audit cross-reference to existing master-corpus evidence EV-B10-004–EV-B10-009. No new source extraction or duplicate evidence row was created.
2. **SEM-038 comparison row:** Updated the observed TC-specific Table 1 value (q_e=90.21 mg/g), kinetic-fit outputs and Langmuir q_m as separate endpoints. Added the more severe Figure 2c feed-mass ceiling inconsistency. All numerical capacity endpoints remain excluded from condition-matched ranking pending source-basis clarification.
3. **Citation linkage ledger:** Populated the six missing current-manuscript key cells for SEM-016, SEM-020, SEM-032, SEM-038, SEM-039 and SEM-040 using their already verified Better BibTeX keys. This brings the ledger into alignment with the 15 primary-study citations actually used.
4. **Main-corpus crosswalk:** Replaced inherited quartile signals in all 51 semester crosswalk rows with an explicit statement that journal quartiles are not used for semester screening, ranking or inclusion. Updated stale references to a 15-entry cited bibliography to the actual 19-entry bibliography where applicable.
5. **Candidate register:** Removed the remaining SEM-038 SJR/Q2 note from its next-screening-action text.

## User-specified scope respected

Journal quartiles are out of scope for this semester paper. No quartile or journal ranking was used to select, prioritize, include, exclude or compare semester candidates. The separate broad-review corpus may retain its own source history, but that does not enter this semester-paper decision process.

## Outstanding source-quality limits

- Four contextual references support background or matrix chemistry only; they are not counted among the 15 empirical primary studies.
- The 15 primary-study set has heterogeneous source-access levels. In particular, SEM-020, SEM-033 and SEM-037 remain limited by abstract/preview-level access, and their claims remain qualified in the manuscript/evidence files.
- SEM-038 remains a serious source-basis/mass-balance hold; the cited value is documented but not promoted to a ranked capacity.
- SEM-029 cost estimate remains non-reproducible due the 100-fold dose mismatch.
- The manuscript's search-platform identification and source-by-source screening-flow counts remain unavailable; the paper is described as a narrative evidence synthesis, not a completed systematic review or PRISMA-compliant search.

## Files updated in this checkpoint

- `data/semester-evidence-readiness-audit.csv`
- `data/semester-condition-labelled-comparison.csv`
- `data/semester-bibtex-citation-linkage-audit.csv`
- `data/semester-main-corpus-crosswalk.csv`
- `data/semester-paper-candidate-register.csv`

## Verified counts

- 35 citation commands; 83 individual citekey mentions; 19 unique citekeys.
- 19 curated BibTeX entries; all 19 manuscript citekeys resolve; no unused bibliography entry.
- 15 cited primary studies map to 15 semester candidate IDs; 4 contextual sources remain external to that candidate register.
