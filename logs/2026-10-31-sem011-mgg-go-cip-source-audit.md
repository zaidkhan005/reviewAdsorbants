# SEM-011 mGG/GO–CIP source and mass-balance audit — 31 October 2026

## Study identity and provenance
Saya, Laishram; Singh, W. Rameshwor; Hooda, Sunita (2023), “Adsorptive removal of ciprofloxacin from aqueous medium by magnetic guar gum grafted graphene oxide nano composite,” *Journal of Environmental Chemical Engineering* 11(5), article 110766. DOI: 10.1016/j.jece.2023.110766.

Author preprint:
- SSRN title: “Wastewater Remediation Through Adsorptive Removal of Ciprofloxacin by Magnetic Guar Gum Grafted Graphene Oxide Nano Composite”
- SSRN ID 4444399; posted 20 May 2023; the SSRN page states that the final peer-reviewed article has been published and links to the ScienceDirect version.
- SSRN page: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4444399
- SSRN PDF delivery was not accessible in this session (HTTP 404 / rate-limit response).

Official publisher:
- https://www.sciencedirect.com/science/article/pii/S2213343723015051
- Official abstract and highlights state the maximum capacity of 555.56 mg/g, and identify Langmuir equilibrium and pseudo-second-order kinetic models as best fits.
- Full publisher article is behind institutional/purchase access; the official ScienceDirect preview exposes title, abstract, highlights, introduction and selected section snippets.

