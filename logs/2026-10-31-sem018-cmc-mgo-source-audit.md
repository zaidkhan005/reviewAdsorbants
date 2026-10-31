# SEM-018 CMC-functionalized magnetic GO/Fe3O4/CMC source audit — 31 October 2026

## Study identity and source
Dipannita, N. T., Yasmin, S., Hasan, M. K., Hossain, M. S., Somapti, M. A. and Kabir, M. H. (2025), “Carboxymethylcellulose functionalized magnetic graphene oxide for the efficient removal of tetracycline from aqueous media,” *RSC Advances* 15, 35219–35232. DOI: 10.1039/D5RA06621B.

Official publisher PDF: https://pubs.rsc.org/en/content/articlepdf/2025/ra/d5ra06621b
Official article HTML: https://pubs.rsc.org/en/content/articlehtml/2025/ra/d5ra06621b
PMC full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC12458999/

The publisher PDF was opened and parsed and checked against indexed full-text HTML. The PDF screenshot endpoint returned HTTP 403 in this session; source text and parsed figure/caption content provided the table and figure information.

## Waste-derived feedstock and preparation process
The authors recover graphite rods from abandoned Li-ion batteries collected from residential areas. Rods are extracted, rinsed to remove MnO2/NH4Cl/carbon paste, air-dried, crushed, purified using Aqua Regia, washed with DI water and dried at60°C for24h.

GO via modified Hummers:
- 270mL H2SO4 +30mL H3PO4 mixed and stirred10min.
- Add2g recovered graphite powder, then12g KMnO4.
- Heat at50°C for12h.
- Cool, ice-bath and quench using6mL of30% H2O2.
- Centrifuge6000rpm; sequential DI water,30% HCl, DI water and ethanol washing.
- Vacuum dry at50°C for24h.

m-GO/Fe3O4/CMC composite:
- Disperse80mg GO in50mL DI water and sonicate30min.
- Dissolve0.01mol FeSO4·7H2O (2.781g) and0.02mol Fe2(SO4)3·7H2O (7.998g) in100mL DI water; sonicate30min.
- Dissolve80mg CMC in50mL DI water.
- Combine GO and CMC suspensions; heat in oil bath; add Fe salt solution; stir30min at45°C.
- Add2.0M NaOH to pH≈11, then heat85°C for2h.
- Magnetically isolate; repeatedly wash with DI water until neutral, then ethanol; vacuum dry60°C for18h.
- Reported saturation magnetization:50.69emu/g; pHpzc≈3.5.

This is a genuinely waste-derived precursor route, but it is not a zero-burden or automatically low-cost process. It uses Aqua Regia,270mL strong acid mixture for2g graphite,12g KMnO4,30% H2O2,30% HCl, substantial Fe salts relative to80mg GO and80mg CMC,2M NaOH, ethanol, repeated washing, sonication, centrifugation and long drying. The paper gives no GO or composite yield, reagent recovery, wash-water management, energy-per-gram, price-year or normalized production/treatment cost. The claim of economic/environmental benefit is qualitative, not a measured TEA or LCA.

## Base adsorption protocol and mass balance
- Batch flask:100mL conical flask.
- Working solution volume:20mL.
- Initial TC:2mg/L for the headline test.
- Composite dose:2mg (0.1g/L).
- pH5;25°C;250rpm;25min.
- Removal:96.04% (abstract, Results §3.2.2 and conclusion).

Mass balance:
- TC feed mass =2mg/L ×0.020L =0.040mg.
- Adsorbent mass =0.002g.
- Feed-limited qe ceiling =0.040mg /0.002g =20mg/g.
- qe derived from96.04% removal =0.040mg ×0.9604 /0.002g =19.208mg/g.

This is internally plausible: derived qe is below the20mg/g feed ceiling. It is a calculation from reported removal and Methods conditions, not a directly tabulated measured qe. Keep its derived status explicit.

## Operating-condition details
- Dose response:1,2,3,5,7 and10mg in20mL atC0=2mg/L. Removal increases with dose; authors select2mg/20mL (=0.1g/L) as a dose-efficient optimum, stating that beyond2mg incremental gains become modest.
- Contact-time response:5–90min; maximum removal is reported by25min and the curve then plateaus.
- pH response:2–10 at2mg dose,25°C,C0=2mg/L; removal rises to a maximum aroundpH5 and declines at higher pH.
- Concentration response:0.2–10mg/L at pH5,2mg dose,25°C. The text reports removal declining from99.43% at0.2mg/L to44.99% at10mg/L. It then calls2mg/L the optimal initial concentration “based on higher removal efficiency.” This is a wording/selection ambiguity: the highest removal in the described concentration range is reported at0.2mg/L, not2mg/L. The abstract and headline optimum use2mg/L and96.04%. Do not rewrite the concentration-response statement or claim2mg/L is the absolute maximum-removal concentration; it may be the authors' selected working point.
- Isotherm concentration range:0.2–10mg/L at pH5, dose0.1g/L,25–50°C. Isotherm and headline removal are distinct protocols.

