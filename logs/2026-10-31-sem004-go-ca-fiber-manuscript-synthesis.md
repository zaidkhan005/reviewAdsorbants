# SEM-004 GO/calcium-alginate fiber tetracycline manuscript-synthesis audit — 31 October 2026

## Study identity
Zhu, H., Chen, T., Liu, J. and Li, D. (2018), “Adsorption of tetracycline antibiotics from an aqueous solution onto graphene oxide/calcium alginate composite fibers,” *RSC Advances* 8, 2616–2621. DOI: 10.1039/C7RA11964J.

Official RSC full text: https://pubs.rsc.org/en/content/articlehtml/2018/ra/c7ra11964j
PubMed Central full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC9077392/
PubMed: https://pubmed.ncbi.nlm.nih.gov/35541451/

The open RSC article was rechecked on 31 October 2026, including Methods §§2.2–2.4, Results §§3.2.1–3.2.4, Tables 1–2, Figure 4 and the mechanism/conclusion sections.

## Material preparation
GO/calcium-alginate (GO/CA) composite fibers were prepared by freeze-drying and CaCl2 crosslinking:
- GO was dispersed in water and ultrasonicated for 30 min.
- A 2 wt.% sodium alginate solution was prepared and mixed with GO.
- The mixture was injected into 5 wt.% CaCl2 solution to form crosslinked fibers.
- Fibers were allowed to stand for 12 h, washed and vacuum freeze-dried.

The authors describe GO/CA as a 3D fiber composite intended to reduce free GO dispersibility and facilitate recovery, but do not demonstrate repeated-cycle regeneration in the adsorption tests. Freeze-drying and CaCl2 crosslinking are explicit processing steps; no quantified freeze-drying energy, GO yield, or complete process-cost inventory is supplied.

## Four distinct experimental endpoints — do not merge
### 1. Equilibrium isotherm points (Table 1 / §3.2.3)
- Adsorbent: 25 mg GO/CA fibers.
- Solution volume: 50 mL.
- Temperature: 25 °C.
- Contact time: 5 h.
- TC initial concentration was varied.

The article reports:
- At C0 = 10 mg/L, Ce = 1.2 mg/L and observed qe = 17.6 mg/g.
- At C0 = 60 mg/L, Ce = 27.3 mg/L and observed qe = 65.4 mg/g.

These are experimental equilibrium uptake values from the concentration/isotherm experiment. Do not pair them with the separate pH-study or time-course percentages.

### 2. pH effect (Figure 4a / §3.2.1)
- GO/CA mass: 10 mg.
- Solution volume: 20 mL.
- TC concentration: 50 mg/L.
- pH varied from 2 to 9.

The paper reports a maximum **removal percentage** of 56.8% at pH 6. This is not an uptake value of 56.8 mg/g. Keep the percent sign and the experiment’s separate 10 mg / 20 mL condition explicit.

### 3. Adsorbent-dose effect (Figure 4b / §3.2.2)
- TC concentration: 50 mg/L.
- Solution volume: 20 mL.
- GO/CA dose varied from 5 to 30 mg.
- Reported removal range: approximately 35.0–69.4%.

Do not combine these dose-series removal percentages with either isotherm qe.

### 4. Agitation-time experiment (Figure 4d / §3.2.4)
- TC initial concentration: 50 mg/L.
- Adsorbent mass: 200 mg GO/CA fibers.
- Solution volume: 400 mL.
- Uptake is higher during the first two hours and then slows.
- The text states that the process reaches equilibrium after 15 h with experimental qe = 56.8 mg/g.

This is a separate time-course endpoint. It is not the same experiment as the isotherm qe values (17.6 and 65.4 mg/g) or the pH removal percentage (56.8%). Keep all three contexts separate.

## Isotherm fit caveat (Table 1)
Table 1 reports:
- Langmuir qmax = 131.57 mg/g, kL = 0.11 L/g, R² = 0.9938.
- Freundlich kF = 16.11 L/g, 1/n = 0.41, R² = 0.9986.

Freundlich has the higher R² (0.9986 versus 0.9938), even though the authors highlight the Langmuir qmax in the abstract and conclusion. Do not state that Langmuir is statistically the best-fitting model without explaining this source-internal model-selection tension. qmax is a fitted asymptote, not a measured qe.

## Kinetic fits versus measured time-course qe (Table 2)
Table 2 reports:
- Pseudo-first-order fitted qe = 40.93 mg/g; k1 = 0.45 min−1; R² = 0.9020.
- Pseudo-second-order fitted qe = 62.50 mg/g; k2 = 23.27 × 10−3 g mg−1 min−1; R² = 0.9990.

The separate experimental time-course text gives qe = 56.8 mg/g at 15 h. The PSO fitted qe = 62.50 mg/g is a model-derived parameter and does not equal the measured time-course endpoint. Preserve both values and their origins. Do not replace the measured qe with the model output or call them equivalent.

The authors' narrative says PSO provides the better kinetic correlation, which is consistent with the higher R². However, a good kinetic fit does not turn its fitted qe into an observed value.

## Mechanism and evidence boundary
The article discusses hydrogen bonding and π–π interactions between TC and the GO/CA fiber surface, along with ionic interactions between tetracycline cations and anionic surface groups. The material contains GO oxygen functionalities and alginate hydroxyl/carboxyl groups.

No real-water/natural-water or actual-wastewater validation, no adsorption–desorption reuse cycles, no cycle-specific capacity retention, and no monetized preparation or treatment cost are reported in the full article.

## Semester-paper decision
Retain SEM-004 as a primary TC/GO–polymer composite example. In synthesis and manuscript comparison:
1. Report isotherm observed qe = 17.6 mg/g at C0=10 mg/L and 65.4 mg/g at C0=60 mg/L under 25 mg/50 mL, 25 °C, 5 h.
2. Report the separate time-course experimental qe = 56.8 mg/g at 15 h (50 mg/L TC, 200 mg adsorbent, 400 mL).
3. Report the separate pH-study maximum as 56.8% removal at pH 6 (not 56.8 mg/g).
4. Report Langmuir qmax = 131.57 mg/g as fitted; note Freundlich R²=.9986 exceeds Langmuir R²=.9938.
5. Report PSO-fitted qe=62.50 mg/g as a kinetic model parameter, not the measured time-course qe=56.8 mg/g.
6. Do not claim regeneration, real-water performance or quantified low-cost preparation.

## Repository updates
Updated in place:
- data/semester-remaining-work-register.csv
- data/semester-paper-candidate-register.csv
- data/semester-evidence-readiness-audit.csv (EV-SEM-002)
- data/semester-condition-labelled-comparison.csv (EV-SEM-002)
- data/semester-manuscript-claim-evidence-audit.csv (CLM-01)
- data/source-caveats.csv
- manuscript/SEMESTER_TABLE_1_CORE_STUDY_COMPARISON_V1.md
- README.md

The existing verified Zotero citation key zhuAdsorptionTetracyclineAntibiotics2018 is retained. No new evidence ID was created.
