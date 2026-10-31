# SEM-016 sulfonated-GO/CIP primary-PDF audit — 31 October 2026

## Study identity and source
Shaha et al. (2025), “Exploring the Adsorption Efficiency of Sulfonated Graphene Oxide for Ciprofloxacin Removal from Aqueous Solution: Insights from Density Functional Theory, Kinetics, Thermodynamics, and Reusability,” *ACS Omega* 10(36), 40817–40832. DOI: 10.1021/acsomega.4c11231.

- Primary source: existing Library file `graphene 1.pdf` (16 pages), downloaded from ACS by the user on 15 October 2026.
- Publisher DOI: https://pubs.acs.org/doi/10.1021/acsomega.4c11231
- PubMed record: https://pubmed.ncbi.nlm.nih.gov/40978422/
- Official supporting information: ao4c11231_si_001.pdf, described by the article as Table S1 (estimated diffusion parameters) and Figure S1 (EDX elemental spectra). This SI does not provide missing adsorption raw measurements that would supersede the main-text values.

Pages 2–14 of the existing Library PDF were inspected; Figures 3–10, Table 1, Table 2 and Figure 15 were visually inspected from rendered PDF pages. This re-audit is based on the user's existing PDF, not a replacement copy found online.

## Material and preparation
- Adsorbent: sulfonated graphene oxide (SGO).
- Raw graphite flakes were purchased from Sigma-Aldrich and used as supplied; this is not a waste-derived adsorbent.
- Modified improved Hummers synthesis: 3.0 g graphite flakes added to a 9:1 mixture of 18.4 mol/L H2SO4 and 14.6 mol/L H3PO4, pre-stirred 30 min; add 18.0 g KMnO4 under magnetic stirring at 30 °C; stir 24 h; add 400 mL cold water and 3 mL of 30% H2O2; allow solid to settle; wash sequentially with 7.7 mol/L HCl, DI water, ethanol and diethyl ether; oven dry at 60 °C. The total mixed-acid volume is not reported in the extracted Methods.
- No mass yield, oxidant/acid recovery, waste-treatment details, energy consumption, or financial process cost is reported.
- The process uses 6 g KMnO4 per gram of graphite, high-molarity concentrated acids, H2O2, strong HCl, two organic washing solvents, and repeated washing. This burden should be stated in the preparation/cost discussion; “sulfonated GO” does not by itself establish low-cost or low-impact production.

## Core batch protocol and equations
The main adsorption method states 50 mL ciprofloxacin solution, SGO dose 0.2 g/L (therefore 0.010 g SGO), pH 4.0, 25 °C and 150 rpm; 240 min was used to reach equilibrium for later studies. The paper gives:
- qe = (C0 − Ce)V/m, using concentration in µmol/L, volume in L and mass in g.
- % removal = (C0 − Ce)/C0 ×100.

The mass-balance feed ceiling is therefore C0 ×0.050 L /0.010 g = 5×C0 µmol/g for this base setup.

## Condition-series consistency audit
### Concentration series (Table 1; Figure 5; §3.4)
Conditions: C0=10, 25, 50, 75 and100 µmol/L; SGO=0.2 g/L; 50 mL; pH4; 25 °C. Table1 reports qe(exp):
- 10 µmol/L: 45.45 µmol/g; feed ceiling 50 µmol/g; implied removal 90.90%.
- 25 µmol/L: 121.06 µmol/g; ceiling125; implied removal 96.85%.
- 50 µmol/L: 237.12 µmol/g; ceiling250; implied removal 94.85%.
- 75 µmol/L: 326.06 µmol/g; ceiling375; implied removal 86.95%.
- 100 µmol/L: 402.58 µmol/g; ceiling500; implied removal 80.52%.

However §3.4 prose says removal decreases from 97.32% at 10 µmol/L to81.28% at100 µmol/L. On the same stated basis the first endpoint differs by about6.42 percentage points (90.90 vs97.32) and the last by about0.76 points (80.52 vs81.28). No source correction or explanation is offered. Retain Table1 qe and prose removal as separate reported streams; do not calculate a replacement qe or select one as “correct”.

