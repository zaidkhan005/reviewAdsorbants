# Final manuscript proofread and production QA — 4 November 2026

## Scope

This proofread pass continued from the canonical assembled V2 manuscript. It focused on sentence-level clarity, paragraph flow, terminology, table pagination and final document rendering. It did not reopen or change the frozen scientific evidence base.

## Editorial changes

1. **Study-by-study paragraph flow.** Dense summaries in Sections 3.1–3.6.4 and practical-feasibility discussion in Sections 5.2–5.3 were divided into shorter study-specific paragraphs. Citations were retained with the paragraph describing the corresponding study.
2. **Duplicated result consolidated.** The rGO/Pr6O11 CIP discussion by Panda et al. now presents removal, derived uptake, observed uptake at the tested concentrations, fitted Langmuir parameters, pH qualification, matrix scope and reuse evidence in one study-specific account. Repetition between Sections 3.6.4 and 5.3 was removed without dropping the matrix or recovery information.
3. **Terminology and notation.** First-use expansions now include TET (tetracycline) and GO–SA (GO–sodium alginate), in addition to the earlier terminology pass. Technical symbols and units were normalized where appropriate, including sp2 to sp², m3 to m³ and leading zeros for reported R² values.
4. **Search-flow figure.** Figure 2 now visibly connects the contextual-reference branch to the focused search overview without suggesting that contextual references passed the primary-study eligibility gate.
5. **Table-note economy.** The Table 2 note for Yasmin et al. (2024) was shortened. The full dose-basis calculation and unresolved 20 mg/L versus 20 g/L source conflict remain in Section 3.1.
6. **Table 2E pagination.** The Shaha et al. (2025) kinetic-model value that previously wrapped onto the following page has been shortened to the defined table notation `NR`. Its source-availability qualification is unchanged.
7. **Math in both output formats.** The build script now normalizes the ten intentional double-escaped Yasmin inline-math spans for both DOCX and PDF. The preceding build correctly normalized Word equations but left literal backslashes in the PDF. The final build fixes both paths and retains an exact-count check.

## Scientific and citation integrity

- Selected works: 49 (unchanged).
- Additional contextual references: 11 (unchanged).
- Total bibliography: 60 entries.
- Unique in-text citation keys: 60.
- Missing citation keys: 0.
- Unused bibliography keys: 0.
- DOI fields: 60; unique DOI values: 60.
- ACS short-journal fields: 60 across 40 distinct journal titles.
- Claim groups: 94 (unchanged).
- Condition-labelled primary-study comparison: 15 studies (unchanged).
- Critical holds for SEM-010, SEM-038, SEM-046, SEM-050 and SEM-051 remain preserved.

No study was added to or removed from the selected set. No evidence value, experimental condition, source-access tier or cost estimate was changed by this editorial pass.

## Final successful production build

- **Latest successful bibliography/production build:** [GitHub Actions run 41786667974](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41786667974)
- **Build source commit:** `82d6e76df2c9c2c4729482a31ff2930482f8d70e`
- **Artifact ID:** `13302025655`
- **Artifact name:** `semester-manuscript-v2-acs-draft`
- **Artifact SHA-256:** `439b3ff431b430e17532f806019180e1b903acbb7a8d7e46b4df11f2255274e1`
- **Artifact expiry:** 4 December 2026

### Generated files

- DOCX: `SEMESTER_MANUSCRIPT_V2_ACS_DRAFT.docx`; 60 A4 pages; SHA-256 `36422875dc9505b73ec88b0b2fba796b41e9acf0e2ee3b71166198b01cd1fddf`.
- PDF: `SEMESTER_MANUSCRIPT_V2_ACS_DRAFT.pdf`; 50 searchable, unencrypted A4 pages; SHA-256 `a2d61bef6ee6398f18743ab778e5575ca700e0f54154962010d7080d4c0617ef`.
- ZIP package SHA-256: `439b3ff431b430e17532f806019180e1b903acbb7a8d7e46b4df11f2255274e1`.

## Visual and technical QA

- DOCX independently rendered to 60 A4 page images.
- PDF independently rendered to 50 A4 page images.
- The final PDF page 9 was inspected at full size: the Yasmin mass-balance equations now render as mathematics, not literal escaped delimiters.
- DOCX page 23 was inspected at full size: Table 2D and the Table 2E kinetic rows remain readable; the Shaha et al. row ends with `NR` on the same page rather than splitting an orphan phrase to the next page.
- PDF pages 23 and 49–50 were inspected at full size. The bibliography runs sequentially through references 36–60, with the final three entries on page 50. DOI links remain present and searchable.
- The PDF text extraction contains no remaining literal `\\(` inline-math markers.
- PDF metadata: 50 pages; A4; unencrypted; 57 outline items; 83 annotations; no forms or attachments.
- The PDF has no tagged-PDF structure tree and is **not PDF/UA-conformant**.
- The earlier DOCX structure/accessibility audit found 0 high, 0 medium and 60 low findings; the low findings are raw DOI URL hyperlink display text. The prose/table edits did not introduce a known high- or medium-severity accessibility issue.

## Remaining qualifications and submission blockers

- ACS numbered/superscript references remain the working bibliography style, pending AMU/supervisor confirmation. The CASSI audit found exact publication records for 30 of 40 distinct journal titles. Two abbreviations were corrected and are applied consistently to every corresponding article record. Ten short forms remain provisional because exact CASSI records were not located in the accessible result set; this does not prove that the titles are absent from CASSI. See `logs/2026-11-04-cassi-and-amu-format-audit.md`.
- AMU's public Department of Chemistry page lists B.Sc. Chemistry syllabus/curriculum information but no applicable semester-review manuscript style or citation rule. Department/supervisor confirmation remains outstanding.
- Author names/order, affiliations, corresponding author, acknowledgements, funding, competing-interest, data-availability and any required author-contribution declarations still require author confirmation.
- This is a proofread working draft, not an institutionally approved submission final. The PDF should not be described as PDF/UA-conformant.

The prior bibliography/layout, table-readability and terminology audits remain in the dated logs linked from the current manuscript file index.
