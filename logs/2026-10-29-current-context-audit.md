# Current repository context audit — 2026-10-29

## Purpose

This audit records the repository structure, live data state, governing scope decisions, cross-workstream boundaries and the next safe execution sequence. It supersedes older live-count summaries in the README, RESEARCH_WORKFLOW.md and the 24-day plan without erasing their dated historical checkpoints.

## Repository map and source-of-truth hierarchy

- `data/corpus-screening-register.csv`: canonical broad-review screening register.
- `data/corpus-evidence.csv`: canonical broad-review source-linked evidence table. This contains evidence findings from original papers and reviews and some rows still marked provisional/staged; row count is not a paper count.
- `data/source-caveats.csv`: caveats/contradictions for the broad corpus.
- `data/candidate-decision-audit.csv` and `data/screening-decision-adjudication-v1.csv`: provisional role/scope/quantitative-use/ranking signals; neither is a final acceptance list.
- `data/journal-quartile-audit.csv`: journal-level ranking evidence; ranking system/year/category and final candidate eligibility are separate.
- `data/primary-study-comparison-matrix.csv`: focused matrix for matched comparisons from a subset of the corpus, not all evidence rows.
- `references/bibtex_full_corpus_processing_queue_2026-10-29.csv`, `references/bibtex_candidate_key_crosswalk_2026-10-29.csv` and `references/BBT_EXPORT_AUDIT_2026-10-29.md`: bibliographic metadata, citation-key mapping and remaining processing tasks.
- `manuscript/REVIEW_OUTLINE.md`, `ORIGINAL_OUTLINE_AS_SUPPLIED.md`, `SECTION_2_1_RAW_BIOMASS_V1.md`, `SECTION_2_2_CLAYS_BIOPOLYMERS_V1.md`, `SECTION_2_3_BIOCHAR_V1.md`, `COMPARATIVE_TABLES_V1.md` and `CONTINUUM_SYNTHESIS_V1.md`: the broader review manuscript. They are working drafts, not submission-ready; retain their original processing–cost–performance framework.
- The separate semester paper is governed by `docs/SEMESTER_PAPER_SCOPE_PROPOSAL.md` and its own register/evidence/search/synthesis files. It must not overwrite the broad workstream.

## Live count state checked directly from current files

| Artifact | Current rows / entries | Interpretation |
|---|---:|---|
| Broad screening register | 111 | Unique candidate records; not accepted citations |
| Broad source-linked evidence CSV | 505 | Evidence findings; includes primary/review, provisional and staged rows |
| Journal quartile audit | 41 | Journal-level records; not final per-paper Q1 eligibility |
| Better BibTeX processing queue | 164 | Exported citation entries; audit reports 58 not yet in the screening register |
| Primary-study comparison matrix | 208 rows; 43 candidate IDs | Deliberately focused subset; not the whole 505-row evidence register |
| Semester candidate register | 44 | Candidate screening records across prior targeted searches and existing-source review; not accepted citations |
| Semester dedicated evidence CSV | 31 | Dedicated extraction rows; the broad evidence is cross-referenced rather than copied |

## Separate workstreams

### Broad review (source of truth remains unchanged)

The broad review's intended structure is based on the supplied outline and processing–cost–performance continuum spanning raw biomass, natural clays, unmodified biopolymers, standard biochar, modified biochar, doped/engineered biochar, activated carbon and nano-engineered carbons. Supervisor planning figures remain roughly 60 distinct works cited for one publication version and 150 for a publisher/journal version. Neither actual citation count is confirmed; do not infer it from candidates/evidence rows. The current queue shows 58 entries still not matched into the register; 11 candidates DISC-069–DISC-079 have recently been added and 16 online/indexed evidence rows are provisional pending primary-PDF/SI pinning. `DISC-022` remains deferred under the historical broad-review instruction; it is not screened or excluded.

The current primary-study matrix has 208 rows for 43 candidates; the 2026-10-28 consolidation crosswalk is staging-to-master mapping, with multiple rows per paper expected. Never count crosswalk rows as distinct studies.

### Semester paper (approved scope)

**Title:** *Assessing the Low-Cost Potential of Non-Conventional Engineered Adsorbents for Ciprofloxacin and Tetracycline Removal from Aqueous Media.*

Include selected GO/rGO and functionalized graphene adsorbents and selected graphene-bearing composites only when the target-specific adsorption contribution is extractable. Core targets are CIP and TC; related antibiotics are not pooled with them. Green/waste-derived is not the defining theme. Low-cost is a claim to assess, not assume. The initial plan calls for about 50 distinct cited works, subject to eligibility and evidence quality.

