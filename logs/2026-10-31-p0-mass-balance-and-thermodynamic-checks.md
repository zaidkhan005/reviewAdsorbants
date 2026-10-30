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

## Overall result — revised after full-PDF inspection

- **Kar:** one confirmed thermodynamic arithmetic/unit contradiction; no corrected parameters inferred.
- **Jiao:** two condition-specific capacity inconsistencies confirmed against the printed figure captions and the article's own qe equation (11.97 mg/g versus 8 mg/g ceiling; kinetic values around 12 mg/g versus 4 mg/g ceiling).
- **Mohammed-Ridha:** a separate kinetic-model mass-balance discrepancy confirmed from Section 4.3 and Table 3 (barley-husk fitted qe 23.81 and 6.87 mg/g versus 4.64 mg/g ceiling).
- **Adu-Poku:** concentration-window conflict confirmed, but the initial 245.9 mg/g kinetic result is **not proven** to violate mass balance because Figure 12 omits its exact dose and a 10 mg dose under 50 mg/L × 50 mL would permit 250 mg/g.
- **García-Criado:** the narrative >200,000 mg/g Langmuir claim conflicts with Table 2 (86.1–1000 mg/g); kinetic qe, isotherm points and fitted q_max are separate datasets/metrics.
- **Zhang & Wu (N-rGO):** concentration/volume basis ambiguity remains; not a proven mass-balance violation.
- No source value has been silently replaced or normalized. Earlier conditional assumptions are explicitly superseded by the source-verified findings below.


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



## Correction to the initial P0 triage

After visually inspecting the original PDFs, the Adu-Poku mass-balance allegation was withdrawn: the Figure 12 kinetic dose is not stated, and a plausible 10 mg / 50 mL / 50 mg/L condition permits 250 mg/g. The 245.9 mg/g result remains condition-incomplete, not proven impossible. The N-rGO concentration basis also remains ambiguous rather than a proven violation and has been downgraded from P0 to P1.

The current priority distribution is **5 P0, 9 P1 and 5 P2**. The P0 list now comprises Kar thermodynamics, Jiao OTC uptake, Adu-Poku concentration/kinetic-condition conflict, Mohammed-Ridha kinetic mass-balance discrepancy, and García-Criado narrative/table capacity mismatch. The detailed register is authoritative.


## P0 source-verification completion — Kar et al. (2025), DISC-024 (2026-10-31 continuation)

The original uploaded PDF was re-opened from the Library attachment `1-s2.0-S2772416625000786-main.pdf`. Text extraction was used only to locate the passages; the original rendered PDF pages were inspected for the displayed equations, dose panels, thermodynamic plot and Table 4.

### Thermodynamic equations and table
- Methods PDF p. 5 define ΔG° = −RT ln K_C and define K_C = C_a/C_e. The same page explicitly gives ΔG° = ΔH° − TΔS°, with ΔH° in kJ/mol and ΔS° in kJ/(mol K); PDF p. 6 repeats the latter equation.
- Table 4, PDF p. 11, prints ΔG° values −3825, −3879, −3916, −3970, −4032 and −4089 under a **kJ/mol** header for 288, 293, 298, 303, 308 and 313 K. It reports ΔH° = −0.735 and ΔS° = −0.107 with R² = 0.992. Fig. 9(a), same PDF page, displays a ΔG axis around −3800 to −4100 and is therefore consistent with the table's plotted magnitude, not with a kJ-to-J unit correction.
- Recalculation from the table's own ΔH°/ΔS° values gives ΔG° = +30.081 kJ/mol at 288 K and +32.756 kJ/mol at 313 K. These are opposite in sign and more than two orders of magnitude different from the printed table values. Interpreting the tabulated ΔG numbers as J/mol does not reconcile the set with the stated ΔH°/ΔS° pair.
- The Methods also define K_C = (C_i-C_e)/C_e, with concentrations in mg/L. This is a dimensionless ratio as written, but the paper does not demonstrate a standard-state conversion or explain the thermodynamic convention. The main-paper evidence therefore does not allow a defensible reconstruction of standard thermodynamic quantities from the concentration ratio. Do not infer a corrected ΔG° from the graph or the tabulated regression.
- Fig. 9(a) plots ln K_C against 1/T and reports the fitted line visually; however, the article does not provide the six underlying K_C observations or a calculation worksheet in the main PDF. The displayed regression and Table 4 do not provide a reproducible independent route to recover valid thermodynamic parameters.

