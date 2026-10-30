# 2026-10-31 manuscript and status reconciliation

## Scope of this checkpoint

This checkpoint continues the existing semester-paper workstream. It does not restart literature screening, change the approved material/antibiotic scope, create new citation keys, or reopen journal-quartile work. GitHub remains the project source of truth and Zotero remains the citation-key source.

## Status inconsistencies corrected

- `README.md`: updated the shared journal metadata inventory from 41 to 45 records; clarified that it is broader-review metadata only and not a semester-paper screening input. Updated the semester condition-labelled comparison count from 27 to 28 rows. Corrected the SEM-051 note so it no longer claims that no extraction occurred.
- `manuscript/SEMESTER_MANUSCRIPT_WORKING_V1.md`: updated the semester candidate-register snapshot from 50 rows / 49 DOI-defined works to 51 rows / 50 DOI-defined works, excluding the SEM-041 alias of SEM-026. Updated the DOI intake audit to 21 unique DOIs checked against all five mounted Better BibTeX exports on 31 October 2026, with no exact matches. Clarified that unexported Zotero collections still require an in-library DOI lookup. Removed the obsolete "complete journal-quartile audit pending" task and stated that quartile auditing is out of scope.
- `references/semester-zotero-doi-import-queue-2026-10-30.txt`: corrected the header to match the live 21-entry queue and the completed five-export DOI check; removed the stale note that SEM-048/049/050 had not yet been checked.

## SEM-035 source-access check

Candidate SEM-035, DOI `10.16796/j.cnki.1000-3770.2025.09.007`, was rechecked against the official publisher record and the Library. The publisher page confirms the primary study identity and abstract: GO–chitosan film (GOCSF) and particles (GOCSP), separate TC and CTC tests, optimum pH 5, and abstract-reported Langmuir capacities of 3.69 mg/g (GOCSP/TC) and 3.50 mg/g (GOCSF/TC). These are model-fitted capacity claims, not observed equilibrium uptake.

The full methods and numerical tables were not available from the publisher page or the relevant Library search results during this checkpoint. No new PDF was requested or assumed. No dedicated evidence row was created; SEM-035 remains a P2 source-strengthening item pending institutional/CNKI full-text access. Do not use the abstract capacities in condition-matched rankings.

Official publisher record: https://www.scljs1975.com/EN/10.16796/j.cnki.1000-3770.2025.09.007

## Validation snapshot

- Semester candidate register: 51 rows (50 DOI-defined works after the known alias).
- Semester remaining-work register: 51 rows.
- Condition-labelled comparison: 28 rows.
- Shared journal metadata inventory: 45 rows; not used for semester screening.
- Zotero DOI intake queue: 21 unique DOIs; exact-match check across the five mounted exports found no matches. This does not establish absence from Zotero collections not represented by those exports.
- Existing 19 cited works and the evidence/comparison records were not changed by this status-only checkpoint.
- No new PDF, evidence row, candidate row, manuscript citation or Better BibTeX key was added.

## Next action

Continue with candidate-specific scientific/source QA that can be performed from existing primary or indexed sources. SEM-035 can be advanced only when its full text/tables are accessible; otherwise retain its current caveat and do not repeat unsuccessful retrieval attempts.


## Additional citation-linkage register reconciliation (31 October 2026)

After reconciling the manuscript and DOI queue, the expanded 21-DOI check was propagated to:

- `docs/SEMESTER_CITATION_LINKAGE_AUDIT.md`
- `data/semester-bibtex-citation-linkage-audit.csv`
- `data/semester-main-corpus-crosswalk.csv`
- `data/semester-remaining-work-register.csv`
- The README citation-readiness summary

Validation found all 21 queued candidate IDs in each of the three CSV registers, with no incorrect row widths and the same 31 October check date. All 21 remain without a verified key in the five mounted exports. The 19 already-cited manuscript works and their citation keys remain unchanged; Zotero in-library searches are still required because unexported collections may contain existing records.


## Latest complete Zotero export comparison (31 October 2026)

The user uploaded `full ++ check again(1).bib` as the latest complete My Library export. SHA-256 of the supplied file: `bc65b1a50bfda09824e8ae8ebbdb4c64270b16108d7ad79abd7675358749ac20`.

### Export integrity summary

- 173 BibTeX entries and 173 unique citation keys.
- 170 DOI fields and 168 unique DOI values.
- Two duplicate DOI groups were detected and left untouched:
  - `10.1016/j.envres.2021.111091`: `ashiqCarbonbasedAdsorbentsFluoroquinolone2021a` and `ashiqCarbonbasedAdsorbentsFluoroquinolone2021b`.
  - `10.1016/j.ijbiomac.2024.133382`: `rostamiSurfaceModifiedChitosan2024a` and `rostamiSurfaceModifiedChitosan2024b`.

### Semester citation matching

- All 21 DOI-queue records were tested against the file by exact DOI and normalized title.
- Result: **0/21 matched** by DOI; **0/21 matched** by normalized title.
- All 19 existing citation keys in `references/semester-manuscript-cited-references.bib` were found in the uploaded export.
- A high lexical-similarity result for SEM-019 was checked: the export item is a distinct 2025 CMC-functionalized magnetic GO/TC paper (DOI 10.1039/d5ra06621b), not the 2026 EDTA-functionalized candidate (DOI 10.1016/j.dwt.2026.101889). No crosswalk was created.
- No citation key was assigned or guessed for any queued candidate. No manuscript citations were added or altered.
- The candidate-level citation linkage CSV, main-corpus crosswalk, remaining-work register, DOI queue, citation audit document, manuscript citation-readiness paragraph and README were updated to reflect the latest export.

### Action boundary

The 21-item DOI list is a candidate metadata-intake queue, not a mandatory bulk import or a final inclusion list. Add metadata only for studies selected for manuscript use after considering evidence strength and scope. The existing 19 cited works remain confirmed against this export. No PDFs are requested.
