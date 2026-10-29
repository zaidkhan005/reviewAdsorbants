# Research and evidence workflow

## Live status overlay (2026-10-29)

The numbers in the 2026-10-27 checkpoint below are historical. Current live files contain 111 candidate records in `data/corpus-screening-register.csv`, 505 evidence rows in `data/corpus-evidence.csv`, and 41 journal records in `data/journal-quartile-audit.csv`. The processed Better BibTeX queue contains 164 entries; 58 are not yet in the screening register, and final paper eligibility and citation status are not complete. The 208-row primary-study comparison matrix covers 43 candidate IDs and is a focused subset, not the full corpus.

A separate approved semester paper is tracked in `docs/SEMESTER_PAPER_SCOPE_PROPOSAL.md`, `data/semester-paper-candidate-register.csv` (40 candidates), `evidence/semester-paper/SEMESTER_CORE_EVIDENCE_EXTRACTION.csv` (16 dedicated records), and `data/semester-main-corpus-crosswalk.csv`. Its scope is graphene-based adsorbents/composites for CIP and TC; do not merge its ~50 actual-citation target with the broad-review ~60/~150 targets. The user has paused new downloads; proceed with available files and accessible sources.


## Historical corpus checkpoint and restart rule (2026-10-27; superseded by live status overlay)

The unified-corpus restart and the intake of the supplied PDFs through Batch 20 are complete. The current canonical records are 68 candidate/screening rows, 311 source-linked evidence findings, and 64 source-caveat entries. Of the 68 candidate rows, 61 had completed full-text screening at the previous checkpoint; six new discovery leads are awaiting source review and `DISC-022` remains deferred. `DISC-022` is deferred until the user supplies the full-text PDF; it is not screened or excluded and is temporarily outside the active queue. The journal-level quartile audit has 38 rows after the latest pass; 34 existing journal titles were audited previously, and four newly encountered titles remain marked not yet audited in `data/journal-quartile-audit.csv`; latest available 2025 SJR profiles were used where found, with historical/discontinued and category-level caveats explicitly recorded. The evidence table contains findings from primary studies and reviews, so it is not a paper count or accepted bibliography.

- The original outline and processing-and-cost continuum remain the manuscript's structural guide.
- The original seven papers remain part of the full corpus, not a separate privileged evidence set.
- Every value, mechanism and bibliographic detail must be checked against its original source before it is treated as verified; review-derived values must remain distinguishable from primary-study results.
- Do not assume additional user-held PDFs remain to be uploaded. Further literature discovery should be targeted to gaps revealed by screening and synthesis.
- See `docs/CORPUS_RESET_AND_RESTART.md` for the historical restart protocol.

## Bibliography targets — mandatory project constraint

The supervisor's broad-review planning targets are approximately **60 distinct relevant works actually cited** for the semester publication and approximately **150 distinct relevant works actually cited** for the publisher/journal version, subject to the eventual journal's current instructions. These must not be merged with the separately approved graphene/CIP/TC semester paper's approximately 50-work planning target. Track these separately from PDF batches, candidate rows, full-text screens and evidence records.

As of the 2026-10-29 live audit, the screening register contains 111 candidates, but the final number of accepted/cited works is **not audited**. The 164-entry Better BibTeX inventory is processed through `references/bibtex_full_corpus_processing_queue_2026-10-29.csv`; it is not proof that all items have been screened or included. Do not claim the broad-review targets are met because the register or evidence table has those row counts. See `docs/REFERENCE_TARGET_PLAN.md` and `docs/LITERATURE_DISCOVERY_PLAN.md`.

Literature discovery continues after intake of the user's existing PDFs through Batch 20. Use targeted gap searches and citation chasing; request a user-supplied full text only when an important candidate cannot be accessed legitimately through available sources. Do not pad counts with duplicate versions, irrelevant studies, or unverified citations.

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

Keep one canonical corpus screening register: `data/corpus-screening-register.csv`. The updated Better BibTeX export was reconciled on 2026-10-25; the 68-row register is now the working canonical register, not an interim record. Its rows are candidates, not automatic final inclusions.

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

