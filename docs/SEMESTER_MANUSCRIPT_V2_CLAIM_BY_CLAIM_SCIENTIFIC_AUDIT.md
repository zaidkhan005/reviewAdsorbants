# Semester Manuscript V2 — Claim-by-Claim Scientific Audit

**Audit date:** 31 October 2026  
**Manuscript:** `manuscript/SEMESTER_MANUSCRIPT_WORKING_V1.md` (content labelled Unified working manuscript V2)  
**Approved scope:** 49 selected works plus four separately identified contextual sources  
**Audit status:** First consolidated scientific claim-audit pass; not final submission sign-off

## 1. Executive finding

The central argument of V2 is scientifically defensible **when the source-tier and endpoint caveats are retained**:

- Selected GO, rGO and graphene-bearing composites have demonstrated CIP and/or TC adsorption under laboratory conditions.
- Reported percentages, observed uptake, fitted isotherm capacities, kinetic-model outputs and column metrics do not form one comparable performance scale.
- Magnetic separation and immobilization can help handling, but do not establish lower overall treatment cost.
- The evidence for full-process affordability is weak; active-layer or author-reported material-price calculations are not equivalent to complete treatment techno-economic analysis.
- Mechanistic explanations are plausible and material/condition-dependent; the available evidence generally does not isolate a unique dominant binding pathway.

**No broad claim that graphene-based adsorbents are universally superior or already low-cost is supported, and V2 does not make that claim.** The most serious problems are local: source-internal mass-balance contradictions, fitted values that exceed finite-feed ceilings, access-gated claims and author cost scenarios whose assumptions do not match the experiments. These have to remain explicitly qualified or held from quantitative comparison.

This audit covers **34 claim groups** in the active claim-evidence ledger. A claim group may cover more than one related sentence or numerical endpoint; it is not a separate claim ID for every sentence in the manuscript. Detailed source-pin notes and required treatment are in `data/semester-manuscript-claim-evidence-audit.csv`.

## 2. Audit basis and limits

The audit compared the V2 manuscript against the project's existing primary-source extractions, evidence notes, condition-labelled comparison, mechanism matrix, practical-feasibility matrix, readiness audit and claim-evidence ledger. Where an original primary full text and its relevant tables/figures had already been extracted, those pins and calculations were used. Where the project evidence is based on an abstract, publisher preview, indexed excerpt or third-party manuscript mirror, the finding is deliberately restricted to that access level.

**This was not a fresh download and re-extraction of all 49 papers in this turn.** In particular, some access-gated records remain dependent on publisher abstracts or indexed snippets, and a complete original table/SI audit is not available for every selected paper. The audit therefore does not upgrade an abstract-level claim to full-text verification merely because it is now cited in V2.

No journal-quartile requirement was applied, in accordance with the semester-paper decision. The active 49-reference selection was not reopened. Candidate SEM-035 remains excluded for administrative/time reasons at the user's direction; this is not a scientific rejection. Evidence ID EV-SEM-035 continues to refer to the SEM-013 theoretical paper.

### Verdict vocabulary

| Verdict | Meaning |
|---|---|
| **SUPPORTED** | The statement is appropriately scoped and supported by the source or evidence record. |
| **QUALIFIED / PARTIAL** | The core statement can be retained, but conditions, metric type, source-access tier or a discrepancy must stay visible. |
| **PROVISIONAL** | Only abstract/preview/indexed evidence is available; use as context, not as a fully verified quantitative result. |
| **HOLD** | A quantitative or cost claim has an unresolved contradiction or inadequate basis and must not be used as an unqualified result or ranking. |
| **CONTEXT ONLY** | The source supports background or mechanism context, not core graphene-adsorbent performance. |

## 3. Section-level scientific assessment

