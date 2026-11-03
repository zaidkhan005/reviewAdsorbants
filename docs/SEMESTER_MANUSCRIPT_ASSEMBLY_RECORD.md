## Status update — 3 November 2026

The production manuscript has since been revised and rebuilt. This update supersedes the earlier standalone-supplement arrangement described below.

- **Canonical manuscript source:** manuscript/SEMESTER_MANUSCRIPT_ASSEMBLED_SOURCE_V2.md.
- **Current integrated table numbering:** Table 1 = literature search strategy and sources (parts 1A–1B); Table 2 = the 15-study condition-labelled comparison (parts 2A–2I); Table 3 = evidence coverage for all 49 selected references.
- **Current table sources:** manuscript/SEMESTER_TABLE_1_SEARCH_STRATEGY_SOURCE.md and manuscript/SEMESTER_TABLE_3_EVIDENCE_COVERAGE_SOURCE.md. The Table 2 panels are maintained in the assembled V2 manuscript source; SEMESTER_TABLE_1_CORE_STUDY_COMPARISON_V1.md is the earlier standalone V1 comparison source and is retained as historical context.
- The former standalone S1 and S2 Markdown source files were removed after their content was integrated into Tables 3 and 1, respectively. There are no separate supplementary-table deliverables in the current manuscript build.
- **Build generator:** scripts/build_semester_manuscript.py; **workflow:** .github/workflows/build-semester-manuscript.yml.
- **Successful integrated build:** GitHub Actions run [41593950973](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41593950973), source commit 8ad688e1b355c932ff1e3f60a442fc939ade9197, artifact ID 13211670732.
- The generated DOCX and PDF are stored in that Actions artifact rather than committed as binary files to the repository. The artifact has the normal GitHub Actions retention period.

See [SEMESTER_MANUSCRIPT_FILE_INDEX.md](SEMESTER_MANUSCRIPT_FILE_INDEX.md) for the current source-of-truth links and version map.

---
# Manuscript assembly record

**Assembly source:** `manuscript/SEMESTER_MANUSCRIPT_ASSEMBLED_SOURCE_V2.md`
**Source of truth:** GitHub repository `zaidkhan005/reviewAdsorbants`.

## Integrated content

- Main V2 narrative with internal manuscript-control notes removed from the publication-facing assembly.
- Four editable Mermaid diagrams embedded at their relevant locations in Sections 2, 3, 4 and 5.
- Revised Table 1 inserted after the Results and Discussion section as nine lettered components, with recovery/regeneration component 1F displayed as two compact four-column panels (1F(a): separation, regenerant and cycle count; 1F(b): cycle metric, result and qualification). The result is ten visible table panels. Water-matrix evidence remains separately divided into feed, test type and limitation.
- Supplementary Table S1 remains a separate 49-work supplement and is linked from the main text.
- The verified 54-entry BibTeX file remains the citation source; it contains 49 selected works, four topical/contextual references, and one separately identified PRISMA 2020 reporting-guideline reference.

## Verified scope and citation status

- 49 selected works plus four topical/contextual references plus one methods/reporting-guideline reference = 54 unique cited references.
- 53 unique citation keys and 53 unique DOI values verified in the bibliography audit.
- SEM-035 remains excluded by user decision; no screening or selection decision was reopened.
- Narrative/focused search scope is preserved; this is not relabelled as systematic or PRISMA-compliant.

## Remaining production tasks

1. Confirm the university or journal reference style; the current ACS Guide 2026 style is provisional. Use the curated 54-entry BibTeX source, not the legacy 19-entry V1 file.
2. Render Supplementary Table S1 separately in the required supplemental format.
3. Complete author details, declarations, acknowledgements, funding/conflict/data availability statements and language proof.
4. Complete the remaining sentence-level claim/source-pin proof and final submission checklist; preserve all source caveats and study holds.

## Latest successful production build — 2 November 2026

