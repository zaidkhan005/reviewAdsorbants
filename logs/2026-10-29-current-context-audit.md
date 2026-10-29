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

## Follow-on evidence wave — 29 October 2026

Latest dedicated semester evidence count is 37 unique rows; candidate register remains 44 rows, with SEM-041 an alias of SEM-026 and SEM-021 missing verified DOI metadata. The crosswalk has 44 rows.

New records:
- EV-SEM-034 / SEM-008: MGO for TC-HCl/OTC/CTC; primary abstract only, capacity metric held because the numeric TC-HCl value comes from a secondary review.
- EV-SEM-035 / SEM-013: DFT-only; mechanism context, not measured adsorption performance.
- EV-SEM-036 / SEM-031: SGO in binary/ternary/quaternary fluoroquinolone mixtures; mixture-level q_m and DMF/1 M HCl regeneration.
- EV-SEM-037 / SEM-033: rotating-field Fe3O4/rGO for TCH; high removal but no electrical energy or field-free comparator.

No new user files are needed. Next highest-value task is metric/provenance QA across the 37 evidence rows, followed by the included-study shortlist and citation-key reconciliation.

## Citation-key linkage status — 29 October 2026

The three available BibTeX exports were checked against the semester candidate register. Six distinct works have exact DOI/key matches: SEM-016, SEM-020, SEM-032, SEM-038, SEM-039 and SEM-040. SEM-016/032/038 keys appear across all three exports; SEM-020/039/040 appear only in `full ++.bib`. No additional exact candidate title matches were found in the target-term title scan. Other candidates are not yet citation-ready from these files, but may exist in Zotero or another export; do not infer absence from one export alone. SEM-041 remains a duplicate alias of SEM-026.

## Narrative drafting checkpoint — 29 October 2026

Created `manuscript/SEMESTER_RESULTS_AND_DISCUSSION_V1.md` (six subsections; 14k+ characters). It uses six keys verified by exact DOI matches across the available BibTeX exports and explicitly flags nine unresolved citation-key positions. Candidate register remains 44 rows, dedicated evidence CSV 37 rows, condition-labelled comparison 18 rows, shortlist 44 rows, readiness audit 37 rows, and citation linkage audit 44 rows. No user download/upload is required. The next best step is to resolve citation links for selected, evidence-ready studies and then draft methods/search and introduction—not add more candidates.


## Latest live-state reconciliation — 29 October 2026 (supersedes earlier counts in this log)

The repo was re-fetched and count-checked for the next execution step. Use these as current live values; earlier counts of 24, 27, 29 or 31 dedicated evidence rows below describe earlier same-day checkpoints and are not current.

- **Candidate register:** 44 rows. SEM-041 is a duplicate alias of SEM-026 (DOI 10.1016/j.jcis.2016.08.068), leaving **43 distinct candidate studies**. SEM-021 still has the placeholder “DOI to verify”; the other 42 distinct records have valid DOI strings. Do not call all 43 “DOI-defined” until SEM-021's DOI is verified.
- **Dedicated evidence CSV:** 37 rows with 37 unique evidence IDs (EV-SEM-001–EV-SEM-037). Every evidence row points to a candidate in the register; no duplicate evidence IDs or orphan candidate links were found in the current validation.
- **Readiness audit:** 37 rows; matches the evidence CSV count.
- **Condition-labelled comparison:** 18 selected rows; not a comprehensive view of all evidence.
- **Inclusion shortlist:** 44 rows, covering the 44 register entries; SEM-041 remains excluded from distinct-work/citation counts.
- **Main-corpus crosswalk:** 44 rows. SEM-038 uses existing broad-corpus evidence EV-B10-004–EV-B10-009 instead of duplicating it in the semester evidence CSV.
- **Citation-key linkage audit:** 44 rows. Six candidates currently have exact DOI-to-Better BibTeX key matches in the inspected exports; the results-and-discussion draft contains nine explicit citation-key-pending markers. The remaining keys must be checked against the actual available exports/Zotero, never guessed.
- **Working Results & Discussion:** `manuscript/SEMESTER_RESULTS_AND_DISCUSSION_V1.md` exists (six subsections). It is a source-cautious draft, not submission-ready; claims still need resolved citation keys and final source-pin review.
- **Next step:** citation-key reconciliation for the selected evidence-ready studies and the nine pending markers, then draft Methods/Search and Introduction around the stable included-study set. Do not add more candidates before this pass is complete unless a real citation/evidence gap is identified.
- **User action:** none. The user's pause on further downloads/uploads remains active.


## Citation-key reconciliation follow-up — Library search and export inventory check (29 October 2026)

This follow-up completes the next bounded check after the initial nine-marker reconciliation. It does not overwrite the existing manuscript draft or infer new keys.

