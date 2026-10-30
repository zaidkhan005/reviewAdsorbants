# SEM-049 primary-source metric, figure and mechanism audit (2026-10-31)

## Candidate and source

Chen et al. (2022), “Effective Removal of Tetracycline from Water Using Copper Alginate @ Graphene Oxide with In-Situ Grown MOF-525 Composite: Synthesis, Characterization and Adsorption Mechanisms,” *Nanomaterials* 12(17), 2897. DOI 10.3390/nano12172897. Official MDPI PDF opened and its extracted text cross-checked against the earlier repository extraction. Source: https://www.mdpi.com/2079-4991/12/17/2897/pdf?version=1661263589.

The MDPI PDF screenshot service returned HTTP 429 during attempted page-image capture. Therefore, this pass verifies the publisher PDF's extracted text, equations, tables and captions but does not claim a successful visual screenshot inspection.

## 1. Experimental conditions and dose discrepancy

Methods §2.4 (printed p. 4) state:
- General baseline adsorbent dose = 0.5 mg/mL.
- General initial TC concentration = 200 mg/L.
- Temperature = 298 K; agitation = 200 rpm; dark conditions; evaluation after 48 h.
- The separate dosage experiment uses 2, 4, 7, 10, 15 and 20 mg.
- The pH range is 2–8.
- The temperature series uses 298, 308 and 318 K.
- Methods state an initial concentration range of 80–280 mg/L for the temperature/concentration experiment.
- A 200 mL TC solution is explicitly stated for the contact-time experiment; the paper does not clearly state that every other variable sub-study used the same volume.

The dosage range 2–20 mg cannot be reconciled to the general dose 0.5 mg/mL without knowing the solution volume used in that separate dosage series. Do not automatically treat 2–20 mg as 0.01–0.1 mg/mL, or assume that 200 mL applied to every variable series.

## 2. Concentration-range / table-unit discrepancy

Table 3's own-study row lists dosage = 0.5 mg/mL and C0 = 80–240, but the table header prints C0 units as **mg/mL**. Methods §2.4 instead reports 80–280 **mg/L**. This is both a unit discrepancy (mg/mL vs mg/L) and a range-endpoint discrepancy (240 vs 280).

Do not silently convert the Table 3 unit to mg/L or overwrite the range. If 80–240 was intended to be mg/L, the maximum feed loading at a 0.5 mg/mL (=500 mg/L) sorbent dose would be 480 mg/g; the fitted Sips q_m=533.2 mg/g is above that maximum point loading and represents an extrapolated fit relative to the table's range. If the Methods upper limit of 280 mg/L is intended, that corresponding loading ceiling is 560 mg/g. The paper does not resolve which reported range/unit should govern.

## 3. Observed removal and uptake statements

- §3.2.2 (printed pp. 7–8) reports pH-dependent removal reaching **96.6% at pH 7**. Methods give the general baseline C0 and dose but do not unambiguously pin solution volume for the pH series; do not add a derived q_e from an assumed volume.
- The same section reports **54.6% TC removal within 38 min**, with removal becoming stable only after about 15 h. The contact-time experiment explicitly uses 200 mL solution. The sentence says “Figure 4f,” but Figure 4's caption maps contact time to panel **(e)** and different-pollutant tests to panel **(f)**. Treat this as an internal figure-panel cross-reference error; the 54.6% result is preserved as a text-reported contact-time result, not as an inference from the mislabeled panel.
- §3.2.2 also states that equilibrium q_e reaches approximately **700 mg/g at low dosage**. The exact low-dose C0, solution volume and mass are not tied together in the text sufficiently to perform a reliable mass-balance check. Retain as an author-reported, condition-incomplete q_e statement; exclude it from condition-matched capacity ranking.

## 4. Kinetic and isotherm model outputs

Table 1 (printed pp. 9–10):
- PFO fitted q_e = 335.4 mg/g, k = 0.03 min−1, R² = 0.940.
- PSO fitted q_e = 364.8 mg/g, v0 = 14.31 mg/g/min, R² = 0.992.
- Elovich R² = 0.975; intraparticle-diffusion stages have R² = 0.973, 0.974 and 0.913.