### Protocol and other interpretation checks
- Abstract PDF p. 1 states dose range 0.2–1 g/L. Methods PDF p. 5 state 0.45–1.5 g/L. Results PDF p. 8 and p. 9 discuss a dose sweep from 0.2 to 1.1 g/L and say maximum removal occurs at 2 g/L. The pH, time and temperature panels use 2 g/L in their inset conditions. This conflict is confirmed, not resolved.
- The article's 96.5% ENF removal is author-reported at pH 6, C0 = 10 mg/L, 2 g/L dose, 24 h and 25 °C (PDF pp. 8–9 and conclusion). Keep it as a condition-labelled result with the dose protocol inconsistency.
- The methods say the 30 mL solution portion was put into a 100 mL flask, but do not explicitly reconcile every figure's stated dose with a weighed sorbent mass. This does not justify inventing a corrected dose.
- Thermodynamic spontaneity and exothermicity claims are quarantined. The negative ΔH°/ΔS° values cannot be combined with the Table 4 ΔG° sequence; do not carry these claims forward. A PSO fit (R² ≈ 0.999) and reported E_a = 61.1 kJ/mol do not independently establish chemisorption or fix the thermodynamic inconsistency.

### Disposition
GAP-001 is **resolved for manuscript use** as an unusable/quarantined thermodynamic parameter set, not as a corrected numeric result. The original source discrepancy remains documented; no table value has been silently altered. EV-B08-004 retains the source-reported values only in its audit description and explicitly excludes them from manuscript thermodynamic conclusions. The remaining condition-labelled removal result can be used with the dose discrepancy attached.

Source pinpoints: original PDF pp. 1, 5–6, 8–11; Methods Eqs. (2)–(5); Fig. 6 dose/pH/time/temperature insets; Fig. 9(a); Table 4.


## P0 source-verification completion — Jiao et al. (2024), DISC-010 (2026-10-31 continuation)

The original uploaded Bioresource Technology PDF `1-s2.0-S096085242400097X-main.pdf` was retrieved from the Library and its rendered PDF pages 3–5 were visually inspected. Text extraction was used to locate passages; the figure captions, table and equation were checked against the rendered source.

### Experimental equation and low-feed kinetic discrepancy
- Methods §2.3, PDF p. 3, define `q_e = (C_0 - C_e) × V / w`, with C0 and Ce in mg/L, V in L and sorbent mass w in g. The same page describes the static adsorption experiment and states the OTC kinetic conditions in Fig. 3a caption.
- Fig. 3a caption, PDF p. 4, specifies adsorbent = 0.5 g/L, OTC = 2 mg/L, 25 °C and pH 6.50 ± 0.1. The mass-balance ceiling is therefore `2 mg/L ÷ 0.5 g/L = 4 mg/g` (equivalently C0×V/w for any common test volume).
- The adjacent Results text reports experimental OTC uptake around 12.07 mg/g; Table 1 gives MBC@MIPs fitted qe = 10.84 mg/g (pseudo-first-order) and 12.55 mg/g (pseudo-second-order). The same paragraph alternates units, labelling the experimental 12.07 once as mg/g and once as mg/L, and the fitted 12.55 once as mg/L although Table 1 labels capacity in mg/g. The article's own qe equation and figure-axis/table units do not reconcile these values with the caption's 4 mg/g ceiling. These low-feed kinetic capacities are therefore not accepted as verified uptake.
- The separate isotherm experiment spans 1–200 mg/L. Table 2 reports MBC@MIPs Langmuir parameter 67.89 mg/g (R²=0.9821), and the body states an experimental value 60.19 mg/g at a separate concentration condition. These are a different experimental series and a fitted asymptote/condition-specific isotherm observation—not a corrected value for the low-feed Fig. 3 kinetic run.

