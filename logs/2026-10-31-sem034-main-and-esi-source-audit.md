# SEM-034 main-text and ESI source audit — 31 October 2026

## Study identity and authoritative sources
Hossain, Kabir, Ali Shaikh, Haque and Yasmin (2024), “Ultrafast and simultaneous removal of four tetracyclines from aqueous solutions using waste material-derived graphene oxide-supported cobalt–iron magnetic nanocomposites,” *RSC Advances* 14, 1431–1444. DOI: 10.1039/D3RA07597D.

Official RSC article: https://pubs.rsc.org/en/content/articlehtml/2024/ra/d3ra07597d
Open full text in PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC10763703/
Official RSC ESI PDF: https://www.rsc.org/suppdata/d3/ra/d3ra07597d/d3ra07597d1.pdf

The RSC HTML direct open was access-limited in this session; the PMC-hosted open full text and official RSC search result were used. The ESI PDF was opened as a parsed PDF record and its Table 1 / Figure S1 text was extracted. The PDF screenshot request returned 404, so the visual page render could not be verified; the extracted ESI table is retained as text evidence.

## Material identity and preparation
The material is a magnetic GO-supported cobalt–iron oxide (GO/Co–Fe) nanocomposite. The waste-derived part is the graphite feedstock for GO, recovered from spent dry-cell batteries; it is not accurate to imply the entire composite is made from waste material.

1. Dry-cell graphite rods are manually extracted, scrubbed, washed with DI water and powdered. Graphite is purified with Aqua Regia, washed to neutral pH and dried at 60 °C for 24 h.
2. Improved Hummers oxidation: 2 g purified graphite in 240 mL H2SO4 + 28 mL H3PO4 (9:1 v/v), add 6 g KMnO4, heat/stir at 50 °C for 2 h; cool, add 400 mL DI water and 18 mL 30% H2O2; centrifuge 4000 rpm; wash with DI water, 30% HCl, DI water and ethanol; vacuum dry at 45 °C for 24 h.
3. Composite synthesis: dissolve Co(NO3)2·6H2O, FeSO4·7H2O and Fe2(SO4)3·nH2O in DI water at a 1:1:2 molar ratio; stir 40 °C for 25 min; add 100 mg GO; adjust pH to approximately 10; heat at 85 °C for 1 h; wash with ethanol and DI water to neutral pH; dry at 60 °C for 24 h.
4. Characterization: average Co–Fe particle size 19.2 nm; saturation magnetization 27.82 emu/g; zeta potential point of zero charge around pH 7.2. XPS assigns Co(II) and Fe(III).

The spent battery graphite is a recovered feedstock, but preparation still uses Aqua Regia, concentrated H2SO4/H3PO4, KMnO4, H2O2, 30% HCl, ethanol and cobalt/iron salts, plus heating, centrifugation, extensive washing and oven drying. No process yield, reagent recovery, energy-per-mass, metal-salt price or waste-treatment cost is given. Avoid treating “waste-derived” as proof of low total production cost or low environmental burden.

## ESI optimum table — previously uninspected
Official ESI Table 1 (“all treatments / combinations of factor levels”) adds the following details:

- Dose test: 0.5–12 mg; 30 min; pH 7; C0 0.2 ppm; 25 °C; optimum dose 3 mg.
- Time test: 3 mg; 0.5–20 min; pH 7; C0 0.2 ppm; 25 °C; optimum time 0.5 min.
- pH test: 3 mg; 0.5 min; pH 2–12; C0 0.2 ppm; 25 °C; optimum pH 7.
- Initial concentration test: 3 mg; 0.5 min; pH 7; C0 0.2 ppm; 25 °C; optimum C0 0.2 ppm.
- Kinetic test: 3 mg; 0.5–90 min; pH 7; C0 0.2 ppm; 25 °C; fitted with pseudo-second-order.
- Isotherm test: 3 mg; 0.5 min; pH 7; C0 0.2–10 ppm; 30, 40 and 50 °C; fitted with Langmuir.

