# Reference-target execution plan — 2026-10-27

## Purpose
Convert the supervisor's approximately 60-reference semester target and approximately 150-reference journal-version target into an auditable acquisition process. Counts refer to distinct, relevant works actually cited in the manuscript—not PDF batches, candidate rows or evidence records.

## Verified starting point
- The current `data/corpus-screening-register.csv` has 62 candidate rows.
- The last project checkpoint recorded 61/62 completed full-text screens; `DISC-022` remains deferred, not screened and not excluded, until the user supplies its full-text PDF.
- The master evidence register contains findings from primary studies and reviews and is not a final bibliography count.
- The repository `references/` directory contains export instructions but no current `review-corpus.bib`, so neither reference-count target is yet verified as met.

## Deliverables added
- Expanded `docs/REFERENCE_TARGET_PLAN.md` with a two-stage plan, a reference-count allocation for the 60-reference semester version, an 80-primary-study class coverage target for the ~150 version, search passes, screening workflow and definitions of done.
- Created `data/reference-acquisition-tracker.csv` to log each search's exact query, filters, results, net-new candidates after deduplication, screen status, ranking status and associated search log. It is a blank tracker until an actual search pass is run; no search counts have been invented.

## Acquisition strategy
1. Reconcile the existing 62 candidates and the manuscript citations against a current Zotero Better BibTeX `review-corpus.bib` export; this is a bibliography export, not a request for an additional existing PDF batch.
2. Build the semester manuscript to approximately 60 distinct cited works from verified existing evidence plus targeted gap searches. Proposed main counting roles: 32 primary adsorption studies, 8 cross-cutting application studies, 7 mechanism/model foundations, 5 process-cost/LCA studies, 4 occurrence/risk/context sources, and 4 high-quality reviews. This is a guide, not a forced quota.
3. Expand the unique candidate pool toward 220–250 records for the journal version. From the current 62 candidate rows, the planning gap is approximately 158–188 net-new candidates before deduplication and screening decisions.
4. Search first for primary studies in under-covered material classes, then for real-water/mixed-feed/regeneration/fixed-bed evidence, mechanism/model validation, processing-cost/energy/LCA/end-of-life, and context/review sources. Use review reference lists and cited-by trails for backward/forward citation chasing.
5. Screen titles/abstracts first; obtain full texts only for promising candidates. Use the user's university access when a subscription full text is not legitimately accessible through the available session. The completion of Batch 20 does not mean literature discovery has ended.
6. Count a source only when the manuscript actually cites that distinct work for a supported claim. Deduplicate preprint/published versions and repeated citations; keep the journal-quartile provider/year/category policy separate from relevance screening.

## Next execution task
Run the first documented gap-led search pass prioritising (1) primary adsorption studies on unmodified biopolymers and pristine biochar, and (2) adsorption-only engineered/doped biochar. Record exact queries and net-new results in `data/reference-acquisition-tracker.csv`; do not fabricate count results or promote search snippets into evidence. Continue later with activated-carbon fixed-bed/real-water work and process cost/LCA gaps.

## Guardrails
- No padding to hit a bibliography count.
- No treating 62 candidates as 60 references.
- No using review tables as the source of experimental capacities without tracing to the original paper.
- No merging removal percentage, observed uptake, fitted qmax, partition coefficients or column metrics.
- No strict Q1 eligibility claims until the required provider/year/category rule is set and verified.
- `DISC-022` stays deferred until the user supplies its full text.