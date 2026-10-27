# Quantitative-comparison readiness audit — 2026-10-27

## Purpose and scope

This audit checks whether the source-linked evidence can be turned into defensible comparisons across the processing–cost–performance continuum. It does **not** produce a global adsorption-capacity ranking. A candidate can be relevant to the review while its fitted capacity remains unusable for quantitative ranking.

## Structural cross-check

- `data/corpus-evidence.csv`: **310 unique evidence IDs**.
- `data/primary-study-comparison-matrix.csv`: **208 rows** containing **248 unique evidence IDs**; there are no duplicate or orphan evidence IDs in the matrix crosswalk.
- The **62 evidence IDs outside the primary-study matrix** map to review/background evidence (61 entries) and one adjacent technology record. They are not missing primary-study rows; they are intentionally outside the core adsorption-capacity matrix.
- The matrix represents 43 candidate IDs. Its columns are a working comparison surface, while the evidence register remains the fuller source-linked record; metric interpretation and caveats should be checked against the evidence row and source location before a manuscript table is assembled.

## What can be compared now

### Tier A — strongest *within-study* comparisons

These can support careful, condition-matched statements because the material variants share a paper and test design. Keep the numerical endpoint and all relevant conditions visible.

| Candidate / evidence | Defensible use | Conditions and guardrail |
|---|---|---|
| **DISC-002 — TC on natural sepiolite vs montmorillonite** (`EV-B04-014`, `EV-B04-016`) | Compare both observed kinetic uptake and fitted Langmuir (q_{max}) across two mineral adsorbents within the same study. At 298 K, observed uptake was 11.252 mg/g (Sep) and 20.736 mg/g (Mt); fitted (q_{max}) was 33.592 mg/g (Sep) and 213.273 mg/g (Mt). | Observed uptake was measured at 25 mg/L TC, pH 7, 1 g/L dose; fitted values use 10–120 mg/L, pH 7, 1 g/L, 24 h and 298–328 K. Never put the observed 25 mg/L uptake and fitted (q_{max}) into the same metric column. |
| **CORP-020 — SF-600 vs PSF treatment** (`EV-B11-013`) | Within-study comparison of fitted equilibrium capacities for TC, CIP and SMX before/after the reported treatment: TC 228.3→429.3 mg/g; CIP 80.8→361.6 mg/g; SMX 129.1→251.3 mg/g. | Keep the comparison explicitly as fitted (q_m), not observed uptake. Tests were at 298 K; feeds were 1–20 mg/L for TC/CIP/SMX. It is evidence of a processing contrast within that study, not proof of lower cost or better lifecycle performance. |
| **CORP-019 — activated carbon vs barley husks for levofloxacin** (`EV-B17-006`) | A narrowly framed comparison of reported removal: 74% for activated carbon and 71% for barley husks at the same 5 g/L dose, pH 7. | Key tests used 150 mg/L LEVX in synthetic water. Exclude eggshell from an equal-dose ranking (its reported 42% removal used 50 g/L). **Do not use the reported fitted (q_m) or disputed kinetic (q_e)**: mass-balance ceilings are inconsistent with the reported values (`EV-B17-007`, `EV-B17-008`). |
| **DISC-008 — single-solute vs binary CIP/Cu²⁺ tests** (`EV-B01-002`, `EV-B01-004`) | Within-study evidence for the effect of a metal co-contaminant on CIP equilibrium fitting. | Single-solute and binary-system values must remain separate; same nominal dose (0.2 g/L) and pH (6.0 ± 0.2), but a binary mixture changes the adsorption system. This is a competition result, not an across-paper capacity ranking. |
| **CORP-027 — low-concentration adsorption in chlorinated hospital wastewater** (`EV-B08-008`, `EV-B08-009`) | Compare single vs mixed-feed linear partition coefficients and competition in the *same* real-wastewater background. | Values are (K_p) (L/g) at μg/L levels, not (q_{max}) in mg/g. Keep the real matrix, dose and mixture with each value; do not place these in the same capacity ranking as high-mg/L batch studies. |
| **DISC-025 — multi-antibiotic fixed-bed tests** (`EV-B07-014`–`EV-B07-016`) | Compare breakthrough, flow-rate and matrix effects within this one column study. | Keep the Thomas/other model-derived dynamic values, observed saturation (q_s), breakthrough times and treated volumes distinct. The buffer vs filtered/autoclaved wastewater comparison is meaningful within-study; do not rank its μmol/g dynamic parameters against batch mg/g (q_{max}). |
| **CORP-023 — separate chitosan vs alginate beads for amoxicillin** (`EV-B20-005`, `EV-B20-007`) | Potential within-study comparison of observed capacities and fitted isotherms for separate bead types. | The uploaded full text was a preprint version; confirm against the published version before final citation. Preserve pH 4, 300 mg/L context and the finding that alginate beads reportedly dissolved above pH 6. The Langmuir values are fitted, even though the authors say Freundlich generally fit better. |

