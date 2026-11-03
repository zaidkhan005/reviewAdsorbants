# Final language-edited manuscript build and QA — 4 November 2026

## Authoritative build

- **GitHub Actions run:** [41718042264 — successful](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41718042264)
- **Source commit:** `ef2b1de98fe4d25c1a05a02bda11d504296e558d`
- **Artifact:** `semester-manuscript-v2-acs-draft`
- **Artifact ID:** `13270582585`
- **Artifact SHA-256:** `97a1ac75e8ea008bdb52db46c65844e9600975705c770580b9a0bad99517f538`
- **Artifact expiry:** 3 December 2026
- **DOCX SHA-256:** `6c324b976cdd0d7f777f3852cc1e3eec841e0fabb68aa2a79f9af4d430520526`
- **PDF SHA-256:** `9b14bb583f729368f11d95a705acc26b021dd3bd1fda1b278f41f27e75dbfaa2`

## Final production checks

| Check | Result |
|---|---:|
| Word render | 60 A4 pages |
| PDF render | 48 A4 pages |
| PDF encryption | None |
| PDF text extraction | Searchable |
| Native Office Math objects in DOCX | 315 |
| Replacement-square / invalid-glyph paragraphs in DOCX | 0 |
| Literal inline-math delimiters in DOCX text | 0 |
| Word bibliography paragraphs marked keep-lines-together | 53 |
| In-text citation keys | 53 |
| Bibliography entries | 53 |
| Missing / unused bibliography keys | 0 / 0 |
| Claim-ledger rows / unique IDs | 94 / 94 |
| Selected-study records / unique IDs | 49 / 49 |

The final bibliography title is rendered as **NH2-UiO-66(Zr)**. The source uses a plain-text NH2 fragment and protected BibTeX capitalization for Zr, avoiding the square placeholder previously visible in the Word render.

## Final visual review

The 60-page Word render and 48-page PDF render were reviewed as page contact sheets. Full-size page inspections included the dense experimental-condition table (Word p. 21), preparation-burden table (Word p. 27), the final bibliography pages (Word pp. 59–60), and the final PDF references page (PDF p. 48).

A final layout defect was found and corrected: Word reference 46 previously broke between pages 59 and 60. The build script now adds `w:keepLines` to each bibliography paragraph. In the final render, page 59 ends after reference 45 and all of reference 46 appears together at the top of page 60, followed by references 47–53. No reference is split across pages.

The final PDF reference section retains reference 46 as a complete entry on page 48. The DOCX/PDF contact sheets show the tables, diagrams, appendix, and bibliography within the page boundaries without visible clipping or overlap.

## Scientific and editorial integrity

The language-edited source remains the canonical manuscript. The build-script change affects Word pagination only. The bibliography-title edit affects capitalization/rendering only; it did not change the Amin citation key, author list, DOI, journal, volume, pages, year, or in-text citations.

The final reconciliations remain:
- 94 claim groups, with all claim IDs intact;
- 49 selected works;
- 53 bibliography records and 53 unique in-text citation keys;
- no missing or unused citation keys;
- no changes to the evidence ledger or selected-study membership during the language pass.

## Submission status

This remains a **working draft**, not submission-ready. ACS Guide 2026 is provisional until AMU/supervisor confirmation. Author information, acknowledgements, funding, conflict-of-interest and data-availability declarations, and the institutional submission checklist remain to be completed. The scientific qualifications and source-access holds remain in place; visual build success is not scientific sign-off.
