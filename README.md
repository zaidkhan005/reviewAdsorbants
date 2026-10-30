# Antibiotic Adsorption Review

A structured workspace for the review paper on antibiotic removal by adsorption, organized around a **processing–cost–performance continuum**.

## Research objective

Compare raw biomass, natural clays and unmodified biopolymers, biochar, and engineered/nano-carbon adsorbents using evidence on preparation requirements, adsorption performance, mechanisms, regeneration, real-water behaviour, practical implementation, and cost/energy burden.

The intended contribution is an integrated comparison—not simply a ranking by maximum adsorption capacity or removal percentage.

## Source-of-truth rules

- **GitHub** is the project log, taxonomy, screening register, evidence summaries, manuscript drafts, decisions and change history.
- **Zotero** remains the bibliographic manager and source for citation keys and local/full-text PDFs.
- Use original research papers to verify numerical results, experimental conditions, and mechanistic claims. Reviews are primarily for field mapping and reference discovery.
- Store DOI/landing-page links, metadata, notes and extracted evidence here. Do not commit copyrighted publisher PDFs or private credentials.
- A capacity fitted from an isotherm (`qmax`) is not the same as observed uptake. Keep the two distinct.
- Keep adsorption separate from catalytic degradation, photocatalysis, membrane rejection and other removal processes.
- Never mark a paper “Q1 verified” without recording the ranking provider, ranking year, subject category, and verification URL.

## Repository status baseline (2026-10-29; continuation audited through 2026-10-30)

This repository now contains **two related but separate workstreams**. Do not combine their candidate counts, reference targets, evidence rows, or manuscript scopes.

### Broad antibiotic-adsorption review
- `data/corpus-screening-register.csv`: **111 unique candidate records**.
- `data/corpus-evidence.csv`: **505 unique evidence rows**. These are evidence findings, not papers or accepted references; provisional and staged rows remain visibly flagged.
- `data/journal-quartile-audit.csv`: **41 journal records**.
- The 2026-10-29 Better BibTeX processing queue has **164 entries**. The current audit reports 58 entries not yet in the screening register, 11 newly registered candidates DISC-069–DISC-079, and 16 provisional online/indexed evidence rows. None of these counts proves final inclusion or Q1 eligibility.
- `data/primary-study-comparison-matrix.csv` is a focused 208-row subset covering 43 candidate IDs; it is not a completed matrix for all 505 evidence rows.
- The broad review remains structured around the original processing–cost–performance continuum across eight material classes. `DISC-022` remains deferred in the historic broad-review register, not screened or excluded.

### Semester paper — approved separate scope
- Title: **Assessing the Low-Cost Potential of Non-Conventional Engineered Adsorbents for Ciprofloxacin and Tetracycline Removal from Aqueous Media**.
- Scope: selected graphene-based adsorbents (GO/rGO and functionalized derivatives) plus selected graphene-bearing composites; target antibiotics CIP and TC only. “Green” or “waste-derived” is not the defining theme. Low cost is assessed, not assumed.
- `data/semester-paper-candidate-register.csv`: **44 candidate records**.
- `evidence/semester-paper/SEMESTER_CORE_EVIDENCE_EXTRACTION.csv`: **39 active unique dedicated evidence records** (checked 2026-10-30 after consolidating the duplicate SEM-037 PRB entry into EV-SEM-040). Reused master-corpus evidence remains cross-referenced, not duplicated.
- `data/semester-main-corpus-crosswalk.csv` maps the semester candidates to the master register and BibTeX queue. SEM-016↔CORP-024, SEM-032↔CORP-015, and SEM-038↔CORP-031 are confirmed master-corpus links; SEM-020 now has an exact-DOI BibTeX queue match; SEM-039 and SEM-040 also have source-linked evidence.
- Target: approximately **50 distinct works actually cited**, subject to eligibility and evidence quality. This target is separate from the broad review's ~60/~150 planning targets.
- The user has asked not to download or upload more papers at present. Continue from existing Library files, master evidence, and accessible source text; no new download request is active.

### Non-negotiable controls
- Keep broad and semester workstreams separate and preserve the original broad-review manuscript.
- Do not count candidates/evidence rows as accepted references.
- Do not rank fitted qmax against observed qe, model-fitted qe, removal percentage, or column metrics as though they were the same quantity.
- Treat cost as unproven when no comparable process-cost inventory is reported.
- Keep SJR/JCR, publication year, category and quartile distinct; do not impose a Q1-only semester rule unless explicitly required.
- The Results/Discussion draft’s 15 citation keys remain reconciled against the 173-entry export. A separate Introduction/Scope draft adds four contextual sources with exact keys already present in that export; the curated working bibliography now has 19 entries across both files. The claim-to-evidence matrix maps 15 empirical study claims plus four contextual sources. Thirteen additional eligible candidates have a DOI intake queue, but none was present by DOI/title in the five exports checked and none has a verified key yet. The approximately 50-work target and final integrated style/claim audit remain pending.

