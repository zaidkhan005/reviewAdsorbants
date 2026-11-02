# Figure rendering and manuscript-page QA record

**Date:** 31 October 2026  
**Project:** Semester manuscript V2 — Antibiotic Adsorption Review

## Rendering route

The repository build workflow uses Mermaid CLI (`mmdc`) to render the four editable Mermaid source blocks embedded in `manuscript/SEMESTER_MANUSCRIPT_ASSEMBLED_SOURCE_V2.md` into PNG images. The images are inserted into both DOCX and PDF outputs by the Pandoc build script. The standalone Mermaid source files remain editable and are retained in the manuscript directory.

## First full build and visual findings

- Build workflow: `Build semester manuscript` (GitHub Actions run 41189830446; artifact created 31 October 2026).
- First PDF: 31 A4 pages. First Word render: 40 pages.
- Four figure blocks were embedded and the authored captions appeared once (no duplicate automatic figure labels).
- Main-text Table 1 was divided into seven focused components: study identity, conditions, experimental endpoints, isotherm outputs, kinetic outputs, recovery/matrix evidence, and preparation/cost evidence.
- Page review found a placement defect in the original vertical Figure 2: its caption touched the page footer in PDF and was split onto the next page in DOCX.

## Figure 2 correction

Figure 2 has been redrawn as a compact left-to-right workflow: material sourcing/GO formation; surface modification/assembly; aqueous CIP/TC adsorption; recovery/regeneration; whole-process cost inventory; and functional-unit normalization. The scientific boundary is unchanged: it consolidates alternative reported routes and is not a standardized synthesis or measured mass balance.

**Status:** The updated Mermaid source and assembled manuscript are committed. The left-to-right build was rendered and reviewed: Figure 2 sits within its page, and its caption remains attached without footer collision.

## Content/claim safeguards

- Figure 1 remains a scope and eligibility map, not a PRISMA flow diagram.
- Figure 2 consolidates alternative preparation, treatment and recovery routes. It is not one standardized process or a measured mass balance.
- Figure 3 depicts candidate, non-exclusive, condition-dependent mechanisms. It does not assign quantitative contribution or prove a unique binding pathway.
- Figure 4 is a non-scoring decision framework. High adsorption performance alone does not demonstrate low cost.

## Table layout refinements following first page review

The main-text Table 1 has seven components. To reduce cell density further, Table 1C is limited to study ID, endpoint class and endpoint value; detailed study-specific caveats stay in the dedicated notes. Table 1D and 1E use separate rows for model type, parameter and fitted value rather than combining different fits in a single cell. Table 1F separates recovery/reuse from water-matrix evidence, and Table 1G separates preparation burden from cost evidence.

## Latest full-page manuscript review

The earlier nine-table rendering identified orphaned headings and split comparison tables. The final 2 November build adds explicit page-flow controls: PDF Tables 1A, 1B and 1C start on clean pages; Word Tables 1A, 1B and 1C each start on their own page. Table 1F is split into 1F(a) and 1F(b), reducing the qualification-column width problem. The final build and visual verification details are recorded below.

## Final production verification — 2 November 2026

- GitHub Actions run `41428502613` completed successfully from commit `85bd3cda83e6f4f8032292e3aa4187e01ef11170`; artifact ID `13133751051` (SHA-256 digest `6900102c8b8daead65d312aa89f142d61da7a8fa1d3b5c62ccc2e0ddccc1cc83`).
- PDF output: 31 A4 pages. Word output: 39 pages when rendered through LibreOffice.
- PDF table sequence: Table 1A page 15; 1B page 16; 1C page 17; 1D page 18; 1F(a)/(b) pages 19–20; 1H page 21; 1I pages 21–22.
- Word comparison layout: scope/reading note remains with the preceding narrative; Tables 1A, 1B and 1C start on pages 19, 20 and 21 respectively. The 28-row endpoint table fits on one page in both formats.
- Targeted visual inspection found no clipped or overlapping content in the revised comparison pages. Figure 2 remains within its page with its authored caption attached. All four figure panels and all ten visible Table 1 panels are in the artifact.
- PDF preflight: openable, text-searchable, unencrypted, no XFA, 31 A4 pages.
- DOCX accessibility audit: zero high- or medium-severity findings; 53 low-severity findings are raw DOI URLs used as bibliography link text.

## Still required before submission

1. Confirm the university-required citation style. ACS Guide 2026 remains provisional.
2. Render Supplementary Table S1 separately if the supervisor/university requires a separate supplement file.
3. Complete remaining sentence-level source-pin proof, language editing, author details, declarations, acknowledgements, funding/conflict/data availability statements and the submission checklist.
4. Keep all source caveats and study holds visible in the final copy.

## Compact Table 1 update (31 October 2026)

The main-text comparison is now divided into nine focused tables: 15 study identities; 19 condition vectors; 26 endpoint metric/value rows; 24 isotherm fit/parameter rows; 17 kinetic rows; 15 recovery rows; 15 matrix-validation rows; 15 preparation rows; and 15 cost-evidence rows. Endpoint rows contain one metric/value, while detailed caveats are retained in study-specific notes. A PDF-only page break before Table 1A is restored so the first table heading is not orphaned.
