# Semester paper — first comparative evidence synthesis

**Status:** Working synthesis from the currently extracted evidence; not a final systematic-review result or a manuscript-ready ranking.  
**Last updated:** 29 October 2026  
**Approved scope:** Selected graphene-based adsorbents and selected graphene-bearing composites for ciprofloxacin (CIP) and tetracycline (TC).  
**Evidence source of truth:** `evidence/semester-paper/SEMESTER_CORE_EVIDENCE_EXTRACTION.csv` and `SEMESTER_CORE_EVIDENCE_NOTES.md`.

## 1. Where we are

The candidate register has 44 study records. The core evidence CSV has 24 dedicated semester evidence records; relevant evidence already extracted in the broad corpus is cross-referenced via `data/semester-main-corpus-crosswalk.csv` rather than duplicated. These are evidence records, not 24 final accepted studies: some are full-text extracted; others rely on indexed text or abstracts and still lack table-level verification.

Two of the newest fully extracted papers were already available in the user's Library, and a further in-scope N-rGO paper is already fully extracted in the broad corpus:
- Shah et al. (2025), sulfonated graphene oxide (SGO) for CIP, DOI [10.1021/acsomega.4c11231](https://doi.org/10.1021/acsomega.4c11231).
- Li et al. (2025), PGOT@GEL graphene-oxide-based hydrogel for CIP, DOI [10.1016/j.psep.2025.107659](https://doi.org/10.1016/j.psep.2025.107659).
- Zhang & Wu (2022), nitrogen-doped reduced graphene oxide (N-rGO) for six trace antibiotics including TC, DOI [10.1002/jeq2.20415](https://doi.org/10.1002/jeq2.20415); its existing evidence IDs are EV-B10-004–EV-B10-009 under broad candidate CORP-031. A mass-balance/unit discrepancy means its fitted capacities are not safe to rank as validated performance.

No new download is required from the user. The DDMGO dual-antibiotic paper and the groundwater PRB study remain less completely verified, but the project proceeds without them.

## 2. Initial study-level performance comparison

This table is deliberately not a ranking. The values come from different concentrations, doses, solution matrices, pH values, timepoints, temperatures and model definitions.

| Study / material | Target | Reported performance | What the result actually means | Key caveat |
|---|---|---|---|---|
| Ghadim et al. (2013), graphene oxide (GO) | TC | Langmuir fitted (q_{max}=322.43) mg/g at 298 K; kinetic equilibrium described within 15 min | Fitted maximum and kinetic observation are separate outcomes | Kinetic experiments used pH 3.6, while equilibrium tests are described at pH 6–7; release/desorption is not proof of multi-cycle reuse |
| GO/calcium-alginate composite fibers (2018) | TC | Fitted Langmuir (q_{max}=131.6) mg/g; measured (q_e=17.6) mg/g at (C_0=10) mg/L and (65.4) mg/g at (C_0=60) mg/L | Measured uptake varies with starting concentration; fitted (q_{max}) is not the same as either measured value | No multi-cycle regeneration result identified in extracted sections; freeze-drying is a preparation burden |
| MnFe₂O₄-decorated reduced GO (2018) | TC | About 41 mg/g at (C_0=10) mg/L; near-equilibrium around 8 h; reported pH optimum 3.3 | Condition-specific uptake, not an isotherm (q_{max}) | HCl regeneration; cycle removal reportedly declines from about 86% initially to 71% in later reuse; cycle indexing must be visually checked |
| DTPA-functionalized magnetic GO (Li et al., 2018) | CIP + TC | Kinetic model-derived (q_e=111.73) mg/g for CIP and (294.12) mg/g for TC | These are pseudo-second-order model-fitted (q_e), not Langmuir (q_{max}) | Indexed primary text supports the conditions, but numeric figures/tables are not visually verified; use values cautiously until exact primary tables are available |
| Zn–C battery-derived GO (2024) | CIP | Langmuir fitted (q_{max}=419.62) mg/g at 30°C; 99.0% removal under (C_0=2) mg/L, dose 20 mg/L, pH 5.7, 20 min | Fitted capacity and low-concentration removal describe different experimental outputs | Quantified manufacturing cost and complete process inventory were not established |
| Sulfonated GO (Shah et al., 2025) | CIP | Langmuir fitted (q_{max}=1000) μmol/g (=331.35 mg/g); experimental (q_e=237.12) μmol/g (=about 78.6 mg/g) at (C_0=50) μmol/L, pH 4, 25°C | High fitted capacity coexists with a substantially lower observed uptake at a specified concentration | Paper also reports 96.53% removal for nominally the same condition; mass-balance check from the listed (q_e), dose and concentration implies about 94.85%, so record a source consistency flag |
| GO–ZnAlNi-LDH composite (Sikri et al., 2025) | CIP | At 1 mg/L CIP, 10 mg/L composite, pH 7 and 60 min: 84.84% removal; equation implies q_e≈84.84 mg/g for these conditions | Kinetic Table 1 also reports model-fitted q_e≈106.96 mg/g, which conflicts with the stated dose/removal mass balance; best isotherm fit is Freundlich, not Langmuir | Use condition-specific removal only; capacity claims remain unresolved. Removal declines from 80.4% to 27% by cycle 5. Preparation includes metal salts, 3.4 M NaOH, 120°C/16 h hydrothermal treatment and extensive washes; no quantified cost |
| Magnetic GO/fibrillated-cellulose composite (2025) | TC | Sips fitted (q_m=130.11) mg/g; measured (q_e=93.36\pm3.85) mg/g at 0.50 g/L dose and (C_0=70) mg/L | Sips (q_m), Langmuir (q_m), kinetic-model (q_e), and measured (q_e) must stay separate | Strong-acid cellulose hydrolysis and 48 h lyophilization; five-cycle removal falls from 88.33% to 75.38% |
| CMC-functionalized magnetic GO (2025) | TC | Linear Langmuir (q_m=54.73) mg/g at 50°C; 96.04% removal at (C_0=2) mg/L, dose 0.1 g/L, pH 5, 25°C and 25 min | The 54.73 mg/g value is a *fitted value at 50°C*; mass-balance-derived uptake for the 25°C removal test is about 19.21 mg/g | Methanol regeneration; ~96% to ~92% removal over ten cycles; extensive synthesis but no whole-process cost calculation |
| PGOT@GEL engineered GO hydrogel (Li et al., 2025) | CIP | Langmuir fitted (q_{max}=821.24) mg/g (R²=0.9908); separate RSM validation measured (q_e=807.54) mg/g at (C_0=296.52) mg/L, pH 6.70, dose 5.08 mg and 298.88 K; separate pH-test (q_e=192.24) mg/g with 96.12% removal at pH 7 | These are three different outputs/conditions and should not be collapsed into one “capacity” | Multi-step P-doping/TETA/β-CD/AMPS hydrogel synthesis; methanol soaking for 12 h/cycle; seven-cycle retention ~90.53%; main text and Fig. 12 caption differ on whether water samples are real or simulated |
| N-rGO (Zhang & Wu, 2022; existing broad-corpus evidence CORP-031) | TC (among six antibiotics) | Kinetic-table qe range 80.58–90.21 mg/g across tested antibiotics; fitted Langmuir q_m for TC 662.25 mg/g; TC described as fastest to adsorb (within ~30 min); up to eight cycles, capacity decline no more than ~25% as reported | A relevant graphene-derived, trace-antibiotic study with matrix-interference and reuse evidence, already in the main corpus | The source's trace-feed/dose details imply an illustrative mass-balance ceiling around 80 mg/g, while some reported kinetic qe and fitted q_m are higher; keep the paper in qualitative synthesis but quarantine its capacity values pending unit/mass-balance reconciliation. Preparation uses strong chemistry and 180°C/24 h autoclaving; no cost inventory reported |
| Zhu et al. (2015), graphene vs GAC benchmark | CIP | Abstract reports graphene equilibrium in ~3 min and Langmuir-fitted q_max=323 mg/g; publisher abstract also covers pH/speciation, ionic strength, 5 mg/L NOM and river/drinking water | Abstract-level primary-source finding; GAC is benchmark only | Full Methods/tables/figures are not available in the current Library view; keep 323 mg/g provisional and out of a final capacity rank until conditions are verified |
| CNF/GO hybrid aerogel (Yao et al., 2017) | TC | Fig. 7 TC removal=82.1%; Langmuir theoretical/fitted q_m=454.6 mg/g in abstract/Results and 454.5 mg/g in Conclusion; kinetic-model q_e=84.8 mg/g; ten-cycle TC removal=78.9% | Removal, fitted isotherm q_m and model-fitted kinetic q_e are separate endpoints; preserve the article's small q_m rounding difference | General method 8 mg/40 mL at 25°C overnight, 160 rpm, feed range 1–100 mg/L; Fig. 7 does not state exact C0. Preparation includes 30 min ultrasonication, freezing and 48 h vacuum freeze-drying; regeneration uses 5 wt.% NaOH for 5 h plus repeat freeze-drying; costs not quantified |
| Graphene at 200 µg/L per antibiotic in a seven-drug mixture (Peng et al., 2016) | TC | Graphene equilibrium about 2.5 h; removal range across seven drugs is 89.3–100%, but exact TC percentage is figure-based and not inferred | Useful low-concentration mixed-solute evidence; no conventional q_max extracted | Kinetic-model q_e is in µg/g and not q_max; biochar results are excluded from this paper's core matrix; no graphene cost or multi-cycle reuse inventory located |
| GO nanosheets (Rostamian & Behnejad, 2018) | CIP + TC (doxycycline also studied; not pooled) | Publisher summary reports CIP model-derived capacity up to 173.4 mg/g; pH ~6–7 and contact time ~100–200 min described as optimum; no numeric TC capacity extracted from the accessible abstract | Useful cross-target GO primary study; model-specific capacity is not measured qe | Exact per-target table values, conditions and fitted model need full-text verification; keep TC quantitative cell blank and cost unreported |
| GO for CIP/NOR/OFL (Yadav et al., 2018) | CIP | Abstract reports a strong pH effect relative to concentration, contact time and dose; no numeric CIP capacity extracted | Qualitative pH/mechanistic coverage only, not a numerical ranking datum | Modified Hummers–Offeman preparation confirmed by abstract; all capacity/removal values and mechanism detail remain unverified from accessible abstract text |
| Magnetic GO sponge (MGOS) for TC (2017) | TC | Publisher abstract reports “adsorption capacity” 473 mg/g, about 50% higher than GO; pseudo-second-order fit and modest pH/ionic-strength effects | Reported endpoint remains metric-unresolved in the abstract excerpt | Do not label 473 mg/g as qmax or compare it numerically until the full table/conditions are verified; lyophilization and Fe₃O₄ addition are uncosted process inputs |
| Rostamian & Behnejad (2018), GO nanosheets | CIP + TC | Abstract reports CIP maximum capacity up to 173.4 mg/g from the fitted Sips model; TC-specific numeric capacity not available in the accessible abstract | One primary study spans both target antibiotics, with pH around 6–7 and contact-time region 100–200 min described as favorable | Abstract-level only; do not infer a TC capacity or treat CIP qmax as measured qe; no quantified cost/reuse extraction |
| Yadav et al. (2018), GO for fluoroquinolones | CIP (plus NOR/OFL separately) | Abstract confirms pH effect and best-fit models but gives no numeric CIP capacity/removal | Qualitative condition/mechanism context only | Abstract-level; figure correction later replaced original Figs. 10–13, so figure-based claims require the corrected figures |
| Magnetic GO sponge (2017) | TC | Abstract reports an adsorption-capacity figure of 473 mg/g and ~50% higher uptake than GO, but the precise fitted-versus-observed endpoint is not clear from the accessible excerpt | Potentially high-performing magnetic graphene composite | Keep 473 mg/g out of ranking until the primary table establishes metric and conditions; lyophilization and full cost/reuse burden unquantified |
| GO–sodium alginate hydrogel/aerogel (Fei et al., 2016; canonical SEM-026, SEM-041 alias) | CIP | Primary abstract reports ~7–9× capacity increase vs alginate-only gel and good Langmuir fit; a secondary source lists q_m=86.12 mg/g | Immobilized GO addresses handling, but gel form and capacity definition matter | q_m is not primary-table verified in this extraction; no cost inventory or confirmed multi-cycle reuse |
| Chitin/nGO hybrid (González et al., 2018) | CIP | Batch isotherm and continuous-flow column work; real-water samples spiked with CIP; 0.1 M NaOH regeneration | Valuable process/application evidence beyond batch-only tests | Indexed “100 g” sorbent quantity conflicts with tiny column geometry; no exact column capacity is reported here until this inconsistency is checked |
| GO sheets (Chen et al., 2015) | CIP (SMX separate) | Abstract reports maximum sorption capacities 379 mg/g for CIP and 240 mg/g for SMX; low-pH CIP sorption destabilized the GO suspension | Directly supports importance of ionic strength, pH and colloidal stability | Abstract-level model value only; keep SMX separate and do not present the maximum as observed qe |
| MgO/chitosan/GO nanosheets (Nazraz et al., 2019) | CIP (NOR separate) | Abstract reports Langmuir maximum capacity 1111 mg/g for CIP and kinetic equilibrium after >120 min | High-capacity graphene-bearing composite lead with mesoporous structure | Abstract-only, unusually high fitted capacity; verify primary table before ranking. No cost inventory or regeneration-cycle result in the abstract |
| GO nanosheets (Gao et al., 2012) | TC (OTC/DOX separate) | Abstract reports Langmuir/Temkin fits and fitted Langmuir q_max=313 mg/g, described as close to measured data; PSO k=0.065 g mg⁻¹ h⁻¹ | Solution chemistry: capacity reportedly declines with increasing pH or Na⁺ | Abstract-only; dose/C0/time/pH/temperature conditions unavailable; do not rank against 2013 GO q_max until conditions and metric definitions are aligned |
| GO nanoparticles (Ghadim et al., 2013; full text reviewed) | TC | Langmuir fitted q_max=322.43 mg/g at 298 K (abstract rounds to 323); article also lists 101.87 at 303 K and 73.53 at 308 K | Full text provides separate general, pH, kinetic and isotherm condition sets; TC pH effect peaks around pH 7 in that pH experiment | The large temperature change is as reported but must be checked against Table 2/source conditions; do not claim universal temperature behavior or rank without conditions. Desorption ≠ confirmed multi-cycle regeneration; cost unreported |
| GO/Ca-alginate–PAM double-network beads (Choi & Choi, 2022) | CIP | Langmuir fitted qₘ=6.846 mg/g (b=0.132 L/mg, R²=0.991); isotherms 1–50 ppm, 0.05 g beads, stated 55 mL, 250 rpm, 24 h at room temperature; temperature series 10–40°C reports increasing qₑ | Fitted capacity and thermodynamic trends are reported, but no directly usable observed qₑ or removal percentage was located in the extracted text | Source says 50 mL conical tube but 55 mL contact volume; flag without correction. No reuse/regeneration result or quantified cost/yield/energy inventory |
| GO/PVA/calcium-alginate beads (Hossain et al., 2026) | CIP | Reported observed qₑ maximum 7.15 mg/g; removal ~89.82/89.92% in different tests; linear/nonlinear Langmuir qₘ=8.210/10.14 mg/g; nonlinear PSO fitted qₑ=4.458 mg/g | Article provides direct observed and modeled endpoints, but they are different metrics/conditions | D–R linear/nonlinear outputs strongly disagree; linear PFO k₁ is negative; cost assumption uses 0.1 g/L vs experimental 0.5 g/50 mL (=10 g/L); 50 mL tube/55 mL volume discrepancy; cost-per-CIP claim not reproducible from stated basis |
| GO/Co–Fe magnetic nanocomposite (Hossain et al., 2024) | TC only (CTC/OTC/DTC separate) | TC removal 94.1% in abstract/body vs 93.94% in concentration section at C₀=0.2 mg/L, dose 0.15 g/L, pH 7, 30 s, 25°C; Langmuir fitted qₘ=64.10 mg/g at 50°C | A highly relevant low-concentration target-specific removal and magnetic-recovery case; qₘ and removal come from different temperatures/tests | Preserve the 94.1/93.94% source mismatch; regeneration values are not fully TC-cycle-pinned; waste-cell source does not establish low cost; no real-water or cost inventory |
| EDTA-functionalized magnetic GO (mGO/EDTA, 2026) | TC | Removal 93.23% at C₀=0.2 mg/L, dose 0.10 g/L, pH 5, 5 min, 25°C; mass-balance qe≈1.865 mg/g; Langmuir fitted q_max=31.32 mg/g (25°C, R²=.691), Freundlich fits better; eight cycles ~94%→90.50% | Fast low-concentration removal and magnetic recovery are useful; use the condition-specific observed removal rather than headline qmax | PSO fitted qe=0.01937 mg/g (R²=1) conflicts by ~96× with mass balance; acid/oxidant/Fe/EDTA/methanol process; no quantified cost |
| GO/calcium-alginate fibers (Wu et al., 2013) | CIP | Wet-spun GO/CA fibers; pH optimum 5.9, equilibrium 24 h; 78.9% removal at 2 g/L dose and 6 wt% GO; reported capacity 18.45→39.06 mg/g as GO loading goes 0→6 wt% at equilibrium C=60 mg/L | Source-reported capacity is a measured/condition-specific result, not a fitted qmax; supports immobilization/handling comparison | Only abstract/snippets available; full wet-spinning recipe, numeric Freundlich parameters, reuse and cost not available; removal and 60 mg/L equilibrium-capacity point should not be merged until paired conditions verified |
| GO·Fe₃O₄ magnetic graphene oxide (2022; DFT + experiment) | TC | Abstract reports capacity 531.93 mg/g at C₀=1000 mg/L, 50 mg adsorbent, pH 7 and 293 K; solution volume and fitted-vs-observed definition are unavailable | Potential experimental plus computational material-design evidence, but the headline capacity lacks enough conditions for independent mass balance | Do not label 531.93 mg/g qₑ or qmax without the primary table; separate DFT binding energy/spin/HOMO–LUMO outputs from adsorption results; no cost or numeric reuse data in accessible preview |
| GO–[Ni(DMG)]ₙ composite (2026) | CIP | Langmuir-comparison qmax 117–159 mg/g across formulations; high removal over pH 2–7; PSO rate constants 0.0005–0.0009 g/(mg·min) | A useful recent coordination-functionalized GO lead, but quantitative source excerpt is only abstract-level | Freundlich/Temkin reportedly fit isotherms better; exact C₀, dose, temperature, formulation-specific qmax/R², reuse, real-water and cost data unavailable; do not treat the capacity range as observed qe |
| Fe₃O₄/GO magnetic composite under ultrasonic treatment (2023) | CIP | 96.39% removal at C₀=15 mg/L, dose 0.55 g/15 mL (=36.7 g/L), pH 7, 33 min; tap/river/lake/wastewater removal 94.12/91.66/90.65/89.96%; seven-cycle regeneration claim | Water-matrix and reuse claims are useful, but the very high dose and ultrasound-assisted condition change practical comparability; mass-balance implies qe≈0.394 mg/g at stated optimum | No qmax/fit parameters in accessible extraction, no ultrasound power/energy or cost. Keep derived qe separate from source metrics and do not assume no transformation without direct evidence |
| Magnetic chitosan-grafted GO (2016; abstract-level) | CIP | Langmuir fitted qₘ=282.9 mg/g; PSO kinetics; ~72% of initial capacity after four uses; Na⁺ 200 mM and Ca²⁺ 10 mM suppress adsorption | Model-capacity and reuse/salt information are available at abstract level | Exact C₀/dose/pH/time/temperature, fit statistics, synthesis recipe, regeneration eluents and cost are not accessible; keep qₘ separate from measured qe |
| Chitin:nGO 3:1 hybrid (González et al., 2018) | CIP | Batch Sips fit best; Langmuir fitted qₘ=73±3 mg/g (pure nGO 282±11 mg/g); dynamic Thomas q₀/YN τ and spiked tap/well water values tabulated in EV-SEM-021 | Separates batch fitted capacity from continuous-flow/modelled dynamic endpoints; application evidence is unusually valuable | Accepted manuscript literally states 100 g in a 1.0-cm-ID × 1.5-cm-bed column, a physically impossible ~84.9 g/cm³ implied density. Quarantine every column q₀/τ from ranking; do not guess intended mass. Spiked real water, not naturally contaminated; no quantified cost inventory |
| GO/alginate PRB hydrogel beads (Zhao et al., 2018) | CIP | Abstract reports 100 mg/g at pH 7 and ~72 h equilibrium; flow-through PRB/column study | Potential application-focused evidence, distinct from a batch-only test | Full cost/lifetime and column details unavailable in the current extraction; the exact capacity-model definition must be checked against full tables |

**Use rule:** No universal capacity ranking should be published from this table. Even apparently similar values can refer to fitted (q_{max}), model-derived (q_e), measured batch uptake, or a selected optimized condition.

## 3. What can be synthesized now

### 3.1 Material modification changes both adsorption and process burden

GO/rGO modification can introduce more functional groups, magnetic recovery, or a recoverable hydrogel/bead format. But the preparation routes differ strongly. SGO uses a long oxidation route with concentrated acids, KMnO₄, multiple washing solvents and subsequent HCl/DMF desorption. PGOT@GEL combines GO oxidation, phosphorus doping, TETA grafting, β-cyclodextrin functionalization and radical polymerization. Magnetic GO/cellulose uses alkali, bleach, 40% H₂SO₄ hydrolysis, magnetite and 48-hour lyophilization.

Therefore, “non-conventional” is not one cost class. The review should compare **the exact synthesis route and usable treatment performance**, not just material names or reported (q_{max}).

### 3.2 High reported capacity does not by itself demonstrate low cost

The two largest extracted fitted/modelled CIP capacities in this batch are the PGOT@GEL Langmuir (q_{max}=821.24) mg/g and the Zn–C-derived GO Langmuir (q_{max}=419.62) mg/g. These are not a head-to-head result: their concentrations, dose, matrix, fitting and operating conditions differ. PGOT@GEL’s reported RSM validation uptake is a separate metric and condition from the pH-test (q_e). Neither paper supplies a complete, comparable cost per mass of CIP removed in the current extraction.

The SGO paper calls the procedure cost-effective, but does not quantify full synthesis or regeneration cost. One needs reagent quantities, product yield, energy, washing/neutralization, solvent recovery, regeneration replacement, sorbent losses and treatment capacity before making an evidence-based low-cost claim.

### 3.3 Recovery helps only when the complete regeneration step is considered

Magnetic separation can simplify solids recovery, but magnetic material synthesis adds Fe-containing reagents and can change accessible adsorption sites. Hydrogel or bead forms may improve handling, but the polymerization, crosslinking and drying route matters. The regeneration solvent or eluent is also part of the process: examples in this evidence set include 1 M HCl in DMF for SGO, 0.1 M HCl for MnFe₂O₄/rGO, methanol for CMC-functionalized magnetic GO and PGOT@GEL, and 0.01 M NaOH for DDMGO.

A defensible comparison records removal or capacity retention by cycle, cycle count, eluent concentration, contact time, washing/drying requirements and spent regeneration liquid. It should not describe “reusable” as equivalent to “low-cost.”

### 3.4 Real-water applicability is a weakly documented part of the current evidence

The GO/CIP synthetic-urine paper is a simulated matrix, not proof from actual urine or wastewater. PGOT@GEL's narrative refers to real-water samples, while its Figure 12 caption says simulated real wastewater; the identity of those matrices must be resolved before calling it true field applicability. The PRB hydrogel paper is particularly relevant because its abstract identifies groundwater and flow-through column tests, but the numeric costs and lifetime assumptions have not been extracted.

This leaves a specific evidence gap: **batch adsorption in synthetic water dominates the extracted comparisons; flow-through and well-described real-water testing are more valuable than another isolated high-capacity claim.**

## 4. Evidence limitations and how they will be handled

| Limitation | Current case | Handling rule |
|---|---|---|
| Fitted versus measured metric | GO SGO and PGOT@GEL have both fitted and test-specific values | Label every number as (q_{max}), observed (q_e), model-fitted (q_e), removal %, or column metric |
| Internal numerical consistency | SGO reported qe/removal pair; GO–LDH capacity pairs | Preserve source values plus explicit calculation flags; do not silently correct |
| Primary tables not visually verified | DDMGO and PRB studies | Use only text-confirmed content; leave numeric details unresolved |
| Matrix naming ambiguity | PGOT@GEL “real water” versus “simulated real wastewater” | Mark as ambiguous, not verified real wastewater |
| Cost evidence absence | Most papers offer qualitative “cost-effective” language | Mark cost evidence “not quantified”; compare process inputs only as proxies |
| Scope drift | Some papers additionally test gatifloxacin, ofloxacin, doxycycline or metals | Use only CIP/TC values in core antibiotic tables; other contaminants only as contextual/co-solute effects |
| Journal quartiles not yet joined | Existing papers have variable ranking-audit status | Do not state Q1-only eligibility until provider/category/year is verified |

## 5. Draft-safe synthesis paragraph

The currently extracted primary studies show that graphene-based adsorbents and graphene-bearing composites can achieve substantial ciprofloxacin or tetracycline uptake under selected laboratory conditions, but the evidence does not support a single performance ranking. Reported fitted capacities must be separated from observed uptake: for example, the GO/calcium-alginate fiber study reports a Langmuir (q_{max}) of 131.6 mg/g while the measured uptake was 17.6 mg/g at 10 mg/L initial TC and 65.4 mg/g at 60 mg/L. The same distinction is needed for functionalized GO and engineered hydrogels. Recovery formats and reuse tests also vary considerably, and some retain high removal only after lengthy solvent-based regeneration, while others show substantial performance loss over a few cycles. Although several papers describe their adsorbents as economical, complete, comparable cost inventories are absent from the extracted evidence. Accordingly, the low-cost potential of these systems should be assessed using the full preparation and regeneration burden, concentration-specific performance, and matrix/column evidence, rather than precursor origin or maximum fitted capacity alone.

This paragraph is a working synthesis, not final manuscript prose; it should be updated after more primary studies pass screening.

## 6. Visual plan for the paper

Retain the supplied review's table-heavy style while making the tables evidence-led and original.

### Tables
1. CIP and TC properties relevant to adsorption and speciation.
2. GO/rGO and functionalized-GO primary-study evidence table.
3. Magnetic/immobilized/composite study evidence table.
4. Performance comparison with columns for measured (q_e), fitted (q_{max}), removal %, conditions, matrix and metric definition.
5. Mechanism evidence matrix distinguishing direct characterization, competition/pH evidence and theoretical/model interpretation.
6. Practical-feasibility matrix covering process steps, reagents, energy/drying, recovery, regeneration, real-water/column evidence and quantified-cost availability.

### Original figures
1. Material taxonomy limited to the two approved families.
2. Preparation/functionalization route map for the selected materials.
3. CIP/TC speciation and proposed interaction map, clearly distinguishing experimentally supported from hypothesized interactions.
4. Performance–preparation–recovery–cost trade-off schematic; do not show a universal “winner” where evidence is not comparable.

The final manuscript's numbering/placement must follow the AMU department or target-journal requirements.

## 7. Next work without new downloads

1. Continue screening existing Library PDFs against the approved two-family/two-antibiotic scope.
2. Strengthen primary-source evidence for the best available CIP/TC studies; keep inaccessible tables marked as gaps rather than delaying all work.
3. Finish the title/DOI duplicate check and join the existing journal-quartile audit.
4. Extract any available column/real-water details already in the corpus.
5. Build the comparison tables and figures only after the evidence categories and metric labels are stable.

**No action is required from the user right now.** The workflow will continue using the files and sources already available.


## Corpus cross-reference added after repository audit

The approved semester scope now includes one additional existing study as SEM-038, cross-linked to CORP-031 rather than re-extracted into duplicate evidence rows. Its TC results are directly on-scope, but its reported capacity values have an unresolved dose/concentration mass-balance concern. Include it in evidence-coverage and mechanism discussion; keep numerical q_m out of ranking until reconciled.

The earlier suggested downloads for SEM-006 and SEM-037 are no longer user actions. Their source-access gaps remain documented, and the review proceeds with existing evidence.


## Existing-source review update — 29 October 2026

Three more on-scope candidate records now have source-linked evidence: SEM-020 (CIP on graphene, abstract-level), SEM-039 (TC on a CNF/GO aerogel), and SEM-040 (TC on graphene in a mixed seven-antibiotic solution at 200 µg/L per drug). The evidence matrix keeps the abstract-level row provisional, records Yao et al.'s q_m and kinetic q_e separately, and does not infer a precise TC percentage from Peng et al.'s figure-only range. The core performance table should remain condition-aware; these are not a universal rank list.

Historical snapshot before the later abstract-screening waves: 40 candidate rows and 16 dedicated evidence rows. Current state is 44 register rows, 43 unique DOI-defined works, and 24 evidence rows. The ~50 distinct cited-work target is still open.


## Abstract-level source wave — 29 October 2026

Three already-registered candidates now have primary-source abstract evidence: SEM-002 (GO nanosheets for CIP and TC), SEM-003 (GO for CIP among fluoroquinolones), and SEM-005 (magnetic GO sponge for TC). The rows add study coverage but deliberately do not claim full-text extraction: SEM-002's numeric TC capacity and SEM-003's numeric CIP results remain unavailable from the abstract text; SEM-005's reported 473 mg/g remains metric-unresolved. These values should stay out of any cross-study numerical ranking until the source tables/conditions can be verified.

Historical snapshot during the third abstract-level source check: 40 candidate rows and 19 evidence rows. Later source waves increased the live counts; no new user download is requested.


## Follow-on source wave — 29 October 2026

Four additional candidates have been registered with target-specific evidence: GO–sodium alginate gel/aerogel for CIP, chitin/nGO for continuous-flow CIP treatment, GO for CIP (with SMX kept separate), and MgO/chitosan/GO for CIP (with NOR kept separate). One additional issue from earlier abstract screening also remains material: the magnetic GO sponge abstract's 473 mg/g figure is not yet mapped to a verified fitted-versus-measured endpoint. These are leads for synthesis, not a capacity leaderboard; abstract-only and secondhand figures are clearly marked.


## Full-text / abstract audit — GO and tetracycline (29 October 2026)

SEM-001 is now explicitly source-audited against the full PLOS text, including its distinct pH/kinetic/isotherm conditions and the reported 298/303/308 K q_max values. The paper's abrupt fitted-capacity drop with temperature is flagged rather than interpreted without rechecking Table 2. SEM-024 is now backed by the primary PubMed abstract (Langmuir q_max 313 mg/g, PSO k 0.065 g mg⁻¹ h⁻¹, pH/Na⁺ effect), but full condition tables are unavailable in the current source view. These two similar GO/TC capacity figures should not be presented as a cross-study head-to-head result until study conditions are aligned.


## Source-audit refinement — GO–ZnAlNi-LDH (SEM-015)

The open publisher text resolves the practical and modeling details but not the capacity contradiction. At 1 mg/L CIP, 10 mg/L sorbent, pH 7 and 60 min, removal is 84.84%; the paper's equation implies q_e≈84.84 mg/g, while the kinetic table reports a fitted q_e≈106.96 mg/g. Do not use 106.97 mg/g as a validated q_max. The best isotherm fit in the detailed Results is Freundlich (R²=0.95), not Langmuir, and fifth-cycle removal is only 27% versus 80.4% initially. Cost-relevant preparation steps are now extracted, but no cost was quantified.


## Source-level process refinement — CNF/GO aerogel (SEM-039)

The publisher Methods now support explicit synthesis burdens: 80 mg CNF + 100 mg GO in 100 mL water; 30 min sonication at 60 kHz (stated 1000 W output) in an ice bath; freezing at −30°C for >5 h; vacuum freeze-drying 48 h at −55°C/80 mTorr. Regeneration uses 5 wt.% NaOH for 5 h, then washing and another freeze-dry. The model-derived kinetic q_e (84.8 mg/g), Langmuir q_m (454.6 in abstract/Results; 454.5 in conclusion) and removal (82.1%) remain separate outputs. Ten-cycle TC removal is 78.9%. This is useful for the preparation–performance–recovery comparison, but the paper lacks a quantified process-cost inventory and the exact Fig. 7 feed concentration remains unspecified in the caption.


## Data-integrity correction — 29 October 2026

The current candidate register has 44 rows but only 43 distinct DOI-defined works because SEM-026 and SEM-041 are duplicate records for Fei et al. (2016). SEM-026 is now canonical; SEM-041 is an alias and must not be counted as a second cited work. EV-SEM-020 is assigned to SEM-026. The schema audit also remapped EV-SEM-010 and EV-SEM-013 to the correct evidence columns, ensuring mechanistic interpretation, regeneration, cost, source location, source URL, extraction status and caveats appear under their intended headings. Numeric capacity values remain provisional as described in those records.


## Full accepted-manuscript audit — SEM-042 / Chi:nGO continuous flow (29 October 2026)

The accepted manuscript has now been checked at Methods, isotherm discussion and the dynamic/real-water tables. Batch Sips fit was best; the model-specific Langmuir qₘ is 73±3 mg/g for the 3:1 Chi:nGO hybrid versus 282±11 mg/g for pure nGO. Table 1 provides Thomas q₀ and Yoon–Nelson τ values across flow rate, pH, Na⁺ and hardness; Table 2 reports spiked real-water q₀/τ (Buenos Aires 49±4 mg/g/154±5 min; Chascomús 26.4±0.8/76±2; Macachín 23.6±0.7/67±2). **These dynamic values are quarantined** because the accepted Methods text explicitly pairs a 100-g bed charge with 1.0-cm-ID, 1.5-cm-bed geometry; the implied density is ~84.9 g/cm³. The article’s low-cost claim is not supported by a quantified cost inventory. Do not interpret the column figures as validated deployment performance until the mass statement is corrected from a reliable source.


## Primary full-text update — SEM-027 / GO/Ca-alginate–PAM beads (29 October 2026)

The open publisher article has now been extracted into EV-SEM-025. The fitted Langmuir qₘ is 6.846 mg/g (R²=0.991; χ²=0.037), with Freundlich and Temkin fits also reported. The study supplies a temperature-dependent thermodynamic analysis but the accessible paper text did not provide an explicit observed equilibrium qₑ/removal percentage for a particular condition. Method-level consistency flag: it states a 50 mL conical tube and 55 mL contact volume; that value has not been silently changed. It reports no multicycle regeneration or monetized preparation cost. The fitted qₘ is not a standalone ranking of practical value.


## Full-text updates: SEM-029 and SEM-034 (29 October 2026)

SEM-029 now has open-source primary extraction in EV-SEM-026. Its fitted qₘ and observed qe are distinct; linear/nonlinear D–R parameters and the linear PFO rate constant are anomalous. Its reported cost-per-CIP claim is not independently validated because the cost section assumes 0.1 g/L beads while the experimental section states a 0.5 g / 50 mL optimum, a 100× discrepancy. SEM-034 now has TC-only evidence EV-SEM-027: removal at 0.2 mg/L is 94.1% in the abstract/body and 93.94% in another section; Langmuir qₘ=64.10 mg/g is fitted at 50°C and must be kept separate from 25°C removal. Neither article supplies quantified full process costs that justify an unconditional low-cost label.


## Follow-on source audit — SEM-019 and SEM-028 (29 October 2026)

The full primary source for mGO/EDTA (SEM-019) reports 93.23% TC removal at C₀=0.2 mg/L and dose=0.10 g/L in 5 min at pH 5/25°C. This implies qₑ≈1.865 mg/g by mass balance, yet the paper’s best-fit PSO model gives qₑ=0.01937 mg/g with R²=1—an approximately 96-fold difference. Keep this as a data-quality issue rather than a ranking value. SEM-028 has accessible primary abstract data: GO/CA fibers at 6 wt% GO show 78.9% removal at 2 g/L and source-reported uptake 39.06 mg/g at equilibrium concentration 60 mg/L, but full method/table details are not accessible, so the results remain snippet-level and condition-separated.


## Source-preview refinements — SEM-005 and SEM-044 (29 October 2026)

The MGOS/TC preview now confirms Fe₃O₄:GO ratio 1:40 and density 4.6 mg/cm³, but not whether 473 mg/g is observed qe or fitted qmax, nor experimental conditions/reuse/cost. The MgO/chitosan/GO CIP/NOR study’s primary abstract confirms Langmuir qmax claims of 1111 mg/g CIP and 1000 mg/g NOR, but the full conditions and fitted statistics are inaccessible; the claim remains provisional. These entries help map the evidence gaps but must not be used as definitive capacity ranks.


## Primary-source update — SEM-014 and SEM-030 (29 October 2026)

The magnetic GO/TC DFT-plus-experiment study reports 531.93 mg/g at C₀=1000 mg/L and 50 mg adsorbent, but the accessible page omits solution volume and fitted-versus-measured definition; its computational output is not a sorption metric. The GO–[Ni(DMG)]ₙ study reports a Langmuir-comparison capacity range of 117–159 mg/g, while stating that Freundlich/Temkin fit the data better; exact conditions and practical cost/reuse evidence were not exposed. Both are tracked as source-level leads, not confirmed positions in a capacity ranking.


## Primary-source update — SEM-012 and SEM-025 (29 October 2026)

The Fe₃O₄/GO CIP paper reports 96.39% removal at a stated dose of 0.55 g in 15 mL (36.7 g/L) with an ultrasonic bath, and spiked water removals around 90–94%; a mass-balance check implies qe≈0.394 mg/g for the stated optimum, but this is calculated rather than reported. No ultrasound energy or numeric model parameters were accessible. The magnetic chitosan-GO CIP paper reports qₘ=282.9 mg/g and ~72% retained capacity after four uses in its abstract preview, but exact conditions and cost details remain unavailable. Both are kept distinct from condition-matched full-text comparisons.

## Evidence-completion wave — four source checks (29 October 2026)

| Candidate / study | Valid use in synthesis | Important restriction |
|---|---|---|
| SEM-008 / MGO for TC-HCl (EV-SEM-034) | pH/speciation, reported PSO/Freundlich model choice and magnetic recoverability | Primary abstract does not disclose numeric capacity; 141.44 mg/g is secondary-review-only until verified against the primary table |
| SEM-031 / SGO in multi-FQ mixtures (EV-SEM-036) | Mixture-level fitted q_m trend and five-cycle solvent/acid regeneration | 370.37/357.14/333.33 mg/g are binary/ternary/quaternary system parameters, not isolated CIP capacities |
| SEM-033 / rotating-field Fe3O4/rGO (EV-SEM-037) | High TCH removal under a specified coupled-field operating condition and four-cycle retention | No q_max/q_e, power consumption or field-free matched baseline; not evidence of low cost by itself |
| SEM-013 / rGO/CIP/TC DFT (EV-SEM-035) | Molecular mechanism/theory subsection only | No experiment, aqueous removal or adsorption-capacity metric; exclude from empirical performance comparison |

The candidate register contains 44 rows, with SEM-041 retained as an alias of SEM-026 and SEM-021 still lacking verified DOI metadata. The dedicated evidence CSV now contains 37 unique records. Evidence rows are not accepted references; abstract-level and theoretical rows must stay labelled. The target of about 50 distinct cited works remains unverified.
## Evidence readiness audit — 29 October 2026

A row-by-row QA matrix now exists at [data/semester-evidence-readiness-audit.csv](../data/semester-evidence-readiness-audit.csv). It separates source-access level, experimental versus theoretical evidence, observed endpoints, fitted parameters, known numerical contradictions, cost status, regeneration evidence, and the permitted way each study may be used in the manuscript.

Initial audit readout: the 37 records are heterogeneous. Several are primary full-text/table-backed studies, others are publisher-abstract or indexed-fragment claims, and EV-SEM-035 is DFT-only theory. Capacity/uptake flags remain on the GO–LDH condition, SGO nominal qe/removal pair, MGO/EDTA mass-balance pair, GO/PVA/alginate dose-cost calculation, accepted-manuscript chitin/nGO column mass, and several abstract-only headline capacities. No cross-study capacity leaderboard should be drafted before these caveats are carried into each row.

Cost evidence remains the weakest common dimension: most studies lack a comparable full-process cost boundary, energy/yield inputs and a cost-per-treated-volume or cost-per-mass-removed denominator. Where a paper asserts 'low-cost', the manuscript should describe that as the authors' claim unless it is supported by a quantified inventory.
## Candidate-to-manuscript inclusion shortlist — 29 October 2026

The candidate-level file `data/semester-study-inclusion-shortlist.csv` now classifies all 44 register rows by evidence linkage, source-access level, permitted quantitative use and next QA action. It prevents three common counting errors: SEM-041 is a duplicate alias, SEM-013 is DFT-only context rather than an empirical adsorption study, and SEM-038 must reuse the broad-corpus evidence rather than create duplicate extracted evidence.

Use the shortlist to draft from the most defensible condition-labelled evidence first. Abstract-only values, figure-only endpoints, cross-study fitted capacities and any mass-balance-inconsistent values should remain explicitly provisional or quarantined rather than appearing in a ranked comparison.
## Condition-labelled empirical comparison — first working table (29 October 2026)

The new file [data/semester-condition-labelled-comparison.csv](../data/semester-condition-labelled-comparison.csv) collects selected target-specific endpoints with their own initial concentration, dose, pH, temperature, time, matrix, model status, recovery and cost caveats. It intentionally is **not** a rank order: removal percentage, measured q_e, mass-balance-derived q_e, model-fitted kinetic q_e and isotherm q_max are separate types of result.

The first table includes 18 rows across TC/CIP cases with the most informative available condition data and/or documented data-integrity issues. Stronger directly condition-labelled examples include GO/calcium-alginate fibers (two observed TC q_e values at separate C₀ levels), battery-derived GO/CIP (99% removal at 2 mg/L under the stated condition), magnetic GO/cellulose TC (observed q_e=93.36±3.85 mg/g at 0.5 g/L and 70 mg/L C₀), CMC-functionalized magnetic GO/TC (96.04% removal at 2 mg/L, 0.1 g/L, pH 5, 25°C, 25 min), GO/Co–Fe/TC (94.1% vs 93.94% at 0.2 mg/L, 0.15 g/L, pH 7, 30 s), and the Fe₃O₄/GO CIP study (96.39% at a very high 36.7 g/L dose and with ultrasound). Each remains subject to the caveats in its row.

Several rows are retained because they teach important limits, not because their headline capacities are validated: SGO/CIP has a removal–q_e mass-balance inconsistency; GO–ZnAlNi-LDH has a condition/model capacity conflict and severe cycle decline; GO/PVA/alginate bead costs use a 100-fold lower dose than the experimental optimum; the chitin/nGO column study has an impossible stated packed-bed mass; EDTA-magnetic GO/TC has a ~96-fold difference between mass-balance q_e and fitted kinetic q_e. These values are visibly held from ranking.

Cost finding from the current evidence: only a small minority of the 37 extracted records has any monetized cost detail, and even one such estimate (GO/PVA/alginate beads) is not presently reproducible because its dose assumption conflicts with the experimental section. For most candidates, “low cost” is therefore a hypothesis or author claim, not demonstrated comparative economics.