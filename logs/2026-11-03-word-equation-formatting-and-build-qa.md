# Word equation formatting correction and final manuscript build QA — 3 November 2026

## Build identity

- Corrected build: [GitHub Actions run 41682709331](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41682709331), completed successfully.
- Source commit: `60cffe8f58724b2755de53ca4236708896d459cd`.
- Artifact ID: `13253501547`; artifact name: `semester-manuscript-v2-acs-draft`.
- Artifact SHA-256: `00ab783d2479efc1d2e86413927fcb0a997d04441a00ea1ad690b0b69d62ad73`.
- Output files: `SEMESTER_MANUSCRIPT_V2_ACS_DRAFT.docx` and `SEMESTER_MANUSCRIPT_V2_ACS_DRAFT.pdf`.

## Issue found and corrected

A cross-format render check showed that the PDF correctly typeset the equations in the SEM-010 dose-basis discussion, but the DOCX displayed literal backslash-parenthesis delimiters in two passages. The assembled source contains ten double-escaped inline-math spans. The DOCX-only preparation stage now normalizes those delimiters and any doubled TeX command escapes before Pandoc conversion; the PDF preparation path is unchanged.

The corrected DOCX contains **308 native Office Math objects** and **zero literal inline-math opening or closing delimiters** in `word/document.xml`. The SEM-010 expressions for the Langmuir-fitted `qmax`, observed kinetic `qe`, fitted PSO `qe`, and derived dose-basis calculation render as Word equations rather than source markup.

An initial invalid build-script edit failed at syntax validation before artifact upload. The script was restored from the last working version and the normalization was reapplied as a separate, verified insertion. The corrected commit and build above are the authoritative production result.

## Output QA

- PDF: 48 A4 pages, searchable and unencrypted.
- DOCX: 59 A4 pages with explicit 22 mm margins.
- The regenerated PDF's extracted text is byte-for-byte identical at the text-output level to the previous successful 48-page PDF from run 41680138826; the Word-only fix did not alter PDF content.
- All 59 DOCX pages were rendered and contact-sheet reviewed. The SEM-010 paragraph was inspected at full size after the correction; the table pages, Table 2 notes, figures and References pages were visually reviewed for pagination/layout issues.
- No visible clipping, overlapping objects, broken figures or missing table content was found. The dense comparison tables keep conditions, observed endpoints, fitted outputs, regeneration, matrix validation and cost limitations in separate columns/panels.

## Content and scope control

- No study selection, adsorption value, evidence tier, citation key or scientific conclusion was changed by this production fix.
- The selected set remains 49 works; four contextual references remain outside it; the consolidated bibliography remains 53 entries.
- SEM-010 retains the reported 99% removal, experimental kinetic `qe=78.82 mg/g`, PSO-fitted `qe=79.36 mg/g`, separate Langmuir `qm`, and the unresolved 20 mg/L versus 20 g/L source conflict. The ~25 mg/L alternative remains a derived possibility only; no source value was silently corrected.
- ACS Guide 2026 is still provisional pending AMU/supervisor confirmation. Scientific source-pin coverage, language editing, author declarations and the institutional submission checklist remain outstanding.



## Follow-up correction after full-manuscript integration — 3 November 2026

The first Word math correction above addressed the earlier SEM-010 double-escaped inline expressions. The subsequent full-manuscript integration introduced other formula groups that were written as standalone empty-base subscript/superscript fragments (e.g., `\(_2\)`, `\(_4\)`, `\(_n\)`, `\(^3\)`, `\(^{-}\)`). LibreOffice displayed square placeholders for these fragments in the first integrated DOCX render.

The assembled Markdown source was corrected to use complete expressions for MnFe₂O₄, TiO₂, NH₂, Fe₃O₄, Pr₆O₁₁, cm³, CO₂ and COO⁻. A post-edit scan found zero remaining empty-base fragments.

**Authoritative latest production build:** [GitHub Actions run 41691972025](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41691972025), source commit `a7ae064028cee61bfaefa81705148b53f7eae56f`, successful. Artifact `semester-manuscript-v2-acs-draft`, ID `13258235067`, SHA-256 `c9c8516f8b3de049eb98527ed921b1d95db0e65516d15aa3fd916790ac412721`, expires 3 December 2026.

- PDF: 48 searchable, unencrypted A4 pages.
- DOCX: A4 portrait, 22 mm margins; LibreOffice rendering yields 58 pages.
- Document XML: 312 native Office Math objects; no literal inline-math delimiters and no replacement-square character.
- The formerly affected DOCX render pages 17, 30, 32, 33 and 34 were inspected at full size after correction. Contact sheets of all 58 DOCX-render pages and all 48 PDF pages were visually reviewed.
- No obvious clipping, overlap, broken table or missing figure was seen in the reviewed pages.

The 58-page DOCX render and 48-page PDF have different pagination because they are separate rendering paths. Both outputs remain working-draft production files; ACS 2026 is provisional pending AMU/supervisor confirmation and final editorial/institutional sign-off remains outstanding.
