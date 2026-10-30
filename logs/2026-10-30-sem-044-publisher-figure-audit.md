# SEM-044 publisher abstract and figure-preview audit — 2026-10-30

## Candidate

**SEM-044:** Nazraz, M., Yamini, Y. & Asiabi, H. (2019). “Chitosan-based sorbent for efficient removal and extraction of ciprofloxacin and norfloxacin from aqueous solutions.” *Microchimica Acta* 186(7), article 459. DOI: [10.1007/s00604-019-3563-x](https://doi.org/10.1007/s00604-019-3563-x). PMID: 31222415.

**Semester-paper scope:** retain provisionally as a selected GO-bearing ternary composite for CIP. NOR is a separate co-target and must not be pooled with CIP.

## Primary publisher access checked

- Official Springer Nature article page: https://link.springer.com/article/10.1007/s00604-019-3563-x
- Official PubMed record: https://pubmed.ncbi.nlm.nih.gov/31222415/
- The Springer page states that this is an Original Paper published 20 June 2019, *Microchimica Acta* volume 186, article 459.
- The abstract and article metadata are accessible. The page explicitly identifies the main article as subscription content and offers institutional login or purchase. Full Methods, tables and figure captions were not available.
- Publisher-hosted preview images for Figures 1–5 are nevertheless accessible through the page. Figure 1 is morphology imagery; Figure 2 is a component-performance comparison; Figure 3 plots capacity vs pH and zeta potential vs pH; Figure 4 shows kinetic fits; Figure 5 shows Langmuir/Freundlich isotherm fits. Figures 2–5 were inspected visually.
- The preview images do not expose their full captions or operating conditions. Do not fill missing C0, dosage, volume, temperature or contact-time details from secondary reviews.

## Abstract-level primary evidence

The Springer abstract confirms:

- MgO/chitosan/graphene oxide (MgO/Chit/GO) nanosheets were hydrothermally synthesized.
- Residual antibiotics were measured using HPLC/UV.
- Characterization included FTIR, XRD, BET, SEM and TEM.
- BET surface area: **294 m²/g**.
- Typical mesopore size: **15 Å**.
- Langmuir-reported maximum adsorption capacity: **1111 mg/g for CIP** and **1000 mg/g for norfloxacin**. These are separate analyte values.
- Pseudo-second-order kinetic behaviour is reported.
- Equilibrium was reported as **over 120 min for CIP** and **over 150 min for norfloxacin**. These are lower-bound statements, not exact equilibrium times.
- Authors describe the material as economical and eco-friendly; no comparable cost inventory is exposed in the abstract.

## Publisher figure-preview observations

### Figure 2 — component comparison

The plotted bars show the ternary MgO/Chit/GO material outperforming GO alone and MgO/chitosan for both CIP and norfloxacin. The exact caption and test conditions are unavailable in the preview. Treat the result qualitatively only; do not transcribe precise removal percentages from the small graph.

### Figure 3 — pH and surface charge

- Figure 3a shows the plotted adsorption capacity for both antibiotics peaking around **pH 7**. This is a visual interpretation of the publisher figure; the caption and conditions are unavailable. Do not use the graph as a condition-labelled numeric qe endpoint.
- Figure 3b shows zeta potential crossing approximately zero near **pH 5.5**. This is a visual estimate from the plotted curve, not a separately stated table value or a fully source-captioned pHpzc value.

### Figure 4 — kinetic fits

The publisher preview shows kinetic-model regression plots, including pseudo-first-order and pseudo-second-order panels. The abstract independently states pseudo-second-order kinetics. The figure preview does not expose caption context, analyte-to-panel assignment, complete parameter table or experimental conditions.

### Figure 5 — isotherm fits

- The preview shows Langmuir and Freundlich linearized fit plots.
- The two Langmuir regression equations visible in the image have slopes approximately **0.0009** and **0.0010**, with R² values approximately **0.9987** and **0.9979**.
- The reciprocals of those slopes are approximately 1111 and 1000 mg/g, consistent with the abstract's two reported Langmuir maximum capacities.
- Because the publisher preview does not expose the Figure 5 caption, do not assign each individual panel to CIP or norfloxacin solely from the image. The abstract already provides the separate analyte assignment.
- These regression plots visually corroborate the model fit, but they do not establish observed qe or the full experimental concentration/dose conditions.

## Quantitative-use decision

**Keep 1111 mg/g for CIP as an abstract-reported, Langmuir-fitted qmax only.** The figure preview strengthens confidence that it is a Langmuir fit rather than a typo in the abstract. It does not clear the quantitative-ranking hold.

The full primary Methods/tables are still needed to verify:
- initial CIP concentration and isotherm concentration range;
- adsorbent dose, solution volume and finite-feed mass balance;
- pH and temperature for the reported qmax;
- model fitting procedure and fit-statistics table;
- directly observed qe values versus fitted qmax;
- exact extraction/analytical protocol and any sample matrix;
- regeneration, desorption and reuse, if any.

No feed mass or adsorbent mass is exposed in the accessible primary page. Therefore a finite-feed ceiling cannot currently be calculated. The high qmax must not be ranked against other studies or presented as directly observed uptake.

## Mechanism, cost and reuse guardrails

The abstract attributes performance to high surface area relative to bare MgO/chitosan or GO, but it does not provide a detailed mechanism. The pH and zeta-potential graphs are suggestive, but without full captions and explanatory text do not claim quantified electrostatic, π–π, hydrogen-bonding or coordination contributions.

“Economical” and “eco-friendly” are author characterizations. There is no accessible normalized production cost, reagent/energy inventory, yield, solvent recovery, regeneration cost or cost-per-mass-CIP-removed denominator. No reuse-cycle evidence is present in the accessible abstract/figures. Do not promote this as demonstrated low-cost or regenerable.

## Repository actions

- Updated `data/semester-paper-candidate-register.csv` to record primary publisher figure review and its limits.
- Updated existing evidence row **EV-SEM-023** in `evidence/semester-paper/SEMESTER_CORE_EVIDENCE_EXTRACTION.csv`.
- Updated `data/semester-study-inclusion-shortlist.csv`.
- Updated `data/semester-evidence-readiness-audit.csv`.
- Added SEM-044 to `data/semester-condition-labelled-comparison.csv` as a provisional, model-only row with missing condition fields explicit.
- Reused existing candidate SEM-044 and evidence ID EV-SEM-023. No duplicate candidate/evidence record created.

## Final disposition

**Retain provisionally for material-design and Langmuir-fit discussion; exclude from capacity rankings pending full primary Methods/tables.** Publisher figure previews add useful verification, but no full-text source was obtained in this audit.
