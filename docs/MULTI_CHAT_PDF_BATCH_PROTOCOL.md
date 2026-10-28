# Multi-chat PDF batch upload protocol

**Project:** Antibiotic Adsorption Review  
**Source of truth:** `zaidkhan005/reviewAdsorbants` on GitHub; Zotero is the reference manager.  
**Effective date:** 2026-10-28

## Why this protocol exists

The user plans to split newly downloaded papers across several branched chats, usually three PDFs per chat. A branch does not automatically receive the later conversation, uploaded PDFs, or uncommitted work from sibling branches. Each chat must therefore use a unique batch ID and write additive, batch-specific outputs. The master evidence/screening CSVs are merged centrally after the individual batches are completed so parallel branches cannot silently overwrite each other's changes.

## Batch IDs, unique namespaces, and expected files

The tracker is `data/new-paper-upload-batch-tracker.csv`. **Do not edit that shared tracker from each branched chat.** The central/master chat updates it during consolidation and assigns the numeric tracking slot after the branch outputs have been collected.

**Critical concurrency rule:** numeric slots such as `BATCH-01` through `BATCH-100` are central tracking labels; they are not a safe shared filename namespace while multiple chats are active. The generic paths `data/batch-extractions/batch-01-evidence.csv` and `...-screening.csv` are already occupied by a separate upload set, as are multiple following numeric batch paths. Never overwrite an existing path just because another branch used the same number.

Before creating outputs, inspect the current repository tree and look for the DOI/title in the master register, all existing staging CSVs, and batch notes. Create a **source-specific unique upload-set ID** for this branch. Prefer a deterministic code from the papers' DOI suffixes, for example `cs-200608028-2022134426-2025144252`, or another unique date-scoped identifier that includes distinct paper identifiers. Use the same unique code in every file path. If the path already exists or contains different papers, do not update or reuse it; choose another unique source-specific code.

Use these staging paths, replacing `<unique-set-id>` with the branch's confirmed unique code:
- Evidence: `data/batch-extractions/<unique-set-id>-evidence.csv`
- Screening: `data/batch-extractions/<unique-set-id>-screening.csv`
- Batch note: `logs/2026-10-28-<unique-set-id>-intake.md` (use the actual current date in the filename).

The tracker currently reserves 100 numeric batches (300 paper slots), but the candidate pool can grow beyond 300. If needed, add more numeric tracker slots **during central consolidation**; do not recycle a set ID or a batch-note path. Ten chats can be active in each wave; once consolidated, free the slots and continue with as many later waves as required.

Keep staging CSV column headers identical to the current master tables:
- Evidence: `data/corpus-evidence.csv` header.
- Screening: `data/corpus-screening-register.csv` header.

The branch must fetch the current headers before creating each staging file. Do not write to `data/corpus-evidence.csv`, `data/corpus-screening-register.csv`, `data/candidate-decision-audit.csv`, `data/screening-decision-adjudication-v1.csv`, `data/journal-quartile-audit.csv`, or the shared tracker from a batch branch. These are updated by the central chat during consolidation.

## Required processing for each uploaded PDF

1. **Inventory and deduplicate.** Record the exact uploaded filename; read the paper title, authors, year, journal and DOI from the PDF itself; match by DOI and title against `data/planned-download-pool.csv`, `data/corpus-screening-register.csv`, and current batch tracker. Report if a paper is already in the corpus or appears in another batch. Do not create a second candidate solely because the title is formatted differently.
2. **Read the full text.** Do not treat the publisher landing page or abstract as a full-text screen. Note whether supporting information is present or missing. Do not fabricate values from abstracts or reviews.
3. **Make a provisional scope decision.** Determine whether it is about antibiotic adsorption and which material class it actually represents. Distinguish raw vs chemically/physically modified; pristine vs activated/doped/magnetic biochar; unmodified biopolymers vs composites; adsorption vs degradation, oxidation, catalysis, membranes or disinfection. Mixed-process studies may support only their separately reported adsorption component.
4. **Extract source-linked evidence.** Each quantitative or mechanistic evidence row must include the specific candidate ID, citation, DOI, target antibiotic, adsorbent, conditions, exact reported result and units, metric/model, and precise source pinpoint (PDF page plus table/figure/section/equation). Retain the paper's stated uncertainty, contradictory reporting, calculation errors and limitations. If you cannot verify a pinpoint, mark it pending rather than guessing.
5. **Prepare staging outputs.** Put new evidence rows in the batch-specific evidence CSV and one screening-register row per new/updated paper in the batch-specific screening CSV. Use a provisional candidate ID only after checking the latest register; mark it clearly as a proposed ID if global allocation cannot be safely reserved. If a paper is a duplicate, record it in the batch note but do not duplicate its evidence or candidate row unless new source material adds distinct evidence.
6. **Quartile handling.** Do not infer Q1 from impact factor, journal reputation, or a current category alone. Mark new records “Not audited” unless publication-year, ranking provider/system and relevant category have actually been verified. Keep SJR and JCR distinct.
7. **Citations.** Do not invent a Zotero/Better BibTeX citation key. A DOI/paper title is not proof that the item exists in the user's Zotero library. Record citation-key matching as pending until a fresh export can be checked.
8. **Write a batch note to GitHub.** Summarize files processed, DOI/candidate matches, screening decisions, evidence row IDs, exact limitations, missing SI, quartile status, and unresolved questions. Use only your batch's unique paths. Re-read the current SHA before updating an existing file; do not overwrite another branch's work. If a commit conflict appears, fetch the latest file and reconcile.
9. **Finish with a user-facing receipt.** State which three files were received, which were fully read, which were duplicates/out of scope, which outputs were committed, and exactly what remains unresolved. Do not claim the master tables or the final citation targets have been updated until the central consolidation is done.

