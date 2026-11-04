# Final technical terminology and editorial QA — 4 November 2026

## Scope

This checkpoint follows the ACS bibliography and Word-layout refinement. It applies a targeted terminology pass to the canonical manuscript source `manuscript/SEMESTER_MANUSCRIPT_ASSEMBLED_SOURCE_V2.md`. It does not reopen source evidence, modify numerical values, change the frozen study set, or add/remove references.

## First-use terminology and model definitions

The following abbreviations and technical terms were clarified at or before first reader-facing use:

- NOM — natural organic matter.
- RSM — response surface methodology.
- DMF — N,N-dimethylformamide.
- DTPA — diethylenetriaminepentaacetic acid.
- CMC — carboxymethyl cellulose.
- PES — polyethersulfone.
- TOC — total organic carbon.
- PVA — poly(vinyl alcohol).
- DFT — density functional theory.
- SMX — sulfamethoxazole.
- EDTA — ethylenediaminetetraacetic acid.
- GO–TOPO:LevA — graphene oxide modified with trioctylphosphine oxide and levulinic acid.
- FITC — fluorescein isothiocyanate.
- FTIR — Fourier-transform infrared spectroscopy.
- XPS — X-ray photoelectron spectroscopy.
- MD — molecular dynamics.
- PFO/PSO — pseudo-first-order/pseudo-second-order kinetic models.
- D–R — Dubinin–Radushkevich model.
- The preparation table spells out triethylenetetramine rather than leaving TETA unexplained.
- Figure 1 spells out carbon nanotubes and metal–organic framework before the abbreviations CNTs and MOF.

The PGOT@GEL primary article identifies TETA as triethylenetetramine; the current wording follows that source. See https://www.sciencedirect.com/science/article/pii/S0957582025009267. The Peng et al. full-text article identifies FITC as fluorescein isothiocyanate; see https://pmc.ncbi.nlm.nih.gov/articles/PMC4989150/.

The first-use check also retains earlier expansions for CIP, TC, GO, rGO, SGO, CNF, PRB, TCH, OFL, DTPA, CMC, PES, RSM, DMF, NOM and TOC. The prose and table guide define PFO/PSO before their first kinetic-table use, and the mechanism section defines D–R at first use.

## Build and production

- **Successful GitHub Actions run:** [41781818385](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41781818385).
- **Source commit:** `9b66056e68bacff4c664de1db7c3f7492c73d40c`.
- **Artifact:** `semester-manuscript-v2-acs-draft`; artifact ID `13299198981`.
- **Artifact SHA-256:** `25e1bca7dfae75bad2d98d6fd93c38d324ebe701ad8b3ca951b5b882b411036c`.
- **Artifact expiry:** 4 December 2026.
- **DOCX:** 60 A4 pages; SHA-256 `f7e6ce272e0555ef08aec18b905dbbeb83d1cf5a478119ef20e34d0b08db36d7`.
- **PDF:** 50 searchable, unencrypted A4 pages; SHA-256 `3e5c32b86174bcd241575cef5eeb5cdfa342194339dd8432470e92bbca95db16`.

The PDF was extracted and checked for the new terminology, the References heading, and final reference (60). The DOCX was independently rendered to a 60-page A4 PDF. The previous page-level visual review of the bibliography remains applicable: references are sequentially numbered, whole paragraphs are kept together, and wrapped lines align under the reference text. The new definitions do not alter evidence tables or bibliography membership.

## Integrity checks

- 60 bibliography entries and 60 unique Better BibTeX keys.
- 60 unique in-text citation keys.
- Zero missing or unused citation keys.
- 60 DOI fields and 60 unique DOI values.
- 60 short-journal fields across 40 journal titles.
- 49 selected works plus 11 contextual references.
- 15-study condition-labelled comparison unchanged.
- 94 claim groups unchanged.
- No new adsorption value, operating condition, source tier, study selection or cost estimate was introduced by this terminology pass.

## Remaining qualifications

ACS numeric/superscript formatting, abbreviated journal titles, DOI links and Word hanging indents are applied in the working output. The 40 short journal titles are CASSI-style; individual CASSI verification for every title and AMU/supervisor confirmation of the required citation format remain outstanding. The PDF is searchable and unencrypted but has no tagged-PDF structure and must not be described as PDF/UA-conformant.

This is still a working manuscript, not an institutionally approved submission final. Author names/order, affiliations, corresponding author, acknowledgements, funding, competing-interest, data-availability and any required author-contribution declarations remain to be confirmed. A final author/supervisor read-through after the intended institutional template is applied also remains advisable.
