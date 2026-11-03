# Final 94-claim manuscript integration audit — 3 November 2026

## Scope

Compared the current `data/semester-manuscript-claim-evidence-audit.csv` (94 source-specific/grouped claim records) against the reader-facing `manuscript/SEMESTER_MANUSCRIPT_ASSEMBLED_SOURCE_V2.md`, the consolidated 53-entry BibTeX file and the frozen 49-study selection.

This pass distinguishes section-level citation integration from source-level scientific qualification. It does not imply that every numerical result in an evidence record is suitable for the main text; existing holds and source-access limits remain controlling.

## Findings

### Section-level integration

- The ledger contains **94 unique claim IDs**, CLM-01–CLM-94.
- Every non-synthesis claim key (53 distinct Better BibTeX keys across 94 records) appears in the manuscript subsection/range declared for that claim.
- The source-specific additions for CLM-47–CLM-94 are represented in the respective Results/Discussion, Mechanism, Practical Feasibility, Cost, Context or Scope sections.
- All 53 manuscript citation keys resolve to the 53-entry consolidated bibliography; no missing or unused key was found.
- The selected-reference file still contains 49 unique selected studies.
- The claim ledger retains the 10-column schema and 94 data rows.

### Integration changes made

1. **Section 3.6.4 consolidated.** Removed the repeated summary of the Jahan magnetic GO/Co-MOF and Tekle Tegie Zr-modified magnetic GO examples. Kept one detailed account of each, with feed ceilings, endpoint types, source-internal percentage conflicts and condition-label caveats. Retained the separate Alishiri/Sikri/Ceylan paragraph; the copper-alginate/MOF-525, GO–TOPO:LevA membrane and CMC/GO cases; and the theory/review/scope-boundary paragraph.
2. **Mechanistic interpretation strengthened.** Section 4.3 now directly cites Jahan et al. (2026), Lemaoui et al. (2026) and Saheed et al. (2026), while keeping proposed coordination/hydrogen-bonding interpretations separate from direct evidence. Section 4.5 now cites the DFT-only rGO/CIP/TC model study as theory context, not an aqueous adsorption experiment.
3. **Preparation burden citations added.** Section 5.1 now cites the battery-derived GO, SGO, PGOT@GEL, cellulose/aerogel, bead, magnetic composite and copper-alginate/MOF-525 preparation examples.
4. **Regeneration evidence integrated.** Section 5.2 now includes battery-derived GO, magnetic GO/Co-MOF, Zr-modified magnetic GO, ultrasound-assisted magnetic GO, N-rGO, PGOT@GEL, GO/PVA/alginate beads and chitin/GO, while keeping removal efficiency, capacity retention and desorption efficiency distinct.
5. **Matrix evidence integrated.** Section 5.3 now cites the Alishiri multi-water tests, chitin/GO spiked-water qualification, Tekle Tegie pharmaceutical-effluent arithmetic and GO–TOPO:LevA prefiltered/spiked municipal wastewater, with each matrix tier stated separately.
6. **Cost source added at point of use.** Section 5.4 now directly cites the Lemaoui USD/m² active-layer estimate and keeps it distinct from financial cost per m³.
7. **Missing feasibility example covered.** Section 5.1 now names the copper-alginate/GO/MOF-525 bead synthesis as a fabrication example and notes that reuse, real-water validation and quantified preparation cost were not reported.
8. **Ledger metadata corrected.** CLM-20–CLM-27 now point to their actual locations in Sections 3.6.1–3.6.3 rather than the outdated Section 3.1 label.
9. **Duplicate prose removed.** Section 3.6.4 contains one integrated treatment of the Jahan and Tekle studies rather than a short summary followed by a repeated longer version.

## Automated checks after the integration edits

| Check | Result |
|---|---:|
| Claim records | 94 |
| Claim IDs unique and contiguous | 94/94 |
| Keys in declared manuscript section/range | 53/53 |
| Distinct bibliography entries | 53 |
| Distinct manuscript citation keys | 53 |
| Missing citation keys | 0 |
| Unused bibliography keys | 0 |
| Frozen selected references | 49 |
| Section 3.6.4 repeated Jahan study summaries | 0 duplicates |
| Section 3.6.4 repeated Tekle study summaries | 0 duplicates |

The section-level check verifies that source keys appear in the manuscript locations declared by the ledger. It is not a substitute for final copy-editing or a renewed primary-source audit. Quantitative holds remain in force, including SEM-010, SEM-015, SEM-019/038, SEM-045/046/050/051, SEM-042 and SEM-044; no held value was promoted to an observed endpoint or ranking by this integration pass.

## Production

The manuscript-source edits triggered GitHub Actions rebuild run [41690681789](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41690681789). This log records the integration audit; production is not marked complete until the DOCX/PDF artifacts from the latest source commit are verified.

## Next work

After the build completes, verify the generated DOCX/PDF pagination and the edited Section 3.6.4, 4.3–4.5 and 5.1–5.4 pages. Then continue final scientific holds and editorial/institutional sign-off: supervisor/AMU citation-style confirmation, language editing, authorship/funding/conflict/data-availability declarations and the institutional submission checklist.
