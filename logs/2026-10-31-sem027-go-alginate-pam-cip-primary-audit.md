# SEM-027 GO/Ca-alginate/PAM bead primary-source audit — 31 October 2026

## Study identity and authoritative source
Choi, J.-W. and Choi, S.-J. (2022), “Polyacrylamide Functionalized Graphene Oxide/Alginate Beads for Removing Ciprofloxacin Antibiotics,” *Toxics* 10(2), 77. DOI: 10.3390/toxics10020077. Published 7 February 2022.

Official full text:
- MDPI: https://www.mdpi.com/2305-6304/10/2/77
- PubMed Central: https://pmc.ncbi.nlm.nih.gov/articles/PMC8876689/
- PubMed: https://pubmed.ncbi.nlm.nih.gov/35202263/

The open-access MDPI text and PMC full-text copy were inspected on 31 October 2026. Methods §§2.1–2.4, Results §§3.1–3.3, Figures 1–6, Tables 1–3 and Conclusion were checked. This audit supersedes the earlier partial extraction and corrects the previous readiness note that suggested reuse/regeneration evidence.

## Material identity and preparation boundary
The adsorbent is a three-dimensional double-network GO/calcium-alginate/polyacrylamide bead, denoted GO/Ca-Alg2–PAM.

Materials:
- GO and PAM were purchased from Aldrich.
- Sodium alginate and calcium chloride dihydrate were purchased commercially.
- Ultrapure water (18.2 MΩ·cm) was used.
- Ciprofloxacin (CPX) was prepared as a simulated aqueous solution.

Bead preparation:
1. Disperse 0.1 g GO in 100 mL ultrapure water by sonication.
2. Add 0.6 g sodium alginate and stir until homogeneous.
3. Slowly add 1.0 g PAM powder.
4. Heat at 80 °C for 4 h, until the solution becomes sticky; cool to 30 °C.
5. Use a syringe pump to drop the mixture at 2 mL/min into a 10 g/L CaCl2·2H2O bath.
6. Stir the beads in the calcium chloride bath for 24 h at room temperature to stabilize the beads.
7. Wash three times with ultrapure water and oven-dry at 80 °C.

The article describes crosslinking and cation exchange between sodium alginate and calcium ions, yielding a Ca-alginate network, with GO and PAM incorporated into the double-network structure. Characterization includes FE-SEM, FTIR, SEM-EDS and TGA. The authors say the beads remain thermally stable/usable up to about 100 °C based on TGA.

Important process boundary: this paper purchases GO and PAM; it does not report its own GO oxidation/exfoliation synthesis. It therefore cannot be used as a complete GO manufacturing-cost inventory. It consumes polymer, CaCl2 crosslinking bath, ultrapure water, heating, 24 h bead stabilization, repeated washing and oven drying. No product yield, water consumption, chemical recovery, energy per gram or normalized cost is reported.

## Adsorption experiments and the physical volume inconsistency
The Methods state that all experiments were performed in duplicate batch systems using a **50 mL conical tube**. For the adsorption isotherm, the article then specifies:
- CPX initial concentrations: 1–50 ppm (approximately 1–50 mg/L for dilute aqueous solution).
- Bead mass: 0.05 g.
- Contact solution volume: 55 mL.
- Agitation: 250 rpm.
- Contact time: 24 h.
- Temperature: room temperature.
- Residual CPX: centrifuge at 3500 rpm for 10 min, filter through 0.20 µm nitrocellulose filter and measure by UV–Vis at 270 nm.
- Batch experiments are stated to be duplicate.

The 50 mL tube cannot contain the stated 55 mL liquid volume. Both values are preserved as printed. Do not silently change 55 mL to 50 mL or infer that the container was actually larger; the article does not resolve the discrepancy.

If the 55 mL volume is used provisionally, the simple feed-limited uptake ceiling is:

`q_{e,max,feed} = C_0 V / m`

For 0.05 g beads and 55 mL:
- At 1 mg/L, maximum available-feed uptake is 1.1 mg/g.
- At 50 mg/L, maximum available-feed uptake is 55 mg/g.

These are calculated upper bounds from the stated volume, not measured uptake. They do not create a contradiction with the fitted Langmuir q_m=6.846 mg/g, which is below the upper-concentration feed ceiling. Because the vessel/volume combination is physically inconsistent, the exact denominator remains uncertain.

## Adsorption-capacity equation dimensionality
The article prints:

`q_e = (C_0 - C_e) V / W`

It defines C0 and Ce in ppm (for dilute water, mg/L), V as contact volume in **mL**, and W as adsorbent mass in g; qe is described as mg/g.

As written, those units do not yield mg/g without a conversion:
- If C is mg/L and V is mL, use V/1000 in litres:
  `q_e (mg/g) = (C_0-C_e) [mg/L] × V [mL] / (1000 × W [g])`.
- Alternatively, V must be expressed in litres and the displayed equation should state that.

The article does not show an explicit /1000 factor or clarify whether it was applied internally in the data processing. This is an unresolved dimensional/unit ambiguity, not proof that the reported q_m is numerically wrong. Since raw residual concentrations and measured qe values are not tabulated, the calculation convention cannot be independently reconstructed. Do not infer a corrected uptake value or rescale q_m by 1000.

