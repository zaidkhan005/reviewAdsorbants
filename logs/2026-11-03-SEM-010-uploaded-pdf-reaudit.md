# SEM-010 uploaded-PDF re-audit

**Date:** 3 November 2026  
**Candidate:** SEM-010  
**Source:** Yasmin, S. et al. (2024), *Heliyon* 10(12), e33317. DOI: 10.1016/j.heliyon.2024.e33317.  
**Supplied file:** `PIIS2405844024093484.pdf` (17 pages).  
**Identity cross-check:** This is the already-registered SEM-010 paper, not a new candidate. The publisher ScienceDirect record and PubMed/PMC identify the same title, DOI, article number, and authors (PMID 39022076; PMCID PMC11253669). The previously inspected official supplementary DOCX is computational/DFT material and contains no experimental adsorption raw data that resolves the dose basis.

## What the uploaded PDF confirms

- **Target/material:** ciprofloxacin (CIP) adsorbed using graphene oxide prepared from recovered graphite/carbon rods from spent Zn–C batteries.
- **Reported optimum:** (C_0=2.0) mg/L, 40 mL solution, GO dose 20 mg/L, pH 5.7, 230 rpm, 30 °C, and 20 min. The abstract reports 99.0% removal. Figure 3(c) shows the contact-time response approaching approximately 98.5–99% at 20 min.
- **Kinetics:** Table 4 and §3.6.6 report experimental (q_e=78.82) mg/g. Pseudo-second-order fitted (q_e=79.36) mg/g (linear (R^2=1.0000); nonlinear (R^2=0.8584)). The PFO fits are poorer (linear (R^2=0.4363); nonlinear (R^2=0.5500)).
- **Isotherm:** Table 1 reports nonlinear Langmuir-fitted (q_m=419.62), 434.56, and 441.44 mg/g at 30, 40, and 50 °C, respectively. At 30 °C, nonlinear Langmuir (R^2=0.9800); these are fitted asymptotes from a separate concentration series, not observed uptake under the 2 mg/L removal test. The paper does not state the complete initial-concentration range for the isotherm series.
- **Regeneration:** §3.6.9 reports methanol regeneration across seven cycles and 92% CIP removal after cycle 7. This is a removal percentage, not a measured capacity-retention percentage; the figure does not provide a full cycle-by-cycle (q_e) series or solvent-recovery data.
- **Preparation:** carbon rods were manually separated, washed, dried, crushed, and pretreated with HCl:HNO3 (3:1) at 60 °C for 2 h. GO was then prepared by an improved Hummers route: 1 g recovered graphite, H2SO4:H3PO4 (9:1), 6 g KMnO4, 50 °C for 12 h, quench with 400 g ice plus 3 mL 30% H2O2, centrifugation, repeated DI-water/30% HCl/DI-water/ethanol washing, and vacuum drying at 45 °C for 48 h. BET area was 61.08 m²/g, average pore width 3.84 nm, and pore volume 0.0926 cm³/g.
- **Applicability/economics:** all solutions are described as ultrapure DI-water based; there is no real wastewater trial, no leaching test, and no quantified yield, reagent recovery, energy, or total process-cost inventory. A waste-derived carbon precursor alone does not establish low total cost.

## Mass-balance audit: distinguish reported values from inferred basis

The article states a 40 mL test volume and an optimum GO concentration of 20 mg/L. If both are applied literally:

- CIP initially present: (2.0 mathrm{mg/L}	imes0.040 mathrm{L}=0.080) mg.
- GO mass: (20 mathrm{mg/L}	imes0.040 mathrm{L}=0.80) mg.
- At 99.0% removal, CIP removed is 0.0792 mg, which implies (q_e=0.0792/0.00080=99.0) mg/g.
- Table 4's experimental (q_e=78.82) mg/g would correspond to 78.82% removal on that same stated 0.80 mg GO basis. The PSO fitted (q_e=79.36) mg/g corresponds to 79.36% on that basis.

A possible explanation is an unreported or mismatched weighed GO mass. Combining 99.0% removal with the measured (q_e=78.82) mg/g implies approximately 1.005 mg GO in 40 mL, equivalent to 25.1 mg/L. Combining it with PSO (q_e=79.36) mg/g implies approximately 0.998 mg GO, equivalent to 25.0 mg/L. The Figure 3(c) value near 98.5% at 20 min also gives approximately 0.99–1.00 mg GO when paired with (q_e=78.82) mg/g. This is an arithmetic inference only: the paper does not state the exact weighed GO mass per kinetic flask or confirm a 25 mg/L dose. Do not replace the source-reported 20 mg/L with 25 mg/L. Keep the removal, observed kinetic (q_e), fitted kinetic (q_e), and isotherm (q_m) as separate source outputs.

A separate unit conflict remains: the Conclusion says 20 g/L, whereas the abstract, figure captions, and Results state 20 mg/L (1000-fold difference). If 20 g/L were applied literally to the 2 mg/L, 40 mL feed, the feed-mass ceiling would be only 0.1 mg/g. The conclusion value is inconsistent with the rest of the reported experiment and should not be adopted as an operating condition without author clarification.

## Project treatment

- SEM-010 remains in the frozen selected-49 set. No reference membership, bibliography key, or Table 2 study-scope change is made.
- Retain the reported 99% removal as a source-reported endpoint but qualify its dose basis.
- Retain experimental kinetic (q_e=78.82) mg/g and PSO-fitted (q_e=79.36) mg/g as distinct outputs.
- Retain nonlinear Langmuir (q_m=419.62) mg/g at 30 °C only as a fitted isotherm parameter, not as observed low-feed uptake or a cost-feasibility proof.
- Use the seven-cycle methanol result as removal-after-regeneration context, not capacity retention.
- Do not claim demonstrated low-cost operation, real-water performance, or scale-up feasibility.
- No author clarification or experimental mass record was found in the supplied PDF or previously inspected official supplement; the mass/dose basis remains unresolved.

**Audit outcome:** the uploaded publisher PDF independently confirms the registered source and its existing caveats. The new contribution is a conditional calculation showing that the 99% removal and measured kinetic uptake could align at approximately 1 mg GO per 40 mL (about 25 mg/L), but this cannot be promoted to a corrected source condition without the missing batch mass record.