### Selectivity discrepancy
- Fig. 4a caption, PDF p. 5, specifies 4 mg/L antibiotic feed, 0.5 g/L adsorbent and 25 °C. The maximum loading is 4/0.5 = **8 mg/g**.
- The selectivity Results §3.4 reports 11.97 mg/g OTC uptake. This exceeds the 8 mg/g ceiling by 49.6%. The adjacent mixture experiment reports 6.10 mg/g OTC with competing antibiotics; that is a separate condition and is not a correction for the individual-selectivity test.
- No alternate volume, actual weighed mass, feed concentration basis, or normalization correction is stated in the main PDF. Do not infer one.

### Disposition
GAP-002 is **resolved for manuscript use** as a confirmed quantitative inconsistency with low-feed kinetic and selectivity qe values quarantined; no corrected capacity is inferred. Preserve the Langmuir 67.89 mg/g only as a separate fitted isotherm parameter, not a measured uptake under the low-feed conditions. The article's Table 2 MBC comparator discrepancy (38.34 mg/g in Table 2 versus 38.84 mg/g in body/abstract) remains a separate unresolved source mismatch and is not silently harmonized.

Source pinpoints: PDF p. 3 Eq. (2), definitions and §2.3; PDF p. 4 Fig. 3a caption and Table 1; PDF p. 5 Fig. 4a caption, §3.4 and Table 2/mixture discussion.


## P0 source-verification completion — Adu-Poku et al. (2024), DISC-026 (2026-10-31 continuation)

The original uploaded Wiley PDF, `Journal of Chemistry - 2024 - Adu-Poku - Acid-Activated Biochar for Efficient Elimination of Amoxicillin From Wastewater.pdf` (DOI 10.1155/2024/3648098), was retrieved from the Library and visually checked at the abstract, Methods, Figures 10–12 and Tables 1–2 (PDF pp. 1, 3–4, 6–10).

### Confirmed concentration-window conflict
- Abstract PDF p. 1 states the initial amoxicillin concentration was 0.5–2.5 mg/L.
- Methods §2.5, PDF p. 3, repeats the initial concentration range 0.5–2.5 mg/L and states adsorbent doses of 2–20 mg. The same Methods section gives a separate typical batch example: 25 mg biochar in 50 mL of 50 mg/L amoxicillin, 6 h.
- Results §3.2.3 and the page-8 Figure 10 caption instead specify a 20–70 mg/L initial-concentration series; Fig. 10 specifies 25 mg biochar, pH 7, 25 °C and 6 h. The plotted uptake increases from roughly 37 mg/g at 20 mg/L to about 136 mg/g at 70 mg/L.
- Figure 11 (PDF p. 9) explicitly uses 50 mg/L amoxicillin, pH 7, 25 °C, 6 h and adsorbent doses 2–20 mg. The range conflict is therefore a source-internal reporting issue, not a transcription introduced by this project.

### Kinetic result: no proven mass-balance violation
- Figure 12 (PDF p. 9) gives PFO, PSO and Weber–Morris plots but its caption does not identify the kinetic experiment's C0, solution volume or biochar mass.
- The Results text (PDF p. 7) reports an experimental equilibrium uptake `qe = 245.9 ± 1.4 mg/g`. Table 1 (PDF p. 10) gives PSO fitted `qe = 243.902 mg/g` (R²=0.999), PFO fitted qe = 0.496 mg/g (R²=0.100), and the Weber–Morris model parameters. Table 2 separately reports Langmuir fitted `qmax = 239.230 mg/g` (R²=0.995) from the isotherm analysis.
- The previous 100 mg/g upper bound is valid only for the separate stated 25 mg / 50 mL / 50 mg/L example. The source does not say that this exact dose-volume-feed combination generated Figure 12. A hypothetical 10 mg adsorbent / 50 mL / 50 mg/L condition would permit up to 250 mg/g. Therefore the 245.9 mg/g kinetic result is **not proven** to violate mass balance.
- Do not substitute the PFO fit, PSO fit, or Langmuir qmax for the reported experimental qe. They are distinct model outputs; their numerical proximity does not validate the missing kinetic condition.