The current dedicated extraction CSV has 24 records. Two already extracted full-text papers in the Library are the 2025 SGO/CIP study (SEM-016/CORP-024) and the 2025 PGOT@GEL/CIP study (SEM-032/CORP-015). A third in-scope item already has main-corpus evidence: Zhang & Wu (2022), N-rGO with tetracycline among six antibiotics (SEM-038/CORP-031), linked to EV-B10-004–EV-B10-009. Those existing evidence rows were cross-referenced rather than duplicated.

`data/semester-main-corpus-crosswalk.csv` now has one row per 38 semester candidate. It records exact DOI/title matches to the broad register and Better BibTeX queue, reused evidence IDs, and unlinked candidates. It shows three broad-register overlaps and one queue-only title match (SEM-020 to the graphene/GAC CIP paper); 34 semester candidates have no exact DOI/title match in those two registries. This does not prove a paper is absent from the Library or ineligible; it flags a crosswalk/screening task only.

## Scientific and workflow safeguards

- Keep fitted Langmuir/Sips qmax separate from measured qe, model-fitted kinetic qe, qt, removal percentage and column/breakthrough metrics.
- Preserve source inconsistencies and mass-balance concerns. Do not silently pick the most flattering capacity or reinterpret unknown units.
- Keep synthetic water, fresh synthetic urine, spiked/treated real water, untreated real wastewater and column studies distinct.
- A pseudo-second-order fit alone does not prove chemisorption; distinguish measured evidence from author interpretation/model speculation.
- Separate adsorption from degradation/oxidation/membrane rejection unless an adsorption contribution is independently separable.
- Do not infer low cost from a waste precursor, large qmax or high removal percentage. If preparation and regeneration costs are not quantified, mark cost evidence “not reported” and discuss process burdens/uncertainty.
- Use Q1 only as a separately verified ranking signal; the semester scope does not impose Q1-only eligibility unless explicitly required. SJR and JCR are distinct systems and publication-year/category matters.
- Use Zotero for final citations. The Better BibTeX inventory is present but final style-rendered citations/bibliography remain pending; check the claim ledger after any Zotero duplicate merges.

## User action status

**No action is required from the user now.** The user explicitly said they are not downloading any more papers. Earlier register/log text asking for SEM-006 and SEM-037 PDFs is superseded; those records now say proceed with accessible indexed/abstract evidence and keep inaccessible numbers/cost assumptions unresolved. No new downloads/uploads are requested.

## Next execution sequence

1. Continue from this crosswalk and inspect existing Library files plus existing master evidence for remaining on-scope GO/rGO/composite studies (CIP/TC), adding no duplicate evidence rows.
2. Prioritize primary-source data validation and source-pin/cost-gap fixes over more broad candidate collection.
3. Make only condition-valid performance comparisons; quarantine N-rGO fitted capacities and other mass-balance-inconsistent values until reconciled.
4. Refresh the broad-review data crosswalk for 58 unregistered BibTeX records after the semester shortlist is made stable; do not conflate that broad task with the semester paper.
5. Keep the paper’s substantive tables and original figure set evidence-driven. Draft final claims only after each relevant table row can point to primary evidence and caveats.


## Follow-on source review — 29 October 2026

- Updated SEM-020 with verified publication metadata (Zhu et al., 2015, *Environmental Technology*, DOI 10.1080/09593330.2015.1054316) and added provisional abstract-level evidence EV-SEM-014; it remains out of final numerical ranking pending full-text condition verification.
- Added SEM-039/EV-SEM-015 for Yao et al. (2017), CNF/GO aerogel for TC; fitted q_m, model-fitted kinetic q_e, removal percentage and ten-cycle reuse are explicitly separated.
- Added SEM-040/EV-SEM-016 for Peng et al. (2016), graphene and TC in a seven-antibiotic mixed solution at 200 µg/L per antibiotic. The exact TC removal percentage was not inferred from the figure-based range. Biochar values remain outside the semester paper's core matrix.
- Semester register: 40 records; dedicated evidence CSV: 16 rows. The updated crosswalk points all three updated/new candidate records to the current Better BibTeX inventory without copying evidence into the broad master corpus. No user download/upload action is active.


## Fourth follow-on source wave — 29 October 2026

The semester candidate register now contains 44 records and the dedicated evidence table contains 24 rows. The latest four candidates are SEM-041 (GO/sodium alginate for CIP), SEM-042 (chitin/nGO with continuous flow and CIP-spiked real-water tests), SEM-043 (GO for CIP; SMX separate), and SEM-044 (MgO/chitosan/GO for CIP; NOR separate). Their evidence IDs are EV-SEM-020–EV-SEM-023. No broad-corpus rows were duplicated based on the current DOI cross-check. The new figures remain provisional: the GO–alginate numeric q_m is only secondarily cross-checked, the Chi:nGO indexed column mass is implausible, the GO/CIP abstract capacity lacks full condition verification, and the MgO/chitosan/GO capacity remains abstract-only.


