# Submission-readiness checkpoint — 4 November 2026

## Purpose and boundary

This checkpoint follows the successful 4 November 2026 60-reference production build. It assesses the remaining author, institutional and publication-finalization work. It does **not** repeat the scientific source audit, change the frozen study selection, or treat successful file generation as scientific or institutional approval.

The canonical manuscript source remains `manuscript/SEMESTER_MANUSCRIPT_ASSEMBLED_SOURCE_V2.md`. The GitHub repository remains the project source of truth.

## Authoritative production snapshot

- Branch: `main`.
- Latest successful build: [GitHub Actions run 41786667974](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41786667974).
- Build source commit: `82d6e76df2c9c2c4729482a31ff2930482f8d70e`.
- Artifact: `semester-manuscript-v2-acs-draft`, ID `13302025655`; SHA-256 `439b3ff431b430e17532f806019180e1b903acbb7a8d7e46b4df11f2255274e1`. Verified present and unexpired on 4 November 2026; expiry 4 December 2026.
- DOCX: 60 A4 pages; SHA-256 `36422875dc9505b73ec88b0b2fba796b41e9acf0e2ee3b71166198b01cd1fddf`.
- PDF: 50 searchable, unencrypted A4 pages; SHA-256 `a2d61bef6ee6398f18743ab778e5575ca700e0f54154962010d7080d4c0617ef`.
- Integrity totals: 94 claim groups; 49 selected works; 11 contextual references; 60 bibliography entries and 60 unique in-text citation keys; 60 unique DOI values; zero missing or unused keys.
- The Word and PDF pipelines both normalize the ten intentional inline-math spans in the Yasmin dose-basis discussion. Page 9 of the final PDF was inspected and shows correctly typeset equations; no literal escaped delimiters remain.
- Word pagination: the Shaha et al. (2025) kinetic-table value uses the defined `NR` notation so the row remains together. Table 2 retains separate panels for conditions, measured/modelled endpoints, regeneration, matrices, preparation and cost evidence.
- The Word build applies numbered-reference hanging indents and tab stops. The consolidated bibliography has short-journal fields for all 60 records across 40 journal titles.
- CASSI audit: exact publication records were confirmed for 30 of 40 distinct journal titles in accessible CASSI results. Chemical Engineering Journal is consistently formatted as `Chem. Eng. J. (Amsterdam, Neth.)` in both article records; Environmental Pollution uses `Environ. Pollut. (Oxford, U. K.)`. Ten short forms remain provisional pending direct title/ISSN lookup in the interactive CASSI tool. See [CASSI and AMU-format audit](../logs/2026-11-04-cassi-and-amu-format-audit.md).
- AMU format: the public Chemistry undergraduate page lists syllabus/curriculum resources but no applicable BSc semester-review template or citation-style rule. ACS remains a working format pending department/supervisor confirmation.
- The final source-level proofread and CASSI corrections are recorded in [the 4 November final proofread QA](../logs/2026-11-04-final-proofread-qa.md) and [CASSI/AMU-format audit](../logs/2026-11-04-cassi-and-amu-format-audit.md).
- Accessibility: the previous structure audit found 0 high, 0 medium and 60 low DOCX findings; all low findings were raw DOI hyperlink display text. Five figures have descriptive alt text and all 13 tables have marked header rows.
- The PDF remains untagged and must not be described as PDF/UA-conformant.

The original 60-reference production record is in [the 4 November final-build QA log](../logs/2026-11-04-final-60-reference-build-qa.md); bibliography, layout, table-readability, terminology and proofread refinements are documented in their linked dated QA logs.


## Readiness matrix

