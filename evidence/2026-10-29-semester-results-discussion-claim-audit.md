# Claim-by-claim evidence audit — semester Results and Discussion

**Audit date:** 29 October 2026  
**Manuscript:** `manuscript/SEMESTER_RESULTS_AND_DISCUSSION_V1.md`  
**Scope:** Numeric and evidence-bearing claims in the current Results & Discussion draft, checked against the repository's condition-labelled comparison, evidence-readiness audit, and broad-corpus evidence rows.

## Outcome

The draft's numeric statements generally match the repository's existing evidence tables, and the prose often appropriately distinguishes observed uptake, fitted isotherm capacity, model-fitted kinetic uptake, removal percentage, and regeneration performance. The main remaining issue is not citation linkage but evidence strength: several numerical claims are based on abstract-level records or source extracts whose exact table/figure pin has not yet been completed.

The machine-readable audit is in [`data/semester-results-discussion-claim-evidence-audit.csv`](../data/semester-results-discussion-claim-evidence-audit.csv). It contains 18 claim groups covering the general comparison framing and every quantitative/feasibility paragraph in the current draft.

## High-priority scientific caveats

1. **Sulfonated GO / ciprofloxacin (EV-SEM-012):** the repository record reports (q_e=237.12 μmol/g), a reported 96.53% removal at the nominally same condition, and a mass-balance check of about 94.85%. In addition, the fitted (q_{max}=1000 μmol/g) is an extrapolated parameter; at the stated highest feed concentration of 100 μmol/L and 0.2 g/L dose, the simple feed-mass ceiling is about 500 μmol/g. The manuscript now flags both the removal/(q_e) mismatch and the limits of the fitted maximum without changing the paper's numbers.

2. **Nitrogen-doped rGO / trace antibiotics (EV-B10-005/006):** the evidence register records 0.1–20 μg/L feeds, reported N-rGO dose of 40–400 μg/L, kinetic (q_e=80.58–90.21) mg/g and fitted Langmuir (q_m=574.71–1265.82) mg/g. An example 10 μg/L feed setup implies a simple mass-balance ceiling of about 80 mg/g. The manuscript correctly keeps these capacities out of the quantitative ranking pending unit/dose reconciliation.

3. **PGOT@GEL / ciprofloxacin (EV-SEM-013):** the reported RSM validation is (q_e=807.54) mg/g at (C_0=296.52) mg/L, pH 6.70, 5.08 mg adsorbent and 298.88 K, but solution volume is not available in the extracted record, so the loading cannot be independently mass-balanced. The source also conflicts on whether its water-matrix test is real water or simulated wastewater. Both limitations remain stated.

4. **GO–alginate permeable-reactive barrier (EV-SEM-011):** the abstract-level record gives a reported maximum capacity of 100 mg/g at pH 7 and approximately 72 h equilibrium, while saying the data fit Freundlich. The manuscript now calls this a “reported maximum adsorption capacity” and notes that its exact meaning is unclear from the abstract. It must not be treated as an identified Langmuir (q_{max}) or a fully verified column result.

5. **GO/PVA/calcium-alginate beads / cost (EV-SEM-026):** the cost calculation's 0.1 g/L assumption differs by 100-fold from 0.5 g in 50 mL (=10 g/L), and the method also says 50 mL in one place and 55 mL elsewhere. Both issues are now identified in the manuscript.

## What was corrected in the manuscript

- Added that the separate 56.8% removal pH test for the GO/calcium-alginate fiber study used 50 mg/L TC.
- Strengthened the SGO/CIP paragraph to note that the fitted (q_{max}) is an extrapolation beyond the loading implied by the stated feed/dose and should not enter an unqualified numeric comparison.
- Clarified the PRB study's 100 mg/g statement as a reported maximum at pH 7 whose capacity definition cannot be determined from the abstract.
- Added the 50 mL/55 mL method inconsistency for the bead-cost paper.
- Fixed stale §3.6 wording that said unresolved citation placeholders remained after all placeholders had been replaced.
- Removed the impression that GO–LDH, EDTA-functionalized GO and chitin/nGO column issues were evaluated in the prose of this draft. Those candidate caveats remain in the evidence register for a future decision if those sources are added.

## What remains before submission

- **Exact source pin:** many readiness rows give section/table/figure hints rather than a final pinpoint for every numeric statement. The audit therefore confirms alignment to the repository's existing evidence record; it does not claim an independent, page-by-page re-extraction of every primary PDF in this pass.
- **Abstract-only evidence:** the graphene/GAC benchmark's 323 mg/g and ~3 min equilibrium (EV-SEM-014), the rotating-field study (EV-SEM-037), the multicomponent SGO results (EV-SEM-036), and the PRB result (EV-SEM-011) should remain provisional until the corresponding tables/conditions are accessible.
- **Missing figure-specific detail:** the TC-specific value in the seven-antibiotic graphene study remains figure-based and unextracted; the exact TC conditions for the cellulose-nanofibril/GO aerogel's 82.1% comparison remain unpinned. The manuscript does not guess either.
- **Cost normalization:** the synthesis is supportable as a caution that comparable full-process cost inventories are largely missing; it is not support for a claim that any one material is the lowest-cost option.
- **Citation workflow:** all 15 citation keys resolve within the project-local BibTeX file, but nine project-local keys are not yet verified as keys generated by the user's live Zotero/Better BibTeX database. Merge/check those records and re-export before final style rendering.

## Source files used for this audit

- `data/semester-condition-labelled-comparison.csv`
- `data/semester-evidence-readiness-audit.csv`
- `data/corpus-evidence.csv` (including EV-B10-004–EV-B10-009 for N-rGO)
- `data/semester-main-corpus-crosswalk.csv`
- `references/semester-manuscript-cited-references.bib`
- `manuscript/SEMESTER_RESULTS_AND_DISCUSSION_V1.md`

**Disposition:** The draft has a consistent citation-to-bibliography map and a more explicit set of caveats, but it remains a working draft. Its next scientific step is targeted source-pin completion for the highest-impact numeric claims, not broadening the reference pool or silently recalculating conflicting paper values.