| Manuscript location | Audit judgement | Finding |
|---|---|---|
| Abstract | **QUALIFIED / defensible** | It accurately describes the evidence as heterogeneous and source-tiered, states that no universal ranking is justified, and does not claim practical low cost has been demonstrated. The phrases “limited and heterogeneous” for real-water evidence and “most studies do not provide” comparable cost inventories are consistent with the extracted corpus. |
| 1.1 Adsorption as separation | **SUPPORTED** | Correctly distinguishes aqueous disappearance from degradation/mineralization and includes recovery, regenerant and spent-media management. The reviews are labelled as context, not primary experiments. |
| 1.2 CIP/TC solution chemistry | **SUPPORTED WITH SCOPE BOUNDARY** | The Ca-montmorillonite and dissolved humic-acid sources are explicitly labelled as context comparators, not graphene performance evidence. Their conditions are not transferred to the core adsorbents. |
| 1.3 Material rationale | **SUPPORTED / QUALIFIED** | GO/rGO and selected composite formats are described as design possibilities, not as proven process advantages. Magnetic recovery is not equated with stronger intrinsic adsorption. |
| 1.4 Affordability gap | **SUPPORTED** | The cost boundary includes yield, reagents, energy, washing, neutralization, recovery, regeneration, waste handling and a meaningful denominator. No unjustified cost ranking is made. |
| 1.5 Aim and questions | **SUPPORTED** | Consistent with the approved CIP/TC and graphene-based scope. |
| 2.1 Eligibility | **SUPPORTED** | The material and antibiotic boundaries are explicit. CIP is kept separate from NOR/OFL; TC is kept separate from CTC/OTC/DTC. Standalone clays, chitosan, alginate and other non-graphene media are not treated as core materials. |
| 2.2 Search strategy | **QUALIFIED** | The manuscript properly calls the process a focused public-web search, reports the dates and recorded query formulations, and does not claim exhaustive database coverage. The discovery platform name, formal source-by-source coverage and a general date/language restriction were not recorded. Scopus/Web of Science completion is not evidenced. |
| 2.3 Screening and deduplication | **QUALIFIED** | The 51 historical candidate rows, 50 DOI-defined works after the SEM-041/SEM-026 alias, and 49 active works are not presented as PRISMA flow counts. Reconciled retrieval, duplicate-removal, title/abstract exclusion and full-text exclusion counts are absent; the manuscript correctly says so. |
| 2.4 Extraction/evidence assessment | **SUPPORTED AS A DESCRIPTION OF THE PROJECT RECORD** | The specified extraction fields and mechanism evidence distinctions are present in the data/evidence registers. Full source pinpoint availability remains uneven by paper. |
| 2.5 Quantitative and cost synthesis | **SUPPORTED** | Endpoint distinctions and process-cost denominator requirements are correctly defined. |
| 3.1–3.2 Core single-solute examples | **QUALIFIED WITH MULTIPLE HOLDS** | The text generally reports the actual source problem rather than hiding it: Zhu et al. (2018) has a Langmuir/Freundlich fit-order issue; SEM-018 has separate temperature/model conditions; SEM-017 lacks one condition; SEM-010 conflicts on removal/uptake and dose units; SEM-032 lacks validation volume; SEM-016 has qe/removal inconsistencies; SEM-038 has a severe feed-basis discrepancy; and SEM-020 is abstract-level only. Do not convert these into a clean leaderboard. |
| 3.3 Composite, recovery and mixed-solute examples | **QUALIFIED** | CNF/GO Fig. 7 has incomplete conditions; the TC value in the seven-drug mixture has a very small feed-ceiling excess; GO/Co–Fe contains internal removal-percentage differences; the rotating-field study is preview-level and has no energy measurement. The manuscript keeps mixture and single-solute endpoints separate. |
| 3.4 Multicomponent and PRB evidence | **SUPPORTED WITH RESTRICTED INTERPRETATION** | SGO values are correctly identified as mixture totals, and the paper's explicit no-real-wastewater statement is retained. The PRB example is abstract/indexed-level and its Freundlich/Langmuir attribution conflict remains visible; no unavailable numerical cost or column performance is invented. |
| 3.5 Low-cost potential | **SUPPORTED, WITH A NEW QUANTITATIVE SANITY CHECK** | The GO/PVA/calcium-alginate bead author cost estimate uses 0.1 g/L, versus a key experimental 10 g/L loading. Its bead price and capacity imply a first-loading material-purchase ratio of roughly USD 1,399–4,196/kg CIP using observed uptake, or USD 986–2,959/kg CIP using fitted qmax. These are explicitly screening ratios, not lifecycle costs; they exclude regeneration and other process costs and do not credit reuse. They make the source's claimed low cost untenable on the stated experimental basis, while not claiming to calculate a validated lifetime cost. |
| 3.6.1–3.6.3 Expanded earlier-study coverage | **QUALIFIED** | The prose generally preserves abstract-only limits, fit-vs-measurement distinctions, corrected-figure requirements, third-party mirror limits and condition mismatches. The older records with unresolved keys or source access should not be upgraded to “fully verified” in the final copy. |
| 3.6.4 Recent composites | **MIXED: PARTIAL, PROVISIONAL AND HOLD** | The seven new claim records CLM-28–34 are documented below. The latest additions broaden the comparison but do not justify ranking fitted capacities or asserting real-water performance from incomplete samples. |
| 3.7 Limitations | **SUPPORTED** | The limitations accurately summarize the most important endpoint, condition, source and citation caveats. The SEM-010, SEM-016, SEM-038, SEM-034 and GO/PVA inconsistencies remain explicit. |
| Section 4 Mechanisms | **QUALIFIED / APPROPRIATELY CAUTIOUS** | π–π, electrostatic, hydrogen-bond and pore/transport pathways are presented as candidates. The text correctly states that PSO fit is not proof of chemisorption, Langmuir fit is not proof of a perfectly homogeneous monolayer, and spectroscopy or DFT alone does not quantify relative interaction contributions. The mechanism matrix should remain the control document for wording. |
| Section 5 Feasibility | **SUPPORTED / QUALIFIED** | Preparation and recovery burdens are described without turning them into fabricated costs. Magnetic recovery is not treated as a full separation cost; solvent/acid/alkali regeneration and spent-stream handling remain visible. SEM-050's membrane tests are distinguished from its powder-batch benchmark. |
| Section 6 Conclusions | **SUPPORTED** | The conclusions follow from the restricted evidence: adsorption promise is demonstrated, universal performance superiority is not, mechanism contributions are not isolated, and comparative low-cost status is unproven. |
| Table 1 | **SUPPORTED AS A 15-STUDY SUBSET** | Conditions and metric types are separated. It is not described as the entire 49-reference evidence set or as a universal rank order. |
| Supplementary Table S1 | **UPDATED** | All 49 rows remain present. The seven latest SEM-045–SEM-051 rows now carry the added source-specific cautions described below. |