## Fifth source-review follow-on — 29 October 2026

- Updated SEM-024 / EV-SEM-024 for Gao et al. (2012), GO adsorption of tetracycline. The primary PubMed abstract reports Langmuir q_max=313 mg/g (described as close to measured data), pseudo-second-order kinetics with k=0.065 g mg−1 h−1 and lower capacity with increasing pH or Na+. The full experimental conditions and primary tables are not accessible in the current Library view; this remains abstract-level.
- Re-audited SEM-001 / EV-SEM-001 against the open PLOS full text. The reported fitted q_max declines from 322.43 mg/g at 298 K to 101.87 mg/g at 303 K and 73.53 mg/g at 308 K. This large change is now flagged for a table/condition consistency check; the manuscript should not use it as an unqualified temperature trend.
- The semester evidence CSV now contains 27 records. The semester candidate register remains 44. No new user download/upload is requested.

  
## Fifth source-review follow-on — GO/TC and GO–LDH audit — 29 October 2026

- Semester candidate register: **44 unique records**. Dedicated semester evidence CSV: **24 unique records**. Crosswalk: **44 rows**. Integrity validation found no duplicate IDs and no evidence rows linked to a missing candidate.
- SEM-024 / EV-SEM-024 records primary PubMed abstract evidence for Gao et al. (2012), GO for tetracycline: Langmuir q_max=313 mg/g, pseudo-second-order k=0.065 g mg−1 h−1, and lower reported capacity with increasing pH or Na+ concentration. Full conditions and tables are not currently accessible.
- SEM-001 / EV-SEM-001 was checked against PLOS full text. The reported fitted Langmuir capacities are 322.43 mg/g at 298 K, 101.87 at 303 K and 73.53 at 308 K; the size of this change remains a source-consistency caveat.
- SEM-015 / EV-SEM-005 was checked against the full Frontiers article. Use 84.84% removal only for 1 mg/L CIP, 10 mg/L composite, pH 7 and 60 min. The paper's equation implies q_e≈84.84 mg/g, while the kinetic table gives model-fitted q_e≈106.96 mg/g; the capacity figures remain quarantined. Preparation involves modified-Hummers GO, metal salts, concentrated NaOH, 120°C/16 h hydrothermal processing, washing and drying. Reported removal falls from 80.4% in cycle 1 to 27% by cycle 5.
- The user has paused new downloads. No user action is required at this stage.


## CNF/GO publisher-text re-audit — 29 October 2026

The full publisher text for Yao et al. (2017; DOI 10.1038/srep45914) was checked at preparation, experiment, results and reuse sections. This updates SEM-039 / EV-SEM-015 with exact CNF/GO input masses, ultrasonication settings, freeze and freeze-drying conditions, condition-separated TC tests, explicit Fig. 7 removal (82.1%), q_e=84.8 mg/g, q_m source discrepancy (454.6 mg/g abstract/Results vs 454.5 mg/g conclusion), and 5 wt.% NaOH × 5 h regeneration followed by wash/freeze-dry across ten cycles. TC removal after ten cycles is 78.9%. No process-cost inventory is reported. The cross-study table will label the exact Fig. 7 feed concentration as unspecified rather than assigning the general range or factor-test C0 to that point.


## Schema validation and duplicate DOI resolution — 29 October 2026

Current integrity checks: 44 candidate-register rows; **43 unique DOI-defined works**; 24 unique evidence IDs; 44 crosswalk rows. No duplicate candidate IDs, duplicate evidence IDs, missing evidence-to-candidate links, or crosswalk orphan/extra IDs were found. One duplicate DOI pair (SEM-026/SEM-041; 10.1016/j.jcis.2016.08.068) was resolved without deleting trace history: SEM-026 is canonical, EV-SEM-020 now links to SEM-026, SEM-041 is a duplicate alias and excluded from distinct-work counts. Two evidence rows (EV-SEM-010 and EV-SEM-013) had column-shift/misalignment anomalies; mechanism/reuse/cost/source/URL/status/caveats were remapped to the intended columns and the previously blank caveat cells were filled. Current evidence readiness remains mixed: abstract-level figures and unresolved capacity-definition issues are not eligible for an unqualified performance ranking.


## SEM-042 accepted-manuscript source audit — 29 October 2026

