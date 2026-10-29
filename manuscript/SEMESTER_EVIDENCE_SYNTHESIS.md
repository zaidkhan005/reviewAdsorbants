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
| GO–sodium alginate hydrogel/aerogel (Fei et al., 2016) | CIP | Primary abstract reports ~7–9× capacity increase vs alginate-only gel and good Langmuir fit; a secondary source lists q_m=86.12 mg/g | Immobilized GO addresses handling, but gel form and capacity definition matter | q_m is not primary-table verified in this extraction; no cost inventory or confirmed multi-cycle reuse |
| Chitin/nGO hybrid (González et al., 2018) | CIP | Batch isotherm and continuous-flow column work; real-water samples spiked with CIP; 0.1 M NaOH regeneration | Valuable process/application evidence beyond batch-only tests | Indexed “100 g” sorbent quantity conflicts with tiny column geometry; no exact column capacity is reported here until this inconsistency is checked |
| GO sheets (Chen et al., 2015) | CIP (SMX separate) | Abstract reports maximum sorption capacities 379 mg/g for CIP and 240 mg/g for SMX; low-pH CIP sorption destabilized the GO suspension | Directly supports importance of ionic strength, pH and colloidal stability | Abstract-level model value only; keep SMX separate and do not present the maximum as observed qe |
| MgO/chitosan/GO nanosheets (Nazraz et al., 2019) | CIP (NOR separate) | Abstract reports Langmuir maximum capacity 1111 mg/g for CIP and kinetic equilibrium after >120 min | High-capacity graphene-bearing composite lead with mesoporous structure | Abstract-only, unusually high fitted capacity; verify primary table before ranking. No cost inventory or regeneration-cycle result in the abstract |
| GO nanosheets (Gao et al., 2012) | TC (OTC/DOX separate) | Abstract reports Langmuir/Temkin fits and fitted Langmuir q_max=313 mg/g, described as close to measured data; PSO k=0.065 g mg⁻¹ h⁻¹ | Solution chemistry: capacity reportedly declines with increasing pH or Na⁺ | Abstract-only; dose/C0/time/pH/temperature conditions unavailable; do not rank against 2013 GO q_max until conditions and metric definitions are aligned |
| GO nanoparticles (Ghadim et al., 2013; full text reviewed) | TC | Langmuir fitted q_max=322.43 mg/g at 298 K (abstract rounds to 323); article also lists 101.87 at 303 K and 73.53 at 308 K | Full text provides separate general, pH, kinetic and isotherm condition sets; TC pH effect peaks around pH 7 in that pH experiment | The large temperature change is as reported but must be checked against Table 2/source conditions; do not claim universal temperature behavior or rank without conditions. Desorption ≠ confirmed multi-cycle regeneration; cost unreported |
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

The semester register now has 40 candidates and 16 dedicated evidence rows, while reusable broad-corpus evidence remains cross-referenced rather than duplicated. The ~50 distinct cited-work target is still open.


## Abstract-level source wave — 29 October 2026

Three already-registered candidates now have primary-source abstract evidence: SEM-002 (GO nanosheets for CIP and TC), SEM-003 (GO for CIP among fluoroquinolones), and SEM-005 (magnetic GO sponge for TC). The rows add study coverage but deliberately do not claim full-text extraction: SEM-002's numeric TC capacity and SEM-003's numeric CIP results remain unavailable from the abstract text; SEM-005's reported 473 mg/g remains metric-unresolved. These values should stay out of any cross-study numerical ranking until the source tables/conditions can be verified.

The semester candidate register remains at 40 records and the dedicated evidence file is now at 19 rows. No new user download is requested.


## Follow-on source wave — 29 October 2026

Four additional candidates have been registered with target-specific evidence: GO–sodium alginate gel/aerogel for CIP, chitin/nGO for continuous-flow CIP treatment, GO for CIP (with SMX kept separate), and MgO/chitosan/GO for CIP (with NOR kept separate). One additional issue from earlier abstract screening also remains material: the magnetic GO sponge abstract's 473 mg/g figure is not yet mapped to a verified fitted-versus-measured endpoint. These are leads for synthesis, not a capacity leaderboard; abstract-only and secondhand figures are clearly marked.


## Full-text / abstract audit — GO and tetracycline (29 October 2026)

SEM-001 is now explicitly source-audited against the full PLOS text, including its distinct pH/kinetic/isotherm conditions and the reported 298/303/308 K q_max values. The paper's abrupt fitted-capacity drop with temperature is flagged rather than interpreted without rechecking Table 2. SEM-024 is now backed by the primary PubMed abstract (Langmuir q_max 313 mg/g, PSO k 0.065 g mg⁻¹ h⁻¹, pH/Na⁺ effect), but full condition tables are unavailable in the current source view. These two similar GO/TC capacity figures should not be presented as a cross-study head-to-head result until study conditions are aligned.


## Source-audit refinement — GO–ZnAlNi-LDH (SEM-015)

The open publisher text resolves the practical and modeling details but not the capacity contradiction. At 1 mg/L CIP, 10 mg/L sorbent, pH 7 and 60 min, removal is 84.84%; the paper's equation implies q_e≈84.84 mg/g, while the kinetic table reports a fitted q_e≈106.96 mg/g. Do not use 106.97 mg/g as a validated q_max. The best isotherm fit in the detailed Results is Freundlich (R²=0.95), not Langmuir, and fifth-cycle removal is only 27% versus 80.4% initially. Cost-relevant preparation steps are now extracted, but no cost was quantified.


## Source-level process refinement — CNF/GO aerogel (SEM-039)

The publisher Methods now support explicit synthesis burdens: 80 mg CNF + 100 mg GO in 100 mL water; 30 min sonication at 60 kHz (stated 1000 W output) in an ice bath; freezing at −30°C for >5 h; vacuum freeze-drying 48 h at −55°C/80 mTorr. Regeneration uses 5 wt.% NaOH for 5 h, then washing and another freeze-dry. The model-derived kinetic q_e (84.8 mg/g), Langmuir q_m (454.6 in abstract/Results; 454.5 in conclusion) and removal (82.1%) remain separate outputs. Ten-cycle TC removal is 78.9%. This is useful for the preparation–performance–recovery comparison, but the paper lacks a quantified process-cost inventory and the exact Fig. 7 feed concentration remains unspecified in the caption.