## 4. Detailed findings for the newest claim groups (CLM-28–34)

| Claim ID | Study | Verdict | Required interpretation |
|---|---|---|---|
| CLM-28 | SEM-045, magnetic GO/Co-MOF for TC | **PARTIAL** | The 98% trace-condition removal and ten-cycle 98→91% removal trend can be reported with their conditions. Do not call PSO-fitted qe=19.5198mg/g observed uptake: it exceeds the same-run feed ceiling of 2mg/g. The 45°C Langmuir q_m=185.87mg/g exceeds the 100mg/g ceiling from the highest stated isotherm feed and dose. Fig.6 caption C0=.2mg/L conflicts with Methods range .05–10mg/L. |
| CLM-29 | SEM-046, ZrO2–Fe3O4/GO for CIP | **HOLD on qe and effluent percentage** | The 93.92% synthetic optimum may be stated as source-reported, but it implies qe≈9.392mg/g on the specified 100mL/0.3g basis; source Figure 5 gives 20.11mg/g and is inconsistent with the 10mg/g feed ceiling. Raw effluent 8.37→2.01mg/L calculates to 76.0%, not the paper's 90.75%. Do not repeat 90.75% as a correct arithmetic result. |
| CLM-30 | SEM-047, magnetic GO/NH2-UiO-66/alginate for TC | **PROVISIONAL** | Publisher abstract only. Keep 98.5% synthetic removal separate from 89.34% river-water removal, whose sample/spiking basis is not disclosed in the accessible preview. Langmuir q_m=161.4mg/g is fitted while Sips is reported best-fit. >80% over ten cycles is removal efficiency, not proven capacity retention. The corrigendum applies to the original paper and directs removal of the erroneous Funding statement; its results/conclusions are unchanged. |
| CLM-31 | SEM-048, rGO/Pr6O11 for CIP | **PROVISIONAL** | Abstract/conclusion give 88.0/88.3% removal; derived qe≈22mg/g is not source-reported, and q_m=85.5mg/g is fitted. Accessible pH-effect points list 2,4,8,10, so the stated pH6.6 condition/optimum is not reconciled to the visible test grid. |
| CLM-32 | SEM-049, Alg-Cu@GO@MOF-525 for TC | **PARTIAL** | pH7 removal96.6% and a separate 54.6% contact-time result within38min may be retained only as distinct sub-study claims. q_m=533.2mg/g is a fitted Sips value. Methods/table concentration units and dose/volume descriptions conflict; the reported low-dose qe≈700mg/g is not condition-pinned and must stay out of ranking. No reuse, real-water or cost result is verified. |
| CLM-33 | SEM-050, GO–TOPO:LevA membrane adsorber | **VERIFIED WITH RESTRICTED INTERPRETATION** | Full text and SI support membrane performance, six-cycle NaOH regeneration and active-layer material/carbon estimates. Municipal wastewater was 0.45µm prefiltered and deliberately spiked; it is not untreated native wastewater. USD2.5–6.8/m² is an active-layer material estimate, while 14–59kgCO2-eq/m² is an active-layer cradle-to-gate footprint. Neither is full-module cost or financial cost/m³. Quarantine the separate powder-batch qe=22.7mg/g because its denominator does not reconcile. |
| CLM-34 | SEM-051, citric-acid-crosslinked CMC/GO beads for TC | **PARTIAL** | The 94.93% time-test result at 200mg/L, 20mL, 20mg beads, pH4 and120min implies a derived qe≈189.86mg/g. The 267–278mg/g Langmuir qmax values are fitted; Hill fits better. The USD1.95/g estimate uses linear Langmuir qmax and an illustrative 1g/L TC scenario above the tested 50–250mg/L feed range. Desorption efficiency is not capacity retention; acid/base concentration differs between Methods and Results. |

