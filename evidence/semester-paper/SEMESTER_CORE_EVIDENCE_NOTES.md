# Semester paper — core evidence extraction notes

**Scope:** Selected graphene-based adsorbents and selected graphene-bearing composites for ciprofloxacin (CIP) and tetracycline (TC).  
**Extraction date:** 28 October 2026 (Asia/Kolkata).  
**Purpose:** First source-grounded evidence extraction from accessible primary-paper full text or indexed full-text sections. This is not yet the final included-study set.  
**Data file:** [SEMESTER_CORE_EVIDENCE_EXTRACTION.csv](SEMESTER_CORE_EVIDENCE_EXTRACTION.csv)

## Extraction standards used

- Each result remains linked to its candidate ID, DOI, source location, units, and conditions.
- Fitted qmax, measured qe, percent removal, model-predicted qe and reuse-cycle removal are stored separately.
- “Not reported in extracted sections” is not silently converted into “the study never reported it.”
- Cost statements from authors are recorded as claims unless the paper gives a cost inventory, currency/year, energy/reagent quantities, yield, process boundary, and a meaningful denominator such as cost per mass of antibiotic removed.
- A paper remains provisionally eligible until the data and full-text screening audit is complete. Abstract-only extraction is explicitly labelled.

## EV-SEM-001 — GO nanoparticles / TC (2013)