## Batch-specific starter message

Copy this into each new branch after identifying a **unique source-specific upload-set ID**. Do not reuse `BATCH-01` or a generic path if that path exists elsewhere in GitHub.

> This branch's unique upload-set ID is **<unique-set-id>**. I am uploading up to three newly downloaded papers. First read `docs/MULTI_CHAT_PDF_BATCH_PROTOCOL.md`, `data/new-paper-upload-batch-tracker.csv`, `data/planned-download-pool.csv`, and the current GitHub screening/evidence register headers. GitHub is the source of truth; do not restart completed work. Identify each PDF by filename, title, DOI, and pool/candidate ID; deduplicate against the latest master tables and every existing staging file/log. Fully inspect the PDFs, make provisional scope decisions, and create source-pinned evidence rows with original page/table/figure/equation locations and caveats. Write only to these unique paths: `data/batch-extractions/<unique-set-id>-evidence.csv`, `data/batch-extractions/<unique-set-id>-screening.csv`, and `logs/YYYY-MM-DD-<unique-set-id>-intake.md`. If any path already exists or contains different papers, do not overwrite it; choose another source-specific ID. Do not edit the shared master evidence, screening, adjudication, quartile or tracker files from this branch; these will be merged centrally. Do not invent data or Zotero citation keys, do not mark new papers Q1 without a separate audit, and preserve DISC-022 as deferred until its full text is supplied. End with an exact receipt and unresolved-items list.

## Central consolidation

After each wave of up to ten branches finishes, the central/master chat must:

1. Fetch all batch notes and staging CSVs from GitHub and validate their schemas.
2. Deduplicate candidates against the 68-row current register and across new batches using DOI plus title, respecting the existing DISC-022 deferral.
3. Allocate stable candidate IDs sequentially without collision; replace proposed IDs in evidence staging rows with the final IDs.
4. Merge only validated evidence rows into `data/corpus-evidence.csv` and only verified screening rows into the central screening register, decision audit and adjudication table. Do not erase existing content. Preserve row-level source pinpoints and caveats.
5. Update the journal-quartile audit separately for the relevant publication year, provider/system and subject category; keep unverified rows pending.
6. Update `data/new-paper-upload-batch-tracker.csv` with uploaded filenames, IDs, paths and consolidation status.
7. Check CSV shape, duplicate IDs, duplicate DOI/title, evidence-to-candidate references, and commit changes. Then report the new totals and remaining work.

## Non-negotiable safeguards

- No citation count is earned just by downloading or screening a paper. The targets remain 60 distinct relevant works actually cited for the semester version and about 150 for the publisher/journal version.
- No paper is accepted solely because it appears in the planned download pool.
- No candidate, evidence ID, source pinpoint, numerical result, quartile, or citation key may be invented.
- `DISC-022` stays deferred until the user supplies its full text.


## Concurrency vs. total volume (important)

The user may have **any number of downloaded papers**. The operating limit is **10 active branched chats at once**, not 10 batches or 30 papers total. Each active chat receives up to three PDFs. Therefore, one wave of 10 chats can process up to 30 papers; once that wave has finished and its outputs have been consolidated, reuse the freed chat slots for the next wave with new, never-reused batch IDs. Repeat for as many waves as necessary.

The tracker currently reserves `BATCH-01` through `BATCH-100` (300 paper slots) to make this convenient. If the corpus exceeds 300 papers, append further batches using `BATCH-101`, `BATCH-102`, etc.; never recycle an existing batch ID or filename. The maximum number of concurrent chats remains 10, even though the tracker can list many future batches.
