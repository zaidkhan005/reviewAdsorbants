# SEM-006 DDMGO main-text source audit — 31 October 2026

## Study identity and source
Li, M.-f., Liu, Y.-g., Liu, S.-b., Zeng, G.-m., Hu, X.-j., Tan, X.-f., Jiang, L.-h., Liu, N., Wen, J. and Liu, X.-h. (2018), “Performance of magnetic graphene oxide/diethylenetriaminepentaacetic acid nanocomposite for the tetracycline and ciprofloxacin adsorption in single and binary systems,” *Journal of Colloid and Interface Science* 521, 150–159. DOI: 10.1016/j.jcis.2018.03.003.

Publisher record: https://www.sciencedirect.com/science/article/abs/pii/S0021979718302455
University-hosted full-text PDF: https://ee.hnu.edu.cn/__local/7/00/07/132E7D46F401B025BF92B18714F_758970B3_2B3DCB.pdf
PubMed record: https://pubmed.ncbi.nlm.nih.gov/29567603/

The 10-page main PDF was opened and parsed from the university-hosted primary copy. The web PDF screenshot renderer timed out on three pages, and a direct file download attempt also failed; therefore no figure-plot points have been visually digitized. The main article explicitly references SI Tables S1–S3 for detailed kinetic, isotherm and thermodynamic parameters, but these were not included with the retrieved 10-page PDF. No new PDF upload is requested.

## Material identity and synthesis
- Adsorbent: diethylenetriaminepentaacetic acid (DTPA)-functionalized magnetic graphene oxide, named DDMGO.
- MGO is prepared by a previous method referenced by the authors; this article does not restate the full GO oxidation and Fe3O4 loading recipe. Do not silently fill it from other papers.
- For DTPA functionalization, 0.8 g DTPA is dissolved in low-concentration ammonia; 0.4 g EDC and 0.4 g NHS are added to activate carboxyl groups with stirring for 2 h at room temperature.
- Then 40 mL diethylenetriamine and a dispersion containing 2 g MGO are added; the reaction is stirred at 80 °C for 6 h, cooled, repeatedly rinsed with Milli-Q water to approximately neutral pH and stored at room temperature.
- BET area: 176 m²/g (compared with 115 m²/g for MGO); mean pore diameter 3.8 nm; pore volume 0.24 cm³/g. Fe3O4 reflections and magnetic performance enable external magnetic separation.
- FTIR includes a new 1458 cm−1 band assigned to amide linkage; post-adsorption shifts in C=C, O–H, C=O and amide-related bands are discussed as supporting interactions.
- Process-burden boundary is incomplete: upstream MGO recipe is referenced elsewhere, but this paper uses DTPA, EDC, NHS, 40 mL diethylenetriamine, ammonia and 80 °C/6 h reaction plus repeated Milli-Q washing. No yield, reagent recovery, energy consumption, normalized cost or LCA/TEA is supplied. Magnetic separability does not prove low total cost.

## Batch conditions and fitted kinetic values
- Kinetics (single antibiotic tests): initial concentration 50 mg/L; dose m/V = 0.09 g/L; pH 3.0; 30 °C; 150 rpm; contact time 0–1560 min. Flasks are described as 25 mL conical flasks, with about 2.28 mg DDMGO per reaction. The precise liquid volume is not explicitly stated, though 2.28 mg / 0.09 g L−1 implies approximately 25.3 mL.
- CIP approaches apparent equilibrium after roughly 1 h; TC continues increasing and reaches a plateau around 24 h.
- Main-text §3.2 gives pseudo-second-order (PSO) calculated qe values of 294.12 mg/g (TC) and 111.73 mg/g (CIP), with both PSO R² values >0.99 and better than pseudo-first-order.
- These are model-fitted kinetic qe values, not directly tabulated measured qe values and not Langmuir qmax. Exact measured qe and numerical kinetic fit statistics are unavailable in the retrieved main text because Table S1 is in missing SI.
- Simple feed-mass ceiling at C0=50 mg/L and m/V=0.09 g/L is 50 / 0.09 = 555.6 mg/g. Both PSO fitted qe values are below that ceiling, so the fitted values do not violate a simple mass-balance limit. This plausibility check does not establish that they equal observed uptake.

## Isotherm and thermodynamics
- Isotherm and thermodynamic tests use TC or CIP initial concentration 0–500 mg/L, pH 3.0, m/V=0.09 g/L, 24 h, and temperatures 293, 303 and 313 K.
- Authors state Freundlich describes the data better than Langmuir at all temperatures, based on higher correlation coefficients and lower RMSE and chi-square. Numerical Table S2 parameters are unavailable in the retrieved main PDF.
- Do not invent a Langmuir qmax or present the PSO qe values as capacity parameters.
- Authors state TC adsorption is endothermic (positive ΔH) and becomes more favorable with increasing temperature; CIP adsorption is exothermic (negative ΔH). ΔG values are negative for both, consistent with spontaneity. Exact Table S3 values are unavailable.