The main article's Methods §2.6 differ in two particulars:
- It lists discrete pH values 2, 3, 6, 7, 8, 9 and 10, whereas ESI Table 1 says pH 2–12.
- Main Methods state isotherm C0 = 2–10 ppm, whereas ESI Table 1 states 0.2–10 ppm.
Preserve both source ranges; do not silently harmonize them. Main Methods also list concentration series 0.2, 0.4, 0.6, 1.0, 1.2, 1.5 and 2.0 ppm for the screening/factor experiments.

ESI gives optimum mass dose 3 mg and the main article gives optimum dose concentration 0.15 g/L. If both describe the same setup, they imply 20 mL liquid volume (3 mg / 0.15 g L−1). However, main Methods do not expressly state the batch volume; 20 mL is an inference from those paired quantities, not a source-stated volume.

## Rapid removal endpoint and mass balance
- The principal reported condition is C0 = 0.2 mg/L (200 ppb), dose = 0.15 g/L, pH 7, 25 °C, 250 rpm, contact time 30 s.
- TC removal has three source values: 94.1% in abstract and §3.2.2/Figure 5(b); 93.91% in §3.2.4; 93.94% in the conclusion. Preserve this 93.91–94.1% reported interval and identify the text location when citing.
- At C0 = 0.2 mg/L and adsorbent dose 0.15 g/L, the feed-limited loading ceiling is C0/dose = 1.333 mg/g. Applying the three reported removal percentages gives qe derived from mass balance ≈1.252–1.255 mg/g. This is a calculated value, not directly quoted as measured qe.
- Table 1 pseudo-second-order fitted qe for TC = 1.2681 mg/g (R² = .9991), which is slightly above the removal-derived estimate but below the 1.333 mg/g feed ceiling. The three source removal values and the fitted qe are close enough to be plausible with rounding/model-fit differences; do not substitute the fitted qe for a measured batch qe.
- The 3 mg ESI dose and 0.15 g/L main-text dose imply 20 mL, but the absent explicit batch-volume statement remains a minor provenance limitation.

## Kinetics and fitting diagnostics
Table 1 linearized kinetic fits:
- Pseudo-first-order TC qe = 0.0990 mg/g; R² = .1174.
- Pseudo-second-order TC qe = 1.2681 mg/g; R² = .9991.
- Elovich TC parameters include extremely small negative alpha (−5.28 × 10−35) and negative beta (−59.523); intraparticle-diffusion slope ki is also negative (−0.0141). These should be retained as source fit outputs but not interpreted as physically meaningful rate evidence without clarification.
- The authors interpret PSO as evidence of chemisorption. Do not repeat that inference as proof; a better PSO fit alone does not identify the molecular mechanism.

## Isotherms
- Langmuir TC q_m = 60.24 mg/g at 30 °C (R²=.9792), 62.50 mg/g at 40 °C (R²=.9781), and 64.10 mg/g at 50 °C (R²=.9980).
- Freundlich TC R² = .0324, .0514 and .2459 at 30, 40 and 50 °C respectively; Langmuir fit is markedly stronger in the authors' reported statistics.
- The isotherm endpoint is distinct from the 25 °C/200 ppb/30 s removal point. Do not attach 64.10 mg/g to the fast removal result.
- On the main reported isotherm maximum C0 = 10 mg/L and dose = 0.15 g/L, the simple feed ceiling is approximately 66.7 mg/g. The 64.10 mg/g fitted q_m at 50 °C is below that nominal ceiling but close to it. This is only a plausibility check, not a validation of all fitted data; the 2–10 vs 0.2–10 ppm starting-range conflict remains.
- At 50 °C TC Langmuir K_L is printed as 1428 L/mg (versus 140.8 and 169.9 L/mg at 30 and 40 °C); preserve the unusually high source value unless the authors clarify it.

