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


## Latest integrated build after six-PDF audit — 3 November 2026

- **GitHub Actions run:** [41676514098](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41676514098) — successful.
- **Source/build commit:** `d85ff06254dbb1a718e60769c7db87a47026d921`; the subsequent evidence-ledger-only commit is `491bd3fc014139d1443304d34de021e35dcdd664`.
- **Artifact:** `semester-manuscript-v2-acs-draft`, ID `13251351229`, created 3 November 2026; normal 30-day retention (expires 3 December 2026).
- **Rendered outputs:** A4 PDF, 47 pages; DOCX, 59 pages. Bibliography text was tightened to 8.5 pt in both outputs to remove the single-reference PDF orphan; the final PDF page now holds references 34–53. Word's final page contains references 47–53.
- **QA:** All 47 PDF and 59 DOCX pages were rendered and visually contact-sheet reviewed; the final bibliography pages and updated Table 3 entries were inspected at full size. All 53 manuscript citation keys resolve to the 53-entry consolidated bibliography; Table 3 and the frozen selection each retain 49 selected works.

The citation style remains a provisional ACS 2026 build pending the supervisor/AMU requirement. This remains a working manuscript draft, not a submission-ready final.


## Corrected Word equation build and output QA — 3 November 2026

The latest Word/PDF production run is [GitHub Actions run 41682709331](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41682709331), completed successfully from source commit `60cffe8f58724b2755de53ca4236708896d459cd`. Artifact ID: `13253501547`; SHA-256: `00ab783d2479efc1d2e86413927fcb0a997d04441a00ea1ad690b0b69d62ad73`.

A cross-format QA check had found that ten double-escaped inline-math spans in the SEM-010 explanation were visible as literal delimiters in the DOCX, even though the PDF rendered them as equations. The DOCX-only build stage now normalizes those spans before Pandoc conversion. The corrected Word file contains 308 native Office Math objects and no literal inline-math delimiters in the document XML. No PDF source, scientific data, evidence grade, selection decision or citation was changed.

The regenerated PDF is 48-page A4, searchable and unencrypted. Its extracted text matches the preceding successful 48-page PDF. The corrected DOCX renders to 59 A4 pages with 22 mm margins; all 59 page images were contact-sheet reviewed, and the revised SEM-010 paragraph and the dense table/notes/reference pages were inspected at full size. No visible clipping, overlap, broken figure or missing table content was found.

The selected 49-reference set and 53-entry bibliography remain unchanged. SEM-010's 99% removal, experimental kinetic `qe=78.82 mg/g`, PSO-fitted `qe=79.36 mg/g`, separate Langmuir `qm`, inferred-but-unconfirmed ~25 mg/L dose possibility and 20 mg/L versus 20 g/L source conflict remain separately qualified.

**Production status:** corrected DOCX/PDF build passed. **Submission status:** still a working manuscript; AMU/supervisor citation style confirmation, remaining sentence-level source-pin coverage, language editing, author declarations and institutional checklist are outstanding. See [the detailed Word equation and build QA log](../logs/2026-11-03-word-equation-formatting-and-build-qa.md).


## Claim-ledger continuation checkpoint — 3 November 2026

The claim-by-claim source audit has been extended to **94 unique groups (CLM-01–CLM-94)**. This includes separate source records for older GO baselines, magnetic derivatives, polymer/immobilized formats, mechanistic evidence, preparation/recovery/reuse, monetary-cost denominators, newer engineered CIP composites, theory/review/scope-boundary roles, and the chitin/GO flow-through and MgO/chitosan/GO preview sources. Dated tranche logs are indexed in [the manuscript file index](SEMESTER_MANUSCRIPT_FILE_INDEX.md).

The final integrity sweep on 3 November 2026 confirms:
- 94 claim IDs, unique and contiguous from CLM-01 to CLM-94, with no missing or duplicate IDs.
- 49 selected-reference rows, all unique; selection membership unchanged.
- 53 distinct bibliography entries and 53 distinct manuscript citation keys; zero missing citation keys and zero unused bibliography entries.
- DOI-matched Better BibTeX keys are recorded in the candidate register for all newly audited candidates checked in this pass.
- The claim-by-claim audit document states the same current total, 94.

No manuscript prose, numerical source values, study selection, or bibliography membership was modified by these audit/register updates. The latest validated Word/PDF production artifact remains run [41682709331](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41682709331); no rebuild was triggered because the manuscript source and production inputs were not changed.

