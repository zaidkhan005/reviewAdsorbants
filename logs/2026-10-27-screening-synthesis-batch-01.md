# Screening and synthesis setup — Batch 01 (2026-10-27)

## Deliverables created

### 1. Candidate-level decision audit

File: data/candidate-decision-audit.csv

All 62 candidate records now have a provisional working role and a quantitative-use guardrail. This is a triage layer over the canonical screening register, not a claim that final manuscript inclusion/exclusion has been completed.

| Working role | Count |
|---|---:|
| Primary adsorption evidence candidate | 24 |
| Primary candidate — hold disputed values from quantitative rankings | 16 |
| Primary candidate — adsorption-only outcomes required | 3 |
| Background / citation mining only (reviews/secondary sources) | 16 |
| Adjacent technology only (membrane/rejection rather than core adsorption capacity) | 1 |
| Deferred pending user-provided full text (DISC-022) | 1 |
| Exclude — out of scope (CORP-062) | 1 |
| **Total candidate rows** | **62** |

Important status distinctions:
- These roles are provisional working recommendations. Full-text screening, current journal-ranking profile and final paper inclusion are separate dimensions.
- “Primary candidate” does not mean every value is safe to rank: 16 primary candidates have recorded data-quality conflicts that hold disputed values out of numerical ranking; three require adsorption-only outcomes to be separated from oxidation, catalytic transformation or another process.
- The 16 review/secondary sources remain useful for background and citation mining but must not be presented as independent primary experiments.
- CORP-030 (membrane rejection/self-cleaning) is kept outside the core adsorption-capacity matrix; it may be mentioned separately as an adjacent technology.
- CORP-062 remains the explicit out-of-scope exclusion.

### 2. Primary-study comparison matrix, version 1

File: data/primary-study-comparison-matrix.csv

- **208 target/material/stage rows**, drawn from source-linked evidence records for **43 primary-study candidates**.
- Each row retains the candidate ID, source citation, journal-ranking signal, target/co-contaminant, adsorbent, material stage, and linked evidence IDs and source locations.
- Separate columns organize preparation, observed uptake/removal, model-fitted capacity/isotherms, kinetics, water chemistry/matrix, regeneration/desorption, column/fixed-bed performance, cost/energy/LCA and mechanism evidence.
- Rows are target/material evidence groupings, not 208 distinct papers.
- The matrix concatenates source-reported evidence with evidence IDs. It has not yet been normalized into a final paper-ready numerical ranking; conflicting units, target mixtures, observed uptake, fitted qmax and percentage removal must remain distinct.
- Co-contaminant-only evidence (for example, metals) is retained where it appears in a study, but it must not be counted as an antibiotic-specific adsorption outcome.

## Quartile audit context

- data/journal-quartile-audit.csv records 34 unique journal titles and is mirrored into data/corpus-screening-register.csv.
- Latest available 2025 SJR profiles were used where located; ranking year does not necessarily equal the paper's publication year.
- SJR and Clarivate/JCR are separate ranking systems and can disagree.
- Five exceptions remain explicit: historical/discontinued status for Arabian Journal of Chemistry; discontinued/no-current-quartile status for Iraqi Journal of Agricultural Sciences; and category-level confirmation for Environmental Research, Journal of Engineering and Carbon Research.
- Most source records are secondary profile displays of SJR data. If journal quartile is a hard inclusion criterion, verify against the institution's required ranking source before making final eligibility decisions.

## Current corpus integrity

- Candidate/screening rows: 62; 34 unique journals.
- Full-text status: 61/62 completed; DISC-022 is explicitly deferred until the user supplies the full-text PDF. It is neither screened nor excluded.
- Source-linked evidence records: 310, with no duplicate evidence IDs.
- Source caveats: 64.
- CORP-025 remains a primary candidate, but its reported 500/526 mg/g statements and fitted Langmuir q_m=558.184 mg/g must not be used as verified comparative capacities until the dose/concentration mass-balance conflict is reconciled.

## Next actions

1. Resolve ranking exceptions against the institution's preferred source if a strict Q1 rule is required.
2. Adjudicate final roles for active primary candidates; keep review papers as background/citation-mining sources and preserve adjacent-process boundaries.
3. Audit the comparison matrix for unit/condition consistency and identify a small number of defensible same-target/same-metric comparisons across the processing continuum.
4. Begin substantive section drafting only after the evidence subset for that section is screened and its limitations are explicit.
5. Keep DISC-022 deferred until the user supplies the full-text PDF.