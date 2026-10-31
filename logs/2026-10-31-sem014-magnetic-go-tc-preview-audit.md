# SEM-014 magnetic GO/TC publisher-preview audit — 31 October 2026

## Study identity and source
Bruckmann, F. da S., Ledur, C. M., da Silva, I. Z., Dotto, G. L. and Rhoden, C. R. B. (2022), “A DFT theoretical and experimental study about tetracycline adsorption onto magnetic graphene oxide,” *Journal of Molecular Liquids* 353, article 118837. DOI: 10.1016/j.molliq.2022.118837. Published 1 May 2022.

Official ScienceDirect preview:
https://www.sciencedirect.com/science/article/pii/S0167732222003749

ResearchGate record:
https://www.researchgate.net/publication/358970157_A_DFT_theoretical_and_experimental_study_about_tetracycline_adsorption_onto_magnetic_graphene_oxide

The official ScienceDirect publisher page was rechecked on 31 October 2026. It exposes the abstract, highlights, Introduction, DFT simulation/results snippets and Conclusions, but directs readers to institutional access or purchase for the full Methods and numerical tables. ResearchGate explicitly says no full-text PDF is available there and offers a request-full-text action. The Library search in this conversation did not find a matching PDF. No new PDF batch is assumed or requested.

## Verified condition fragment and author-reported capacity
The publisher abstract explicitly reports:
- Adsorbent: magnetic graphene oxide, GO·Fe3O4.
- Magnetite incorporation: GO·Fe3O4 at a 1:1 ratio gives the highest adsorption capacity among the tested compositions.
- Adsorbent mass: 50 mg.
- Initial tetracycline concentration: 1000 mg/L.
- pH: 7.0.
- Temperature: 293 K.
- Author-described maximum tetracycline adsorption capacity: 531.93 mg/g.

The abstract calls 531.93 mg/g a “maximum adsorption capacity”; it does not identify it as directly observed equilibrium qe, a conventional Langmuir qmax, or a statistical/fitted saturation parameter. No isotherm model, kinetic model, table coefficients or fit statistics are exposed in the preview. Do not assign a model label that the accessible source does not provide.

## Feed-mass lower bound
The reported capacity and adsorbent mass imply a loaded tetracycline mass of:
- 531.93 mg/g ×0.050 g = 26.5965 mg TC.

At the initial concentration of1000mg/L, the absolute minimum liquid volume required to supply26.5965mg TC is:
- 26.5965 mg ÷1000 mg/L =0.0265965 L =26.60 mL.

This is only a lower-bound plausibility calculation assuming 100% removal and no residual TC. Actual volume would need to be greater if the equilibrium concentration were non-zero. The actual solution volume, equilibrium concentration, contact time and directly measured qe are not exposed in the preview. Therefore this check does not verify the experimental result; it only defines a condition the missing Methods/table must satisfy.

## Material architecture and preparation
- The material is GO decorated with magnetite (Fe3O4), fabricated by a co-precipitation method while controlling magnetite incorporation on the GO surface.
- The 1:1 GO·Fe3O4 composition is the best-performing magnetite fraction in the publisher highlights.
- Characterization methods stated in the abstract include FTIR, XRD and SEM.
- The preview explains the motivation for adding magnetic nanoparticles: improve separation/recovery of GO after adsorption, since conventional GO nanosheets are difficult to separate from aqueous media.
- The exact GO oxidation recipe, Fe(II)/Fe(III) salt concentrations/masses, precipitation pH, temperature/time, washing, drying, final composite yield and magnetite mass fraction are not exposed in the accessible preview. Do not reconstruct the recipe from another magnetic-GO study.

## Thermodynamics and DFT are separate evidence streams
The publisher abstract describes the adsorption process as spontaneous, exothermic and chemical. Numerical thermodynamic parameters (ΔG°, ΔH°, ΔS°), measured temperature range and detailed fits are not visible in the preview.

The theoretical conclusion snippet reports for configuration1:
- Binding energy =−3.86eV.
- Spin polarization =14.99μB.
- HOMO–LUMO gap =0.22eV.

These are computational electronic/interaction descriptors, not empirical adsorption capacities. The DFT calculations used SIESTA, GGA for exchange/correlation, a double-zeta basis including polarization orbitals, and a 200Ry energy cutoff. The authors say calculations were used to examine possible chemical interactions between TC and GO/Fe3O4. Keep the DFT values separate from the experimental 531.93mg/g endpoint.

## Reuse, cost and application limits
The publisher highlights say GO·Fe3O4 1:1 shows “excellent reuse” and easy operation, with magnetic separation reducing subsequent steps. The accessible abstract and snippets do not reveal:
- cycle count;
- desorption/regeneration eluent;
- cycle-specific qe/removal or retained-capacity percentage;
- real wastewater/river water matrix testing;
- metal/iron leaching;
- GO/Fe3O4 yield or process energy;
- financial preparation cost, cost per gram TC removed, treatment cost per m3, TEA or LCA.

Do not turn the qualitative “excellent reuse” highlight into a quantitative multi-cycle claim, and do not treat magnetic separability as proof of low-cost/full-scale applicability.

## Semester-paper decision
Retain SEM-014 / EV-SEM-030 as a publisher-preview-level TC/magnetic-GO study with a partial condition vector. In any synthesis:
1. Quote531.93mg/g only as the author-reported maximum adsorption capacity.
2. Preserve the reported condition fragment: GO·Fe3O4=1:1;50mg adsorbent;C0=1000mg/L;pH7;293K.
3. State that solution volume/contact time and the capacity metric's precise empirical/model status are unavailable.
4. Keep the minimum feed-volume estimate26.60mL as a plausibility lower bound, not a reconstructed experimental volume or confirmation.
5. Keep DFT binding energy−3.86eV, spin14.99μB and HOMO–LUMO gap0.22eV separate from empirical qe/qmax.
6. Keep the abstract's reuse claim qualitative; no verified cycle count or regenerant is available.
7. Exclude531.93mg/g from condition-matched numeric rankings until the full publisher Methods and results tables are inspected.

## Citation workflow
The DOI/title and source identity are confirmed, but the latest inspected Zotero citation exports had no verified Better BibTeX key. Do not invent one. Add/reconcile the DOI in Zotero only if selected for citation, then use the actual generated key.

## Repository updates
Updated in place:
- data/semester-remaining-work-register.csv
- data/semester-paper-candidate-register.csv
- data/semester-evidence-readiness-audit.csv (EV-SEM-030)
- data/semester-condition-labelled-comparison.csv (partial-condition row)
- data/semester-manuscript-claim-evidence-audit.csv (CLM-22)
- README.md

No duplicate evidence ID was created; EV-SEM-030 was updated in place. The main manuscript comparison table was not given an unverified numeric citation/benchmark.