- Re-read the three existing Library Better BibTeX exports: `full ++.bib` (164 entries), `Antibiotic Adsorption Review new — Full Corpus.bib` (61 entries), and `Antibiotic Adsorption Review — Full Corpus.bib` (31 entries).
- Re-ran programmatic DOI and exact-title searches across all three raw exports. The nine pending candidate records (SEM-004, SEM-010, SEM-017, SEM-018, SEM-029, SEM-031, SEM-033, SEM-034, and SEM-037) have no DOI or exact-title match in those export files. A nearest-title check did not identify a plausible alternate keyed record.
- Checked the existing Library search surface using the target DOIs and titles. Some search hits are other papers whose reference lists cite a target article; that is not evidence that the cited article has a Zotero item or a Better BibTeX key in the current exports.
- No connected Zotero or Better BibTeX tool is exposed in this session, so a fresh live export cannot be generated from the underlying Zotero collection here. This means the result is **unresolved in the available exports**, not proof the items are absent from the user's Zotero library.
- Updated `data/semester-bibtex-citation-linkage-audit.csv` for the nine pending rows to distinguish the live-library access limitation and state the exact missing input: an existing Zotero item's generated key or a fresh Better BibTeX export of the user's existing collection. No additional paper PDF is required.
- Preserved the six previously verified keys and left all nine manuscript markers unchanged. `manuscript/SEMESTER_RESULTS_AND_DISCUSSION_V1.md` was not edited. No screening decisions, evidence records, study counts, or scientific claims were changed.

**Gate:** do not invent citation keys. When a key-bearing export of the existing Zotero items becomes available, reconcile only these nine DOI-to-key mappings first; otherwise keep them explicitly pending. Do not broaden the literature search or start a manuscript rewrite in this step.


## Extended citation-key coverage check — repository queues and full Library inventory (29 October 2026)

A second coverage pass checked whether any of the nine unresolved semester citations were present indirectly in repository-generated inventories or in a differently titled/versioned bibliography record. This was a metadata/key linkage check only; it did not change study eligibility or evidence interpretation.

- Reconfirmed the three actual Library BibTeX exports: `full ++.bib` (164 parsed entries), `Antibiotic Adsorption Review new — Full Corpus.bib` (61 entries), and `Antibiotic Adsorption Review — Full Corpus.bib` (31 entries). A recursive Library listing filtered for BibTeX files returned these three exports only.
- Rechecked the corresponding 164-row `bibtex_reference_inventory_audit.csv` inventories and the Library-held candidate/key crosswalk snapshot. No target DOI or candidate-ID record appeared there.
- Rechecked repository `references/bibtex_full_corpus_processing_queue_2026-10-29.csv` (164 entries) and `references/bibtex_candidate_key_crosswalk_2026-10-29.csv` (111 candidates): **zero exact DOI matches** for SEM-004, SEM-010, SEM-017, SEM-018, SEM-029, SEM-031, SEM-033, SEM-034, and SEM-037.
- Rechecked `data/semester-main-corpus-crosswalk.csv` (44 semester candidates). All nine target rows are present, retain their evidence IDs, and explicitly state that there is no exact DOI/title match in the current main register or Better BibTeX queue.
- Programmatic normalized-title similarity checks against the 256 export-entry instances did not identify a defensible alternate item. The nearest title was still a different article; similarity is not evidence for assigning its key.
- The previous six exact DOI-to-key links remain the only verified key mappings for this draft. The manuscript `manuscript/SEMESTER_RESULTS_AND_DISCUSSION_V1.md` remains unchanged, with the nine placeholders intact.

**Disposition:** The unresolved state is now corroborated across the Library exports, the export-derived inventory audit, the repository processing queue and candidate/key crosswalk, and the semester-specific main-corpus crosswalk. This still does **not** prove the items are absent from Zotero itself; direct Zotero/Better BibTeX access is unavailable here. To resolve these nine mappings without guessing, the needed evidence is the actual generated key for each existing Zotero item or a fresh Better BibTeX export of those existing items. No additional article PDF or repeat upload of the already inspected exports is needed.


## DOI-based citation-linkage resolution — manuscript-local bibliography added (29 October 2026)

The nine previously pending citation positions are now linked to DOI-checked bibliographic records. This resolves the manuscript's local citation/bibliography linkage without claiming that the nine new keys were generated by the user's live Zotero/Better BibTeX instance.

### Files changed

