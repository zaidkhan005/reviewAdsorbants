# Manuscript assembly record

**Assembly source:** `manuscript/SEMESTER_MANUSCRIPT_ASSEMBLED_SOURCE_V2.md`
**Source of truth:** GitHub repository `zaidkhan005/reviewAdsorbants`.

## Integrated content

- Main V2 narrative with internal manuscript-control notes removed from the publication-facing assembly.
- Four editable Mermaid diagrams embedded at their relevant locations in Sections 2, 3, 4 and 5.
- Revised Table 1 inserted after the Results and Discussion section as nine lettered components, with recovery/regeneration component 1F displayed as two compact four-column panels (1F(a): separation, regenerant and cycle count; 1F(b): cycle metric, result and qualification). The result is ten visible table panels. Water-matrix evidence remains separately divided into feed, test type and limitation.
- Supplementary Table S1 remains a separate 49-work supplement and is linked from the main text.
- The verified 53-entry BibTeX file remains the citation source; citation-style conversion is not applied in this source assembly.

## Verified scope and citation status

- 49 selected works plus four retained contextual references = 53 unique cited works.
- 53 unique citation keys and 53 unique DOI values verified in the bibliography audit.
- SEM-035 remains excluded by user decision; no screening or selection decision was reopened.
- Narrative/focused search scope is preserved; this is not relabelled as systematic or PRISMA-compliant.

## Remaining production tasks

1. Confirm the university or journal reference style; the current ACS Guide 2026 style is provisional. Use the curated 53-entry BibTeX source, not the legacy 19-entry V1 file.
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