## Current semester-paper working files

- `data/semester-condition-labelled-comparison.csv` — a 26-row condition-labelled comparison of selected empirical CIP/TC endpoints, with fitted and observed metrics separated and data-quality/cost caveats preserved.
- `data/semester-study-inclusion-shortlist.csv` — candidate-level disposition for the 44-row register (duplicate alias, context-only/review, provisional empirical, held quantitative metrics, and cross-linked master evidence clearly separated).
- `data/semester-evidence-readiness-audit.csv` — metric, source-access, cost and regeneration QA for all 39 active dedicated evidence records.

## Citation readiness

- `data/semester-bibtex-citation-linkage-audit.csv` — candidate-level verified citation-key coverage, with 13 selected candidate DOIs marked absent from the five exports checked on 30 October 2026.
- `docs/SEMESTER_CITATION_LINKAGE_AUDIT.md` — explains verified key matches and how to handle unmatched candidates safely. The 2026-10-30 continuation additionally checks five available BibTeX exports.

## 2026-10-30 continuation closeout

- SEM-042: accepted-manuscript column mass remains physically impossible (100 g in approximately 1.178 cm³); continuous-flow metrics remain quarantined, while batch evidence is retained cautiously.
- SEM-043: publisher-preview claims are separated from detailed Methods/Table 1 values extracted from a non-publisher mirror; a condition-labelled CIP/GO baseline is now present.
- SEM-044: publisher abstract and figure previews support the reported Langmuir-fit and qualitative pH findings; the 1111 mg/g CIP qmax remains excluded from condition-matched ranking because operating conditions and full tables are inaccessible.
- No exact DOI or normalized-title match for SEM-042, SEM-043 or SEM-044 was found in any of five available Library BibTeX exports (173, 164, 164, 61 and 31 entries). These candidates are not citation-ready; no keys were guessed.
- See [the 30 October closeout log](logs/2026-10-30-sem-042-044-and-citation-closeout.md) for source decisions, counts and repository updates.

## Current manuscript draft

- `manuscript/SEMESTER_INTRODUCTION_AND_SCOPE_V1.md` — working Introduction and Scope draft with four contextual source keys; includes an editorial hold for the final reproducible search-method details.
- `manuscript/SEMESTER_RESULTS_AND_DISCUSSION_V1.md` — source-cautious Results and Discussion working draft using 15 DOI-verified citation keys, explicit evidence-record tags and source-quality caveats; not submission-ready.
- `data/semester-citation-expansion-shortlist.csv` and `references/semester-zotero-doi-import-queue-2026-10-30.txt` — 13 candidate DOIs prioritized for Zotero metadata reconciliation; no guessed citekeys.
- `data/semester-mechanism-evidence-matrix.csv` and `data/semester-practical-feasibility-matrix.csv` — evidence-weighted synthesis of the 15 currently discussed empirical studies. Mechanism grades distinguish measured/spectral evidence from author interpretation; cost and recovery gaps remain explicit.

## Repository map

- `docs/PROJECT_CHARTER.md` — scope, contribution and research questions
- `docs/MATERIAL_TAXONOMY.md` — material classes and stage-boundary rules
- `docs/RESEARCH_WORKFLOW.md` — paper-to-evidence process and quality checks
- `docs/CORPUS_RESET_AND_RESTART.md` — unified full-corpus restart, including the original seven papers
- `docs/LITERATURE_DISCOVERY_PLAN.md` — structured plan and logs for finding papers missing from the downloaded library
- `docs/PAPER_INGESTION_AND_EXTRACTION.md` — how to obtain, read, extract, verify and record each paper's evidence
- `docs/AUTOMATION_ROADMAP.md` — $0-first workflow; no n8n or paid automation dependency
- `docs/24_DAY_PLAN.md` — original sprint plan and progress status
- `data/master-evidence.csv` — condensed index of the initial core papers
- `data/master-evidence-detailed.csv` — the full 15-column evidence matrix for the seven core papers
- `data/source-caveats.csv` — source-specific inconsistencies and next verification actions
- `data/paper-screening-register.csv` — candidate screening and verification status
- `references/README.md` — single-collection Zotero intake and full-corpus bibliography export instructions
- `data/corpus-screening-template.csv` — blank screening schema for the unified corpus
- `data/corpus-screening-register.csv` — live unified screening register; 111 candidate rows as of 2026-10-29; candidates are not automatically accepted references
- `docs/LITERATURE_DISCOVERY_PLAN.md` — how we will find missing literature to complete the bibliography against the original outline
- `docs/REFERENCE_TARGET_PLAN.md` — planning funnel and coverage map for a defensible ~150-reference journal version
- [`manuscript/ORIGINAL_OUTLINE_AS_SUPPLIED.md`](manuscript/ORIGINAL_OUTLINE_AS_SUPPLIED.md) — normalized Markdown transcription of the supplied original PDF outline
- [`manuscript/REVIEW_OUTLINE.md`](manuscript/REVIEW_OUTLINE.md) — current working outline; includes a standalone Section 4 on mechanisms of antibiotic adsorption
- `logs/` — dated decisions, actions and unresolved questions