Primary text source: [CONICET-hosted accepted manuscript](https://ri.conicet.gov.ar/bitstream/11336/87000/11/CONICET_Digital_Nro.b2e52671-05bf-40a5-9fe0-525a5cfb6f21_J.pdf), DOI 10.1016/j.carbpol.2018.02.021. The candidate and EV-SEM-021 were updated with preparation, batch and dynamic details. Key batch finding: best overall fit Sips; Langmuir qₘ=73±3 mg/g for Chi:nGO 3:1 versus 282±11 mg/g pure nGO. Dynamic tables list Thomas q₀ and Yoon–Nelson τ, including spiked water results for Buenos Aires, Chascomús and Macachín, but the source literally states 100 g is in a 1-cm-ID, 1.5-cm-bed column. The 1.178-cm³ geometric volume implies ~84.9 g/cm³, physically impossible. No correction was guessed: dynamic values remain quarantined. Source claims “low-cost,” but quantified process-cost evidence is absent. PDF screenshot rendering failed (cache miss), so text/table values were accessed but table appearance not visually checked.


## Follow-on full-text extractions — 29 October 2026

The latest three source-based extracts are:
- **EV-SEM-025 / SEM-027** (Choi & Choi 2022, GO/Ca-alginate–PAM for CIP): fitted Langmuir qₘ 6.846 mg/g; no explicit measured qe/removal or multicycle reuse was identified. Methods state 55 mL in a 50 mL tube.
- **EV-SEM-026 / SEM-029** (Hossain et al. 2026, GO/PVA/calcium-alginate beads for CIP): observed qe maximum 7.15 mg/g; fitted linear/nonlinear Langmuir qₘ 8.210/10.14 mg/g; modelled PSO qe 4.458 mg/g. Source reports conflicting D–R fits, negative linear PFO k₁, 50 mL/55 mL method inconsistency and a 100× discrepancy between dose basis in the cost calculation (0.1 g/L) and experimental optimum (0.5 g/50 mL = 10 g/L). The claimed < $1/kg CIP removed should be called an author estimate, not validated lifecycle cost.
- **EV-SEM-027 / SEM-034** (Hossain et al. 2024, GO/Co–Fe for TC): TC removal 94.1% in abstract/body but 93.94% elsewhere at C₀=.2 mg/L, dose=.15 g/L, pH 7, 30 s, 25°C; fitted Langmuir qₘ=64.10 mg/g at 50°C. Four tetracycline species stay separate, and the paper has no real-water/cost inventory.

Current direct count: 44 candidate-register rows, 43 DOI-defined works (SEM-041 remains duplicate alias), 27 unique evidence IDs, 44 crosswalk rows. No download/upload action is required. The next high-value review focus is primary data validation of SEM-005, SEM-026, SEM-043 and SEM-044, as well as the no-evidence candidates whose target and material identity can be confirmed from already accessible primary pages.


## Follow-on source checks — SEM-019 and SEM-028 (29 October 2026)

- SEM-019 / EV-SEM-028: the 2026 EDTA-mGO/TC paper reports 93.23% removal under the stated low-concentration optimum. Mass balance implies qₑ≈1.865 mg/g; its PSO fit reports qₑ=0.01937 mg/g at R²=1. This roughly 96× contradiction is preserved and prevents treating the fit as validated uptake. Freundlich fits better than Langmuir at 25°C; eight-cycle removal falls from ~94% to 90.50%; no quantified cost.
- SEM-028 / EV-SEM-029: 2013 GO/calcium-alginate fibers. Accessible primary abstract/snippets report 78.9% removal at 2 g/L and 6 wt% GO; capacity rises from 18.45 to 39.06 mg/g with GO loading from 0% to 6% at equilibrium C=60 mg/L. No numeric fitted parameters, full recipe, reuse or cost was accessible.
- Semester count now 44 register rows / 43 DOI-defined studies, 29 unique dedicated evidence rows, 44 crosswalk identifiers. Download/upload pause unchanged; no user action requested.


## Additional primary-publisher checks — SEM-014 / SEM-030 (29 October 2026)

- SEM-014 / EV-SEM-030: magnetic GO·Fe₃O₄ for TC; abstract says C₀=1000 mg/L, 50 mg material, pH 7 and 293 K, headline maximum capacity 531.93 mg/g. Solution volume and measured/fitted definition are missing from accessible preview; DFT outputs (−3.86 eV binding energy; 14.99 μB spin polarization; 0.22 eV HOMO–LUMO gap) are computational, not adsorption-capacity metrics. No cycle-level reuse/cost details.
- SEM-030 / EV-SEM-031: GO–[Ni(DMG)]ₙ for CIP; one-pot GO/ethanol + Ni(II) + DMG, 24 h at room temperature; Langmuir-comparison capacity 117–159 mg/g, pH 2–7 removal trend, PSO k=0.0005–0.0009 g/(mg·min). Freundlich/Temkin are reported as better isotherm fits. Exact feed/dose/formulation-specific metrics, reuse, matrix and cost are unavailable in the abstract.
- Current counts: 44 candidate-register rows, 43 DOI-defined works, 31 unique semester evidence rows, 44 crosswalk rows. These counts are inventory, not final included/cited works.