**Remaining before institutional submission sign-off:** confirm the citation style required by AMU/the supervisor (ACS 2026 remains provisional); complete the remaining sentence-level source-pin and editorial coverage beyond the current claim groups; perform final language editing; confirm author details, acknowledgements, funding, conflict-of-interest and data-availability declarations; and complete the AMU submission checklist. Existing scientific holds—including SEM-010, SEM-038, SEM-046, SEM-050 and SEM-051—must remain visible and must not be silently corrected.


## Claim-ledger CSV repair and final coverage verification — 3 November 2026

The claim/evidence CSV had two structural defects: CLM-08 lacked a final closing quote, and CLM-46 contained an 11-field row in a 10-column schema. Both were repaired without changing any scientific content. Blank separator lines were removed.

Read-back verification now confirms 94 claim rows with 10 columns each, CLM-01–CLM-94 contiguous and unique, zero malformed rows, and zero unbalanced quote lines. The 53 distinct source keys in the claim ledger all match the bibliography and are all cited in the assembled manuscript. The bibliography contains 53 distinct entries, all cited; no missing or unused entries were found. The frozen reference selection remains 49 unique rows.

The repair affected only the evidence ledger. Manuscript prose, production source, citations and numerical results were not changed, so no Word/PDF rebuild was triggered. The [CSV integrity repair log](../logs/2026-11-03-claim-ledger-csv-integrity-repair.md) is linked from the file index.


## Final 94-claim manuscript integration audit — 3 November 2026

The latest integration pass compared all 94 claim-ledger records with the reader-facing manuscript. Each of the 53 distinct source keys now appears in its declared manuscript section/range; all 53 manuscript citation keys resolve to the 53-entry bibliography, with no missing or unused entries. The 49-study frozen selection is unchanged.

Targeted manuscript updates:
- Consolidated Section 3.6.4 and removed duplicated Jahan/Tekle magnetic-composite text.
- Added source-specific mechanistic qualifications/citations for Jahan, Lemaoui and Saheed in §4.3, and cited the DFT-only rGO model study with the correct theory-only limitation in §4.5.
- Added source citations and process-boundary examples across §§5.1–5.3, including battery-derived GO, magnetic recovery/reuse, N-rGO, alginate/MOF beads, multi-water tests, chitin/GO column hold and membrane matrix qualifications.
- Added Lemaoui's active-layer cost source directly to §5.4, keeping USD/m² and carbon-footprint metrics separate from financial cost per m³.
- Corrected legacy claim-ledger section labels CLM-20–CLM-27 to their actual §3.6.1–3.6.3 locations.

Automated check: 94 claim rows; 53/53 keys present in their declared manuscript section/range; 53 bibliography entries and 53 cited keys; zero missing/unused citation keys; 49 unique selected references. The full findings and exact scope limits are in the [final 94-claim integration audit log](../logs/2026-11-03-final-94-claim-manuscript-integration-audit.md).

These are reader-facing manuscript-source edits, so GitHub Actions run [41690681789](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41690681789) is rebuilding the Word/PDF outputs. Production sign-off remains pending artifact/pagination verification.


## Latest corrected production artifact — 3 November 2026

The final 94-claim integration manuscript was rebuilt after correcting the Word rendering of standalone chemical subscripts/superscripts. The earlier integrated build had displayed square placeholders in several formula groups in the editable DOCX; the source now uses complete chemical expressions.

- **Successful build:** [GitHub Actions run 41691972025](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41691972025).
- **Source commit:** `a7ae064028cee61bfaefa81705148b53f7eae56f`.
- **Artifact ID:** `13258235067`; artifact SHA-256 `c9c8516f8b3de049eb98527ed921b1d95db0e65516d15aa3fd916790ac412721`; expires 3 December 2026.
- **PDF:** 48 searchable, unencrypted A4 pages.
- **DOCX:** A4 portrait with 22 mm margins; independent LibreOffice render produced 58 pages.
- **Formula QA:** final DOCX XML contains 312 native Office Math objects, zero literal inline-math delimiters and zero replacement-square characters. Previously affected formula pages (DOCX render pp. 17, 30, 32–34) were inspected at full size after correction; placeholders are gone.
- **Pagination QA:** contact sheets for all 58 DOCX-render pages and all 48 PDF pages were reviewed; affected formula pages and integration-edited sections were inspected at full size. No obvious clipping, overlapping objects, broken figures or missing table content was seen in the reviewed pages. The DOCX and PDF have different pagination because the DOCX count is from a separate LibreOffice render.
- **Citation/content integrity remains:** 94 unique claim groups; 49 selected studies; 53 bibliography entries and 53 manuscript citation keys; zero missing or unused citation keys.

