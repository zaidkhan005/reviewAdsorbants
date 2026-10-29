# Semester evidence readiness and next-execution audit

**Date:** 29 October 2026  
**Status:** Working audit of the semester review files, not a final systematic-review decision or accepted-paper list.

## Current snapshot

| Register or artifact | Live count | Interpretation |
|---|---:|---|
| Semester candidate register | 44 rows | Includes one duplicate alias row |
| Unique DOI-defined studies | 43 | SEM-026 is canonical for Fei et al. (2016); SEM-041 is its alias |
| Semester evidence CSV | 33 rows / 33 unique evidence IDs | Source-linked evidence records, not 33 validated or accepted studies |
| Semester crosswalk | 44 rows | One row per retained register identifier, including the alias |
| Broad candidate register | 111 rows | Separate full-review workstream |
| Broad evidence CSV | 505 rows | Separate full-review evidence stream |
| Better BibTeX processing queue | 164 entries | Bibliographic inventory; not proof of eligibility or citation |

## Integrity checks completed

- No duplicate candidate IDs.
- No duplicate evidence IDs.
- No evidence row points to a missing candidate ID.
- No crosswalk IDs are missing from or extra to the 44-row register.
- One duplicate DOI was identified: SEM-026 and SEM-041, DOI 10.1016/j.jcis.2016.08.068. SEM-026 is now canonical, evidence EV-SEM-020 points to SEM-026, and SEM-041 remains as an alias for traceability. Count this paper once.
- EV-SEM-010 and EV-SEM-013 had source content shifted across the declared evidence CSV fields. Those rows are now remapped so observed results, fitted/model values, kinetics, mechanism, reuse, cost, source pin, URL, extraction status and caveats appear in their intended columns.
- The previously blank caveat cells in EV-SEM-010 and EV-SEM-013 are now filled.

## Evidence-readiness tiers

### Tier 1 — usable quantitative source material, still condition-bound

- **SEM-001 / EV-SEM-001, GO for TC:** full PLOS source audited; fitted Langmuir values differ sharply across 298/303/308 K (322.43/101.87/73.53 mg/g), so the temperature/table consistency caveat must stay.
- **SEM-015 / EV-SEM-005, GO–ZnAlNi-LDH for CIP:** full article audited; 84.84% removal at C0 1 mg/L, dose 10 mg/L, pH 7, 60 min; equation implies qe≈84.84 mg/g while the kinetic table gives model-fitted qe≈106.96 mg/g; capacities quarantined.
- **SEM-016 / EV-SEM-012, sulfonated GO for CIP:** full Library PDF; Langmuir fitted qmax=1000 μmol/g (=331.35 mg/g), but qe/removal source consistency flag remains; multistep strong-acid/oxidant preparation and 1 M HCl in DMF regeneration are uncosted.
- **SEM-032 / EV-SEM-013, PGOT@GEL for CIP:** full Library PDF; fitted qmax, RSM-predicted response, measured validation qe, and separate pH-test qe now restored to the correct columns; matrix wording and cost remain caveated.
- **SEM-039 / EV-SEM-015, CNF/GO aerogel for TC:** publisher full text reviewed; Fig. 7 removal=82.1%; model qe=84.8 mg/g; Langmuir qm=454.6 mg/g in abstract/Results and 454.5 mg/g in conclusion; ten-cycle removal=78.9%. Preparation uses 30 min ultrasonication, >5 h freezing and 48 h vacuum freeze-drying; regeneration uses 5 wt.% NaOH for 5 h; no quantified cost inventory.
- **SEM-040 / EV-SEM-016, graphene for TC in a mixed seven-antibiotic solution:** publisher full text reviewed; initial concentration 200 μg/L per drug, pH 7, 298 K, 120 rpm; exact TC percent is figure-based and was not guessed.

### Tier 2 — target-relevant, numeric claims provisional or source access partial

