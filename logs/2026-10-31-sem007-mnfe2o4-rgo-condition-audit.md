# SEM-007 MnFe2O4/rGO tetracycline condition and mass-balance audit — 31 October 2026

## Study identity
Bao, J. et al. (2018), “Adsorption of Tetracycline with Reduced Graphene Oxide Decorated with MnFe2O4 Nanoparticles,” *Nanoscale Research Letters* 13, article 396. DOI: 10.1186/s11671-018-2814-9.

Official primary full text:
- PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC6281545/
- Springer: https://link.springer.com/article/10.1186/s11671-018-2814-9
- PubMed: https://pubmed.ncbi.nlm.nih.gov/30519822/

The full text, original eight-page PDF and figure/table content were reviewed previously. This targeted pass rechecked the exact kinetic/pH/cycle condition lines and reconciled them with the condition-labelled comparison.

## Kinetic uptake condition — volume now explicitly verified
The primary Methods state:
- TC concentration: 10 mg/L.
- Adsorbent mass: 5 mg MnFe2O4/rGO.
- Solution volume: 30 mL (the adsorption equation's V is explicitly stated to be 30 mL).
- Temperature: 25 °C.
- Oscillator speed: 180 rpm.
- Equilibrium: approximately 8 h.

Thus, the adsorbent dose is:
- 5 mg / 30 mL = 0.1667 g/L.

The total TC feed mass is:
- 10 mg/L × 0.030 L = 0.30 mg TC.

With 0.005 g adsorbent, the feed-limited capacity ceiling is:
- 0.30 mg / 0.005 g = 60 mg/g.

The source-reported uptake is approximately 41 mg/g at C0=10 mg/L. This is below the 60 mg/g feed ceiling and is therefore mass-balance plausible. The pH for the main kinetic uptake point is not explicitly stated in the text; do not assign the pH optimum from the separate pH experiment to this point.

## Separate pH-dependence experiment
The Methods state that 30 mL TC solution at 10 mg/L and 5 mg MnFe2O4/rGO were used, with pH adjusted across:
- 2.0
- 3.3
- 5.0
- 7.7
- 9.0
- 9.7
- 10.5

The maximum adsorption capacity in this pH series is reported at pH 3.3, with the Figure 6 text/plot giving a Q value up to approximately 53.6 mg/g. This is a separate condition-resolved pH result and should not be substituted for the ~41 mg/g kinetic uptake point with unspecified pH.

## Isotherm model and ranking caveat
Table 2 reports Langmuir fitted q_m:
- 283 K: 870 mg/g (R²=.9838)
- 298 K: 1131 mg/g (R²=.9723)
- 313 K: 1326 mg/g (R²=.9795)

Freundlich fit statistics:
- 283 K: R²=.9951
- 298 K: R²=.9978
- 313 K: R²=.9981

Freundlich R² is higher than Langmuir at each reported temperature. Therefore:
- keep Langmuir q_m values explicitly model-derived;
- do not rank them as observed uptake or compare them directly with the ~41 mg/g condition-specific uptake;
- do not claim Langmuir is the preferred model on fit quality when the paper's own R² values favor Freundlich.

## Acid regeneration — method/figure count discrepancy
The primary text states:
- Eluent: 0.1 mol/L HCl.
- Initial TC removal: 86%.
- After HCl elution, removal values are 85%, 82%, 79% and 71% for the first four cycles shown in Figure 6.

However, the Methods text says elution was carried out three times, while the figure presents four post-initial cycle points. Preserve both facts. Do not silently change the stated number of elutions or remove the fourth plotted cycle.

These values are removal efficiency, not a capacity-retention series. The source does not provide a cycle-resolved qe-retention table.

## Semester-paper decision
Retain SEM-007 as a primary MnFe2O4/rGO–TC example for:
- magnetic recovery and acid regeneration;
- a condition-specific ~41 mg/g uptake at 10 mg/L, 5 mg/30 mL, 25 °C, 180 rpm, ~8 h;
- a separate pH optimum at pH 3.3 with Q≈53.6 mg/g;
- qualitative comparison of Freundlich and Langmuir model fit.

Do not:
1. Assign pH 3.3 to the kinetic ~41 mg/g result; pH is not specified for that point.
2. Compare the Langmuir fitted q_m values (870–1326 mg/g) as observed uptake; Freundlich has higher R² at all temperatures.
3. Treat cycle removal percentages as retained q-capacity.
4. Hide the three-method-elutions versus four-plotted-post-initial-points discrepancy.
5. Claim a quantified cost, real-water validation or economic advantage.

## Citation workflow
The latest uploaded 173-entry BibTeX/candidate key export did not contain a verified citation key for DOI 10.1186/s11671-018-2814-9. Do not invent a Better BibTeX key. Add the DOI in Zotero only if the study is selected for manuscript inclusion, then verify the generated key before citing.

## Repository updates
Updated in place:
- data/semester-remaining-work-register.csv
- data/semester-paper-candidate-register.csv
- data/semester-evidence-readiness-audit.csv (EV-SEM-003)
- data/semester-condition-labelled-comparison.csv (EV-SEM-003)
- data/source-caveats.csv
- README.md

No new evidence ID was created. The manuscript's current 15-study citation table does not yet include SEM-007 because its citation key is not verified.
