# Screening and first-pass Q1 checkpoint — 2026-10-27

## CORP-025 — full-text screen closed

The open-access article was reviewed from PubMed Central (PMCID PMC10865401): https://pmc.ncbi.nlm.nih.gov/articles/PMC10865401/

- Primary experimental study: Shi et al. (2024), “Nano-clay montmorillonite removes tetracycline in water.”
- Five evidence records were added: EV-AUD-001–EV-AUD-005.
- The article reports 500 mg/g in the results discussion, 526 mg/g in the abstract/conclusion, and fitted Langmuir q_m=558.184 mg/g.
- High-priority caveat: methods say 0.03 g clay in 50 mL (0.6 g/L), but the conclusion says optimum dosage 0.03 g/L. If C0=120 mg/L and 0.03 g in 50 mL apply to the >90%/526 mg/g statement, the mass-balance ceiling is 200 mg/g. Concentration/dose labels need reconciliation; the capacity is not used as a verified comparative benchmark.
- Simulated aqueous tests; no demonstrated real wastewater, column, repeated regeneration, cost, or LCA in the accessible main article.

## DISC-022 — deferred until user provides full text

Public metadata and publisher preview were checked:
- Publisher preview: https://www.sciencedirect.com/science/article/pii/S0304389421029150
- PubMed record: https://pubmed.ncbi.nlm.nih.gov/34891019/

The abstract identifies a broad review of biochar, biopolymers, CNTs, clays, MOFs, microalgae, adsorption mechanisms, isotherms/kinetics, regeneration, cost and future directions. Complete text/tables were not accessible from the public pages inspected in this session. Per the user's instruction on 2026-10-27, this candidate is deferred until they provide the full-text PDF. Detailed tables have not been extracted as if read; it is neither screened nor excluded and is temporarily outside the active queue.

## Initial quartile entries (historical; superseded by the expanded 2025 SJR audit below)

| Candidate | Provider recorded | Ranking year | Category | Quartile | Verification source |
|---|---|---:|---|---|---|
| CORP-025 — iScience | SCImago SJR (profile-mirror evidence; canonical profile confirmation pending) | 2024 | Multidisciplinary | Q1 — first-pass | https://www.akaturk.com/journals/21100907125?lang=en |
| DISC-022 — Journal of Hazardous Materials | Scopus Journal Metrics / SJR (displayed by WUR Library) | 2024 | Environmental Engineering; Waste Management and Disposal; Pollution; Environmental Chemistry | Q1 | https://library.wur.nl/WebQuery/utbrowser/501 |

These were the initial first-pass entries only. The expanded journal-level audit below updates both entries to the latest available SJR year, records category-level differences where visible, and keeps full-text screening independent of journal quartile.

## Expanded journal-quartile audit — 2026-10-27

The screening register now carries ranking metadata for all 62 candidate rows, consolidated into 34 unique journal records in `data/journal-quartile-audit.csv`.

- Ranking year: 2025 SCImago/SJR profiles where available; Arabian Journal of Chemistry uses a historical 2024 SJR result because source-list mirrors report Scopus coverage discontinued after 2024.
- System distinctions are preserved: SJR Q1 does not imply JCR Q1. For example, RSC Advances, ACS Omega, Materials Advances and ACS ES&T Engineering are shown as SJR Q1 while their current JCR field result is Q2. Sources: https://akaturk.com/journals/21100199840?lang=en ; https://scienceaijournal.com/journals/acs-omega-2470-1343 ; https://www.akaturk.com/journals/21101041808?lang=en ; https://scijournal.org/acs-es-and-t-engineering.
- Two indexing exceptions: Arabian Journal of Chemistry is recorded as historical 2024 Q1 with a discontinuation caveat; Iraqi Journal of Agricultural Sciences is marked discontinued in a current source-list mirror and has no current quartile assigned.
- Three category-level caveats remain: Environmental Research (exact relevant environmental category should be reconfirmed), Journal of Engineering (category breakdown not exposed in the accessed profile), and Carbon Research (category breakdown not exposed in the accessed profile).
- Most results are secondary profile displays of SCImago/SJR data, not direct canonical SCImago page captures. The audit is therefore a structured first pass; consult the exact institutional ranking source before using a Q1-only rule as a final eligibility gate.
- Quartile year is the year of the ranking data, not necessarily the paper's publication year.

## Updated corpus state

- Candidate/screening rows: 62 (unchanged)
- Evidence records: 311 (305 batch-intake records + 5 CORP-025 audit records + 1 CORP-023 published-abstract audit record)
- Full-text checked: 61 / 62
- Full-text pending: 1 (DISC-022)
- Source caveats: 64 (62 prior + 2 new)
- Journal-quartile audit: all 34 unique journal titles have records in `data/journal-quartile-audit.csv`; 29 have profile-checked results with category detail, while five are explicitly flagged for discontinued/historical status or category-level follow-up
- No final include/exclude decision was made from abstract alone.

## Next actions

1. Resolve the five quartile-audit exceptions using the institution's required ranking source if a strict Q1-only decision is required.
2. Keep DISC-022 deferred until the user supplies the PDF; then screen its full text and tables.
3. Reconcile the nano-montmorillonite dose/capacity issue before any performance ranking.
4. Make retain/exclude/background-only decisions for active candidates, build comparative evidence tables, then draft the manuscript.
