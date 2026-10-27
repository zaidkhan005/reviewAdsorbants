# Migration handoff — Antibiotic Adsorption Review
**Prepared:** 2026-10-27  
**Purpose:** Transfer the project into a fresh ChatGPT conversation after the current chat reached its maximum length. Treat this handoff and the current GitHub repository as the continuity record.

## 1. Start here / source of truth

Repository: https://github.com/zaidkhan005/reviewAdsorbants

- Project checkpoint: [logs/2026-10-27-project-checkpoint.md](../logs/2026-10-27-project-checkpoint.md)
- 24-day sprint: [docs/24_DAY_PLAN.md](24_DAY_PLAN.md)
- Research workflow: [docs/RESEARCH_WORKFLOW.md](RESEARCH_WORKFLOW.md)
- Working outline: [manuscript/REVIEW_OUTLINE.md](../manuscript/REVIEW_OUTLINE.md)
- Original outline transcription: [manuscript/ORIGINAL_OUTLINE_AS_SUPPLIED.md](../manuscript/ORIGINAL_OUTLINE_AS_SUPPLIED.md)
- Material taxonomy: [docs/MATERIAL_TAXONOMY.md](MATERIAL_TAXONOMY.md)
- Evidence extraction protocol: [docs/PAPER_INGESTION_AND_EXTRACTION.md](PAPER_INGESTION_AND_EXTRACTION.md)
- Citation and claim rules: [manuscript/CITATION_AND_CLAIM_RULES.md](../manuscript/CITATION_AND_CLAIM_RULES.md)

**System of record:** GitHub stores project status, screening decisions, evidence, caveats, logs and manuscript drafts. Zotero is the reference manager and home for bibliographic records/local PDFs. Do not treat chat history as the only record.

## 2. Project aim and core argument

The review compares antibiotic removal by adsorption through a **processing–cost–performance continuum**: raw/minimally processed biomass and waste-derived sorbents; natural clays and unmodified biopolymers; modified biopolymers/composites; biochar and modified/doped biochar; activated carbon; engineered/nano-carbon adsorbents.

The contribution is **not** a league table sorted by the largest reported qmax or removal percentage. The review should connect preparation/processing burden, performance under stated conditions, mechanisms and evidence strength, regeneration/desorption, real-water performance, fixed-bed/continuous-flow evidence, cost/energy/LCA, media recovery, and spent-sorbent/end-of-life risks.

Keep material category separate from processing route. Do not silently combine raw, activated, chemically modified, doped, composite or nano-engineered materials.

## 3. Current repository state at migration

The latest checkpoint records:

- PDF intake completed through **Batch 20**. Do not assume the user has more downloaded PDF batches waiting to upload; the user said they had provided the papers they had downloaded.
- **312 source-linked evidence records** in `data/corpus-evidence.csv`. These are evidence findings, not 312 unique papers.
- **62 candidate rows** in `data/corpus-screening-register.csv`.
- **61/62** candidates have completed full-text screening. **DISC-022 is deferred**, not screened and not excluded, until the user supplies its full-text PDF.
- **64 source-caveat entries** in `data/source-caveats.csv`.
- **34 unique journal titles** in `data/journal-quartile-audit.csv`; first-pass journal-level audit is complete, but not every journal has the same level of authoritative/category-specific verification.
- `data/candidate-decision-audit.csv`: provisional role and quantitative guardrail for all 62 candidates; not final inclusion/exclusion.
- `data/screening-decision-adjudication-v1.csv`: 62 rows separating scope role, quantitative-use decision and ranking eligibility; still provisional.
- `data/primary-study-comparison-matrix.csv`: 208 target/material/stage groupings for primary-study evidence from 43 primary-study candidates; references 249 unique evidence IDs and retains source locations and caveats.
- `manuscript/COMPARATIVE_TABLES_V1.md`: five endpoint-separated comparison panels; working version.
- `manuscript/CONTINUUM_SYNTHESIS_V1.md`: cross-class synthesis draft.
- `manuscript/SECTION_2_1_RAW_BIOMASS_V1.md`: working draft for raw biomass / low-processed waste-derived sorbents.
- `manuscript/SECTION_2_2_CLAYS_BIOPOLYMERS_V1.md`: working draft for natural clays and biopolymers; verify exact filename/current contents before editing.
- The next planned material-class draft is biochar / modified biochar (Section 2.3, per working outline/plan). Section numbering should be checked against `manuscript/REVIEW_OUTLINE.md`, not guessed.
- Final inclusion/exclusion, fully reconciled condition-matched comparisons, final journal-eligibility rule, Zotero-formatted author–date citations, complete bibliography, and editorial completion remain unfinished.

