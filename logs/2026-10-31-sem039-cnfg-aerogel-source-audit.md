# SEM-039 CNF/GO aerogel source audit — 31 October 2026

## Study identity and source
Yao, Fan, Xiong, Jin, Sun and Sheng (2017), “3D assembly based on 2D structure of Cellulose Nanofibril/Graphene Oxide Hybrid Aerogel for Adsorptive Removal of Antibiotics in Water,” *Scientific Reports* 7, article 45914. DOI: 10.1038/srep45914.

Official open-access publisher article: https://www.nature.com/articles/srep45914
PubMed/PMC full-text copy: https://pmc.ncbi.nlm.nih.gov/articles/PMC5377467/

Primary article sections, figures, captions and Materials and Methods rechecked. No journal-quartile status was considered, per the semester-paper instruction.

## Material identity and preparation
- Material: cellulose nanofibril/graphene oxide (CNF/GO) hybrid aerogel, a graphene-bearing biopolymer composite.
- CNF feedstock: moso bamboo (Phyllostachys heterocycla). The CNF and GO precursor syntheses are attributed to earlier literature methods; the article does not give a full upstream CNF pulping/fibrillation or GO Hummers process inventory.
- Aerogel precursor mixture: 80 mg CNF + 100 mg GO in 100 mL deionized water. The nominal dry-solids mixture is therefore 44.4 wt% CNF and 55.6 wt% GO before any process yield losses.
- One-step sonication: 30 min at 60 kHz using a 25-mm titanium horn, 0.5 s on / 0.5 s off duty cycle, ice bath, stated output power 1000 W.
- Freeze at −30 °C for more than 5 h.
- Vacuum freeze-dry for 48 h at condenser temperature −55 °C and 80 mTorr.
- The paper describes hydrogen bonding between oxygen-containing groups of GO and hydroxyl groups in CNF; BET area increases from 3.3 m²/g for CNF to 97.5 m²/g for CNF/GO, with pore volume 0.4 cm³/g and a mesopore peak near 10.2 nm.

This is a simple-looking aqueous assembly route, but not automatically a low-cost route: the high-output sonication and 48 h vacuum freeze-drying are material energy/time burdens. The study reports no measured power consumption, freeze-dryer throughput, process yield, reagent recovery, CNF/GO price or normalized cost. Its “economical” characterization is not supported by a financial TEA or LCA.

## Adsorption method and the missing Figure 7 operating point
General batch method:
- 8 mg CNF/GO aerogel in 40 mL antibiotic solution (nominal 0.2 g/L dose).
- 50 mL Erlenmeyer flask, water-bath shaker at 160 rpm.
- Overnight incubation at 25 °C, covered with foil to reduce possible photodegradation.
- General feed concentration range 1–100 mg/L and pH adjustable from 2 to 12.
- Removal and qe calculated from initial/equilibrium concentration, volume and adsorbent mass.

Figure 7 reports tetracycline (TC) removal of 82.1% in the 21-antibiotic screening panel. It also reports DXC 90.5%, CTC 88.3% and OTC 87.9%. Crucially, Figure 7's caption does not specify a unique initial concentration, pH or dose. The general protocol gives a broad concentration and pH range, not the precise operating point for this particular Figure 7 endpoint. Do not attach the separate Figure 10 factor-test settings to Figure 7 and do not use 82.1% in a condition-matched removal ranking.

The article screens 21 compounds and discusses their relative removal. The article's separate Figure 3f / competition-type claims should be distinguished from the Figure 7 endpoint; the audit does not relabel every Figure 7 bar as a simultaneous mixed-feed test without explicit source confirmation.

## Separate TC factor tests — do not transfer these to Figure 7
- pH: C0=20 mg/L, 4 mg aerogel in 40 mL (0.1 g/L), 160 rpm, 24 h, 25 ± 2 °C, pH 2–12. Highest TC removal occurs at pH 2.
- Temperature: C0=20 mg/L, 4 mg/40 mL, pH 2, 8 h, 25/35/45 °C. Methods contains a typographic concentration string “20 mg mg/L”; this is recorded as a source typo, not silently repaired in the original.
- Dose: C0=20 mg/L, pH 2, 24 h, 0.25–2 g/L; removal rises with dose and approaches a plateau at approximately 1 g/L.
- TC initial-concentration series: 20, 30, 50, 100 and 160 mg/L, 4 mg aerogel in 40 mL, pH 2, 24 h. Removal decreases as feed concentration increases.
- These factor tests use 4 mg/40 mL (0.1 g/L), which differs from the general batch protocol of 8 mg/40 mL (0.2 g/L). Preserve the distinction.

