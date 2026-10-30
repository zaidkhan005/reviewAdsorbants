# P0 quantitative consistency checks — 2026-10-31

## Scope

This is a calculation-only audit using the experimental conditions and values already transcribed from the original uploaded-paper extraction notes and `data/corpus-evidence.csv`. It does not silently correct any source value. The purpose is to quantify the size of the discrepancy and specify what source detail would resolve it.

For batch adsorption, the basic upper bound is:

```
q_max, mass-balance = C0 × V / m
```

where C0 is in mg/L, V in L and adsorbent mass m in g, giving mg/g. This bound assumes the full initial analyte mass is available to adsorb and is therefore an upper bound, not an observed uptake.

## P0 checks

### GAP-001 — Kar et al. (2025), DISC-024, DOI 10.1016/j.hazadv.2025.100666

Source-transcribed values: ΔH° = −0.735 kJ/mol; ΔS° = −0.107 kJ/(mol K); first listed temperature = 288 K; paper states ΔG° = ΔH° − TΔS°.

Independent arithmetic:
- TΔS° = 288 × (−0.107) = −30.816 kJ/mol.
- ΔG° = −0.735 − (−30.816) = **+30.081 kJ/mol**.
- This is not the printed approximately −3825 kJ/mol.

At 313 K the same printed ΔH° and ΔS° imply:
- ΔG° = −0.735 − 313 × (−0.107) = **+32.756 kJ/mol**.

The mismatch is not rounding. The printed ΔG° sequence cannot be used as valid thermodynamic evidence unless the authors' units, logarithm convention, equilibrium constant and/or table calculation are corrected. The sign implied by the printed ΔH°/ΔS° pair is positive throughout the listed temperature interval.

Dose inconsistency remains separate: abstract 0.2–1 g/L; Methods 0.45–1.5 g/L; Results/optimum 2 g/L. The reported 96.5% removal can only be quoted with the stated optimum (pH 6, C0 10 mg/L, 2 g/L, 24 h, 25 °C) and an explicit protocol discrepancy.

**Disposition:** thermodynamic spontaneity claim quarantined; author-reported removal may be used conditionally; cost claim remains a separate incomplete-boundary issue.

### GAP-002 — Jiao et al. (2024), DISC-010, DOI 10.1016/j.biortech.2024.130394

The individual-selectivity condition transcribed in EV-B02-005 is C0 = 4 mg/L and adsorbent dose = 0.5 g/L. For 1 L:
- Initial OTC mass = 4 mg.
- Adsorbent mass = 0.5 g.
- Maximum possible uptake = 4/0.5 = **8 mg/g**.

Reported individual OTC uptake = **11.97 mg/g**, which is 1.496 times the simple mass-balance ceiling (49.6% above it).

The mixture result (6.10 mg/g) is a different condition and should not be substituted for the individual result. Need confirm whether C0, liquid volume, dose, recovered dry sorbent mass or normalization basis differs from the described conditions.

**Disposition:** 11.97 mg/g not accepted as verified observed uptake; retain as author-reported with explicit mass-balance flag. No replacement value inferred.

### GAP-003 — Adu-Poku et al. (2024), DISC-026, DOI 10.1155/2024/3648098

The original PDF has conflicting concentration descriptions: the abstract and Methods state 0.5–2.5 mg/L for the initial-concentration study, while Results/Fig. 10 show 20–70 mg/L. Figure 10 uses 25 mg biochar and C0=20–70 mg/L; Figure 11 uses C0=50 mg/L and doses 2–20 mg. Figure 12 reports kinetic qe(exp)=245.9 ± 1.4 mg/g and PSO qe(cal)=243.902 mg/g, but its caption does not state C0, solution volume or adsorbent mass.

The 100 mg/g ceiling from 25 mg/50 mL/50 mg/L applies to the separately described typical/pH condition only; it cannot be assigned automatically to Figure 12's kinetic run. For example, 10 mg adsorbent in 50 mL at 50 mg/L gives a 250 mg/g upper bound, so 245.9 mg/g is not proven impossible. This candidate remains open due to conflicting concentration ranges and missing kinetic conditions, not a confirmed mass-balance violation.