## Isotherm results: fitted parameters only
The paper fits Langmuir, Freundlich and Temkin isotherms to the isotherm data. Table 1 reports:

| Model | Parameters | R² | χ² |
|---|---|---:|---:|
| Langmuir | q_m = 6.846 mg/g; b = 0.132 L/mg | 0.991 | 0.037 |
| Freundlich | K_F = 1.260; n = 2.372 | 0.932 | 0.282 |
| Temkin | B = 1954.69 (source-reported units L/mg); K_T = 2.074 L/g | 0.966 | 0.142 |

Langmuir is the best of the three models by the reported R² and chi-square values. q_m=6.846 mg/g is a **fitted Langmuir asymptote**, not a directly observed qe at a named initial concentration. The article includes an isotherm plot (Figure 4) but does not tabulate numerical experimental qe/removal values for individual C0 points in the text. Do not substitute q_m for measured qe.

The paper's printed Temkin B unit and equation notation should be treated as source-reported conventions; do not build an independent mechanistic interpretation from that parameter without checking its dimensional definition.

## Temperature and thermodynamics
Temperature-effect experiments use CPX initial concentrations of 0.5, 1 and 2 ppm at 10, 25 and 40 °C, using the same basic adsorption procedure. The paper states that experiments in this series were conducted in triplicate, and that qe increased as temperature increased for all three CPX concentrations. Figure 5 presents the temperature response; exact individual qe values are not tabulated numerically in the article text.

Table 3 reports:
| CPX concentration | ΔH (kJ/mol) | ΔS (kJ/mol·K) | ΔG at 283 K (kJ/mol) | ΔG at 298 K | ΔG at 313 K |
|---:|---:|---:|---:|---:|---:|
| 0.5 ppm | 10.7 | 0.056 | −5.29 | −6.13 | −6.98 |
| 1 ppm | 4.4 | 0.035 | −5.57 | −6.10 | −6.63 |
| 2 ppm | 7.2 | 0.044 | −5.25 | −5.91 | −6.57 |

The entropy entries in kJ/mol·K correspond to 56, 35 and 44 J/mol·K, respectively. This is consistent with the article's prose stating that ΔS is in the range 35–56 J/mol·K. Do not incorrectly flag this as a thousand-fold entropy unit error; it is a unit conversion between kJ and J.

The positive ΔH values and negative ΔG values support the authors' interpretation that adsorption is endothermic and spontaneous over the examined conditions. Keep thermodynamic quantities separate from capacity measurements. There is no numeric observed qe table from which to reconstruct each temperature-series uptake.

## Regeneration, reuse and practical applicability
There is **no adsorption–desorption regeneration experiment or cycle-resolved reuse result** in the article. The authors state that the beads can be separated conveniently from water and discuss their potential for wastewater treatment. TGA indicates thermal behavior/stability up to about 100 °C. Neither bead separability nor thermal stability establishes adsorbent regeneration or adsorption-capacity retention.

The article does not test actual municipal, industrial or natural wastewater. It uses simulated CPX solutions. There is no fixed-bed/column performance experiment, despite the authors' discussion that bead shape could reduce pressure drop and be useful in a packed bed. There is no metal-leaching issue quantified, no field validation and no cost or process-energy analysis. The conclusion's suggestion of use in actual wastewater should be described as a proposed application, not a demonstrated real-water result.

## Semester-paper decision
Retain SEM-027 / EV-SEM-025 as:
- a GO/polymer double-network bead architecture;
- an easy-solid-separation design feature;
- a low Langmuir fitted q_m example (6.846 mg/g), not an observed qe result;
- an example of endothermic/spontaneous thermodynamic interpretation.

For quantitative manuscript treatment:
1. Label 6.846 mg/g as **Langmuir-fitted q_m**, not measured uptake.
2. State that the source does not numerically tabulate observed qe/removal points.
3. Flag the stated 55 mL solution volume in a 50 mL conical tube.
4. Flag the dimensional ambiguity in the qe equation (V defined in mL while C is mg/L, no explicit /1000 conversion).
5. Do not call the ΔS values erroneous; .035–.056 kJ/mol·K is 35–56 J/mol·K, matching the narrative.
6. Do not claim reuse/regeneration; no adsorption–desorption cycles are reported.
7. Do not claim real-water validation or a quantified low-cost advantage. GO and PAM are purchased, and the paper supplies no yield, energy or normalized cost data.

## Citation workflow
No matching Better BibTeX key was verified in the latest inspected citation export. Do not invent a key. If selected for citation, add/verify the Zotero metadata and use the actual generated key.

## Repository updates
Updated in place:
- data/semester-remaining-work-register.csv
- data/semester-paper-candidate-register.csv
- data/semester-evidence-readiness-audit.csv (EV-SEM-025)
- data/semester-condition-labelled-comparison.csv (EV-SEM-025)
- data/semester-manuscript-claim-evidence-audit.csv (CLM-25)
- data/source-caveats.csv
- README.md

No duplicate SEM or evidence ID was created. No observed qe or false reuse result was added to the manuscript comparison.
