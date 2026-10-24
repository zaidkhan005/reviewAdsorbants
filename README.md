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
- `docs/AUTOMATION_ROADMAP.md` — $0-first workflow; no n8n or paid automation dependency
- `docs/24_DAY_PLAN.md` — original sprint plan and progress status
- `data/master-evidence.csv` — condensed index of the initial core papers
- `data/master-evidence-detailed.csv` — the full 15-column evidence matrix for the seven core papers
- `data/source-caveats.csv` — source-specific inconsistencies and next verification actions
- `data/paper-screening-register.csv` — candidate screening and verification status
- [`manuscript/ORIGINAL_OUTLINE_AS_SUPPLIED.md`](manuscript/ORIGINAL_OUTLINE_AS_SUPPLIED.md) — normalized Markdown transcription of the supplied original PDF outline
- [`manuscript/REVIEW_OUTLINE.md`](manuscript/REVIEW_OUTLINE.md) — current working outline; includes a standalone Section 4 on mechanisms of antibiotic adsorption
- `logs/` — dated decisions, actions and unresolved questions

## Outline decision

The supplied outline is preserved separately so the original framework is not overwritten. In the working manuscript outline, adsorption kinetics/isotherms are in Section 3 and **mechanisms are promoted to standalone Section 4**; techno-economic evaluation, implementation, challenges, and conclusions are renumbered to Sections 5–8. The mechanism section includes an evidence-weighted matrix and explicit checks against conflating adsorption with catalytic degradation.

## Current status (2026-10-24)

- The initial seven-paper evidence matrix is preserved here in `data/master-evidence-detailed.csv` (15 fields × 7 core papers), with source-specific verification tasks in `data/source-caveats.csv`. The formatted `.xlsx` workbook remains a separate working artifact.
- The outline's core class list is retained: raw lignocellulosic biomass, natural clays, unmodified biopolymers, standard biochar, chemically modified biochars, atomically doped biochars, activated carbon, and nano-engineered carbons.
- The boundary between the outline's Stage 2 and the current Zotero tag `STAGE-2-MODIFIED` remains unresolved; keep material category and processing route explicit in evidence records.
- Q1 status for several recent candidate papers has not been fully verified; candidates must not be treated as accepted until checked.

## Working loop

**Discover → screen → verify journal and source → retrieve full text → extract evidence → reconcile units/conditions → draft → cite through Zotero → audit claims.**

Every work session should end with a visible GitHub change or a clearly recorded blocker. The automation plan is $0-first: no n8n, paid automation service, or paid API is a prerequisite.
