# SEM-009 GO/CIP aqueous versus synthetic-urine publisher-preview audit — 31 October 2026

## Study identity
Bruckmann, F. da S., Fuhr, A. C. F. P., Zibetti, L., Bender, C. R., Silva, L. F. O., Martinello, K. da B., Ahmad, N., Mohandoss, S. and Dotto, G. L. (2024), “Adsorption of ciprofloxacin from aqueous solution and fresh synthetic urine by graphene oxide: Conventional and statistical physics modeling approaches,” *Chemical Engineering Journal* 487, article 150484. DOI: 10.1016/j.cej.2024.150484. Published 1 May 2024.

Official publisher page: https://www.sciencedirect.com/science/article/pii/S1385894724019715
ResearchGate record: https://www.researchgate.net/publication/379028644_Adsorption_of_ciprofloxacin_from_aqueous_solution_and_fresh_synthetic_urine_by_graphene_oxide_Conventional_and_statistical_physics_modeling_approaches

## Source access and limitation
The official ScienceDirect abstract, highlights, Introduction and section snippets were reviewed on 31 October 2026. The publisher page exposes an “Access through your organization” link, an “Open Manuscript” link and purchase access. The exact Open Manuscript link returned a page-not-found response in this session. The ResearchGate record explicitly says no full text is available and offers a request-full-text option. The current Library search did not locate a matching PDF. No new PDF upload is assumed or requested.

This is therefore a primary-publisher **preview-level** audit, not a full-table/source audit. The article's numeric endpoints can be quoted as author-reported abstract/conclusion values but cannot be assigned to a directly observed qe, conventional Langmuir qmax or a specific statistical-physics model parameter without the tables.

## What the publisher preview establishes
The work studies ciprofloxacin (CIP) adsorption by graphene oxide (GO) from two distinct media:
1. Aqueous solution.
2. Fresh synthetic urine, a simulated matrix prepared using urine-related chemical constituents.

The publisher abstract states that batch adsorption experiments varied initial concentration, adsorbent dosage, pH and temperature. It also states that five statistical-physics models covering monolayer, double-layer and multilayer assumptions were tested for equilibrium; kinetic data were adjusted using pseudo-first-order, pseudo-second-order and general-order models.

The two capacities are explicitly matrix-specific:
- Aqueous medium: maximum adsorption capacity 354.24 mg/g at pH 5.0.
- Fresh synthetic urine: maximum adsorption capacity 291.39 mg/g at pH 6.0.

The abstract/highlights say that a double layer with one energy model describes the equilibrium data well. The conclusion snippet states that general-order kinetics describe the adsorption kinetics well. The urine section snippet states that at pH 6.0 the antibiotic is zwitterionic.

Do not merge these two capacity numbers or treat the difference as a pure adsorbent-performance loss attributable only to urine chemistry; the pH and matrix are different (5 versus6), and the missing table/Methods details prevent a matched-condition comparison.

## Capacity metric classification — unresolved
The accessible abstract/conclusion calls the numbers “adsorption capacity” and “maximum adsorption capacity”. It does **not** specify whether:
- 354.24 and291.39mg/g are directly observed equilibrium uptake values qe;
- they are conventional Langmuir/Freundlich/Temkin model qmax values;
- they are saturation capacities (qsat/Qmax) from the double-layer one-energy statistical-physics model; or
- they are another fitted/model-derived statistic.

Because conventional and statistical-physics models are both used, do not assume that the two numbers are interchangeable with an experimentally observed qe or conventional Langmuir qmax. Do not insert them in the numeric comparison table as qmax/qe until full-text tables are available.

## Synthetic urine and reagent context
The publisher “Chemicals” snippet lists the following reagents: NaCl, HCl, NaOH, Na2SO4, KCl, MgCl2·6H2O, NaH2PO4, CaCl2·2H2O, KMnO4, H2SO4, H2O2, sodium citrate dihydrate, urea and graphite. This indicates a salt/urea-based synthetic medium and GO synthesis chemicals, but the exact recipe, salt concentrations, preparation sequence and final ionic composition are not exposed in the preview.

