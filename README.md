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

## Repository status baseline (2026-10-29; continuation audited through 2026-10-31)

This repository now contains **two related but separate workstreams**. Do not combine their candidate counts, reference targets, evidence rows, or manuscript scopes.

### Broad antibiotic-adsorption review
- `data/corpus-screening-register.csv`: **111 unique candidate records**.
- `data/corpus-evidence.csv`: **505 unique evidence rows**. These are evidence findings, not papers or accepted references; provisional and staged rows remain visibly flagged.
- `data/journal-quartile-audit.csv`: **45 journal metadata records** in the shared inventory (broader-review metadata only; never a semester-paper screening criterion).
- The 2026-10-29 Better BibTeX processing queue has **164 entries**. The current audit reports 58 entries not yet in the screening register, 11 newly registered candidates DISC-069–DISC-079, and 16 provisional online/indexed evidence rows. None of these counts proves final inclusion or Q1 eligibility.
- `data/primary-study-comparison-matrix.csv` is a focused 208-row subset covering 43 candidate IDs; it is not a completed matrix for all 505 evidence rows.
- The broad review remains structured around the original processing–cost–performance continuum across eight material classes. `DISC-022` remains deferred in the historic broad-review register, not screened or excluded.

### Semester paper — approved separate scope
- Title: **Assessing the Low-Cost Potential of Non-Conventional Engineered Adsorbents for Ciprofloxacin and Tetracycline Removal from Aqueous Media**.
- Scope: selected graphene-based adsorbents (GO/rGO and functionalized derivatives) plus selected graphene-bearing composites; target antibiotics CIP and TC only. “Green” or “waste-derived” is not the defining theme. Low cost is assessed, not assumed.
- `data/semester-paper-candidate-register.csv`: **51 candidate rows representing 50 DOI-defined works** (excluding the SEM-041 alias).
- `evidence/semester-paper/SEMESTER_CORE_EVIDENCE_EXTRACTION.csv`: **46 active dedicated evidence records** (latest check 31 October 2026). Reused master-corpus evidence remains cross-referenced, not duplicated.
- `data/semester-main-corpus-crosswalk.csv` maps the semester candidates to the master register and BibTeX queue. SEM-016↔CORP-024, SEM-032↔CORP-015, and SEM-038↔CORP-031 are confirmed master-corpus links; SEM-020 now has an exact-DOI BibTeX queue match; SEM-039 and SEM-040 also have source-linked evidence. The primary-PDF mass-balance recheck on31Oct2026 confirmed a strict80mg/g ceiling for Fig2a and a much lower≈8–25mg/g ceiling in Fig2c versus plotted TC≈88–90mg/g; Table1/Fig2 are single-analyte tests and Fig3f is the separate competition test. See [SEM-038 source audit](logs/2026-10-31-sem038-original-pdf-mass-balance-recheck.md).
- Target: approximately **50 distinct works actually cited**, subject to eligibility and evidence quality. This target is separate from the broad review's ~60/~150 planning targets.
- The user has asked not to download or upload more papers at present. Continue from existing Library files, master evidence, and accessible source text; no new download request is active.

### Non-negotiable controls
- Keep broad and semester workstreams separate and preserve the original broad-review manuscript.
- Do not count candidates/evidence rows as accepted references.
- Do not rank fitted qmax against observed qe, model-fitted qe, removal percentage, or column metrics as though they were the same quantity.
- Treat cost as unproven when no comparable process-cost inventory is reported.
- Semester paper: journal quartiles are explicitly out of scope. Do not audit, rank, prioritise, include or exclude SEM candidates by SJR/JCR/CiteScore quartile. The shared journal-ranking audit is not an eligibility input for this workstream. Broad-review ranking rules remain separate.
- The unified manuscript still cites 19 distinct works (15 target-material primary-study records plus four contextual sources); all 19 keys match the 19-entry curated bibliography. The semester register has 51 rows representing 50 DOI-defined studies after excluding the SEM-041 alias of SEM-026. The dedicated evidence extraction has 46 records; candidate/evidence counts are not final inclusion counts. The Zotero DOI queue has 21 unique records. The latest complete My Library export (173 entries) was also checked by exact DOI and normalized title: none of the 21 queue records matched, while all 19 existing manuscript citation keys were present. Add metadata only for candidates selected for citation; do not guess keys. The approximately 50-work target and final integrated style/claim audit remain pending.