### Tier B — cross-study cohorts exist, but no pooled ranking is justified

- **Tetracycline (TC):** multiple source-linked fitted capacities are available in mg/g, including natural clays (`DISC-002`), modified sawdust (`CORP-004`), activated/engineered carbons (`CORP-020`, `DISC-012`), and magnetic biochar (`DISC-030`). They span different initial concentrations, dose, pH, temperature, test duration and fitted models. Use them for a structured narrative or condition-stratified table—not a universal high-to-low (q_{max}) league table.
- **Ciprofloxacin (CIP):** the corpus includes conventional batch fits, high-feed clay adsorption, modified-carbon estimates, low-μg/L hospital-wastewater partition coefficients, and fixed-bed results. Those are different endpoints and concentration regimes. Build separate batch-fit, low-concentration matrix and dynamic-column panels.
- **Amoxicillin (AMX):** values from activated carbon, bead adsorbents and retention tests differ in solution conditions and source confidence. At least one reported capacity exceeds the mass-balance ceiling under the paper's stated batch conditions (`DISC-026`); quarantine that result rather than choosing the largest value.
- **Levofloxacin (LEV):** raw rice-husk (q_{max}=2.47) mg/g at a very high 90 g/L sorbent dose (`CORP-010`) is not directly comparable with the disputed fitted capacities for barley husks/eggshells in `CORP-019`. The equal-dose removal comparison above is the safer use of CORP-019.
- **Sulfamethoxazole (SMX), trimethoprim (TMP) and multi-antibiotic feeds:** some useful single-study and fixed-bed comparisons exist, but different units (mg/g, μmol/g, μmol/kg or (K_p) in L/g), feed concentration, mixture status and column endpoints need to stay explicit.

## Quantitative quarantine / hold list

Do **not** use the following values to order adsorbents until the original inconsistency is resolved. Other non-disputed findings from the same paper can still be cited with their own caveats.