### Manuscript disposition
GAP-003 is resolved for manuscript use as a confirmed concentration-window conflict plus missing kinetic-condition disclosure. Retain 245.9 ± 1.4 mg/g only as an author-reported, condition-incomplete kinetic result; exclude it from condition-matched quantitative rankings. Do **not** allege a mass-balance violation, and do not silently normalize the abstract/Methods concentration range to the Results range. The original discrepancy remains visible.

Source pinpoints: Abstract PDF p. 1; Methods §§2.2–2.5 PDF pp. 3–4; Results §3.2.3 and Fig. 10 PDF p. 8; Fig. 11 and Fig. 12 PDF p. 9; kinetic/isotherm Tables 1–2 PDF p. 10.


## P0 source-verification completion — Mohammed-Ridha & Abdul-Ahad (2014), CORP-019

The original uploaded PDF `Mohammed-Ridha and Abdul-Ahad - 2023 - Adsorption of Levofloxacine Antibacterial from Contaminated Water by Non – Conventional Low Cost Nat.pdf` was retrieved from the Library and checked against the other duplicate copies mapped in the attachment crosswalk. The PDF was text-located and rendered; Table 2 and Table 3 were visually inspected.

### Publication year
- The article imprint on PDF p. 1 states *Journal of Engineering*, Number 12, Volume 20, December 2014. The same imprint appears on the subsequent pages. The 2023 string in the attachment filename/export title is not the article's publication year. Cite as Mohammed-Ridha & Abdul-Ahad (2014).

### Kinetic mass-balance check — barley husk
- Section 3.4, PDF p. 6 (printed p. 93), states a 2 L beaker filled with **1 L of 150 mg/L LEVX**; the sorbent is added after agitation starts. The dosage is calculated for target equilibrium concentration ratio `C_e/C_0 = 0.05`.
- Section 4.3, PDF p. 7 (printed p. 94), identifies the amounts for the 1 L, 150 mg/L kinetic setup: activated carbon 20.745 g, barley husk **30.722 g**, eggshell 720 g. Figure 7, PDF p. 15 (printed p. 102), independently labels barley-husk `C_absorbent = 30.722 g/L` and `C_0 = 150 mg/L`.
- For 1 L, initial LEVX mass is 150 mg. The target residual fraction is 0.05, so the maximum mass removed under the stated design is `150 × (1 − 0.05) = 142.5 mg`. Dividing by 30.722 g barley husk gives `142.5 / 30.722 = 4.64 mg/g`.
- Table 3, PDF p. 12 (printed p. 99; rendered image checked), reports barley-husk PFO `q_e = 23.81 mg/g` (R²=0.7022) and PSO calculated `q_e = 6.87 mg/g` (R²=0.9966). The former is about 5.13 times and the latter about 1.48 times the 4.64 mg/g ceiling. They are kinetic model parameters, not direct observed capacities, and cannot be reconciled with the stated dose/target mass balance as reported. No corrected value is inferred.
- Do not apply this kinetic ceiling to other sorbents or other tests; the finding here is specifically for the barley-husk 1 L kinetic setup.

### Separate isotherm fitted-capacity issue
- Section 3.3, PDF p. 5 (printed p. 92), states 100 mL tests with 25–150 mg/L initial LEVX and 0.5 g barley husks, pH 7 and 3 h. At the maximum 150 mg/L feed, the maximum loading available is `150 × 0.100 / 0.5 = 30 mg/g`.
- Table 2, PDF p. 11 (printed p. 98; visually checked), reports barley-husk Langmuir `q_m = 125.735 mg/g` (R²=0.988). This is a fitted asymptote well above the largest loading experimentally accessible under the specified feed/dose conditions; it is not a demonstrated observed uptake. Exclude from observed-capacity rankings.