- GitHub Actions run: `41428502613` — success.
- Source commit: `85bd3cda83e6f4f8032292e3aa4187e01ef11170`.
- Artifact ID: `13133751051`; artifact digest: `sha256:6900102c8b8daead65d312aa89f142d61da7a8fa1d3b5c62ccc2e0ddccc1cc83`.
- Rendered output: 31-page A4 PDF and 39-page Word document.
- The build is still a draft using ACS Guide 2026 provisionally; the required AMU/supervisor style has not yet been confirmed.

## Final Table 1 layout

Table 1 contains nine lettered components and ten visible panels because recovery/regeneration is split into 1F(a) and 1F(b). Endpoint metrics are separated into individual rows; process evidence is split into recovery method, cycle performance, matrix validation, preparation and cost panels. Detailed qualifications remain in the study-specific notes and the 1F(b) qualification column rather than being repeated inside each data cell.


Table 1C now contains 28 metric/value rows because the three conflicting SEM-034 removal values (abstract/§3.2.2, §3.2.4 and conclusion) are shown separately.

## Reader-facing author–year labels and final production build — 2 November 2026

The publication-facing manuscript now identifies studies by author and year rather than internal candidate IDs.

- The 49 rows in Supplementary Table S1 use author–year study labels, with article titles in a separate column.
- All study-linked panels in main-text Table 1 use author–year labels: identity, conditions, endpoints, isotherm and kinetic outputs, recovery/reuse, matrix validation, preparation burden and cost evidence.
- The assembled manuscript narrative has reader-facing study references converted to author–year labels where candidate IDs were used.
- The internal audit mapping remains in docs/SEMESTER_AUTHOR_YEAR_CROSSWALK.md. The SEM-### and EV-SEM-### codes remain available in internal registers and evidence ledgers, not in the exported reader-facing manuscript.
- The computational rGO interaction paper's author order was corrected against its publisher byline and is labelled **Nguyen et al. (2024)**.
- This is a study-identification convention, not a switch to author–date bibliography formatting. The rendered citation system remains ACS-numbered provisionally, pending AMU/supervisor confirmation.

### Successful build and output QA

- GitHub Actions run: 41438565195 — success, source commit f3df2c2c3868a30fb9720e287d7836731d3edb9a.
- Artifact ID: 13138200918; artifact digest: sha256:cc6ce7cac4ac6f6bb060ce549b61f3b1d8a14c3a26758809da8726c3336ea0ee.
- Final outputs: 31-page A4 PDF and 39-page Word document.
- Word pagination: Table 1B's 19 condition rows fit on one page using compact 9-pt table text; Table 1C's 28 metric/value rows fit on one page; Table 1D begins on page 22 without a blank intervening page.
- Reader-facing leakage check: no SEM-###, EV-SEM-###, CORP-031 or editorial “Cite with” markers in either exported file.
- PDF preflight: openable, searchable, unencrypted, no XFA, 31 A4 pages.
- DOCX accessibility audit: zero high- and medium-severity findings; 53 low-severity flags are raw DOI URLs used as bibliography hyperlink display text.
- Scientific values, evidence qualifications, the 49-work selection and the four contextual citations were not changed by the naming revision.

The manuscript remains a working draft. Citation-style confirmation, author/declaration fields, language proof and the final sentence-level source-pin check remain outstanding. Supplementary Table S1 has now been rendered as a separate Word/PDF pair; see the QA record below.


## Standalone Supplementary Table S1 — 2 November 2026

