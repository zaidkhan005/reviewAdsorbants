# Semester-paper citation linkage audit — 29 October 2026

## Purpose

This audit maps each semester candidate to existing Better BibTeX citation keys using the three available Library exports:
- `full ++.bib`
- `Antibiotic Adsorption Review new — Full Corpus.bib`
- `Antibiotic Adsorption Review — Full Corpus.bib`

The full ++ export was inspected at 164 BibTeX entries (164 unique keys; 161 DOI fields; 159 unique DOI values). The newer export has 61 entries (61 unique keys; 58 DOI fields), and the older export has 31 entries (31 unique keys and DOI fields). These exports overlap; their record totals must not be added as if they represent separate papers.

## Findings

- **Six distinct semester candidates have verified DOI-to-key matches:** SEM-016, SEM-020, SEM-032, SEM-038, SEM-039, and SEM-040.
- Three keys are consistent across all three exports: `shahaExploringAdsorptionEfficiency2025` (SEM-016), `liThreedimensionalGrapheneOxidebased2025` (SEM-032), and `zhangAdsorptionCharacteristicsNrGO2022` (SEM-038).
- Three keys were found only in `full ++.bib`: `zhuCiprofloxacinAdsorptionGraphene2015a` (SEM-020), `yao3DAssemblyBased2017` (SEM-039), and `pengAdsorptionAntibioticsGraphene2016` (SEM-040).
- The target-term title-line scan of the three exports did not locate further exact candidate-title matches among the remaining records. This means the records were not found in these exports by the checked DOI/title evidence; it does **not** prove that they are absent from the user's Zotero library or every other export.
- SEM-041 is a duplicate alias of SEM-026 and must not be counted as a separate cited work. SEM-021's DOI metadata remains unresolved.

## What this means for in-text citations

The stable keys above are the only keys verified by exact DOI matching from these exports. For other studies, do not invent `@key` strings based on authors, titles or candidate IDs. First find/verify the existing item in Zotero or another export; if it is not there, add/verify its metadata from accessible sources and regenerate the Better BibTeX export. Then insert the in-text citations with the manuscript's chosen citation style and run a final bibliography reconciliation.

Detailed candidate-level results are in [data/semester-bibtex-citation-linkage-audit.csv](../data/semester-bibtex-citation-linkage-audit.csv). This is a linkage audit, not a final inclusion list or a claim that 50 references have already been cited.


## Addendum — current export and manuscript reconciliation (2026-10-30)

The older counts above remain a dated 29 October snapshot. The user has now supplied a new `full ++ check again.bib` export with **173 entries, 173 unique keys, 170 DOI fields and 168 unique DOI values**. All six manuscript citation keys previously matched in the old 164-entry export remain present, and all nine previously unresolved citations now match an exact DOI record in the newer export. Their actual Better BibTeX keys have been updated in the manuscript, the 15-entry cited-reference subset, and the candidate-level citation linkage audit. The current manuscript's 15 distinct citation keys resolve locally; this checkpoint does not mean all 44 semester candidates are in Zotero or that 50 works have been cited.

**Candidate-level gaps remain.** For example, SEM-001 (Ghadim et al. 2013, DOI 10.1371/journal.pone.0079254) was checked against the new export and remains absent by DOI. Do not invent a citation key or cite it in the manuscript until a verified Zotero/Better BibTeX key exists. The nine-record batch prepared on 29 October has been marked historical/superseded for current citation linkage; do not re-import it by default.

The new export also contains two duplicate DOI groups elsewhere (`10.1016/j.envres.2021.111091` and `10.1016/j.ijbiomac.2024.133382`). Neither affects the 15 citations in the current semester manuscript. Audit those duplicate records separately before any merge/deletion so attachments and notes are not lost.
