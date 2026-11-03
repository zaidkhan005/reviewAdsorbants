# Author–year study labels and final manuscript build QA — 2 November 2026

## Reader-facing naming

The publication-facing manuscript uses author–year labels rather than internal study identifiers. Supplementary Table S1 contains 49 selected-study rows. Main-text Table 1 uses author–year labels in all study-linked panels. The manuscript narrative no longer exposes candidate IDs used as reader-facing labels.

The internal crosswalk remains at docs/SEMESTER_AUTHOR_YEAR_CROSSWALK.md, preserving the mapping between SEM-###, author–year labels and the consolidated bibliography citation keys. Internal evidence IDs and audit registers remain unchanged.

The computational rGO interaction work is labelled **Nguyen et al. (2024)** after correcting the BibTeX author order to match the publisher byline.

## Production identity

- GitHub Actions run: [41438565195](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41438565195) — success.
- Source commit: f3df2c2c3868a30fb9720e287d7836731d3edb9a.
- Artifact ID: 13138200918.
- Artifact digest: sha256:cc6ce7cac4ac6f6bb060ce549b61f3b1d8a14c3a26758809da8726c3336ea0ee.
- Output: 31-page A4 PDF and 39-page DOCX.

## Layout and output checks

- Word Table 1B fits 19 condition rows on one page with compact 9-pt table text.
- Table 1C fits all 28 separately labelled endpoint rows on one page.
- The redundant Word page break before Table 1D was removed; Table 1D begins on page 22 with no intervening blank page.
- PDF remains 31 pages and retains its own authored page breaks.
- PDF preflight passed: openable, searchable, unencrypted, no XFA.
- Exported PDF and DOCX contain none of these internal/editorial markers: SEM-###, EV-SEM-###, CORP-031, “Cite with”.
- DOCX accessibility audit: 0 high, 0 medium, 53 low. All low-severity findings are DOI hyperlinks displayed as raw URLs.

## Scope and remaining holds

The naming change did not alter reference selection, reported scientific values, model/observed endpoint distinctions, source tiers, caveats or study holds. The active selection remains 49 works plus four contextual references. ACS-numbered citation formatting remains provisional pending AMU/supervisor confirmation. The separate S1 file, author/declaration fields, language proof and final sentence-level source-pin pass remain outstanding.

## Standalone Supplementary Table S1 build and visual QA

- GitHub Actions run: [41488999074](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41488999074) — success.
- Source commit: 93360238f3a0edbc15add6d8d89060b061913a90.
- Artifact ID: 13164305624; digest: sha256:17fcad92f88bb37f1cc204666de26aa260dae89882279c78b597fae8823fe5d5.
- S1 DOCX: 26 A4 pages. S1 PDF: 20 A4 pages, searchable, unencrypted, no XFA.
- Structure: 49 unique author–year labels in the index; 49 study-by-study evidence notes; 49 numbered citation links; 49 numbered bibliography entries. The four contextual references remain included in the manuscript reference system as previously defined; they are not added to the 49-row selected-study register.
- Layout: the index is a compact three-column table; no Word index row splits across pages. In Word, each numbered study heading stays with its title and first metadata fields. In PDF, a page-space guard keeps study headings and their first metadata block together. Longer guardrail notes may continue on the following page where necessary.
- Export leakage check: no SEM-###, EV-SEM-### or CORP-031 markers in either S1 DOCX or PDF text.
- DOCX accessibility audit: 0 high, 0 medium, 49 low findings; all low findings are bibliography DOI hyperlinks shown as raw URLs.
- Full-page visual inspection of Word/PDF page renders found no clipped text, broken table rows, missing glyphs or overlapping objects.
- The S1 build did not modify study selection, numerical values, source tiers, caveats, or claim-level scientific conclusions. ACS-numbered citations remain provisional pending AMU/supervisor confirmation.

## Updated deliverables from the same build

- Manuscript DOCX: 39-page editable draft.
- Manuscript PDF: 31-page searchable A4 draft.
- Standalone S1 DOCX/PDF: 26-page Word and 20-page PDF.


## Reader-facing section-reference wording cleanup — 3 November 2026

The section sign (§), previously used as conventional shorthand when identifying sections of cited source papers, has been replaced with the explicit word **Section** throughout the assembled manuscript, Table 1 source and standalone Supplementary Table S1 source. All article section numbers and citations are retained. This is an editorial readability change only.

- Replaced 13 occurrences in the assembled manuscript source, 2 in Table 1 source, and 2 in S1 source (17 total source occurrences).
- Export checks: zero section-sign characters in manuscript DOCX/PDF and S1 DOCX/PDF. Source-paper section pointers are now written as, e.g., `Section 3.3.6`.
- Successful GitHub Actions run: [41569093216](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41569093216) — success; commit `072b0fdc8c1f0b1bfeb54316649c5882ab5e3333`.
- Artifact ID: `13200661552`; digest: `sha256:bab349c81c50ca92f8b14205feaf353e2665f80ca642f5a951fd3936d56e8ad1`.
- Final manuscript PDF: 31-page searchable A4. Final S1 PDF: 20-page searchable A4. DOCX page-image renders were inspected after the text substitution; no clipping or overlapping objects were found.
- No numerical values, evidence-tier decisions, study inclusion/exclusion, scientific conclusions or bibliography entries were changed.

## Methods refinement and standalone search-strategy supplement — 3 November 2026

Sections 2.2–2.4 were shortened and made more publication-facing. The detailed historical candidate-register counts were removed from the main text; the section now reports the active 49-reference set, the four contextual references, the 15-study condition-labelled comparison subset, the source-access hierarchy, and the absence of a reconciled PRISMA-style record flow. Extraction and critical-appraisal fields remain explicit, including the distinction between observed, calculated and fitted adsorption endpoints and the limitations of mechanistic inference from model fit alone.

The 11 query formulations logged on 28 October 2026 and three later formulations logged on 31 October 2026 were moved to **Supplementary Table S2**. S2 also records the limitations of the search log: the general public-web discovery platform was not preserved, query-to-platform attribution is unavailable, no Scopus or Web of Science search is documented, and some later 30–31 October searches are retained only as topic summaries because exact strings were not recorded.

- Main-text Section 2.2 points to Supplementary Table S2; S1 remains the 49-reference evidence-coverage supplement.
- S2 contains 14 numbered query formulations: 11 logged on 28 October and 3 logged on 31 October 2026.
- Manuscript Word/PDF: 39-page editable Word and 31-page A4 PDF. S1 Word/PDF: 26-page Word and 20-page A4 PDF. S2 Word/PDF: one page each, A4.
- PDF preflight: all three PDFs are openable, searchable, unencrypted and have no XFA.
- DOCX accessibility audit: zero high- and medium-severity findings across all three files. Low-severity findings are 53 in the manuscript and 49 in S1 (DOI hyperlinks displayed as raw URLs); S2 has none.
- Reader-facing `§` count remains zero in manuscript, S1 and S2 DOCX/PDF outputs.
- No scientific values, source tiers, caveats, reference-selection decisions or claims were changed by the methods reorganization.
- Successful GitHub Actions run: [41571976064](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41571976064). Source commit: `18fece36a03a20c5f2fdbb8165d285a9e2a213e8`. Artifact ID: `13201751961`; digest: `sha256:fc464d9bbf8052b4a042eef5984ebc8d9042be5893687f7baf20a9e2e074d544`.
