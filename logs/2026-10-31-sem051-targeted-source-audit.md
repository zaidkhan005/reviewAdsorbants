# SEM-051 targeted source audit — 31 October 2026

## Study identity and source
Saheed, Raji, Abdul-Raheem, Azeez, Jimoh, Hanafiah and Suah (2026), “Citric acid crosslinked carboxymethyl cellulose/graphene oxide bead for adsorption of tetracycline from an aqueous system,” *Journal of Taibah University for Science*, 20(1), article 2613597. DOI: 10.1080/16583655.2026.2613597. Published online 18 January 2026.

Primary publisher page: https://www.tandfonline.com/doi/full/10.1080/16583655.2026.2613597

The Taylor & Francis page is access-limited to direct page fetch in this session, but publisher-indexed article text returns extensive Methods, Results, captions and reported fit statistics. The audit therefore reflects the exposed primary-source text; complete numerical Table 3/Table 8 exports and detailed cost line items were not recovered. No journal-quartile assessment was made, per the semester-paper instruction.

## Material and preparation
- Product: citric-acid-crosslinked carboxymethyl cellulose/graphene oxide (CMC/GO) composite beads.
- CMC/GO formulation: 1.0 g CMC dissolved in 50 mL of 3% acetic acid; 0.2 g GO dispersed in 50 mL water after 30 min sonication; mix, sonicate another 30 min, stir 550 rpm for 1 h; add 0.5 g citric acid dissolved in 20 mL water; stir 2 h at 60 °C; centrifuge; syringe-drop into 1 M NaOH for 24 h hardening; rinse and dry at 40 °C.
- GO uses a modified Hummers route: 2 g graphite, 2 g NaNO3, 46 mL concentrated H2SO4; 6 g KMnO4; 100 mL water quench; 6 mL H2O2; 5% HCl rinse, repeated water wash/centrifugation and 60 °C drying. Reported synthesis conditions include 350 rpm for the initial mixing, then 550 rpm for 4 h at 50 °C after KMnO4 addition.
- Process-burden implications: strong acid and oxidant handling, substantial washing/centrifugation, sonication, multiple stirring/holding steps, 24 h alkaline hardening and drying. No scale-up yield, water-recovery, solvent-recovery, reagent-recycle or waste-treatment inventory was reported in the exposed text.

## Condition-specific adsorption evidence and mass balance
The paper reports batch tests in synthetic aqueous TC solutions, with no real-water trial.

1. Time test: 200 mg/L TC, 20 mL, 20 mg bead, pH 4; removal rose from 44.80% at 5 min to 94.93% at 120 min, then approached a plateau through 720 min. Using qe = (C0-Ce)V/m, the 120 min point implies qe ≈ 189.86 mg/g. Available-feed ceiling = 200 mg/g. This is a derived, condition-specific result, not an author-reported table qe.
2. pH test: 20 mg/20 mL/200 mg/L/120 min; removal was 70.01% at pH 2 and peaked at 97.34% at pH 4. The latter implies derived qe ≈ 194.68 mg/g under the stated nominal basis.
3. Concentration test: 20 mg bead/20 mL, pH 7 and 120 min; removal declined from 74.64% at 50 mg/L to 60.08% at 250 mg/L. Derived qe is approximately 37.32 mg/g at 50 mg/L and 150.2 mg/g at 250 mg/L, preserving the tested concentration conditions.
4. Dose test: Methods describe a 10–50 mg dosage range but then state that the test was performed with a fixed 20 mg amount. Results separately give 71.15%, 97.35% and 99.1% removal for 10, 20 and 30 mg respectively. This internal Methods/Results conflict is preserved; do not silently infer missing 40 and 50 mg results.
5. Temperature test: Methods text states 20 mg bead/20 mL/200 mg/L at pH 7, whereas Figure 11 caption states 25 mg at pH 4, 200 mg/L and 2 h. Reported removal values are 68.60%, 79.95% and 90.75% at 25, 40 and 60 °C. This condition discrepancy prevents assigning a unique qe from the temperature series.