Download copies of this verified build were generated in the current working session as `SEMESTER_MANUSCRIPT_V2_ACS_DRAFT_integrated.docx` and `SEMESTER_MANUSCRIPT_V2_ACS_DRAFT_integrated.pdf`. The repository file index points to this build as the latest verified output.

**Status:** production build and visual QA completed for this working draft. Not final submission approval: ACS 2026 remains provisional pending AMU/supervisor confirmation; final language edit, author/funding/conflict/data-availability declarations and the AMU submission checklist remain outstanding.


## Critical scientific-hold visibility check — 3 November 2026

A final reader-facing check was completed for SEM-010, SEM-038, SEM-046, SEM-050 and SEM-051. All five holds remain explicit; none was promoted into an unqualified observed capacity, condition-matched ranking, verified native real-water result or full-system low-cost claim.

- SEM-010: 99% removal, experimental (q_e=78.82) mg/g and PSO-fitted (q_e=79.36) mg/g remain separate; 20 mg/L versus 20 g/L and the unverified ~25.1 mg/L dose-basis possibility remain qualified.
- SEM-038: TC feed ceiling versus 90.21 mg/g remains held; 1,265.82 mg/g is explicitly assigned to CLI, while TC Langmuir (q_m=662.25) mg/g remains fitted.
- SEM-046: 8.37→2.01 mg/L gives 76.0% calculated removal versus 90.75% source-reported; body/abstract reuse percentage discrepancy remains.
- SEM-050: prefiltered-and-spiked municipal wastewater is not called native wastewater; powder (q_e=22.7pm0.6) mg/g remains quarantined; USD/m² active-layer estimate and kg CO₂-eq footprint remain separate from financial cost per m³.
- SEM-051: USD 1.95/g remains an author estimate with model/feed assumptions; 0.1 M versus 1.0 M regeneration discrepancy and 83.9% desorption-efficiency metric remain explicit.

See the [critical scientific-hold visibility log](../logs/2026-11-03-critical-hold-visibility-check.md). This check documents unresolved source limitations; it does not resolve them.


## Controlled language-editing pass — 4 November 2026

A language-editing pass has been applied to the canonical assembled manuscript V2. It covers the abstract, Introduction, Scope and methods, Results and discussion, Mechanistic interpretation, Practical feasibility, and Conclusions. The pass improves sentence structure, grammar, clarity, and consistency and standardizes common spelling variants to American English for the provisional ACS-style working draft.

No source tables, claim-ledger rows, candidate selection, bibliography records, or citation keys were edited. The 94-claim ledger remains intact; all 53 distinct citation keys remain present in the manuscript and resolve to the 53-entry bibliography; all 49 selected studies remain unchanged; and all 94 claim rows retain citation coverage in their declared manuscript section/range. The empty-base math-fragment scan remains clear.

The language changes were deliberately conservative: numerical endpoints, conditions, units, source tiers, equations, limitations, and unresolved holds were preserved. See the [4 November language-editing log](../logs/2026-11-04-language-editing-pass.md).

A new Word/PDF production build has been triggered by the latest manuscript source commit. Production sign-off for this language-edited version remains pending a successful build and visual QA of the refreshed DOCX/PDF renders.


## Final language-edited build and pagination QA — 4 November 2026

The language-edited manuscript has been rebuilt after correcting the Amin et al. bibliography title rendering and adding Word bibliography paragraph keep-lines formatting.

- **Successful build:** [GitHub Actions run 41718042264](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41718042264).
- **Source commit:** `ef2b1de98fe4d25c1a05a02bda11d504296e558d`.
- **Artifact ID:** `13270582585`; artifact SHA-256 `97a1ac75e8ea008bdb52db46c65844e9600975705c770580b9a0bad99517f538`.
- **PDF:** 48 searchable, unencrypted A4 pages.
- **DOCX:** 60 A4 pages; 315 native Office Math objects; zero replacement glyphs and zero literal inline-math delimiters.
- **Bibliography pagination:** each of the 53 DOCX bibliography entries is protected with keep-lines-together. Reference 46 (`NH2-UiO-66(Zr)`) now remains intact on Word page 60; Word page 59 ends after reference 45.
- **Integrity:** 94 claim IDs, 49 selected works, 53 in-text citation keys and 53 bibliography entries; no missing or unused citation keys.

DOCX/PDF hashes, final visual checks, the exact bibliography correction and the remaining submission caveats are recorded in the [final language-edited build QA log](../logs/2026-11-04-language-edited-final-build-qa.md). The manuscript remains a working draft pending AMU/supervisor citation-style confirmation and required author/institutional declarations.
