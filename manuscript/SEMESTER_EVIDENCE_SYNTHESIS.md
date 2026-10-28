# Semester paper — first comparative evidence synthesis

**Status:** Working synthesis from the currently extracted evidence; not a final systematic-review result or a manuscript-ready ranking.  
**Last updated:** 29 October 2026  
**Approved scope:** Selected graphene-based adsorbents and selected graphene-bearing composites for ciprofloxacin (CIP) and tetracycline (TC).  
**Evidence source of truth:** `evidence/semester-paper/SEMESTER_CORE_EVIDENCE_EXTRACTION.csv` and `SEMESTER_CORE_EVIDENCE_NOTES.md`.

## 1. Where we are

The candidate register has 37 study records. The core evidence CSV has 13 evidence records. These are *evidence records*, not 13 final accepted studies: some are full-text extracted; others rely on indexed text or abstracts and still lack table-level verification.

Two of the newest fully extracted papers were already available in the user's Library:
- Shah et al. (2025), sulfonated graphene oxide (SGO) for CIP, DOI [10.1021/acsomega.4c11231](https://doi.org/10.1021/acsomega.4c11231).
- Li et al. (2025), PGOT@GEL graphene-oxide-based hydrogel for CIP, DOI [10.1016/j.psep.2025.107659](https://doi.org/10.1016/j.psep.2025.107659).

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
| GO–ZnAlNi layered-double-hydroxide composite (2025) | CIP | 84.84% removal at (C_0=1) mg/L, dose 10 mg/L, pH 7 and 60 min | A condition-specific removal value remains usable with caveat | Capacity figures conflict with the paper's stated mass-balance equation; fifth-cycle removal reportedly falls to 27%; don't rank its capacity |
| Magnetic GO/fibrillated-cellulose composite (2025) | TC | Sips fitted (q_m=130.11) mg/g; measured (q_e=93.36\pm3.85) mg/g at 0.50 g/L dose and (C_0=70) mg/L | Sips (q_m), Langmuir (q_m), kinetic-model (q_e), and measured (q_e) must stay separate | Strong-acid cellulose hydrolysis and 48 h lyophilization; five-cycle removal falls from 88.33% to 75.38% |
| CMC-functionalized magnetic GO (2025) | TC | Linear Langmuir (q_m=54.73) mg/g at 50°C; 96.04% removal at (C_0=2) mg/L, dose 0.1 g/L, pH 5, 25°C and 25 min | The 54.73 mg/g value is a *fitted value at 50°C*; mass-balance-derived uptake for the 25°C removal test is about 19.21 mg/g | Methanol regeneration; ~96% to ~92% removal over ten cycles; extensive synthesis but no whole-process cost calculation |
| PGOT@GEL engineered GO hydrogel (Li et al., 2025) | CIP | Langmuir fitted (q_{max}=821.24) mg/g (R²=0.9908); separate RSM validation measured (q_e=807.54) mg/g at (C_0=296.52) mg/L, pH 6.70, dose 5.08 mg and 298.88 K; separate pH-test (q_e=192.24) mg/g with 96.12% removal at pH 7 | These are three different outputs/conditions and should not be collapsed into one “capacity” | Multi-step P-doping/TETA/β-CD/AMPS hydrogel synthesis; methanol soaking for 12 h/cycle; seven-cycle retention ~90.53%; main text and Fig. 12 caption differ on whether water samples are real or simulated |
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