Table 2 (printed pp. 11–12), at 298/308/318 K:
- Langmuir q_m = 430.7 / 472.7 / 501.1 mg/g (R² = 0.977 / 0.983 / 0.992).
- Freundlich R² = 0.919 / 0.923 / 0.901.
- Sips q_m = 455.9 / 511.6 / 533.2 mg/g (R² = 0.977 / 0.988 / 0.996).

The Sips model is the best-fitting of the three reported models; **533.2 mg/g at 318 K is a fitted q_m**, not directly observed qe. The PFO/PSO qe values are kinetic-model outputs, not observed equilibrium uptake. The high PSO R² does not establish chemisorption. Keep the source-reported low-dose q_e≈700 mg/g distinct from all fitted model outputs.

## 5. Characterization and mechanism interpretation

The study reports SEM/EDS, XRD, BET, FTIR and TGA characterization. The composite has BET surface area 807.30 m²/g and reported pore volume 0.43 cm³/g, with pore-size modes around 1.18 and 1.58 nm. The text describes before/after-TC FTIR and reports disappearance of a carbonyl peak near 1715 cm−1 after adsorption.

Authors propose pore filling, Cu2+/Zr4+ complexation, π–π stacking, hydrogen bonding and electrostatic repulsion. The pH discussion says TC is predominantly neutral in the pH region around 7 and argues electrostatic repulsion is reduced near the optimum. The FTIR change, surface characterization and pH response provide supportive evidence for multiple possible interactions, but do not quantify individual contributions or prove a unique/dominant pathway.

**Mechanism grade: M2 — characterization and condition-response supportive, non-exclusive.** Do not promote the authors' PSO/thermodynamic interpretation into proof of chemisorption. The paper's positive ΔH (31.6 kJ/mol), PSO fit and FTIR band change are complementary evidence, not a direct bond-energy measurement or force partition.

## 6. Practical-feasibility boundary

The full article reports no real-water or wastewater matrix experiment, no verified adsorption–desorption regeneration protocol or multicycle reuse data, and no quantified process cost, product yield, synthesis energy, solvent recovery or cost per mass/volume treated. The process involves modified-Hummers GO (method referenced but not repeated in this paper), sodium alginate, 0.3 M CuSO4 crosslinking, ZrOCl2·8H2O, benzoic acid, H4TCPP, DMF, ultrasound, hydrothermal processing, centrifugation, repeated DMF/acetone washing and vacuum drying/activation. These steps are process burdens, not a quantified cost analysis.

## 7. Repository propagation

Updated existing records without creating a duplicate evidence ID:
- `data/semester-mechanism-evidence-matrix.csv`: retained/clarified SEM-049 M2 evidence and boundaries.
- `evidence/semester-paper/SEMESTER_CORE_EVIDENCE_EXTRACTION.csv`: added verified Methods/Table/Figure distinctions and Figure 4 caption error.
- `data/semester-evidence-readiness-audit.csv`: corrected permitted use and recorded missing cost/reuse evidence.
- `data/semester-condition-labelled-comparison.csv`: added condition-labelled row; removal, low-dose qe and fitted parameters remain distinct.
- `data/semester-remaining-work-register.csv`: source audit closed; citation selection/key remains pending.
- `data/semester-paper-candidate-register.csv`: updated disposition and next action.
- `data/semester-study-inclusion-shortlist.csv`: updated numeric-use rule and source caveats.
- `README.md`: comparison count updated to 30 rows.

## 8. Citation status

The latest uploaded `full ++ check again(1).bib` export was searched directly for DOI 10.3390/nano12172897; no exact DOI match was found. The candidate's citation-linkage row likewise records no exact DOI/title match in the 173-entry export. No citekey was guessed and no manuscript citation was inserted. SEM-049 remains a candidate/evidence record until selected and an actual Zotero Better BibTeX key is available.

Journal quartiles were not consulted or used.