## Current semester-paper working files

- `data/semester-remaining-work-register.csv` — 51-row candidate-specific remaining-work register, reconciled on 31 October 2026; see [the continuation reconciliation log](logs/2026-10-31-continuation-register-reconciliation.md).
- `logs/2026-10-31-manuscript-status-reconciliation.md` — reconciles the manuscript/README counts, 21-DOI citation-audit note and the remaining SEM-035 source-access status.
- `data/journal-quartile-audit.csv` — shared journal metadata for the broader review only. Journal quartiles are not used in semester-paper screening; see [the scope clarification](logs/2026-10-31-semester-quartile-out-of-scope.md).
- `data/semester-condition-labelled-comparison.csv` — a 31-row condition-labelled comparison of selected empirical CIP/TC endpoints, with fitted and observed metrics separated and data-quality/cost caveats preserved.
- `data/semester-study-inclusion-shortlist.csv` — candidate-level disposition for the 51-row register (duplicate alias, context-only/review, provisional empirical, held quantitative metrics, and cross-linked master evidence clearly separated).
- `data/semester-evidence-readiness-audit.csv` — metric, source-access, cost and regeneration QA for 47 rows: 46 dedicated evidence records plus one SEM-038 cross-reference to existing master-corpus evidence.

## Citation readiness

- `data/semester-bibtex-citation-linkage-audit.csv` — candidate-level citation-key linkage; all 21 DOI-queue records were checked by DOI and normalized title against the latest complete 173-entry My Library export, with no matches. All 19 existing manuscript keys were confirmed present. See the expanded [citation-linkage audit](docs/SEMESTER_CITATION_LINKAGE_AUDIT.md).
- `docs/SEMESTER_CITATION_LINKAGE_AUDIT.md` — explains verified key matches and how to handle unmatched candidates safely, including the latest complete My Library export check.

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
- `data/original-pdf-batch-attachment-crosswalk.csv` maps all 60 PDF records supplied in original Batches 01–20 to Library filenames, candidate IDs, DOI, extracted evidence IDs and batch notes; see `logs/2026-10-31-original-pdf-batch-integrity-audit.md` for the integrity audit.
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

The semester candidate register has **51 rows representing 50 DOI-defined studies**, after excluding SEM-041 as a duplicate alias of SEM-026. The dedicated evidence CSV has **46 active evidence records**; reusable master-corpus evidence is linked in `data/semester-main-corpus-crosswalk.csv`. The approximate 50-reference target is counted as distinct works actually cited, not candidates or evidence rows. Zotero metadata reconciliation and a fresh Better BibTeX export remain the next citation-workflow dependency.


Current semester-paper evidence register: **46 active unique dedicated evidence rows** after consolidation of duplicate SEM-037 PRB evidence and addition of EV-SEM-041–047 (verified 31 October 2026). The readiness audit has 47 rows because SEM-038 reuses six existing master-corpus evidence IDs through a cross-reference, not a duplicate extraction. These include provisional abstract-level entries and one DFT-only theory/context row, so they are not a count of accepted empirical studies or cited bibliography works.

## Semester manuscript — unified working draft

- `manuscript/SEMESTER_MANUSCRIPT_WORKING_V1.md` — the single continuous semester-paper draft (Introduction, scope/search/evidence method, Results and Discussion, mechanism synthesis, practical feasibility and conclusions). It documents the 28 October focused discovery pass and 28–30 October source audits without claiming a systematic/PRISMA search.
- `references/semester-manuscript-cited-references.bib` — 19 distinct references currently cited in the unified draft; contextual sources are distinguished from the 15 target-material primary-study records.
- The separate Introduction/Scope and Results/Discussion files are retained as component drafts/source history. The unified manuscript is the current integration point.


## New semester candidate additions — 30 October 2026