- **SEM-002 / EV-SEM-017:** GO nanosheets tested on both CIP and TC; publisher text supports CIP capacity up to 173.4 mg/g and pH/time conditions, but a numeric TC capacity and full condition table were not verified.
- **SEM-003 / EV-SEM-018:** GO for CIP/NOR/OFL; pH effect confirmed, no quantitative CIP value extracted.
- **SEM-005 / EV-SEM-019:** magnetic GO sponge for TC; abstract reports 473 mg/g but fitted-versus-observed metric is not established.
- **SEM-020 / EV-SEM-014:** graphene versus GAC for CIP; publisher abstract reports fitted qmax=323 mg/g and rapid equilibrium, but detailed conditions/tables remain unavailable. GAC is benchmark only.
- **SEM-024 / EV-SEM-024:** GO for TC; abstract reports fitted Langmuir qmax=313 mg/g and pseudo-second-order kinetic constant; conditions and tables remain unavailable.
- **SEM-026 / EV-SEM-020:** GO–sodium alginate hydrogel/aerogel for CIP; primary abstract reports ~7–9-fold capacity improvement after GO incorporation and Langmuir fit. q_m=86.12 mg/g appears only in a secondary comparison table; it is not primary-table verified.
- **SEM-043 / EV-SEM-022:** GO for CIP/SMX; primary abstract reports 379 mg/g for CIP and 240 mg/g for SMX. Use CIP only; exact experimental conditions and fitted/observed endpoint remain unverified.
- **SEM-044 / EV-SEM-023:** MgO/chitosan/GO for CIP/NOR; abstract reports capacities 1111 mg/g CIP and 1000 mg/g NOR; high value needs primary-table confirmation. Keep NOR separate.
- **SEM-038 / broad CORP-031 / EV-B10-004–009:** N-rGO/TC; evidence is cross-referenced, not duplicated. The qm and kinetic qe values remain quarantined due the dose/concentration mass-balance concern.

### Tier 3 — source access or specific data-quality issue

- **SEM-006:** DTPA-functionalized magnetic GO tests both CIP and TC; indexed values are pseudo-second-order model-derived qe, not Langmuir qmax; primary numeric tables are not verified.
- **SEM-037:** GO–alginate PRB for CIP groundwater; abstract reports 100 mg/g at pH 7 and ~72 h equilibrium, but cost/lifetime/column assumptions remain unavailable.
- **SEM-041:** duplicate alias of SEM-026; not a separate study.
- **SEM-042 / EV-SEM-021:** chitin/nGO continuous-flow CIP; primary abstract confirms flow testing, alkali regeneration/reuse and CIP-spiked real-water testing. The indexed “100 grams” in a small 1-cm-ID column is physically implausible and remains quarantined; do not repeat as fact.
- **Other candidates without dedicated evidence rows:** these remain discovery-stage or not yet extracted to the evidence schema. Their absence from the evidence CSV is not automatically an exclusion decision.

## Next execution sequence

1. Prioritize primary-source data validation rather than more broad searches. Next high-value details are SEM-026’s primary isotherm table, SEM-043’s exact condition/fitted metric, SEM-044’s unusually high reported CIP capacity, and SEM-005’s 473 mg/g metric definition. SEM-042’s accepted-manuscript text has now been audited; its 100-g/column-geometry anomaly is confirmed and dynamic q₀/τ values are quarantined. SEM-027, SEM-029 and SEM-034 have also been extracted from open full text as EV-SEM-025–EV-SEM-027. SEM-019 and SEM-028 have since been added as EV-SEM-028–EV-SEM-029; SEM-014 and SEM-030 are now represented by EV-SEM-030–EV-SEM-031.
2. Keep low-cost claims evidence-based. No study should be called demonstrably low-cost when whole-process synthesis, yield, energy, recovery and cost denominator are missing. Preparation and regeneration burdens are proxies, not monetary estimates.
3. Build comparisons around evidence class: batch results, mixed-solute tests, water-matrix tests and continuous-flow/column evidence. Put qmax/qm in a fitted-capacity column; do not merge it with observed qe, kinetic-model qe or removal percentage.
4. Complete final inclusion only after target-drug, material-family, article type, source status and journal/year/category ranking checks. The approximately 50-work citation target remains open and is counted as distinct works actually cited, not candidate rows.

**User action required: none.** The user has paused new downloads/uploads. Continue with existing Library files and accessible publisher/abstract sources.


## Follow-on validation — SEM-042 accepted-manuscript column audit (29 October 2026)

The accepted manuscript reports batch Sips fit as best and Langmuir qₘ=73±3 mg/g for Chi:nGO versus 282±11 mg/g for pure nGO. Table 1/2 include Thomas q₀ and Yoon–Nelson τ results across flow/pH/salinity/hardness and CIP-spiked real waters. However, Methods says 100 g packed into a 1.0-cm-ID column with a 1.5-cm bed (1.178 cm³), an impossible ~84.9 g/cm³ implied density. Do not use dynamic q₀/τ to rank performance until the amount is corrected by a reliable source. The manuscript’s qualitative low-cost claim remains unquantified.


## Follow-on primary-source extraction — 29 October 2026

The semester evidence CSV now contains **27 unique evidence IDs**. Three further primary open-access papers were extracted:

