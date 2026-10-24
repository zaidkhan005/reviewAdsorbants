# Full-corpus restart protocol

## Decision

Restart the literature workflow from one unified corpus, including the original seven seed papers and all other relevant papers already downloaded. Do not require the user to classify every paper into a material section, rebuild Zotero tags, or manually reorganize the library before screening begins.

**Restart the screening and evidence-verification process, not the manuscript's agreed scope or outline.** Keep the original supplied outline preserved in `manuscript/ORIGINAL_OUTLINE_AS_SUPPLIED.md`. Use `manuscript/REVIEW_OUTLINE.md` as the working outline, retaining the original processing-and-cost continuum and eight core material classes with the separately numbered mechanisms section.

## What "from scratch" means

- Every item in the new corpus starts as a candidate until it has been screened.
- The original seven papers are included in the same corpus as all other downloads.
- Prior evidence CSVs and caveats are retained as historical/seed notes. They are useful leads, but **their values are not treated as verified merely because they were previously entered**. Re-check every number, mechanism, and bibliographic detail against the original paper.
- Do not delete previous work, repeat manual taxonomy tagging, or move papers across many section-specific collections.
- Material category and processing stage are assigned during screening from the actual paper, not demanded from the user at intake.

## Minimal user workflow

### Step 1 — One Zotero collection

Create one collection named **`Antibiotic Adsorption Review — Full Corpus`**.

Add:
- the original seven seed papers;
- all other papers already downloaded that might be relevant;
- any new candidates the user has already saved.

If a paper is currently in another Zotero collection, add it to this collection without deleting the original collection. If a PDF is only in a local folder and not in Zotero, import it into this collection. Do not spend time applying material tags or arranging subcollections at this stage.

### Step 2 — One bibliography export

Right-click the full-corpus collection → **Export Collection…** → choose **Better BibTeX**. Uncheck Export Notes, Export Files, Include Annotations and Use Journal Abbreviation; leave Keep updated unchecked for the manual handoff. Save as **`review-corpus.bib`** and upload it in chat.

This export is an inventory of reference metadata; it does not include readable full-text PDFs under the selected settings. Inspect the actual export before assuming abstracts or attachments are included.

### Step 3 — Metadata audit and screening

Use the export to create one corpus-level screening register. Deduplicate records; normalize metadata where possible; flag missing DOI/title/year; identify study type, likely material class and antibiotic targets from accessible metadata/abstracts; and record whether full text is accessible.

Do not require the user to pre-sort papers. The assistant can assign preliminary categories during screening and flag ambiguity for review.

### Step 4 — Read the papers in small batches

Start with the seven seed papers as a calibration batch, while keeping them in the unified corpus. Read the actual accessible PDFs, cross-check earlier suspect values, and create page/table/figure-linked evidence notes. Then work through the remaining corpus in priority batches by relevance and study quality. PDFs may be uploaded here in small batches or accessed through legitimate full-text sources; Zotero's local attachments do not automatically appear in chat.

### Step 5 — Preserve structure and scope

The original outline is the structural source of truth:
- Stage 1: raw/unrefined lignocellulosic sorbents;
- Stage 2: natural clays and unmodified biopolymers;
- Stage 3: standard and chemically modified biochars;
- Stage 4: atomically engineered biochars, activated carbon, and nano-engineered carbons.

The working outline separates adsorption kinetics/isotherms from a standalone mechanisms section. This is a deliberate addition to make the missing mechanism coverage visible, not a replacement of the processing-and-cost continuum.

Keep adsorption-only evidence distinct from catalytic oxidation/degradation, photocatalysis and membrane rejection. Any claims in the original outline (including qualitative cost/energy ordering or mechanism assignments) are hypotheses to verify against primary studies, not assumptions.

## Work products

- `references/review-corpus.bib` — optional repository copy of the reviewed bibliographic export, added only after a quick privacy/content check.
- `data/corpus-screening-register.csv` — canonical screening register for the entire corpus.
- `data/corpus-evidence.csv` — canonical evidence table after full-text extraction and verification.
- `data/source-caveats.csv` — discrepancies and follow-up checks, including the older seven-paper seed set.
- `logs/` — decisions and session records.

Keep full-text PDFs in Zotero or another appropriately licensed location. Do not upload copyrighted publisher PDFs to GitHub unless the applicable licence permits it.

## First deliverable

The first deliverable is `review-corpus.bib` exported from the single Full Corpus collection. After receiving it, audit metadata and establish the screening register before asking for specific PDFs. The export should cover all papers, not only the original seven.
