# Biochar section and citation audit — 2026-10-27

## Deliverables
- Drafted `manuscript/SECTION_2_3_BIOCHAR_V1.md` from existing evidence records for DISC-025 (brewery-grain biochar), CORP-020 (sunflower-husk SF-600/PSF) and DISC-028 (KOH-activated dyeing-sludge biochar).
- Added `manuscript/CLAIM_TO_SOURCE_CITATION_LEDGER.md` to establish a per-claim chain from manuscript location to candidate/evidence ID, source page/table/figure, exact Zotero item, Better BibTeX key, final citation and bibliography audit.
- The section draft remains a working draft and uses temporary internal candidate IDs in its audit trail; final author–date citations have not been fabricated.

## Source-selection rationale
- DISC-025 is the strongest standard-biochar case in the supplied corpus because the existing extraction includes production yield, batch and fixed-bed data, matrix effects, regeneration and production-stage LCA.
- CORP-020 offers a controlled within-study SF-600 versus phosphoric-acid-activated PSF contrast for TC/CIP/SMX.
- DISC-028 offers activation, batch, matrix, fixed-bed, regeneration and author-reported cost data but has important internal inconsistencies. It is included as a caveated case, not a ranking exemplar.
- Biochar reviews were not used as primary quantitative sources in this draft; they remain secondary context/citation discovery only.

## Traceability and data integrity
- Each key paragraph is tied to one or more existing evidence IDs and exact PDF page / table / figure locations as recorded in `data/corpus-evidence.csv`.
- Fixed-bed `q_TH`, `q_Y`, experimental `q_s`, breakthrough time and treated volume remain separate.
- Observed uptake and fitted `q_m`/`q_max` remain separate.
- Filtered/autoclaved real wastewater is not called untreated wastewater.
- The sunflower paper's Figure 2 panel-condition mismatch is carried forward.
- The dyeing-sludge paper's BET-area, isotherm-temperature, dosage, removal-equation, regeneration-label and fixed-bed-capacity issues are preserved; disputed metrics are not presented as rankings.
- Section 2.3 content is not ranked by journal Q1 signal. Publication-year/category rules remain unresolved at project level.

## Citation integrity
The ledger uses pending fields for Zotero item matching, Better BibTeX keys and final author–date strings because those must be read from the live Zotero record/export and chosen journal style. DOI links/candidate IDs are not final manuscript citations.

## Next actions
1. Verify Better BibTeX keys using an actual current Zotero export and resolve metadata/version identity; do not guess keys from DOI or author name.
2. Confirm the required Q1 provider/year/category before final include/exclude decisions.
3. Recheck source figures and supplements for held metrics, especially DISC-028, and use a transparent “not accessible” status when supplements are unavailable.
4. Continue a sentence/table-row claim audit for earlier Sections 2.1 and 2.2, then run final citation and bibliography consistency checks.
5. Keep DISC-022 deferred and outside the active queue until the full-text PDF is provided by the user.