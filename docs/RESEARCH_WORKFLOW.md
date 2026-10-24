# Research and evidence workflow

## 1. Discover

Use Consensus, publisher platforms, DOI/Crossref lookups, and other scholarly search tools to identify candidate papers. Reviews help map a field; original papers supply experimental values.

## 2. Screen

For each candidate, record:
- material category and exact adsorbent;
- target antibiotic(s);
- study type and whether removal is adsorption only;
- publication year, journal, DOI;
- journal-quartile provider, year and category;
- relevance to processing–cost–performance;
- keep/exclude/pending decision and reason.

## 3. Verify Q1 status

A paper is not Q1-verified until the register records the ranking source (for example, Clarivate JCR or SCImago/SJR), ranking year, subject category, quartile, and verification source URL. Do not mix ranking systems silently. “High impact factor” is not itself a quartile check.

## 4. Retrieve and verify full text

Keep full-text PDFs in Zotero or another appropriate licensed repository. Verify bibliographic metadata against the publisher/DOI record. Use the original article’s methods, tables, figures and supplements to check numerical claims.

## 5. Extract evidence

For each exact adsorbent–antibiotic pairing, record:
- preparation/feedstock, modification steps and relevant preparation parameters;
- pH and antibiotic speciation;
- initial concentration, adsorbent dose, contact time, temperature, mixing and matrix;
- observed uptake/removal and model-fitted qmax separately;
- kinetic and isotherm models with fit metrics;
- mechanism: measured evidence versus author-proposed explanation;
- desorption, regeneration cycles, real water, fixed-bed/column data;
- costs, chemical/energy inputs, life-cycle data and scale-up evidence;
- limitations and any internal inconsistencies.

## 6. Draft and cite

Draft only after evidence for the paragraph is extracted. Add citations using Zotero, then check that every numerical or mechanistic claim traces to a primary source. Keep claim wording proportional to the evidence.

## 7. GitHub storage convention

- Every session ends with a dated entry in `logs/`.
- Update `data/paper-screening-register.csv` when a candidate changes status.
- Update `data/master-evidence.csv` when paper evidence has been checked against the original.
- Record major scope/taxonomy decisions in `docs/MATERIAL_TAXONOMY.md` and the dated log.
- Save manuscript drafts under `manuscript/`.
- Prefer small, descriptive commits. Do not commit private credentials or copyrighted PDFs.

## Paper status vocabulary

`DISCOVERED` → `SCREENING` → `Q1-PENDING` / `FULLTEXT-PENDING` → `EVIDENCE-VERIFIED` → `ACCEPTED` / `EXCLUDED`.

The Q1 decision and full-text evidence decision are independent. A relevant paper can be useful for background and still fail the Q1-only inclusion rule.