- **SEM-027 / EV-SEM-025 — Choi & Choi (2022), GO/Ca-alginate–PAM beads for CIP.** Langmuir fitted qₘ=6.846 mg/g (R²=.991), with temperature-series thermodynamics. No directly observed qe/removal or reuse result was identified in the accessible text. The source states 55 mL solution in a 50 mL tube; preserve this method inconsistency.
- **SEM-029 / EV-SEM-026 — Hossain et al. (2026), GO/PVA/calcium-alginate beads for CIP.** Observed qe max 7.15 mg/g; linear/nonlinear Langmuir qₘ=8.210/10.14 mg/g; nonlinear PSO model qe=4.458 mg/g; separately reported removal ~89.82/89.92%. Linear/nonlinear D–R model outputs conflict; linear PFO k₁ is negative. The cost analysis assumes 0.1 g/L while the paper's stated optimum is 0.5 g/50 mL (=10 g/L), a 100× discrepancy; its lifecycle cost claim is not independently reproducible.
- **SEM-034 / EV-SEM-027 — Hossain et al. (2024), GO/Co–Fe magnetic nanocomposite for TC.** At C₀=.2 mg/L, dose=.15 g/L, pH 7, 30 s and 25°C, removal is 94.1% in the abstract/body but 93.94% elsewhere. Langmuir qₘ=64.10 mg/g is fitted at 50°C, not the same condition. CTC/OTC/DTC are kept separate; no cost or real-water test was reported.

These papers provide usable source-derived evidence, but none supports an unconditional cost or capacity ranking. Candidate register remains 44 rows / 43 DOI-defined works (SEM-041 is the SEM-026 alias). The ~50 actually-cited-work target remains open.


## Follow-on extraction — SEM-019 and SEM-028 (29 October 2026)

The evidence CSV now has **29 unique records**.

- **SEM-019 / EV-SEM-028 — EDTA-functionalized magnetic GO for TC:** 93.23% removal at C₀=0.2 mg/L, 20 mL, dose 0.10 g/L, pH 5, 5 min and 25°C. Mass-balance qₑ≈1.865 mg/g, while the source reports PSO fitted qₑ=0.01937 mg/g (R²=1), about 96× lower. Keep the discrepancy explicit and quarantine the kinetic-model qₑ; Langmuir qmax=31.32 mg/g at 25°C has weak R²=.691, while Freundlich fits better. Eight-cycle removal declines ~94%→90.50%; no quantified cost.
- **SEM-028 / EV-SEM-029 — GO/calcium-alginate fibers for CIP:** abstract/snippets report 78.9% removal at 2 g/L and 6 wt% GO, optimum pH 5.9 and 24 h equilibrium, plus observed capacity 18.45→39.06 mg/g as GO loading increases 0→6 wt% at equilibrium C=60 mg/L. Exact paired conditions, numeric fitted parameters, full spinning recipe and cost/reuse data were not accessible.

The register remains 44 rows / 43 DOI-defined studies (SEM-041 is a retained alias of SEM-026). These additions do not expand the approved scope; they fill evidence gaps in already registered candidates.


## Latest primary-publisher preview checks — SEM-014 and SEM-030

The dedicated evidence CSV now has **31 unique rows**. SEM-014 (GO·Fe₃O₄ for TC) reports 531.93 mg/g at C₀=1000 mg/L, 50 mg dose, pH 7 and 293 K; solution volume and whether the reported capacity is observed or fitted are not visible in the preview. DFT values are not experimental adsorption metrics. SEM-030 (GO–[Ni(DMG)]ₙ for CIP) reports Langmuir-comparison qmax 117–159 mg/g and PSO k=0.0005–0.0009 g/(mg·min), but says Freundlich/Temkin fit the isotherms better; exact conditions, ratios, reuse and cost are not accessible in the abstract. Both rows remain provisional and cannot be ranked as validated capacities.


## Further source checks — SEM-012 and SEM-025 (29 October 2026)

The dedicated evidence CSV now contains **33 unique records**. SEM-012’s primary publisher text reports 96.39% CIP removal at 15 mg/L, 0.55 g composite in 15 mL (=36.7 g/L), pH 7, 33 min and ultrasonic-bath conditions; source-derived matrix results are ~90–94% removal in tap, river, lake and wastewater. A mass-balance calculation implies qe≈0.394 mg/g at the stated optimum, but that is derived rather than directly reported. Ultrasound power/energy and numerical isotherm parameters are unavailable, so this case needs a distinct ultrasound-assisted operating label. SEM-025’s abstract-level preview reports fitted Langmuir qₘ=282.9 mg/g, PSO kinetics and ~72% of initial capacity after four uses, but exact feed/dose/temperature and cost are not accessible. These remain provisional source records, not validated rankings.