**Primary source:** Ghadim et al., *Adsorption properties of tetracycline onto graphene oxide: equilibrium, kinetic and thermodynamic studies*, DOI [10.1371/journal.pone.0079254](https://doi.org/10.1371/journal.pone.0079254); [full-text record](https://pmc.ncbi.nlm.nih.gov/articles/PMC3841164/).

**Extracted:** batch formulations, pH and contact conditions, 15-minute kinetic equilibrium, fitted Langmuir qmax 322.43 mg/g at 298 K (abstract rounds to 323), plus the release result (up to 99.8%). The paper’s modeled/author-interpreted mechanism includes π–π and cation–π interaction and hydrophobic/dispersion effects.

**Audit point:** Different sub-experiments use different pH and solution formulations. Do not treat the fitted qmax as the observed qe at a selected initial concentration. Release is not proof of durable reuse over several adsorption cycles. Quantified cost evidence has not been established.

**Primary-source QA addendum (checked 30 October 2026):** Table 2 was re-opened in the publisher's full HTML and its values are confirmed as printed: Langmuir-fitted q_m = 322.43±1.25 mg/g at 298 K, 101.87±1.08 mg/g at 303 K and 73.53±0.55 mg/g at 308 K (R² = 0.997, 0.993 and 0.998). Table 2 also reports D–R-model q_m = 24.62±0.74, 22.92±0.59 and 24.94±0.61 mg/g at those temperatures; these are different model parameters and must not be conflated with Langmuir q_m or observed uptake. The unresolved caveat is not a transcription error: Methods and Figure 6 caption specify isotherms at 298, 303 and 308 K, but the Results paragraph describing constants says 298, 303, 308, 310 and 313 K; Table 2 contains only three temperature rows. The same article's thermodynamic discussion calls adsorption endothermic from positive ΔH°, while the reported Langmuir q_m falls sharply from 298 to 308 K. Preserve both source statements without correcting either or inferring the missing 310/313 K parameters. Use the 298 K fitted value only as a clearly labelled baseline, not as a universal rank or observed q_e. PLOS full-text sections checked: isotherm Methods; Results isotherm paragraph; Figure 6 caption; Table 2; Table 3/thermodynamic discussion. The DOI is not in the current 173-entry user-supplied Better BibTeX export, so its citation key remains unresolved for manuscript insertion.

## EV-SEM-002 — GO/calcium-alginate fibers / TC (2018)

**Primary source:** *Adsorption of tetracycline antibiotics from an aqueous solution onto graphene oxide/calcium alginate composite fibers*, DOI [10.1039/C7RA11964J](https://doi.org/10.1039/C7RA11964J); [full-text record](https://pmc.ncbi.nlm.nih.gov/articles/PMC9077392/).

**Extracted:** freeze-dried GO/CA fibers cross-linked with CaCl2; 25 mg adsorbent in 50 mL for equilibrium experiments at 25°C over 5 h; observed qe of 17.6 mg/g at C0 10 mg/L and 65.4 mg/g at C0 60 mg/L; highest reported removal in the pH experiment was 56.8% at pH 6; fitted Langmuir qmax = 131.6 mg/g (R² 0.9938).

**Audit point:** The paper's fitted qmax and measured qe at specific starting concentrations must be reported separately. Freeze-drying is a preparation step but no quantified energy/cost inventory has been extracted. A multi-cycle regeneration result was not found in the sections extracted.

## EV-SEM-003 — MnFe2O4/rGO / TC (2018)

**Primary source:** *Adsorption of Tetracycline with Reduced Graphene Oxide Decorated with MnFe2O4 Nanoparticles*, DOI [10.1186/s11671-018-2814-9](https://doi.org/10.1186/s11671-018-2814-9); [open full-text record](https://pmc.ncbi.nlm.nih.gov/articles/PMC6281545/).

**Extracted:** one-step MnFe2O4/rGO preparation; about 41 mg/g uptake reported at initial TC 10 mg/L; near-equilibrium around 8 h; pH optimum reported at 3.3; 0.1 M HCl elution and re-use performance declining from 86% initial removal to reported 85%, 82%, 79%, and 71%.

**Audit point:** Check precise cycle numbering from Figure 6 before manuscript use. Although magnetic recovery is an operational benefit, measured synthesis cost and acid-waste burden are not available in the extracted evidence.

## EV-SEM-004 — Zn–C battery-derived GO / CIP (2024; primary-source consistency audit)

**Primary source:** Yasmin et al., *Efficient removal of ciprofloxacin from aqueous solution using Zn-C battery derived graphene oxide enhanced by hydrogen bonding, electrostatic and π-π interaction*, DOI [10.1016/j.heliyon.2024.e33317](https://doi.org/10.1016/j.heliyon.2024.e33317); [open full-text article](https://pmc.ncbi.nlm.nih.gov/articles/PMC11253669/). Official supplementary document [mmc1.docx](https://pmc.ncbi.nlm.nih.gov/articles/instance/11253669/bin/mmc1.docx) was also inspected; it contains DFT/computational geometry and orbital data, not additional adsorption-volume or experimental uptake reconciliation.

**Material preparation (Methods §§2.3–2.4):** Carbon rods from spent Zn–C batteries were washed, dried at 60°C for 24 h, crushed, treated with HCl:HNO₃ (3:1) at 60°C for 2 h, washed and dried another 48 h at 60°C. GO synthesis used 1.0 g recovered graphite, H₂SO₄:H₃PO₄ (9:1 v/v), 6 g KMnO₄ at 50°C for 12 h, then 400 g ice and 3 mL of 30% H₂O₂; the product was centrifuged and repeatedly washed with water, 30% HCl, water and ethanol, then vacuum-dried at 45°C for 48 h. No GO yield, reagent recovery, process energy or normalized cost inventory is reported. Waste-derived graphite does not alone establish low total process cost.

**Reported optimum:** Abstract/Fig. 3 and §§3.6.2–3.6.3 report 99.0% CIP removal at C₀=2.0 mg/L, GO dose=20 mg/L, pH 5.7, 20 min, 30°C and 230 rpm. Methods §2.5 states that each experiment used 40 mL CIP solution. Thus, on the stated condition, initial CIP mass=2 mg/L × 0.040 L=0.08 mg, while GO mass=20 mg/L × 0.040 L=0.8 mg. If 99.0% removal is applied to these conditions, removed CIP=0.0792 mg and the calculated qe is 0.0792 mg/0.0008 g=**99 mg/g**.

**Same-condition discrepancy:** Fig. 5's caption identifies the kinetic test with C₀=2.0 ppm, GO=20 mg/L, pH 5.7, 230 rpm and 30°C. Table 4/§3.6.6 gives an experimental kinetic qe=78.82 mg/g and pseudo-second-order fitted qe=79.36 mg/g (linear R²=1.0000; nonlinear R²=0.8584). With the same 40 mL, 2 mg/L and 20 mg/L dose basis, experimental qe=78.82 mg/g corresponds to 0.063056 mg CIP removed and **78.82% removal**, not 99%; the fitted qe corresponds to 79.36% removal. The difference between the 99% headline and the experimental kinetic qe is **20.18 percentage points** on that implied basis. The primary text does not reconcile these outputs. Preserve both author-reported values and the calculated mismatch; do not silently change either.

**Independent dosage-unit conflict:** Abstract, Fig. 3 captions and §3.6.3 state 20 mg/L GO, but §4 Conclusion calls the dosage **20 g/L**, a 1000-fold difference. This cannot be resolved from the main article or supplementary DOCX; do not assume the conclusion is a confirmed typo or use its unit as a corrected basis.

**Metric/model distinction:** Table 1 reports nonlinear Langmuir fitted qₘ values of 419.62, 434.56 and 441.44 mg/g at 30, 40 and 50°C (R²=0.9800, 0.9844 and 0.9814); linear Langmuir qₘ values are 400.00, 416.67 and 434.78 mg/g. These are isotherm-fit asymptotes from a separate concentration series, not observed uptake at the 2 mg/L optimum. Table 4 also shows substantial PFO fit sensitivity: linear qₑ=3.26 mg/g (R²=0.4363) versus nonlinear qₑ=77.99 mg/g (R²=0.5500). PSO qₑ=79.36 mg/g is a fitted kinetic value, not qₘ. Do not merge fitted capacities, kinetic qₑ and percent removal.

**Recovery and cost:** No multicycle adsorption–desorption test or cycle-specific reuse result was verified in the main text. Although the authors describe battery-waste-derived GO as economical, there is no normalized cost, material yield, reagent-recovery inventory, energy consumption or cost per mass CIP removed. Preparation includes strong acids, KMnO₄, H₂O₂, repeated acid/water/ethanol washing and long drying.

**Evidence-use rule:** The material/preparation and proposed electrostatic, hydrogen-bonding and π–π interaction discussion may be used with source attribution. The 99.0% removal result should only be quoted as an author-reported headline with the same-condition kinetic-qₑ conflict stated. Do not use this study as a condition-matched quantitative performance benchmark until values are reconciled. Keep the 419.62 mg/g fitted Langmuir qₘ separate from the kinetic experiment.
## EV-SEM-005 — GO–ZnAlNi LDH / CIP (2025)

**Primary source:** Sikri et al., *Graphene oxide/layered double hydroxide composite as highly efficient and recyclable adsorbent for removal of ciprofloxacin from aqueous phase*, DOI [10.3389/fnano.2025.1578620](https://doi.org/10.3389/fnano.2025.1578620); [full article](https://www.frontiersin.org/journals/nanotechnology/articles/10.3389/fnano.2025.1578620/full).

**Extracted:** batch tests used 20 mL, 0.225–10 mg/L CIP, composite dose 1–12 mg/L, pH 3–11, and 0–4 h contact at 180 rpm. The paper reports 84.84% removal at C0 1 mg/L, composite dose 10 mg/L, pH 7 and 60 min. Reuse results decline from 80.4% removal at cycle 1 to 27% at cycle 5. Freundlich R² is reported as 0.95, better than Langmuir; Temkin R² is 0.90.

**Critical audit point (primary text checked 30 October 2026):** The Methods section defines adsorption capacity as q_t=(C_0−C_t)V/W and gives a 20 mL batch volume. For C_0=1 mg/L, composite dose=10 mg/L, pH 7, and reported removal=84.84%, the equation implies a derived q_e≈84.84 mg/g; the feed-mass ceiling under that concentration/dose basis is 100 mg/g. Yet §3.2.1 separately pairs 84.84% removal with 97.43 mg/g, Table 1 gives pseudo-first-order fitted q_e=106.96 mg/g (R²=0.949), the abstract gives 106.97 mg/g, and Table 3 lists 106.9 mg/g for the headline low-concentration condition. The 106.96/106.9 values exceed the feed-mass ceiling if they refer to the same stated conditions; because Table 1 is a fitted kinetic endpoint, do not label it observed q_e or q_max. The paper reports Freundlich as its best isotherm fit (R²=0.95) and says Langmuir does not fit significantly. The source does not resolve the discrepancies, so retain the 84.84% removal as the usable endpoint and hold all capacities pending raw-data/author clarification. Five-cycle removal declines from 80.4% at cycle 1 to 27% at cycle 5, which tempers the article’s positive characterization of recyclability. The article itself says real-water/scale-up and techno-economic/life-cycle work are needed; do not describe this synthetic aqueous batch test as real-wastewater validation.

## EV-SEM-006 — magnetic GO/fibrillated cellulose / TC (2025)

**Primary source:** Dang et al., *Integration of magnetic graphene oxide and office waste paper-derived fibrillated cellulose into a composite adsorbent for effective tetracycline elimination*, DOI [10.1039/D5RA00877H](https://doi.org/10.1039/D5RA00877H); [full article](https://pubs.rsc.org/en/content/articlehtml/2025/ra/d5ra00877h).

**Extracted:** M-GO/PFC composite; batch dose tests at C0 TC 70 mg/L and contact 960 min, with observed qe 93.36 ± 3.85 mg/g at 0.50 g/L and 59.52 ± 0.11 mg/g at 1.17 g/L; optimum pH for subsequent tests was 5. Sips fitted qm = 130.11 mg/g (R² 0.988), while the Langmuir fitted value was 107.06 mg/g (R² 0.916). The pseudo-second-order model predicts qe 87.74 mg/g (R² 0.997). Five-cycle removal decreases from 88.33% to 75.38%.

**Cost relevance:** The methods use modified-Hummers GO synthesis, magnetite functionalization, 5% NaOH, 2% NaClO, 40% H2SO4 cellulose hydrolysis, 360 W ultrasonication and 48 h lyophilization at −40°C. The paper emphasizes low-cost waste paper, but a quantified whole-process cost/energy inventory was not found in the extracted article sections. The preparation burden is therefore a real unresolved part of the “low-cost potential” question.

## EV-SEM-007 — CMC-functionalized magnetic GO / TC (2025)

**Primary source:** *Carboxymethylcellulose functionalized magnetic graphene oxide for the efficient removal of tetracycline from aqueous media*, DOI [10.1039/D5RA06621B](https://doi.org/10.1039/D5RA06621B); [full-text record](https://pmc.ncbi.nlm.nih.gov/articles/PMC12458999/).

**Extracted:** reported TC removal 96.04% in 25 min at pH 5 and dose 0.1 g/L; Langmuir fitted qmax 54.73 mg/g; saturation magnetization 50.69 emu/g; reuse reportedly changes removal from roughly 96% to 92% after ten cycles.

**Audit point:** The initial TC concentration and exact eluent/protocol conditions for ten-cycle regeneration have not been captured in this pass. The PMC web interface limited direct line-by-line access, so verify full methods and supplementary information before treating this as completed full-text extraction. The pseudo-second-order fit is not proof of chemisorption.

## EV-SEM-008 — DTPA-functionalized magnetic GO / CIP + TC (2018; primary full-text audit)

**Primary source:** Li et al., *Performance of magnetic graphene oxide/diethylenetriaminepentaacetic acid nanocomposite for the tetracycline and ciprofloxacin adsorption in single and binary systems*, DOI [10.1016/j.jcis.2018.03.003](https://doi.org/10.1016/j.jcis.2018.03.003); [PubMed record](https://pubmed.ncbi.nlm.nih.gov/29567603/); [university-hosted 10-page full text PDF](https://ee.hnu.edu.cn/__local/7/00/07/132D7E46F401B025BF92B18714F_758970B3_2B3DCB.pdf).

**Synthesis (Methods §2.2, printed p. 152):** The main PDF reports DTPA functionalization of magnetic GO using 0.8 g DTPA, 0.4 g EDC and 0.4 g NHS in low-concentration ammonia for 2 h at room temperature, followed by 40 mL diethylenetriamine and 2 g MGO stirred at 80°C for 6 h. The material was rinsed repeatedly with Milli-Q water to about neutral pH. Material yield, reagent recovery and process-cost/energy inputs are not reported in the accessible text.

**Kinetic test conditions (Methods §2.4 and Fig. 3, printed pp. 152–153):** 25 mL conical flasks, 150 rpm, approximately 2.28 mg DDMGO per reaction (about 0.09 g/L), C₀=50 mg/L for each single-antibiotic test, pH 3.0, 30°C; kinetic contact-time range 0–1560 min. The text reports CIP uptake approaching equilibrium after about 1 h, while TC uptake continues increasing and plateaus near 24 h. The caption states C₀=50 mg/L, m/V=0.09 g/L, 30°C and pH 3.0 for Fig. 3.

**Kinetic parameter identity and mass-balance screen:** The main text (§3.2) explicitly identifies 294.12 mg/g (TC) and 111.73 mg/g (CIP) as (q_e) values calculated from the pseudo-second-order equation; both PSO (R^2) values are stated to exceed 0.99. They are **model-fitted kinetic (q_e)**, not Langmuir (q_{max}) or directly tabulated experimental (q_e). At C₀=50 mg/L and m/V=0.09 g/L, the complete-removal mass-balance ceiling is (50/0.09=555.6) mg/g. Both fitted values fall below this ceiling; no mass-balance impossibility is indicated by these values. The text says equilibrium data fit Freundlich better than Langmuir; exact kinetic and isotherm parameter tables are in cited Supporting Information Tables S1–S3, which were not included in the retrieved 10-page main PDF.

**Provisional cross-figure QA flag (not a confirmed contradiction):** A text-layer extraction of the plotted values suggests the Fig. 3 kinetic endpoint for CIP at pH 3 is around 111–114 mg/g, while the Fig. 5 pH-response value at pH 3 appears around 86 mg/g at 24 h; corresponding TC points appear similar, around 290 mg/g. The base concentration, dose, temperature and pH are nominally the same, and the paper says CIP reaches equilibrium after ~1 h, so this difference is worth checking. However, these values were extracted from plots rather than transcribed from a numerical source table, and the browser screenshot route did not render the PDF. Therefore **do not treat this as a confirmed source contradiction or use the pH-3 CIP point in matched numerical comparison until the figures/SI can be visually checked**. No value was silently corrected.

**Regeneration and cost:** Methods §2.4 reports four adsorption–desorption cycles using 0.01 M NaOH, with single 50 mg/L solutions or binary 50/10 mg/L pairs, 250 mL suspension, about 22.8 mg adsorbent, 24 h, 30°C and pH 3.0. Cycle-by-cycle retention was not verified from the extracted text. No normalized cost/yield/energy inventory was found; magnetic separation is an operational advantage, not proof of low total cost.

**Evidence-use rule:** retain the two PSO (q_e) values only as model-derived kinetic parameters with the Fig. 3 test conditions. Do not use them as (q_{max}) or directly measured uptake, and keep the provisional Fig. 3/Fig. 5 CIP flag out of numerical ranking pending figure/SI verification.

## Cross-study conclusions that are safe at this stage

1. Several candidate materials show high uptake or removal in particular laboratory conditions, but those values are not directly rankable across different initial concentrations, doses, pH, times and isotherm models.
2. Magnetic attachment can simplify recovery; it does not by itself establish lower total cost or low leaching risk.
3. GO-based material and composite preparation may include multi-step chemistry, strong reagents, ultrasonication or freeze-drying. A waste precursor does not prove low total manufacturing cost.
4. Reuse evidence varies. Some reported five-cycle profiles look fairly stable, while the GO–ZnAlNi LDH study falls to 27% removal by cycle 5. Each reuse protocol must be captured exactly.
5. The evidence base remains provisional; journal quartile verification, complete full-text screening and remaining-candidate deduplication are separate tasks.

## Next actions

- Obtain the full text for EV-SEM-008 (Li et al., 2018) and extract numerical CIP/TC data.
- Verify detailed experimental conditions and supplementary results for EV-SEM-007 (CMC-functionalized magnetic GO).
- Reconcile the GO–ZnAlNi LDH capacity inconsistency against the article’s figures and equations.
- Continue screening the remaining candidate register; do not infer that 8 records equals 8 final eligible references.
- Add full-text source-page citations to the eventual manuscript and keep the evidence database as the traceable source of truth.


## Superseding audit corrections — 29 October 2026

This section supersedes earlier shorter summaries for EV-SEM-005, EV-SEM-007 and EV-SEM-008 above.

### EV-SEM-007 — CMC-functionalized magnetic GO: detailed conditions and model temperatures

The full open-access RSC article is available at [DOI 10.1039/D5RA06621B](https://doi.org/10.1039/D5RA06621B). Base-condition tests use C0(TC)=2 mg/L, 2 mg sorbent in 20 mL (0.1 g/L), pH 5, 25°C, 250 rpm and 25 min. At the reported 96.04% removal, the mass-balance-derived uptake is 19.208 mg/g; this is calculated from the reported removal and dose and is not a directly quoted observed qe.

The reported Langmuir capacities depend on fitting method and temperature. Linear Langmuir qm: 45.5581 mg/g (25°C), 51.4933 mg/g (40°C), 54.7346 mg/g (50°C). Nonlinear Langmuir qm: 44.0051, 48.6490 and 48.4744 mg/g at those temperatures. The article’s 54.73 mg/g headline value corresponds to the linear fit at 50°C, not to the 25°C optimum-removal test. Model-fitted qe values (around 19.35–19.50 mg/g) also remain model estimates.

The regeneration method is magnetic separation followed by methanol treatment. The article reports reuse through ten cycles and a reduction in removal from about 96% to 92%. A quantified cost inventory is absent. Preparation inputs documented in Methods include aqua-regia cleaning of graphite recovered from spent lithium-ion batteries; modified-Hummers oxidation with concentrated H2SO4/H3PO4, KMnO4 and H2O2; HCl, water and ethanol washing; 80 mg GO plus 80 mg CMC; 2.781 g FeSO4·7H2O and 7.998 g Fe2(SO4)3·7H2O; 2.0 M NaOH to about pH 11; 85°C stirring for 2 h; and vacuum drying at 60°C for 18 h. These burdens should be recorded as preparation inputs, not converted into a monetary cost without prices/yield/system boundary.

### EV-SEM-005 — GO–ZnAlNi LDH: capacity claims fail a mass-balance consistency check

The primary article is available at [DOI 10.3389/fnano.2025.1578620](https://doi.org/10.3389/fnano.2025.1578620). Its Methods give q=(C0−Ct)V/W. At C0=1 mg/L and dose=10 mg/L, 84.84% removal implies qe=84.84 mg/g, if those reported values refer to the same experiment and dose basis.

Yet the article’s narrative reports 97.43 mg/g with the 84.84% removal condition, while its abstract and Table 3 state 106.97/106.9 mg/g. Other dose-series pairs are also inconsistent with the equation: 64% removal at 7.5 mg/L dose implies about 85.33 mg/g, not 88.89 mg/g; 73.86% removal at 12 mg/L dose implies about 61.55 mg/g, not 77.95 mg/g. The article’s Table 2 reports Freundlich and Temkin parameters; it does not provide a clear, verified Langmuir qm in that table.

**Decision:** Keep 84.84% removal at C0=1 mg/L, dose=10 mg/L, pH 7 and 60 min as a reported condition-specific outcome. Mark capacity unresolved and do not publish a single authoritative capacity value until the source data/calculation is reconciled. The study’s five-cycle removal reportedly declines from 80.4% to 27%, which should be reported alongside any reuse claim.

The methods also document reagent-intensive processing: Zn/Al/Ni nitrate precursors, 3.4 M NaOH, modified-Hummers GO, one-hour ultrasonication, hydrothermal aging at 120°C for 16 h, water/ethanol washing, and drying at 70°C. The article itself notes that techno-economic and life-cycle evaluation is needed to substantiate economic claims.

### EV-SEM-008 — DTPA-functionalized magnetic GO: distinguish secondary leads from primary evidence

A university-hosted PDF of Li et al. (2018), DOI [10.1016/j.jcis.2018.03.003](https://doi.org/10.1016/j.jcis.2018.03.003), was located, but the browser retrieval timed out and the numerical results tables could not be verified in this extraction session. The primary abstract confirms TC and CIP were tested separately and in binary systems; it reports Freundlich fits, pseudo-second-order kinetics, different thermodynamic signs for TC versus CIP, stronger competition effects on TC, and good reusability.

Secondary reviews report DDMGO capacities of 294.12 mg/g for TC and 111.73 mg/g for CIP. One secondary table lists a 50 mg/L adsorbate concentration and 1440 min contact time, but its adsorbent-dose notation is ambiguous. These are **retrieval clues only**. They must not enter the final primary-study evidence table until checked against Li et al.’s original tables/figures and exact conditions. The immediate action is to retrieve the full paper through university library access or an author copy.



## Third evidence batch — new CIP anchors and a cost-relevant column study (29 October 2026)

### EV-SEM-009 — GO for CIP in aqueous medium and fresh synthetic urine (2024)

**Primary source:** Bruckmann et al., DOI [10.1016/j.cej.2024.150484](https://doi.org/10.1016/j.cej.2024.150484); [publisher record](https://www.sciencedirect.com/science/article/pii/S1385894724019715).

Indexed primary text reports maximum capacities of 354.24 mg/g in aqueous medium at pH 5 and 291.39 mg/g in fresh synthetic urine at pH 6. The study analyzes conventional adsorption models and statistical-physics models and concludes that general-order kinetics describe the kinetic data well. The exact initial concentration, GO dose, contact time and precise capacity-model definition for these headline values still need table-level verification. Fresh synthetic urine must not be described as real urine or wastewater.

### EV-SEM-010 — magnetic guar-gum/GO nanocomposite for CIP (2023; capacity/condition audit)

**Official publisher record:** Saya, Singh & Hooda, *Adsorptive removal of ciprofloxacin from aqueous medium by magnetic guar gum grafted graphene oxide nano composite*, *Journal of Environmental Chemical Engineering* 11 (2023), 110766, DOI [10.1016/j.jece.2023.110766](https://doi.org/10.1016/j.jece.2023.110766); [ScienceDirect record](https://www.sciencedirect.com/science/article/abs/pii/S2213343723015051). The official publisher preview confirms the title, authors, 555.56 mg/g headline and model types. Detailed methods/tables below were extracted from a [third-party 14-page text mirror](https://www.scribd.com/document/1043011820/1-s2-0-S2213343723015051-main), which reproduces the publisher-formatted article but is not publisher-hosted. Treat details derived only from the mirror as provisional pending publisher/author-hosted full text.

**Material and preparation (mirror §§2.2–2.3):** The authors report a two-step approach: improved-Hummers graphene oxide followed by magnetic guar-gum/GO nanocomposite formation by co-precipitation. The mirror's GO route starts with 1.0 g graphite flakes and 25 mL 98% H₂SO₄ below 5°C; after 2 h stirring, 3 g KMnO₄ is added and the mixture stirred at 40°C, diluted and further stirred, then quenched/wash-centrifuged. For the composite, 2 mg GO in 10 mL DI water is ultrasonicated for 1 h and mixed with 2 mg guar gum in 50 mL water; separate 25 mL aqueous FeCl₂ and FeCl₃ solutions (reported 2:1 molar ratio) are used, and ~3 mL ammonia is added dropwise to precipitate magnetic Fe₃O₄ with the composite. The product is magnetically separated, washed to neutral pH, vacuum-dried and powdered. This detailed procedure is from the nonofficial mirror, not an official publisher PDF.

**Condition-basis issue:** The mirrored methods state a general/optimized setup of 10 mL CIP solution at 3 mM with 5 mg mGG/GO NC, pH 7.1 and 298 K. This equals 0.5 g/L adsorbent; 3 mM CIP is about 994 mg/L. The same paper's dosage-response section says uptake capacity increases up to 5 g/L and decreases beyond that—10 times the general 0.5 g/L basis. The text does not clearly reconcile whether the two values refer to different experimental subsets or which dose applies to the isotherm parameter. Do not silently choose one. The separate concentration-response/isotherm series is reported as C₀=100, 300, 500 and 700 mg/L at pH 7.1 and 298/313/323 K.

**Capacity and model parameters:** The publisher highlights report a maximum adsorption capacity of 555.56 mg/g. The mirrored Table 2 identifies 555.56 mg/g as **Langmuir-fitted (q_{max})**, with (K_L=0.0173) L/mg and (R^2=0.9915); it is not a directly tabulated observed (q_e). The body text separately states Langmuir (R^2=0.9989), while the table gives 0.9915. Because the paper discusses linear fits and a combined nonlinear fit, this may reflect different fit forms, but the text/table do not clearly map the values in the relevant sentence; retain both without asserting a definite contradiction. The mirrored text describes uptake around 560 mg/g at C₀=700 mg/L. Since the isotherm-specific adsorbent dose is not unambiguously pinned against the 0.5 vs 5 g/L discrepancy, a condition-specific mass-balance check of (q_{max}) is incomplete.

**Kinetics:** Mirrored Table 1 gives pseudo-second-order fitted (q_e=38.7596) mg/g, (k_2=0.000979) g mg⁻¹ min⁻¹, (R^2=0.9961); pseudo-first-order fitted (q_e=26.15) mg/g, (k_1=0.0055) min⁻¹, (R^2=0.8544); intraparticle diffusion (k_{IPD}=1.7547) mg g⁻¹ min⁻½, intercept 7.5976 mg/g, (R^2=0.8706). Keep the kinetic-model (q_e) separate from Langmuir (q_{max}). These exact values are from the third-party text mirror and remain provisional pending official table verification.

**Regeneration and mechanism:** Mirror §4.5 reports six adsorption–desorption cycles. After adsorption to equilibrium, material is magnetically separated, desorbed in 1% ethanol for 3 h at room temperature, washed with distilled water to neutral pH and dried. The authors state removal efficiency remains around 95% after the sixth cycle. The publisher abstract/mirror attribute uptake to combined electrostatic/Coulombic interactions, hydrogen bonding, hydrophobic interactions and π–π/electron-donor–acceptor interactions; treat these as authors' mechanism interpretation rather than quantitatively separated contributions.

**Cost and applicability:** No normalized cost per kg of sorbent, cost per mass of CIP removed, synthesis yield, reagent-recovery inventory or energy inventory was found. The process uses concentrated sulfuric acid, KMnO₄, iron salts, ammonia, multiple washes and drying; magnetic separation is an operational advantage but not evidence of low total cost. Do not infer real-wastewater validation from the publisher abstract's broad wastewater framing.

**Evidence-use rule:** Do not describe 555.56 mg/g as observed uptake; it is Langmuir-fitted (q_{max}). Keep it out of condition-matched ranking until the exact isotherm dose and fit-form statistics can be verified from an official or author-hosted full text. Preserve the unresolved 0.5 vs 5 g/L dosage statements and the prose/table (R^2) difference without inventing corrections.
### EV-SEM-011 — sodium alginate/GO hydrogel beads for PRB application (2018)

**Primary source:** Zhao et al., DOI [10.1016/j.chemosphere.2018.02.157](https://doi.org/10.1016/j.chemosphere.2018.02.157); [PubMed record](https://pubmed.ncbi.nlm.nih.gov/29510369/).

The primary abstract reports GSA hydrogel beads used as permeable reactive barrier backfill for ciprofloxacin-contaminated groundwater, maximum capacity 100 mg/g at pH 7, pseudo-second-order kinetics, and flow-through column tests varying flow rate, influent concentration and ionic strength. The abstract says PRB lifetime and cost were calculated, making this a high-priority source for the practical-feasibility section. It also contains a model-description conflict: the abstract says the isotherm follows Freundlich but attributes the 100 mg/g maximum capacity to Langmuir. The source full text must resolve this; cost values, column parameters, lifetime assumptions and model table must be extracted before use.



## Fourth evidence update — primary indexed full text for DDMGO and PRB (29 October 2026)

### EV-SEM-008 / SEM-006 — Li et al. (2018), DDMGO for both TC and CIP

The institutional PDF search index exposed substantial primary-text content at [the Hunan University-hosted PDF](https://ee.hnu.edu.cn/__local/7/00/07/132E7D46F401B025BF92B18714F_758970B3_2B3DCB.pdf). Direct browser retrieval timed out and the screenshot tool could not resolve the PDF as an application/pdf resource, so the text is extracted from search-indexed primary content rather than visual page-image review. This constraint is important: numeric tables/figures are not considered fully audited.

**Confirmed primary methods:** 25 mL conical flasks, 150 rpm, about 2.28 mg DDMGO per reaction; pH experiments at 50 mg/L and 30°C; kinetics at 50 mg/L, 30°C and 0–1560 min; isotherms over initial concentrations 0–500 mg/L at pH 3.0 and 293/303/313 K; NaCl effects 0–0.5 M; foreign ions K+, Mg2+, Cl−, SO4²− at 0–0.1 M; binary competition tests with 50 mg/L target plus 0–20 mg/L co-antibiotic; four successive adsorption/desorption cycles using 0.01 M NaOH. Equilibrium tests used approximately 24 h at 30°C and pH 3.

**Confirmed kinetic observations:** CIP sorption reached equilibrium after about one hour, whereas TC continued increasing until roughly 24 h. The paper explicitly says the 294.12 mg/g (TC) and 111.73 mg/g (CIP) values are (q_e) calculated from the pseudo-second-order equation and closer to experimental values. They are therefore kinetic-model-fitted (q_e), **not Langmuir (q_{max})**. The equilibrium data are described as fitting Freundlich better. The exact measured experimental (q_e), kinetic R²/rate constants, isotherm parameters, binary-competition effect sizes and cycle-by-cycle regeneration retention still need transcription from the actual tables/figures.

**Additional material characterization:** DDMGO BET surface area 176 m²/g, mean pore diameter 3.8 nm and pore volume 0.24 cm³/g; indexed FTIR text indicates DTPA amino groups react with GO carboxyl groups to form amide bonds. Magnetic separation is supported by Fe3O4 characterization. Cost was not quantified. Preparation uses GO oxidation, Fe3O4 functionalization and DTPA coupling (EDC/NHS listed among reagents); no total cost/energy inventory is available.

### EV-SEM-011 / SEM-037 — Zhao et al. (2018), GO–alginate hydrogel beads as a PRB

**Primary sources:** [PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/29510369/), [publisher indexed article](https://www.sciencedirect.com/science/article/pii/S0045653518303692), DOI 10.1016/j.chemosphere.2018.02.157.

The abstract confirms the GSA hydrogel beads were evaluated for ciprofloxacin-contaminated groundwater, in batch and flow-through columns; kinetic data were described by pseudo-second-order, equilibrium data by Freundlich, and reported capacity was 100 mg/g at pH 7.0. The paper explicitly says PRB lifetime and cost were calculated. The actual cost value, lifetime, currency/year, system boundary, column dimensions/flow rates and hydrogeological assumptions were not retrieved in this pass.

Earlier wording suggested a confirmed Freundlich/Langmuir inconsistency. This was too strong based on the verified abstract alone and is now corrected: the full text must be checked to establish how the 100 mg/g value is defined. Do not call it Langmuir qmax without source-table support.



## Fifth evidence batch — extracting existing Library PDFs (29 October 2026)

No new download or upload was requested. Instead, two PDFs already in the user's Library were fully inspected:
- `graphene 1.pdf`: Shah et al., ACS Omega 2025, sulfonated graphene oxide (SGO) for ciprofloxacin; DOI 10.1021/acsomega.4c11231.
- `graphene 2.pdf`: Li et al., Process Safety and Environmental Protection 2025, phosphorus-doped/TETA-modified GO hydrogel (PGOT@GEL) for CIP, gatifloxacin and Cu2+; DOI 10.1016/j.psep.2025.107659.

### EV-SEM-012 — SGO for CIP

The full article was read from the Library copy. It reports a Langmuir (q_m=1000.00) μmol/g, equivalent to 331.35 mg/g, with R²=0.9998 at 25°C. Table 1 reports experimental (q_e=237.12) μmol/g at initial CIP 50 μmol/L; the same nominal condition is reported as 96.53% removal in the text. Given 50 mL solution and 0.2 g/L SGO (0.01 g), 237.12 μmol/g implies ~94.85% removal by mass balance. This is recorded as a source consistency flag, not silently corrected.

Preparation uses 3.0 g graphite, a 9:1 mix of 18.4 M H2SO4 and 14.6 M H3PO4, 18.0 g KMnO4, 24 h stirring, H2O2 quench, sequential washes with 7.7 M HCl/water/ethanol/diethyl ether and drying at 60°C. The nominally high capacity should be viewed against these uncosted synthesis inputs. Regeneration uses 1 M HCl in DMF, 99.14% release within 240 min, washing to neutral pH and 100°C drying, followed by five-cycle reuse with >95.78% initial capacity retained. No monetary cost/energy inventory or yield is supplied.

This study is especially useful for the mechanism/performance table: pH optimum 4, cation-salt inhibition, FTIR/SEM/EDX and DFT interpretation. It is also a strong case study for showing why a reported “cost-effective” adsorbent may still lack a quantified process-cost case.

### EV-SEM-013 — PGOT@GEL for CIP (2025)

The full article was read from the Library copy. Material construction involves GO preparation, hypophosphorous-acid P doping, TETA grafting using EDC/NHS, β-cyclodextrin acrylation, then copolymerization with AMPS to form a hydrogel. The authors report a Langmuir (q_{max}=821.24) mg/g (R²=0.9908) and a separate RSM validation at CIP 296.52 mg/L, pH 6.70, adsorbent dosage 5.08 mg and 298.88 K, with measured uptake (q_e=807.54) mg/g versus model prediction 800.60 mg/g. A separate pH test gives (q_e=192.24) mg/g and 96.12% removal at pH 7. Equilibrium is reached around 120 min; seven-cycle removal reportedly retains about 90.53% of the initial value after methanol regeneration for 12 h/cycle.

**Critical interpretation:** The fitted qmax and RSM-verified uptake are different outputs and need their own rows in comparative tables. The article calls the matrix experiment “real water samples” in its text, while the Fig. 12 caption labels it “simulated real wastewater”; the available supplementary information is not included in the Library file. Treat as a matrix-ambiguity flag, not definitive true-wastewater validation.

**Cost finding:** Despite a large reported qmax and reuse, no numerical whole-process cost is supplied. The synthesis uses multiple reagents, surface-modification stages and polymerization. It is a valuable high-performance contrast, but cost potential remains unproven.

### Scope/evidence consequence

These two existing PDFs bring the evidence extraction table to 13 study records. They are not new user downloads and have been linked to existing candidate IDs SEM-016 and SEM-032. The remaining gaps on DDMGO and PRB are retained in the evidence as unresolved access/table-audit limitations; the project will proceed without asking the user for more PDFs.


## Cross-repository linkage — no duplicate evidence row created (29 October 2026)

The full repository review identified one additional directly in-scope paper already extracted in the broad corpus: Zhang & Wu (2022), “Adsorption Characteristics of N-rGO for Multiple Representative Trace Antibiotics in Water” (DOI 10.1002/jeq2.20415). It is now registered as SEM-038 and cross-referenced to broad-corpus candidate CORP-031. Reuse the original evidence IDs EV-B10-004–EV-B10-009 rather than copying them into a second extraction table.

**CIP/TC eligibility:** Tetracycline is one of the six target antibiotics, and N-rGO is a graphene-derived material within the approved semester scope. The article is listed as Q2 in five 2025 SJR categories in the broad audit; the semester scope does not impose a universal Q1-only rule unless the requirement is explicitly confirmed.

**Data-quality hold:** The primary evidence records flag a mass-balance/unit concern. The paper reports kinetic qe values 80.58–90.21 mg/g across the six antibiotics and a fitted Langmuir q_m of 662.25 mg/g for TC, despite a trace-concentration setup where the illustrative stated feed/dose combination implies a loading ceiling near 80 mg/g. Keep the reported values and condition labels for audit, but do not rank or reproduce the q_m as validated capacity until concentration/dose units and calculations can be reconciled.

Preparation is chemically intensive (strong acid/oxidant treatment, extensive washing/ultrasonication and 180°C/24 h autoclave processing); the existing source record reports no quantified yield, chemical recovery, energy or cost/LCA. This is useful both for adsorption-mechanism evidence and for the review's distinction between high fitted capacity and demonstrated low-cost potential.


## EV-SEM-014 — Graphene versus GAC / CIP (Zhu et al., 2015)

**Primary source:** Zhu et al., *Ciprofloxacin adsorption on graphene and granular activated carbon: kinetics, isotherms, and effects of solution chemistry*, DOI [10.1080/09593330.2015.1054316](https://doi.org/10.1080/09593330.2015.1054316); [publisher full-text page](https://www.tandfonline.com/doi/full/10.1080/09593330.2015.1054316).

**Accessible evidence used:** The publisher abstract states that graphene reached equilibrium in about 3 min and reports a Langmuir-fitted maximum capacity of 323 mg/g. It also describes pH/speciation effects, ionic strength of 0.01–0.5 mol/L, NOM at 5 mg/L, and river-water/drinking-water tests, with less adverse effect on graphene than on GAC under the tested conditions.

**Status and limitation:** The full Methods/tables/figures and supplementary material are not available in the current Library view, so this is an abstract-level extraction—not a completed paper audit. Keep 323 mg/g separate as a fitted qmax, and do not use it in a final numerical ranking until conditions and isotherm range are verified. GAC is only a clearly labelled benchmark, not part of the semester paper's core material scope. No new download request is active.

## EV-SEM-015 — CNF/GO aerogel / TC (Yao et al., 2017)

**Primary source:** Yao et al., *3D assembly based on 2D structure of cellulose nanofibril/graphene oxide hybrid aerogel for adsorptive removal of antibiotics in water*, DOI [10.1038/srep45914](https://doi.org/10.1038/srep45914); [open publisher full text](https://www.nature.com/articles/srep45914).

**Preparation method confirmed from the publisher text:** 80 mg CNF + 100 mg GO are dispersed in 100 mL deionized water, then ultrasonicated for 30 min using a 60 kHz, 25-mm titanium horn in an ice bath (0.5 s on/off duty cycle; stated 1000 W output). The dispersion is frozen at −30°C for >5 h and vacuum freeze-dried for 48 h at −55°C and 80 mTorr. The upstream CNF and GO synthesis methods are citations to other papers and are not costed here. This is a concrete example where an apparently simple material has a substantial drying/energy step.

**Condition-specific adsorption evidence:** The publisher methods describe a general batch setup of 8 mg aerogel in 40 mL, 160 rpm, 25°C overnight, concentrations spanning 1–100 mg/L, with pH 2–12 adjustments. The TC factor tests do not all share those conditions: pH uses 20 mg/L TC, 4 mg sorbent and 24 h; temperature is tested at 25/35/45°C for 8 h; dosage at 0.25–2 g/L for 24 h; initial TC concentration at 20–160 mg/L for 24 h. Figure 7 reports 82.1% TC removal, but does not explicitly restate its exact feed concentration in the caption/text. Do not attach one C0 value to the 82.1% point unless the figure is visually checked.

**Do not collapse these three endpoints:** The pseudo-second-order model-derived (q_e) is 84.8 mg/g (R²≈0.99 compared with PFO R²≈0.83). The Langmuir theoretical/fitted (q_m) appears as 454.6 mg/g in abstract/Results text and as 454.5 mg/g in the conclusion; preserve the small source-reported rounding difference rather than silently choosing one. The removal result is 82.1%. The model-fit preference itself is not proof of chemisorption.

**Regeneration:** The aerogel is soaked in 5 wt.% NaOH for 5 h, washed, then vacuum freeze-dried before reuse. After ten cycles, TC removal is 78.9% compared with 82.1% in the initial across-antibiotic comparison. That is a 3.2-percentage-point absolute decrease, approximately 3.9% relative to the initial percentage.

**Cost/feasibility:** The paper does not quantify cost per gram, cost per treated volume, product yield, energy, GO purchase/production cost, upstream CNF/GO costs, freeze-drying electricity or caustic consumption/waste per cycle. Thus the description “economical” is qualitative, not a demonstrated cost calculation.

**Source pin:** Publisher HTML lines 230–233 (preparation), 240–249 (batch method), 266–271 (factor tests/regeneration), 141–151 (Fig. 7 removal), 152–175 (kinetic/isotherm results), 213–221 (reuse). PDF/printed page numbering was not independently checked.


## EV-SEM-016 — Graphene at low antibiotic concentrations / TC (Peng et al., 2016)

**Primary source:** Peng et al., *Adsorption of antibiotics on graphene and biochar in aqueous solutions induced by π–π interactions*, DOI [10.1038/srep31920](https://doi.org/10.1038/srep31920); [open publisher full text](https://www.nature.com/articles/srep31920).

**Extracted:** The paper tests seven antibiotics, including TC, in a mixed solution at 200 ng/mL per antibiotic (200 µg/L), using 100 mg sorbent in 100 mL, pH 7, 298 K and 120 rpm. Graphene is one of the sorbents; the bamboo and coconut-shell biochar results must not enter the core graphene comparison. The publisher text reports that TC approached graphene adsorption equilibrium in about 2.5 h, and gives a range of 89.3–100% removal across the seven antibiotics for graphene at equilibrium. The exact TC percentage is figure-based and should not be guessed from the range. The study reports kinetic-model fits in µg/g, not a conventional Langmuir q_max in the text reviewed.

**Mechanism and cost caveats:** The authors emphasize π–π interactions, with fluorescence quenching of FITC (a structural surrogate) and DFT calculations. These are supportive but do not prove π–π interaction is the sole mechanism for TC. No quantified graphene production/purchase cost, yield, process-energy inventory or multicycle regeneration result was identified in the source sections reviewed.

**Audit points:** Treat this as mixed-solute, low-concentration evidence rather than a single-solute TC isotherm or real untreated wastewater. The exact TC endpoint and supplementary kinetic-table entries remain figure/SI checks; PDF page pins were not independently verified.


## EV-SEM-017 — Graphene oxide nanosheets / CIP and TC (Rostamian & Behnejad, 2018)

**Primary source:** Rostamian & Behnejad, *A comprehensive adsorption study and modeling of antibiotics as a pharmaceutical waste by graphene oxide nanosheets*, DOI [10.1016/j.ecoenv.2017.08.019](https://doi.org/10.1016/j.ecoenv.2017.08.019); [publisher record](https://www.sciencedirect.com/science/article/pii/S0147651317305158) and [PubMed record](https://pubmed.ncbi.nlm.nih.gov/28841526/).

**Accessible evidence:** The abstract confirms that GO nanosheets were tested on CIP, tetracycline (TCN/TC) and doxycycline, with initial concentration, pH, temperature and contact time varied. It describes pH around 6–7 and 100–200 min as the optimum region, with lower reported capacity at higher temperature (25–45°C). The publisher highlight reports CIP capacity up to 173.4 mg/g, with the paper's modeling summary identifying Sips-derived capacity and a CIP > doxycycline > TC ordering at a common temperature. A numeric TC-specific capacity was not present in the accessible abstract excerpt, so it remains blank in the evidence table.

**Model/mechanism caveats:** Hill and Toth reportedly described the equilibrium data well; kinetic fits varied by target (Elovich for CIP, pseudo-second-order for TC/doxycycline). The paper deduces π–π and cation–π interactions through analysis; do not state that these uniquely prove molecular mechanism. No regeneration or quantified cost inventory was found in accessible abstract-level material.

**Status:** Abstract-level primary-source extraction only; do not treat 173.4 mg/g as a measured qe, and do not extrapolate its fit/model to the unreported TC numerical value. No user download request is active.

## EV-SEM-018 — Graphene oxide / fluoroquinolones including CIP (Yadav et al., 2018)

**Primary source:** Yadav et al., *Removal of fluoroquinolone from aqueous solution using graphene oxide: experimental and computational elucidation*, DOI [10.1007/s11356-017-0596-8](https://doi.org/10.1007/s11356-017-0596-8); [PubMed record](https://pubmed.ncbi.nlm.nih.gov/29147984/).

**Accessible evidence:** The abstract says oxygen-functionalized graphene oxide was prepared by a modified Hummers–Offeman method, and adsorption was studied for CIP, norfloxacin and ofloxacin. It states that solution pH influenced adsorption more strongly than initial concentration, contact time or adsorbent dosage. No numeric CIP-specific capacity/removal or complete conditions were provided in the abstract used here.

**Status:** Qualitative abstract-level primary-source evidence only. Keep CIP separate from norfloxacin/ofloxacin, and don't use this record to support a numerical capacity ranking unless the relevant primary table/figure is accessible. No quantified process cost or verified regeneration information was available from the abstract; no new download is requested.

## EV-SEM-019 — Magnetic graphene oxide sponge / TC (2017)

**Primary source:** *Adsorption behaviors of tetracycline on magnetic graphene oxide sponge*, DOI [10.1016/j.matchemphys.2017.05.042](https://doi.org/10.1016/j.matchemphys.2017.05.042); [publisher record](https://www.sciencedirect.com/science/article/pii/S025405841730411X).

**Accessible evidence:** The publisher abstract says magnetic graphene oxide sponge (MGOS) was prepared by lyophilizing a dispersion of Fe₃O₄ nanoparticles and GO. It reports an adsorption capacity of 473 mg/g for TC, about 50% higher than GO in the authors' comparison; uptake was described as moderately fast, the pseudo-second-order model as a suitable kinetic fit, pH as having mild influence, and ionic strength as having little impact. Thermodynamic analysis was described as endothermic with an entropy-increase driving force.

**Metric/cost caveat:** The accessible abstract calls 473 mg/g an “adsorption capacity” without establishing in the excerpt whether this is a fitted qmax or a measured endpoint. Do not normalize/rank it as qmax until the full table and conditions are checked. Lyophilization is an explicit process step, but no quantified yield, energy, cost, Fe₃O₄ input burden or multicycle regeneration details were extracted from the abstract.

**Status:** Abstract-level primary-source extraction, provisional. No user download request is active.


## EV-SEM-020 — GO–sodium alginate hydrogel/aerogel for CIP (Fei et al., 2016)

**Primary source:** Fei et al., *Adsorptive removal of ciprofloxacin by sodium alginate/graphene oxide composite beads from aqueous solution*, DOI [10.1016/j.jcis.2016.08.068](https://doi.org/10.1016/j.jcis.2016.08.068); [publisher abstract and article preview](https://www.sciencedirect.com/science/article/abs/pii/S0021979716306312).

The primary abstract says GO was encapsulated in sodium alginate to form hydrogel and aerogel adsorbents; incorporating GO increased the adsorption capacity of SA composite gels roughly 7–9 times, Langmuir fitted the isotherm data well, and GO-SA aerogel showed relatively low sensitivity to pH and ionic-strength changes. The synthesis preview describes ultrasound dispersion of GO, mixing with alginate and CaCl2 hardening. A secondary comparison table reports q_m=86.12 mg/g for GO-SA at pH 4 and 25°C, but I did not verify the exact primary table or whether this number refers to a particular gel form. It is therefore a secondary-source cross-check, not a primary-verified quantitative value. No quantitative cost or multi-cycle regeneration inventory was extracted.

## EV-SEM-021 — Chitin/nGO continuous-flow composite for CIP (González et al., 2018)

**Primary source:** González et al., *Continuous flow adsorption of ciprofloxacin by using a nanostructured chitin/graphene oxide hybrid material*, DOI [10.1016/j.carbpol.2018.02.021](https://doi.org/10.1016/j.carbpol.2018.02.021); [PubMed record](https://pubmed.ncbi.nlm.nih.gov/29525158/) and the [accepted manuscript](https://ri.conicet.gov.ar/bitstream/11336/87000/11/CONICET_Digital_Nro.b2e52671-05bf-40a5-9fe0-525a5cfb6f21_J.pdf).

The accessible text describes batch isotherms with 10 mg Chi:nGO powder in 2 mL CIP solution, pH 6.30, 25°C, 120 rpm and C0=4–850 mg/L, plus continuous-flow column tests varying flow rate, pH, Na+ concentration and water hardness. CIP-spiked real-water samples were tested. CIP was eluted at column exhaustion with 0.1 M NaOH followed by water; the authors describe reuse after alkaline regeneration. Sips is reported as a better isotherm description. A method-text line states “100 grams” of sorbent in a very small column (1-cm internal diameter, 1.5-cm bed height), which is physically inconsistent; do not repeat that mass without checking the page image. No numeric capacity or cost figure is added from this source excerpt.

## EV-SEM-022 — GO for CIP (with SMX as a separate co-target; Chen et al., 2015)

**Primary source:** Chen et al., *Removal of sulfamethoxazole and ciprofloxacin from aqueous solutions by graphene oxide*, DOI [10.1016/j.jhazmat.2014.03.063](https://doi.org/10.1016/j.jhazmat.2014.03.063); [primary abstract](https://pubmed.ncbi.nlm.nih.gov/24755346/).

The abstract reports maximum sorption capacities of 379 mg/g for CIP and 240 mg/g for SMX. It attributes CIP sorption mainly to electrostatic attraction, describes lower sorption with added NaCl/CaCl2 and reports that CIP sorption at pH 2 destabilized GO suspension and caused aggregation. The 379 mg/g number is retained as an abstract-reported model/source value, not observed qe; the full fitted model/conditions are not verified from the abstract. SMX is kept separate and does not enter the CIP/TC core comparison. No quantified GO cost or multi-cycle regeneration result was extracted.

## EV-SEM-023 — MgO/chitosan/GO nanocomposite for CIP (Nazraz et al., 2019)

**Primary source:** Nazraz et al., *Chitosan-based sorbent for efficient removal and extraction of ciprofloxacin and norfloxacin from aqueous solutions*, DOI [10.1007/s00604-019-3563-x](https://doi.org/10.1007/s00604-019-3563-x); [PubMed record](https://pubmed.ncbi.nlm.nih.gov/31222415/).

The abstract describes hydrothermally synthesized MgO/chitosan/GO nanosheets, BET area 294 m²/g and characteristic pore size ~15 Å. It reports a Langmuir model and a maximum capacity of 1111 mg/g for CIP (with 1000 mg/g for NOR as a separate target) and kinetic equilibrium for CIP after >120 min. These remain abstract-reported fitted/model values, not observed qe; the unusually high CIP value needs table-level verification before ranking. The authors describe the material as economical, but the abstract provides no cost inventory, process yield or energy data. NOR is not merged into the CIP value.



## Full-text re-audit of EV-SEM-001 — Ghadim et al. (2013), GO for TC

**Primary full text:** [PLOS ONE article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0079254), DOI 10.1371/journal.pone.0079254.

The full HTML Methods and Results were rechecked. The study used improved-Hummers GO. Its *general* adsorption experiment describes 20 mg/L GO with 25 mL TC solution (6–180 mg/L), adjusted to pH 6–7 and incubated overnight. Separate pH tests use 2 mL GO suspension at 20 mg/L plus 4 mL TC (10–100 mg/L), pH 2–10, overnight. Kinetic tests use 2 mL GO (20 mg/L) plus 4 mL TC (6–180 mg/L) at pH 3.6, sampled every 15 min. The isotherm section also uses 6–180 mg/L TC, 20 mg/L GO, pH 3.6, with temperature sets; Fig. 6/Table 2 label 298, 303 and 308 K.

The paper reports fitted Langmuir q_max values of **322.43 mg/g at 298 K, 101.87 mg/g at 303 K and 73.53 mg/g at 308 K**. The abstract rounds the first to 323 mg/g. This unusually large decline with a 5–10 K change is what the article reports, but it should not be used to claim a well-established temperature trend until Table 2 and the source's multiple temperature series have been visually reconciled. The authors report a D–R mean adsorption energy of 1.83 kJ/mol at 298 K (1.69 at 303 K; 1.4 at 308 K) and say TC adsorption is favored at pH 7 within the pH study; fitted q_max and percent removal remain different endpoints.

The authors propose π–π/cation–π interactions and report a molecular-dynamics simulation. These are interpretations supported by spectral and modeled evidence; they do not quantify each interaction contribution. TC release was examined, including high release at some pH values, but that is not proof of reliable repeated-cycle regeneration. No cost/yield/energy inventory is reported.

**Table-use decision:** retain the reported 298 K q_max with the exact source and temperature, flag the temperature-series anomaly, do not rank it directly against unrelated studies without condition caveats, and keep regeneration and cost evidence as “not established.”

## EV-SEM-024 — Graphene oxide for tetracycline / Gao et al. (2012)

**Primary source:** Gao et al., *Adsorption and removal of tetracycline antibiotics from aqueous solution by graphene oxide*, *Journal of Colloid and Interface Science* 368(1), 540–546 (2012), DOI [10.1016/j.jcis.2011.11.015](https://doi.org/10.1016/j.jcis.2011.11.015); [PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/22138269/).

The primary abstract reports that TC adsorption onto GO follows Langmuir and Temkin isotherms, with a theoretical Langmuir maximum of **313 mg/g**, described as close to measured data. The abstract reports pseudo-second-order kinetics with k=0.065 g mg−1 h−1, and says TC capacity declines as pH or Na+ concentration increases. It also discusses oxytetracycline and doxycycline isotherms; these are separate antibiotics, not pooled with TC in this review.

The accessible abstract does not supply the complete initial concentration, dose, solution volume, time, temperature, or isotherm-table conditions; nor does it establish multi-cycle regeneration or a quantitative preparation cost. This record is therefore a **primary-source abstract extraction**, not a full-text extraction. Keep 313 mg/g as a model-reported maximum, not measured q_e, and do not treat it as directly comparable to Ghadim et al.'s 298 K q_max without aligned conditions and full table checks.


## Full-text quantitative re-audit of SEM-015 / EV-SEM-005 — GO–ZnAlNi-LDH for CIP

**Primary full text:** Sikri et al. (2025), *Graphene oxide/layered double hydroxide composite as highly efficient and recyclable adsorbent for removal of ciprofloxacin from aqueous phase*, DOI [10.3389/fnano.2025.1578620](https://doi.org/10.3389/fnano.2025.1578620); [full publisher article](https://www.frontiersin.org/journals/nanotechnology/articles/10.3389/fnano.2025.1578620/full).

The primary Methods specify 20 mL batch volume, CIP 0.225–10 mg/L, adsorbent 1–12 mg/L, pH 3–11, 0–4 h and 180 rpm. At **1 mg/L initial CIP, 10 mg/L composite, pH 7 and 60 min**, the paper reports **84.84% removal**. It defines q=(C₀−Cₜ)V/W, so those same conditions imply q_e≈84.84 mg/g if the units are as stated. However, its abstract and Table 1 also report an equilibrium/model value around 106.96–106.97 mg/g. Table 1 labels 106.96 mg/g as pseudo-first-order fitted q_e (R²=0.949); the article does not reconcile it with the stated removal/dose condition. Other sections compare additional capacity figures under different conditions. This is a source inconsistency; do not present 106.97 mg/g as a validated q_max or use it in ranking.

The detailed results report pseudo-first-order R²=0.949, Elovich R²=0.945 and intraparticle diffusion R²=0.88, while pseudo-second-order fits poorly in that section despite contrary generic wording elsewhere. Freundlich is the best reported isotherm (n=1.29, K_f=244.32, R²=0.95); Temkin R²=0.90, and Langmuir is reported as not fitting significantly. Five-cycle reuse declines from 80.4% removal in cycle 1 to 27% by cycle 5 after three distilled-water washes between adsorption runs.

**Preparation burden now verified from the Methods:** modified-Hummers GO; 500 mg GO; 1 h ultrasonication; Zn/Al/Ni nitrate salts, carbonate and concentrated 3.4 M NaOH to pH 10; hydrothermal treatment at 120°C for 16 h; filtering, water/ethanol washing to neutral and oven drying at 70°C. These are concrete cost/process variables, but no monetary cost, product yield or energy inventory is reported.

**Table decision:** include the 84.84% removal result only with its stated conditions; quarantine reported capacities; use the five-cycle decline as a practical limitation; do not repeat the authors' positive reusability characterization without the numerical decline.


## Schema and duplicate-record audit — 29 October 2026

The integrity review found that EV-SEM-010 and EV-SEM-013 had their final columns misassigned: narrative intended for mechanism/reuse/cost/source/caveat fields had drifted into adjacent columns. Those rows have now been remapped to the declared 20-column schema. The empty caveat cells are filled. A duplicate DOI was found for Fei et al. (2016), 10.1016/j.jcis.2016.08.068, in SEM-026 and SEM-041. SEM-026 is now the canonical candidate and EV-SEM-020 is linked to it; SEM-041 remains as a traceable alias, not a second bibliography item. The register therefore has 44 rows but **43 unique DOI-defined works**.


## EV-SEM-021 — full accepted-manuscript audit (González et al., 2018; SEM-042)

**Primary source:** [accepted manuscript PDF](https://ri.conicet.gov.ar/bitstream/11336/87000/11/CONICET_Digital_Nro.b2e52671-05bf-40a5-9fe0-525a5cfb6f21_J.pdf), DOI [10.1016/j.carbpol.2018.02.021](https://doi.org/10.1016/j.carbpol.2018.02.021).

### Preparation and batch test
The manuscript’s Methods §2.2 says nGO was prepared by Hummers’ method, exfoliated by 35 kHz sonication for 30 min in 0.4 M citrate buffer at pH 4.20, centrifuged, washed with water and methanol, and dried at 60°C. The chitin suspension used 42.5 g CaCl₂·2H₂O in 50 mL methanol, refluxed 30 min at 82°C; 1 g chitin was added and refluxed 2 h at 90°C. A 10 g aliquot of chitin suspension containing 120 mg pure chitin was combined with 40 mg nGO (Chi:nGO=3:1), wet-spun into methanol at −10 to −8°C, washed repeatedly with methanol and ultrapure water, dried at 60°C to constant weight, then ground/sieved to 35 mesh. These are real preparation inputs, but the GO upstream cost and complete reagent/energy/yield inventory are not provided.

Batch isotherms used 10 mg Chi:nGO in 2 mL CIP solution, pH 6.30, 25°C, 120 rpm and C₀ 4–850 mg/L; qe was calculated by mass balance. Five nonlinear models were tested; Sips was reported as the best fit, with heterogeneity parameter nₛ=0.38±0.09. The Langmuir model-specific qₘ was 282±11 mg/g for pure nGO and 73±3 mg/g for Chi:nGO 3:1. Those are fitted capacities, not observed qe and not interchangeable with column capacities.

### Dynamic column and real-water findings
The accepted manuscript’s column method explicitly says “One hundred grams” of Chi:nGO 3:1 were packed in a 1.0-cm internal-diameter, 10-cm-high glass column with a 1.5-cm bed height. It states the column was preconditioned with ultrapure water, 0.1 M HCl, water, 0.1 M NaOH and water; CIP was eluted with 0.1 M NaOH followed by water until baseline.

**Critical source inconsistency:** A 1.0-cm-ID × 1.5-cm-bed geometry has volume π(0.5 cm)²(1.5 cm)=1.178 cm³. The literal 100-g charge implies approximately 84.9 g/cm³, physically impossible for this composite. Do not silently “correct” this to 100 mg. The same mass is a dependency for the dynamic Thomas q₀ results, so those column q₀/τ values must be quarantined from final numeric rankings until the intended mass is resolved.

The text/table reports Thomas q₀ for flow rates 1/2/4 mL/min at pH 6.3 as 53±1/90±1/91±4 mg/g; at pH 4/9 (1 mL/min), 72±3/24±2 mg/g; at Na⁺ 50/100 mg/L, 92±1/110±1 mg/g; and hardness 50/200 mg/L as CaCO₃, 64±1/84±1 mg/g. Yoon–Nelson τ (50% breakthrough) for flow 1/2/4 mL/min was 153±3/128±1/65±3 min; for pH 4/9, 207±7/69±6 min; for Na⁺ 50/100 mg/L, 263±3/315±2 min; and hardness 50/200 mg/L, 182±3/241±3 min. These are model-derived dynamic values, and they remain on hold because of the mass anomaly.

For CIP-spiked real waters, tabled Thomas q₀ is Buenos Aires tap water 49±4 mg/g, Chascomús well water 26.4±0.8 mg/g, and Macachín well water 23.6±0.7 mg/g; τ is 154±5, 76±2 and 67±2 min respectively. Authors report that Chascomús and Macachín water had less than half the τ of ultrapure water/Buenos Aires. These were spiked water tests, not untreated CIP-contaminated water. Keep the real-water distinction explicit; the modelled q₀ figures also share the suspect packed-mass dependency.

### What it adds to the cost/performance assessment
The article calls the composite low-cost because of component sources and reusability, but supplies no monetized cost per g, treated volume, CIP removed or column lifetime; no product yield, Hummers reagent inventory, methanol/CaCl₂ budget, sonication/heating energy, pressure drop, eluent consumption or waste-treatment inventory. The precise synthesis steps help classify process burdens, but **do not establish low cost**.

**Source pins:** accepted manuscript PDF DOI 10.1016/j.carbpol.2018.02.021: Methods §2.2 at printed pp. 4–5 / text lines 156–181; batch/column Methods §§2.4.1–2.4.2 at pp. 6–7 / lines 218–249; batch model results at pp. 13–14 / lines 438–474; dynamic interpretation pp. 15–18 / lines 476–563; Tables 1–2 pp. 27–28 / lines 783–818. Browser text for tables was accessible; screenshot-rendered layout was not due browser cache failure, so visual table layout is not claimed as checked.


## EV-SEM-025 — GO/Ca-alginate–polyacrylamide beads for CIP (Choi & Choi, 2022)

**Primary source:** Choi & Choi, *Polyacrylamide Functionalized Graphene Oxide/Alginate Beads for Removing Ciprofloxacin Antibiotics*, *Toxics* 10(2), 77 (2022), DOI [10.3390/toxics10020077](https://doi.org/10.3390/toxics10020077); [open full text](https://www.mdpi.com/2305-6304/10/2/77).

**Preparation (Methods §2.2):** 0.1 g GO dispersed in 100 mL ultrapure water by sonication; add 0.6 g sodium alginate and stir; slowly add 1.0 g PAM; heat at 80°C for 4 h; cool to 30°C; pump the solution at 2 mL/min into 10 g/L CaCl₂·2H₂O solution; stir 24 h at room temperature to stabilize beads; wash three times and dry at 80°C. These are process inputs, not an economic cost estimate.

**Isotherms (Methods §2.4; Results §3.2, Table 1):** duplicate batch adsorption, initial CIP 1–50 ppm, 0.05 g beads, stated 55 mL contact volume, 250 rpm, 24 h at room temperature. The residual concentration was measured at 270 nm following centrifugation and 0.20 μm filtration. Langmuir: fitted qₘ=6.846 mg/g, b=0.132 L/mg, R²=0.991, χ²=0.037. Freundlich: K_F=1.260 (mg/g)(L/mg)^(1/n), n=2.372, R²=0.932, χ²=0.282. Temkin: B=1954.69 L/mg, K_T=2.074 L/g, R²=0.966, χ²=0.142. The Langmuir qₘ is a fitted parameter; the accessible text did not provide a specific measured equilibrium qₑ/removal percentage to quote.

**Method consistency flag:** the paper says the experiments used a 50 mL conical tube but reports 55 mL contact solution. Preserve both source values and flag them; do not silently reduce the solution volume or compute a derived qₑ from these values.

**Temperature/thermodynamics (Results §3.3, Fig. 5 and Table 3):** tests used 0.5, 1 and 2 ppm CIP at 10, 25 and 40°C. The paper reports qₑ rising with temperature at all three starting concentrations. For 0.5 ppm: ΔH=10.7 kJ/mol, ΔS=0.056 kJ/(mol·K), ΔG=−5.29, −6.13 and −6.98 kJ/mol at 283, 298 and 313 K. For 1 ppm: ΔH=4.4, ΔS=0.035, ΔG=−5.57, −6.10 and −6.63 kJ/mol. For 2 ppm: ΔH=7.2, ΔS=0.044, ΔG=−5.25, −5.91 and −6.57 kJ/mol. This supports the paper's thermodynamic analysis, not an observed removal/capacity comparison across studies.

**Mechanism, recovery and cost:** Authors discuss Ca²⁺ “egg-box” alginate crosslinking and PAM amide groups as contributors to CIP interaction, with FE-SEM/SEM-EDS/FTIR/TGA for characterization. These techniques do not quantify mechanism shares. No multicycle regeneration result, product yield, quantified process cost, or energy inventory was identified. The article's modeled qₘ is modest relative to some other fitted values, but cross-study ranking would still be inappropriate without aligned dose, concentration, matrix and metric.



## EV-SEM-026 — GO/PVA/calcium-alginate beads for CIP (Hossain et al., 2026)

**Primary source:** Hossain, Karim & Dipti, *Removal of ciprofloxacin from aqueous solutions using GO/PVA/calcium alginate composite beads as an absorbent*, *RSC Advances* (2026), DOI [10.1039/d6ra00494f](https://doi.org/10.1039/d6ra00494f); [open publisher text](https://pubs.rsc.org/en/content/articlehtml/2026/ra/d6ra00494f).

**Synthesis (Methods §§2.2–2.3):** Modified-Hummers GO synthesis uses a 9:1 H₂SO₄:H₃PO₄ mixture (170.2 mL/19.4 mL for the stated 200 mL mixture), 1 g graphite and 9.8 g KMnO₄; 90°C for 90 min; then water reaction, H₂O₂/water quench, 20% HCl treatment, centrifugation, repeated washing to neutral and ~36 h oven drying at 100°C. Bead formulations tested 0.5 or 1.0 g GO in 100 mL water (sonicate 60 min); add 5 g PVA and dissolve at 85°C; add 5 g sodium alginate at 65°C; sonicate 3 h and degas; dropwise bead formation into 5% boric acid + 5% CaCl₂ bath using a peristaltic pump (15 rpm, 1 mm tubing), then soak 12 h. Several strong acids/oxidants/salts, heating, sonication, washing and long drying are involved.

**Batch data and model outputs:** Experimental ranges include CIP 20–100 mg/L, pH 4–10, bead mass 0.1–0.5 g, contact 30–180 min and 30–70°C; 50 mL solution, 200 rpm; some parameter tests use C₀=40 mg/L. The paper reports observed qe=7.15 mg/g as its maximum over concentration tests, and removal around 89.82% / 89.92% under different sections/tests; do not assign both to one condition without checking the exact figure/table. Linear Langmuir qₘ=8.210 mg/g (R²=0.9588); nonlinear Langmuir qₘ=10.14 mg/g (R²=0.9715). These are fitted values, not the observed qe. Nonlinear kinetic fits give model-derived qe=3.3675 mg/g for PFO (R²=0.9979; k₁=0.028±0.001 min⁻¹) and 4.45827 mg/g for PSO (R²=0.9941). Linear PFO gives k₁=−0.00018 min⁻¹, an anomalous negative rate constant. The two D–R versions diverge sharply: linear fit qₘ=0.00013811 mg/g and E=11,800 kJ/mol; nonlinear fit qₘ=5.7715 mg/g and E=0.1984 kJ/mol. Preserve these as source-table outputs and do not endorse the D–R results as physically comparable.

**Thermodynamics:** At 0.5/1/2 mg/L CIP and 303–343 K, the article reports ΔH°=−66.9 kJ/mol, ΔS°=−177.4 J/(mol·K), and ΔG° values −13.74, −10.44, −9.434, −8.855 and −5.857 kJ/mol at 303, 313, 323, 333 and 343 K. The temperature tests and thermodynamic values are not evidence of practical low-energy operation; tested optima are condition-dependent.

**Regeneration and source-reported cost (Section 3.13):** The paper claims 4–5 reuse cycles with <25% capacity loss using 0.1 M HCl or NaOH; this is an author-reported claim, not a fully verified cycle-by-cycle curve in this extraction. It estimates ingredient prices and bead cost at $10–30/kg, desorption solution <$0.5/L, operational cost $0.1–0.5/kg wastewater per cycle, and lifecycle cost <$1/kg CIP removed over five cycles.

**Critical cost-basis mismatch:** Section 3.13 bases operation on 0.1 g beads/L. Elsewhere the article gives an experimental range of 0.1–0.5 g beads per 50 mL and says 0.5 g is optimal, equivalent to 10 g/L. These stated doses differ by a factor of 100. The claimed lifecycle cost per kg CIP removed therefore cannot be independently reproduced from the presented assumptions without a consistent treatment scenario, verified cycle data, and a traceable mass-of-CIP denominator. Report the dollar figures as author estimates—not validated lifecycle cost.

**Other caveats:** Section 2.4 mentions 55 mL contact volume while other experimental sections describe 50 mL and a 50 mL tube; preserve the inconsistency. The article uses synthetic solution tests only; real wastewater/industrial water tests are not reported. No numerical process-energy consumption or product yield is given.

**Source pins:** Methods §§2.2–2.4; §3.2/Table 1 and §3.10/Tables 2–3 (isotherm fits); §3.11/Table 4 (kinetics); §3.12/Table 5 (thermodynamics); §3.13 (cost/reuse claims).

**Focused mass-balance and cost-basis audit (30 October 2026):**

The open-access full text is accessible from the [RSC article](https://pubs.rsc.org/en/content/articlehtml/2026/ra/d6ra00494f) and its [PMC full-text record](https://pmc.ncbi.nlm.nih.gov/articles/PMC12999272/). Section 3.6.2 states that 0.5 g of beads was added to 50 mL at 298 K for 150 min and reports 89.82% removal at C₀=40 mg/L. Using those same reported conditions:

- Initial CIP mass = 40 mg/L × 0.050 L = 2.0 mg.
- CIP removed = 2.0 mg × 0.8982 = 1.7964 mg.
- Derived qₑ = 1.7964 mg / 0.5 g = **3.5928 mg/g**.
- Feed-mass ceiling = 2.0 mg / 0.5 g = **4.0 mg/g**.

This endpoint passes the simple mass-balance check. qₑ=3.5928 mg/g is a calculation from removal and stated conditions, not a source-tabulated observed qₑ. The separately reported maximum observed qₑ=7.15 mg/g belongs to the 20–100 mg/L concentration sweep and must not be paired with the 89.82% result. At C₀=100 mg/L, 50 mL and 0.5 g, the feed ceiling would be 10 mg/g. The nonlinear Langmuir qₘ=10.14 mg/g is 0.14 mg/g (1.4%) above that ceiling; because qₘ is a fitted asymptote rather than observed uptake, record this as a marginal fit/extrapolation concern, not a confirmed impossible experimental value. Linear Langmuir qₘ=8.210 mg/g is a separate fitted output. Linear/nonlinear D–R values remain strongly discordant, and the linear pseudo-first-order k₁ is negative.

Section 3.13 estimates the bead material at $10–30/kg but uses 0.1 g beads/L for its operational-cost scenario. Elsewhere, 0.5 g in 50 mL is described as the optimum, equivalent to 10 g/L: **100× the cost-section dose**. For a 100 L comparison, these loadings imply 10 g versus 1 kg beads; applying the paper's own estimated bead price alone gives $0.10–0.30 versus $10–30, before GO synthesis reagents, washing, drying, regeneration or waste treatment. This calculation illustrates the dose-basis sensitivity and does not independently estimate total process cost. The paper's <$1/kg CIP-removed lifecycle claim remains unreproducible because the cost worksheet, consistent loading basis and explicit removed-CIP denominator are not supplied. Preserve the paper's 50/55 mL method inconsistency rather than guessing a correction. No real wastewater trial, quantified energy inventory or material yield is reported.

**Evidence-use rule:** condition-specific removal may be retained with the calculated qₑ label and source conditions; keep measured/derived qₑ, kinetic-fit qₑ and isotherm qₘ separate. Do not treat this paper as a validated low-cost winner.


## EV-SEM-027 — GO/Co–Fe magnetic nanocomposite for tetracycline (Hossain et al., 2024)

**Primary source:** Hossain et al., *Ultrafast and simultaneous removal of four tetracyclines from aqueous solutions using waste material-derived graphene oxide-supported cobalt–iron magnetic nanocomposites*, DOI [10.1039/d3ra07597d](https://doi.org/10.1039/d3ra07597d); [open RSC full text](https://pubs.rsc.org/en/content/articlehtml/2024/ra/d3ra07597d).

**Synthesis:** Graphite recovered from waste dry cells was cleaned, treated with Aqua Regia, washed and dried at 60°C for 24 h. GO synthesis used a modified-Hummers route with 240 mL H₂SO₄ + 28 mL H₃PO₄, 2 g graphite and 6 g KMnO₄; 50°C for 2 h; water/H₂O₂ quench; centrifugation, 30% HCl purification, repeated washing and drying at 45°C for 24 h. GO/Co–Fe was made using Co(NO₃)₂·6H₂O, FeSO₄·7H₂O and Fe₂(SO₄)₃·nH₂O at 1:1:2 molar ratio; stir 40°C for 25 min, add 100 mg GO, adjust pH to ~10, heat 85°C for 1 h, wash and dry at 60°C for 24 h. Waste-cell origin does not itself establish low cost; no quantified yield/energy/reagent-recovery/cost inventory was reported.

**TC-specific adsorption:** At C₀=0.2 mg/L (200 ppb), GO/Co–Fe dose 0.15 g/L, pH 7, 30 s, 250 rpm and 25°C, the paper reports TC removal as 94.1% in abstract/body and 93.94% in a concentration section. Keep both values with a source consistency flag rather than choosing one. The experiment is a low-concentration synthetic-water test, not a real-water test. pH was tested from 2 to 10, with maximum removal around pH 7; initial concentration range 0.2–2.0 mg/L.

**Capacity/model outputs:** Table 2 gives Langmuir fitted qₘ for TC=64.10 mg/g at 50°C. CTC, OTC and DTC have separate fitted qₘ values (71.43, 72.46 and 99.01 mg/g) and must not be pooled with TC. The reported PSO fit has R²=0.999; a model-fitted qe was not captured in the accessible extraction. Do not compare the fitted qₘ at 50°C directly to the TC removal % at 25°C.

**Recovery and remaining limits:** The paper describes magnetic separation, methanol treatment, distilled-water washing, drying at 50°C, and up to eight regeneration rounds; a reported efficiency drop from ~95% to ~90% is not completely pinned to TC-only cycle-by-cycle values in this extraction. No real-water testing or quantified cost data were reported. Cost claims should not be inferred merely from the waste-derived graphite feedstock.

**Source pins:** Scheme 1; §3.1 characterization; §§3.2.2–3.2.7 adsorption/pH/concentration/kinetics/isotherms/reuse; Table 2 and Fig. 9.


## EV-SEM-028 — EDTA-functionalized magnetic GO / tetracycline (mGO/EDTA, 2026)

**Primary source:** *EDTA-functionalized magnetic graphene oxide for rapid and efficient removal of tetracycline from aqueous media*, DOI [10.1016/j.dwt.2026.101889](https://doi.org/10.1016/j.dwt.2026.101889); [ScienceDirect primary article](https://www.sciencedirect.com/science/article/pii/S1944398626002638).

**Preparation:** GO was prepared from 3 g spent-dry-cell graphite with 360 mL concentrated H₂SO₄, 40 mL H₃PO₄, 18 g KMnO₄, 3 mL 30% H₂O₂, 30% HCl and ethanol. Magnetic GO was made by dispersing 0.08 g GO in 50 mL water (35-min sonication), combining with Fe₂(SO₄)₃·7H₂O (7.998 g) and FeSO₄·7H₂O (2.781 g) in 100 mL water (35-min sonication), mixing at 50°C/30 min, precipitating at pH≈11 with 2 M NaOH, stirring 80°C/2 h, washing and vacuum drying at 60°C/18 h. mGO/EDTA then used 0.50 g mGO in 20 mL 10% aqueous acetic acid, mixed with 3 g EDTA in 50 mL methanol for 24 h at room temperature; magnetic isolation, water/ethanol washes and drying at 50°C. No cost/yield/energy inventory.

**Optimized batch result:** Total 20 mL TC solution (18 mL water + 2 mL stock), C₀=0.2 mg/L, dose=0.10 g/L (=0.002 g adsorbent), pH 5, contact time 5 min, 25°C, 250 rpm. Removal is 93.23%. The initial TC mass is 0.2 mg/L × 0.020 L = 0.004 mg; removed mass is 0.004 × 0.9323 = 0.0037292 mg; division by 0.002 g adsorbent implies **qₑ≈1.8646 mg/g** under the listed conditions.

**Important kinetic inconsistency:** The article's best-R² pseudo-second-order fit reports qₑ=0.01937 mg/g (R²=1), about **96× lower** than mass-balance-implied qₑ≈1.865 mg/g. Its pseudo-first-order fit reports qₑ=3.65672 mg/g (R²=.62776), while Elovich α=2.88×10⁷⁴ in the printed units is also extreme. Do not quote the R²=1 fitted qₑ as a physically validated uptake value; record the source model output and the mass-balance flag side by side.

**Isotherms:** Freundlich is the best reported fit at 25°C (n=1.97, K_F=13.27, R²=.94957). The Langmuir fitted q_max=31.32 mg/g at 25°C has only R²=.69125; it declines to 28.22 mg/g at 35°C (R²=.4795) and 10.79 mg/g at 45°C (R²=.98312). Keep these fitted parameters separate from the specific low-C₀ removal test. Eight adsorption–desorption cycles are reported with removal decreasing from ~94% to 90.50%; spent material was magnetically recovered, washed three times with methanol under ultrasonication, and dried at 60°C.

**Cost:** No monetized cost, yield, energy, solvent-recovery balance, or cost per mass of TC removed. The dry-cell feedstock is not proof of low cost: the recipe still uses strong acids/oxidants, iron salts, NaOH, EDTA, acetic acid, methanol, extensive washing, sonication and drying.

**Source pins:** Methods §2; results §§3.1–3.2; Tables 1–5 (isotherm, kinetics and thermodynamics). Exact printed page pins not independently captured from the browser view.



**Secondary source/table consistency QA (30 October 2026):** The publisher's indexed full text exposes exact table and figure pages: Fig. 3 conditions are on p. 7; Table 2 kinetic fit values are on p. 8; Table 3 isotherm fits are on p. 9; Fig. 6 reuse is on p. 10. The mass-balance conflict is broader than one fit: for C₀=0.2 mg/L, 20 mL, dose=0.10 g/L (=0.002 g), and 93.23% removal, the implied uptake is ~1.8646 mg/g and the feed-mass ceiling is 2.0 mg/g. Table 2's PFO fitted qₑ=3.65672 mg/g exceeds that ceiling if interpreted for this setup (R²=.62776); the PSO fitted qₑ=0.01937 mg/g is ~96× lower than the mass-balance estimate despite R²=1. No raw data are available in the authors' data-availability statement to resolve this. Also, Table 3's 45°C Langmuir R²=.98312 is higher than Freundlich R²=.79037, even though the text claims Freundlich is the best fit overall. At 25°C, the stated Langmuir qₘ=31.32 mg/g has R²=.69125 and should be treated as a weak model output, not a robust observed capacity. Preserve source values and flag both internal inconsistencies; no correction inferred.
## EV-SEM-029 — GO/calcium-alginate composite fibers / ciprofloxacin (Wu et al., 2013)

**Primary source:** Wu et al., *Adsorption of ciprofloxacin onto biocomposite fibers of graphene oxide/calcium alginate*, *Chemical Engineering Journal* 230 (2013), 389–395, DOI [10.1016/j.cej.2013.06.072](https://doi.org/10.1016/j.cej.2013.06.072); [ScienceDirect abstract](https://www.sciencedirect.com/science/article/abs/pii/S1385894713008450).

**Accessible primary-source statements:** GO/CA fibers were prepared by wet spinning; GO loading varied from 0 to 6 wt%. The abstract reports optimum pH 5.9 and equilibrium contact time 24 h. Removal percentage reached 78.9% at 2 g/L adsorbent dose and 6 wt% GO loading. At equilibrium CIP concentration 60 mg/L, reported adsorption capacity rose from 18.45 mg/g at 0 wt% GO to 39.06 mg/g at 6 wt% GO.

**Model and limits:** Freundlich was reported to fit isotherm data well, and pseudo-second-order was reported for kinetics, but numeric Freundlich parameters, kinetic qe/k₂, exact wet-spinning ingredient quantities, and regeneration details were not present in the accessible abstract/section snippets. Do not call 39.06 mg/g a fitted q_max; it is the source-reported capacity at the specified equilibrium concentration. The reported 78.9% removal is at 2 g/L dose and 6 wt% GO, while the exact paired starting concentration is not available in the snippet, so don't merge it with the 60 mg/L equilibrium-capacity point without verifying the primary table. No specific cost/yield/energy inventory or multicycle reuse result was accessible.


## Source-preview re-audit — EV-SEM-019 and EV-SEM-023 (29 October 2026)

### EV-SEM-019 — magnetic graphene oxide sponge (MGOS) for TC
The accessible primary *Materials Chemistry and Physics* preview confirms the material is made by lyophilizing GO with sodium-citrate-coated Fe₃O₄ at a **1:40 Fe₃O₄:GO mass ratio**, density 4.6 mg/cm³. GO uses a modified-Hummers route, and the magnetite nanoparticles are synthesized by co-precipitation with sodium citrate. The headline **473 mg/g** TC adsorption capacity is confirmed but its definition (measured qₑ at a given condition versus model-fitted q_max) is not provided in the preview. Langmuir, Freundlich and Temkin isotherms and PFO/PSO/intraparticle kinetics are listed, but numeric fit parameters, test conditions, reuse and costs are unavailable. Do not classify or rank 473 mg/g more specifically without the full primary data.

### EV-SEM-023 — MgO/chitosan/GO nanosheets for CIP (CIP separate from NOR)
The primary Springer abstract for DOI [10.1007/s00604-019-3563-x](https://doi.org/10.1007/s00604-019-3563-x) confirms hydrothermal MgO/chitosan/GO nanosheets, BET surface area 294 m²/g and typical pore size about 15 Å. The abstract reports Langmuir maximum capacities of 1111 mg/g for CIP and 1000 mg/g for norfloxacin; these are reported model-capacity claims, not observed qe at a stated C₀. PSO kinetics and equilibrium times >120 min (CIP) / >150 min (NOR) are stated. No dose, C₀ range, pH, fit statistics, table values, regeneration or quantified cost are available in the accessible abstract. The unusually high 1111 mg/g stays provisional and out of an unqualified ranking until conditions/tables can be verified. The author’s “economical” wording is not cost evidence.


## EV-SEM-030 — GO·Fe₃O₄ / tetracycline (DFT plus experiment; 2022)

**Primary source:** *A DFT theoretical and experimental study about tetracycline adsorption onto magnetic graphene oxide*, DOI [10.1016/j.molliq.2022.118837](https://doi.org/10.1016/j.molliq.2022.118837); [ScienceDirect article](https://www.sciencedirect.com/science/article/pii/S0167732222003749).

**Accessible experimental condition:** Abstract reports TC initial concentration 1000 mg/L, adsorbent mass 50 mg, pH 7 and 293 K. It calls the maximum adsorption capacity 531.93 mg/g. **The accessible source does not expose solution volume or define whether the 531.93 mg/g is measured qₑ or a fitted qmax**, and no isotherm fit statistics, contact time, reuse-cycle values, or cost are available in the preview. Do not calculate mass-balance uptake, relabel the metric, or rank it as validated without the complete primary table.

**Preparation:** GO·Fe₃O₄ magnetic composite produced by co-precipitation, controlling magnetite incorporation on GO; exact amounts, pH sequence, washes, drying and yield are not visible in the accessed text.

**Computational outputs are separate:** the paper’s DFT conclusion reports binding energy −3.86 eV, spin polarization 14.99 μB, and HOMO–LUMO gap 0.22 eV for configuration 1. These are electronic structure values, not experimental sorption outcomes or kinetic/isotherm parameters.

**Reuse/cost:** The publisher highlight calls the material reusable/easy to operate, but exact cycle counts and retained capacity are not available in the accessible preview. No real-water data or quantified cost/energy/yield was found.



## EV-SEM-031 — GO–[Ni(DMG)]ₙ / ciprofloxacin (2026)

**Primary source:** *Tailored graphene oxide – [Ni(DMG)]n composites for enhanced adsorption of ciprofloxacin: Kinetic, Isothermal, and pH-dependent behavior*, DOI [10.1016/j.jwpe.2026.110335](https://doi.org/10.1016/j.jwpe.2026.110335); [ScienceDirect article](https://www.sciencedirect.com/science/article/pii/S2214714426008937).

**Preparation excerpt:** One-pot reaction of ethanol-dispersed GO suspension, Ni(II) ions and dimethylglyoxime (DMG), with 24 h stirring at room temperature. The accessible abstract does not give the GO:Ni:DMG quantities/ratios, work-up, product yield, or reagent recovery.

**Performance/model excerpt:** The abstract reports Langmuir-comparison maximum capacities of 117–159 mg CIP/g across formulations and high removal across pH 2–7. However, it explicitly says Freundlich and Temkin provided better agreement with the isotherm data; Langmuir was additionally used to compare maximum capacities because its R² values were considered reasonably high. PSO gives the best kinetic fit, k=0.0005–0.0009 g/(mg·min). Exact initial concentration, dose, solution volume, temperature, time series, qmax per formulation and fit statistics are not available in the accessible excerpt. Do not call 117–159 mg/g measured qe or describe Langmuir as the best-fit model.

**Practical evidence:** No regeneration/reuse data, real-water tests, quantified process cost, energy, yield or cost per mass of CIP removed were exposed in the source excerpt. Ni(II) and DMG are relevant formulation inputs, but the accessible source does not allow a cost calculation.


## EV-SEM-032 — Fe₃O₄/GO / ciprofloxacin and cephalexin with ultrasonic treatment (2023; official full-text + SI audit)

**Primary source:** Alishiri et al., *Removal of ciprofloxacin and cephalexin antibiotics in water environment by magnetic graphene oxide nanocomposites; optimization using response surface methodology*, *Results in Engineering* 20 (2023), 101507, DOI [10.1016/j.rineng.2023.101507](https://doi.org/10.1016/j.rineng.2023.101507); [official open-access full text](https://www.sciencedirect.com/science/article/pii/S2590123023006345). Official publisher [Supplementary Material mmc1.docx](https://ars.els-cdn.com/content/image/1-s2.0-S2590123023006345-mmc1.docx) inspected (Tables S1–S2).

**Synthesis (Methods §§2.2–2.4):** GO by Hummers method: 2 g graphite in 46 mL concentrated H₂SO₄ in an ice bath; add 6 g KMnO₄ below 15°C, stir 60 min at 40°C; add ~92 mL water and 7 mL 30% H₂O₂; centrifuge 2500 rpm for 30 min; wash with 150 mL 5% HCl and water; dry at room temperature. Fe₃O₄: dissolve 2.15 g FeCl₂·4H₂O and 5.84 g FeCl₃·6H₂O in 100 mL water under N₂ at 80°C; add 10 mL 25% ammonia over 20 min; magnetically recover, wash three times and dry at 60°C for 12 h. Composite: ultrasonicate 0.03 g GO in 30 mL DI water and separately disperse 0.08 g Fe₃O₄ in 80 mL 1 M HNO₃ using ultrasound; magnetically settle/decant the Fe₃O₄, combine precipitate with GO suspension, stir 5 h, magnetically recover, wash and dry 60°C/12 h.

**CCD/RSM design (Methods §§2.5–2.6):** 30-run central composite design with four variables: nanocomposite amount 0.05–0.85 g, pH 3–11, initial antibiotic concentration 10–50 mg/L and contact time 10–50 min. Each test uses 15 mL antibiotic solution. Reaction mixture is placed in an ultrasonic bath at laboratory temperature, then magnetically separated; residual concentration measured by UV–Vis. Ultrasound is therefore part of the adsorption/removal protocol, not merely a composite-preparation step. The paper's highlights say antibiotic removal is significantly accelerated by ultrasound. The acoustic bath's power, frequency and delivered energy are not provided, and ultrasound is not one of the four RSM factors.

**Optimum and validation (Abstract, §3.5 and official SI Table S2):** Optimum CIP condition: C₀=15 mg/L, composite mass=0.55 g, pH 7, 33 min, 15 mL solution, laboratory temperature with ultrasonic-bath treatment. Official SI Table S2 reports experimental CIP removal **96.39±3.3 (n=3)** against predicted 95.51%; for cephalexin it reports 97.69±2.3 (n=3) against predicted 97.20%. Thus 96.39% is not merely a model prediction; it is experimentally validated at the optimum. The stated solid loading is 0.55 g / 0.015 L = **36.7 g/L**.

**Derived mass balance, not a reported capacity:** At the CIP optimum, initial CIP mass = 15 mg/L × 0.015 L = 0.225 mg. Applying 96.39% removal gives 0.2168775 mg removed. Dividing by 0.55 g nanocomposite gives (q_e≈0.3943) mg/g. This is a calculation from the source's reported mean removal and conditions; it is not a source-reported or fitted (q_e), and not (q_{max}). The high dose explains why a high removal percentage cannot be compared directly with high-capacity sorbents.

**RSM statistics (official SI Table S1):** This is a response-surface polynomial for percent removal, not an adsorption isotherm or kinetic model. CIP: R²=0.9905, adjusted R²=0.9817, predicted R²=0.9523; model F=111.81, p<0.0001; lack-of-fit F=2.43, p=0.16. Cep: R²=0.9940, adjusted R²=0.9885, predicted R²=0.9747; model F=178.73, p<0.0001; lack-of-fit F=0.93, p=0.56. The CIP response polynomial in coded factors A=dose, B=pH, C=initial concentration and D=contact time is: (%R_{CIP}=85.32+10.92A+6.97B-9.46C+5.57D+2.29AB-0.20AC+2.57AD-0.30BC-0.11BD+1.46CD-7.08A²-8.18B²-6.13C²-5.29D²). No Langmuir/Freundlich (q_{max}) or pseudo-order kinetic (q_e) is reported. Do not label RSM (R²) values as adsorption capacity/kinetic statistics.

**Real-water results and replication-count discrepancy (§3.9 / Table 5):** CIP removal: tap 94.12±2.2, river 91.66±1.8, lake 90.65±3.1 and wastewater 89.96±2.3. Cep results: tap 95.83±2.4, river 93.04±3.2, lake 90.87±2.5 and wastewater 92.45±2.8. The article says samples were filtered to remove suspended particles and used without further treatment. However, §3.9 says each experiment was repeated three times, while Table 5's column headings identify RSD with n=5. Preserve this unresolved internal sample-count inconsistency; do not silently decide which count is correct. The optimum-condition validation in SI Table S2 separately reports n=3.

**Regeneration (§§3.7 and 3.10):** Methanol was selected as the best eluent among chloroform, methanol, acetonitrile and ammonia. Regeneration used 2 mL methanol plus 10 mL DI water. The authors report stable removal for at least seven adsorption–desorption cycles, with no degradation in magnetic properties. Fig. 5 caption identifies 0.55 g composite, 15 mg/L antibiotic, pH 7 and 33 min.

**Practical and attribution caveats:** The adsorbent dose is 36.7 g/L. Ultrasound is applied in GO/Fe₃O₄ composite preparation and in every adsorption experiment, but power, frequency and energy are not stated; the RSM does not optimize sonication settings. No matched ultrasound-only or non-sonicated control is described in the methods/design, so the removal contribution from ultrasound-associated losses cannot be separated from adsorption on the reported evidence; this does not establish that degradation occurred. No quantitative cost, yield, energy inventory or cost per mass antibiotic removed is reported. Material preparation also uses Hummers chemicals, 1 M nitric acid, ammonia, repeated washing/drying and methanol regeneration.

**Evidence-use rule:** cite the 96.39% CIP removal only with all condition boundaries, including 0.55 g in 15 mL and ultrasonic-bath treatment. If useful, show (q_e≈0.394) mg/g only as an explicitly calculated mass-balance check. Do not present this study as a high-(q_{max}) adsorbent or compare its removal percentage alone against passive adsorption studies. Keep the ultrasound-energy/control gap and Table 5 n=3 vs n=5 discrepancy visible.

## EV-SEM-033 — Magnetic chitosan-grafted graphene oxide / ciprofloxacin (2016)

**Primary source:** *Removal of ciprofloxacin from aqueous solution by a magnetic chitosan grafted graphene oxide composite*, DOI [10.1016/j.molliq.2016.07.037](https://doi.org/10.1016/j.molliq.2016.07.037); [ScienceDirect abstract preview](https://www.sciencedirect.com/science/article/abs/pii/S0167732215312848).

**Accessible findings:** The preview reports a Langmuir fitted maximum capacity qₘ=282.9 mg/g, pseudo-second-order kinetic behavior, and Freundlich and Langmuir isotherms describing equilibrium data. The composite retained about 72% of initial adsorption capacity after four uses. Adsorption was reduced at pH 7 and 9; Na⁺ at 200 mM and Ca²⁺ at 10 mM significantly reduced CIP adsorption.

**Limits:** The accessible preview does not provide exact preparation ratios, C₀, dose, solution volume, contact time, temperature, fit statistics, regeneration eluent, cycle-by-cycle capacity, or quantified cost/yield/energy. Treat 282.9 mg/g as model-fitted qₘ, not observed qe, and do not rank it against condition-specific measured uptakes until the full condition set is verified.

## EV-SEM-034 — Magnetic GO for tetracycline hydrochloride (2019)

Primary publisher source: https://www.sciencedirect.com/science/article/abs/pii/S0169433219300455 (DOI 10.1016/j.apsusc.2019.01.036).

The publisher abstract identifies MGO, examines pH and temperature effects, and reports PSO kinetics plus a Freundlich isotherm. TC-HCl and OTC adsorption are strongest at pH 3.3; CTC behaves differently and performs better under alkaline conditions. The accessible synthesis snippet states expandable GO was prepared by a modified Hummers route and 100 mg GO dispersed in 30 mL NMP by ultrasonication. The abstract does not state numeric capacity, feed/dose conditions, yield or a cost inventory. The often quoted 141.44 mg/g for TC-HCl is found in a separate secondary review, not verified in the primary table; keep it out of quantitative ranking.

## EV-SEM-035 — DFT-only rGO/CIP/TC study (2024)

Primary publisher source: https://www.sciencedirect.com/science/article/abs/pii/S0301010424000363 (DOI 10.1016/j.chemphys.2024.112207).

This study uses Gaussian 09, PBEPBE/6-31G(d,p), and AIM/NBO calculations for TC and CIP on pristine and Ca2+-supported rGO models. Its reported adsorption-energy range (−8.0 to −19.9 kcal/mol) and proposed hydrogen-bond/Ca···O interactions are molecular-model outputs. No physical sorbent was manufactured or tested in water; there is no measured q_e, q_max, removal, regeneration, or process-cost data. Retain only as theory/mechanism context, never as an empirical performance-table entry.

## EV-SEM-036 — Sulfonated GO in multi-fluoroquinolone mixtures (2026)

Primary open-access source: https://www.sciencedirect.com/science/article/pii/S2590123026011011 (DOI 10.1016/j.rineng.2026.110064).

The abstract describes equimolar binary (CIP + moxifloxacin), ternary (+ levofloxacin), and quaternary (+ sparfloxacin) systems. Langmuir-model capacities at 25°C are reported as 370.37, 357.14 and 333.33 mg/g for the three mixtures; these are mixture-level fitted capacities, not verified single-CIP q_max values. DMF containing 1 mol/L HCl reportedly desorbed >97% of antibiotics; >92% of initial performance remained after five cycles. No complete preparation or process-cost inventory is available in the abstract. DMF and strong-acid regeneration require solvent/acid handling and recovery.

## EV-SEM-037 — Rotating-field Fe3O4/rGO for tetracycline hydrochloride (2026)

Primary publisher source: https://www.sciencedirect.com/science/article/pii/S1383586625046465 (DOI 10.1016/j.seppur.2025.136049).

The abstract reports a co-precipitated Fe3O4/rGO composite (95.12 m²/g) operated with a rotating magnetic field. For TCH, the reported optimum uses C0=30 mg/L, dose=1.0 g/L, pH 5 and 2 A excitation current, with >96% removal and >87% efficiency after four cycles. The abstract gives no numeric q_max or observed q_e; power draw, frequency, matched field-free controls, regeneration recipe and specific matrix details are not available. A current of 2 A alone is not energy consumption and does not establish low-cost performance.
## EV-SEM-034 — Magnetic GO for tetracycline hydrochloride (2019)

Primary publisher source: https://www.sciencedirect.com/science/article/abs/pii/S0169433219300455 (DOI 10.1016/j.apsusc.2019.01.036).

The publisher abstract identifies MGO, examines pH and temperature effects, and reports PSO kinetics plus a Freundlich isotherm. TC-HCl and OTC adsorption are strongest at pH 3.3; CTC behaves differently and performs better under alkaline conditions. The accessible synthesis snippet states expandable GO was prepared by a modified Hummers route and 100 mg GO dispersed in 30 mL NMP by ultrasonication. The abstract does not state numeric capacity, feed/dose conditions, yield or a cost inventory. The often quoted 141.44 mg/g for TC-HCl is found in a separate secondary review, not verified in the primary table; keep it out of quantitative ranking.

## EV-SEM-035 — DFT-only rGO/CIP/TC study (2024)

Primary publisher source: https://www.sciencedirect.com/science/article/abs/pii/S0301010424000363 (DOI 10.1016/j.chemphys.2024.112207).

This study uses Gaussian 09, PBEPBE/6-31G(d,p), and AIM/NBO calculations for TC and CIP on pristine and Ca2+-supported rGO models. Its reported adsorption-energy range (−8.0 to −19.9 kcal/mol) and proposed hydrogen-bond/Ca···O interactions are molecular-model outputs. No physical sorbent was manufactured or tested in water; there is no measured q_e, q_max, removal, regeneration, or process-cost data. Retain only as theory/mechanism context, never as an empirical performance-table entry.

## EV-SEM-036 — Sulfonated GO in multi-fluoroquinolone mixtures (2026)

Primary open-access source: https://www.sciencedirect.com/science/article/pii/S2590123026011011 (DOI 10.1016/j.rineng.2026.110064).

The abstract describes equimolar binary (CIP + moxifloxacin), ternary (+ levofloxacin), and quaternary (+ sparfloxacin) systems. Langmuir-model capacities at 25°C are reported as 370.37, 357.14 and 333.33 mg/g for the three mixtures; these are mixture-level fitted capacities, not verified single-CIP q_max values. DMF containing 1 mol/L HCl reportedly desorbed >97% of antibiotics; >92% of initial performance remained after five cycles. No complete preparation or process-cost inventory is available in the abstract. DMF and strong-acid regeneration require solvent/acid handling and recovery.

## EV-SEM-037 — Rotating-field Fe3O4/rGO for tetracycline hydrochloride (2026)

Primary publisher source: https://www.sciencedirect.com/science/article/pii/S1383586625046465 (DOI 10.1016/j.seppur.2025.136049).

The abstract reports a co-precipitated Fe3O4/rGO composite (95.12 m²/g) operated with a rotating magnetic field. For TCH, the reported optimum uses C0=30 mg/L, dose=1.0 g/L, pH 5 and 2 A excitation current, with >96% removal and >87% efficiency after four cycles. The abstract gives no numeric q_max or observed q_e; power draw, frequency, matched field-free controls, regeneration recipe and specific matrix details are not available. A current of 2 A alone is not energy consumption and does not establish low-cost performance.