**Disposition:** 245.9 mg/g quarantined as unresolved. The 100 mg/g ceiling applies only if the cited 25 mg/50 mL/50 mg/L condition is the same experiment that generated the kinetic qe.

### GAP-004 — Mohammed-Ridha & Abdul-Ahad (2014), CORP-019, DOI 10.31026/j.eng.2014.12.06

The isotherm condition is C0 max = 150 mg/L, V = 100 mL and barley-husk mass = 0.5 g, giving a maximum observed loading of **30 mg/g** at the top of the tested feed range. The reported barley-husk Langmuir q_m = **125.735 mg/g** is a fitted asymptote, not observed uptake; it is more than four times the largest loading available in the stated experiment and is weakly constrained.

The separate kinetic setup in Section 4.3 states 1 L at 150 mg/L, target Ce/C0 = 0.05 and 30.722 g barley husk. Maximum removed mass is 142.5 mg, so the ceiling is **4.64 mg/g**. Table 3 reports fitted barley-husk qe values of 23.81 mg/g (PFO) and 6.87 mg/g (PSO), respectively about 5.13× and 1.48× this ceiling. These are model-fitted parameters and cannot be used as validated measured capacities without clarification.

The PDF's internal imprint is December 2014. The filename's 2023 label is not the publication year.

**Disposition:** 125.735 mg/g and kinetic fitted values excluded from performance ranking; low observed removal/uptake data may be cited only with the high-feed and tablet-excipient caveats.

### GAP-005 — García-Criado et al. (2025), DISC-018, DOI 10.3390/antibiotics14040395

The original PDF distinguishes several experiments: kinetic Table 1 values (qe exp ≈0.983–1.575 mg/g), a separate isotherm series reported over 1–100 mg/L and plotted in Figure 6 (observed points roughly reach 30–40 mg/g), and fitted Langmuir q_max values in Table 2. Table 2 lists values from 86.1 to 1000 mg/g, whereas the narrative claims the Langmuir q_max for tetracyclines extends to over 200,000 mg/g. The narrative extreme is not supported by Table 2. The authors also state Freundlich fits are better (R² 0.817–0.968) than Langmuir fits (R² 0.755–0.908).

Do not compare the kinetic qe values directly with the separate isotherm capacities. The Table 2 q_max values are fitted asymptotes and should not be presented as measured uptake; the >200,000 mg/g narrative claim should be excluded. The exact isotherm dose/volume basis and the cause of the prose/table discrepancy remain to be clarified.

**Disposition:** extreme narrative qmax and Table 2 fitted values excluded from ranking. Use coherent observed uptake only with source-specific conditions and degradation caveat.

### GAP-006 — Zhang & Wu (2022), CORP-031, DOI 10.1002/jeq2.20415

The methods describe 80 mL antibiotic feed plus 20 mL N-rGO dispersion at 0.5 mg/L, corresponding to 0.01 mg N-rGO. For nominal C0 = 10 μg/L:
- If C0 refers to the original 80 mL feed: analyte mass = 0.8 μg; upper-bound uptake = 0.8 μg / 0.01 mg = **80 mg/g**.
- If C0 refers to the final 100 mL mixture: analyte mass = 1.0 μg; upper-bound uptake = **100 mg/g**.

The reported experimental qe range 80.58–90.21 mg/g is therefore compatible with the final-mixture interpretation but may exceed the original-feed interpretation for some analytes. The available method wording does not resolve which concentration basis is used. Langmuir q_m values (about 562–1266 mg/g) are fitted extrapolations and must not be presented as measured qe.

**Disposition:** not labelled a proven mass-balance violation. Retain experimental qe as source-reported with concentration-basis caveat; exclude very large fitted q_m from cross-paper capacity ranking pending clarification.

## Overall result

- One clear arithmetic contradiction: Kar et al. thermodynamics.
- Two direct condition-specific uptake/kinetic mass-balance flags: Jiao and Adu-Poku, subject to confirmation of the exact test conditions.
- Two high fitted-capacity extrapolation concerns: Mohammed-Ridha and García-Criado; fitted asymptotes are not equivalent to observed uptake, but are weakly constrained by the stated loading range.
- One ambiguous concentration/volume basis for N-rGO: not a proven violation; both plausible bases have been calculated.
- No source value has been silently replaced or normalized.