## Outline decision

The supplied outline is preserved separately so the original framework is not overwritten. In the working manuscript outline, adsorption kinetics/isotherms are in Section 3 and **mechanisms are promoted to standalone Section 4**; techno-economic evaluation, implementation, challenges, and conclusions are renumbered to Sections 5–8. The mechanism section includes an evidence-weighted matrix and explicit checks against conflating adsorption with catalytic degradation.

## Historical status snapshot (2026-10-24; superseded by the 2026-10-27 checkpoint and 2026-10-29 live status above)

- The original seven-paper matrix (`data/master-evidence-detailed.csv`) and caveats (`data/source-caveats.csv`) are preserved as historical seed records. Their values and mechanisms are **provisional until re-verified against the original full texts**. The formatted `.xlsx` workbook remains a separate working artifact.
- Initial bibliography audit: 31 records parsed; no exact duplicate DOI or normalized title was detected. Eight entries lack abstracts in the export. The Pinheiro chitosan/alginate record and Mohammed-Ridha publication year were corrected/flagged using publisher or PubMed records, and the original export should not be treated as complete evidence.
- Literature intake is restarting from one Zotero collection, `Antibiotic Adsorption Review — Full Corpus`, containing the original seven plus all other relevant downloads. No manual material-by-material reorganisation is required; classification happens during screening. The uploaded Better BibTeX export currently contains 31 downloaded records; it is a starting library, not the complete bibliography. Additional structured literature discovery is required.
- The outline's core class list is retained: raw lignocellulosic biomass, natural clays, unmodified biopolymers, standard biochar, chemically modified biochars, atomically doped biochars, activated carbon, and nano-engineered carbons.
- The boundary between the outline's Stage 2 and the current Zotero tag `STAGE-2-MODIFIED` remains unresolved; keep material category and processing route explicit in evidence records.
- Q1 status for several recent candidate papers has not been fully verified; candidates must not be treated as accepted until checked.

## Historical update snapshot (2026-10-27; superseded by live status above)

The following dated status was accurate at the time of the 2026-10-27 checkpoint. For current counts, use the live status section at the top of this README and the 2026-10-29 context-audit log.

## Working loop

**Discover → screen → verify journal and source → retrieve full text → extract evidence → reconcile units/conditions → draft → cite through Zotero → audit claims.**

Every work session should end with a visible GitHub change or a clearly recorded blocker. The automation plan is $0-first: no n8n, paid automation service, or paid API is a prerequisite.


## Download-ready literature pool (2026-10-27)

- **[Download the 250-record planned literature pool (CSV)](data/planned-download-pool.csv)** — current register inventory plus 183 new DOI-linked discovery leads. The file separates already represented items from new downloads, includes DOI/PMC/PubMed links, and marks screening/quartile status.
- **[How to use the pool](docs/PLANNED_DOWNLOAD_POOL_GUIDE.md)** — batches, access notes, and how the pool relates to the final 60/150 cited-work targets.

The pool is not a final bibliography. New leads require full-text screening; Q1 status must be audited separately. Historical note: DISC-022 was deferred at the 2026-10-27 pool snapshot. The user has since paused further downloads; no PDF request is active.


## Multi-chat PDF upload workflow (2026-10-28)

For newly downloaded papers being uploaded in batches of three across branched chats, use [`docs/MULTI_CHAT_PDF_BATCH_PROTOCOL.md`](docs/MULTI_CHAT_PDF_BATCH_PROTOCOL.md) and track the first ten batches in [`data/new-paper-upload-batch-tracker.csv`](data/new-paper-upload-batch-tracker.csv). Each branch writes unique batch-specific staging files; the central chat consolidates these into master evidence and screening data to avoid parallel overwrites. GitHub remains the source of truth, and `DISC-022` was deferred in the historical 2026-10-28 batch-protocol snapshot. The user has since paused further downloads; no full-text request is active.