- SEM-045 / EV-SEM-041: 2026 magnetic GO-supported Co-MOF for tetracycline; full RSC/PMC text audited, kinetic qe mass-balance flag and 10-cycle methanol regeneration.
- SEM-046 / EV-SEM-042: 2026 ZrO2–Fe3O4/GO for ciprofloxacin; official AJOL PDF audited. All three Figure 5 qe values exceed the stated-condition feed-mass ceiling; Langmuir q_m is from the poorer-fitting model; real-effluent concentration pair computes 76.0%, not the reported 90.75%. AJOL Vol.40 No.5 metadata conflicts with an extracted PDF running footer marked 40(6).
- Both are in the candidate/evidence pool and expanded 21-DOI Zotero queue, not yet in the 19-work cited manuscript. No guessed citekeys.


- SEM-047 / EV-SEM-043: 2026 magnetic GO/NH2-UiO-66(Zr)/alginate TC composite; abstract/article-preview candidate with river-water and ten-cycle claims. Publisher corrigendum DOI10.1016/j.ijbiomac.2026.154444 says the Funding statement should be removed entirely and does not alter results/conclusions. PubMed EFR metadata mislinks to unrelated DOI10.1016/j.ijbiomac.2026.154185; publisher cross-link is authoritative. Full Methods/results tables remain access-gated.

- The Zotero DOI intake queue now contains21 unique original-study DOIs. Twenty-one DOIs are now in the queue; the 31 October five-export check found no exact matches for the new candidate DOIs. Search Zotero by DOI before metadata addition. SEM-047/SEM-048 remain abstract/preview-level candidates.

- SEM-030 / EV-SEM-031: GO/[Ni(DMG)]n for CIP (2026) is an existing registered abstract-level P2 candidate. Its DOI and normalized title are absent from the latest complete 173-entry My Library export; it remains in the Zotero intake queue. The 2024 rGO/CIP/TC DFT study SEM-013 remains theory-only, not empirical adsorption evidence.

- A 31 October broad-corpus cross-check found no additional unregistered empirical graphene/CIP/TC study; three existing primary overlaps are already mapped to SEM-038, SEM-016 and SEM-032. Review-only matches were not counted as primary studies.

- **SEM-039 / EV-SEM-015:** 2017 CNF/GO aerogel TC adsorption source QA completed 31 October 2026. Figure7 TC removal is82.1%, but the caption does not give a specific C0/pH/dose; keep it out of condition-matched ranking. PSO fitted qe84.8mg/g and Langmuir fitted qm454.6mg/g (454.5mg/g in conclusion) are separate model outputs. TC removal after ten cycles is78.9% vs82.1% initially. Preparation uses1000W stated-output ultrasound and48h freeze-drying; no normalized cost/LCA or real-water test is reported. See [SEM-039 source audit](logs/2026-10-31-sem039-cnfg-aerogel-source-audit.md).

- **SEM-034 / EV-SEM-027:** the 31 October ESI audit confirmed the optimum point (3mg,30s,pH7,0.2ppm,25°C) and exposed main-text/ESI mismatches in pH and isotherm concentration ranges. TC removal is reported as94.1/93.91/93.94%; the derived qe is1.252–1.255mg/g against a1.333mg/g feed ceiling, close to PSO fitted qe1.2681mg/g. q_m remains separately model-fitted at60.24/62.50/64.10mg/g for30/40/50°C. Waste dry-cell graphite is an input to GO, but Aqua Regia, Hummers reagents and Co/Fe salts remain in the process; no real-water or normalized cost evidence. See [SEM-034 primary and ESI audit](logs/2026-10-31-sem034-main-and-esi-source-audit.md).

- **SEM-006 / EV-SEM-008:** primary main-text audit completed 31 October 2026. DDMGO single-solute kinetics at C0=50mg/L,m/V=.09g/L,pH3,30°C yield PSO-fitted qe=294.12mg/g (TC) and111.73mg/g (CIP), both below the555.6mg/g feed ceiling; not measured qe/qmax. TC pH optimum≈3 vs CIP≈8. In binary tests, TC q_b/q_s falls to0.39–0.90 with CIP, while CIP remains near1.00 with TC. Four0.01M NaOH cycles keep removal above78%, but no TC-specific capacity retention. Freundlich fits better than Langmuir; SI Tables S1–S3 remain unavailable. No real-water or cost/energy inventory. See [SEM-006 source audit](logs/2026-10-31-sem006-ddmgo-main-text-source-audit.md).