## Kinetics and isotherm — separate fitted quantities
- Table 1 / Figure 8 report pseudo-second-order fitted qe=84.8 mg/g, with R² approximately .99 compared with PFO R² approximately .83; the authors interpret this as chemisorption. For the semester synthesis, PSO fit superiority alone is not proof of a chemical adsorption mechanism.
- Table 2 / Figure 9 report Langmuir fitted theoretical qm=454.6 mg/g, R²=.99; Freundlich fit R²=.98. The conclusion rounds the same q_m to 454.5 mg/g. Preserve the source's 454.6/454.5 rounding difference. Neither q_m nor kinetic fitted qe is an observed qe.
- On the general protocol basis, the maximum feed-limited qe at C0=100 mg/L is 500 mg/g (100 mg/L ×0.040 L /0.008 g). The fitted qm=454.6 mg/g is below that ceiling, but that is only a plausibility check against the general upper range; it does not convert a model fit into an observed capacity or establish the Figure 7 condition.

## Ten-cycle regeneration
- Regeneration: immerse the exhausted aerogel in 5 wt.% NaOH for 5 h, separate, wash, then vacuum freeze-dry before the next run.
- For TC, removal after ten cycles is reported as 78.9% versus 82.1% in the initial screening.
- This is a decline of 3.2 percentage points, or approximately 3.9% relative to the initial 82.1% removal. Do not label 78.9% as adsorption-capacity retention unless the source provides that metric.
- The paper's phrase “lost 2–5.7%” across the 21 antibiotics is a removal-percentage comparison; the TC-specific values above remain the directly stated evidence.

## Mechanism evidence
The article proposes electrostatic attraction, π–π stacking, π–p stacking and hydrogen bonding. The proposed interactions are supported by pre-/post-adsorption SEM/TEM and FTIR changes, plus characterization of GO/CNF bonding. This supports an evidence-based mechanism hypothesis, but not quantitative apportionment among pathways. Pseudo-second-order kinetics do not independently prove chemisorption.

## Low-cost and practical relevance
- Positive practical attributes: a macroscopic aerogel is easier to separate from solution than dispersed GO; ten-cycle TC removal remains close to the initial percentage; bamboo-derived CNF is a renewable feedstock.
- Limitations: GO remains a significant mass fraction (~55.6% of the initial dry CNF+GO blend); CNF/GO precursor production is not fully documented in this paper; stated 1000 W ultrasonication and 48 h lyophilization are energy/time intensive; regeneration needs 5 wt.% NaOH and repeated freeze-drying.
- No actual municipal/river/industrial wastewater test, column/flow experiment, adsorbent yield, measured operating energy, reagent-recovery data, financial cost, treatment cost per m³ or full-process LCA/TEA was found in the article.
- Therefore retain it as a composite architecture and regeneration case, not as a demonstrated low-cost treatment winner.

## Semester-paper decision
Retain SEM-039 / EV-SEM-015. Report separately:
1. Figure 7 TC removal 82.1%, but not condition-matched because its caption omits C0/pH/dose.
2. PSO fitted qe 84.8 mg/g.
3. Langmuir fitted qm 454.6 mg/g in Results/abstract; 454.5 mg/g in conclusion.
4. TC removal 78.9% after ten-cycle reuse vs 82.1% initially.
Do not merge these values or attach conditions from separate factor tests to Figure 7. Highlight the energy-intensive sonication/freeze-drying and absence of cost/real-water evidence.

## Repository updates
Updated in place:
- data/semester-remaining-work-register.csv
- data/semester-paper-candidate-register.csv
- data/semester-evidence-readiness-audit.csv (existing EV-SEM-015)
- data/semester-condition-labelled-comparison.csv
- README.md

No new evidence ID was created; EV-SEM-015 was updated in place.
