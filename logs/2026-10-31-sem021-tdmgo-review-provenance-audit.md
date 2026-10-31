# SEM-021 TDMGO primary-abstract and review-provenance audit — 31 October 2026

## Study identity
Yang, Y., Hu, X., Zhao, Y., Cui, L., Huang, Z., Long, J., Xu, J., Deng, J., Wu, C. and Liao, W. (2017), “Decontamination of tetracycline by thiourea-dioxide–reduced magnetic graphene oxide: Effects of pH, ionic strength, and humic acid concentration,” *Journal of Colloid and Interface Science* 495, 68–77. DOI: 10.1016/j.jcis.2017.01.075. PMID: 28189111.

Official ScienceDirect page: https://www.sciencedirect.com/science/article/abs/pii/S0021979717300978
PubMed record: https://pubmed.ncbi.nlm.nih.gov/28189111/
ResearchGate record: https://www.researchgate.net/publication/312870416_Decontamination_of_tetracycline_by_thiourea-dioxide-reduced_magnetic_graphene_oxide_Effects_of_pH_ionic_strength_and_humic_acid_concentration

The primary publisher abstract, Materials snippet, Characterization snippet, Conclusion snippet and PubMed record were checked on 31 October 2026. The full article and supplementary information are behind organizational access/purchase; ResearchGate says no full text is available. A search of the current conversation/Library surfaces did not locate the primary PDF. No new PDF batch is assumed or requested.

## What the primary abstract actually supports
The abstract confirms:
- Adsorbent: thiourea-dioxide-reduced magnetic graphene oxide (TDMGO).
- Target: tetracycline (TC) from aqueous solution.
- Characterization: SEM, TEM, EDS, TGA, FTIR, XPS, XRD and VSM.
- The study varied pH, TC concentration and temperature.
- Kinetic data were described by a pseudo-second-order model.
- Isotherm data were described by a Langmuir model.
- Langmuir-fitted maximum adsorption capacity q_m = 1233 mg/g at 313 K.
- Thermodynamics are described as spontaneous and endothermic.
- The pH effect is described as slight.
- NaCl facilitates adsorption; the abstract says optimum adsorption capacity was obtained when NaCl concentration was greater than 0.001 M.
- Adsorption capacity decreased slightly as humic-acid concentration increased.
- The abstract says the adsorbent could be regenerated and reused, but it provides no cycle count, regeneration method or retention metric.

The 1233 mg/g figure is explicitly a **Langmuir-calculated q_m**, not a directly observed equilibrium uptake q_e. The abstract contains no observed qe, no exact concentration range, no batch volume or adsorbent dose, and no fit statistics.

## Materials snippet and preparation boundary
The publisher Materials snippet reports:
- Graphite powder, particle size ≤30 μm.
- Tetracycline hydrochloride, C22H24N2O8·HCl, MW 480.9 g/mol.
- Formamidine sulfinic acid (thiourea dioxide), 98% purity.
- Humic acid.
- Hydrochloric acid (37%), sulfuric acid (95–98%), ethanol and sodium hydroxide, among other reagents.

The accessible snippet does not expose a full GO/MGO/TDMGO synthesis recipe, reagent masses or ratios, pH/temperature/time of the thiourea-dioxide reduction, magnetic-iron precursor conditions, product yield, washing volume, drying conditions or energy use. Do not reconstruct the synthesis from another magnetic GO study.

## Secondary review cross-check — Fan et al. (2021)
Fan, B. et al., “Application of Magnetic Composites in Removal of Tetracycline through Adsorption and Advanced Oxidation Processes (AOPs): A Review,” *Processes* 2021, 9, 1644. DOI: 10.3390/pr9091644.
Full-text copy inspected: https://psecommunity.org/wp-content/plugins/wpor/includes/file/2302/LAPSE-2023.5213-1v1.pdf

The review's Table 2 (printed page 6) explicitly labels columns:
- Initial concentration of TC (mg/L)
- Dosage (g/L)
- pH
- Temperature (K)
- Contact time (min)
- Adsorption capacity (mg/g)
- Isotherm/kinetics model
- Reference

Its TDMGO row lists:
- Initial TC concentration: 10 mg/L
- Dosage: 70 g/L
- pH: 4
- Temperature: 313 K
- Time: 1440 min
- Adsorption capacity: 1233 mg/g
- Models: Langmuir / pseudo-second-order
- Reference: [63]

The review bibliography confirms reference 63 is the correct Yang et al. (2017) primary paper, DOI 10.1016/j.jcis.2017.01.075. This is a correct secondary-source linkage, but its operating-condition vector is not primary-verified in this audit.