## 5. Cross-study high-risk holds to preserve

These are not all failures of the manuscript. They are the source discrepancies the manuscript must not silently repair or turn into headline performance claims.

1. **SEM-010 (CLM-04):** 99% CIP removal on the stated 40mL basis implies about99mg/g, while Table4 experimental kinetic qe is78.82mg/g; the conclusion also says20g/L where other source locations say20mg/L. Keep on hold.
2. **SEM-016 (CLM-06):** SGO experimental qe and prose removal do not reconcile across concentration, temperature and dose series. Keep measured values and prose distinct; fitted q_m is a separate isotherm result.
3. **SEM-038 (CLM-07):** N-rGO TC qe is above the strict finite-feed ceiling at the stated 80mL feed basis; Figure2c shows a larger mismatch. Do not use its q_e or q_m in quantitative ranking pending author clarification.
4. **SEM-032 (CLM-05):** PGOT@GEL validation qe=807.54mg/g lacks solution volume in the main paper; the matrix is described inconsistently as real vs simulated real wastewater. It can remain a reported validation result only with that caveat.
5. **SEM-046 (CLM-29):** synthetic qe and real-effluent removal percentage are arithmetically inconsistent as detailed above.
6. **SEM-029 (CLM-15):** the source's bead-price/cost estimate assumes a dose100-fold below a key experimental condition. The new first-loading ratio is a transparent arithmetic check, not a substitute for a real TEA.
7. **SEM-045, SEM-049 and SEM-051 (CLM-28, 32, 34):** fitted capacities, source caption/table conflicts, or author cost scenarios must not be relabelled as experimentally observed uptake or validated process economics.

## 6. Mechanism audit

The manuscript's general mechanism narrative is appropriate when kept at the stated evidence strength:

- π–π association is chemically plausible for conjugated antibiotics and graphenic sp² domains, but computational energy or surrogate fluorescence evidence does not isolate its contribution in an aqueous adsorption experiment.
- Electrostatic effects depend on pH, ionic strength, surface charge and antibiotic speciation. A pH optimum or point-of-zero-charge value alone does not prove a unique electrostatic attraction mechanism. In particular, near-neutral CIP is not simply a single anionic species.
- FTIR/XPS changes can support altered surface-group environments but do not quantify the fraction of adsorption energy attributable to a given bond.
- Pseudo-second-order kinetics do not independently prove chemisorption; Langmuir fits do not prove a perfectly homogeneous monolayer; intraparticle-diffusion plots do not by themselves establish that pore diffusion is the sole rate-limiting step.
- Fe3O4 primarily provides magnetic response/recovery potential; it does not by itself demonstrate stronger intrinsic CIP/TC binding. Calcium–alginate crosslinking establishes network formation, not a proven antibiotic–calcium bridge.

