# SEM-029 GO/PVA/calcium-alginate ciprofloxacin cost and condition audit — 31 October 2026

## Study identity and source
“Removal of ciprofloxacin from aqueous solutions using GO/PVA/calcium alginate composite beads as an absorbent,” *RSC Advances* (2026), DOI: 10.1039/D6RA00494F.

Official open-access article: https://pubs.rsc.org/en/content/articlehtml/2026/ra/d6ra00494f
The article and its Methods, adsorption experiments, isotherm/kinetic sections, regeneration claims and §3.13 cost analysis were rechecked on 31 October 2026.

The purpose of this audit is not to discard the adsorption results; it is to test whether the low-cost/lifecycle assertions can be reconciled with the dose and material-price numbers the authors themselves provide.

## Experimental adsorption endpoints — keep separate
### Specific 89.82% removal point (§3.6.2)
- Initial CIP concentration, C0 = 40 mg/L.
- Solution volume, V = 50 mL = 0.050 L.
- GO/PVA/calcium-alginate bead mass, m = 0.5 g.
- Temperature = 298 K.
- Contact time = 150 min.
- Removal = 89.82%.

Mass-balance-derived uptake:
`qe = C0 × V × removal / m`
`qe = 40 mg/L × 0.050 L × 0.8982 / 0.5 g = 3.5928 mg/g`.

Available-feed ceiling for this batch:
`40 mg/L × 0.050 L / 0.5 g = 4.0 mg/g`.

This endpoint is internally plausible: the derived qe=3.5928 mg/g is below the 4.0 mg/g feed ceiling. It is a calculated qe, not a directly tabulated experimental qe.

### Separate maximum uptake from the concentration sweep
The concentration study uses 20–100 mg/L, 50 mL solution, 0.5 g beads, 298 K and 150 min. The paper reports a maximum observed qe of 7.15 mg/g in this concentration sweep. Do not pair this 7.15 mg/g value with the 89.82% removal at 40 mg/L unless the paper explicitly provides that same-row association. The two endpoints are distinct reported results.

### Fitted isotherm and kinetic values
- Linear Langmuir qmax = 8.210 mg/g (R²=.9588).
- Nonlinear Langmuir qmax = 10.14 mg/g (R²=.9715).
- At C0=100 mg/L, V=50 mL and m=0.5 g, the feed ceiling is 10 mg/g. Thus the nonlinear fitted qmax is 0.14 mg/g (1.4%) above that upper-feed ceiling. This is a fit/extrapolation caution; qmax is a model parameter, not an observed qe, so do not describe it as a directly measured mass-balance violation.
- Nonlinear kinetic-fit qe values: PFO=3.3675 mg/g and PSO=4.45827 mg/g.
- Linear and nonlinear Dubinin–Radushkevich fitted qm values diverge strongly (0.00013811 versus 5.7715 mg/g). Preserve the fit form and model identity; do not select one value without explaining the regression form.
- The source also has a 50/55 mL wording discrepancy in the methods. Keep both statements in the audit and do not silently correct the solution volume.

## Cost-section claims (§3.13)
The paper gives the following input prices:
- GO: approximately USD 50–200 per kg.
- PVA: USD 2–5 per kg.
- Sodium alginate: USD 5–10 per kg.
- CaCl2 crosslinker: USD 1 per kg.
- Total bead material cost: estimated at USD 10–30 per kg of beads.

It also states:
- Desorption using mild acid/alkali, e.g. 0.1 M HCl or NaOH, at less than USD 0.5/L.
- Operational cost per cycle: USD 0.1–0.5 per kg wastewater treated, assuming a bead dose of 0.1 g/L and a 100 L batch.
- Total lifecycle cost: less than USD 1 per kg of CPX removed over five cycles.

The article does not provide an itemized costing worksheet, price year, bead yield, mass balance across synthesis/washing, exact CIP mass captured per cycle, regenerant volume per cycle, energy/electricity, water/washwater, labor or waste-treatment costs. No calculation is shown that leads from the listed prices and adsorption capacity to the claimed lifecycle cost per kg CPX.

## Central dose inconsistency: 100-fold
The cost section assumes a dose of 0.1 g/L. The experimental concentration/removal runs use 0.5 g beads in 50 mL:
`0.5 g / 0.050 L = 10 g/L`.

Therefore, the cost-model dose is 100 times lower than the experimental adsorption dose:
`10 g/L / 0.1 g/L = 100`.

For a 100 L treatment batch:
- At the assumed 0.1 g/L cost dose: 10 g beads.
- At the experimental 10 g/L dose: 1,000 g = 1 kg beads.

Using the authors' own estimated bead price USD 10–30/kg:
- Cost-model 0.1 g/L batch: 10 g beads costs about USD 0.10–0.30.
- Experimental 10 g/L batch: 1 kg beads costs USD 10–30.