| Workstream | Status | Remaining action |
|---|---|---|
| Manuscript assembly and production | **Complete** | Rebuild only after approved changes to source or target formatting. |
| Citation linkage and bibliography reconciliation | **Complete for the current 60-entry build** | Re-run the linkage check after any reference or citation edit. |
| Claim-ledger integration | **Complete for 94 recorded claim groups** | Do not treat this count as a replacement for the documented source-level qualifications and holds. |
| Scientific caveats and critical holds | **Preserved; not all resolved** | Keep SEM-010, SEM-038, SEM-046, SEM-050 and SEM-051 qualifications visible. Do not silently normalize unresolved source conflicts. |
| Language editing | **Final source-level proofread complete** | After the AMU/journal template is confirmed and applied, make a final destination-specific read-through for pagination, voice and instructions. |
| Citation style and target format | **ACS numeric style applied; institutional requirement unconfirmed** | CASSI exact records have been confirmed for 30 of 40 journal titles; ten remain provisional pending direct title/ISSN lookup. Confirm the required citation style, target template and short-journal forms with the AMU Department of Chemistry/supervisor. |
| Author list and affiliations | **Missing from manuscript** | Confirm every author, order, institutional affiliation at the time the work was carried out, corresponding author, and approved contact details. Do not infer authorship from supervision or project assistance. |
| Acknowledgements | **Not present** | Confirm whether any non-author contribution or facility support should be acknowledged; obtain permission where appropriate. |
| Funding statement | **Not present** | Confirm whether any grant, institutional, departmental, scholarship or other financial support supported the work. Include grant identifiers if applicable. |
| Conflict-of-interest statement | **Not present** | Obtain confirmation from every author before inserting a “no competing interests” declaration. |
| Data-availability statement | **Not present** | Decide which repository version should be cited. Consider a tagged, immutable release and a DOI archive if the target journal requires persistent data citation. |
| Author contributions / CRediT | **Not present** | Include only if required by the selected journal or institution; agree roles with all authors. |
| Ethics statement | **Not present** | The paper is a review of published literature. Confirm whether the target requires an ethics declaration or a “not applicable” statement. |
| Figure/table permissions | **Not re-audited in this checkpoint** | Confirm that all diagrams are original and that any reused/adapted third-party material has the necessary permission and attribution. |
| Final institutional checklist | **Pending** | Obtain the applicable AMU/Department of Chemistry instructions and supervisor sign-off. |
| Final target-format QA | **Pending** | After the style/template is confirmed, regenerate DOCX/PDF and repeat citation, pagination, figure, table and accessibility checks. |

## Declaration wording — drafts only, not approved for insertion

The following are candidate formulations. They must not be inserted as factual declarations until the relevant authors confirm them and the target's wording requirements are known.

- **Funding — only if accurate:** “This work received no external funding.” If support was received, replace this with the funder and grant details.
- **Competing interests — only if every author confirms:** “The authors declare no competing financial interests.” Use the journal's required wording if different.
- **Data availability — draft, subject to repository/version decision:** “The evidence tables and claim-to-source audit records supporting this review are available in the project repository at https://github.com/zaidkhan005/reviewAdsorbants. The underlying studies are cited in the reference list.” A journal may require a version-specific archive DOI rather than a mutable repository URL.
- **Ethics — only if requested and confirmed:** “Not applicable. This review synthesizes previously published literature and reports no new experiments involving human participants or animals.”
- **Acknowledgements:** identify specific non-author contributions only after confirming the contribution and obtaining any required permission.
- **Author contributions:** assign roles only after the author list and contribution agreement are settled.

## Institutional-format note

The public AMU Research & Development Cell page located during this checkpoint lists research-project proposal and execution procedures. It does not establish the required manuscript style for a BSc Chemistry semester paper. The department or supervisor must therefore confirm the applicable student-paper requirements; a research-project SOP should not be substituted for a manuscript-format instruction.

## Finalization sequence

1. Confirm the destination: AMU semester assessment, journal submission, or both.
2. Confirm author names/order, affiliations, corresponding author and contribution roles.
3. Confirm the applicable citation style, journal/department template, word limits, and any required supplementary files.
4. Confirm acknowledgements, funding, conflicts, ethics and data-availability wording.
5. Apply only the approved metadata/declaration changes to the canonical source.
6. After the target style/template and author declarations are confirmed, make the approved changes, rebuild, and repeat the target-specific QA.

