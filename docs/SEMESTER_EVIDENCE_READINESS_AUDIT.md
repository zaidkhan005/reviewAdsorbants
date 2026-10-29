# Semester evidence readiness and next-execution audit

**Date:** 29 October 2026  
**Status:** Working audit of the semester review files, not a final systematic-review decision or accepted-paper list.

## Current snapshot

| Register or artifact | Live count | Interpretation |
|---|---:|---|
| Semester candidate register | 44 rows | Includes one duplicate alias row |
| Unique DOI-defined studies | 43 | SEM-026 is canonical for Fei et al. (2016); SEM-041 is its alias |
| Semester evidence CSV | 24 rows / 24 unique evidence IDs | Source-linked evidence records, not 24 validated or accepted studies |
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

1. Prioritize primary-source data validation rather than more broad searches. Next high-value details are SEM-026’s primary isotherm table, SEM-043’s exact condition/fitted metric, SEM-044’s unusually high reported CIP capacity, and SEM-005’s 473 mg/g metric definition. SEM-042’s accepted-manuscript text has now been audited; its 100-g/column-geometry anomaly is confirmed and dynamic q₀/τ values are quarantined.
2. Keep low-cost claims evidence-based. No study should be called demonstrably low-cost when whole-process synthesis, yield, energy, recovery and cost denominator are missing. Preparation and regeneration burdens are proxies, not monetary estimates.
3. Build comparisons around evidence class: batch results, mixed-solute tests, water-matrix tests and continuous-flow/column evidence. Put qmax/qm in a fitted-capacity column; do not merge it with observed qe, kinetic-model qe or removal percentage.
4. Complete final inclusion only after target-drug, material-family, article type, source status and journal/year/category ranking checks. The approximately 50-work citation target remains open and is counted as distinct works actually cited, not candidate rows.

**User action required: none.** The user has paused new downloads/uploads. Continue with existing Library files and accessible publisher/abstract sources.


## Follow-on validation — SEM-042 accepted-manuscript column audit (29 October 2026)

The accepted manuscript reports batch Sips fit as best and Langmuir qₘ=73±3 mg/g for Chi:nGO versus 282±11 mg/g for pure nGO. Table 1/2 include Thomas q₀ and Yoon–Nelson τ results across flow/pH/salinity/hardness and CIP-spiked real waters. However, Methods says 100 g packed into a 1.0-cm-ID column with a 1.5-cm bed (1.178 cm³), an impossible ~84.9 g/cm³ implied density. Do not use dynamic q₀/τ to rank performance until the amount is corrected by a reliable source. The manuscript’s qualitative low-cost claim remains unquantified.
