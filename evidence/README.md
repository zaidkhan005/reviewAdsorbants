# Evidence notes index

This directory contains human-readable, source-linked extraction notes for the review paper. The structured evidence register lives in [`data/corpus-evidence.csv`](../data/corpus-evidence.csv); per-batch staging records and the consolidation crosswalk live in [`data/batch-extractions/`](../data/batch-extractions/).

## Latest upload batch

- [2026-10-29 — First processing wave from the full BibTeX](2026-10-29-bibtex-initial-screening.md) — DISC-069–DISC-079; 16 provisional evidence rows; PDF-page/SI checks still pending.


- [2026-10-28 — Upload batches: DISC-037–DISC-068, 177 source-linked evidence rows](2026-10-28-upload-batches.md)

## Provenance and integrity audit

- [2026-10-31 — original PDF batch integrity audit](../logs/2026-10-31-original-pdf-batch-integrity-audit.md) — confirms original Batches 01–20 evidence-row counts, documents five master-CSV field repairs, and records verified Library filename matches for Batches 03 and 08 (plus Batch 12's CNT PDF).

## Provenance and integrity audit

- [2026-10-31 — original PDF batch integrity audit](../logs/2026-10-31-original-pdf-batch-integrity-audit.md) — confirms the original Batches 01–20 notes, repairs five malformed evidence rows and verifies the complete 60-paper attachment-to-evidence mapping.
- [Original PDF batch attachment crosswalk](../data/original-pdf-batch-attachment-crosswalk.csv) — 60 uploaded-paper records mapped to Library filenames, DOI, candidate IDs, source-batch evidence IDs and extraction notes.

## Scientific evidence gaps

- [Prioritized original-corpus scientific gap register](../data/original-corpus-scientific-gap-register.csv) — 19 ranked issues, separating quantitative/mass-balance blockers from optional SI and editorial boundaries.

## Previous PDF batches

- [2026-10-25-batch-01](2026-10-25-batch-01.md)
- [2026-10-25-batch-02](2026-10-25-batch-02.md)
- [2026-10-25-batch-03](2026-10-25-batch-03.md)
- [2026-10-26-batch-04](2026-10-26-batch-04.md)
- [2026-10-26-batch-05](2026-10-26-batch-05.md)
- [2026-10-26-batch-06](2026-10-26-batch-06.md)
- [2026-10-26-batch-07](2026-10-26-batch-07.md)
- [2026-10-26-batch-08](2026-10-26-batch-08.md)
- [2026-10-26-batch-09](2026-10-26-batch-09.md)
- [2026-10-26-batch-10](2026-10-26-batch-10.md)
- [2026-10-26-batch-11](2026-10-26-batch-11.md)
- [2026-10-26-batch-12](2026-10-26-batch-12.md)
- [2026-10-26-batch-13](2026-10-26-batch-13.md)
- [2026-10-26-batch-14](2026-10-26-batch-14.md)
- [2026-10-27-batch-15](2026-10-27-batch-15.md)
- [2026-10-27-batch-16](2026-10-27-batch-16.md)
- [2026-10-27-batch-17](2026-10-27-batch-17.md)
- [2026-10-27-batch-18](2026-10-27-batch-18.md)
- [2026-10-27-batch-19](2026-10-27-batch-19.md)
- [2026-10-27-batch-20](2026-10-27-batch-20.md)

## Workflow rule

For every new PDF batch, update both the source-pinned master data and a Markdown narrative under this directory. Keep original staged inputs, preserve page/table/figure pinpoints, and record limitations or discrepancies explicitly. Evidence extraction does not by itself mean final inclusion or Q1 eligibility.
