# SEM-003 GO/fluoroquinolone full-text source audit — 31 October 2026

## Study identity and source provenance
Yadav, S., Goel, N., Kumar, V., Tikoo, K. and Singhal, S. (2018), “Removal of fluoroquinolone from aqueous solution using graphene oxide: experimental and computational elucidation,” *Environmental Science and Pollution Research* 25(3), 2942–2957. DOI: 10.1007/s11356-017-0596-8. Epub 16 November 2017. PMID 29147984.

Primary article:
- PubMed metadata and abstract: https://pubmed.ncbi.nlm.nih.gov/29147984/
- Author-uploaded full-text copy (ResearchGate): https://www.researchgate.net/publication/320944938_Removal_of_fluoroquinolone_from_aqueous_solution_using_graphene_oxide_experimental_and_computational_elucidation
- Publisher DOI: https://doi.org/10.1007/s11356-017-0596-8

Correction/erratum:
- “Correction to: Removal of fluoroquinolone from aqueous solution using graphene oxide: experimental and computational elucidation,” DOI 10.1007/s11356-018-1381-z, published June 2018, *Environmental Science and Pollution Research* 25(16), 16261–16265.
- PubMed correction record: https://pubmed.ncbi.nlm.nih.gov/29460240/
- Author-uploaded correction: https://www.researchgate.net/publication/323264406_Correction_to_Removal_of_fluoroquinolone_from_aqueous_solution_using_graphene_oxide_experimental_and_computational_elucidation

The author-uploaded full text was inspected on 31 October 2026. The formal correction explicitly states that Figures 10, 11, 12 and 13 in the original article must be replaced by the corrected figures supplied in the erratum. These are the Langmuir isotherm, Freundlich isotherm, pseudo-first-order kinetic and pseudo-second-order kinetic plots. Cite/use only the corrected versions of these four figures. The notice does not list any replacement of Tables 2 or 4; those numeric tabular outputs are transcribed from the article, but plot-based interpretation must remain tied to the corrected figures.

## Target/material scope and target separation
The study synthesizes graphene oxide (GO) via modified Hummers–Offeman oxidation and evaluates three fluoroquinolones:
- Ciprofloxacin (CIP)
- Norfloxacin (NOR)
- Ofloxacin (OFL)

These are separate target-drug experiments, not one mixed-antibiotic co-adsorption test. CIP is the target relevant to the semester paper; NOR and OFL provide separate chemical comparators only. Do not pool their capacities or treat a single “FQ” value as CIP-specific.

## GO synthesis and preparation burden
- Graphite powder: 3 g (commercial material purchased from Otto Chemicals).
- Add to 300 mL of cooled 98% H2SO4 at 0 °C.
- Slowly add 20 g KMnO4 and 3 g NaNO3, maintaining the mixture below 10 °C using an ice bath.
- Stir in a water bath at 35 °C for 30 min.
- Add 200 mL DI water, heat to 98 °C with effervescence, maintain 30 min.
- Terminate with 500 mL DI water and 40 mL of 30% H2O2.
- Wash repeatedly with distilled water until pH 7; filter and vacuum-dry at 50 °C for 24 h.

The paper does not report GO yield, acid/oxidant recovery, washing-water volume, waste neutralization burden, electricity consumed, or a monetized material cost. This is a strong-acid/oxidant-intensive modified Hummers route using commercial graphite, not a waste-derived graphite process. Do not describe it as a demonstrated low-cost route.

## General adsorption method
- 100 mL of antibiotic solution is placed in a 250 mL beaker.
- A defined GO mass is dispersed using an ultrasonicator.
- The dispersion is stirred continuously at 500 rpm until equilibrium.
- All adsorption experiments are conducted at room temperature; a precise °C value is not stated.
- At periodic time points, 4 mL of dispersion is withdrawn and filtered through a 0.45 µm nylon syringe filter.
- Residual antibiotic is estimated by UV–Vis spectroscopy.
- Removal and uptake are calculated using the standard equations: R% = (C0−Ct or Ce)/C0 ×100 and qt/qe = (C0−Ct or Ce)V/m.

Because the text states that 4 mL aliquots are withdrawn periodically from the GO dispersion, but does not explain whether sorbent mass and liquid-volume corrections are applied to later time points, avoid reverse-engineering exact observed qt values from the plotted kinetic curves.

## Condition-specific operating conditions
- pH test: pH 2–12 adjusted with 1 M HCl and 1 M NaOH. CIP and NOR have maximum adsorption near pH 7; OFL maximum is near pH 4.
- Dose-response test: GO dosage 50–150 mg per 100 mL, at each drug's selected pH and initial drug concentration 5 mg/L. Removal increases as GO dose is increased.
- Initial-concentration test: 5–15 mg/L. The paper reports decreasing removal percentage with increasing initial antibiotic concentration.
- Contact-time test: all three antibiotics reach a plateau by approximately 50 min according to the text.
- Isotherm test: 100 mL antibiotic solution at 5–15 mg/L with 0.05 g GO; pH 7 for CIP and NOR, pH 4 for OFL; contact time up to 50 min; room temperature.
- Kinetic model test: 5 mg/L CIP or NOR solution, 100 mL, 0.05 g GO, at neutral pH for CIP/NOR; 5 mg/L OFL at pH 4. Kinetic samples were obtained up to 230 min for model fitting.