- The 49 selected-study records are now available as a separate editable Word document and searchable A4 PDF.
- Part A is a compact three-column author–year coverage index. Part B provides each article title, target, material family/role, source tier, and permitted evidence/numeric guardrail as distinct labelled fields. This avoids overloading wide table cells with paragraph-length content.
- Study records use author–year labels; ACS-numbered citations and the 49-item bibliography are retained provisionally. Internal SEM/EV-SEM identifiers are not exposed in the S1 reader render.
- Word output: 26 A4 pages. PDF output: 20 A4 pages. Long notes may continue across pages, but headings and the initial metadata block are kept together; index rows do not split across pages in Word.
- PDF preflight: openable, searchable, unencrypted, no XFA. Visual render inspection completed for all pages.
- S1 DOCX accessibility audit: 0 high, 0 medium, 49 low findings. All low findings are DOI hyperlinks displayed as raw DOI URLs in the bibliography.
- Values, source-access tiers, evidence guardrails and selected-work membership were carried over; no scientific values or reference-selection decisions were changed.
- Successful GitHub Actions run: 41488999074, commit 93360238f3a0edbc15add6d8d89060b061913a90. Artifact ID 13164305624; digest sha256:17fcad92f88bb37f1cc204666de26aa260dae89882279c78b597fae8823fe5d5.


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

## PRISMA-informed selection flow diagram — 3 November 2026

Figure 2 has been added to the main manuscript as a **PRISMA-informed selection flow**, not a PRISMA 2020-compliant flow diagram. It documents only the verified candidate-list and selection stages:

- The authoritative study-inclusion shortlist contains 51 candidate entries (`data/semester-study-inclusion-shortlist.csv`). These are shortlist rows, not all records retrieved by the public-web search.
- One known duplicate DOI alias was consolidated: SEM-041 is the same DOI-defined work as SEM-026. This leaves 50 unique DOI-defined works.
- SEM-035 was not carried into the active semester set for administrative/time reasons, not scientific rejection; 49 distinct works remain selected.
- The active 49 comprise 46 empirical primary studies and three context/boundary roles. Table 1 is a 15-study condition-labelled subset; S1 covers all 49. Four additional topical/contextual references sit outside the selected 49.
- The source log does not preserve per-source retrieval totals, title/abstract screening/exclusion counts, reports sought/not retrieved, or full-text exclusion reasons. Those boxes are marked as not recorded rather than estimated. The 51 shortlist entries are not presented as the total search yield.

Page et al. (2021), the PRISMA 2020 reporting-guideline paper, is added as a methods citation only. The bibliography now contains 54 distinct references: 49 selected works + four topical/contextual references + one reporting-guideline reference. Later figure numbering is shifted consistently: preparation-to-recovery is Figure 3, interaction pathways Figure 4, and the low-cost evidence framework Figure 5.

### Final outputs and QA

- Successful build: [GitHub Actions run 41577292915](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41577292915), source commit `d8548b04878dc3b54d9b097daac6af04925560fd`.
- Artifact ID `13204476413`; digest `sha256:6a6f52d0848444bfb100d782aed8cd1037754fe8f19499335f5328d0c283e4a1`.
- Main manuscript: 40-page editable DOCX; 32-page searchable A4 PDF.
- Supplementary Table S1: 26-page DOCX; 20-page searchable A4 PDF. Supplementary Table S2: one-page DOCX and one-page searchable A4 PDF.
- The Figure 2 image and caption appear together on PDF page 6 and Word page 7; figure 3–5 numbering and in-text references were checked. Full 32-page PDF and 40-page Word renders were reviewed; no clipped text, overlap or broken table layout was identified.
- PDF preflight: all three PDFs openable, searchable, unencrypted and without XFA. Section-sign (`§`) leakage remains zero.
- DOCX accessibility audit: zero high/medium findings. Low findings: 54 in manuscript and 49 in S1, all DOI hyperlinks displayed as raw URLs; S2 has no findings.
- No extracted numerical values, source-access tiers, study-selection decisions or scientific conclusions were altered by adding the diagram.


## Reader-facing methodology and Figure 2 consistency revision — 3 November 2026

The manuscript's Methods section and standalone search supplement were revised to read as publication-facing scientific prose rather than an account of the project workflow. Date-stamped statements about when searches were logged or rerun were removed. Search concepts, sources consulted, the iterative nature of the search, and the limitations of the retained search documentation remain stated. The 14 representative query formulations remain available in Supplementary Table S2; the supplement no longer presents them as a dated activity log.