**Current disposition:** technically produced and internally reconciled working draft; not yet submission-ready. The blockers are author/institution decisions and target-specific formatting, not a failed production build.

## Initial accessibility and artifact-handoff audit — 4 November 2026 (53-reference iteration; superseded)

A separate [accessibility and artifact-integrity audit](../logs/2026-11-04-submission-accessibility-handoff-audit.md) was completed on the current build.

- DOCX accessibility audit: 0 high, 0 medium, 60 low findings. All 60 low findings are visible raw DOI URLs in the bibliography.
- All five embedded figures have descriptive alt text; all 13 tables have their first row marked as a table header.
- DOCX core properties (title, subject, author and keywords) remain blank pending author metadata.
- PDF: 50 searchable A4 pages, 57 outline/bookmark entries and 86 link/annotation entries; openable, unencrypted and without XFA.
- The PDF catalog has no tagged-PDF structure tree. It is searchable and bookmarked, but should not be described as fully tagged or PDF/UA-conformant. A tagged-PDF step is needed only if required by the destination or accessibility needs.
- The loose PDF mismatch was corrected by extracting the PDF from the verified Actions ZIP. Final DOCX, PDF and ZIP hashes now match the recorded build values.

This audit made no changes to the manuscript source, scientific content or citations.

## Final proofread 60-reference build — 4 November 2026

The final source-level proofread, paragraph restructuring, table pagination correction and PDF/Word equation-rendering correction are included in the successful production output.

- Successful build: [GitHub Actions run 41784649185](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41784649185); artifact ID `13301131061`.
- Source commit: `a98bb2f66f763455941e4e6fc3d973dc56f9d0f7`.
- Artifact SHA-256: `49852e5e1bbe0bd44c9f326de8e6b5304c29c23a6d67ba35d3b3338e53021c94`.
- Output: 60-page editable A4 DOCX and 50-page searchable A4 PDF; checksums and proofread findings are recorded in the [final proofread QA log](../logs/2026-11-04-final-proofread-qa.md).
- Citation linkage: 60 manuscript keys, 60 bibliography records and 60 unique DOIs; zero missing or unused keys.
- The ten intentional inline-math spans are rendered correctly in both formats. Table 2E's Shaha et al. (2025) unavailable kinetic result is marked NR, preventing an orphaned continuation on the following page.
- The seven contextual references remain outside the frozen 49-study set. The 15-study condition-labelled comparison and 94-claim ledger are unchanged.
- Accessibility: the DOCX structural audit remains at 0 high, 0 medium and 60 low hyperlink-display findings. The PDF is searchable but untagged and not PDF/UA-conformant.

The preceding 60-reference expansion build and its bibliography QA are retained as historical production evidence. The latest source of truth is this proofread build and its dated QA record.


## Final 60-reference accessibility and artifact-handoff status

The current build is covered by the [final 60-reference build QA log](../logs/2026-11-04-final-60-reference-build-qa.md). The prior 53-reference accessibility audit above is retained as historical evidence only.

- Current Word file: 60 pages; 0 high-severity, 0 medium-severity and 60 low-severity accessibility findings. All 60 low findings are raw DOI URLs used as bibliography link display text.
- All five figures have descriptive alt text. All 13 tables have their first row marked as a table header. All 60 bibliography entries are kept together in Word page layout.
- Current PDF: 50 searchable A4 pages; 57 outline/bookmark entries; 86 annotations/links; no forms or attachments; no encryption or XFA.
- The PDF is not tagged and should not be described as PDF/UA-conformant. A tagged-PDF conversion remains conditional on institutional, journal or reader accessibility requirements.
- The final artifact and DOCX/PDF hashes are reconciled to Actions run 41762141686. The earlier loose-file mismatch note refers only to the 53-entry iteration.