## CIP-specific fitted isotherm result
Table 2 reports the following CIP parameters:
- Langmuir qmax = 18.65 mg/g
- Langmuir KL = 1.956 L/mg
- Langmuir R² = 0.999
- Freundlich KF = 0.015
- Freundlich 1/n = 0.25
- Freundlich R² = 0.974

The authors state that Langmuir fits better than Freundlich and interpret the adsorption as monolayer. The Langmuir value is a fitted qmax, not an observed experimental qe. The CIP isotherm series uses C0=5–15 mg/L, 100 mL solution and 0.05 g GO at pH 7. At the highest feed concentration of 15 mg/L, the available-feed ceiling is:
- 15 mg/L ×0.100 L /0.050 g = 30 mg/g.

The fitted qmax of 18.65 mg/g does not exceed that simple upper feed ceiling. It remains a model asymptote, not a directly measured uptake at a single operating point.

## CIP-specific kinetic fit and mass balance
Table 4 reports:
- Pseudo-first-order fitted qe = 1.22 mg/g; k1 = 0.026 min−1; R² = 0.428.
- Pseudo-second-order fitted qe = 9.25 mg/g; k2 = 0.056 g mg−1 min−1; R² = 0.999.

The kinetic model data were collected using 5 mg/L CIP, 100 mL solution, 0.05 g GO and neutral pH. The available CIP mass is 5 mg/L ×0.100 L = 0.5 mg; divided by 0.05 g GO, the feed-limited qe ceiling is 10 mg/g. The PSO-fitted qe = 9.25 mg/g is below the feed ceiling and is physically plausible. However, Table 4 presents calculated/model-fitted qe, not a separate directly tabulated observed qe. The article text says the PSO qe values are close to experimental values, but the numerical experimental value itself is not listed in that table; do not relabel 9.25 mg/g as observed qe.

For both CIP and NOR, PSO R² is 0.999, while PFO fit quality is much poorer. OFL PSO fitted qe = 8.34 mg/g (R²=.999), PFO qe=1.58mg/g (R²=.532). Keep every drug's values separated.

## pH/speciation and mechanism
The authors report:
- CIP pKa1 = 6.1 and pKa2 = 8.7.
- NOR pKa1 = 6.22 and pKa2 = 8.51.
- OFL pKa1 = 6.1 and pKa2 = 8.28.

CIP and NOR adsorption peaks near pH 7, where zwitterionic species dominate and the protonated amine group remains available to interact with GO. Lower pH gives cationic forms and weaker uptake; above pH 7, deprotonation and increasingly negative GO/antibiotic groups can cause repulsion. OFL peaks at pH 4, attributed by the authors to different charge/surface behavior and OH− competition at higher pH.

The article discusses GO oxygen functionalities (hydroxyl, epoxy and carboxyl), electrostatic effects, hydrogen bonding and π interactions. DFT uses a simplified GO model and calculates a generic fluoroquinolone–GO interaction energy of −20.15 kcal/mol in gas phase and −28.63 kcal/mol in aqueous phase. It describes favorable hydrogen-bond geometries (approximately 1.69, 1.99 and 3.00 Å), while a parallel π-stacked orientation is not the most stable configuration. These are computationally supported mechanistic hypotheses; do not report a CIP-specific DFT adsorption energy because Table 5 labels the system generically as GO/FQ.

## Cost, real-water and reuse evidence boundary
- No real wastewater, river-water or natural-matrix experiment is reported.
- No regeneration/desorption or repeated adsorption–desorption cycle test is identified in the article.
- No metal leaching is relevant to this plain GO system, but no other GO particulate-release or regeneration stability test is given.
- No GO synthesis yield, normalized material cost, process energy, cost per volume treated, acid/oxidant recovery or full LCA/TEA is presented.

Do not claim reusability, field suitability or low-cost performance for this source.

## Semester-paper decision
Retain SEM-003 as a CIP-specific GO model comparator, with NOR and OFL explicitly separate. The defensible quantitative entries are:
1. CIP Langmuir fitted qmax = 18.65 mg/g (KL=1.956 L/mg, R²=.999) under the separate isotherm range 5–15 mg/L, 100 mL, 0.05 g GO, pH 7, room temperature.
2. CIP PSO fitted qe = 9.25 mg/g (R²=.999) under 5 mg/L, 100 mL, 0.05 g GO, pH 7; kinetic feed ceiling 10 mg/g.
3. CIP PFO fitted qe = 1.22 mg/g (R²=.428), kept separate from the PSO fit.
4. No direct numeric observed qe/removal endpoint is tabled in the source text reviewed.
5. The erratum replaces Figures 10–13; use corrected plots only.
6. No regeneration, actual wastewater or monetized cost evidence.

Do not pool CIP/NOR/OFL or label fitted qmax/PSO qe as observed uptake. The existing Zotero export search did not identify a matched Better BibTeX key; do not invent one. Keep citation insertion pending until the actual key is verified.

## Repository updates
Updated in place:
- data/semester-remaining-work-register.csv
- data/semester-paper-candidate-register.csv
- data/semester-evidence-readiness-audit.csv (EV-SEM-018)
- data/semester-condition-labelled-comparison.csv (new CIP-only model row)
- data/semester-manuscript-claim-evidence-audit.csv (CLM-20)
- README.md

No duplicate SEM evidence ID was created. The manuscript's cited-reference comparison table was not given an invalid placeholder citation; insert this source only after the verified Zotero key is available.
