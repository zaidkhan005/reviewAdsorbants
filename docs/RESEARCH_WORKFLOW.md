# Research and evidence workflow

## Current corpus state and restart rule (2026-10-27)

The unified-corpus restart and the intake of the supplied PDFs through Batch 20 are complete. The current canonical records are 62 candidate/screening rows, 310 source-linked evidence findings, and 64 source-caveat entries. Of the 62 candidates, 61 are marked full-text checked; `DISC-022` remains `FULLTEXT-NEEDED`. Q1 verification has started but is not complete. The evidence table contains findings from primary studies and reviews, so it is not a paper count or accepted bibliography.

- The original outline and processing-and-cost continuum remain the manuscript's structural guide.
- The original seven papers remain part of the full corpus, not a separate privileged evidence set.
- Every value, mechanism and bibliographic detail must be checked against its original source before it is treated as verified; review-derived values must remain distinguishable from primary-study results.
- Do not assume additional user-held PDFs remain to be uploaded. Further literature discovery should be targeted to gaps revealed by screening and synthesis.
- See `docs/CORPUS_RESET_AND_RESTART.md` for the historical restart protocol.

## 1. Ingest the whole corpus

Use one Zotero collection: **Antibiotic Adsorption Review — Full Corpus**. Add the original seven papers plus all other relevant papers already downloaded. Do not manually classify or retag them at intake.

Export the collection once as `review-corpus.bib` using Better BibTeX. The export is reference metadata, not full-text content. The attachments in a local Zotero library do not automatically become readable in chat.

## 2. Inventory and deduplicate

From the complete export:
- identify exact and likely duplicate records;
- check titles, authors, year, journal and DOI/URL;
- preserve original citation keys when possible;
- flag records with incomplete or inconsistent metadata;
- record what information is unavailable rather than guessing.

Keep one canonical corpus screening register: `data/corpus-screening-register.csv`. The updated Better BibTeX export was reconciled on 2026-10-25; the 62-row register is now the working canonical register, not an interim record. Its rows are candidates, not automatic final inclusions.

## 3. Screen without asking the user to classify papers

For each candidate, determine from the accessible metadata, abstract and then full text:
- likely material category and processing stage;
- antibiotic(s) studied;
- original research, review or other study type;
- whether the reported removal is adsorption-only or includes degradation, oxidation, photocatalysis or membrane rejection;
- relevance to the processing–cost–performance continuum;
- full-text availability, Q1 verification status and next action.

Record uncertain material categories as provisional; don't demand manual pre-sorting from the user.

## 4. Obtain and verify full text

Use an uploaded PDF or a legitimate, accessible full-text source identified through a DOI/publisher link. Keep full text in Zotero or another appropriately licensed location. If only an abstract is available, mark the item `FULLTEXT-NEEDED`.

For values, read the original paper's methods, tables, figures, captions and supplements. Keep source page/table/figure pointers with extracted values. A citation, abstract or search snippet is not evidence that the full article was read.

## 5. Extract evidence

For each exact adsorbent–antibiotic pairing, record:
- preparation/feedstock, modification route and preparation parameters;
- pH/speciation, concentration, adsorbent dose, contact time, temperature, particle size, mixing and solution matrix;
- observed uptake/removal and model-fitted (q_{max}) separately;
- kinetic/isotherm models and fit-quality information;
- mechanism: direct experimental evidence versus author-proposed explanation;
- desorption, regeneration cycles, real-water and fixed-bed/column evidence;
- chemical/energy inputs, cost, yield, leaching, end-of-life and scale-up information;
- limitations and conflicts among abstract, narrative, tables, figures and supplements.

Use `Not reported`, `Not accessible`, or `Needs verification` where appropriate. Never invent a missing result.

## 6. Validate each value and mechanism

- Confirm the units and experimental conditions before comparing papers.
- Never equate observed uptake, percentage removal and fitted (q_{max}).
- Don't infer chemisorption solely from a pseudo-second-order fit or a unique mechanism from a model fit alone.
- Check suspect values against the actual tables/figures and supplementary material; preserve contradictions in the caveat register.
- Do not treat catalytic contaminant transformation as adsorption performance.

## 7. Verify Q1 independently

A paper is not Q1-verified until the register records the ranking source (e.g. Clarivate JCR or SCImago/SJR), ranking year, subject category, quartile and verification URL. Do not mix ranking systems silently. Impact factor and journal reputation do not themselves establish Q1 status.

## 8. Draft and cite

Draft only after evidence for the paragraph is extracted. Use Zotero for citation insertion and bibliography generation, then check that each numerical or mechanistic claim traces to a primary source. Preserve the original outline and continuum, including a standalone mechanisms section in the working outline.

## 9. GitHub storage convention

- Every session ends with a dated entry in `logs/`.
- Reconcile the canonical screening register only when the Zotero corpus changes; the current 62-row register has already been reconciled against the updated export dated 2026-10-25.
- Update canonical evidence tables only after checking original papers.
- Keep the old seven-paper table and caveats as a historical seed record until each paper has been re-verified.
- Record major scope/taxonomy decisions in `docs/MATERIAL_TAXONOMY.md` and the dated log.
- Save manuscript drafts under `manuscript/`.
- Do not commit copyrighted PDFs unless permitted, or private credentials/notes.

## Paper status vocabulary

`SCREEN-NEW` → `METADATA-CHECKED` → `FULLTEXT-NEEDED` / `FULLTEXT-RECEIVED` → `EVIDENCE-EXTRACTED` → `EVIDENCE-VERIFIED` → `ACCEPTED` / `EXCLUDED`.

Full-text/evidence status and quartile verification are independent. A relevant paper can be useful for background and still fail a Q1-only inclusion rule.
