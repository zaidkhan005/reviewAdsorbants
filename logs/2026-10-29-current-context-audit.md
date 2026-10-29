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
| Semester candidate register | 38 | 37 prior targeted candidates plus one existing master-corpus candidate cross-referenced for TC |
| Semester dedicated evidence CSV | 13 | Dedicated extraction rows; the broad evidence is cross-referenced rather than copied |

## Separate workstreams

### Broad review (source of truth remains unchanged)

The broad review's intended structure is based on the supplied outline and processing–cost–performance continuum spanning raw biomass, natural clays, unmodified biopolymers, standard biochar, modified biochar, doped/engineered biochar, activated carbon and nano-engineered carbons. Supervisor planning figures remain roughly 60 distinct works cited for one publication version and 150 for a publisher/journal version. Neither actual citation count is confirmed; do not infer it from candidates/evidence rows. The current queue shows 58 entries still not matched into the register; 11 candidates DISC-069–DISC-079 have recently been added and 16 online/indexed evidence rows are provisional pending primary-PDF/SI pinning. `DISC-022` remains deferred under the historical broad-review instruction; it is not screened or excluded.

The current primary-study matrix has 208 rows for 43 candidates; the 2026-10-28 consolidation crosswalk is staging-to-master mapping, with multiple rows per paper expected. Never count crosswalk rows as distinct studies.

### Semester paper (approved scope)

**Title:** *Assessing the Low-Cost Potential of Non-Conventional Engineered Adsorbents for Ciprofloxacin and Tetracycline Removal from Aqueous Media.*

Include selected GO/rGO and functionalized graphene adsorbents and selected graphene-bearing composites only when the target-specific adsorption contribution is extractable. Core targets are CIP and TC; related antibiotics are not pooled with them. Green/waste-derived is not the defining theme. Low-cost is a claim to assess, not assume. The initial plan calls for about 50 distinct cited works, subject to eligibility and evidence quality.

The current dedicated extraction CSV has 13 records. Two already extracted full-text papers in the Library are the 2025 SGO/CIP study (SEM-016/CORP-024) and the 2025 PGOT@GEL/CIP study (SEM-032/CORP-015). A third in-scope item already has main-corpus evidence: Zhang & Wu (2022), N-rGO with tetracycline among six antibiotics (SEM-038/CORP-031), linked to EV-B10-004–EV-B10-009. Those existing evidence rows were cross-referenced rather than duplicated.

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
