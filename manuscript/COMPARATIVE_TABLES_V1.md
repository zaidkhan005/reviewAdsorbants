# Comparative evidence tables — v1 (working draft)

**Status:** Evidence-grounded table draft; not yet manuscript-final. Candidate IDs and evidence IDs are retained for traceability. Confirm the journal ranking year/category required by the supervisor before using these as a Q1-only shortlist: current 2025 SJR signals in the repository do not automatically establish quartile in each paper's publication year or in JCR.

**Comparison rule:** Each table is a distinct endpoint. Observed uptake, fitted equilibrium capacity, removal percentage, linear distribution coefficient and dynamic-column capacity must not be pooled into one rank order.

## Table 1. Tetracycline uptake on two natural clays under the same study design

Source: Zhou et al. (2024), *Effective microwave regeneration of natural sepiolite and montmorillonite as adsorbents for tetracycline removal and mechanism insight*, DOI [10.1016/j.seppur.2024.127767](https://doi.org/10.1016/j.seppur.2024.127767). Evidence: `EV-B04-014`.

| Temperature | Natural sepiolite observed uptake (mg/g) | Montmorillonite observed uptake (mg/g) | Interpretation guardrail |
|---:|---:|---:|---|
| 298 K | 11.252 | 20.736 | Same initial TC concentration (25 mg/L), pH 7 and 1 g/L dose. |
| 308 K | 11.721 | 21.815 | Observed uptake from the study's temperature series. |
| 318 K | 11.958 | 22.564 | Keep distinct from fitted isotherm capacity. |

**Reported contact to approximate equilibrium:** approximately 240 min for sepiolite and 120 min for montmorillonite. The source describes 0.02 g adsorbent in 20 mL TC solution, pH 7 and 100 rpm. These are laboratory batch data, not real-wastewater or column capacities.

## Table 2. Fitted Langmuir (q_{max}) for tetracycline on natural clays

Source and conditions: same study as Table 1; 10–120 mg/L TC, 1 g/L adsorbent, pH 7, 24 h; fit temperatures 298–328 K. Evidence: `EV-B04-016`.

| Temperature | Sepiolite fitted (q_{max}) (mg/g) | Montmorillonite fitted (q_{max}) (mg/g) |
|---:|---:|---:|
| 298 K | 33.592 ± 1.290 | 213.273 ± 42.057 |
| 308 K | 38.057 ± 1.202 | 237.854 ± 45.135 |
| 318 K | 48.363 ± 1.347 | 242.557 ± 50.620 |
| 328 K | 65.040 ± 3.011 | 245.411 ± 34.842 |

Langmuir (R^2) is reported as greater than 0.97; Freundlich (R^2) is roughly 0.936–0.976. These are model-fitted asymptotes across the concentration series. Do **not** substitute them for observed uptake at 25 mg/L from Table 1.

## Table 3. Within-study processing contrast: sunflower-seed-husk carbon before and after activation

Source: Nguyen et al. (2023), *Phosphoric Acid-Activated Biochar Derived from Sunflower Seed Husk: Selective Antibiotic Adsorption Behavior and Mechanism*, DOI [10.1016/j.biortech.2023.128593](https://doi.org/10.1016/j.biortech.2023.128593). Evidence: `EV-B11-013`.

| Target | SF-600 fitted Langmuir (q_m) (mg/g) | PSF fitted Langmuir (q_m) (mg/g) | PSF/SF-600 ratio (calculated) |
|---|---:|---:|---:|
| Tetracycline (TC) | 228.3 | 429.3 | 1.88× |
| Ciprofloxacin (CIP) | 80.8 | 361.6 | 4.48× |
| Sulfamethoxazole (SMX) | 129.1 | 251.3 | 1.95× |

*Ratios are arithmetic calculations from the reported fitted values, not independently measured performance indices.* The same record reports 298 K, 10 mM NaNO₃ and concentration series of 1–20 mg/L for TC/CIP/SMX. The extracted method description lists PSF at 25 mg/L; verify the exact adsorbent-dose wording in the source before final publication. These values support a within-study processing contrast, not a general claim that activation always improves performance or lowers cost. Ibuprofen is excluded from this antibiotic-only table because it is not an antibiotic.

## Table 4. Low-concentration adsorption in a real chlorinated hospital-wastewater background

Source: Sompornpailin et al. (2024), *Removal of Antibiotics, Bacterial Toxicity, and Occurrence of Antibiotic Resistance Genes in Secondary Hospital Effluents Treated with Granular Activated Carbon and the Impact of Preceding Chlorination*, DOI [10.1016/j.scitotenv.2024.172095](https://doi.org/10.1016/j.scitotenv.2024.172095). Evidence: `EV-B08-008`, `EV-B08-009`. These values are linear isotherm distribution coefficients (K_p) (L/g), **not** (q_{max}) (mg/g).

| Antibiotic label in source | Single-solute (K_p) (L/g) | Mixed-feed (K_p) (L/g) | Reported change / interpretation |
|---|---:|---:|---|
| PCG | 0.3778 | 0.2996 | Adsorption modestly reduced in mixture. |
| AMP | 0.8379 | 0.5292 | Approximately 37% decrease at the reported comparison point. |
| CAZ | 0.3916 | 0.3770 | Small change at the reported comparison point. |
| CIP | 0.4157 | 0.1738 | Approximately 58% decrease at the reported comparison point. |
| MEM | 1.5674 | Not fitted/reported | Not reported as adsorbed/fitted in the mixed solution. |
| SMZ | 0.7876 | Not fitted/reported | Not reported as adsorbed/fitted in the mixed solution. |

Single-solute comparison conditions: initial concentration 100 μg/L, GAC dose 1 g/L, pH 7, 25 °C, phosphate-buffered solution with actual chlorinated hospital wastewater as background matrix. Mixed-feed tests covered 50–200 μg/L. Retain the original antibiotic abbreviations as reported in the source until the final reference and analyte names are checked. This is the low-concentration/matrix panel; do not compare these (K_p) values numerically with mg/g batch capacities.

## Table 5. Fixed-bed dynamic adsorption values — retain model and unit

Source: Sousa et al. (2026), *Fixed-bed adsorption of antibiotics using a brewery residue-derived biosorbent: Matrix effects, regeneration, and environmental assessment*, DOI [10.1016/j.jwpe.2025.109355](https://doi.org/10.1016/j.jwpe.2025.109355). Evidence: `EV-B07-014`–`EV-B07-016`.

| Antibiotic | Thomas-model (q_{TH}) at 0.042 L/h (μmol/g) | Column-specific interpretation |
|---|---:|---|
| SMX | 11.4 ± 0.2 | Dynamic-model estimate under the reported buffered-water column condition. |
| TMP | 33 ± 1 | Keep the (q_{TH}) model parameter separate from observed saturation capacity. |
| CIP | 18.9 ± 0.2 | Keep flow rate, feed, pH and bed geometry attached to the value. |

The reported apparatus was a 13 cm column with 1.0 cm internal diameter, 4.4 cm bed depth and approximately 2 g biosorbent, operated at 25 °C and pH 8 with 20 μmol/L feed. The paper separately reports buffered-water versus filtered/autoclaved wastewater comparisons and several other fitted/experimental dynamic measures. Those must remain separate fields: (q_{TH}), model-derived (q_Y), experimental (q_s), breakthrough time and treated volume are not interchangeable. Supplementary LCA details were not in the supplied main-text PDF; process-impact claims need the full inventory/model boundaries.

## Items intentionally not promoted into these core tables yet

- **CORP-019 (levofloxacin; Journal of Engineering):** the within-study removal values for activated carbon and barley husks (74% and 71% at equal 5 g/L dose) could serve as a low-processing comparison, but the journal is currently Q2 in the accessed 2025 SJR categories, and the fitted (q_m)/kinetic entries have mass-balance problems. Do not treat it as a current-Q1 core item or rank its suspect capacities.
- **CORP-023 (amoxicillin, chitosan vs alginate beads):** the accessible source was a preprint version; the published version must be checked before adopting its reported observed capacities or fitted (q_{max}).
- **CORP-025, DISC-018, CORP-031, DISC-028, DISC-026, CORP-017, DISC-004, DISC-007, DISC-014 and DISC-027:** retain their independently useful qualitative/condition findings but hold the specific values listed in the [comparison-readiness audit](../logs/2026-10-27-comparison-readiness-audit-01.md) from cross-paper ranking until the source/mass-balance/endpoint issues are reconciled.
- **DISC-022:** deferred by the user until they provide the full text; not screened or excluded.

## Current use and next work

These tables are a v1 evidence artifact, not final publication tables. Before final use: apply publication-year/category quartile rules; confirm source wording for the SF-600/PSF dose; check each cited PDF/table and supplement where noted; use Zotero-formatted citations; and adjudicate final retain/exclude/background-only status. Do not generate an overall material ranking from these tables.
