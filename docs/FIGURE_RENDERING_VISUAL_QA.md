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

**Status:** The updated Mermaid source and assembled manuscript are committed. The left-to-right build was rendered and reviewed: Figure 2 sits within its page, and its caption remains attached without footer collision. A further final build is underway after the additional Table 1C–1E cell reduction/model-row split; its final page placement is pending.

## Content/claim safeguards

- Figure 1 remains a scope and eligibility map, not a PRISMA flow diagram.
- Figure 2 consolidates alternative preparation, treatment and recovery routes. It is not one standardized process or a measured mass balance.
- Figure 3 depicts candidate, non-exclusive, condition-dependent mechanisms. It does not assign quantitative contribution or prove a unique binding pathway.
- Figure 4 is a non-scoring decision framework. High adsorption performance alone does not demonstrate low cost.

## Table layout refinements following first page review

The main-text Table 1 has seven components. To reduce cell density further, Table 1C is limited to study ID, endpoint class and endpoint value; detailed study-specific caveats stay in the dedicated notes. Table 1D and 1E use separate rows for model type, parameter and fitted value rather than combining different fits in a single cell. Table 1F separates recovery/reuse from water-matrix evidence, and Table 1G separates preparation burden from cost evidence.

## Latest full-page manuscript review

The latest nine-table rendering (before the final page-break patch) produced a 30-page PDF and a 39-page DOCX when rendered through LibreOffice. The left-to-right Figure 2 fits within its page and its caption stays with the image. Table 1F and 1G are legible with the added columns, although some qualifications wrap over several lines. Two pagination issues were found: Table 1A began with two rows at the bottom of the preceding page, and the Table 1D heading was left at the foot of the prior page. Cross-format page breaks (LaTeX `\\newpage` for PDF and raw OpenXML page breaks for DOCX) have now been committed before both headings. The latest build must confirm that the breaks work in both outputs.

## Still required before submission

1. Inspect the refreshed Figure 2 placement in the final PDF and Word outputs; confirm that caption and footer do not overlap and the caption stays with the figure.
2. Complete page-by-page review of the complete refreshed DOCX/PDF, including all table splits, figure captions, citation placement and references.
3. Confirm the university-required citation style. ACS Guide 2026 is only the current provisional build style.
4. Render Supplementary Table S1 separately if the supervisor/university requires a separate supplement file.
5. Complete language proof, authorship details, declarations, acknowledgements and submission checklist.

## Compact Table 1 update (31 October 2026)

The main-text comparison is now divided into nine focused tables: 15 study identities; 19 condition vectors; 26 endpoint metric/value rows; 24 isotherm fit/parameter rows; 17 kinetic rows; 15 recovery rows; 15 matrix-validation rows; 15 preparation rows; and 15 cost-evidence rows. Endpoint rows contain one metric/value, while detailed caveats are retained in study-specific notes. A PDF-only page break before Table 1A is restored so the first table heading is not orphaned.
