# SEM-045 targeted source, model and mechanism audit (2026-10-31)

## Candidate / source identity

Jahan et al., “Fabrication of a magnetic graphene oxide-supported hexagonal cobalt MOF for fast and effective removal of tetracycline in water,” *RSC Advances* 16(41) (2026), 49206–49219, DOI 10.1039/d6ra02920e. Official RSC-hosted PMC full text inspected. PMID 42630936. The RSC page gives article date 21 August 2026 and collection date 16 September 2026. The study uses spent Li-ion battery graphite as its GO precursor.

Official full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC13494955/

## 1. Trace-concentration removal

Methods §2.7 (official full text) states 20 mL TET batch volume, adsorbent dosage range 0.05–0.6 g/L, initial concentration range 0.05–10 mg/L, pH 3–11, 250 rpm and contact time 1–60 min. Kinetic tests varied time; isotherm tests varied C0 across 0.05–10 mg/L; thermodynamic tests used 25, 35 and 45°C.

At the trace-condition point:
- C0 = 0.2 mg/L
- V = 20 mL = 0.020 L
- m-GO/Co-MOF = 2 mg = 0.002 g (0.1 g/L)
- pH = 7; T = 25°C; 250 rpm
- Abstract reports 98% removal.
- Figure 4 time-effect paragraph reports approximately 97% at equilibrium around 20–30 min.
- Figure 4 caption states the conditions above.

The abstract and Figure 4 narrative values are not identical; preserve them as separate source-reported endpoints rather than choosing one. On the abstract's 98% result, the source conditions imply 0.004 mg initial TET and a 2 mg/g absolute feed-mass ceiling; the calculated qe is approximately 1.96 mg/g. This is a mass-balance-derived check, not a directly measured/source-quoted qe.

## 2. Kinetic-model inconsistency

Table 2 reports:
- PFO fitted qe = 0.5270 mg/g; R² = 0.9540.
- PSO fitted qe = 19.5198 mg/g; R² = 1.000.
- Elovich and Weber–Morris parameters are reported separately.

Figure 5's caption confirms the kinetic fit uses C0=0.2 mg/L, dose=0.1 g/L, pH7, 25°C and 250 rpm. At 20 mL and 0.002 g sorbent, the maximum feed-limited qe is 2 mg/g. Therefore the PSO fitted qe is approximately 9.76 times the entire TET mass available per unit sorbent and cannot represent physical uptake under the stated conditions. The PFO fitted value is below the mass ceiling but remains a separate model output, not the observed value. A perfect PSO R² does not make the fitted qe physically consistent and does not establish chemisorption. Preserve the reported fit; do not invent a corrected value.

## 3. Isotherm caption / Methods inconsistency

Methods §2.7 explicitly states that isotherm experiments varied initial TET concentration from 0.05 to 10.0 mg/L. However, Figure 6's caption states C0=0.2 mg/L for the Langmuir, Freundlich and Temkin isotherm plots (alongside pH7 and dose0.1g/L). This is an unresolved within-paper methods/caption inconsistency; do not silently assume that the figure caption is a harmless typo or that a complete concentration series is confirmed by the caption.

Table 3 reports linear Langmuir q_m=74.18, 127.71 and 185.87 mg/g at 25, 35 and 45°C respectively (R²=.9959, .9769, .9945). Freundlich R²=.9740, .9687 and .9530; Temkin R²=.8760, .8963 and .9511. The maximum stated Methods concentration (10 mg/L) with a 0.1 g/L dose gives a feed-loading ceiling of 100 mg/g. The 127.71 and 185.87 mg/g fitted q_m values exceed that maximum experimental feed loading, indicating model extrapolation beyond the maximum feed loading, not an observed uptake. Keep all q_m as fitted model outputs, separate from the trace-condition removal and derived qe. The figure-caption uncertainty further limits their provenance.

## 4. pH / speciation and mechanism

The paper reports pHpzc=3.0, and gives TET pKa values around 3.3, 7.7 and 9.7. It describes the zwitterion as dominant approximately pH3.3–7.7. At the pH7 optimum, the surface is above pHpzc and is expected to have a negative net surface character, while TET is predominantly zwitterionic. The paper states that electrostatic repulsion is minimized; avoid simplifying this to a simple net-charge attraction model.

The authors propose electrostatic effects, π–π stacking, hydrogen bonding, Co²⁺ coordination and pore filling. The methods identify FTIR instrumentation for characterization of synthesized materials; microscopy, XRD and BET characterize the prepared composite. In the inspected source sections, no direct post-adsorption FTIR/XPS binding-state spectrum or quantitative partition of force contributions was identified. The claim of chemisorption relies in part on PSO fitting, whose qe is inconsistent with the same-condition feed ceiling.

**Mechanism grade: M1 — plausible multi-pathway interpretation; individual interactions not isolated.** Prepared-material characterization and pH/speciation response support hypotheses, but do not prove unique/dominant mechanisms or chemisorption.

## 5. Reuse and practical applicability

The paper reports magnetic separation and methanol regeneration over 10 reuse cycles, with removal declining from approximately 98% to 91%. Methanol volume/recovery, adsorbent loss, mass yield and solvent-recovery balance are not quantified. All batch experiments use ultrapure DI water (Methods §2.1); no actual real-water test or competing-ion/humic-acid interference set was located in the inspected results. No normalized cost, energy or cost-per-volume/mass-treated inventory is reported. Waste-battery graphite is a potential feedstock advantage but its recovery uses aqua-regia purification and GO oxidation uses concentrated acid/oxidant, while Fe/Co salts, methanol/ethanol washing and drying also carry uncosted burdens.

## Repository propagation

Updated without adding a new evidence ID:
- `data/semester-mechanism-evidence-matrix.csv`: corrected SEM-045 M1 grade and Figure 6 provenance limitation.
- `evidence/semester-paper/SEMESTER_CORE_EVIDENCE_EXTRACTION.csv`: EV-SEM-041 model and mechanism caveats.
- `data/semester-evidence-readiness-audit.csv`: q_m provenance, feed ceiling and mechanism caveats.
- `data/semester-condition-labelled-comparison.csv`: added condition-labelled SEM-045 record; observed, fitted and derived metrics remain separate.
- `data/semester-remaining-work-register.csv`: targeted source QA closed; citation reconciliation remains.
- `data/semester-paper-candidate-register.csv`: screening action updated.

## Citation / scope boundary

DOI 10.1039/d6ra02920e was absent from the last checked 173-entry Zotero Better BibTeX export. No citation key was guessed, no entry was added to the curated manuscript bibliography, and no manuscript citation was inserted. SEM-045 is a candidate/evidence record pending actual Zotero key reconciliation and final selection. Journal quartiles were not consulted or used.