Figure 2 now uses the same reader-facing author–year convention as the main manuscript. The internal candidate identifiers for the duplicate and administratively omitted candidate were removed. The duplicate is identified as **Fei et al. (2016)**. The figure and Section 2.3 distinguish the 51 candidate records considered for selection from the total number retrieved by searching; the latter is unavailable. The flow retains the 50 unique DOI-defined works and 49 selected works, including 46 empirical primary studies and three theory, review or scope-boundary roles. Four additional contextual references remain outside the selected set.

The methods now explain the focused narrative search, study eligibility and selection, source availability, data extraction, endpoint separation, mechanistic-evidence limitations and the basis for assessing low-cost potential. No formal systematic-review or PRISMA 2020-compliance claim is made. The selection-flow diagram remains explicitly PRISMA-informed only.

Figure 2 is fixed at its authored position in the PDF build so that it appears after Section 2.3 and before Section 2.4; the Word version retains the same reading order. The diagram and its full caption appear together on PDF page 6 and Word page 7.

- Successful GitHub Actions build: [41580995762](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41580995762).
- Source commit: `a8e58697d3bce10c5412d080a9492db6f948f840`.
- Artifact ID: `13206246434`; digest: `sha256:f11fc14b466f2851f7aea82bf55d1a31a08fcbba3016cb74b486aaffbc94f3a4`.
- Main manuscript: 41-page editable Word and 32-page searchable A4 PDF. Supplementary Table S1: 26-page Word and 20-page searchable A4 PDF. Supplementary Table S2: one-page Word and one-page searchable A4 PDF.
- Main and S2 PDFs are openable, searchable, unencrypted and have no XFA. The final PDF text confirms that Figure 2 precedes Section 2.4; the flow diagram contains no internal candidate/evidence IDs, and the revised Methods/S2 text contains no date-stamped search-log chronology.
- No extracted numerical adsorption values, source-access tiers, study inclusion decisions, scientific conclusions or bibliography records were changed by this editorial revision.


## Figure 2 and study-selection wording refinement — 3 November 2026

The Figure 2 introduction has been shortened to avoid repeating the study-selection totals immediately after they are stated in Section 2.3. Its caption now identifies the figure as an overview of literature identification and evidence organization. The diagram shows the focused literature search, eligibility assessment, the 49 works discussed in the review (46 empirical primary studies and three contextual publications), the 15-study comparison in Table 1, the 49-work evidence summary in Supplementary Table S1, and four additional background references.

Section 2.3 describes title/abstract assessment, examination of available full texts, application of the stated eligibility criteria, and variation in source availability in conventional academic prose. The figure is an overview of the available selection information; it does not imply a complete PRISMA flow or supply search-result totals that were not preserved.

The reader-facing manuscript source no longer contains internal study/evidence identifiers or inline evidence-ledger annotations. The S1 build text presents the purpose, study notes and interpretation rules without internal project-management explanations. Scientific qualifications, study counts, source-access limitations and citation keys were retained.

### Successful production build and verification

- GitHub Actions run: [41585076559](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41585076559) — success.
- Source commit: `081037f8adee72767888b498eacdb0a026f916e0`.
- Artifact ID: `13207467919`; digest: `sha256:2778b99f8e7ff1160773018c0dbd68ce03de5c22fc16ff4b2083888a65a802db`.
- Main manuscript: 39-page editable Word document and 31-page searchable A4 PDF.
- Supplementary Table S1: 26-page Word document and 20-page searchable A4 PDF.
- PDF preflight: main manuscript and S1 PDFs openable, searchable and unencrypted.
- Visual review: Figure 2 appears after the selection discussion and before Section 2.4 in both manuscript formats; the diagram, caption and surrounding text are legible and consistent.
- Reader-facing text check: no internal study/evidence identifiers or internal selection-process explanations remain in the manuscript or S1 output.
- Citation style remains ACS Guide 2026 provisionally, pending confirmation of AMU or supervisor requirements.


