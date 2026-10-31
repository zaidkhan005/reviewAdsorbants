# SEM-001 GO–TC temperature-series and metric harmonization — 31 October 2026

## Study identity and source
Ghadim, E. E., Manouchehri, F., Soleimani, G., Hosseini, H., Kimiagar, S. and Nafisi, S. (2013), “Adsorption Properties of Tetracycline onto Graphene Oxide: Equilibrium, Kinetic and Thermodynamic Studies,” *PLOS ONE* 8(11): e79254. DOI: 10.1371/journal.pone.0079254.

Official PLOS full text: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0079254
PubMed: https://pubmed.ncbi.nlm.nih.gov/24302989/
DOI record: https://doi.org/10.1371/journal.pone.0079254

The PLOS publisher HTML was rechecked on 31 October 2026, including Methods, Figure 5/Table 1, Figure 6/Table 2, Table 3 thermodynamics, pH results and the release conclusion. The study was previously fully extracted; this pass harmonizes rather than repeats the entire extraction.

## Four protocol families must remain distinct
### 1. General adsorption / release experiment
The Methods describe 50 mL flasks containing GO at 20 mg/L and 25 mL TC solution at 6–180 mg/L, adjusted to pH 6–7 and incubated overnight. This context is described as demonstrating release efficiency. It is not the same as the smaller kinetic/isotherm mixing protocol.

### 2. pH-effect experiment
- GO stock: 2 mL at 20 mg/L.
- TC feed: 4 mL at 10–100 mg/L.
- pH adjusted from 2 to 10.
- Temperature: 25 ± 0.1 °C.
- Maximum adsorption is reported near pH 7.

This is a separate pH-response test. Do not combine its removal percentage with the isotherm or kinetic fitted endpoints.

### 3. Kinetic and kinetic-temperature series
- GO stock: 2 mL at 20 mg/L.
- TC feed: 4 mL at 6–180 mg/L.
- pH = 3.6.
- Aliquots/supernatant measurements are made at 15-minute intervals.
- The abstract reports equilibrium within 15 minutes.
- Figure 5 and Table 1 use 298, 308 and 318 K.

The kinetic Table 1 reports the pseudo-second-order model:
| T (K) | k2 | q2 (mg/g) | h (mg/g·min) | R² |
|---:|---:|---:|---:|---:|
| 298 | 0.3468 | 198.54 | 68.89 | 0.996 |
| 308 | 0.2742 | 381.77 | 104.7 | 0.994 |
| 318 | 0.5362 | 411.76 | 221.8 | 0.986 |

These are model outputs. The kinetic table labels the fitted capacity as q2, so keep that source notation rather than silently relabelling it as measured q_e. There is also a unit discrepancy: Table 1 labels k2 with units of 1/min, while the kinetic-equation text defines k2 with units of g/(mg·min). Preserve both source statements; do not choose one without author clarification.

### 4. Isotherm and thermodynamic temperature series
Isotherm conditions:
- GO stock: 2 mL at 20 mg/L.
- TC feed: 4 mL at 6–180 mg/L.
- pH = 3.6.
- Overnight incubation.
- Centrifugation: 6000 rpm for 30 minutes.
- Figure 6 and Table 2 specify 298, 303 and 308 K.

Table 2 values:
| T (K) | Langmuir fitted q_m (mg/g) | Langmuir R² | Freundlich K_F (mg/g) | n | Freundlich R² | D–R fitted q_m (mg/g) | D–R E (kJ/mol) | D–R R² |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 298 | 322.43 ± 1.25 | 0.997 | 21.40 | 3.656 | 0.943 | 24.62 ± 0.74 | 1.83 | 0.961 |
| 303 | 101.87 ± 1.08 | 0.993 | 20.09 | 3.762 | 0.962 | 22.92 ± 0.59 | 1.69 | 0.988 |
| 308 | 73.53 ± 0.55 | 0.998 | 20.13 | 3.721 | 0.983 | 24.94 ± 0.61 | 1.40 | 0.988 |

The two q_m columns are from different isotherm models. Do not compare D–R q_m as if it were a Langmuir q_m, or either as directly observed uptake.

**Important internal temperature inconsistency:**
- Methods, Figure 6 and Table 2 identify the isotherm temperatures as 298, 303 and 308 K.
- A Results sentence says isotherm constants were determined at 298, 303, 308, 310 and 313 K.
- The thermodynamic section independently discusses 298, 303, 308, 310 and 313 K.
- Table 2 contains only three temperature rows (298, 303 and 308 K).

