# SEM-038 original-PDF mass-balance recheck — 31 October 2026

## Study identity and source
Zhang and Wu (2022), “Adsorption Characteristics of N-rGO for Multiple Representative Trace Antibiotics in Water,” *Journal of Environmental Quality* 51(6), 1298–1309. DOI: 10.1002/jeq2.20415.

Publisher DOI page: https://doi.org/10.1002/jeq2.20415
Original Library PDF inspected: `ato eng 2.pdf` (12 pages), with Methods §2.3, Figure 2, Table 1, Table 2, influencing-factor and regeneration sections re-read and rendered page screenshots checked on 31 October 2026.

The study is retained for N-rGO synthesis/characterization, trace-antibiotic context, simulated matrix effects and reuse. This audit is about whether its quantitative TC uptake can be used in the semester paper's comparisons.

## Critical correction: single-analyte vs competitive tests
The Methods say 80 mL of each antibiotic solution (SMZ, LVX, CLI, TC, PEN and CHL) was separately added to vials with 20 mL N-rGO dispersion. Figure 2a/Table 1 are therefore separate single-analyte tests, one antibiotic at a time. The six-analyte simultaneous/competitive test is a separate experiment shown in Figure 3f (§3.5.6). Earlier evidence wording that described the Table 1 TC value as part of a six-analyte mixture has been corrected in the candidate/evidence/comparison records and manuscript table. Do not conflate the two experiments.

## Methods and reported values
- §2.3 states: 80 mL antibiotic solution + 20 mL N-rGO dispersion at 0.5 mg/L; 120 rpm; 25 ± 1 °C.
- Separate series: antibiotic C0 = 0.1, 1, 10 and 20 µg/L; N-rGO dosage values = 40, 60, 80, 100, 200, 300 and 400 µg/L. pH 3–12 and temperature 288.15–318.15 K are separate factor tests.
- Figure 2a/Table 1 kinetic comparison uses C0 = 10 µg/L, 288.15 K. Table 1 reports TC experimental qe = 90.21 mg/g. First-order fitted qe = 93.13 mg/g (R² = .9579); second-order fitted qe = 92.84 mg/g (R² = .9291). The authors say first-order fits better. TC is reported to adsorb fastest, within 30 min; these are single-analyte TC results.
- Figure 2c is a separate dosage experiment at C0 = 1 µg/L and 288.15 K. Its x-axis is “Dosage of N-rGO (×10−1 mg/L)” with ticks 0.4–1.0, i.e. 40–100 µg/L. The plotted TC qe curve is about 88–90 mg/g.
- Table 2 gives TC Langmuir q_m = 662.25 mg/g, K_L = 0.142 L/mg, R² = .9989. The 1,265.82 mg/g maximum highlighted in the abstract/body is the clindamycin (CLI) Table 2 row, not tetracycline. Keep fitted q_m separate from measured qe; do not misattribute CLI to TC.

## Mass-balance calculations
### Figure 2a / Table 1
The Methods' physical preparation basis gives:
- TC feed mass: 80 mL × 10 µg/L = 0.8 µg TC.
- N-rGO mass: 20 mL × 0.5 mg/L = 0.01 mg N-rGO.
- Maximum feed-limited qe = 0.8 µg / 0.01 mg = 80 mg/g.

Table 1's TC experimental qe = 90.21 mg/g is approximately 12.8% above that ceiling. A previous alternative ceiling of 100 mg/g would require 10 µg/L to apply to the final 100 mL mixture after addition of the dispersion. That interpretation is not established by the paper, which describes 80 mL of antibiotic solution as the feed. Preserve the ambiguity, but use the strict 80 mL feed as the stated physical basis and seek author clarification rather than treating 100 mg/g as an equally documented interpretation.

### Figure 2c dosage experiment
At C0 = 1 µg/L, 80 mL feed contains only 0.08 µg TC. The N-rGO dosage axis spans 40–100 µg/L, while Figure 2c plots TC qe at approximately 88–90 mg/g. Depending on whether the dose concentration is converted using 80 mL feed or 100 mL total liquid, the available-feed qe ceiling across those dosage settings is only approximately 8–25 mg/g. This is several-fold below the plotted curve. The figure and Methods do not state a consistent volume/dose basis that resolves the discrepancy. The plotted TC qe therefore cannot be accepted into a quantitative capacity ranking.