### Disposition
GAP-004 is resolved for manuscript use: cite the paper as 2014; exclude the two barley-husk kinetic fitted qe values from quantitative ranking due to the stated mass-balance ceiling; and keep the 125.735 mg/g q_m only as a model-fitted extrapolation with the 30 mg/g isotherm loading ceiling explicitly stated. No source values have been overwritten and no corrected capacities have been invented.

Source pinpoints: Journal imprint PDF p. 1; kinetic setup §3.4 PDF p. 6; §4.3 PDF p. 7; Table 3 PDF p. 12; Figure 7 PDF p. 15; isotherm design §3.3 PDF p. 5; Table 2 PDF p. 11.

## P0 source-verification completion — García-Criado et al. (2025), DISC-018 (2026-10-31)

Original PDF `antibiotics-14-00395-v2.pdf` was retrieved from the Library. Text passages were located and original rendered pages p. 6, p. 8 and p. 9 inspected; abstract/methods/equation/conclusion were separately checked in extracted full-text. No SI file was part of the inspected Library bundle.

### 1) Kinetic experiment: unresolved concentration input, not a proven violation
- Abstract p. 1 reports 5 mg/L for the headline removal condition.
- General Methods §3.4 p. 18 state C0=2 mg/L, V=10 mL and ST=20 mg (2 g/L).
- Kinetic Methods §2.2.1 p. 6 literally prints antibiotic concentration `2 mg mL−1` with 0.02 g adsorbent/10 mL. Do not call this a typo without author confirmation.
- Eq. (2), §3.6 p. 19: `q_t=(C_0-C_e)V/m`, V=0.01 L and m=0.02 g. The maximum available q is 1 mg/g at 2 mg/L, 2.5 mg/g at 5 mg/L, and 1000 mg/g at 2 mg/mL. Table 1 p. 8 has experimental kinetic qe values 0.983–1.575 mg/g. If the actual kinetic C0 was 2 mg/L, some reported qe exceed the cap; if it was 5 mg/L, all fit within the cap; if 2 mg/mL, they are far below it. The source does not resolve which condition generated Table 1. The correct disposition is condition-incomplete; no mass-balance violation is established.

### 2) Isotherm experiment: fitted qmax is extrapolated
- Methods §3.4 p. 18 report isotherm C0=0.25–100 mg/L; Results §2.2.2 pp. 8–9 say 1–100 mg/L. Upper-end 100 mg/L with V=0.01 L and m=0.02 g gives max available experimental loading 50 mg/g.
- Figure 6 p. 8 (original rendered image checked) shows experimental points generally below about 40 mg/g.
- Table 2 p. 9 lists Langmuir qmax estimates 86.1–1000 mg/g. All exceed the 50 mg/g loading available at the maximum tested feed. These are fitted Langmuir asymptotes, not observed loading. The fit quality is also poorer: Langmuir R² 0.755–0.908, versus Freundlich 0.817–0.968. Exclude these qmax values from empirical capacity rankings; do not call them direct mass-balance violations.

### 3) Extreme prose error
- Results p. 9 states qmax >200,000 mg/g for tetracycline/TC; conclusion p. 20 says >200,000 mg/g for TGC.
- Table 2 p. 9 actually lists TC=1000 mg/g and TGC=86.1 mg/g. Neither the extreme magnitude nor stable analyte attribution is supported by the table. Do not correct by guessing; quarantine the prose claim.

### Disposition
GAP-005 is resolved for manuscript use with explicit source caveats: remove the >200,000 mg/g claim; do not use fitted Langmuir qmax values for comparative capacity ranking; keep Figure 6 observed data as a separate isotherm evidence class; retain Table 1 kinetic qe only as source-reported and condition-incomplete. Underlying article discrepancy remains visible; no replacement values invented.

Source pinpoints: PDF pp. 1, 6, 8–9, 18–20; Table 1, Fig. 6, Table 2, §§2.2.1, 2.2.2, 3.4, 3.6.
