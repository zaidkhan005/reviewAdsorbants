# SEM-026 GO–sodium alginate/CIP accepted-manuscript audit — 31 October 2026

## Study identity and source provenance
Yu, F., Li, Y., Han, S. and Ma, J. (2016), “Adsorptive removal of ciprofloxacin by sodium alginate/graphene oxide composite beads from aqueous solution,” *Journal of Colloid and Interface Science* 484, 196–204. DOI: 10.1016/j.jcis.2016.08.068. PMID: 27614043.

Official publisher abstract/preview: https://www.sciencedirect.com/science/article/abs/pii/S0021979716306312
PubMed abstract/metadata: https://pubmed.ncbi.nlm.nih.gov/27614043/
Full accepted-manuscript text mirror: https://www.scribd.com/document/1064243350/rp-10

The official ScienceDirect and PubMed pages confirm the article identity and abstract claims. A 23-page third-party-hosted Scribd document contains the accepted manuscript and is explicitly marked “Accepted Manuscript”; it warns that it is an unedited pre-publication version that may differ from the final copyedited article. The text is useful for recovering Tables 2 and 3 and the Methods/Results, but it is not publisher-hosted. No supporting-information PDF was recovered. The numerical table evidence in this audit is therefore classified as accepted-manuscript/third-party-mirror evidence, cross-checked against the publisher abstract rather than treated as publisher-hosted typeset full text.

SEM-026 is the canonical record. SEM-041 remains a duplicate alias and must not be counted as another study.

## Adsorbent configurations and nomenclature
Four forms are compared:
- SA-H: sodium alginate hydrogel.
- SA-A: sodium alginate aerogel, obtained by lyophilizing the hydrogel.
- GO-SA-H: graphene oxide/sodium alginate composite hydrogel.
- GO-SA-A: graphene oxide/sodium alginate composite aerogel, obtained by lyophilizing the composite hydrogel.

These forms should remain distinct in synthesis and capacity comparisons. The abstract reports a seven-to-nine-fold improvement in kinetic adsorption capacity after GO incorporation. Table 2 supports an approximately 8.9-fold experimental qe increase for hydrogel (25.86/2.90) and 7.9-fold for aerogel (22.59/2.87). Table 3 reports still different fold changes in fitted Langmuir qmax: GO-SA-H/SA-H is about9.9×; GO-SA-A/SA-A is about13.1×. Do not combine the kinetic enhancement and isotherm qmax enhancement into one number.

## Preparation method and process boundary
### Sodium alginate hydrogel/aerogel
- Dissolve 1 g sodium alginate in 40 mL deionized water under magnetic stirring.
- Sonicate the SA solution for approximately20 min.
- Add dropwise by peristaltic pump at6 mL/min into0.2 mol/L CaCl2 under constant gentle magnetic stirring.
- Continue stirring to promote uniformity and avoid agglomeration.
- Harden in CaCl2 for2–3 days without stirring.
- Wash with DI water3–4 times and store at4°C.
- Produce SA aerogel (SA-A) by lyophilizing the SA hydrogel.

### GO–SA hydrogel/aerogel
- Graphite oxide is prepared by a modified Hummers method, but the accepted manuscript refers to earlier literature for the full synthesis recipe rather than reproducing all reagent quantities.
- Disperse graphite oxide in DI water and ultrasonicate for10 h to obtain a GO flake dispersion at1.0 mg/mL.
- Slowly add SA powder to the GO aqueous dispersion while stirring. The exact GO:SA formulation mass ratio is not explicitly stated in the recovered Methods text.
- Sonicate the SA/GO mixture for20 min, then add dropwise at6 mL/min into0.2 mol/L CaCl2 under gentle constant stirring.
- Harden for2–3 days, wash3–4 times with DI water and store at4°C.
- Obtain GO-SA-A by lyophilizing the GO-SA hydrogel.

The article's XPS discussion describes GO content as approximately4% in the composite, but the exact recipe mass ratio is not clearly exposed in the Methods text. Preserve this distinction; do not reverse-engineer an exact starting formulation from the XPS discussion.

### Preparation/cost interpretation
The process requires prolonged GO dispersion sonication, CaCl2 hardening for2–3 days, repeated washing and lyophilization for aerogel production. The upstream modified-Hummers GO synthesis is referenced rather than fully itemized. No synthesis yield, water-use balance, electricity-per-gram, lyophilizer energy, salt recovery, washing-waste treatment or monetary cost is reported. The paper's use of environmentally benign sodium alginate does not itself prove low production cost or low life-cycle impact.

