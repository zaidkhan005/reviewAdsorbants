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

**Candidate-level gaps remain.** For example, SEM-001 (Ghadim et al. 2013, DOI 10.1371/journal.pone.0079254) and SEM-015 (GO–ZnAlNi LDH/CIP, DOI 10.3389/fnano.2025.1578620) were checked against the new export and remain absent by DOI. Do not invent citation keys or cite either study in the manuscript until verified Zotero/Better BibTeX keys exist. The nine-record batch prepared on 29 October has been marked historical/superseded for current citation linkage; do not re-import it by default.

The new export also contains two duplicate DOI groups elsewhere (`10.1016/j.envres.2021.111091` and `10.1016/j.ijbiomac.2024.133382`). Neither affects the 15 citations in the current semester manuscript. Audit those duplicate records separately before any merge/deletion so attachments and notes are not lost.

## 2026-10-30 continuation addendum — SEM-042 to SEM-044

The three most recently source-audited candidates were checked against **five** available Library BibTeX exports by exact DOI and normalized title:

- `full ++ check again.bib` — 173 entries
- `full ++.bib` — 164 entries
- `full ++=.bib` — 164 entries
- `Antibiotic Adsorption Review new — Full Corpus.bib` — 61 entries
- `Antibiotic Adsorption Review — Full Corpus.bib` — 31 entries

No exact DOI or normalized-title match was found for SEM-042 (10.1016/j.carbpol.2018.02.021), SEM-043 (10.1016/j.jhazmat.2014.03.063), or SEM-044 (10.1007/s00604-019-3563-x) in these five exports. Their rows in `data/semester-bibtex-citation-linkage-audit.csv` and `data/semester-main-corpus-crosswalk.csv` now record the absence and the required action. This result does not prove that the records are absent from every Zotero collection or an unexported collection; it only establishes that no Better BibTeX key can be verified from the five available exports. Do not invent citation keys. Locate/add each DOI-verified Zotero record, export Better BibTeX, and then update the linkage rows from the generated keys.


## 2026-10-30 citation expansion continuation — working Introduction and DOI intake

A new working Introduction/Scope draft adds four contextual sources whose keys already existed in the 173-entry Better BibTeX export:

- Ahmed et al. (2015), DOI 10.1016/j.scitotenv.2015.05.130, key `ahmedAdsorptiveRemovalAntibiotics2015a` — review-level background/cost framework only.
- Jiao et al. (2025), DOI 10.1016/j.jhazmat.2025.137566, key `jiaoCarbonNanomaterialsCoremoval2025` — review-level carbon nanomaterial/matrix/cost context only.
- Wang et al. (2010), DOI 10.1016/j.jhazmat.2010.07.025, key `wangCationExchangeInteraction2010` — CIP speciation/cation-exchange comparator on montmorillonite; clay is outside core material scope.
- Gu et al. (2007), DOI 10.1016/j.chemosphere.2006.08.028, key `guComplexationAntibioticTetracycline2007a` — TC/dissolved-humic-acid complexation; humic acid is not a solid adsorbent.

These four contextual entries are now appended to `references/semester-manuscript-cited-references.bib`. The Results/Discussion file still has 15 distinct citation keys; the separate Introduction/Scope file has four additional keys, giving **19 distinct cited works across the two working drafts**. Four are context/review sources, not additional core graphene adsorption studies.

A separate source-quality shortlist and DOI queue have been created for 13 additional semester candidates (SEM-001, 006, 007, 009, 011, 012, 015, 019, 025, 027, 028, 042 and 043). A direct DOI scan of all five available Library exports on 30 October 2026 found **no exact DOI match for any of the thirteen**. No BBT key has been invented. Use the DOI queue to search Zotero and import metadata only where missing; then export a fresh Better BibTeX file and update actual keys from that export before citing any of them.

The claim-to-evidence matrix now includes CLM-16–CLM-19 for the four contextual sources, with explicit labels preventing their use as core empirical performance records. The introduction also marks the final reproducible search-method details as pending: exact search platforms, dates, strings, date limits, deduplication and screening flow must be reconciled before describing the work as a completed systematic review.


## 2026-10-31 expanded DOI queue audit — 21 records

