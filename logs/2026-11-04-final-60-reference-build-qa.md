# Final 60-reference manuscript build and QA — 4 November 2026

## Authoritative production build

- **GitHub Actions run:** [41762141686 — successful](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41762141686)
- **Source commit:** `82e47d1c85912159858a4b0d053e3048fe8c4395`
- **Artifact:** `semester-manuscript-v2-acs-draft`
- **Artifact ID:** `13290473226`
- **Artifact SHA-256:** `6a99f2576d777d5a2b6cf9cf8f4631f49f93be7dcbdb8610c105d4dada5cf82c`
- **Artifact expiry:** 4 December 2026
- **DOCX SHA-256:** `9645308ac946ef009b88a22a99bbd7af9fff80dbd3592006b53d4d28c814015c`
- **PDF SHA-256:** `eeb830df8877aaa85205f2f9d3da3662be0d807a12142028e9c444cde2db9a7a`

## Output files and technical preflight

| Check | Result |
|---|---:|
| Word document | 60 A4 pages |
| PDF | 50 A4 pages |
| PDF encryption | None |
| PDF text extraction | Searchable |
| PDF bookmarks/outlines | 57 |
| PDF annotations/links | 86 |
| PDF form fields | 0 |
| PDF attachments | 0 |
| PDF tagged structure | Not present |
| Word accessibility high / medium / low findings | 0 / 0 / 60 |
| Word embedded figures | 5 |
| Figures with non-empty descriptive alternative text | 5 |
| Word tables | 13 |
| Tables with first row marked as header | 13 |
| Word replacement-square / invalid-glyph findings | 0 |
| Word raw DOI URL accessibility findings | 60 |

All 60 low-severity Word accessibility findings are bibliography hyperlinks whose visible display text is a raw DOI URL. The audit found no high- or medium-severity findings.

The PDF is openable, searchable, bookmarked and A4, but the PDF catalog has no tagged-PDF structure tree. It should not be described as PDF/UA-conformant or as a fully tagged accessible PDF. The Word document has semantic heading styles, descriptive image alt text and table-header row markup. Core document properties for title/author remain blank pending confirmation of the author list and metadata.

## Visual review and pagination

- Contact sheets were reviewed across all 60 Word-render pages and all 50 PDF pages. Dense, changed and critical pages were also opened at full size, including the new contextual-reference content and final bibliography pages.
- The last Word page displays references 47–60 as intact bibliography entries; the final PDF page displays references 55–60. No visible clipping, overlap or broken table content was identified in the reviewed pages.
- The current run's DOCX differs from the fully rendered comparison DOCX only in `docProps/core.xml`; the document XML, styles, numbering, relationships and embedded content are byte-identical. Thus the reviewed Word pagination/content is unchanged in the current build.
- The extracted PDF text is byte-identical to the comparison 60-reference build, and the side-by-side 50-page render comparison reported zero changed pages. The final file itself was independently preflighted after download.
- All seven newly added DOI strings are present in extracted final PDF text, including Ge et al.'s verified DOI `10.15244/pjoes/125561`.

## Bibliography and scientific integrity

- **60 bibliography records:** 49 selected works plus 11 contextual references.
- **Selected studies:** 49 unique DOI-defined works; selection remains frozen.
- **Condition-labelled comparison:** 15 primary studies; unchanged.
- **Claim ledger:** 94 unique claim groups; unchanged.
- **Citation linkage:** 60 unique in-text keys, 60 unique bibliography keys and 60 unique DOI values; zero missing or unused keys.
- The seven added references provide background or methodological context on cost-estimation methods, graphene/rGO production burdens, treatment-system costing and spent-media management. They are not added to the empirical selected-study set and are not used to supply CIP/TC adsorption-performance values.
- The Ge et al. N-rGO life-cycle assessment DOI was verified against the publisher PDF and restored to `10.15244/pjoes/125561` before this build.

The new GO/rGO life-cycle production reference reports laboratory-scale energy estimates of approximately 25 kJ/g for GO and 61 kJ/g for rGO; these are production-energy indicators, not monetary treatment costs. <https://doi.org/10.1021/acsomega.5c09672>

## Remaining submission decisions

This is now the current **60-reference working build**, not a submission-approved final. The destination-specific citation style remains provisional. Author names/order, affiliations, corresponding author, acknowledgements, funding, conflict-of-interest, data-availability and any required author-contribution statements still need confirmation. The existing scientific holds and source-access qualifications remain in place.

See the [submission-readiness checklist](../docs/SEMESTER_MANUSCRIPT_SUBMISSION_READINESS_CHECKLIST.md), [contextual reference expansion log](2026-11-04-contextual-reference-expansion.md), and [updated file index](../docs/SEMESTER_MANUSCRIPT_FILE_INDEX.md).