- **SEM-010 / EV-SEM-004:** source re-audit confirms an unresolved same-condition conflict: 99% optimum removal at2mg/L CIP/40mL/20mgL−1 GO implies qe99mg/g, while Table4 experimental qe78.82mg/g implies78.82% removal; PSO fitted qe79.36mg/g. The conclusion's GO dosage20g/L conflicts1000× with the abstract/Fig3/Results dose20mg/L. New verified reuse evidence: methanol regeneration, seven cycles,92% CIP removal after cycle7 (not capacity retention). Nonlinear Langmuir qm=419.62/434.56/441.44mg/g at30/40/50°C are fitted asymptotes. The waste-derived carbon precursor still requires HCl/HNO3, strong acid/oxidant, long wash/dry steps; no normalized cost or real-water test. See [SEM-010 targeted source audit](logs/2026-10-31-sem010-zinc-carbon-go-source-audit.md).
- **SEM-016 / EV-SEM-012:** original Library ACS Omega PDF audit completed31Oct2026. Table1 experimental qₑ values and prose removal percentages disagree at same nominal concentration/temperature/dose conditions: the 10µmol/L endpoint implies90.90% vs reported97.32%; at50µmol/L/25°C qₑ237.12µmol/g implies94.85% vs96.53%; at25→40°C the Table1 qₑ values imply94.85→97.70% vs prose96.53→99.66%. Hold the paired endpoints from quantitative ranking; do not silently reconcile. Langmuir qₘ=1000µmol/g (331.35mg/g) is fitted to separate50–1000µmol/L isotherm series. Five reuse cycles retain95.78% of qₑ (239.39→229.29µmol/g); DMF+1M HCl releases>99.14% by240min. Graphite precursor is commercial, not waste-derived; strong acids/oxidants and DMF regeneration are uncosted. See [SEM-016 source audit](logs/2026-10-31-sem016-sulfonated-go-primary-pdf-audit.md).
- **SEM-018 / EV-SEM-007:** official RSC full-text PDF audit completed31Oct2026. At2mg/L,20mL,2mg adsorbent,pH5,25°C,25min,96.04% removal implies derived qe19.208mg/g, below the20mg/g feed ceiling. The linear PSO qe fit is19.5008mg/g (R²=.9999), while the nonlinear PSO fit is19.3522mg/g (R²=.8004). Abstract54.73mg/g is the linear Langmuir fitted qmax at50°C; the nonlinear qmax is48.4744mg/g, and at50°C nonlinear Freundlich R²=.9609 exceeds nonlinear Langmuir=.9425. The concentration-response section says99.43% at0.2mg/L to44.99% at10mg/L, then labels2mg/L optimum. Ten methanol reuse cycles reduce removal≈96→92%, not measured q-capacity retention. Spent Li-ion graphite is waste-derived, but Hummers oxidants/acids, large Fe-salt loading, alkaline precipitation and drying remain uncosted. See [SEM-018 source audit](logs/2026-10-31-sem018-cmc-mgo-source-audit.md).

## Core study comparison table

- `manuscript/SEMESTER_TABLE_1_CORE_STUDY_COMPARISON_V1.md` — 15-study comparison of target/material, operating context, observed endpoint, fitted parameter, recovery and evidence caveat. The SEM-038 N-rGO row is explicitly cross-referenced to master records EV-B10-004–EV-B10-009, not duplicated.
- `data/semester-condition-labelled-comparison.csv` — condition-labelled machine-readable source for the study comparison (31 rows, including the SEM-038 master-evidence cross-reference).
- `manuscript/SEMESTER_FIGURE_1_SCOPE_TAXONOMY_V1.md` — editable Mermaid source for the original scope/material-taxonomy figure, based on the approved scope proposal.
- `manuscript/SEMESTER_FIGURE_2_PROCESS_RECOVERY_COST_BOUNDARY_V1.md` — editable Mermaid source for the original preparation–adsorption–recovery–cost-boundary schematic.
- `manuscript/SEMESTER_FIGURE_3_MECHANISM_EVIDENCE_SCHEMATIC_V1.md` — editable Mermaid source for the conceptual CIP/TC–graphenic-surface interaction map, with evidence and inference limits.
- `manuscript/SEMESTER_FIGURE_4_PERFORMANCE_PROCESS_RECOVERY_COST_FRAMEWORK_V1.md` — editable Mermaid source for the evidence-based performance–preparation–recovery–cost assessment framework.


