# SEM-046 primary-source, model-fit and mass-balance audit (2026-10-31)

## Source identity and access

Candidate: Tekle Tegie, T.; Admassu Workie, Y.; Leul Mekonnen, M.; Ayele Tessema, D. (2026), “Optimization of ciprofloxacin adsorption onto zirconium-modified magnetic graphene oxide: Response surface methodology,” *Bulletin of the Chemical Society of Ethiopia*, 40(5), 1147–1171. DOI: 10.4314/bcse.v40i5.15.

- Official AJOL article record: https://www.ajol.info/index.php/bcse/article/view/318556
- Official AJOL-hosted PDF: https://www.ajol.info/index.php/bcse/article/view/318556/299750
- AJOL record identifies Vol. 40 No. 5 (2026), pages 1147–1171, publication date 6 March 2026.
- The extracted PDF text contains a running footer “Bull. Chem. Soc. Ethiop. 2026, 40(6)” on article pages. This conflicts with the canonical AJOL issue record and DOI path (v40i5). Preserve the discrepancy; use the AJOL bibliographic record (40(5)) unless the publisher issues a correction. The extracted PDF layout was not visually inspected.

## 1. Study design and optimized synthetic-water conditions

The paper describes a 30-run, four-factor central-composite RSM design. The stated factor ranges are adsorbent dose 0.1–0.5 g/100 mL, CIP concentration 10–50 mg/L, contact time 15–75 min and pH 5–9. The optimized point is reported as:

- C0 = 30 mg/L CIP
- V = 100 mL
- adsorbent mass = 0.3 g (0.3 g/100 mL)
- pH = 7
- contact time = 45 min
- shaking = 180 rpm
- room/ambient temperature

The paper reports 93.92% removal at this point.

## 2. Figure 5 measured-qe / removal mass-balance conflict

Figure 5 reports the following equilibrium uptake and removal pairs:

| Material | Reported qe (mg/g) | Reported removal (%) |
|---|---:|---:|
| GO | 13.44 | 85.75 |
| Fe3O4-GO | 16.95 | 90.05 |
| ZrO2-Fe3O4/GO | 20.11 | 93.92 |

At the stated optimized feed condition, the initial CIP mass is 30 mg/L × 0.100 L = 3.0 mg. With 0.3 g adsorbent, the absolute feed-mass ceiling is 3.0 mg / 0.3 g = 10.0 mg/g, even if every CIP molecule is removed.

The removal percentages imply the following calculated qe values:

- GO: 3.0 mg × 0.8575 / 0.3 g = 8.575 mg/g
- Fe3O4-GO: 3.0 mg × 0.9005 / 0.3 g = 9.005 mg/g
- ZrO2-Fe3O4/GO: 3.0 mg × 0.9392 / 0.3 g = 9.392 mg/g

All three Figure 5 qe values exceed the 10.0 mg/g absolute ceiling if they are associated with the stated 30 mg/L, 100 mL, 0.3 g condition. They also disagree with the qe values implied by the corresponding removal percentages. Preserve the source-reported values as printed, label the calculated values as mass-balance diagnostics, and quarantine all three Figure 5 qe values from comparative uptake ranking pending clarification. Do not silently “correct” the paper.

## 3. Isotherm model and fitted capacity

The article reports:

- Langmuir qm = 313.48 mg/g, KL = 1.2 L/mg, R2 = 0.9807.
- Freundlich 1/n = 0.59 and R2 = 0.9997.
- The authors state that adsorption is better aligned with the Freundlich model.

Therefore 313.48 mg/g is a Langmuir-fitted model parameter from the poorer-fitting of the two reported models, not observed qe and not the model the authors identify as best fitting. One discussion passage prints 313.8 mg/g rather than 313.48 mg/g; preserve this small internal numerical discrepancy.

The Figure 7 caption does not state its experimental dose/concentration conditions. The Methods gives the broad RSM ranges and the calibration standards, but the exact Figure 7 condition linkage is not fully specified in the caption. Do not claim a precise isotherm-specific mass-balance ceiling without that linkage. As a diagnostic only, even the most generous combination of the stated 100 mL batch basis, lowest dose (0.1 g/100 mL) and highest calibration concentration (60 mg/L) would allow at most 60 mg/g feed loading, still far below the fitted 313.48 mg/g; this is conditional on those general ranges applying to the isotherm run.

## 4. Pharmaceutical-effluent result

The study sampled the Cadila Pharmaceutical Industry effluent stream in January 2025, approximately 200 m downstream of the discharge point. Four discrete samples were collected at 3-hour intervals over 12 hours and combined into a composite sample.

The article reports CIP concentration changing from 8.37 mg/L to 2.01 mg/L, while also reporting 90.75% removal. The concentration pair gives:

(8.37 - 2.01) / 8.37 × 100 = 75.99%, approximately 76.0%.

The paper does not explain how 90.75% was calculated from those two concentrations. Retain the concentration pair and the authors’ 90.75% claim as conflicting source statements. For any calculation from the stated pair, report 76.0% and explicitly label it as recalculated.

## 5. Reuse and regeneration

The paper reports two different regeneration approaches:

- Water-only washing: removal declines from 93.45% to 58.42% over five consecutive cycles.
- Sequential washing: 30 mL each of distilled water, acetone and methanol; three rinses with each solvent, shaking 30 minutes under the optimum conditions, magnetic separation and drying at 60 °C. The abstract reports 85.45% after eight cycles, while the Results text reports 85.7%. Preserve the abstract/body difference.

Solvent volumes, recovery/recycling and solvent-loss accounting are not developed into a process-cost inventory.

## 6. Mechanism evidence

The reported points of zero charge are GO 5.1, Fe3O4/GO 6.2 and ZrO2-Fe3O4/GO 6.5. The paper discusses CIP pKa values around 6.1 and 8.7; at pH 7 CIP is near its zwitterionic region while the composite is above its pHpzc. The authors propose electrostatic interactions, π–π association, hydrogen bonding and metal complexation.

The inspected characterization includes pre-adsorption FTIR/XRD and pHpzc/pH-response data. It does not isolate the contributions of individual forces or establish a unique dominant mechanism. A pseudo-second-order fit is not proof of chemisorption.

**Mechanism grade: M1 — plausible multi-pathway interpretation; evidence supportive but non-exclusive.**

## 7. Cost and citation boundary

No monetized manufacturing or treatment cost, product yield, energy inventory, reagent recovery or normalized cost-per-volume inventory is reported. The synthesis uses modified-Hummers GO chemistry, iron and zirconium precursors, heating, stirring, sonication and washing; sequential acetone/methanol regeneration adds solvent burden.

The DOI was not found in the latest uploaded 173-entry My Library Better BibTeX export. No citation key was guessed, no curated bibliography entry was created, and no manuscript citation was inserted. Reconcile the DOI in Zotero and use only the actual generated Better BibTeX key if the study is selected for citation.

Journal quartiles were not consulted or used; they are out of scope for the semester paper.

## Repository propagation

Updated existing records without creating a duplicate evidence ID:

- `data/semester-remaining-work-register.csv`
- `data/semester-paper-candidate-register.csv`
- `data/semester-evidence-readiness-audit.csv`
- `data/semester-condition-labelled-comparison.csv`
- `data/semester-mechanism-evidence-matrix.csv`
- `README.md`

Existing evidence ID remains EV-SEM-042. The audit is source-QA complete; verified Zotero key reconciliation and final manuscript selection remain open.