## Primary-PDF visual verification — Kar and Jiao

Both original main PDFs were located in the Library, materialized and rendered for visual inspection of the relevant pages. Text extraction was used as a locator; the rendered original tables/figure captions were used to confirm the printed conditions and values.

### Kar et al. (2025): discrepancy confirmed

- Table 4 on PDF p. 11 visibly prints ΔG° = −3825, −3879, −3916, −3970, −4032 and −4089 under a kJ/mol heading; ΔH° = −0.735; ΔS° = −0.107; R² = 0.992.
- The Methods on PDF pp. 4–5 define ΔG° = −RT ln KC and ΔG° = ΔH° − TΔS°, and state ΔH° in kJ/mol and ΔS° in kJ/(mol K).
- Recalculation under those explicit units gives +30.081 kJ/mol at 288 K and +32.756 kJ/mol at 313 K. This conflicts with both the sign and magnitude in the table. Merely interpreting the six ΔG values as J/mol would not reconcile them with the stated ΔH°/ΔS° pair.
- PDF p. 11 also includes Fig. 9(a), whose plotted ΔG axis itself is around −3800 to −4100 and labelled kJ/mol. This corroborates that the problem is present in the paper's displayed thermodynamic output, not introduced by a CSV transcription.
- Dose range mismatch is also present in the main PDF: abstract/Methods/Results report differing ranges and the optimum at 2 g/L. The main Methods state 0.45–1.5 g/L, while the optimized results use 2 g/L.
- The synthesis method on PDF p. 4 says 33.372 g carbonized shell is activated in 50 mL of 85% (w/v) H3PO4 solution at 35 °C for 24 h. The cost table on PDF p. 12 reports 1.5 kg H3PO4 in a per-kilogram estimate without a transparent yield/scale bridge. Retain the author's INR 239.22/kg as a preliminary estimate, not a validated process cost.

**Verdict:** the reported thermodynamic set is not usable; no corrected values are inferred. The reported 96.5% removal optimum can be cited only as author-reported with the dose-range discrepancy attached.

### Jiao et al. (2024): two separate uptake discrepancies confirmed

- Methods on PDF p. 3 define qe = (C0 − Ce)V/w and state the adsorbent dosage for the specificity assessment is 0.5 g/L.
- Figure 4a caption on PDF p. 5 specifies 4 mg/L antibiotics and 0.5 g/L adsorbent. The selectivity text reports OTC uptake 11.97 mg/g. Under those printed conditions the absolute mass-balance ceiling is 4/0.5 = **8 mg/g**.
- Figure 3a caption on PDF p. 4 specifies 2 mg/L OTC and 0.5 g/L adsorbent. The text refers to experimental uptake about 12.07 mg/g; Table 1 reports fitted qe values 10.84 mg/g (PFO) and 12.55 mg/g (PSO). The corresponding loading ceiling is 2/0.5 = **4 mg/g**.
- The prose directly adjacent to Table 1 alternates between mg/g and mg/L for the 12.07/12.55 quantities, whereas Table 1 and graph axes label qe in mg/g. This is a source unit inconsistency, but the repeated values cannot be accepted as verified uptake under the figure-caption conditions.
- Table 2's 67.89 mg/g Langmuir parameter is from a different isotherm series (1–200 mg/L); it is a fitted isotherm parameter and should not be conflated with the selectivity or kinetic uptake under the low-concentration conditions.

**Verdict:** both the 11.97 mg/g selectivity uptake and the ≈12.07/12.55 mg/g kinetic results are excluded from verified quantitative rankings pending clarification of concentration, dosage, total volume or normalization. The 67.89 mg/g Langmuir fit remains a separately labelled fitted parameter, not an observed low-feed uptake.

### Files/pages inspected

- Kar original PDF `1-s2.0-S2772416625000786-main.pdf`: PDF pp. 4–5, 10–12; especially Eqs. 3–5, Table 4, Fig. 9, Table 5.
- Jiao original PDF `1-s2.0-S096085242400097X-main.pdf`: PDF pp. 3–5; especially qe equation, Fig. 3/Table 1, Fig. 4a and selectivity text.