## Simultaneous tetracycline co-targets and percentage discrepancy
The paper studies four tetracyclines together: TC, CTC, OTC and doxycycline (DTC). Keep per-analyte values distinct; do not treat all four as a single total removal value.
- Abstract reports 94.1% TC, 94.32% CTC, 94.22% OTC and 96.94% DTC.
- Main concentration-response subsection reports at C0 0.2 mg/L: 93.91% TC, 95.51% CTC, 93.21% OTC and 91.12% DTC.
- Conclusion gives 93.94% TC, 95.51% CTC, 93.21% OTC and 91.12% DTC.
For TC specifically the variation is small (94.1/93.91/93.94%); other tetracyclines show larger abstract-vs-main/conclusion differences. Keep the author locations visible instead of selecting one number.

## Recovery and magnetic separation
- The composite can be collected using an external magnetic field, consistent with its reported 27.82 emu/g saturation magnetization.
- Regeneration consists of methanol treatment, distilled-water wash and drying at 50 °C.
- The paper reports up to eight rounds and an overall removal-efficiency decrease from approximately 95% to 90%.
- No cycle-by-cycle TC-specific retained adsorption capacity or per-target regeneration profile is tabulated in the main text. Do not call the overall 95→90% profile a verified TC-only retained capacity.
- Methanol use, wash-water demand, separation time, adsorbent loss and spent-solvent handling are not costed.

## Mechanism and matrix applicability
- The ESI Figure S1 depicts electrostatic interaction, π–π interaction and hydrogen bonding. Main text also mentions electron-donor/acceptor interactions.
- FTIR peak changes, XPS Co/Fe states, zeta potential, and pH dependence provide support for plausible surface interactions. The point of zero charge is around pH 7.2; pH 7 is close to that value and the paper treats tetracyclines as zwitterionic around neutral pH.
- These findings support a mechanistic hypothesis, not a quantitative contribution breakdown. The PSO fit does not establish chemisorption by itself.
- No actual municipal/river/industrial wastewater trial, natural organic matter/ion interference study, or metal-leaching test was identified in the audited main text/ESI.

## Low-cost interpretation
The study reuses graphite rods from waste dry cells, and magnetic separation may ease solid recovery. But the whole route is not costed: Aqua Regia purification, strong-acid/oxidant GO synthesis, cobalt/iron salts, alkali pH adjustment, ethanol and DI-water washing, oven drying, methanol regeneration and waste solvent management are all burdens. No reagent prices, yield, electricity, regeneration operating cost, USD/kg adsorbent, USD/m³ treated, LCA or TEA is provided. Retain as an adsorption-performance and material-recovery case, not a validated low-cost winner.

## Semester-paper decision
Retain SEM-034 / EV-SEM-027. Report:
1. Simultaneous four-TC system; TC removal 94.1/93.91/93.94% depending source location.
2. qe derived from removal ≈1.252–1.255 mg/g; feed ceiling 1.333 mg/g; PSO fitted qe 1.2681 mg/g.
3. Langmuir fitted TC q_m 60.24/62.50/64.10 mg/g at 30/40/50 °C, separate from the 25 °C rapid-removal test.
4. ESI source ranges and main Methods source ranges separately.
5. Up to eight methanol regeneration rounds with broad 95→90% efficiency statement, without claiming TC-only capacity retention.
Do not call the full composite “waste-derived” without qualification; waste-cell graphite is the GO precursor input. No real water, cost or leaching evidence is established.

## Repository updates
Updated in place:
- data/semester-remaining-work-register.csv
- data/semester-paper-candidate-register.csv
- data/semester-evidence-readiness-audit.csv (EV-SEM-027)
- data/semester-condition-labelled-comparison.csv
- manuscript/SEMESTER_TABLE_1_CORE_STUDY_COMPARISON_V1.md
- README.md

No new evidence ID created; EV-SEM-027 updated in place.