## Final pre-submission production pass — 3 November 2026

The manuscript was rebuilt after correcting Word page geometry and pagination controls. These changes affect production only; no adsorption values, evidence tiers, study-selection decisions or scientific conclusions were modified.

### Production corrections

- The Word build now writes explicit A4 portrait page dimensions (11906 × 16838 twips) and 22 mm margins. This prevents Word from falling back to US Letter where the DOCX section geometry was previously unspecified.
- Table 1 now begins on a new page. Table 3 also begins on a new page. Continuation pages retain table headers.
- A dedicated **References** heading is included in both the DOCX and PDF.
- The version index now records the current successful build and the corrected bibliography count (49 selected + four contextual = 53 unique references).
- The remaining-work register and citation-linkage audit now reflect the completed manuscript-level citation reconciliation.

### Citation reconciliation

- All **49 selected references** have verified Better BibTeX keys in the frozen selection register.
- All 49 selected keys are present in the consolidated 53-entry bibliography.
- The assembled manuscript contains 53 unique citation keys; all 53 resolve to bibliography entries. There are no missing or unused keys.
- This is a repository-level V2 linkage check, not an exhaustive audit of every live Zotero collection, attachment or note.

### Latest successful build and visual QA

- Successful GitHub Actions run: [41602499154](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41602499154).
- Build source commit: `6c6cc26c058fdf4ea113f944553ad9c87121d133`.
- Artifact ID: `13214429824`; digest: `sha256:6367e4365c9024290ab5545f25146a19c9082fca4186954fe0060f335f90e4a7`; retention expires 3 December 2026 at 08:22 UTC.
- PDF: 47 pages, A4, searchable, unencrypted.
- DOCX: explicit A4 geometry with 22 mm margins; LibreOffice visual render produced 58 A4 pages.
- All 47 PDF pages and all 58 DOCX-render pages were visually inspected. No clipping, overlapping objects, corrupted formulas, broken diagrams or missing table content was observed. Dense comparison tables remain legible and use separate fields for conditions, endpoints, model outputs, recovery, matrix evidence and cost caveats.
- Table 1 and Table 3 start on separate pages. The References heading is present. The Table 3 index and all 49 study-level evidence notes are present.

### Items still preventing a submission-ready freeze

- The current citation style remains ACS Guide 2026 provisionally; AMU/supervisor requirements must be confirmed before a final style conversion.
- The remaining sentence-level source-pin audit beyond the 46 current claim groups is not complete.
- HOLD/PROVISIONAL values remain explicitly qualified or excluded from cross-study rankings. In particular, SEM-010 and SEM-038 retain unresolved source/mass-balance conflicts; SEM-050 and SEM-051 retain cost/data-basis qualifications. These are not silently “corrected.”
- Full text/SI for SEM-047 and SEM-048 and additional cost-itemization details for SEM-051 remain desirable source improvements, not grounds to invent missing values.
- Final author details, acknowledgements, funding, conflict-of-interest and data-availability statements, language edit and AMU submission checklist still require author/supervisor confirmation.
- The manuscript must continue to be described as a focused narrative evidence synthesis, not as a completed systematic review or PRISMA-compliant review.

**Production QA status:** complete for the 3 November 2026 build. **Scientific and institutional submission sign-off:** still pending the items above.


## User-supplied full-text evidence update — 3 November 2026

Five selected papers (SEM-038, SEM-047, SEM-048, SEM-050 and SEM-051) were re-audited from the user's newly uploaded primary PDFs. Their source tiers and endpoint distinctions have been updated in Table 3 and the reader-facing V2 manuscript. The sixth upload is a separate Kabir et al. (2024) GrGO/TC paper, not SEM-010; it remains unselected pending a separate inclusion decision. The frozen 49-reference set, 53-entry bibliography and citation keys are unchanged. See [the six-PDF audit log](../logs/2026-11-03-user-supplied-six-paper-full-text-audit.md).