## Additional studies screened — 31 October 2026

- **SEM-002 / EV-SEM-017:** abstract-level study audit completed31Oct2026. Publisher/PubMed identify GOS tested against ciprofloxacin (CPN), tetracycline (TCN) and doxycycline (DCN); fitted qmax order CPN≫DCN>TCN, with CPN up to173.4mg/g. Hill/Toth are the reported equilibrium models; Elovich kinetics for CPN and PSO for TCN/DCN. Abstract describes pH≈6–7 and contact100–200min as optimal, and lower fitted capacities at45°C than25°C. No numeric TC-specific qmax/qe or complete conditions are exposed; do not infer from CPN or ordinal ranking. No matched full-text PDF was found in the existing Library search. See [SEM-002 abstract-level audit](logs/2026-10-31-sem002-abstract-level-source-audit.md).

- **SEM-048 / EV-SEM-044:** rGO/Pr6O11 for CIP; publisher preview now exposes synthesis and batch-method snippets. Optimum removal is 88.0% in abstract vs 88.3% in conclusion at C0=10mg/L, dose0.4g/L, pH6.6, 298K, 160min; calculated qe≈22.0–22.075mg/g, feed ceiling25mg/g. Langmuir q_m=85.5mg/g is fitted; ethanol-water/0.1M HCl regeneration reports85.8% capacity retention after4 cycles. pH optimum6.6 is not among explicitly listed pH test points2,4,8,10; full Results tables remain access-gated.
- **SEM-049 / EV-SEM-045:** Alg-Cu@GO@MOF-525 for TC; full open-access article. High reported capacity endpoints require reconciliation of conflicting dose and concentration details.
- **SEM-050 / EV-SEM-046:** GO–TOPO:LevA DES membrane for TET; full article and supplements reviewed. It provides the strongest current active-layer cost/carbon, membrane, leaching and spiked-municipal-water evidence, but the batch qe denominator and life-cycle boundary remain caveated. The 31 October targeted audit now records single-solute and four-drug spiked-MWW results separately, six-cycle NaOH regeneration, TOC-based leaching tests, and the USD/m² and CO2-eq estimates as active-layer-only (not full treatment economics); batch qe22.7±0.6mg/g remains quarantined pending feed-mass reconciliation. See [SEM-050 targeted source audit](logs/2026-10-31-sem050-targeted-source-audit.md).
- **SEM-051 / EV-SEM-047:** targeted publisher-indexed source audit completed 31 October 2026. Condition-specific 94.93% removal at200mg/L,20mL,20mg,pH4,120min implies derived qe≈189.86mg/g; abstract Langmuir qmax basis5mg conflicts with Methods/Fig8/Table3 captions using20mg. Hill fits best, but author cost uses linear Langmuir qmax. Desorption Methods specify0.1M acid/base while Results/Figure10 report1.0M; these are desorption efficiencies, not capacity retention. USD1.95/g-TC is an author laboratory chemical+energy estimate with a functional-unit mismatch (1g/L application statement vs tested maximum250mg/L), not treatment cost/m³. See [SEM-051 targeted source audit](logs/2026-10-31-sem051-targeted-source-audit.md).

- SEM-050 is the strongest current cost-evidence candidate, but its USD 2.5–6.8/m² estimate is for active-layer material only; its 0.02–0.08 kg CO2-eq/m³ figure is a throughput-normalized footprint, not financial treatment cost. Full module and life-cycle boundaries remain incomplete.

