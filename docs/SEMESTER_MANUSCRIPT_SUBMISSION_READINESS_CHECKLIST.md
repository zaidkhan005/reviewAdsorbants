# Submission-readiness checkpoint — 4 November 2026

## Purpose and boundary

This checkpoint follows the successful 4 November 2026 60-reference production build. It assesses the remaining author, institutional and publication-finalization work. It does **not** repeat the scientific source audit, change the frozen study selection, or treat successful file generation as scientific or institutional approval.

The canonical manuscript source remains `manuscript/SEMESTER_MANUSCRIPT_ASSEMBLED_SOURCE_V2.md`. The GitHub repository remains the project source of truth.

## Authoritative production snapshot

- Branch: `main`.
- Latest successful build: [GitHub Actions run 41762141686](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41762141686).
- Build source commit: `82e47d1c85912159858a4b0d053e3048fe8c4395`.
- Artifact: `semester-manuscript-v2-acs-draft`, ID `13290473226`; SHA-256 `6a99f2576d777d5a2b6cf9cf8f4631f49f93be7dcbdb8610c105d4dada5cf82c`. The artifact was verified present and unexpired on 4 November 2026.
- DOCX: 60 A4 pages; SHA-256 `9645308ac946ef009b88a22a99bbd7af9fff80dbd3592006b53d4d28c814015c`.
- PDF: 50 searchable, unencrypted A4 pages; SHA-256 `eeb830df8877aaa85205f2f9d3da3662be0d807a12142028e9c444cde2db9a7a`.
- Integrity totals: 94 claim groups; 49 selected studies; 60 bibliography entries and 60 in-text citation keys; zero missing or unused keys; 60 unique DOIs.
- Current integrated structure: Tables 1–3 are in the main manuscript. The former separate S1/S2 arrangement is not part of the current build.

The current build and page-layout results are detailed in [the final 60-reference build QA log](../logs/2026-11-04-final-60-reference-build-qa.md).

## Readiness matrix

| Workstream | Status | Remaining action |
|---|---|---|
| Manuscript assembly and production | **Complete** | Rebuild only after approved changes to source or target formatting. |
| Citation linkage and bibliography reconciliation | **Complete for the current 60-entry build** | Re-run the linkage check after any reference or citation edit. |
| Claim-ledger integration | **Complete for 94 recorded claim groups** | Do not treat this count as a replacement for the documented source-level qualifications and holds. |
| Scientific caveats and critical holds | **Preserved; not all resolved** | Keep SEM-010, SEM-038, SEM-046, SEM-050 and SEM-051 qualifications visible. Do not silently normalize unresolved source conflicts. |
| Language editing | **Controlled edit complete** | A final human proofread for voice, transitions, and correctness remains advisable after the target template is applied. |
| Citation style and target format | **Pending** | Confirm whether this is an AMU semester submission, a journal submission, or both. For a journal, select the target journal and follow its current author instructions. ACS Guide 2026 is provisional only. |
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

## Final 60-reference build — 4 November 2026

The 60-reference manuscript has been built successfully and the resulting DOCX/PDF have been independently checked. This supersedes the 53-entry language-edited artifact and the earlier intermediate 60-reference build. The active bibliography input is `semester-manuscript-cited-references-49-selected-plus-11-context.bib`.

- Successful build: [GitHub Actions run 41762141686](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41762141686); artifact ID `13290473226`.
- Build SHA-256: `6a99f2576d777d5a2b6cf9cf8f4631f49f93be7dcbdb8610c105d4dada5cf82c`.
- Output: 60-page editable A4 DOCX and 50-page searchable A4 PDF; checksums and complete preflight findings are recorded in the [final 60-reference build QA log](../logs/2026-11-04-final-60-reference-build-qa.md).
- Citation linkage: 60 manuscript keys, 60 BibTeX records and 60 unique DOIs; zero missing or unused keys.
- Accessibility: 0 high, 0 medium, 60 low DOCX findings; all low findings are raw DOI URLs used as bibliography hyperlinks. Five figures have descriptive alt text; all 13 tables have header-row markup. The searchable PDF is not tagged and is not PDF/UA-conformant.
- The seven contextual references remain outside the frozen 49-study set. The 15-study condition-labelled comparison and 94-claim ledger are unchanged.

The earlier 53-entry accessibility and handoff log applies only to that previous iteration. The final build QA log records the corrected DOI for Ge et al. against the publisher PDF and the current file hashes.

No selected-study membership or scientific evidence values were changed by the seven-reference expansion.

## Final 60-reference accessibility and artifact-handoff status

The current build is covered by the [final 60-reference build QA log](../logs/2026-11-04-final-60-reference-build-qa.md). The prior 53-reference accessibility audit above is retained as historical evidence only.

- Current Word file: 60 pages; 0 high-severity, 0 medium-severity and 60 low-severity accessibility findings. All 60 low findings are raw DOI URLs used as bibliography link display text.
- All five figures have descriptive alt text. All 13 tables have their first row marked as a table header. All 60 bibliography entries are kept together in Word page layout.
- Current PDF: 50 searchable A4 pages; 57 outline/bookmark entries; 86 annotations/links; no forms or attachments; no encryption or XFA.
- The PDF is not tagged and should not be described as PDF/UA-conformant. A tagged-PDF conversion remains conditional on institutional, journal or reader accessibility requirements.
- The final artifact and DOCX/PDF hashes are reconciled to Actions run 41762141686. The earlier loose-file mismatch note refers only to the 53-entry iteration.

