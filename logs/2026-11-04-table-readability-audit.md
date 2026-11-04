# Final table-readability audit — 4 November 2026

## Scope

This pass reviewed the canonical manuscript V2, Table 1 search-strategy source, Table 3 evidence-coverage source and the reader-facing Table 2 construction. The user's table-layout rule is applied: individual cells should carry one concise item, and qualifications or secondary details should be separated rather than packed into one cell.

## Findings

### Table 1 — search strategy

- Table 1A contains 14 exact search strings. The longest query is 134 characters (16 words), which is expected because the cell preserves the reproducible search expression verbatim.
- Table 1B has short source/coverage descriptions; the longest cells contain eight words.
- No search string or source boundary was shortened because doing so would alter the recorded search method.

### Table 2 — condition-labelled comparison

The nine panels (2A–2I, including 2F(a) and 2F(b)) are split by endpoint class rather than placing performance, conditions, recovery and cost in one oversized table.

- Table 2A: 15 rows; longest data cell is five words.
- Table 2B: 19 condition rows; the longest cell is an 11-word contact-time qualification. It preserves a source limitation that should not be dropped.
- Table 2C: 28 observed/source-reported endpoints; the longest metric label is six words.
- Table 2D: 24 fitted-isotherm rows; study/model/parameter/value remain in separate columns.
- Table 2E: 17 kinetic-model rows; the longest value note is six words.
- Table 2F(a) and 2F(b): recovery method and cycle outcome are separated.
- Table 2G: matrix/feed and evidence limitation are separate fields.
- Table 2H: precursor, processing steps and energy/drying note are separate fields.
- Table 2I: reported price/cost and cost-evidence limitation are separate fields; the longest qualification is 11 words.

No Table 2 source edit was warranted. The longest cells preserve concise, decision-relevant qualifications and are not paragraphs of unrelated detail.

### Table 3 — 49-reference evidence coverage

The raw Table 3 source contains long evidence/guardrail entries (some exceed 90 words). The production builder does **not** render these as giant cells in the final manuscript. Instead, the reader-facing build creates:
1. a compact three-column selected-reference index; and
2. separate study-level evidence notes with labelled fields for target, adsorbent/study role, source tier, evidence qualification and citation.

This preserves the source-access caveats, numerical holds and citation trail while avoiding a dense 49-row table with long narrative cells. No scientific qualification was removed.

## Disposition

- **Table readability:** pass for the current reader-facing DOCX/PDF.
- **Scientific content:** unchanged.
- **Table source data:** unchanged.
- **Production rebuild:** not required; this was an audit of the existing rendered structure.
- **Next proofread focus:** sentence-level consistency and repetition in Sections 3–5, followed by title/abstract/conclusion alignment and the remaining institutional declarations.