These are bead-material-only figures and do not include other process expenses. The paper does not explain the 100-fold dose change or show that the low-dose cost scenario achieves the same removal/capacity.

## Lower-bound material cost per kg CPX captured
A second, independent consistency check uses the bead price per kg and the paper's own adsorption capacities.

### Using nonlinear Langmuir qmax = 10.14 mg/g
A qmax of 10.14 mg/g means 1 kg beads can adsorb, at the model asymptote:
`10.14 mg/g × 1,000 g = 10,140 mg = 10.14 g = 0.01014 kg CIP`.

At USD 10–30 per kg beads, bead-only material cost per kg of CIP captured is:
`USD 10 / 0.01014 kg = about USD 986/kg CIP`
`USD 30 / 0.01014 kg = about USD 2,959/kg CIP`.

### Using observed concentration-sweep qe = 7.15 mg/g
At 7.15 mg/g:
`7.15 mg/g × 1,000 g = 7,150 mg = 7.15 g = 0.00715 kg CIP`.

The bead-only cost per kg CIP captured is therefore:
`USD 10 / 0.00715 kg = about USD 1,399/kg CIP`
`USD 30 / 0.00715 kg = about USD 4,196/kg CIP`.

These are derived best-case material-only bounds. They optimistically assume the stated capacity is fully realized over the full bead mass and exclude all acid/alkali, regeneration, energy, labor, water/washing, synthesis yield loss, bead attrition and waste handling. Even this bead-only material cost is around three orders of magnitude above the claimed lifecycle cost of less than USD 1/kg CPX. Consequently, the <USD 1/kg CPX lifecycle claim cannot be reconciled with the article's own listed bead price and capacities under a per-kilogram-CPX interpretation.

This conclusion does not mean the adsorption result is false; it means the stated lifecycle-cost number lacks a defensible mass denominator and is internally inconsistent with the stated price/capacity inputs.

## Operational cost per kg wastewater
The article's USD 0.1–0.5 per kg wastewater claim corresponds, for approximately 100 L (about 100 kg) wastewater, to USD 10–50 per batch. However:
- At the paper's assumed 0.1 g/L dose, bead material is only about USD 0.10–0.30 per 100 L.
- At the actual experimental 10 g/L dose, bead material alone is USD 10–30 per 100 L.

No itemized calculation explains the remaining difference between bead-material cost and the stated operational cost. It is also unclear whether the stated operational figure includes acid/alkali regenerant, energy, labor, mixing, filtration/centrifugation, washwater or waste treatment. The number must be retained as an author estimate, not presented as a reproducible operating cost.

## Regeneration and lifecycle claim
The article states that mild 0.1 M HCl or NaOH can be used for desorption and that four to five cycles are possible with less than 25% capacity loss / more than 85% efficiency after five cycles. But cycle-by-cycle qe, bead mass loss, regenerant volume, CIP recovered per cycle and cost per cycle are not sufficiently detailed to validate the lifecycle-cost denominator. Retain the reuse statement as author-reported; do not infer a verified cost-per-kg-CIP result from it.

## Semester-paper decision
Retain the adsorption results with correct metric labels:
1. 89.82% removal at40mg/L,50mL,0.5g,298K,150min; derived qe=3.5928mg/g, feed ceiling4mg/g.
2. Separate observed concentration-sweep maximum qe=7.15mg/g.
3. Linear Langmuir qmax=8.210mg/g and nonlinear Langmuir qmax=10.14mg/g; fitted parameters, not observed qe.
4. Kinetic fitted qe values and D–R model divergence remain separate.
5. Preserve the source's 50/55mL method issue.

Do **not** describe the beads as a validated low-cost system or repeat the lifecycle claim (<USD 1/kg CPX) as fact. The source's own bead price and capacity imply bead-material-only costs of approximately USD 986–2,959/kg CIP at fitted qmax and USD 1,399–4,196/kg CIP at observed qe=7.15mg/g. The cost-model dose is 100× lower than the experimental dose. Any future cost comparison should require a corrected, auditable scenario with a consistent bead dose, explicit treated-water volume, bead yield, actual CIP mass removed, cycle-by-cycle capacity, regenerant, energy, water and labor.

## Repository updates
Updated in place:
- data/semester-remaining-work-register.csv
- data/semester-paper-candidate-register.csv
- data/semester-evidence-readiness-audit.csv (EV-SEM-026)
- data/semester-condition-labelled-comparison.csv (EV-SEM-026)
- data/semester-manuscript-claim-evidence-audit.csv (CLM-15)
- data/source-caveats.csv
- README.md

No duplicate SEM/evidence ID was created. The existing Zotero key hossainRemovalCiprofloxacinAqueous2026 is preserved.