The DOI intake queue now contains **21 distinct semester-candidate DOIs**: SEM-001, SEM-006, SEM-007, SEM-009, SEM-011, SEM-012, SEM-015, SEM-019, SEM-025, SEM-027, SEM-028, SEM-030, SEM-042, SEM-043, and SEM-045–SEM-051.

On 31 October 2026, all 21 DOI strings were searched by exact DOI across the five mounted Library Better BibTeX exports:

- `full ++ check again.bib` — 173 entries
- `full ++.bib` — 164 entries
- `full ++=.bib` — 164 entries
- `Antibiotic Adsorption Review new — Full Corpus.bib` — 61 entries
- `Antibiotic Adsorption Review — Full Corpus.bib` — 31 entries

**No exact DOI match was found for any of the 21 queued records.** This result does not establish that the records are absent from Zotero: items in collections not represented by these five exports may still exist. Search Zotero itself by exact DOI before adding metadata, to avoid duplicates. If an item is absent, add/verify metadata, export a fresh Better BibTeX file and use only the generated key. Do not guess or manually construct citekeys.

The candidate-level linkage audit, main-corpus crosswalk and remaining-work register now carry the 31 October result for all 21 queued candidate IDs. The current manuscript's 19 existing cited works and their verified keys were not changed. Candidate/evidence records in the queue are not automatically eligible for citation and do not count toward the approximately 50-works-cited target until selected and actually cited.


## 2026-10-31 latest complete Zotero My Library export check

The user supplied `full ++ check again(1).bib`, identified as the latest complete Zotero My Library export. The file contains:

- **173 BibTeX entries**
- **173 unique citation keys**
- **170 DOI fields**
- **168 unique DOI values**
- Two duplicate DOI groups: `10.1016/j/envres.2021.111091` (keys `ashiqCarbonbasedAdsorbentsFluoroquinolone2021a` and `ashiqCarbonbasedAdsorbentsFluoroquinolone2021b`); and `10.1016/j.ijbiomac.2024.133382` (keys `rostamiSurfaceModifiedChitosan2024a` and `rostamiSurfaceModifiedChitosan2024b`). These duplicate groups were recorded, not merged or deleted.

All **21 DOI-queue records** were checked against the uploaded export by exact DOI and normalized title. **No exact DOI or normalized-title match was found for any of the 21.** A near-title result for SEM-019 is a different CMC-functionalized magnetic GO paper (DOI 10.1039/d5ra06621b), not the EDTA-functionalized candidate; it must not be linked to SEM-019.

Separately, all **19 citation keys already used in the unified manuscript** are present in the supplied export. Thus the current bibliography is linked to the supplied Zotero export, and no new citekeys were identified for the 21 queued candidates. Do not change the 19 existing manuscript citations.

The candidate-level citation linkage audit, main-corpus crosswalk, remaining-work register and intake queue now reflect this complete-library check. Add Zotero metadata only for candidate studies selected for manuscript inclusion, then export again and capture the actual Better BibTeX key. The 21 candidates are not an automatic import/citation list.


## Latest upload recheck — 31 October 2026

The user uploaded `full ++ check again(2).bib`. Its SHA-256 (`bc65b1a50bfda09824e8ae8ebbdb4c64270b16108d7ad79abd7675358749ac20`) is identical to the prior `full ++ check again(1).bib` export, so it is not a new bibliographic snapshot. Reconciliation against the frozen 50 candidate works found 15 exact DOI/key matches and 35 selected-study DOIs still absent from the export. All 19 existing manuscript keys (15 selected candidate keys plus four contextual keys) remain present. See [the latest export reconciliation log](../logs/2026-10-31-latest-bib-export-reconciliation.md) for the 15 matched keys, complete 35-DOI list and duplicate-DOI groups. Do not re-run this same-file audit unless a genuinely new export has a different SHA-256.


## 31 October 2026 — 28-entry Zotero export reconciliation

