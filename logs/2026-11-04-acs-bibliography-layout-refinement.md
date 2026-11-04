# ACS bibliography and Word-layout refinement — 4 November 2026

## Scope

This pass refines the verified 60-reference working build without changing the manuscript's scientific content, selected-study membership, claim ledger, or evidence values. The canonical manuscript remains `manuscript/SEMESTER_MANUSCRIPT_ASSEMBLED_SOURCE_V2.md`; the active bibliography remains `semester-manuscript-cited-references-49-selected-plus-11-context.bib`.

## Changes committed

1. **Word numbered-reference alignment.** The build script now applies a 0.5-inch hanging indent and explicit tab stop to bibliography paragraphs. This keeps each reference number in the left margin and aligns wrapped author/title/journal/DOI lines with the entry text. Each reference paragraph remains protected with keep-lines-together.
2. **Journal short-title fields.** The BibTeX input now carries a `shortjournal` field for every one of the 60 bibliography records, covering 40 distinct journal titles. The full journal-title field is retained in every record. The ACS CSL renderer uses the short form consistently.
3. **OOXML property order.** A follow-up correction ensures the Word paragraph tab-stop element precedes the indentation element in the paragraph properties, as required for the intended Word document structure.

These changes affect reference presentation only. All 60 records, citation keys, DOI fields and article metadata remain in the bibliography source.

## Production build

- **GitHub Actions run:** [41772042785 — successful](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41772042785)
- **Final source commit:** `24f87ecf4a3d343f9bce9ee85ab44eb5b0874bd8`
- **Artifact:** `semester-manuscript-v2-acs-draft`; artifact ID `13295043105`
- **Artifact SHA-256:** `5cd7300858a95091ba66d684fd408e1862978c813dd4e1bfade039f92f64d428`
- **Artifact expiry:** 4 December 2026
- **DOCX:** 60 A4 pages; SHA-256 `4a7ac9592245f156810144804842b686f7a85bf6980b78fbbd13fb3654c2b26f`
- **PDF:** 50 A4 pages; SHA-256 `677942f682f0464ced04685e5cc39ed085676fc1e81d8ea055f92ca93af91795`

## Verification

- GitHub Actions build and artifact upload completed successfully.
- The final DOCX was rendered independently to 60 page images. All 60 pages were reviewed in contact sheets; the detailed Table 3/citation pages and the four bibliography pages were inspected at full size.
- The DOCX renders pixel-identically to the preceding ACS-refined build; the final change after that build corrected paragraph-property ordering without changing visible page layout.
- The bibliography occupies the end of the Word document, with references 1–60 sequentially numbered and no split reference paragraphs. The hanging-indent alignment is visible on the final bibliography pages.
- The final PDF was independently rendered to 50 pages and reviewed in contact sheets, with the final bibliography page inspected at full size. It remains searchable and unencrypted, with 57 outline items and 83 annotations/links.
- PDF text extraction returned approximately 149,000 searchable characters; the References section and final reference 60 are present.
- Bibliography linkage check: 60 unique BibTeX keys; 60 unique manuscript citation keys; zero missing and zero unused keys; 60 DOI fields and 60 unique DOI values.
- Word accessibility audit: **0 high, 0 medium, 60 low** findings. All 60 low findings are raw DOI URLs used as hyperlink display text. No high- or medium-severity issue was identified.
- The previous QA's figure and table checks remain applicable: five figures have descriptive alternative text and all 13 tables have a marked header row.
- The PDF remains searchable and bookmarked but is **not tagged** and should not be described as PDF/UA-conformant.

## ACS/CASSI qualification

The bibliography uses the repository's ACS Guide 2026 numeric/superscript CSL, with article titles, bold years, italic journal titles/volumes, page or article numbers, and DOI links. The 60 records now have consistent short journal-title fields. The short forms are CASSI-style editorial abbreviations; this pass did **not** independently certify every one of the 40 distinct titles against an individual CASSI record. The CAS CASSI Search Tool is the authoritative lookup source and states that its database was updated on 25 October 2026: https://cassi.cas.org/about.jsp. For strict journal-specific publication formatting, verify each short title against CASSI and the chosen journal's current author instructions. The AMU/supervisor requirement also remains to be confirmed.

## Status and remaining submission blockers

This is the latest **ACS-refined 60-reference working build**, not an institutionally approved submission final. Remaining decisions are author names/order and affiliations, corresponding author, declarations, AMU/supervisor formatting approval, and final target-specific proofing. Existing scientific holds and access qualifications remain unchanged.
