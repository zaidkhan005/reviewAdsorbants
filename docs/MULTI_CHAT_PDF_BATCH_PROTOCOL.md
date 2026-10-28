# Multi-chat PDF batch upload protocol

**Project:** Antibiotic Adsorption Review  
**Source of truth:** `zaidkhan005/reviewAdsorbants` on GitHub; Zotero is the reference manager.  
**Effective date:** 2026-10-28

## Why this protocol exists

The user plans to split newly downloaded papers across several branched chats, usually three PDFs per chat. A branch does not automatically receive the later conversation, uploaded PDFs, or uncommitted work from sibling branches. Each chat must therefore use a unique batch ID and write additive, batch-specific outputs. The master evidence/screening CSVs are merged centrally after the individual batches are completed so parallel branches cannot silently overwrite each other's changes.

## Batch IDs and expected files

Use `BATCH-01` through `BATCH-10` for the first ten chats. Each branch should be titled “PDF Upload 01”, “PDF Upload 02”, etc. Three PDFs per branch is the working default. If the user has fewer than 30 papers, leave unused slots empty; if they have more, assign new unique IDs after checking the tracker.

The tracker is `data/new-paper-upload-batch-tracker.csv`. **Do not edit that shared tracker from each branched chat.** The central/master chat updates it during consolidation.

Each branch should create its own unique outputs after the PDFs are uploaded:

- Batch note: `logs/2026-10-28-batch-01-upload.md` (change the batch number for each branch).
- Evidence staging CSV: `data/batch-extractions/batch-01-evidence.csv`.
- Screening staging CSV: `data/batch-extractions/batch-01-screening.csv`.

Keep the staging CSV column headers identical to the master tables:
- Evidence: `data/corpus-evidence.csv` header.
- Screening: `data/corpus-screening-register.csv` header.

The branch must fetch the current header before creating each staging file. Do not write to `data/corpus-evidence.csv`, `data/corpus-screening-register.csv`, `data/candidate-decision-audit.csv`, `data/screening-decision-adjudication-v1.csv`, or `data/journal-quartile-audit.csv` from a batch branch. Those shared files are updated by the central chat during consolidation.

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

Copy this into each new branch after assigning the right batch number:

> This is **BATCH-XX** for the ongoing Antibiotic Adsorption Review project. I am uploading up to three newly downloaded papers. First read `docs/MULTI_CHAT_PDF_BATCH_PROTOCOL.md`, `data/new-paper-upload-batch-tracker.csv`, `data/planned-download-pool.csv`, and the current GitHub screening/evidence register headers. GitHub is the source of truth; do not restart completed work. Identify each uploaded PDF by filename, title, DOI and existing pool/candidate ID; deduplicate against the latest repository and other logged batches. Fully inspect the PDFs, make provisional scope decisions, and create source-pinned evidence rows with original page/table/figure/equation locations and caveats. Create only the unique batch note and staging CSVs assigned to BATCH-XX. Do not edit the shared master evidence, screening, adjudication, quartile or tracker files from this branch; these will be merged centrally. Do not invent data or Zotero citation keys, do not mark new papers Q1 without a separate audit, and preserve DISC-022 as deferred until I provide its full text. End with an exact receipt and unresolved-items list.

## Central consolidation

After the branches finish, the central/master chat must:

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