The article's synthetic-urine section snippet says the test represents simulated CIP excretion in the unmetabolized form by kidneys; it is not a collected urine sample from a patient. The article also references urine-related modelling using fraction excreted unmetabolized, defined daily dose and average daily urine volume. The numerical assumptions and calculation are not exposed in the current preview.

Do not call this a real urine, clinical sample, hospital wastewater, municipal wastewater or field-water experiment.

## Equilibrium and kinetic modelling
Accessible claims:
- Five statistical-physics equilibrium models are considered, involving mono-, double- and multilayer adsorption.
- Steric/energetic parameters considered include number of adsorbed molecules per site, receptor site density and half-saturation.
- Highlights: double-layer with one energy provides a good equilibrium description.
- Conventional kinetic fits: pseudo-first-order, pseudo-second-order and general-order.
- Conclusion snippet: general-order model best describes the kinetic data, with the adsorbent surface treated as the rate-determining step.

Not exposed:
- Which exact fitted model produced the aqueous 354.24mg/g and synthetic-urine 291.39mg/g values.
- Conventional Langmuir/Freundlich/Temkin fit coefficients, qmax and goodness-of-fit metrics.
- Statistical-physics qsat/Qmax, number of molecules per site, receptor density, half-saturation, energy values and fit statistics by matrix.
- Kinetic qe, k1/k2/general-order parameters, R²/RMSE and direct experimental qe.
- Concentration ranges, batch volume, GO dose, exact temperature, contact time and residual concentrations for each matrix.

No feed-mass ceiling can be calculated without the exact C0, volume and GO mass. Do not reverse-engineer missing operating conditions from the reported capacity.

## Preparation, mechanism and practical boundary
The publisher snippet states that GO is prepared by oxidation and chemical exfoliation of graphite flakes using KMnO4; listed reagents also include concentrated H2SO4 and H2O2. A complete GO recipe, GO yield, wash-water volume, process energy or material cost is not exposed.

Characterization methods include FTIR, XRD, SEM, TGA, BET and EDS. The abstract states that adsorption-mechanism hypotheses are proposed based on experimental data and statistical-physics modelling, but the exact CIP-GO interaction mechanisms and quantitative contributions are not in the preview.

No confirmed desorption/regeneration protocol, cycle-resolved reuse data, GO leaching, actual urine testing, real wastewater trial, cost per mass/volume treated, yield, energy inventory, LCA or TEA was found in accessible source snippets. Absence in the preview is not proof that a full paper table does not contain further details; it remains an access limitation.

## Semester-paper decision
Retain SEM-009 as important **abstract-level matrix-context evidence** for GO/CIP adsorption in aqueous solution and fresh synthetic urine. Report:
1. 354.24mg/g in aqueous medium atpH5;
2. 291.39mg/g in fresh synthetic urine atpH6;
3. both as author-reported “maximum adsorption capacity” values with metric/model provenance unresolved;
4. synthetic urine as a simulated matrix rather than real human urine or wastewater;
5. double-layer one-energy statistical-physics equilibrium model highlighted as a good fit and general-order kinetics reported in the conclusion.

Do not:
- label the values as observed qe or conventional Langmuir qmax;
- compare them directly with condition-matched capacities without exact C0/dose/volume/time/temp;
- treat the synthetic urine result as a real sample or field validation;
- assign regeneration, reuse or cost claims absent from accessible evidence;
- add a numeric condition-labelled comparison row until the full article tables are inspected.

## Citation workflow
No matched Better BibTeX key was identified in the current 173-entry citation export. Do not invent a key. Add the DOI to Zotero only if selected for citation; then verify the actual key before inserting manuscript citations.

## Repository updates
Updated in place:
- data/semester-remaining-work-register.csv
- data/semester-paper-candidate-register.csv
- data/semester-evidence-readiness-audit.csv (EV-SEM-009)
- README.md

No row was added to the condition-labelled comparison because metric provenance and matched operating conditions remain unavailable. No duplicate evidence ID was created.
