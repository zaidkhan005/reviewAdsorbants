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
- `data/corpus-screening-register.csv` — unified screening register: 31 downloaded records plus 21 externally discovered candidate leads (52 total candidate records); all still require full-text/Q1 verification as appropriate
- `docs/LITERATURE_DISCOVERY_PLAN.md` — how we will find missing literature to complete the bibliography against the original outline
- [`manuscript/ORIGINAL_OUTLINE_AS_SUPPLIED.md`](manuscript/ORIGINAL_OUTLINE_AS_SUPPLIED.md) — normalized Markdown transcription of the supplied original PDF outline
- [`manuscript/REVIEW_OUTLINE.md`](manuscript/REVIEW_OUTLINE.md) — current working outline; includes a standalone Section 4 on mechanisms of antibiotic adsorption
- `logs/` — dated decisions, actions and unresolved questions

## Outline decision

The supplied outline is preserved separately so the original framework is not overwritten. In the working manuscript outline, adsorption kinetics/isotherms are in Section 3 and **mechanisms are promoted to standalone Section 4**; techno-economic evaluation, implementation, challenges, and conclusions are renumbered to Sections 5–8. The mechanism section includes an evidence-weighted matrix and explicit checks against conflating adsorption with catalytic degradation.

## Current status (2026-10-24)

- The original seven-paper matrix (`data/master-evidence-detailed.csv`) and caveats (`data/source-caveats.csv`) are preserved as historical seed records. Their values and mechanisms are **provisional until re-verified against the original full texts**. The formatted `.xlsx` workbook remains a separate working artifact.
- Initial bibliography audit: 31 records parsed; no exact duplicate DOI or normalized title was detected. Eight entries lack abstracts in the export. The Pinheiro chitosan/alginate record and Mohammed-Ridha publication year were corrected/flagged using publisher or PubMed records, and the original export should not be treated as complete evidence.
- Literature intake is restarting from one Zotero collection, `Antibiotic Adsorption Review — Full Corpus`, containing the original seven plus all other relevant downloads. No manual material-by-material reorganisation is required; classification happens during screening. The uploaded Better BibTeX export currently contains 31 downloaded records; it is a starting library, not the complete bibliography. Additional structured literature discovery is required.
- The outline's core class list is retained: raw lignocellulosic biomass, natural clays, unmodified biopolymers, standard biochar, chemically modified biochars, atomically doped biochars, activated carbon, and nano-engineered carbons.
- The boundary between the outline's Stage 2 and the current Zotero tag `STAGE-2-MODIFIED` remains unresolved; keep material category and processing route explicit in evidence records.
- Q1 status for several recent candidate papers has not been fully verified; candidates must not be treated as accepted until checked.

## Working loop

**Discover → screen → verify journal and source → retrieve full text → extract evidence → reconcile units/conditions → draft → cite through Zotero → audit claims.**

Every work session should end with a visible GitHub change or a clearly recorded blocker. The automation plan is $0-first: no n8n, paid automation service, or paid API is a prerequisite.
