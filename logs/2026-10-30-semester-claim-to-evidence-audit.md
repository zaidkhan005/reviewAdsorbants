# Initial manuscript claim-to-evidence audit — 30 October 2026

## Scope and method

This checkpoint audits the complete current file `manuscript/SEMESTER_RESULTS_AND_DISCUSSION_V1.md` (Sections 3.1–3.6), not sections that do not yet exist in this working draft. The draft contains 15 distinct in-text citation keys and a 15-entry cited-reference subset. Each key was checked against the DOI-linked candidate record and citation-linkage audit for the user-supplied 173-entry `full ++ check again.bib` export dated 30 October 2026. Each scientific paragraph was then mapped to its candidate ID and dedicated or master-corpus evidence record, and checked against the source pins/access level already recorded in the repository.

The claim-by-claim matrix is in [`data/semester-manuscript-claim-evidence-audit.csv`](../data/semester-manuscript-claim-evidence-audit.csv).

## Overall result

- **Citation-key linkage:** 15/15 manuscript keys resolve to the 15-entry cited-reference subset and have exact DOI matches in the latest supplied export. This is a linkage result, not proof of scientific correctness or final citation-style rendering.
- **Claim coverage:** all 15 cited works are mapped to candidate IDs and evidence records. Six study paragraphs previously lacked explicit evidence tags; those tags have now been added. N-rGO reuses master evidence rather than duplicating it.
- **Evidence-record reconciliation:** SEM-037 (Zhao et al., 2018) had two dedicated evidence rows, EV-SEM-011 and EV-SEM-040. EV-SEM-040 is retained as the canonical record. EV-SEM-011 has been removed from the active evidence CSV and readiness audit; the earlier notes remain as clearly superseded historical provenance. The active dedicated evidence set is **39 unique records**, not 40.
- **Source access:** three cited studies remain abstract/preview-level for the claims made here: the graphene-versus-GAC benchmark (SEM-020), rotating-field Fe3O4/rGO (SEM-033), and groundwater PRB (SEM-037). Other studies have primary full-text or Library-PDF evidence, though individual conditions/SI may remain incomplete.

## Manuscript corrections made

1. **TC/GO–alginate fibres (SEM-004):** added the fit caveat that Freundlich R² (.9986) is slightly higher than Langmuir R² (.9938), even though the paper highlights the Langmuir qmax.
2. **Battery-derived GO/CIP (SEM-010):** made the source discrepancy explicit. Under the stated 40 mL volume, 99.0% removal would imply qe≈99 mg/g, while Table 4 reports experimental qe=78.82 mg/g and PSO-fitted qe=79.36 mg/g at overlapping nominal conditions. Also preserved the 20 mg/L versus 20 g/L GO dose conflict between abstract/Methods/figures and Conclusion.
3. **Graphene/TC seven-drug mixture (SEM-040):** added official SI Table S2 TC-specific experimental kinetic qe=200.2202 μg/g and fitted qe values 198.8393/200.6055 μg/g. Clarified that the main-text 190.3 μg/g mean is a seven-drug average. Preserved the approximately 0.11% excess over the feed-mass ceiling; no TC-specific removal percentage is inferred.
4. **Groundwater PRB (SEM-037):** consolidated EV-SEM-040 as the single active evidence record and aligned manuscript, linkage, readiness and crosswalk. The publisher abstract identifies Freundlich, while an indexed conclusion snippet attributes the same 100 mg/g maximum to Langmuir. The discrepancy is preserved.
5. **Cost-process paragraph:** removed unsupported NMP and ultrasound-energy examples from the current cited set. The revised examples are tied to cited studies: acid/oxidant functionalization, freeze-drying, NaOH or methanol/DMF-HCl regeneration, high bead dose and rotating-field operation with energy unreported.
6. **Citation status:** replaced stale 164-entry/nine-record import-batch wording in §3.6 with the current 173-entry/15-key reconciliation; the old import batch is noted as historical rather than a current import action.

## Remaining evidence caveats

- **SEM-004:** fit preference between Freundlich and Langmuir.
- **SEM-010:** same-condition removal/uptake mismatch and 1000-fold dose-unit discrepancy.
- **SEM-032:** validation solution volume and supplement remain unavailable; figure says simulated real wastewater while prose calls the samples real water.
- **SEM-016:** measured qe and removal percentage do not reconcile by mass balance at nominal stated conditions.
- **SEM-038:** 80 mL antibiotic feed plus 20 mL N-rGO dispersion leaves ambiguity over whether C0 refers to feed or final mixture.
- **SEM-020:** abstract-only evidence for rapid adsorption, matrix comparison and 323 mg/g fitted capacity.
- **SEM-039:** Fig. 7 TC removal does not specify a single C0/pH/dose; do not borrow conditions from separate factor tests.
- **SEM-040:** SI TC qe is approximately 0.11% above its stated feed ceiling; keep as a minor inconsistency.
- **SEM-034:** source gives 94.1%, 93.91% and 93.94% TC removal values in different locations; q_m=64.10 mg/g is fitted at 50°C.
- **SEM-033:** preview does not expose numerical qmax/qe, contact time, temperature, power or energy per treated volume.
- **SEM-031:** reported uptake/capacity values are mixture totals, not CIP-specific; no real wastewater tested.
- **SEM-037:** abstract/conclusion model attribution differs; numerical PRB column and cost/lifetime outputs remain inaccessible.
- **SEM-029:** experimental test dose is 10 g/L while cost model assumes 0.1 g/L; 50/55 mL wording also differs.

No comparable cost-per-volume or cost-per-mass-removed result can currently be calculated from the 15 cited studies. Author-described “low-cost” or “economical” performance remains unverified without a reproducible process boundary and cost denominator.

## Remaining work

The current working draft cites **15 distinct works** against the project target of approximately **50**, leaving about **35 additional distinct cited works**, subject to scope and evidence quality. Do not inflate the bibliography with weak, duplicate, out-of-scope or citation-key-unverified records. Next, expand the synthesis from eligible candidates already present in the repository/Library, reconcile new citations through Zotero/Better BibTeX, and repeat the claim audit after expansion. Final citation-style rendering and bibliography reconciliation remain pending.

## Primary-source links for the PRB model attribution audit

- [ScienceDirect article record](https://www.sciencedirect.com/science/article/pii/S0045653518303692)
- [PubMed record](https://pubmed.ncbi.nlm.nih.gov/29510369/)
