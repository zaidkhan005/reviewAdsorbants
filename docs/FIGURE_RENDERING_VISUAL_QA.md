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

Figure 2 has been redrawn as a left-to-right workflow with six linked stages: material sourcing/GO formation; surface modification/assembly; aqueous CIP/TC adsorption; recovery/regeneration; whole-process cost inventory; and functional-unit normalization. The scientific boundary is unchanged: it consolidates alternative reported routes and is not a standardized synthesis or measured mass balance.

**Status:** The updated Mermaid source and assembled manuscript are committed. The refreshed DOCX/PDF build is in progress; final figure-placement status is pending visual review of that artifact.

## Content/claim safeguards

- Figure 1 remains a scope and eligibility map, not a PRISMA flow diagram.
- Figure 2 consolidates alternative preparation, treatment and recovery routes. It is not one standardized process or a measured mass balance.
- Figure 3 depicts candidate, non-exclusive, condition-dependent mechanisms. It does not assign quantitative contribution or prove a unique binding pathway.
- Figure 4 is a non-scoring decision framework. High adsorption performance alone does not demonstrate low cost.

## Still required before submission

1. Inspect the refreshed Figure 2 placement in the final PDF and Word outputs; confirm that caption and footer do not overlap and the caption stays with the figure.
2. Complete page-by-page review of the complete refreshed DOCX/PDF, including all table splits, figure captions, citation placement and references.
3. Confirm the university-required citation style. ACS Guide 2026 is only the current provisional build style.
4. Render Supplementary Table S1 separately if the supervisor/university requires a separate supplement file.
5. Complete language proof, authorship details, declarations, acknowledgements and submission checklist.