## 4. Critical deferred item: DISC-022

DISC-022 = Mangla et al. (2022), “Critical review on adsorptive removal of antibiotics: Present situation, challenges and future perspective,” *Journal of Hazardous Materials* 425, 127946, DOI 10.1016/j.jhazmat.2021.127946.

The accessible publisher preview/abstract and metadata were checked, but the complete article/tables were not accessible. The user explicitly said they will send the PDF when they have it. **Do not ask the user to retrieve it again now, do not keep it in the active queue, and do not label it screened or excluded.** Keep its abstract-level metadata recorded. Resume full-text screening only when the user uploads it.

## 5. Citation concern raised by user — high priority

The user correctly asked: “You are writing everything and doing everything but how in the end the draft will have all the citations of different papers and everything?”

Answer/workflow must be explicit and transparent:

1. Every factual claim in the prose must map to one or more source-backed evidence records and a candidate/source identifier.
2. Working drafts currently use temporary candidate-ID DOI links such as `[CORP-005](https://doi.org/...)`. These are useful audit links, **not the final reference style**.
3. Before submission, map every cited candidate to the exact Zotero item and stable Better BibTeX citation key; use Zotero/Better BibTeX (or an exported citation workflow) to insert author–date in-text citations and generate the reference list in the target journal's style.
4. Do not simply replace a candidate ID with an author name by guesswork. Verify author spelling/order, year, title, journal, volume/pages/article number and DOI from the actual Zotero record/publisher metadata.
5. Primary-paper numerical claims must cite the original primary paper, not merely a review that repeats its numbers. Reviews are primarily for field mapping, context and citation mining.
6. For claims supported by multiple papers, cite the set that genuinely supports the sentence. Keep the citation close to the claim. Tables need source citations per row/entry and notes defining units/metrics/conditions.
7. Create a claim-to-source audit: manuscript sentence/table row → candidate ID → evidence ID(s) → page/table/figure in source → Zotero citation key → final citation. Run a missing-citation audit and a bibliography consistency audit (every in-text citation in references, and every reference cited or intentionally listed).
8. Never mark the manuscript publication-ready while temporary candidate-ID citations remain. Citation conversion is a required manuscript phase, not a cosmetic final touch.

The rules are in `manuscript/CITATION_AND_CLAIM_RULES.md`. It says original sources are required for numerical claims; raw/modified/composite materials must be distinct; removal %, observed uptake (qe), fitted qmax and column capacity must remain separate; units and conditions must be checked; and mechanisms must be labelled according to evidence strength.

## 6. High-priority evidence quality rules

- Separate percentage removal, observed uptake, fitted isotherm qmax, kinetic/model parameters and column/working capacity.
- Check mass-balance feasibility before using fitted capacities in comparisons.
- Record concentration, dose, volume, pH, temperature, contact time, matrix, competing solutes and model conditions.
- Distinguish synthetic water, spiked real water and unmodified real wastewater.
- Separate adsorption from catalytic oxidation, photodegradation, biodegradation, membrane rejection and other processes.
- Treat mechanism claims as experimentally supported, model-inferred, author-proposed or uncertain.
- Do not infer low cost/sustainability just because a material is waste-derived. Record preparation chemicals, energy, yield, washing/neutralization, regeneration, recovery, leaching and end-of-life.
- Q1 eligibility is independent of whether the paper was read. Record provider/system, ranking year, category, quartile and source URL. SJR and JCR are different ranking systems; do not call them interchangeable.
- Do not invent missing values. Use “Not reported,” “Not accessible,” or “Unclear in source.”

### Specific caveat: CORP-025

Shi et al. (2024), iScience, nano-montmorillonite for tetracycline. The method says 0.03 g in 50 mL (0.6 g/L), while the conclusion says optimum 0.03 g/L. Reported capacities differ: 500 mg/g in Results discussion, 526 mg/g in abstract/conclusion, and fitted Langmuir qm = 558.184 mg/g. If C0 = 120 mg/L and 0.03 g/50 mL apply to the headline statement, the mass-balance ceiling is 200 mg/g. Keep these values out of comparative rankings until conditions are reconciled. The material is processed nano-clay, not untreated clay.