## Matrix effects and competitive adsorption
- Coexisting-ion tests include Na+, K+, Ca2+, Mg2+, Cl−, HCO3−, CO3²− and NO3− at the stated 100 mmol/L test level. These are controlled simulated-ion tests, not actual natural-water validation.
- Humic-acid concentrations tested are 0.5–10 mg/L. At 10 mg/L, uptake of antibiotics decreases by up to 30%.
- Figure 3f/§3.5.6 is the separate simultaneous six-antibiotic competitive experiment. Individual capacities in the multi-component system are reported at roughly 70–80% of single-component levels; the aggregate mixed-system value must not be attributed to TC alone.

## Kinetics, isotherm and mechanism
- First-order kinetics fit better than second-order for TC (Table 1).
- Langmuir fits the isotherm data per the authors' reported Table 2 statistics, but q_m = 662.25 mg/g is a fitted parameter extrapolated from trace-level concentration conditions and not observed uptake. It is excluded from cross-study capacity ranking.
- The source discusses electrostatic interactions, π–π interactions and van der Waals forces. FTIR, XPS and Raman characterize the N-rGO surface; nitrogen bonding fractions are pyridinic 50.91%, pyrrolic 26.49% and graphitic 22.60%. These identify plausible interactions; they do not quantify the contribution of each mechanism.
- TC thermodynamic parameters in Table 3: ΔH = −13.6 kJ/mol; ΔS = 36.78 J/(mol K); ΔG = −24.19 kJ/mol at 288.15 K to −25.30 kJ/mol at 318.15 K. The paper interprets the process as exothermic and spontaneous over the examined temperatures.

## Regeneration
The Methods specify 0.1 M HCl elution, 0.1 M NaOH regeneration and deionized-water washing. Section 3.5.5 reports that adsorption capacity across antibiotics decreases by no more than 25% after eight cycles. Figure 3e displays cycling curves, but the text does not provide a separate exact numeric TC-only retention after cycle eight. Report this as a broad author-reported multi-antibiotic regeneration result, not a verified TET-specific capacity-retention value. No reagent recovery or waste-treatment balance is supplied.

## Processing/cost boundary
Synthesis burden is substantial: graphite pre-oxidation with concentrated nitric acid, K2S2O8 and P2O5; GO oxidation using concentrated H2SO4/H3PO4 and KMnO4; H2O2 quench; HCl wash; 100 W ultrasonic exfoliation; ammonia-assisted autoclaving at 180 °C for 24 h; centrifugation, repeated washing and drying at 60 °C. The method also specifies 30 min ultrasound for exfoliation and 1 h GO sonication before hydrothermal N-doping.
No product yield, reagent recovery, energy-per-mass inventory, normalized cost, treatment cost or full process LCA/TEA is provided in the audited source text.

## Decision for the semester paper
- Retain SEM-038 for material/synthesis context, trace-antibiotic adsorption discussion, simulated humic-acid/ion interference, competitive adsorption and broad eight-cycle regeneration discussion.
- Keep Table 1 TC qe = 90.21 mg/g as source-reported but HOLD from quantitative rankings because it exceeds the strict feed ceiling derived from stated Methods.
- Keep Figure 2c dosage-derived TC uptake out of rankings because its plotted 88–90 mg/g is far above available-feed mass.
- Keep Table 2 TC q_m = 662.25 mg/g as a fitted model parameter only. Do not attribute 1,265.82 mg/g to TC; it is the CLI value.
- Correct the evidence description: Figure 2a/Table 1 are separate single-analyte tests; Figure 3f is the separate six-analyte competition experiment.
- Ask the authors to clarify C0 before/after dilution, exact total volume, dose-concentration basis and Figure 2c qe calculation if quantitative TC capacity is required. Do not create new SEM evidence IDs; reuse EV-B10-004–EV-B10-009.

## Repository updates
Updated in place:
- data/semester-remaining-work-register.csv
- data/semester-paper-candidate-register.csv
- data/semester-evidence-readiness-audit.csv (existing cross-reference only)
- data/semester-condition-labelled-comparison.csv
- data/source-caveats.csv
- data/semester-manuscript-claim-evidence-audit.csv (CLM-07)
- manuscript/SEMESTER_TABLE_1_CORE_STUDY_COMPARISON_V1.md
- README.md

No duplicate evidence ID created; all six master evidence records EV-B10-004–EV-B10-009 remain the source of truth.