A paper's journal ranking record must state the ranking system, ranking year, subject category, quartile and verification URL. SJR and Clarivate/JCR are distinct systems and can return different quartiles for the same journal. Use the latest available SJR year (2025 where located) for the current journal profile, but do not imply that this was the journal's quartile in the paper's publication year. Where only a secondary profile was accessible, label the result provisional until checked against the ranking source required by the institution. Impact factor and journal reputation do not themselves establish Q1 status.

Current ranking details are in `data/journal-quartile-audit.csv` and `logs/2026-10-27-q1-audit-batch-01.md`. Provisional working roles for all candidates are recorded in `data/candidate-decision-audit.csv`; `data/screening-decision-adjudication-v1.csv` currently maps the 111-candidate corpus into provisional scope/ranking signals with provisional scope decisions separated from ranking-eligibility signals; the CORP-023 published abstract check is logged in `logs/2026-10-27-corp-023-published-abstract-check.md`; target/material/stage comparison groupings for primary-study evidence are in `data/primary-study-comparison-matrix.csv`; the evidence-weighted processing–cost–performance working draft is in `manuscript/CONTINUUM_SYNTHESIS_V1.md`; the initial raw-biomass subsection working draft is in `manuscript/SECTION_2_1_RAW_BIOMASS_V1.md`. These drafts use internal candidate IDs pending the final Zotero citation audit. The quantitative-comparison readiness audit is in `logs/2026-10-27-comparison-readiness-audit-01.md`; it cross-checks the 208-row matrix (now 249 unique evidence IDs) against the 311-record evidence register and separates the most defensible within-study comparisons from values held due to mass-balance, unit or endpoint conflicts. The first evidence-grounded comparison tables are in `manuscript/COMPARATIVE_TABLES_V1.md`; CORP-023's headline pH-4 capacities have now been confirmed against the published abstract while its detailed published tables remain unverified (see `logs/2026-10-27-corp-023-published-abstract-check.md`); they are working tables and still require source-PDF/supplement checks and final journal-year eligibility adjudication. Two journals in the corpus have a current-source-list discontinuation flag (Arabian Journal of Chemistry and Iraqi Journal of Agricultural Sciences); the latter is not assigned a current quartile. Follow-up verification confirms current 2025 SJR Q2 across six categories for Journal of Engineering and Q1 across three categories for Carbon Research; iScience Q1 is corroborated for 2025 and the 2024 snapshot. Environmental Research remains provisional for the exact 2025 Environmental Science category. The candidate-role audit, scope/ranking adjudication sheet and comparison matrix are aids for human adjudication and normalization, not final manuscript inclusion decisions or a finished ranking of adsorbents. `DISC-022` remains deferred by the user until their full-text PDF is supplied, and cannot be treated as screened or excluded.

## 8. Draft and cite

Draft only after evidence for the paragraph is extracted. Use Zotero for citation insertion and bibliography generation, then check that each numerical or mechanistic claim traces to a primary source. Preserve the original outline and continuum, including a standalone mechanisms section in the working outline.

## 9. GitHub storage convention

- Every session ends with a dated entry in `logs/`.
- Reconcile the canonical screening register only when the Zotero corpus changes. **Historical note:** the register was 68 rows on 2026-10-25; the current 111-row register and 164-entry Better BibTeX processing queue are described in the live overlay at the top of this document.
- Update canonical evidence tables only after checking original papers.
- Keep the old seven-paper table and caveats as a historical seed record until each paper has been re-verified.
- Record major scope/taxonomy decisions in `docs/MATERIAL_TAXONOMY.md` and the dated log.
- Save manuscript drafts under `manuscript/`.
- Do not commit copyrighted PDFs unless permitted, or private credentials/notes.

## Paper status vocabulary

`SCREEN-NEW` → `METADATA-CHECKED` → `FULLTEXT-NEEDED` / `FULLTEXT-RECEIVED` → `EVIDENCE-EXTRACTED` → `EVIDENCE-VERIFIED` → `ACCEPTED` / `EXCLUDED`.

Full-text/evidence status and quartile verification are independent. A relevant paper can be useful for background and still fail a Q1-only inclusion rule.
