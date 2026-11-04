# Submission accessibility and artifact-integrity audit — 4 November 2026

## Scope

A handoff audit was performed on the 4 November language-edited manuscript files. No manuscript content, evidence records, bibliography entries or citations were changed.

## Authoritative file verification

| File | SHA-256 | Result |
|---|---|---|
| `SEMESTER_MANUSCRIPT_V2_ACS_DRAFT.docx` | `6c324b976cdd0d7f777f3852cc1e3eec841e0fabb68aa2a79f9af4d430520526` | Matches the final build QA record. |
| `SEMESTER_MANUSCRIPT_V2_ACS_DRAFT.pdf` | `9b14bb583f729368f11d95a705acc26b021dd3bd1fda1b278f41f27e75dbfaa2` | Matches the PDF extracted from the verified Actions artifact and the final build QA record. |
| `SEMESTER_MANUSCRIPT_V2_ACS_DRAFT_BUILD_ARTIFACT.zip` | `97a1ac75e8ea008bdb52db46c65844e9600975705c770580b9a0bad99517f538` | Matches the recorded artifact digest. |

A loose PDF copy present in the working directory initially had a different hash. It was replaced with the PDF extracted directly from the verified build ZIP. The DOCX and ZIP were already correct. Final hashes above were rechecked after the replacement.

## Word accessibility and structure

The DOCX accessibility audit reported:

| Finding | Count |
|---|---:|
| High severity | 0 |
| Medium severity | 0 |
| Low severity | 53 |

All 53 low-severity findings are bibliography hyperlinks whose visible text is a raw DOI URL. The audit found no missing heading hierarchy, image-alt or table-header issue.

Additional OOXML inspection confirmed:
- Five embedded figures; all five have non-empty, descriptive alternative text.
- Thirteen tables; all thirteen first rows are marked as table headers.
- Semantic heading styles are present for the title, main sections, subsections and References.
- Core document properties for title, subject, author, keywords and last-modified-by are blank. This is consistent with author metadata still being pending; populate these only after author details are confirmed.

The 53 raw DOI strings are standard, resolvable identifiers and were retained to avoid changing the current bibliography display during a handoff-only audit. Descriptive link labels could be considered later if required by an accessibility specification or target style.

## PDF technical inspection

The final PDF preflight confirms:
- 48 pages, A4 geometry (595 × 842 pt).
- Openable and searchable; not encrypted.
- No XFA forms.
- 57 outline/bookmark entries.
- 76 link/annotation entries.
- No file attachments or form fields.

The PDF catalog does not expose a tagged-PDF structure tree (`/StructTreeRoot`). The PDF is searchable and bookmarked, but it should **not** be represented as a fully tagged/accessibility-conformant PDF. The DOCX currently carries the stronger semantic structure (headings, image alternative text and table-header rows). If the institution, journal, or reader requires a tagged PDF or PDF/UA, a separate tagged-PDF production and validation step will be necessary.

## Visual/layout verification boundary

The verified 4 November build record already documents page-contact-sheet review of all 60 Word-render pages and all 48 PDF pages, with full-size inspection of dense/changed pages. The present audit did not introduce layout edits and therefore did not trigger a new render. The corrected loose PDF is byte-identical to the PDF in that already-reviewed artifact.

## Disposition

- File hashes and artifact identity are reconciled.
- Word accessibility audit: no high- or medium-severity findings; 53 low-severity raw-DOI hyperlink findings.
- Figures have descriptive alt text and all tables have marked header rows.
- PDF is searchable and bookmarked but not tagged as a structured accessible PDF.
- No edits were made to the canonical manuscript source.

See also the [submission-readiness checklist](../docs/SEMESTER_MANUSCRIPT_SUBMISSION_READINESS_CHECKLIST.md) and [current file index](../docs/SEMESTER_MANUSCRIPT_FILE_INDEX.md).