### Temperature series (Table 1; Figure 7; §3.6)
At C0=50 µmol/L, SGO0.2 g/L,50mL,pH4:
- Table1 qe(exp) at25,30,35,40 °C =237.12,242.12,242.72,244.24 µmol/g.
- Feed ceiling at each temperature is250 µmol/g, giving derived removals94.85,96.85,97.09,97.70%.
- §3.6 prose states removal rises from96.53% at25 °C to99.66% at40 °C. The endpoint differences from Table1's mass-balance-derived percentages are about1.68 and1.96 percentage points.

Again, retain the prose removals and Table1 qe separately; do not repair them.

### Dosage series (Figure 4; §3.3)
At C0=50 µmol/L,50mL,pH4,25°C, SGO dose rises from0.06 to0.4 g/L:
- Source prose: removal rises60.10→97.98%; qe falls495.96→121.29 µmol/g.
- At0.06 g/L, sorbent mass in50mL is0.003 g, feed ceiling833.33 µmol/g; qe495.96 implies59.52% removal.
- At0.4 g/L, sorbent mass is0.020 g, feed ceiling125 µmol/g; qe121.29 implies97.03% removal.
- Differences are approximately0.59 and0.95 percentage points respectively.
These are smaller than the concentration/temperature endpoint conflicts, but preserve the discrepancy in the audit.

### pH series (Figure 3; §3.2)
At50 µmol/L,0.2 g/L,50mL,25°C, pH2–11 is tested. Maximum uptake reported atpH4, qe=238.48 µmol/g; lower uptake atpH2 is attributed to competition/repulsion involving protonated CIP, while uptake declines above pH9 as hydroxide and deprotonated CIP compete for sites. Source-specified CIP species: CPF3+ below pH3.64; CPF2+ up topH5.05; CPF+ up topH6.95; neutral between6.95–8.95; CPF− abovepH8.95. Treat the pH optimum as condition-specific, not a universal material property.

## Kinetics and model fit
Table1 concentration-series PSO fitted qe(cal) values are46.95,123.46,243.90,333.33 and416.67 µmol/g, with R²=.9995–.9999. The Table1 temperature-series PSO fitted qe(cal) values are243.90,243.90,243.90 and250.00 µmol/g at25/30/35/40 °C. PSO RMSE (1.73–14.82) is lower than PFO (28.70–206.49) and Elovich (4.27–21.12). These are fitted kinetic parameters, not the measured qe(exp) nor q_m. The paper interprets the fit as compatible with adsorption, but PSO superiority alone does not prove chemisorption.
Film diffusion and intraparticle diffusion analysis suggests more than one stage; Figure8 does not cross the origin, so intraparticle diffusion is not the sole rate-limiting step.

## Isotherm capacity — fitted q_m, separate concentration range
Figure10 states isotherm C0=50–1000 µmol/L, SGO0.2 g/L,pH4, temperatures25/30/35/40 °C. This is separate from the kinetic/concentration series10–100 µmol/L.
Table2 nonlinear Langmuir q_m=1000 µmol/g (=331.35 mg/g using CIP molar mass331.35 g/mol) for all four temperatures, R²=.9998. Langmuir is the best of the four fitted models according to the table (Freundlich R²=.9127–.9150; Temkin=.9642–.9662; Dubinin–Radushkevich=.7513–.7592). q_m is a model asymptote, not an observed uptake and must not replace qe(exp). D–R fitted capacity is797.43–805.05 µmol/g with E=.75–1.00 kJ/mol; keep that model parameter distinct as well.

Thermodynamic results: ΔH=+6.35 kJ/mol; ΔS=+113.64 J/(mol K); ΔG=−27.50 to−29.22 kJ/mol across25–40 °C. The source interprets adsorption as spontaneous and endothermic. Activation energy Ea=20.67 kJ/mol; activation ΔH‡=18.13 kJ/mol and ΔS‡=−128.79 J/(mol K).