| Candidate / evidence | Why the capacity or endpoint is on hold |
|---|---|
| **CORP-025** (`EV-AUD-002`, `EV-AUD-003`) | Nano-montmorillonite dose is 0.03 g/50 mL in Methods (0.6 g/L) but 0.03 g/L in the conclusion; 500, 526 and fitted 558.184 mg/g are not interchangeable. Under the stated 120 mg/L initial concentration and 0.03 g in 50 mL, the mass-balance ceiling is 200 mg/g. |
| **CORP-019** (`EV-B17-007`, `EV-B17-008`) | Barley-husk fitted (q_m=125.735) mg/g exceeds the 30 mg/g ceiling implied by the isotherm maximum concentration and dose; eggshell (q_m=5.6423) mg/g exceeds its 3 mg/g ceiling. Several kinetic (q_e) entries also conflict with the described batch conditions. |
| **DISC-018** (`EV-B09-010`) | Narrative states (q_{max}>200{,}000) mg/g while Table 2 reports values near 1,000 mg/g and experimental kinetic (q_e) around 0.98–1.58 mg/g. Do not rank these fitted capacities. |
| **CORP-031** (`EV-B10-005`, `EV-B10-006`) | The stated trace feeds are 0.1–20 μg/L, while reported (q_e)/(q_m) are tens to hundreds of mg/g; the described solution/dose units do not support those values without clarification. |
| **DISC-028** (`EV-B01-013`, `EV-B01-017`) | Batch adsorbent dose is missing from the accessible main text and the temperature differs between the conclusion and method; the reported maximum column capacity (1124.2 mg/g) exceeds the reported batch Langmuir (q_{max}) (1081.3 mg/g), despite being described as nearly equal. |
| **DISC-026** (`EV-B15-006`, `EV-B15-007`) | Reported amoxicillin experimental/fitted capacities around 239–246 mg/g exceed the 100 mg/g mass-balance ceiling if the stated 25 mg in 50 mL of 50 mg/L AMX condition applies. The abstract's 0.5–2.5 mg/L range also conflicts with methods/results stating 20–70 mg/L. |
| **CORP-017** (`EV-B16-003`) | Pine-bark TMP Langmuir (q_{max}=76{,}429) μmol/kg exceeds the 12,000 μmol/kg ceiling from the highest stated test point and dose; other fits from this paper also need the same mass-balance check before capacity ranking. |
| **DISC-004** (`EV-B02-017`) | Negative Langmuir (Q_m) estimates for antibiotic/material pairs are physically unusable; retain as model-fit failure rather than a capacity value. |
| **DISC-007** (`EV-B19-003`) | KN@Alg pseudo-second-order calculated (q_e=144.307) mg/g is more than twice experimental equilibrium uptake (68.700 mg/g), and the fit has (R^2=0.838). Use the experimental observation, not the modelled (q_e), for a like-for-like comparison. |
| **DISC-014** (`EV-B19-010`) | Three-cycle column table values sum to 187.11 mg/g, but the conclusion reports 178.11 mg/g. Keep the table/conclusion discrepancy and separate column (q_{bed}) from batch capacity. |
| **DISC-027** (`EV-B05-015`, `EV-B05-017`) | TC batch dose is ambiguous after doubling the solution volume; fixed-bed Thomas/Adams–Bohart fits are explicitly described as inadequate. Do not label the modelled column values as validated service capacity. |

## Rules for the integrated comparison tables

1. Separate **observed batch uptake** ((q_e)), **fitted equilibrium capacity** ((q_{max}) or (q_m)), **percentage removal**, **linear partition coefficient** ((K_p)), and **dynamic column metrics** ((q_{TH}), (q_s), (q_{bed}), (q_{total}), breakthrough time/volume).
2. Show antibiotic identity/form, initial concentration, solution matrix, dose and solution volume, pH, temperature, contact time, and model/fit quality beside the value wherever reported.
3. Treat source/condition inconsistencies as hold flags; never select one conflicting value silently. “Waste-derived” and a high removal percentage do not by themselves establish low cost or process sustainability.
4. Convert μmol/kg, μmol/g or μg/g only with the antibiotic-specific molecular weight and retain the originally reported unit alongside the conversion. Do not convert (K_p) to a capacity.
5. Keep review-derived values as citation leads, not primary data. The deferred review `DISC-022` remains outside this audit pending the user's full text.

## Outcome and next action

- **No global adsorbent capacity ranking is defensible yet.**
- The strongest present outputs are condition-matched *within-study* contrasts and separate panels for batch equilibrium, low-concentration real-matrix adsorption, and fixed-bed operation.
- First table artifact now exists at `manuscript/COMPARATIVE_TABLES_V1.md`: five panels cover TC natural-clay observed uptake and fitted capacity, a within-study carbon-processing contrast, low-concentration real-matrix `K_p`, and fixed-bed model values. It retains candidate/evidence IDs and key caveats.
- Next: apply final retain / exclude / background-only decisions with explicit quartile-system/year rules; verify each comparison table against the source PDFs and supplements before marking it manuscript-ready.
