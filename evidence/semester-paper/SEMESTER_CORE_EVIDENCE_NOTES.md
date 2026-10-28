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

## EV-SEM-002 — GO/calcium-alginate fibers / TC (2018)

**Primary source:** *Adsorption of tetracycline antibiotics from an aqueous solution onto graphene oxide/calcium alginate composite fibers*, DOI [10.1039/C7RA11964J](https://doi.org/10.1039/C7RA11964J); [full-text record](https://pmc.ncbi.nlm.nih.gov/articles/PMC9077392/).

**Extracted:** freeze-dried GO/CA fibers cross-linked with CaCl2; 25 mg adsorbent in 50 mL for equilibrium experiments at 25°C over 5 h; observed qe of 17.6 mg/g at C0 10 mg/L and 65.4 mg/g at C0 60 mg/L; highest reported removal in the pH experiment was 56.8% at pH 6; fitted Langmuir qmax = 131.6 mg/g (R² 0.9938).

**Audit point:** The paper's fitted qmax and measured qe at specific starting concentrations must be reported separately. Freeze-drying is a preparation step but no quantified energy/cost inventory has been extracted. A multi-cycle regeneration result was not found in the sections extracted.

## EV-SEM-003 — MnFe2O4/rGO / TC (2018)

**Primary source:** *Adsorption of Tetracycline with Reduced Graphene Oxide Decorated with MnFe2O4 Nanoparticles*, DOI [10.1186/s11671-018-2814-9](https://doi.org/10.1186/s11671-018-2814-9); [open full-text record](https://pmc.ncbi.nlm.nih.gov/articles/PMC6281545/).

**Extracted:** one-step MnFe2O4/rGO preparation; about 41 mg/g uptake reported at initial TC 10 mg/L; near-equilibrium around 8 h; pH optimum reported at 3.3; 0.1 M HCl elution and re-use performance declining from 86% initial removal to reported 85%, 82%, 79%, and 71%.

**Audit point:** Check precise cycle numbering from Figure 6 before manuscript use. Although magnetic recovery is an operational benefit, measured synthesis cost and acid-waste burden are not available in the extracted evidence.

## EV-SEM-004 — Zn–C battery-derived GO / CIP (2024)

**Primary source:** Yasmin et al., *Efficient removal of ciprofloxacin from aqueous solution using Zn-C battery derived graphene oxide enhanced by hydrogen bonding, electrostatic and π-π interaction*, DOI [10.1016/j.heliyon.2024.e33317](https://doi.org/10.1016/j.heliyon.2024.e33317); [open full-text record](https://pmc.ncbi.nlm.nih.gov/articles/PMC11253669/).

**Extracted:** 99.0% removal at initial CIP 2.0 mg/L, GO dose 20 mg/L, pH 5.7, 20 min, 30°C and 230 rpm. Experimental qe in the kinetic experiment is 78.82 mg/g; pseudo-second-order fitted qe is 79.36 mg/g. A separate isotherm analysis gives a fitted Langmuir qm of 419.62 mg/g at 30°C.

**Audit point:** qmax comes from the isotherm analysis and should not be presented as the observed qe at the optimum low-concentration batch condition. The article frames its waste-battery precursor as economical, but no normalized preparation cost or complete process-energy inventory has been established in this extraction.

## EV-SEM-005 — GO–ZnAlNi LDH / CIP (2025)

**Primary source:** Sikri et al., *Graphene oxide/layered double hydroxide composite as highly efficient and recyclable adsorbent for removal of ciprofloxacin from aqueous phase*, DOI [10.3389/fnano.2025.1578620](https://doi.org/10.3389/fnano.2025.1578620); [full article](https://www.frontiersin.org/journals/nanotechnology/articles/10.3389/fnano.2025.1578620/full).

**Extracted:** batch tests used 20 mL, 0.225–10 mg/L CIP, composite dose 1–12 mg/L, pH 3–11, and 0–4 h contact at 180 rpm. The paper reports 84.84% removal at C0 1 mg/L, composite dose 10 mg/L, pH 7 and 60 min. Reuse results decline from 80.4% removal at cycle 1 to 27% at cycle 5. Freundlich R² is reported as 0.95, better than Langmuir; Temkin R² is 0.90.

**Critical audit point:** Reported capacity values are inconsistent across the article. It reports 84.84% at C0 1 mg/L and dose 10 mg/L, elsewhere reports 97.43 mg/g for a stated 1 mg/L, 10 mg/L condition, and Table 3 lists 106.9 mg/g for the current material. These need reconciliation against calculations, figure data and supplementary material. Until resolved, the removal percentage can be cited with its condition and the discrepancy disclosed; do not use one capacity value as authoritative. The reuse loss is also substantial and should temper the article’s positive characterization of recyclability.

## EV-SEM-006 — magnetic GO/fibrillated cellulose / TC (2025)

**Primary source:** Dang et al., *Integration of magnetic graphene oxide and office waste paper-derived fibrillated cellulose into a composite adsorbent for effective tetracycline elimination*, DOI [10.1039/D5RA00877H](https://doi.org/10.1039/D5RA00877H); [full article](https://pubs.rsc.org/en/content/articlehtml/2025/ra/d5ra00877h).

**Extracted:** M-GO/PFC composite; batch dose tests at C0 TC 70 mg/L and contact 960 min, with observed qe 93.36 ± 3.85 mg/g at 0.50 g/L and 59.52 ± 0.11 mg/g at 1.17 g/L; optimum pH for subsequent tests was 5. Sips fitted qm = 130.11 mg/g (R² 0.988), while the Langmuir fitted value was 107.06 mg/g (R² 0.916). The pseudo-second-order model predicts qe 87.74 mg/g (R² 0.997). Five-cycle removal decreases from 88.33% to 75.38%.

**Cost relevance:** The methods use modified-Hummers GO synthesis, magnetite functionalization, 5% NaOH, 2% NaClO, 40% H2SO4 cellulose hydrolysis, 360 W ultrasonication and 48 h lyophilization at −40°C. The paper emphasizes low-cost waste paper, but a quantified whole-process cost/energy inventory was not found in the extracted article sections. The preparation burden is therefore a real unresolved part of the “low-cost potential” question.

## EV-SEM-007 — CMC-functionalized magnetic GO / TC (2025)

**Primary source:** *Carboxymethylcellulose functionalized magnetic graphene oxide for the efficient removal of tetracycline from aqueous media*, DOI [10.1039/D5RA06621B](https://doi.org/10.1039/D5RA06621B); [full-text record](https://pmc.ncbi.nlm.nih.gov/articles/PMC12458999/).

**Extracted:** reported TC removal 96.04% in 25 min at pH 5 and dose 0.1 g/L; Langmuir fitted qmax 54.73 mg/g; saturation magnetization 50.69 emu/g; reuse reportedly changes removal from roughly 96% to 92% after ten cycles.

**Audit point:** The initial TC concentration and exact eluent/protocol conditions for ten-cycle regeneration have not been captured in this pass. The PMC web interface limited direct line-by-line access, so verify full methods and supplementary information before treating this as completed full-text extraction. The pseudo-second-order fit is not proof of chemisorption.

## EV-SEM-008 — DTPA-functionalized magnetic GO / CIP + TC (2018; abstract-only)

**Primary source:** Li et al., *Performance of magnetic graphene oxide/diethylenetriaminepentaacetic acid nanocomposite for the tetracycline and ciprofloxacin adsorption in single and binary systems*, DOI [10.1016/j.jcis.2018.03.003](https://doi.org/10.1016/j.jcis.2018.03.003); [PubMed record](https://pubmed.ncbi.nlm.nih.gov/29567603/).

**Extracted:** abstract confirms CIP and TC were tested separately and in binary solution, with pH, ionic strength and foreign ions affecting removal. TC showed stronger inhibition from competing antibiotic than CIP. Abstract states pseudo-second-order kinetics, Freundlich equilibrium and good reuse.

**Limit:** Numeric capacities, detailed batch conditions, and exact regeneration results are not extracted. This study is a priority because it directly connects the two target antibiotics, but it is **not yet approved for the quantitative evidence table** until the full text is obtained.

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

### EV-SEM-010 — magnetic guar-gum/GO composite for CIP (2023)

**Primary source:** DOI [10.1016/j.jece.2023.110766](https://doi.org/10.1016/j.jece.2023.110766); [publisher record](https://www.sciencedirect.com/science/article/pii/S2213343723015051).

The indexed abstract reports a maximum capacity of 555.56 mg/g, with Langmuir isotherm and pseudo-second-order kinetic fits. It describes a two-step synthesis using improved-Hummers GO and then a magnetic guar-gum/GO nanocomposite via co-precipitation. Exact C0, adsorbent dose, model R², cycle number and regeneration retention remain to be verified. A nearby result snippet described 67.6% removal for CSN@GO, which is not the same material name; that percentage is deliberately not assigned to mGG/GO NC.

### EV-SEM-011 — sodium alginate/GO hydrogel beads for PRB application (2018)

**Primary source:** Zhao et al., DOI [10.1016/j.chemosphere.2018.02.157](https://doi.org/10.1016/j.chemosphere.2018.02.157); [PubMed record](https://pubmed.ncbi.nlm.nih.gov/29510369/).

The primary abstract reports GSA hydrogel beads used as permeable reactive barrier backfill for ciprofloxacin-contaminated groundwater, maximum capacity 100 mg/g at pH 7, pseudo-second-order kinetics, and flow-through column tests varying flow rate, influent concentration and ionic strength. The abstract says PRB lifetime and cost were calculated, making this a high-priority source for the practical-feasibility section. It also contains a model-description conflict: the abstract says the isotherm follows Freundlich but attributes the 100 mg/g maximum capacity to Langmuir. The source full text must resolve this; cost values, column parameters, lifetime assumptions and model table must be extracted before use.