## Salt effects
Na2SO4, K2SO4, CaSO4 and MgSO4 were each tested at0.1 M. The presence of the salts reduces qe and removal; the source's effect order is Ca2+>Mg2+>K+>Na+. These are high-concentration single-salt stress tests in synthetic solution, not actual water-matrix validation or a substitute for multi-ion/DOM testing.

## Mechanistic interpretation
The source proposes electrostatic attraction between negatively charged SGO surface groups (carboxylate/sulfonate above pH2.5) and cationic CIP, hydrogen bonding between hydroxyl/carboxyl groups and polar CIP groups, and π–π stacking between aromatic domains. FTIR peak shifts: SGO O–H 3406→3452 cm−1; carboxyl C=O 1734→1754; C=C 1624→1628; C–O–C, C–O and S–O bands also shift. EDX detects fluorine only after CIP uptake; SEM shows a smoother loaded surface. DFT calculates two SGO–CIP complex interaction energies of−9.08 and−4.48 kJ/mol and optimized structures. Use these as convergent support for plausible interactions, not quantitative proof of each contribution.

## Regeneration and reusability — directly verified
- Adsorption basis for Figure15: 50 µmol/L CIP, SGO0.2 g/L, pH4,25 °C; the article reports the direct baseline uptake as239.39 µmol/g.
- Desorption: 0.010 g loaded SGO into50 mL DMF containing1 mol/L HCl; 98.11% of loaded CIP released within10 min; >99.14% released within240 min.
- The loaded SGO is collected, washed with water until neutral pH and oven-dried at100 °C before reuse.
- Figure15b reports qe for direct and subsequent reuse:239.39,237.94,233.27,231.46,229.91 and229.29 µmol/g (cycles1–5).
- Fifth-use qe retention =229.29/239.39×100 =95.78%. This is a direct qe-based capacity-retention calculation; it is distinct from the >99.14% desorption release.
- The conclusion says five to six adsorption–desorption cycles; Figure15 graph shows direct plus five reuse points. Report five reuse cycles as clearly evidenced.
- DMF and 1 M HCl, solvent handling/recovery, neutralization, and 100 °C drying are significant regeneration burdens; no solvent recovery or regeneration cost is reported.

## Cost and application boundary
No actual wastewater or natural water test is reported; no monetized preparation/operating cost, USD/kg adsorbent, treatment cost per m³, measured energy, production yield, acid recovery, solvent recovery or complete TEA/LCA is presented. The graphite is commercial graphite flakes, not waste. The process uses concentrated acid/oxidant and organic solvents for synthesis and DMF+1M HCl for regeneration. Do not present this as a demonstrated low-cost adsorbent despite the authors' qualitative cost-effectiveness statements.

## Semester-paper decision
Retain SEM-016 as an SGO/CIP mechanism, salt-sensitivity and solvent-regeneration study. Do not use its paired qe/removal endpoints as clean quantitative benchmarks until the authors clarify the inconsistencies. Present:
1. Table1 qe(exp) values and prose removal percentages separately, with explicit mass-balance discrepancy.
2. PSO fitted qe(cal) separately from measured qe(exp).
3. Langmuir q_m=1000 µmol/g (331.35 mg/g) as a fitted asymptote for the separate50–1000 µmol/L isotherm series.
4. Five-cycle qe retention95.78% separately from >99.14% CIP release in DMF+1M HCl.
5. Commercial graphite precursor and strong acid/oxidant + DMF/HCl process boundary; no real-water trial or quantified cost.

## Citation workflow
The exact DOI/title match and Better BibTeX key `shahaExploringAdsorptionEfficiency2025` were already verified in the supplied Zotero citation export. Keep that existing key; no new key is needed.

## Repository updates
Updated in place:
- data/semester-remaining-work-register.csv
- data/semester-paper-candidate-register.csv
- data/semester-evidence-readiness-audit.csv (EV-SEM-012)
- data/semester-condition-labelled-comparison.csv
- data/semester-manuscript-claim-evidence-audit.csv (CLM-06)
- manuscript/SEMESTER_TABLE_1_CORE_STUDY_COMPARISON_V1.md
- README.md

No duplicate evidence ID created; EV-SEM-012 and master evidence EV-B14-011–EV-B14-015 remain in place.