Do not infer missing 310/313 K isotherm parameters or silently expand Table 2. Keep the thermodynamic series distinct from the isotherm-fit table.

## Temperature interpretation caveat
The Langmuir q_m values fall sharply from 322.43 mg/g at 298 K to 73.53 mg/g at 308 K, while the authors interpret positive ΔH° and negative ΔG° as endothermic and spontaneous adsorption. The D–R q_m values, in contrast, remain in a narrower range around 23–25 mg/g across the same three isotherm temperatures.

Kinetic PSO model q2 rises across its separate kinetic temperature series (298/308/318 K), but those are not the same metric or temperature points as the isotherm q_m values. Do not combine the two series into a single statement such as “capacity increases with temperature” or “capacity decreases with temperature.” The paper contains model- and protocol-specific results that cannot be reconciled from the published text alone.

## GO stock concentration versus final mixture dose
The kinetic and isotherm Methods state 2 mL of GO suspension at 20 mg/L mixed with 4 mL of TC feed. This supplies:
- GO mass = 20 mg/L × 0.002 L = 0.04 mg.
- Total mixed volume = 6 mL.
- Derived final GO concentration in the mixed suspension = 0.04 mg / 0.006 L ≈ 6.67 mg/L.

The paper labels the GO suspension as 20 mg/L; do not state 20 mg/L is the final mixed-system dose. TC feed concentrations 6–180 mg/L are stated for the 4 mL TC solution before mixing. The paper does not fully clarify whether the TC concentration used in every qe calculation is the pre-mix concentration or dilution-corrected final-mixture concentration, nor whether the mass-balance volume uses 4 mL feed or 6 mL total mixture. Preserve the feed-concentration label and the derived GO mass separately; do not reverse-engineer a direct qe endpoint without clarification.

## Release, mechanism and applicability
The conclusion reports up to 99.8% TC release across pH 2–10. This is pH-dependent desorption/release of TC from GO and is not a repeated adsorption–desorption cycle test or capacity-retention result.

Authors propose non-electrostatic dispersion/hydrophobic interactions, π–π stacking and cation–π bonding. The D–R adsorption energy values (1.83, 1.69 and 1.40 kJ/mol at 298, 303 and 308 K) are below 8 kJ/mol and are interpreted by the authors as physisorption. A pseudo-second-order kinetic fit does not itself prove chemisorption; keep the model fit separate from the authors’ broader interaction interpretation.

The study is an early synthetic GO–TC adsorption/release system. No actual wastewater/natural-water validation, normalized treatment cost, process energy inventory, GO yield or complete cost/LCA/TEA is available from the article.

## Semester-paper decision
Retain SEM-001 as an early GO–TC historical/model comparator and source for GO–TC interaction and release discussion. The condition-labelled evidence row should:
1. Keep kinetic and isotherm protocols separate.
2. Keep kinetic q2, Langmuir q_m and D–R q_m separate and explicitly fitted/model-derived.
3. Preserve kinetic temperatures 298/308/318 K, isotherm temperatures 298/303/308 K and thermodynamic temperatures 298/303/308/310/313 K as separate sets.
4. Preserve the Results/Table 2 temperature-count inconsistency and the k2 unit discrepancy.
5. Preserve GO stock concentration separately from final mixed-system dose; do not infer a direct measured q_e.
6. Treat up to 99.8% TC release as release, not multi-cycle reuse.
7. Avoid describing the paper as a validated wastewater treatment or low-cost demonstration.

## Citation workflow
The uploaded bibtex candidate-key crosswalk was searched for the DOI and title; no matching entry was found. Do not invent a Better BibTeX key. Add the DOI in Zotero only if selected for manuscript inclusion, then export and verify the actual key before inserting a citation into the manuscript.

## Repository updates
Updated in place:
- data/semester-remaining-work-register.csv
- data/semester-paper-candidate-register.csv
- data/semester-evidence-readiness-audit.csv (existing EV-SEM-001)
- data/semester-condition-labelled-comparison.csv (existing EV-SEM-001)
- data/source-caveats.csv
- data/semester-manuscript-claim-evidence-audit.csv (CLM-24)
- README.md

The manuscript's current 15-study comparison table was not expanded because SEM-001 has no verified Zotero citation key and is not yet among the 15 cited records. The condition-labelled evidence register retains its row with explicit caveats. No duplicate evidence ID was created.