### Feed-limitation calculation for the review's condition vector
If the review's C0 and dosage are interpreted as one batch condition:
- C0 = 10 mg/L
- adsorbent dose = 70 g/L
- maximum possible feed-limited uptake = C0 / dose = 10 mg/L ÷ 70 g/L = 0.1429 mg/g.

That ceiling is far below 1233 mg/g. This does **not** prove that the fitted Langmuir q_m itself is mathematically impossible, because a Langmuir asymptote may be fitted from a separate concentration series and exceed observed qe values at individual lower-concentration test points. It does prove that the review's single-point 10 mg/L / 70 g/L vector cannot be treated as the measured-uptake condition supporting q_m=1233 mg/g. Keep the fit and that vector separate until the primary isotherm range and dose are verified.

## Secondary review cross-check — Gopal et al. (2020)
Gopal, G. et al., “A review on tetracycline removal from aqueous systems by advanced treatment techniques,” *RSC Advances* 2020, 10, 27081–27095. DOI: 10.1039/D0RA04264A. PMCID: PMC9055545.
Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC9055545/
Publisher page: https://pubs.rsc.org/en/content/articlehtml/2020/ra/d0ra04264a

The RSC review contains two different TDMGO reference trails:
1. Section 4.2.4 describes TDMGO and gives q_m=1233.257 mg/g at 39.85 °C, citing reference 85. The review's bibliography confirms reference 85 is Yang et al. (2017), DOI 10.1016/j.jcis.2017.01.075. This is the correct citation.
2. Table 3, row 9, lists TDMGO with “Sorbent 70 g, TC 10 mg L−1, pH 4, 39.85 °C, 24 h,” capacity 1233.257 mg/g, but the row's citation is reference 73. The bibliography confirms reference 73 is Xiang et al. (2019), “Carbon-based materials as adsorbent for antibiotics removal: Mechanisms and influencing factors,” *Journal of Environmental Management* 237, 128–138, DOI 10.1016/j.jenvman.2019.02.068. That is an unrelated review, not the primary TDMGO paper. Therefore the RSC Table 3 row's reference is mismapped. The RSC table also states a sorbent mass of 70 g without reporting a solution volume, so this entry cannot support a feed-mass calculation.

Do not silently change “70 g” to “70 mg,” do not infer an unreported solution volume, and do not use the RSC Table 3 operating vector as primary evidence. The RSC narrative's reference 85 is correct; its Table 3 row reference 73 is not.

## Solution chemistry and practical evidence boundary
The primary abstract provides only qualitative directions:
- pH has a slight effect.
- NaCl facilitates uptake; capacity is reported optimum above 0.001 M.
- Humic acid increases slightly reduce adsorption capacity.

Exact salt concentration series, humic-acid concentrations, pH range, TC concentration range, temperature range, adsorption dose, solution volume and contact times are absent from the accessible primary snippets.

No real wastewater, natural-water or field-matrix test is identified in the primary abstract. No actual cost, cost per volume treated, process energy, yield, reagent recovery, wash-water inventory, LCA or TEA evidence is exposed. The statement that the adsorbent can be regenerated and reused is qualitative; no cycle count, eluent, cycle-specific capacity or capacity-retention percentage is visible.

## Semester-paper decision
Retain SEM-021 as an abstract-supported example of thiourea-dioxide-reduced magnetic GO for TC adsorption and as a source for qualitative matrix effects (NaCl facilitation and humic-acid inhibition).

The only quantitative primary claim safe to carry forward at this stage is:
- Langmuir-fitted q_m = 1233 mg/g at 313 K.

It must be labelled **model-derived** and not presented as observed qe. Keep it out of condition-matched quantitative rankings until the full primary concentration series, adsorbent dose, batch volume, Langmuir coefficients/fit quality and observed uptake are verified.

Do not:
1. Pair q_m=1233 mg/g with the Fan et al. 2021 Table 2 single-condition vector as if it were observed qe. The vector's feed ceiling is 0.1429 mg/g.
2. Copy the Gopal et al. 2020 Table 3 condition/reference bundle. Its row cites unrelated reference 73 and lists 70 g with no volume; the review's narrative section correctly cites ref85.
3. Correct g to mg, infer volume or assume the full primary isotherm range from review rows.
4. Claim quantified regeneration, actual-water performance, or economic advantage based only on the primary abstract.

## Repository updates
Updated in place:
- data/semester-remaining-work-register.csv
- data/semester-paper-candidate-register.csv
- data/semester-evidence-readiness-audit.csv (existing EV-SEM-038)
- data/source-caveats.csv
- data/semester-manuscript-claim-evidence-audit.csv (CLM-23)
- README.md

No condition-labelled numeric comparison row was added. No duplicate evidence ID was created. Zotero Better BibTeX key remains unverified; do not invent one.
