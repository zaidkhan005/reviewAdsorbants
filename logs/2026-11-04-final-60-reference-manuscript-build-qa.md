# Final 60-reference manuscript build and QA — 4 November 2026

## Authoritative build

- **GitHub Actions run:** [41761643515 — successful](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41761643515)
- **Run/build-head commit:** `997ee0fe6f528dd815170d971f9be70b3b5e3c9d` (final workflow configuration; includes the 60-reference manuscript source and bibliography-path update).
- **Canonical manuscript source commit:** `30be3527b70a478a20a2e25df033ce8facbd4731`.
- **Bibliography input:** `semester-manuscript-cited-references-49-selected-plus-11-context.bib`.
- **Artifact:** `semester-manuscript-v2-acs-draft`, ID `13290887042`.
- **Artifact SHA-256:** `f0774f13e8b1125807700ca7f7cd847e3d5447b838c14b451b81d505e0631132`.
- **Artifact size:** 1,922,726 bytes; verified present and unexpired on 4 November 2026.
- **DOCX SHA-256:** `1472d96d224f8a0e1b3ba5e448208f988d3dd8b7f25ecef941f682bde086ea97`.
- **PDF SHA-256:** `5b3e40cf66f467c000558101d6cacbe41e0388094d8e9bb97d52db6a0aceaf24`.

## Current manuscript scope and citation reconciliation

| Control | Verified result |
|---|---:|
| Frozen selected works | 49 |
| Additional contextual references | 11 |
| Total bibliography entries | 60 |
| Unique BibTeX keys | 60 |
| Unique DOIs | 60 |
| Unique in-text citation keys | 60 |
| Missing bibliography keys | 0 |
| Unused bibliography entries | 0 |
| Claim-ledger groups | 94 |
| Selected-study IDs | 49, unchanged |
| Condition-labelled primary-study comparison | 15, unchanged |

The seven new contextual sources are Mnguni and Nomngongo (2026), Pryce et al. (2022), Gkika et al. (2025), Tzatzadakis et al. (2026), Ge et al. (2021), Wurzer et al. (2023), and Viegas et al. (2020). They support contextual statements about cost-estimation methods, graphene/rGO production burdens, treatment-system costs and spent-carbon management. None is promoted to the selected empirical evidence set or used as new CIP/TC adsorption-capacity evidence. See the [contextual-reference expansion log](2026-11-04-contextual-reference-expansion.md).

## Output and technical checks

| Check | Result |
|---|---:|
| PDF pages | 50 |
| DOCX pages (LibreOffice render) | 60 |
| Page geometry | A4 portrait, 22 mm margins |
| PDF text | Searchable |
| PDF encryption | None |
| PDF XFA | None |
| PDF preflight warnings | 0 |
| PDF outline/bookmark entries | 57 |
| PDF link/annotation entries | 86 |
| Native Office Math objects | 315 |
| DOCX bibliography paragraphs protected with keep-lines-together | 60 |
| Figure count / descriptive alternative text | 5 / 5 |
| Table count / header-row markers | 13 / 13 |
| Replacement-square / invalid-glyph paragraphs | 0 |
| High / medium DOCX accessibility findings | 0 / 0 |
| Low DOCX accessibility findings | 60 |

All 60 bibliography entries appear in the rendered Word document in a consecutive numbered sequence (1–60). The seven new sources are present in the rendered bibliography. The final PDF likewise includes references 1–60. The new PDF has 50 searchable A4 pages; the DOCX rendering has 60 A4 pages.

All 60 low-severity DOCX accessibility findings are raw DOI URLs used as bibliography hyperlink display text. The audit found no high- or medium-severity accessibility issue. All five embedded figures have descriptive alternative text, and all 13 tables have marked header rows. Core Word metadata (title/author/keywords) remains blank pending the confirmed author list and affiliation details.

The PDF is searchable and bookmarked but does not contain a tagged-PDF structure tree. It should not be described as PDF/UA-conformant. If the institution or target journal requires a tagged PDF, that needs a separate tagged-PDF production and validation step.

## Visual review

- Contact sheets were generated and reviewed across all 50 PDF pages and all 60 DOCX-render pages.
- Full-size inspection included the expanded-cost discussion page (PDF p. 3), the complete final bibliography page (PDF p. 50), and the updated Word reference pages (pp. 57–60).
- No clipping, overlapping text, broken glyphs, missing figures, or split bibliography entries were observed in the reviewed outputs.
- All 60 Word bibliography paragraphs have keep-lines-together formatting.

## Scientific and editorial integrity

- The 49-work selection, the 15-study condition-labelled comparison, all 94 claim groups, and the established scientific holds were retained.
- The new references are used as contextual/methodological sources only. Their cost and life-cycle figures are not represented as directly comparable to CIP/TC-specific process costs.
- The expanded manuscript explicitly distinguishes material-synthesis prices, life-cycle environmental indicators, system-level cost per treated volume, and lab-scale cost per mass of antibiotic removed.
- ACS Guide 2026 remains provisional pending AMU/supervisor or target-journal confirmation.
- This remains a working draft, not submission approval.

## Supersession

This 60-reference build supersedes the 4 November 53-reference artifact documented in [the earlier language-edited build QA log](2026-11-04-language-edited-final-build-qa.md). Use Actions run 41761643515 and the hashes above for the current working files.