Third-party full-text mirror:
- Scribd: https://www.scribd.com/document/1043011820/1-s2-0-S2213343723015051-main
- 14-page text mirror uploaded by a third party (not the publisher or authors, based on the page's visible attribution). Its extracted text includes the complete main article body and Tables 1–2 / Figures 1–13. This provides useful detail but remains third-party source evidence. The published full text and SSRN PDF were not independently downloaded, so all detailed values below should retain a provisional mirror flag.

The article identity, official abstract, author preprint abstract, third-party mirror and its uploader/source provenance were checked on 31 October 2026. No Better BibTeX key was found in the inspected Zotero export; do not invent one.

## Headline endpoint and model distinction
The official publisher highlights and abstract report a maximum ciprofloxacin adsorption capacity of 555.56 mg/g. The abstract also says the adsorption behavior is best described by a Langmuir isotherm and pseudo-second-order kinetics.

The third-party mirror's Table 2 identifies 555.56 mg/g as Langmuir-fitted q_max:
- Langmuir q_max = 555.56 mg/g
- Langmuir K_L = 0.0173 L/mg
- Table 2 R² = 0.9915
- The prose in §4.3 says the Langmuir R² is 0.9989.

This discrepancy is retained. The source does not clarify whether the table and prose R² correspond to different linear/nonlinear fitting forms; do not choose one or silently correct the other. The 555.56 mg/g value is a fitted Langmuir asymptote, not a directly measured q_e at a named condition.

Other third-party Table 2 parameters:
- Freundlich K_F = 25.738; 1/n = 0.5026; R² = 0.9689.
- Temkin A_T = 0.2278 L/mg; B = 106.57; R² = 0.9699.

The third-party Table 1 kinetic model values are:
- Pseudo-first-order fitted q_e = 26.15 mg/g; k_1 = 0.0055 min−1; R² = 0.8544.
- Pseudo-second-order fitted q_e = 38.7596 mg/g; k_2 = 0.000979 g mg−1 min−1; R² = 0.9961.
- Intraparticle diffusion k_i = 1.7547 mg g−1 min−1/2; intercept C = 7.5976 mg/g; R² = 0.8706.

These kinetic q_e values are model-fitted parameters, not a direct measurement of equilibrium uptake. Keep the PFO and PSO values separate from each other and from Langmuir q_max.

## Experimental setup and the central dosage discrepancy
The third-party mirror's §2.5 describes the optimized/baseline set of conditions as:
- 10 mL ciprofloxacin solution.
- Initial ciprofloxacin concentration = 3 mM.
- 5 mg mGG/GO NC.
- pH = 7.1.
- Temperature = 298 K.
- Adsorption allowed to reach dynamic equilibrium.

Thus, for this baseline:
- 5 mg sorbent in 10 mL = 0.5 g/L.
- Ciprofloxacin molecular mass used for conversion ≈331.34 g/mol.
- 3 mM CIP ≈994 mg/L.
- Initial CIP mass = 0.003 mol/L ×0.010 L ×331.34 g/mol ≈0.00994 g = 9.94 mg.
- Feed-limited q_e ceiling = 9.94 mg /0.005 g sorbent ≈1,988 mg/g.

Both the fitted Langmuir q_max (555.56 mg/g) and PSO-fitted q_e (38.76 mg/g) are below that baseline feed-mass ceiling. This demonstrates only that they do not violate the baseline's crude mass ceiling; it does not validate that the fit parameters belong to this exact batch.

However, §4.1.3 “Effect of adsorbent dosage” says uptake capacity rises up to 5 g/L and starts decreasing at doses greater than that. This is ten times the baseline dose:
- Baseline: 5 mg /10 mL = 0.5 g/L.
- Dose-response stated optimum: 5 g/L.

The mirror does not clearly state the exact dosage corresponding to the Langmuir q_max fit in Table 2. Do not assign 5 g/L to the isotherm fit unless the full Methods/table clarify it. The conflict is important for mass balance:
- At C0 = 700 mg/L in 10 mL and 5 mg sorbent, initial CIP mass = 7 mg; the feed ceiling is 7mg /0.005g = 1,400mg/g.
- If the same 10 mL /700mg/L condition instead used a 5g/L dose (50mg sorbent), the ceiling would be 7mg/0.05g = 140mg/g.
- In the latter scenario, a 555.56mg/g q_max cannot be achieved because it exceeds the available CIP feed by about four times. This would not be a valid contradiction if the 5g/L dose-response test is a separate experiment from the concentration/isotherm series; the manuscript simply does not pin the isotherm dose clearly enough to resolve the ambiguity.

The 10× difference must remain visible in the candidate and condition-labelled rows. Do not silently change 5g/L to0.5g/L or vice versa.

## Concentration and temperature series
The mirror's §4.1.2 states that initial CPX concentrations of 100, 300, 500 and 700 mg/L were tested at pH 7.1 at 298, 313 and 323 K while contact-time behavior was recorded. The text reports:
- Uptake increases with initial CPX concentration.
- At the highest initial concentration (700 mg/L), the graph is described as reaching approximately 560 mg/g, then approaching a plateau.
- This is an approximate plotted value from the text, not an exact tabulated observed qe. Do not present it as a direct numerical table endpoint.
- Higher temperatures decrease uptake relative to 298 K; the authors select 298 K as optimal for adsorption.
- The full plot values and exact experimental q_e data are not independently verifiable without the publisher-hosted article or an author-provided copy.

## pH, pH_zpc and speciation
The mirror states:
- mGG/GO NC pH_zpc = 8.
- Maximum adsorption efficiency is at pH 7.1.
- CIP pKa_1 = 5.9 ±0.15; pKa_2 = 8.89 ±0.11.
- CIP is predominantly cationic below pKa_1, anionic above pKa_2, and neutral/zwitterionic over the intervening pH region.

The authors propose that pH 7.1 (just below the pH_zpc) places the surface slightly positive and CIP largely zwitterionic, allowing electrostatic interactions and hydrophobic effects. At strongly acidic/alkaline pH, charge repulsion and lower hydrophobic interaction may reduce uptake. These mechanisms are proposed, not quantitatively apportioned.

## Preparation and material characterization (third-party mirror text)
### GO by modified improved Hummers
- 1.0 g finely powdered graphite flakes in25 mL of98% H2SO4, maintained below5°C in an ice bath, stir2h.
- Add3g KMnO4 slowly; stir at40°C for2h.
- Add50mL DI water and stir3h; then add a further100mL DI water.
- Cool in ice-cold water to control the exothermic rise and quench with1mL of30% H2O2.
- Filter/purify by alternating37% HCl and DI-water washes, centrifuging at approximately7000rpm and vacuum-drying after wash steps.
- Final isopropanol wash to obtain finely separated GO.

### Magnetic guar gum/GO composite
The mirror reports:
- 25mL aqueous FeCl2 and25mL aqueous FeCl3 solutions in a2:1 molar ratio; concentrations and iron-salt masses are not given.
- Disperse2mg GO in10mL DI water and ultrasonicate1h.
- Disperse2mg guar gum in50mL DI water; combine with GO dispersion and stir1h.
- Add approximately3mL of30wt% aqueous ammonia dropwise to co-precipitate magnetic Fe3O4.
- Separate with an external magnet, wash repeatedly with DI water to neutral pH, vacuum-dry under moderate heating, crush and grind.

The printed mirror values of2mg GO and2mg guar gum are preserved as transcribed; no unit correction is assumed. The missing FeCl2/FeCl3 solution concentrations also prevent reconstruction of the iron mass balance and final composite yield.

Characterization in the mirror includes XRD, Raman, FTIR, HRTEM, EDX, FESEM, VSM, pH_zpc and TGA. Saturation magnetization is reported as18emu/g, with no visible coercivity/hysteresis, suggesting superparamagnetic behavior.

## Thermodynamics
The mirror's Table 3 reports:
- ΔG° = −8.047 kJ/mol at298K.
- ΔG° = −5.833 kJ/mol at313K.
- ΔG° = −6.061 kJ/mol at323K.
- ΔH° = −33.055 kJ/mol.
- ΔS° = +84.8 J/mol/K.

The authors interpret the process as spontaneous and exothermic. Values are retained as mirror-provisional; note the unusual non-monotonic ΔG° sequence with the largest magnitude at298K, consistent with the authors' selection of298K as the optimum condition.

## Regeneration
The mirror's §4.5 describes six adsorption–desorption cycles:
- Magnetically separate the spent adsorbent.
- Transfer into1% ethanol solution.
- Desorb for3h in an incubator shaker at room temperature.
- Wash with distilled water to neutral pH and dry before the next adsorption cycle.
- The paper states that approximately95% adsorption efficiency remains after the sixth cycle.

This is not a cycle-resolved q_e or adsorption-capacity-retention table. Do not rewrite “95% adsorption efficiency” as “95% capacity retained” without the figure's exact metric and values. Ethanol concentration/volume recovery and solvent treatment are not costed.

## Cost and real-water evidence
- The paper describes the composite as low-cost/sustainable, but no normalized preparation cost, yield, energy per gram, water/solvent inventory, treatment cost per m³, or full TEA/LCA is provided in the accessible article text.
- The batch work is based on prepared CIP aqueous solutions. No separately verified real municipal/industrial wastewater sample, natural-water trial, continuous-flow column, or full-scale demonstration is identified.
- Magnetic separability and guar-gum use are relevant design benefits, but they do not establish the economic advantage of the full GO/Fe3O4/guar-gum process.

## Decision for the semester paper
Retain SEM-011 as a provisional magnetic polysaccharide/GO/CIP study:
1. Cite the publisher-supported maximum capacity555.56mg/g as author-reported and, based on the mirror's Table2, as Langmuir-fitted q_max; do not label it observed qe.
2. Keep PSO-fitted qe38.7596mg/g separate from PFO-fitted qe26.15mg/g.
3. Preserve the discrepancy between Table2 R²=.9915 and prose R²=.9989.
4. Flag the baseline dose0.5g/L vs the dosage-response peak5g/L (10×) and keep the isotherm-specific dose unresolved.
5. Keep the 700mg/L approximate graph uptake (~560mg/g) separate from q_max.
6. Treat six-cycle1% ethanol and≈95% efficiency after cycle6 as provisional mirror-only; do not call it q-capacity retention.
7. No verified real-water/cost/energy/yield evidence.

The record is excluded from a clean quantitative ranking until the publisher/author full text clarifies the dosage used for the isotherm fit and resolves the regression R² mapping.

## Repository updates
Updated in place:
- data/semester-remaining-work-register.csv
- data/semester-paper-candidate-register.csv
- data/semester-evidence-readiness-audit.csv (EV-SEM-010)
- data/semester-condition-labelled-comparison.csv (EV-SEM-010)
- data/semester-manuscript-claim-evidence-audit.csv (CLM-21)
- data/source-caveats.csv
- README.md

No new SEM evidence ID was created. The main manuscript comparison table was not given a numeric winner row or invalid citation, because the full-text/dose issue remains provisional and no verified Better BibTeX key was found.