The newly uploaded `Untitled.bib` contains 28 BibTeX entries with 28 unique keys and 28 unique DOI values. All 28 DOIs match previously unresolved selected semester candidates. Combined with the prior 15 exact DOI/key matches from the complete 173-entry export, **43/50 selected DOI-defined works now have verified Better BibTeX keys; 7 remain unmatched**. The candidate-selection and citation-linkage CSVs now record the 28 verified keys. The remaining seven DOI list is in `references/semester-final-35-doi-import-queue.txt`; it has been reduced to the seven unresolved candidates. See `logs/2026-10-31-untitled-bib-reconciliation.md` for the full key mapping and audit details. This file is a 28-entry subset export, not a complete My Library export.


## 31 October 2026 — Untitled +.bib reconciliation

The newest `Untitled +.bib` contains 40 BibTeX entries, 40 unique keys, 40 DOI-bearing entries and 34 distinct DOI values. All 34 DOIs match selected semester candidates. Together with the earlier 15 and 28 matched candidates (with overlap correctly deduplicated), **49/50 DOI-defined semester works are now matched; SEM-035 (10.16796/j.cnki.1000-3770.2025.09.007) remains absent**. The export also contains six duplicate DOI pairs for SEM-046–SEM-051, so the surviving keys must be re-exported after Zotero Duplicate Items merges. For SEM-049 and SEM-050, preserve both PDF attachments if useful. The current remaining DOI file lists SEM-035 and the duplicate-cleanup instruction. See `logs/2026-10-31-untitled-plus-reconciliation.md`.


## SEM-035 identifier lookup diagnosis — 31 October 2026

The user attempted Zotero's Add by Identifier with DOI `10.16796/j.cnki.1000-3770.2025.09.007` and received `Lookup Failed`. Independent verification confirms the DOI is valid and resolves to the official *Technology of Water Treatment* journal record: Peng Bo, Ouyang Feng, Liu Liao, Wang Songtao, Tang Chengrui and He Yang, “Adsorption Characteristics of Modified Graphene Oxide on Tetracycline Antibiotics in Water,” 2025, 51(9), 41–47. EBSCO independently indexes the same article/DOI. Thus this is an identifier-lookup-service limitation, not a malformed DOI. Manual Zotero Journal Article entry is the next action; no Better BibTeX key should be fabricated. The article studies GO–chitosan film/particles and reports TC separately from CTC; preserve analyte separation. Official publisher URL: https://www.scljs1975.com/EN/10.16796/j.cnki.1000-3770.2025.09.007 .


## 31 October 2026 — final DOI intake closure

The latest uploaded `Untitled ++.bib` contains 41 BibTeX entries, 41 unique citation keys, and 35 unique DOI values. It adds SEM-035, DOI `10.16796/j.cnki.1000-3770.2025.09.007`, with the Zotero-generated Better BibTeX key `AdsorptionCharacteristicsModified2025`. Combining the verified 15 matches in the earlier complete 173-entry export and the 35 previously missing selected works now present in the later exports, **all 50/50 distinct DOI-defined semester works have verified Better BibTeX keys**. SEM-041 remains the duplicate alias of SEM-026 and is not a 51st work. DOI intake is closed; no new metadata lookup or PDF downloads are needed. The only reference-database cleanup remaining is six duplicate DOI pairs for SEM-046–SEM-051 in the latest export. Merge the duplicate Zotero items while preserving PDF attachments where needed, then regenerate Better BibTeX to confirm surviving keys. The queue `references/semester-final-35-doi-import-queue.txt` has been retired to a completion/cleanup note. See `logs/2026-10-31-untitled-plus-reconciliation.md` and the current final export reconciliation log.


## Correction after inspection of `Untitled +++.bib` — 31 October 2026

The newest file contains 35 BibTeX entries, 35 unique keys, 34 DOI-bearing entries and 34 unique DOI values. There are **zero duplicate DOI groups**; the six previously identified duplicate groups SEM-046–SEM-051 have disappeared from this export, apparently successfully consolidated. However, the SEM-035 title-matching record is incomplete: no DOI, journal, year, volume, issue or pages, and only three of six authors. Its export key is `zotero-item-589`, a fallback placeholder, not approved as a manuscript citation key. Therefore the accurate status is **49/50 fully DOI/key-verified; SEM-035 is represented by title only but is not citation-ready**. Complete that Zotero record with its publisher metadata and re-export Better BibTeX before declaring 50/50 citation readiness. The current DOI queue file has been converted into this final metadata-completion instruction.