## Additional primary-PDF verification — four remaining P0 cases

### Adu-Poku et al. (2024), DOI 10.1155/2024/3648098

The full PDF confirms:
- Abstract and Methods state an initial-concentration range of 0.5–2.5 mg/L.
- Results/Figure 10 instead plot 20–70 mg/L with 25 mg biochar; Figure 11 uses C0=50 mg/L and dosage 2–20 mg.
- Figure 12/Table 1 report qe(exp)=245.9 ± 1.4 mg/g and PSO qe(cal)=243.902 mg/g, but Figure 12 does not state C0, V or sorbent mass.
- The earlier 100 mg/g calculation assumed the typical 25 mg/50 mL/50 mg/L experiment applied to Figure 12, which is not established. A 10 mg dose in 50 mL at 50 mg/L allows up to 250 mg/g, so the reported value is **not proven impossible**.

**Corrected verdict:** do not label 245.9 mg/g a mass-balance violation. Retain it as author-reported, with an incomplete kinetic-condition caveat. The concentration-window inconsistency is confirmed.

### Mohammed-Ridha & Abdul-Ahad (2014), DOI 10.31026/j.eng.2014.12.06

The full PDF confirms the kinetic design in Section 4.3: 1 L of 150 mg/L LEVX, target Ce/C0=0.05, barley-husk dose 30.722 g. Maximum mass removed = 150 mg × 0.95 = 142.5 mg; ceiling = 142.5/30.722 = **4.64 mg/g**. Table 3 on PDF p. 12 (printed p. 99) reports barley-husk fitted qe=23.81 mg/g (PFO) and 6.87 mg/g (PSO). Both exceed the ceiling, by about 5.13× and 1.48× respectively.

The separate isotherm experiments use 100 mL and 0.5 g at feed concentrations up to 150 mg/L, giving 30 mg/g maximum tested loading. The 125.735 mg/g Langmuir q_m is a fitted asymptote, not observed uptake and not adequately demonstrated by the accessible isotherm loading.

The issue is not the publication year: the original issue header shows December 2014, Volume 20, Number 12. The upload filename's 2023 is incorrect.

**Verdict:** quarantine kinetic fitted qe values pending explanation of the mismatch; do not use 125.735 mg/g as a measured capacity; use 2014 bibliographic year.

### García-Criado et al. (2025), DOI 10.3390/antibiotics14040395

Visual inspection confirms:
- Table 1 on PDF p. 8 presents the kinetic qe values, approximately 0.983–1.575 mg/g.
- Figure 6 is a separate isotherm dataset over 1–100 mg/L, with measured points reaching roughly 30–40 mg/g.
- Table 2 on PDF p. 9 lists Langmuir q_max values 86.1–1000 mg/g.
- The adjacent narrative says q_max ranges to over 200,000 mg/g. That extreme is not supported by Table 2.
- The paper states Freundlich fits are better overall (R² 0.817–0.968) than Langmuir (R² 0.755–0.908).

**Corrected verdict:** the narrative extreme is a source discrepancy; do not use it. Do not compare kinetic qe to isotherm q_max. Keep fitted Langmuir values out of capacity rankings unless model and loading basis are independently resolved.

### Zhang & Wu (2022), DOI 10.1002/jeq2.20415

Visual inspection confirms:
- Methods §2.3 on PDF p. 3: 80 mL antibiotic solution plus 20 mL N-rGO dispersion at 0.5 mg/L; hence 0.01 mg sorbent.
- Figure 2a/Table 1 on PDF p. 5: C0=10 μg/L; qe(exp)=80.58–90.21 mg/g.
- The stated pre-mix 80 mL feed gives an 80 mg/g upper bound; if the concentration is defined in the final 100 mL volume, the upper bound is 100 mg/g. The paper does not clarify this. Thus some values exceed one interpretation but all are within the other.
- Table 2 on PDF p. 6 lists fitted Langmuir q_m values 561.80–1265.82 mg/g. These are fitted parameters, not measured qe.

**Corrected verdict:** no proven mass-balance violation. Keep the experimental values with the concentration/volume-basis caveat; exclude fitted q_m from capacity rankings pending fit/basis verification.

