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

**Extracted:** The CNF/GO composite uses freeze-drying to create an interconnected 3D porous aerogel. The paper reports TC removal of 82.1% in its across-antibiotic comparison, fitted Langmuir q_m=454.5 mg/g, and pseudo-second-order model-derived q_e=84.8 mg/g. These are three separate endpoints. The batch method describes 8 mg aerogel in 40 mL solution, 160 rpm, 25°C and overnight incubation over 1–100 mg/L; some TC factor tests have different conditions, so do not assume these general conditions apply to every figure. The study used 5 wt.% NaOH for 5 h for desorption and reports ten cycles; TC removal was 78.9% after reuse versus 82.1% in the initial comparison (3.2 percentage points absolute, about 3.9% relative decline).

**Cost/feasibility:** No cost per gram, cost per treated volume, yield, GO input cost, freeze-drying energy or NaOH use per cycle was quantified. The author's statement that the material is economical is not a cost analysis.

**Audit points:** Check the figure-specific conditions for Fig. 7 and pinpoint the kinetic/isotherm tables before formal use. Do not report q_m=454.5 mg/g as observed uptake. The accessible source is publisher HTML; PDF pagination is not independently confirmed.

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