## Batch adsorption conditions
### Equilibrium/isotherm series
The accepted-manuscript Methods specify:
- 150 mL Erlenmeyer flasks.
- 50 mL CPX solution.
- C0 series:10,20,30,40,50,60,70,80,90,110,130 and150 mg/L.
- Sorbent masses:20 mg SA or15 mg GO-SA; the manuscript says the hydrogel weights were calculated after lyophilization.
- Temperature:298±0.5 K.
- Shaker speed:180 rpm.
- Equilibration:128 h.
- The equilibrium solution was filtered through a0.45-µm membrane and analysed by UV–Vis.

For the GO-SA tests,15 mg sorbent in50 mL is0.30 g/L. At the maximum initial concentration150 mg/L, the available-feed ceiling is:
150 mg/L ×0.050 L /0.015 g =500 mg/g.
The GO-SA Langmuir-fitted qmax values of86.12 and55.55 mg/g are both below this ceiling. This is only a simple feed-ceiling plausibility check; qmax remains a fitted asymptote, not an observed qe at a single concentration.

### Kinetic series
- C0=50 mg/L CPX.
- 50 mL solution.
- 20 mg SA or15 mg GO-SA (dry-mass basis as described by the authors).
- 298±0.5 K.
- 180 rpm.
- The authors describe a rapid initial rise, followed by a transient maximum and redistribution before a stable value.
- Hydrogel systems reach a stable value at approximately48 h; the aerogels take longer to reach equilibrium. The prose does not give one exact aerogel equilibrium time, so do not assign the hydrogel's48 h time to the aerogels.

For GO-SA, the initial feed contains2.5 mg CPX and the sorbent mass is0.015 g; feed ceiling is166.67 mg/g. Experimental kinetic qe values25.86 mg/g (GO-SA-H) and22.59 mg/g (GO-SA-A) are comfortably below this ceiling. They are not the Table 3 Langmuir qmax values.

## Experimental kinetic qe and fitted kinetic model outputs — Table 2
At298 K, Table 2 reports:

| Form | Experimental qe (mg/g) | PFO fitted qe (mg/g) | PFO R² | PSO fitted qe (mg/g) | PSO R² |
|---|---:|---:|---:|---:|---:|
| SA-H | 2.90 | 1.52 | 0.023 | 2.78 | 0.996 |
| SA-A | 2.87 | 1.34 | 0.516 | 2.97 | 0.994 |
| GO-SA-H | 25.86 | 2.62 | 0.313 | 25.38 | 0.999 |
| GO-SA-A | 22.59 | 2.47 | 0.452 | 22.68 | 0.999 |

The pseudo-second-order fits are markedly better than pseudo-first-order for all four forms according to the reported R². For GO-SA-H the PSO fitted qe25.38 is close to experimental qe25.86; for GO-SA-A PSO fitted qe22.68 is close to experimental qe22.59. Keep the experimentally tabulated qe and the fitted qe as separate fields. A strong PSO fit alone does not conclusively prove chemisorption.

## Fitted isotherm parameters — Table 3
The table provides Langmuir and Freundlich model fits at298 K:

| Form | Langmuir qmax (mg/g) | KL (L/mg) | Langmuir R² | Freundlich KF | 1/n | Freundlich R² |
|---|---:|---:|---:|---:|---:|---:|
| SA-H | 8.66 | 0.025 | 0.819 | 0.915 | 0.412 | 0.698 |
| SA-A | 4.23 | 0.021 | 0.864 | 0.319 | 0.469 | 0.789 |
| GO-SA-H | 86.12 | 0.010 | 0.941 | 2.514 | 0.610 | 0.900 |
| GO-SA-A | 55.55 | 0.018 | 0.967 | 3.873 | 0.477 | 0.934 |

The Langmuir R² exceeds Freundlich for each form in the accepted-manuscript Table3, consistent with the abstract's statement that non-linear Langmuir represents the isotherm well.

Crucial metric/form distinction:
- 86.12 mg/g is the fitted Langmuir qmax for GO-SA-H (hydrogel).
- 55.55 mg/g is the fitted Langmuir qmax for GO-SA-A (aerogel).
- Neither number is an observed qe or the kinetic Table2 experimental qe.
- The abstract does not distinguish the hydrogel and aerogel values; Table3 and conclusion do.