## Isotherm and kinetic model caveats
- Abstract: nonlinear and linear Langmuir qmax = 267.11 and 277.78 mg/g at 200 mg/L and neutral pH using 5 mg bead.
- Figure 8/Table 3 captions and Methods concentration series instead indicate 20 mg bead/20 mL, pH 7. This 5 mg versus 20 mg condition discrepancy materially changes the feed-mass basis. Preserve both statements.
- Reported isotherm goodness-of-fit: nonlinear Langmuir R²=.9898 and Hill R²=.9939; linear Langmuir R²=.9506 and Hill R²=.9869. Hill is the best fit by the reported R² values. qmax values remain fitted model parameters, not observed uptake.
- If the 20 mg/20 mL condition and maximum test concentration 250 mg/L are used, the maximum available-feed ceiling at the highest concentration is 250 mg/g. The fitted Langmuir qmax values are slightly above that tested-range feed ceiling and should be treated as model extrapolations rather than experimentally attained uptake. If the abstract's 5 mg condition was actually used, the feed ceiling differs; the source does not reconcile these.
- PSO has the strongest reported kinetic fit (R²=.9871 nonlinear; .9973 linear). This alone does not demonstrate chemisorption. The Weber–Morris plot has two stages and a non-zero intercept; the Boyd plot also deviates from the origin (reported R²=.9255), so intraparticle diffusion is not the sole rate-controlling step.
- Authors propose interactions involving oxygen-rich –COOH, C=O, C–O and –OH groups, electrostatic interactions and hydrogen bonding. Treat these as proposed mechanisms supported by material characterization and pH response, not as quantitatively isolated contributions.

## Desorption and reusability — concentration conflict and metric distinction
- Section 2.9 Methods specifies distilled water, 0.1 M HCl and 0.1 M NaOH.
- Section 3.5 Results and Figure 10 caption report 1.0 M HCl and 1.0 M NaOH. This tenfold concentration discrepancy is retained.
- Figure 10 loading conditions: 50 mg bead, 20 mL of 200 mg/L TC, pH 4, 2 h; the spent bead was treated in 20 mL desorption medium for 2 h, dried at 50 °C for 24 h and reused for two further cycles.
- Reported three-cycle desorption efficiencies: water 60.35→52.95%; HCl 58.35→51.80%; NaOH 92.90→83.90%.
- These are desorption efficiencies, not adsorption-capacity retention or removal efficiency after each reuse cycle. The stated equation is Cdesorb/C0, where C0 is the initial concentration used for loading; it is not explicitly normalized to the mass of TC adsorbed onto the bead. Do not rewrite the 83.9% third-cycle result as 83.9% retained adsorption capacity.

## Author-estimated cost — useful method, not yet decision-grade
- Authors report USD 1.95 per gram of TC removed, based on laboratory-scale chemical purchase and energy costs, with Malaysian electricity tariff used for energy. The stated chemical list includes CMC, citric acid, 37% HCl, graphite, H2SO4, NaNO3, KMnO4, H2O2, glacial acetic acid, NaOH and ethanol.
- The cost equation divides chemical-plus-energy preparation cost per gram of adsorbent by adsorption capacity (mg/g × 10^-3). The narrative explicitly uses the linear Langmuir qmax of 277.78 mg/g even though Hill is the best-fitting isotherm model.
- The paper describes removing 1 g TC from 1 L wastewater (~1 kg wastewater) at USD 1.95. Yet the experimental concentration series spans 50–250 mg/L, not a 1 g/L feed. The functional-unit example is therefore not directly demonstrated by the tested feed conditions.
- Complete Table 8 line items, quantity basis, price year, energy-use breakdown, bead synthesis yield, uncertainty/sensitivity and regeneration cost were not recoverable from the indexed text. No USD/m3 treated, full treatment train cost, scale-up TEA or actual wastewater performance is established.
- Use this as an example of how authors attempt a chemical-plus-energy adsorbent cost calculation, with strong qualifications. Do not rank it as a verified low-cost winner or compare USD/g-TC directly with SEM-050's USD/m2 active-layer cost.

## Semester-paper recommendation
Retain provisionally as a relevant TC-specific CMC/GO composite-bead empirical study. Use its condition-specific removal and clearly labelled derived qe values, not the fitted qmax as measured capacity. Explicitly flag condition inconsistencies in dosage, temperature, isotherm basis and regeneration concentration. Treat the USD 1.95/g-TC as an author estimate whose functional unit and input transparency are limited. No real-water, continuous-flow or full-scale economics evidence.

## Citation workflow
The latest uploaded 173-entry Zotero export had no exact DOI/title match. No Better BibTeX key has been invented. Add and reconcile Zotero metadata only if the study is selected for citation, then use the actual generated key.

## Repository updates
Updated:
- data/semester-remaining-work-register.csv
- data/semester-paper-candidate-register.csv
- data/semester-evidence-readiness-audit.csv
- data/semester-condition-labelled-comparison.csv
- README.md

No new evidence ID was created; EV-SEM-047 was updated in place.
