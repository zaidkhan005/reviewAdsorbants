# Mechanism and practical-feasibility synthesis — 30 October 2026

## Source-record QA

Before synthesis, the active evidence extraction CSV was checked for field alignment. Records EV-SEM-002, EV-SEM-016, EV-SEM-022, EV-SEM-027, EV-SEM-036 and EV-SEM-037 had record-specific alignment/shape defects: either preparation content was merged into the material-identity field and subsequent fields shifted, or the final caveat field had an extra value. These records were normalized so all 39 active rows have 20 fields matching the CSV header. The fixes were limited to moving existing source text into its correct semantic field, splitting material identity from preparation where necessary, and consolidating duplicate cost/caveat text; no numerical result was changed.

## New synthesis outputs

- `data/semester-mechanism-evidence-matrix.csv`: 15 currently discussed empirical study claims, with source evidence, proposed interaction, qualitative evidence grade and limits on inference.
- `data/semester-practical-feasibility-matrix.csv`: same 15 studies, covering preparation burden, recovery, regeneration, matrix tests, cost data and feasibility constraint.
- Added manuscript Sections 4 and 5 to `manuscript/SEMESTER_RESULTS_AND_DISCUSSION_V1.md`, using only the 15 citation keys already reconciled in the Results/Discussion draft.

## Main synthesis findings

1. The source set supports several plausible, concurrent mechanisms—π–π interactions, electrostatic/speciation effects, hydrogen bonding, and pore/diffusion contributions—but not one universal mechanism.
2. Spectroscopy, pH/ion-response data, surrogate fluorescence and DFT strengthen mechanistic discussion but rarely quantify how much each interaction contributes. Abstract-only or preview-only sources receive lower evidence grades.
3. Pseudo-second-order and Langmuir/Freundlich model fits are not direct molecular proof; do not infer chemisorption, a homogeneous monolayer, or a unique interaction from fit quality alone.
4. Magnetic response or immobilization can improve recovery/handling but does not automatically improve intrinsic binding affinity. Immobilization/crosslinking (e.g., Ca-alginate egg-box network) must be distinguished from direct antibiotic–surface binding.
5. Process burdens are material: modified-Hummers acids/oxidants and washing, solvent/acid/alkali regeneration, drying/freeze-drying, long hydrothermal or polymerization steps, and rotating-field energy measurement gaps.
6. Only one cited study gives a nominal bead-price estimate; the assumed 0.1 g/L dose differs by 100× from a key 10 g/L experimental dose. Its cost-per-removal conclusion is not reproducible from the available worksheet/assumptions.
7. There is no harmonized cost per treated volume or mass of CIP/TC removed across the cited studies. “Low-cost potential” remains unproven, to be evaluated from process boundaries rather than inferred from waste feedstock or high qmax.

## Scope and citation control

No new citation key was added. The mechanism and feasibility chapters reuse only the existing verified keys in the 15-source Results/Discussion draft. The DOI intake queue and the four contextual Introduction sources remain separate from these 15 empirical study claims. Do not use the new matrices to count new references.