The SEM-032 pH/surface-charge explanation remains graded M1: a relevant pH response is supported, but the paper's simplified CIP charge assignment around pH7 should not be repeated as established speciation or dominant attraction. The mechanism-evidence matrix remains authoritative for source-by-source grades.

## 7. Cost and feasibility audit

The manuscript's affordability conclusion is properly conservative. Three cost-related cases need distinct treatment:

- **SEM-029 GO/PVA/calcium-alginate beads:** the nominal USD10–30/kg bead price can be divided by an observed qe or fitted qmax to obtain a first-loading material-purchase ratio. This is a lower-bound screening calculation before regeneration, labour, transport, water, energy and waste handling. It is not a lifecycle cost and does not prove a lifetime-use cost because cumulative mass treated across reuse cycles is not adequately reconciled.
- **SEM-050 GO–TOPO:LevA membrane:** USD2.5–6.8/m² is an active-layer material estimate. The carbon footprint is an active-layer cradle-to-gate estimate and the per-volume footprint projection depends on assumed service life and throughput. These cannot be relabelled as a complete financial treatment cost or full-system LCA.
- **SEM-051 CMC/GO beads:** the author's USD1.95/g-TC estimate uses a linear Langmuir qmax even though Hill is the better isotherm fit, and the illustrative 1g/L wastewater scenario exceeds the maximum tested initial concentration. It is an author-reported laboratory estimate, not independently reproduced full-system TEA.

The final paper should continue to use *low-cost potential* as a question being assessed, not as a demonstrated conclusion.

## 8. Work completed in this audit pass

1. Updated four sections/claim passages in the unified manuscript:
   - added a transparent first-loading material-purchase ratio and its strict limitations for SEM-029;
   - added feed-ceiling and Methods/Figure caption conflicts for SEM-045;
   - added the unresolved pH6.6 provenance caveat for SEM-048;
   - clarified the tested-feed versus illustrative-cost scenario and absent real-water/flow validation for SEM-051.
2. Added claim records CLM-28 through CLM-34 for SEM-045–SEM-051 to the claim-evidence audit ledger.
3. Updated all seven SEM-045–SEM-051 rows in Supplementary Table S1 so the source limits agree with the main manuscript and claim ledger.
4. Left the active 49-reference selection unchanged. No screening, selection, Zotero merge or DOI-intake decisions were reopened.

## 9. Remaining work before submission

- Obtain full text and SI for SEM-047 and SEM-048 if possible; retrieve complete accessible tables/price basis for SEM-051. Until then, retain provisional/partial status.
- Reconcile or explicitly quarantine all HOLD claims listed above; do not silently fix source values.
- Complete any remaining sentence-level and table-row source-pin audit beyond the 34 current claim groups, especially older studies whose keys, errata, or publisher-access level are still unresolved in the ledger.
- Render the four editable Mermaid figure sources and check figure numbering, captions and in-text cross-references in a single Word/PDF manuscript.
- Recheck the 49 selected + 4 contextual bibliography in the university's required style; citation-key linkage is complete but style rendering is not.
- Complete language editing, author details, acknowledgements, funding/conflict/data availability statements and any university submission checklist.
- Do not describe the paper as a systematic review or PRISMA-compliant review unless the missing reproducible search and screening counts are reconstructed.

## 10. Source-of-truth project files

- Unified working manuscript V2: `manuscript/SEMESTER_MANUSCRIPT_WORKING_V1.md`
- Main-text condition-labelled Table 1: `manuscript/SEMESTER_TABLE_1_CORE_STUDY_COMPARISON_V1.md`
- 49-study Supplementary Table S1: `manuscript/SEMESTER_SUPPLEMENTARY_TABLE_S1_49_REFERENCE_COVERAGE.md`
- Detailed claim-evidence ledger: `data/semester-manuscript-claim-evidence-audit.csv`
- Mechanism evidence grades: `data/semester-mechanism-evidence-matrix.csv`
- Practical feasibility matrix: `data/semester-practical-feasibility-matrix.csv`
- Citation/bibliography linkage audit: `docs/FINAL_SEMESTER_MANUSCRIPT_V2_BIBLIOGRAPHY_AUDIT.md`

**Bottom line:** V2's main scientific position is sound as a cautious narrative synthesis. It is not yet submission-ready, and the flagged numerical holds must remain visible. The latest changes improve internal consistency and traceability without expanding or changing the selected 49-reference corpus.