## pH response and ionic-strength effects
### pH
The pH response tests used50 mg/L CPX and pH values2,4,6,8,10 and12.
- SA-H hydrogel capacity rises from low pH to a maximum aroundpH4, then decreases toward a plateau.
- GO-SA-H follows a similar pH trend to SA-H.
- SA-A and GO-SA-A aerogels show their highest capacities atpH2.
- The authors explain stronger uptake at low pH by positively charged CPX interacting with the gel surfaces. At higher alkaline pH, additional sodium ions can disrupt the transient Ca2+-alginate crosslinks and release previously adsorbed CPX.

Do not state one universal pH optimum for all GO-SA forms: hydrogel and aerogel behavior differs.

### Ionic strength
NaCl concentrations tested:0,0.001,0.01,0.1,0.2 and0.5 mol/L, with50 mg/L CPX.
- SA-H and GO-SA-H capacities decline as NaCl increases, with a stronger decrease at higher concentrations (especially0.01–0.5 mol/L), attributed by the authors to sodium-ion effects on gel structure.
- GO-SA-A retains comparatively stable adsorption capacity over0.001–0.1 mol/L NaCl.
- SA-A shows a slight capacity increase over0.001–0.1 mol/L.
- Lyophilization therefore appears to improve tolerance to ionic-strength changes, although aerogel maximum qmax is lower than GO-SA-H hydrogel qmax.

These are controlled single-salt tests, not a real wastewater or mixed-ion/organic-matter validation.

## Mechanism/characterization
- BET surface area: SA-H66.57 m²/g; GO-SA-H91.86 m²/g (approximately38% higher).
- Mean pore diameter:19.83 nm (SA-H) and13.55 nm (GO-SA-H).
- Pore volume:0.49 and0.42 cm³/g, respectively.
- XPS discussion reports that GO introduces C=O and C=C functionality into the composite; GO content is discussed as approximately4%.
- The authors attribute improved CPX adsorption to increased/more uniform porosity, π–π electron donor–acceptor interactions between GO and CPX, and introduction of C=O groups.

Use these as proposed mechanism support; they do not quantify the contribution of each interaction.

## Regeneration, real-water and cost evidence
- No adsorption–desorption regeneration-cycle experiment or cycle-resolved retained-capacity result was identified in the accepted manuscript.
- Lyophilization is a manufacturing/storage step for the aerogel, not an adsorbent regeneration test.
- No actual wastewater, river-water or other real-water validation was identified.
- No cost per kg adsorbent, cost per volume treated, material yield, electrical energy, wash-water consumption, regeneration cost, LCA or TEA was reported.

Do not claim reuse or low-cost performance for this paper. The alginate carrier and bead/aerogel form provide a practical immobilized architecture, but economics and regeneration were not demonstrated in the accessible article.

## Semester-paper decision
Retain SEM-026 as a condition-labelled GO–alginate/CIP study. Report separately:
1. GO-SA-H experimental kinetic qe25.86mg/g and fitted PSO qe25.38mg/g under50mg/L,50mL,15mg,298K,180rpm.
2. GO-SA-A experimental kinetic qe22.59mg/g and fitted PSO qe22.68mg/g under the same nominal kinetic protocol.
3. GO-SA-H fitted Langmuir qmax86.12mg/g and GO-SA-A fitted Langmuir qmax55.55mg/g at298K in the10–150mg/L isotherm series.
4. pH response differs between hydrogels (maximum aroundpH4) and aerogels (maximum aroundpH2).
5. GO-SA-A shows better salt tolerance over NaCl0.001–0.1M than the hydrogel forms.
6. No regeneration, actual-water or quantified cost evidence.

Keep SEM-041 as an alias only; do not count it as a distinct study. The Zotero/Better BibTeX key remains unverified; do not insert a guessed citation key into the manuscript comparison table.

## Repository updates
Updated in place:
- data/semester-remaining-work-register.csv
- data/semester-paper-candidate-register.csv
- data/semester-evidence-readiness-audit.csv (existing EV-SEM-020)
- data/semester-condition-labelled-comparison.csv (EV-SEM-020 row added)
- data/semester-manuscript-claim-evidence-audit.csv (CLM-27 added)
- data/source-caveats.csv
- README.md

No duplicate evidence ID created. SEM-041 remains alias-only. The manuscript's cited-reference comparison table was not modified because the Zotero key is not yet verified.
