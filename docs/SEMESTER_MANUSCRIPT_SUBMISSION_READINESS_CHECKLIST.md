# Submission-readiness checkpoint — 4 November 2026

## Purpose and boundary

This checkpoint follows the successful language-edited production build. It assesses the remaining author, institutional and publication-finalization work. It does **not** repeat the scientific source audit, change the frozen study selection, or treat successful file generation as scientific or institutional approval.

The canonical manuscript source remains `manuscript/SEMESTER_MANUSCRIPT_ASSEMBLED_SOURCE_V2.md`. The GitHub repository remains the project source of truth.

## Authoritative production snapshot

- Branch: `main`.
- Latest successful build: [GitHub Actions run 41718042264](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41718042264).
- Build source commit: `ef2b1de98fe4d25c1a05a02bda11d504296e558d`.
- Artifact: `semester-manuscript-v2-acs-draft`, ID `13270582585`; SHA-256 `97a1ac75e8ea008bdb52db46c65844e9600975705c770580b9a0bad99517f538`. The artifact was verified present and unexpired on 4 November 2026.
- DOCX: 60 A4 pages; SHA-256 `6c324b976cdd0d7f777f3852cc1e3eec841e0fabb68aa2a79f9af4d430520526`.
- PDF: 48 searchable, unencrypted A4 pages; SHA-256 `9b14bb583f729368f11d95a705acc26b021dd3bd1fda1b278f41f27e75dbfaa2`.
- Integrity totals: 94 claim groups; 49 selected studies; 53 bibliography entries and 53 in-text citation keys; zero missing or unused keys.
- Current integrated structure: Tables 1–3 are in the main manuscript. The former separate S1/S2 arrangement is not part of the current build.

The build and page-layout results are detailed in [the final language-edited build QA log](../logs/2026-11-04-language-edited-final-build-qa.md).

## Readiness matrix

| Workstream | Status | Remaining action |
|---|---|---|
| Manuscript assembly and production | **Complete** | Rebuild only after approved changes to source or target formatting. |
| Citation linkage and bibliography reconciliation | **Complete for the current 53-entry build** | Re-run the linkage check after any reference or citation edit. |
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
6. Rebuild and rerun the final format-specific QA; retain the current successful artifact as the prior verified version.

**Current disposition:** technically produced and internally reconciled working draft; not yet submission-ready. The blockers are author/institution decisions and target-specific formatting, not a failed production build.