- Added `references/semester-manuscript-cited-references.bib` with **15 unique article entries**: the six key-bearing entries preserved from the provided `full ++.bib` export, plus nine DOI-matched records for previously unlinked semester candidates.
- Updated `manuscript/SEMESTER_RESULTS_AND_DISCUSSION_V1.md`: replaced each temporary citation placeholder with a matching `\\cite{...}` command and retained the corresponding evidence IDs as draft provenance. The underlying scientific claim text and values were not rewritten in this citation pass.
- Updated `data/semester-bibtex-citation-linkage-audit.csv`: added the `Project-local manuscript citation key` column. The nine rows retain blank `Verified Better BibTeX key` values because those exact new keys are project-local, not keys retrieved from the live Zotero database. The 44-row candidate audit is retained.

### Project-local citation keys and metadata sources

| Candidate | Project-local key | DOI / metadata source |
|---|---|---|
| SEM-004 | `sem004Zhu2018GOAlginateFiber` | [10.1039/C7RA11964J — RSC Publishing](https://pubs.rsc.org/en/content/articlelanding/2018/ra/c7ra11964j) |
| SEM-010 | `sem010Yasmin2024ZnCGrapheneOxide` | [10.1016/j.heliyon.2024.e33317 — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2405844024093484) |
| SEM-017 | `sem017Dang2025MagneticGOFibrillatedCellulose` | [10.1039/D5RA00877H — RSC Publishing](https://pubs.rsc.org/en/content/articlehtml/2025/ra/d5ra00877h) |
| SEM-018 | `sem018Dipannita2025CMCFunctionalizedMGO` | [10.1039/D5RA06621B — RSC Publishing](https://pubs.rsc.org/en/content/articlelanding/2025/ra/d5ra06621b) |
| SEM-029 | `sem029Hossain2026GOPVACA` | [10.1039/D6RA00494F — RSC Publishing](https://pubs.rsc.org/en/content/articlehtml/2026/ra/d6ra00494f) |
| SEM-031 | `sem031Shaha2026SulfonatedGrapheneOxide` | [10.1016/j.rineng.2026.110064 — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2590123026011011) |
| SEM-033 | `sem033Ding2026RotatingFieldFe3O4rGO` | [10.1016/j.seppur.2025.136049 — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1383586625046465) |
| SEM-034 | `sem034Hossain2024GOCoFeTetracyclines` | [10.1039/D3RA07597D — RSC Publishing](https://pubs.rsc.org/en/content/articlelanding/2024/ra/d3ra07597d) |
| SEM-037 | `sem037Zhao2018AlginateGOBarrier` | [10.1016/j.chemosphere.2018.02.157 — PubMed indexed record](https://pubmed.ncbi.nlm.nih.gov/29510369/) |

### Integrity checks

- The local bibliography has 15 entries and 15 distinct citation keys.
- All citation keys used in the Results & Discussion draft have a matching entry in `references/semester-manuscript-cited-references.bib`.
- No `CITATION KEY PENDING` marker remains in the manuscript.
- The six existing Better BibTeX keys remain unchanged.
- The audit still leaves the `Verified Better BibTeX key` field blank for the nine newly created records. When synchronizing with Zotero, import/verify those DOI records and use the keys from a subsequent actual Better BibTeX export if the generated keys differ. Until then, the repository-local bibliography is the source of truth for the manuscript's 15 cited works.

**Scope boundary:** This work resolves key-to-entry linkage for the current draft. It is not the final journal-style bibliography rendering, a full manuscript scientific audit, a quartile audit, or a fresh export from live Zotero.


## Publisher metadata verification follow-up — manuscript-local bibliography (29 October 2026)

After replacing the nine citation placeholders, the nine new bibliography records were cross-checked against publisher or indexed publication records for title, DOI, authors, publication year, and available volume/issue/page metadata. Publisher/indexed records consulted include:

- SEM-004, DOI 10.1039/C7RA11964J: RSC Publishing and PubMed verify title, authors Haotian Zhu, Tao Chen, Jingquan Liu and Da Li, volume 8, issue 5, pages 2616–2621 (2018).
- SEM-010, DOI 10.1016/j.heliyon.2024.e33317: ScienceDirect and PubMed verify title, five authors, Heliyon 10(12), article e33317 (2024).
- SEM-017, DOI 10.1039/D5RA00877H: RSC Publishing and PubMed verify the title, eleven authors, RSC Advances 15(27), pages 22138–22153 (2025).
- SEM-018, DOI 10.1039/D5RA06621B: RSC Publishing and PubMed verify the title, six authors, RSC Advances 15(42), pages 35219–35232 (2025).
- SEM-029, DOI 10.1039/D6RA00494F: RSC Publishing and PubMed verify the title, three authors, RSC Advances 16(17), pages 15225–15241 (2026).
- SEM-031, DOI 10.1016/j.rineng.2026.110064: the publisher-indexed ScienceDirect record verifies title, journal, volume 30, month June 2026, and article number 110064; the indexed article copy lists the four authors used in the BibTeX entry.
- SEM-033, DOI 10.1016/j.seppur.2025.136049: ScienceDirect verifies title, authors, Separation and Purification Technology volume 382, and article number 136049 (published 26 February 2026).
- SEM-034, DOI 10.1039/D3RA07597D: RSC Publishing verifies title, five authors, RSC Advances 14(2), pages 1431–1444 (2024).
- SEM-037, DOI 10.1016/j.chemosphere.2018.02.157: PubMed verifies title, five authors, Chemosphere volume 200, pages 612–620 (2018).

The issue numbers for SEM-017, SEM-018, and SEM-029 are now included in the local BibTeX file. The other six bibliography entries retain the exported metadata and keys as captured from the supplied BibTeX files. DOI links and publication metadata are not substitutes for the source evidence: the Results & Discussion claim-to-evidence audit remains the next step.

**Post-update integrity gate:** re-fetch the bibliography, manuscript and citation audit after each file update. Require every cited key to match one bibliography entry, no pending placeholders, 15 distinct entries/DOIs, and separate identification of project-local versus exported Better BibTeX keys.


## Claim-by-claim audit of semester Results & Discussion (29 October 2026)

Completed a claim-group audit against the existing semester condition-labelled comparison and evidence-readiness tables, plus the broad-corpus evidence records for N-rGO. The machine-readable output is `data/semester-results-discussion-claim-evidence-audit.csv` (18 audited claim groups); the narrative log is `evidence/2026-10-29-semester-results-discussion-claim-audit.md`.

### Main findings and edits
- The manuscript's condition-specific values for EV-SEM-002, 004, 006, 007, 011, 012, 013, 014, 015, 016, 026, 027, 036 and 037 align with the values currently transcribed into the repository's comparison/readiness records. This is an internal evidence-table cross-check; it is not a new full page-by-page extraction of each primary source.
- **Superseded correction (29 October 2026, later source-pin audit):** an earlier note incorrectly applied the 100 µmol/L kinetic-series ceiling (~500 µmol/g) to the fitted Langmuir parameter. Figure 10's separate isotherm range is 50–1000 µmol/L (printed p. 40824), so that ceiling objection is invalid and has been removed from the manuscript and current audit/caveat tables. The real qe/removal discrepancy (237.12 μmol/g / ~94.85% by mass balance versus text-reported 96.53%) remains.
- Added that the GO/calcium-alginate fiber's separate 56.8% pH-test maximum used 50 mg/L TC.
- Clarified the PRB paper's abstract-level 100 mg/g statement as a reported maximum capacity at pH 7 whose exact capacity definition is unclear given the abstract's Freundlich fit.
- Added the 50 mL/55 mL method-volume inconsistency to the GO/PVA/calcium-alginate cost caveat alongside the already documented 100-fold dose-basis discrepancy.
- Corrected §3.6's stale citation-readiness wording and removed references to three other screened-study issues from the prose checklist because those studies are not actually discussed/cited in the current Results & Discussion text. Those issues remain in the broader evidence register.

### Remaining scientific gates
- Exact page/table/figure pins remain incomplete in multiple semester evidence-readiness rows; abstract-only items include EV-SEM-014 (graphene/GAC benchmark), EV-SEM-036 (multicomponent SGO), EV-SEM-037 (rotating-field adsorbent) and EV-SEM-011 (permeable-reactive-barrier study).
- Exact TC-specific removal in the seven-antibiotic graphene study remains unextracted from a figure; the relevant manuscript paragraph does not guess it.
- The 15-key manuscript-local bibliography is internally consistent; nine project-local keys still need synchronization/verification against live Zotero/Better BibTeX before final citation-style rendering.

**Current disposition:** Internal citation linkage and draft-level claim consistency are improved. The work is still not submission-ready because source pinpoint verification, unresolved data arithmetic/conditions and final citation-manager synchronization remain. Do not start another bulk PDF upload or broaden candidate screening for this task.


## Follow-up source-pin verification for high-impact numeric claims — 29 October 2026

The three priority claims were checked against the full source PDFs already in the Library. Their relevant table/figure pages were visually inspected; the source of truth remains the primary PDF plus the evidence data files.

### SGO/CIP: correct the earlier, inapplicable loading-ceiling warning
- **Methods and equations:** printed p. 40819; the article defines (q_e=V(C_0-C_e)/m) and removal ((C_0-C_e)/C_0 × 100%), and specifies the 50 mL solution/10 mg SGO setup.
- **Table 1 and Fig. 7:** printed p. 40822. Table 1 gives (q_{e(exp)}=237.12 μmol/g) for the 50 μmol/L kinetic/concentration condition at 25 °C. The prose reports 96.53% removal for the same nominal 25 °C condition.
- **Fig. 10:** printed p. 40824, explicitly labels the isotherm concentration range as 50–1000 μmol/L at SGO 0.2 g/L and pH 4.
- **Table 2:** printed p. 40825, reports fitted Langmuir (q_m=1000 μmol/g) at 25, 30, 35 and 40 °C (R²=0.9998).

**Correction:** the previous audit inferred a 500 μmol/g feed-mass ceiling from the separate 10–100 μmol/L kinetic series and applied it to the isotherm fit. That was not a valid cross-series inference. The isotherm series reaches 1000 μmol/L, so the earlier ceiling statement is removed from the manuscript, claim audit, narrative audit and source-caveat register. Keep (q_m=1000 μmol/g) as a fitted parameter, not as an observed uptake. The genuine discrepancy remains: (q_e=237.12 μmol/g), C0=50 μmol/L and dose 0.2 g/L imply about 94.85% removal by the paper's own mass-balance equation, while the text reports 96.53%. The reuse section also reports 239.39 μmol/g as the direct/initial uptake at the 50 μmol/L condition, versus 237.12 in Table 1; both values are preserved as a separate minor source discrepancy.

### N-rGO/trace antibiotics: distinguish a conditional qe bound from fitted q_m
- **Methods §2.3:** printed p. 1300; the article describes 80 mL of antibiotic solution combined with 20 mL N-rGO dispersion at 0.5 mg/L, and states concentration/dose ranges.
- **Fig. 2a and Table 1:** printed p. 1302; nominal C0=10 μg/L and observed (q_e) values 80.58–90.21 mg/g.
- **Fig. 2b and Table 2:** printed pp. 1302–1303; Table 2 includes fitted Langmuir (q_m=662.25) mg/g for TC and 1265.82 mg/g for clindamycin.

The volume/C0 basis is not clarified: if 10 μg/L refers to the original 80 mL before N-rGO dispersion is added, the mass-balance ceiling is about 80 mg/g; if it refers to the final 100 mL mixture, it is about 100 mg/g. Accordingly, the top observed (q_e) values are not categorically labelled impossible. The much larger (q_m) values remain model-fitted values with a major trace-concentration/dose-basis concern and stay excluded from quantitative cross-study ranking until the isotherm concentration, dose, volume and fit inputs are reconciled. `data/corpus-evidence.csv` and `data/source-caveats.csv` now reflect this conditional interpretation.

### PGOT@GEL/CIP: source pin located, volume still unavailable
- **Methods §2.6:** printed p. 3, says full adsorption-test detail is in Supporting Materials.
- **Langmuir discussion:** printed p. 8, reports (q_{max}=821.24) mg/g.
- **RSM §3.3.6:** printed p. 9, reports predicted (q_e=800.60) mg/g and validation (q_e=807.54) mg/g at C0=296.52 mg/L, pH 6.70, dose 5.08 mg and 298.88 K.
- **Figure 12 and caption:** printed pp. 10–11; the caption identifies the application matrix as simulated real wastewater, which should not be rewritten as native real wastewater without clarification.

At the reported validation (q_e) and adsorbent mass, approximately 4.1023 mg CIP is adsorbed; at C0=296.52 mg/L, an initial solution volume of at least approximately 13.84 mL is required for the simple feed-mass balance to be feasible. The main article does not state the volume. The available project files and the retrieved publisher page did not expose the cited Supporting Materials file, so the volume check remains incomplete and the (q_e) is not declared wrong.

### Repository updates completed
- Revised the Results & Discussion manuscript to correct the SGO caveat and add source-page pins and an N-rGO conditional mass-balance caveat.
- Updated `data/semester-evidence-readiness-audit.csv` for EV-SEM-012 and EV-SEM-013 with page/table/figure pins and next QA actions.
- Updated `data/corpus-evidence.csv` for EV-B10-005/006 (N-rGO) and EV-B14-012 (SGO) to correct concentration-range interpretations and record exact source pins.
- Updated `data/source-caveats.csv` for the SGO and N-rGO entries.
- Updated `data/semester-results-discussion-claim-evidence-audit.csv` and `evidence/2026-10-29-semester-results-discussion-claim-audit.md` to reflect the corrected findings.

**Outstanding:** PGOT@GEL still requires the Supporting Materials for an independent volume/mass-balance check. No new PDFs were requested or uploaded; the audit used existing Library copies and publisher text.


### Final synchronization after source-page verification (29 October 2026)

The corrected source-range interpretation was also propagated to the rest of the project tables so later synthesis does not resurrect the superseded claim.

- Updated `data/semester-condition-labelled-comparison.csv` for EV-SEM-012 to state the separate 10–100 μmol/L kinetic/concentration range and the 50–1000 μmol/L isotherm range explicitly.
- Updated `data/primary-study-comparison-matrix.csv` for CORP-024 (SGO) and CORP-031 (N-rGO), preserving source-page pins and conditional interpretation. The SGO mechanism entry is now in the mechanism column rather than the cost column; its cost field correctly states that comparable cost/LCA data are absent.
- Updated the broad-corpus EV-B14-015 caveat to avoid describing (q_m) as invalid merely because the independent kinetic series ended at 100 μmol/L. It remains a fitted parameter, not an observed uptake; the real qe/removal and Table 1/reuse discrepancies remain.
- Rechecked the current manuscript, its 15-entry local bibliography, the 18-row claim audit, the 37-row semester readiness audit, the 505-row broad evidence register, the 64-row source-caveat register and both comparison matrices. The manuscript has 15 unique cited keys, every key has a bibliography entry, and no citation-key placeholder remains.

The only unresolved primary-source check among the three priority claim groups is the PGOT@GEL validation solution volume, which is referred to in the article's Supporting Materials but absent from the available main PDF. No extra PDF was requested or uploaded.


## Follow-up source-pin audit — SEM-031 / EV-SEM-036 (29 October 2026)

The public author-uploaded full text of Shaha et al. (2026), Results in Engineering 30, article 110064, DOI 10.1016/j.rineng.2026.110064, was retrieved from the ResearchGate article page and checked. This closes an abstract-only source-pin gap, but reveals a material applicability conflict.

- §2.4 (printed p. 3) states the batch methods and mixed-solution ranges. The isotherm set used SGO 0.2 g/L, pH 5, and a reported mixed-solution range of 18.24–371.64 mg/L; Fig. 3 p. 5, Fig. 4 p. 6, and Fig. 6 p. 9 provide condition-labelled results.
- Table 3 (printed p. 10) reports fitted Langmuir q_m values at 25 °C of 370.37, 357.14, and 333.33 mg/g for binary, ternary, and quaternary mixed systems. These are mixture-system fitted results, not isolated-CIP capacities.
- Fig. 12 (printed p. 13) and the text report >97% desorption using 1 mol/L HCl in DMF and >92% of initial performance retained after five cycles; solvent/acid recovery, spent-liquid handling, and a normalized cost inventory are not reported in the extracted evidence.
- **Important source contradiction:** while the abstract says the material is effective for treating real wastewater, §3.12 (printed p. 14) explicitly acknowledges that real-wastewater samples were not tested. Ionic-strength effects and continuous-flow/long-term stability are also not examined. This claim is corrected in the manuscript and audits; do not repeat the abstract wording as observed validation.
- Updated the semester evidence-readiness table (EV-SEM-036), condition-labelled comparison (EV-SEM-036), claim audit (RD-014), SEM-031 main-corpus crosswalk, manuscript §3.4, and narrative claim-audit report.

Primary-source link: https://doi.org/10.1016/j.rineng.2026.110064
Public full-text article record: https://www.researchgate.net/publication/402064345_Kinetic_Isotherm_and_Thermodynamic_Analysis_of_the_Simultaneous_Adsorption_of_Ciprofloxacin_Moxifloxacin_Levofloxacin_and_Sparfloxacin_onto_Sulfonated_Graphene_Oxide_in_Binary_Ternary_and_Quaternary_A



## Follow-up source check — SEM-033 / EV-SEM-037 (29 October 2026)

The rotating-field Fe3O4/rGO study was rechecked using the official ScienceDirect abstract and selected indexed article-preview content. ResearchGate indicates no full-text access, and the inspected Library search did not reveal its PDF/supplement.

- Abstract-level conditions: 30 mg/L pollutant, 1.0 g/L dose, 2 A excitation current; optimum pH 5 for TCH and pH 7 for OFL; material surface area 95.12 m²/g; >96% removal for both antibiotics; >87% efficiency after four cycles.
- The publisher preview includes a qualitative RMF-present vs absent comparison for three material variants and says all variants adsorbed more under RMF, with CP-Fe3O4/rGO best. The prior note claiming the field-free comparator was unavailable is corrected. Quantitative effect sizes are still not extracted.
- Full matrix composition, field frequency/strength, voltage/power, energy per volume, numerical q_max/q_e, detailed cycle protocol and full article/SI tables remain unavailable. Keep the material as provisional configuration evidence and do not infer energy efficiency or low-cost superiority.
- Updated manuscript §3.3; EV-SEM-037 in the readiness and condition-labelled tables; RD-013 in the claim-audit; SEM-033 in the crosswalk; and the narrative audit report.

Primary publisher source: https://www.sciencedirect.com/science/article/pii/S1383586625046465
ResearchGate accessibility record: https://www.researchgate.net/publication/397666081_Rotating_magnetic_field-enhanced_adsorption_of_tetracycline_hydrochloride_and_ofloxacin_using_Fe3O4reduced_graphene_oxide_composites



## Follow-up abstract cross-check — SEM-020 / EV-SEM-014 (29 October 2026)

The graphene-vs-GAC ciprofloxacin benchmark was rechecked against the official Taylor & Francis publisher abstract and PubMed (PMID 26050736). Both abstracts support the claims that graphene reached equilibrium within ~3 minutes and had a reported Langmuir-fitted q_max of 323 mg/g; they also describe less adverse effects than GAC from ionic strength 0.01–0.5 mol/L, NOM 5 mg/L and river/drinking-water sources. The reported value is still abstract-only because feed concentration, dose, temperature, exact pH/range, isotherm concentration range and numerical effect sizes remain unavailable. The publisher lists supplemental data, but the full article/SI could not be retrieved in this pass or located by Library search; ResearchGate also reports no full text. The manuscript now preserves the separation/recovery caveat and avoids a condition-matched numerical ranking.

Updated: data/semester-evidence-readiness-audit.csv (EV-SEM-014); data/semester-results-discussion-claim-evidence-audit.csv (RD-009); data/semester-condition-labelled-comparison.csv (new provisional EV-SEM-014 row); data/semester-main-corpus-crosswalk.csv (SEM-020); manuscript §3.2; narrative audit report.

Sources: https://www.tandfonline.com/doi/full/10.1080/09593330.2015.1054316 ; https://pubmed.ncbi.nlm.nih.gov/26050736/


## Follow-up source check — SEM-037 / EV-SEM-011 (29 October 2026)

The sodium alginate/graphene oxide hydrogel-bead PRB study was checked against the PubMed abstract and indexed ScienceDirect full-text excerpts. The complete PDF/table-level extraction remains inaccessible in the inspected Library/public routes.

- Accessible source text confirms batch and flow-through column experiments; flow rate, influent CIP concentration and ionic strength were varied; a two-site chemical non-equilibrium model was used to design the PRB based on local hydrogeology.
- The source reports approximately 72 h equilibrium and 100 mg/g at pH 7. An internal source inconsistency is documented: the abstract says the isotherm follows Freundlich, while the indexed conclusion labels 100 mg/g a Langmuir-model maximum.
- The abstract says PRB lifetime and cost were calculated. Numerical lifetime/cost results, assumptions and supporting tables are not accessible in the indexed excerpts. The manuscript acknowledges the existence of the analysis but does not quote unverified outputs.
- Updated the evidence-readiness row EV-SEM-011, claim-audit row RD-015, added a condition-labelled comparison row, updated the SEM-037 crosswalk, and revised manuscript §3.4 and the claim-audit report.

Sources: https://pubmed.ncbi.nlm.nih.gov/29510369/ ; https://www.sciencedirect.com/science/article/pii/S0045653518303692

## Follow-up full-text audit — SEM-039/EV-SEM-015 and SEM-040/EV-SEM-016 (29 October 2026)

Official open-access publisher HTML for both Scientific Reports papers was rechecked.

- CNF/GO aerogel (DOI 10.1038/srep45914): Fig. 7/text verifies TC removal=82.1% in the 21-antibiotic screen; Fig. 13/text gives TC removal=78.9% after ten cycles. General methods specify 8 mg in 40 mL, 160 rpm and 25 °C overnight, with C0 1–100 mg/L and pH adjusted 2–12, but Fig. 7's caption does not give a single C0/pH/dose. Table 1 PSO fitted qe=84.8 mg/g; Table 2/Fig. 9 Langmuir fitted qm=454.6 mg/g, rounded to 454.5 in the conclusion; regeneration uses 5 wt.% NaOH for 5 h and wash/freeze-drying.
- Seven-antibiotic graphene (DOI 10.1038/srep31920): Experimental design specifies seven-drug mixture at 200 ng/mL each (200 μg/L), 100 mg sorbent/100 mL (1 g/L), pH 7, 298 K, 120 rpm. Results/Fig. 2 text reports graphene TC equilibrium at ~2.5 h; 89.3–100% is a range across all seven drugs, not the TC-specific value. Mean qe=190.3 μg/g for graphene is also across the seven drugs. Exact TC removal remains figure-only and is not guessed.
- Updated readiness rows EV-SEM-015/016, claim audit RD-010/011, condition comparison rows, SEM-039/040 crosswalks, manuscript §3.3 and the narrative audit report. No new PDF intake was requested.

Source pages: https://www.nature.com/articles/srep45914 ; https://www.nature.com/articles/srep31920

## Follow-up full-text source audit — SEM-034 / EV-SEM-027 (29 October 2026)

Direct RSC full-text retrieval succeeded for Hossain et al., RSC Advances 14 (2024), 1431–1444, DOI 10.1039/d3ra07597d. It supplies exact source locations for the previously noted GO/Co–Fe claim:

- Abstract and §3.2.2/Fig. 5(b): TC removal 94.1%.
- §3.2.4/Fig. 5(d): TC removal 93.91%.
- §4 Conclusion: TC removal 93.94%.
- §2.6: methods/ranges; reported optimum TC removal condition C0=0.2 mg/L, dose 0.15 g/L, pH7, room temperature (~25°C), 250rpm and 30s.
- Table 2: Langmuir-fitted TC q_m=60.24/62.50/64.10 mg/g at 30/40/50°C respectively.
- §3.2.7/Fig.9: up to eight reuse rounds with methanol/water rinse, drying at 50°C, and efficiency reported declining from 95% to 90%.

The three removal percentages are a genuine internal inconsistency; they are now all preserved with separate source locations. No normalized cost estimate or real-water trial was found in the full text sections inspected. The readiness table, RD-012, condition-labelled comparison, SEM-034 crosswalk and manuscript were updated.

Source: https://pubs.rsc.org/ra/article/14/2/1431/825803/Ultrafast-and-simultaneous-removal-of-four

## Citation-key reconciliation follow-up — 29 October 2026

The actual Library file `/full ++.bib` was located and materialized for a direct check. It contains 164 BibTeX entries, 164 unique keys and no duplicate keys. Comparing the 15 distinct citation keys in `manuscript/SEMESTER_RESULTS_AND_DISCUSSION_V1.md` against the DOI/key fields in `full ++.bib` gives six exact DOI/key matches and nine cited references whose DOI/title is absent from that export. The six matching records are:

- `liThreedimensionalGrapheneOxidebased2025`
- `shahaExploringAdsorptionEfficiency2025`
- `zhangAdsorptionCharacteristicsNrGO2022`
- `zhuCiprofloxacinAdsorptionGraphene2015a`
- `yao3DAssemblyBased2017`
- `pengAdsorptionAntibioticsGraphene2016`

The other nine have complete records in `references/semester-manuscript-cited-references.bib`, but use project-local citation keys not verified as live Better BibTeX keys. To make that gap actionable without importing the six records already present in the export, created `references/zotero-import-batch-missing-nine-2026-10-29.bib` with only those nine entries. The linkage audit rows are updated to point to this batch.

**Next action:** before importing, search Zotero by DOI for duplicates (the checked export may be older than the live Zotero library). Import only missing items, generate a fresh Better BibTeX export, then map the newly generated citation keys back into the manuscript. Until that re-export exists, the current standalone manuscript bibliography is citation-complete locally but not fully synchronized to the user's Zotero/Better BibTeX keyspace.

## Final synchronization after citation batch creation (29 October 2026)

The manuscript §3.6 citation-readiness note and claim-audit row RD-018 were updated after the import-batch creation. A fresh repository fetch confirms: 14 citation commands cover 15 distinct unique keys; the local standalone bibliography has 15 entries; every manuscript key resolves locally; there are no orphan entries or `CITATION KEY PENDING` placeholders. The import file contains exactly nine unique entries, all of them already represented by project-local entries in the standalone bibliography. Six references remain exact DOI/key matches in full ++.bib; the nine missing-export items remain not synchronized until a fresh Zotero/Better BibTeX export is checked.

Validated links:
- `manuscript/SEMESTER_RESULTS_AND_DISCUSSION_V1.md`
- `references/semester-manuscript-cited-references.bib`
- `references/zotero-import-batch-missing-nine-2026-10-29.bib`
- `data/semester-bibtex-citation-linkage-audit.csv`
- `data/semester-results-discussion-claim-evidence-audit.csv`

## Recheck of the user-provided full++ BibTeX attachment

- On 2026-10-29, the user re-attached `full ++=.bib` as `full ++=.bib`.
- The attached file was byte-for-byte identical to the previously materialized `/full ++.bib` export: SHA-256 `e8275eb705f3e1d3c85ba0acdc6caeda37f8ffe6c1ea5000f69c1d72c85f16ec`, 337,912 bytes.
- Parsed integrity: 164 entries, 164 unique citation keys, no duplicate keys; 161 entries contain a DOI.
- The six previously matched semester-manuscript keys remain present. None of the nine DOI-checked records in `references/zotero-import-batch-missing-nine-2026-10-29.bib` is present by DOI or project-local key in this export.
- This attachment therefore does not establish that those nine records were imported into the live Zotero library or that Better BibTeX was re-exported after import. Keep the synchronization status **pending**; do not relabel the project-local keys as Zotero-generated keys.
- Next checkpoint: import/check the nine DOI records in Zotero (avoiding duplicates), then provide a genuinely new Better BibTeX export. Reconcile its generated keys against the manuscript and retain the current 15-entry local bibliography until the fresh export is verified.