**Batching clarification (2026-10-28):** The ten-chat limit means up to ten upload chats at once, not 30 papers total. Process batches in successive waves, consolidating each wave before reusing the ten chat slots. The tracker now reserves 100 sequential batches (300 paper slots) and can be extended further.


## Approved semester paper scope (2026-10-28; separate workstream)

**Working title:** *Assessing the Low-Cost Potential of Non-Conventional Engineered Adsorbents for Ciprofloxacin and Tetracycline Removal from Aqueous Media.*

The scope is approved and locked in `docs/SEMESTER_PAPER_SCOPE_PROPOSAL.md`. Include selected graphene-based adsorbents and selected graphene-bearing composites, with CIP and TC as the two targets. “Green”, “sustainable”, and “waste-derived” are not defining themes. Low cost is assessed from reported preparation, reagent/energy burden, recovery, regeneration and real-water/application evidence; it is not inferred from material origin or high qmax.

The semester candidate register has 44 rows: 43 distinct candidate studies after excluding SEM-041 (duplicate alias of SEM-026); 42 have valid DOI strings and SEM-021 still needs DOI verification. The dedicated evidence CSV has 39 active unique records after the SEM-037 duplicate was consolidated into EV-SEM-040 (verified 2026-10-30); reusable master-corpus evidence is linked in `data/semester-main-corpus-crosswalk.csv`. The approximate 50-reference target is counted as distinct works actually cited, not candidates or evidence rows. No new paper download/upload is requested from the user at this stage.


Current semester-paper evidence register: **39 active unique evidence rows** after consolidation of the duplicate SEM-037 PRB record into EV-SEM-040 (verified 30 October 2026). These include provisional abstract-level entries and one DFT-only theory/context row, so they are not a count of accepted empirical studies or cited bibliography works.

## Semester manuscript — unified working draft

- `manuscript/SEMESTER_MANUSCRIPT_WORKING_V1.md` — the single continuous semester-paper draft (Introduction, scope/search/evidence method, Results and Discussion, mechanism synthesis, practical feasibility and conclusions). It documents the 28 October focused discovery pass and 28–30 October source audits without claiming a systematic/PRISMA search.
- `references/semester-manuscript-cited-references.bib` — 19 distinct references currently cited in the unified draft; contextual sources are distinguished from the 15 target-material primary-study records.
- The separate Introduction/Scope and Results/Discussion files are retained as component drafts/source history. The unified manuscript is the current integration point.


## New semester candidate additions — 30 October 2026

- SEM-045 / EV-SEM-041: 2026 magnetic GO-supported Co-MOF for tetracycline; full RSC/PMC text audited, kinetic qe mass-balance flag and 10-cycle methanol regeneration.
- SEM-046 / EV-SEM-042: 2026 ZrO2–Fe3O4/GO for ciprofloxacin; AJOL primary PDF text extracted, pharmaceutical-effluent testing, qe and real-sample arithmetic conflicts.
- Both are in the candidate/evidence pool and expanded 16-DOI Zotero queue, not yet in the 19-work cited manuscript. No guessed citekeys.


- SEM-047 / EV-SEM-043: 2026 magnetic GO/NH2-UiO-66(Zr)/alginate TC composite; abstract-level candidate with river-water and ten-cycle claims. Its publisher corrigendum is verified as a funding-statement-only correction; full paper remains access-gated.

- DOI intake queue currently contains 16 unique records; the three supplementary 2026 DOIs were checked against the five mounted BibTeX exports on 31 October and had no exact matches. SEM-047 remains P2/abstract-only.

- SEM-030 / EV-SEM-031: GO/[Ni(DMG)]n for CIP (2026) is an existing registered abstract-level P2 candidate. Its DOI is absent from the five mounted BibTeX exports; it is now in the expanded Zotero intake queue. The 2024 rGO/CIP/TC DFT study SEM-013 remains theory-only, not empirical adsorption evidence.

- A 31 October broad-corpus cross-check found no additional unregistered empirical graphene/CIP/TC study; three existing primary overlaps are already mapped to SEM-038, SEM-016 and SEM-032. Review-only matches were not counted as primary studies.

## Core study comparison table

- `manuscript/SEMESTER_TABLE_1_CORE_STUDY_COMPARISON_V1.md` — 15-study comparison of target/material, operating context, observed endpoint, fitted parameter, recovery and evidence caveat. The SEM-038 N-rGO row is explicitly cross-referenced to master records EV-B10-004–EV-B10-009, not duplicated.
- `data/semester-condition-labelled-comparison.csv` — condition-labelled machine-readable source for the study comparison (27 rows, including the SEM-038 master-evidence cross-reference).