## pH response and speciation
- pH tests use C0=50 mg/L and 30 °C over pH 2–10.
- TC adsorption maximum is around pH 3. The authors state electrostatic attraction is not the main driver for TC there; cation–π interaction and other mechanisms likely contribute.
- CIP adsorption increases with pH to a maximum around pH 8, then declines. Authors discuss CIP speciation (cation below pH5.9, zwitterion pH5.9–8.9, anion above pH8.9) and DDMGO charge transition from positive below pH4 to negative above pH4.
- A potential discrepancy between text-layer plot extraction at CIP pH3 in Figures 3 and 5 was previously flagged, but it cannot be visually confirmed because the PDF screenshot renderer timed out and direct download failed. Do not quote the machine-extracted pH3 curve point; the main prose explicitly says CIP maximum is around pH8 and the pH3 condition is selected for later ion/binary experiments.

## Ionic-strength and background electrolyte effects
- NaCl ionic strength tested from 0 to 0.5 M. Low ionic strength 0–0.01 M inhibited uptake; beyond 0.01 M the paper reports increased uptake, attributed to salting-out effects.
- Background ions K+, Mg2+, Cl− and SO4²− tested from 0 to 0.1 M at pH3. SO4²− has a stronger promoting effect than Cl−; low Cl− slightly inhibits. Mg²⁺ reduces TC adsorption, while K+ has little distinct effect on TC. Low K+/Mg²⁺ compete with CIP; at higher concentration the authors invoke salting-out to explain a rebound in CIP uptake.
- These are controlled simulated electrolyte tests, not a real-water validation. Some ion concentrations are far above typical freshwater concentrations; describe as mechanistic stress tests rather than natural-water performance.

## Binary TC/CIP competition
- Binary experiments: 50 mg/L TC with 0–20 mg/L CIP, and 50 mg/L CIP with 0–20 mg/L TC; same stated single-system conditions.
- With increasing CIP concentration, TC adsorption decreases. The ratio q_b/q_s for TC is 0.39–0.90 over the tested CIP range.
- By contrast, CIP adsorption changes only slightly when TC is added; q_b/q_s for CIP remains close to 1.00 over 0–20 mg/L added TC.
- This asymmetry is useful mechanistic/application evidence: CIP competition suppresses TC uptake more strongly than TC suppresses CIP uptake. Do not combine their capacities into one pooled value.

## Desorption and reuse
- Four successive adsorption/desorption cycles use 0.01 M NaOH as eluent.
- Cycle-specific setup: 250 mL of 50 mg/L single TC or CIP solution, or binary feeds (50 mg/L TC +10 mg/L CIP; 50 mg/L CIP +10 mg/L TC); DDMGO dose about22.8mg; 30 °C; pH3; 24 h. Solid/liquid separation is by permanent magnet.
- Authors report removal efficiencies remain above 78% after at least four cycles in single and binary systems. The main text does not give a clean numerical TC-only retained-capacity series. Do not report this as a precise percentage capacity retention for TC.

## Mechanism evidence
- Main proposed mechanisms: π–π interactions, hydrogen bonding and amidation-related interactions; TC additionally through cation–π interactions; CIP affected by electrostatic interactions.
- FTIR shifts in C=C, O–H, C=O and amide-associated bands and XPS shifts in C 1s/N 1s/O 1s support changes in surface bonding after adsorption.
- Treat this as an evidence-supported mechanism hypothesis. The data do not quantitatively apportion individual mechanisms, and a PSO fit alone does not prove chemisorption.

## Cost, scale and real-water evidence
- No monetized cost, yield, electricity, normalized cost per gram or per treated m³, regeneration operating cost or full LCA/TEA is reported.
- No actual wastewater matrix experiment is reported; the authors themselves state that real wastewater has additional organic and inorganic components and further study is needed.
- No metal/iron leaching quantification or long-term field stability test is found in the main article.
- Suitable use: compare how functionalization and magnetic separation can address the recovery challenge, and discuss asymmetric binary competition. Not suitable as a validated low-cost real-water treatment winner.

## Semester-paper decision
Retain SEM-006 / EV-SEM-008 as a primary DDMGO study. In quantitative synthesis:
1. Label 294.12 mg/g (TC) and 111.73 mg/g (CIP) strictly as PSO-fitted qe; do not call them measured qe or qmax.
2. Keep both separate from the Freundlich equilibrium fit; numerical SI fit tables are not available.
3. State TC pH optimum≈3 and CIP≈8.
4. Report TC q_b/q_s=0.39–0.90 with added CIP, and CIP q_b/q_s≈1 with added TC.
5. Describe four-cycle 0.01 M NaOH regeneration with removal >78%, not TC-only capacity retention.
6. Flag no real-water test and no quantified preparation/treatment cost.
7. Leave the extracted CIP pH3 plot discrepancy unresolved; no guessed value.

## Repository updates
Updated in place:
- data/semester-remaining-work-register.csv
- data/semester-paper-candidate-register.csv
- data/semester-evidence-readiness-audit.csv (EV-SEM-008)
- data/semester-condition-labelled-comparison.csv
- README.md

No new evidence ID was created; EV-SEM-008 was updated in place. SI Tables S1–S3 remain a source-access limitation. No new PDF upload has been requested.