## Kinetics: fitted qe, not observed qe
Table2:
- Linear PFO: fitted qe=1.4174mg/g; k1=.0597; R²=.8895.
- Linear PSO: fitted qe=19.5008mg/g; k2=.0900; R²=.9999.
- Nonlinear PFO: fitted qe=19.0358mg/g; k1=.5658; R²=.4777.
- Nonlinear PSO: fitted qe=19.3522mg/g; k2=.1282; R²=.8004.
- Elovich R²=.8711; Weber–Morris R²=.7783 (ki=.1920, Ci=17.8541).

The linear PSO fit is excellent by R², but the non-linear PSO fit is substantially weaker. Both fitted qe values (~19.35–19.50mg/g) are slightly above mass-balance-derived qe=19.208mg/g, yet remain below20mg/g feed ceiling. The linear and non-linear forms should not be presented as if they gave equivalent fit quality. PSO fit superiority does not prove chemisorption by itself.

## Isotherms: temperature-specific fitted qmax and regression sensitivity
Table3 reports linear and non-linear fits separately at25,40 and50°C.

Linear Langmuir:
- qmax=45.5581mg/g at25°C (R²=.9952).
- qmax=51.4933mg/g at40°C (R²=.9969).
- qmax=54.7346mg/g at50°C (R²=.9809).

Non-linear Langmuir:
- qmax=44.0051mg/g at25°C (R²=.9569).
- qmax=48.6490mg/g at40°C (R²=.9895).
- qmax=48.4744mg/g at50°C (R²=.9425).

At50°C, non-linear Freundlich R²=.9609 is greater than non-linear Langmuir R²=.9425. Thus, “Langmuir is best” is true for the linear-model comparison (linear Langmuir is top at all three temperatures), but is not uniformly true across regression forms at50°C. The abstract's54.73mg/g is the linear Langmuir fitted qmax at50°C; it is not measured qe and is not comparable to the25°C headline removal point. Preserve the linear/non-linear distinction and avoid presenting54.73mg/g as an unqualified observed capacity.

## Magnetic separation, reuse and regeneration
- The material is superparamagnetic (saturation magnetization50.69emu/g), enabling external magnetic separation.
- Section3.2.8 reports methanol regeneration.
- The adsorbent is reused up to10 cycles; removal efficiency declines only slightly from approximately96% to92% across the sequence (Fig.7).
- The article does not report cycle-resolved qe, direct capacity-retention percentages, methanol concentration/volume, contact time, solvent recovery or regenerant treatment.
- Therefore report “removal efficiency remains about92% after ten cycles” rather than “92% adsorption capacity retained.” Reuse is promising, but the methanol and wash-water burden is not costed.

## Mechanism and practical applicability
Authors propose π–π interactions, electrostatic attraction and hydrogen bonding, supported by FTIR peak changes, pH dependence and the CMC/GO/Fe3O4 composition. TC speciation as stated: cationic belowpH3.3, zwitterionic frompH3.3–7.68, and anionic abovepH7.68. The composite pHpzc≈3.5; pH5 is above pHpzc and within the zwitterionic TC region. Treat the mechanism as convergent support for likely interactions, not quantitative attribution of each contribution.

No actual wastewater sample, field matrix, column/flow test, or quantified metal leaching result was found. “Potential for wastewater” is not a demonstration on real wastewater.

## Semester-paper decision
Retain SEM-018 / EV-SEM-007 as a primary TC adsorption study. Use:
1. 96.04% removal under2mg/L,20mL,2mg,0.1g/L,pH5,25°C,25min.
2. Derived qe=19.208mg/g, explicitly labelled calculated; feed ceiling20mg/g.
3. Linear and non-linear PSO fitted qe values separately.
4. Linear Langmuir qmax54.7346mg/g at50°C vs non-linear qmax48.4744mg/g, and note nonlinear Freundlich R²=.9609 exceeds nonlinear Langmuir=.9425 at50°C.
5. Ten-cycle methanol reusability as removal efficiency ~96→92%, not qe retention.
6. Waste-Li-ion graphite precursor with high acid/oxidant/Fe-salt/wash/dry burden; no real-water test or monetized cost.

Do not call2mg/L the maximum-removal concentration without explaining the0.2–10mg/L response text. Do not label fitted qmax or PSO qe as observed uptake.

## Citation workflow
The DOI/title and Better BibTeX key `dipannitaCarboxymethylcelluloseFunctionalizedMagnetic2025` are already verified in the supplied citation set. Preserve the existing key.

## Repository updates
Updated in place:
- data/semester-remaining-work-register.csv
- data/semester-paper-candidate-register.csv
- data/semester-evidence-readiness-audit.csv (EV-SEM-007)
- data/semester-condition-labelled-comparison.csv
- data/semester-manuscript-claim-evidence-audit.csv (CLM-02)
- manuscript/SEMESTER_TABLE_1_CORE_STUDY_COMPARISON_V1.md
- README.md

No duplicate evidence ID created; EV-SEM-007 was updated in place.
