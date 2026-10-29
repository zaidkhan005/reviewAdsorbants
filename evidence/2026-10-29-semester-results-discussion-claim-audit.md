# Claim-by-claim evidence audit — semester Results and Discussion

**Audit date:** 29 October 2026  
**Manuscript:** `manuscript/SEMESTER_RESULTS_AND_DISCUSSION_V1.md`  
**Scope:** Numeric and evidence-bearing claims in the current Results & Discussion draft, checked against the repository's condition-labelled comparison, evidence-readiness audit, and broad-corpus evidence rows.

## Outcome

The draft's numeric statements generally match the repository's existing evidence tables, and the prose often appropriately distinguishes observed uptake, fitted isotherm capacity, model-fitted kinetic uptake, removal percentage, and regeneration performance. The main remaining issue is not citation linkage but evidence strength: several numerical claims are based on abstract-level records or source extracts whose exact table/figure pin has not yet been completed.

The machine-readable audit is in [`data/semester-results-discussion-claim-evidence-audit.csv`](../data/semester-results-discussion-claim-evidence-audit.csv). It contains 18 claim groups covering the general comparison framing and every quantitative/feasibility paragraph in the current draft.

## High-priority scientific caveats

1. **Sulfonated GO / ciprofloxacin (EV-SEM-012):** the source pinpoint is now verified against the project PDF: Methods/equations and 50 mL/0.01 g basis, printed p. 40819; pH study, printed p. 40820; Table 1 and Fig. 7 temperature series, printed p. 40822; Fig. 10 isotherm range of 50–1000 μmol/L, printed p. 40824; Table 2 fitted model parameters, printed p. 40825. Table 1's qe(exp)=237.12 μmol/g at C0=50 μmol/L corresponds to ~94.85% removal using the article's stated dose and equation, while the text reports 96.53%. That mismatch remains. **The earlier 500 μmol/g ceiling warning was incorrect** because it applied the separate 10–100 μmol/L kinetic range to the isotherm fit; qmax=1000 μmol/g is fitted to the isotherm series reaching 1000 μmol/L, so that earlier ceiling cannot be used to disqualify it. The manuscript now removes this erroneous ceiling claim.

2. **Nitrogen-doped rGO / trace antibiotics (EV-B10-005/006):** primary-PDF source pins are now explicit: Methods §2.3, printed p. 1300, states 80 mL antibiotic solution plus 20 mL of N-rGO dispersion at 0.5 mg/L; Fig. 2a/Table 1 are printed p. 1302; Fig. 2b is printed p. 1302; Table 2 is printed p. 1303. Table 1 gives q_e(exp)=80.58–90.21 mg/g at nominal C0=10 μg/L. The paper does not clarify whether C0 refers to the original 80 mL or the final 100 mL mixture. If it refers to 80 mL before mixing, the 0.01 mg N-rGO mass implies an ~80 mg/g ceiling; if it describes the final 100 mL system, the ceiling is ~100 mg/g. This is an unresolved concentration/volume basis, not a settled correction. The much larger Table 2 Langmuir q_m outputs (574.71–1265.82 mg/g, including TC 662.25 and CLI 1265.82) remain model-fitted values and stay out of cross-study ranking pending dose, volume and fit-range reconciliation.

3. **PGOT@GEL / ciprofloxacin (EV-SEM-013):** the source pin is now verified: §2.6 on printed p. 3 points to Supporting Materials for full adsorption-test details; §3.3.6 on printed p. 9 gives the RSM conditions C0=296.52 mg/L, pH 6.70, dose 5.08 mg, 298.88 K, predicted qe=800.60 mg/g and validation qe=807.54 mg/g. The required adsorbed mass is about 4.1023 mg, so initial solution volume must be at least ~13.84 mL for simple mass-balance feasibility. The main PDF omits the volume and the supporting file was not found in the available project files or retrieved publisher page; leave this check incomplete rather than infer the qe is wrong. Figure 12's caption (printed pp. 10–11) labels the application as simulated real wastewater despite 'real water' wording elsewhere.

4. **GO–alginate permeable-reactive barrier (EV-SEM-011):** the abstract-level record gives a reported maximum capacity of 100 mg/g at pH 7 and approximately 72 h equilibrium, while saying the data fit Freundlich. The manuscript now calls this a “reported maximum adsorption capacity” and notes that its exact meaning is unclear from the abstract. It must not be treated as an identified Langmuir (q_{max}) or a fully verified column result.

5. **GO/PVA/calcium-alginate beads / cost (EV-SEM-026):** the cost calculation's 0.1 g/L assumption differs by 100-fold from 0.5 g in 50 mL (=10 g/L), and the method also says 50 mL in one place and 55 mL elsewhere. Both issues are now identified in the manuscript.

## What was corrected in the manuscript

- Added that the separate 56.8% removal pH test for the GO/calcium-alginate fiber study used 50 mg/L TC.
- Corrected the SGO/CIP source-pin audit: the isotherm range is 50–1000 μmol/L (Fig. 10, printed p. 40824), so the prior 500 μmol/g ceiling from the separate kinetic range was inapplicable and was removed. The real qe/removal mismatch remains flagged.
- Clarified the PRB study's 100 mg/g statement as a reported maximum at pH 7 whose capacity definition cannot be determined from the abstract.
- Added the 50 mL/55 mL method inconsistency for the bead-cost paper.
- Fixed stale §3.6 wording that said unresolved citation placeholders remained after all placeholders had been replaced.
- Removed the impression that GO–LDH, EDTA-functionalized GO and chitin/nGO column issues were evaluated in the prose of this draft. Those candidate caveats remain in the evidence register for a future decision if those sources are added.

## What remains before submission

- **Exact source pin:** the three priority claims now have source-page/table pinpoints in the readiness and claim-audit CSVs. This does not mean all other manuscript claims or every source in the evidence base received a fresh page-by-page audit; remaining provisional items are listed below.
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