### Ranking caveats

The audit covers 34 journals, but some entries rely on secondary profiles displaying SJR metrics rather than direct canonical SCImago records. Environmental Research's exact current category quartile remains provisional; Arabian Journal of Chemistry has a historical 2024 Q1 record with reported Scopus discontinuation; Iraqi Journal of Agricultural Sciences is flagged discontinued with no current quartile assigned. Final Q1-only inclusion depends on the supervisor/journal's required ranking system and year/category.

## 7. Material taxonomy and outline

Preserve the user's working taxonomy:
- Natural clays: bentonite, kaolinite, sepiolite/stevensite and related minerals.
- Unmodified biopolymers: chitosan, cellulose, alginate.
- Modified biopolymers: crosslinked chitosan, chemically functionalized cellulose, etc.
- Biopolymer-based composites: clay–chitosan and polymer–carbon composites.
- Biochar and modified biochar, including chemically activated and doped/engineered biochars.
- Activated carbon (industrial benchmark and waste-derived AC).
- Nano-engineered carbons: CNTs, graphene/rGO and advanced composites.

Use explicit material categories and preparation routes. Do not use a single “Stage 2 modified” label as a substitute for the material category. The working outline puts mechanisms in a standalone Section 4; kinetics/isotherms are Section 3; techno-economic evaluation, implementation, challenges and conclusions follow in Sections 5–8. Confirm current outline before writing.

## 8. Work done recently in the previous chat

- Added missing logs for batches 13–20 and a project checkpoint.
- Updated the 24-day plan and research workflow.
- Screened CORP-025 from accessible PMC full text and recorded five audit evidence records (EV-AUD-001 to EV-AUD-005); flagged its dose/capacity inconsistency.
- Checked DISC-022 abstract/metadata but did not falsely claim to have read the full text; later marked it deferred at the user's instruction.
- Completed a first-pass journal-level audit across 34 journal titles, with unresolved source/category caveats preserved.
- Built provisional candidate-role and scope/ranking adjudication files.
- Built and audited the 208-row primary-study comparison matrix, keeping endpoint types distinct.
- Created comparison-readiness audit and five-panel comparative table draft.
- Created continuum synthesis and Section 2.1 raw-biomass draft.
- Current repository checkpoint says Section 2.2 clays/biopolymers draft also exists; use the repo's current contents as the truth, not old chat snapshots.
- User asked to continue the work and then raised the important question of how the final draft will contain citations. The next chat must address this citation workflow and continue actual repository work, not merely reassure the user.

## 9. Recommended next actions in the new chat

1. Read this handoff and re-fetch the current checkpoint, 24-day plan, working outline, Section 2.2 draft, citation rules, screening register, journal audit, and decision files from GitHub. Do not assume this handoff overrides newer commits.
2. Answer the user's citation question in practical terms: explain temporary candidate-ID links versus final Zotero author–date citations and show the audit trail.
3. Continue the next unfinished material-class section (likely Section 2.3 biochar/modified biochar) only after confirming status in the current repo.
4. Use a small evidence subset with source locations and caveats; no unsupported values and no broad ranking based on heterogeneous conditions.
5. Build and maintain the claim-to-source/citation-key mapping, then convert draft citations with Zotero/Better BibTeX after final source screening and target citation style are confirmed.
6. Keep DISC-022 deferred until the user uploads the PDF.
7. Every session should end with a concrete repository deliverable or a clearly documented blocker.

## 10. Suggested opening prompt for the new ChatGPT chat

I am migrating my Antibiotic Adsorption Review project from a conversation that reached its maximum length. The GitHub repository `zaidkhan005/reviewAdsorbants` is the source of truth. First read `logs/2026-10-27-migration-handoff.md`, then verify the current repository state and latest commits before doing any work. Continue from the existing evidence, screening, quartile audit, comparison matrix, synthesis and manuscript drafts; do not restart or assume I have more PDFs to upload. DISC-022 is explicitly deferred until I provide its full-text PDF. My most important concern is citation integrity: explain and implement the workflow that maps every manuscript claim to evidence IDs and source locations, then to Zotero/Better BibTeX citation keys, final author–date citations and a complete bibliography. Temporary candidate-ID DOI links are not final citations. After checking current status, continue the next genuinely unfinished task and commit a visible deliverable to GitHub. Preserve all source caveats and never invent evidence.
