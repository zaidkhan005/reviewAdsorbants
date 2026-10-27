# Targeted literature discovery pass 01 — 2026-10-27

## Objective
Run the first gap-led search pass to grow the candidate pool toward the existing 220–250 record planning range for a ~150-work journal manuscript. Focus: unmodified biopolymer evidence, pristine/unactivated biochar and adsorption-only biochar literature. Search result records are candidate leads, not automatically accepted references. No new PDF batch was requested.

## Search method and provenance
- Ran broad web-discovery queries combining antibiotic names, adsorption/sorption, chitosan/alginate/cellulose, pristine biochar, pyrolysis, doped biochar, regeneration and real-water contexts; then ran exact-title/DOI confirmation queries for candidate leads.
- This is a targeted discovery pass, **not** a comprehensive Scopus/Web of Science search and not a systematic review search. Per-query hit counts were not exposed by the search interface, so they have not been invented. Exact queries, the result-count limitation and the six net-new candidate credits are in `data/reference-acquisition-tracker.csv`.
- Compared DOI/title against the current screening register. Existing sources already in the register (including pristine macadamia-nut-shell biochar and existing N-doped/engineered-biochar studies) were not added again.
- No evidence rows were added to `data/corpus-evidence.csv` in this pass because source page/table/figure extraction and mass-balance review have not yet been completed for these new candidates.

## Net-new candidate leads added

| ID | Study / material | Why it merits assessment | Current status / caveat |
|---|---|---|---|
| DISC-031 | Adriano et al. (2005), “Adsorption of amoxicillin on chitosan beads: Kinetics, equilibrium and validation of finite bath models,” *Biochemical Engineering Journal*, DOI `10.1016/j.bej.2005.08.010` | A potentially useful earlier primary study of amoxicillin adsorption on chitosan beads, with batch kinetics/equilibrium and finite-bath model validation. | Abstract/publisher metadata only; verify bead preparation, source location and ranking eligibility; do not assume it satisfies a Q1-only core-study rule. |
| DISC-032 | Qian et al. (2025), “Sodium Alginate/Carboxymethyl Chitosan Hydrogel Microbeads for Antibiotic Adsorption in Single and Binary Systems,” *Gels*, DOI `10.3390/gels11080646` | Recent primary evidence on TC/CIP in single and binary feeds; useful for modified biopolymer hydrogels and competition. | Full text is available via PMC/MDPI, but it has not yet been systematically extracted. Carboxymethyl chitosan is modified biopolymer, not unmodified chitosan. Journal quartile audit pending. |
| DISC-033 | Zhang et al. (2024), “Preparation of mesoporous biogas residue biochar via a self-template strategy for efficient removal of ciprofloxacin: Effect of pyrolysis temperature,” *Journal of Environmental Management*, DOI `10.1016/j.jenvman.2024.121140` | Compares biochars produced at 300–900 °C from food-waste anaerobic-digestion residue; the abstract says no activator was used and reports a model-fitted 70.29 mg/g value for BRBC900. | Abstract/publisher metadata only. Keep the 70.29 mg/g figure as an abstract-level lead, not verified evidence; test conditions, observed vs fitted endpoint and full-text locations need checking. Current 2025 SJR journal signal is not paper-year eligibility. |
| DISC-034 | Silori et al. (2023), “Adsorptive removal of ciprofloxacin and sulfamethoxazole from aqueous matrices using sawdust and plastic waste-derived biochar,” *Bioresource Technology*, DOI `10.1016/j.biortech.2023.129537` | A direct contrast between sawdust-only biochar and sawdust/plastic co-pyrolysis for CIP and SMX, relevant to process route and feedstock decisions. | Abstract/publisher metadata only. Extract actual matrix, dose, feed, processing inventory and evidence locations before using removal percentages. Current 2025 SJR journal signal is not paper-year eligibility. |
| DISC-035 | Zhao et al. (2024), “Efficient Removal of Tetracycline from Water by One-Step Pyrolytic Porous Biochar Derived from Antibiotic Fermentation Residue,” *Nanomaterials*, DOI `10.3390/nano14171377` | Primary TC adsorption study using a circular feedstock; KOH activation is part of the one-step preparation, so it belongs in chemically activated—not pristine—biochar. | Full text is openly available at PMC. Methods print `q_e=(C_e−C_0)V/m` and `R%=(C_e−C_0)/C_0×100%`, signs inconsistent with positive adsorption where `C_e<C_0`; resolve this before using its capacity/removal claims. Quartile audit pending. |
| DISC-036 | Raju et al. (2026), “Antibiotic mitigation of aqueous systems using untapped potential of unsorted garden waste-derived biochar: performance evaluation and mechanistic insights,” *Environmental Geochemistry and Health*, DOI `10.1007/s10653-026-02982-7` | Recent CIP adsorption study comparing garden waste and cashew-nut-shell feedstocks and pyrolysis conditions; abstract reports tests at 5 mg/L CIP. | Abstract and PDF link located; full extraction pending. The abstract does not establish whether chemical activation was used, so the final material class must be verified rather than assumed. Quartile audit pending. |

## Repository changes
- Added DISC-031–DISC-036 as provisional leads in `data/corpus-screening-register.csv`.
- Added matching provisional roles to `data/candidate-decision-audit.csv` and `data/screening-decision-adjudication-v1.csv`.
- Added four newly encountered journal titles as **not yet audited** rows in `data/journal-quartile-audit.csv`; no quartile was invented.
- Added 21 query rows (exploratory and exact-title confirmation queries) to `data/reference-acquisition-tracker.csv`. The tracker records that per-query result counts were not exposed and credits each net-new candidate once.

## Updated corpus position
- Candidate register: **68 rows** (62 previous rows + 6 new discovery leads).
- Full-text screening: the previous checkpoint had 61/62 completed; the six new candidates remain at discovery stage. Do not describe these leads as full-text screened or accepted.
- Journal audit: **38 journal titles** (previous 34 + four new titles still pending audit).
- Evidence register: unchanged in this pass; no source-location evidence was added.
- Final reference count: still **not audited**; candidate rows and evidence records are not a count of distinct works actually cited.

## Immediate next task
1. Screen the accessible open full texts first: DISC-032 (PMC/MDPI hydrogel) and DISC-035 (PMC fermentation-residue biochar), preserving DISC-035's equation-sign caveat; inspect DISC-036's full text if the PDF source is accessible.
2. Then retrieve/inspect full text for DISC-033, DISC-034 and DISC-031 through legitimate publisher or institutional access as available; if subscription access is required, ask for only the specific relevant PDFs that cannot be accessed, not a bulk upload.
3. Keep discovery going after this pass: it added six net-new candidates, moving the inventory from 62 to 68—not close to the 220–250 planning pool yet.
4. Do not include any of these works in the final bibliography count until the source is judged relevant and actually cited in manuscript prose/table with a verified Zotero record.
5. Keep `DISC-022` deferred, not screened or excluded, until the user provides its full text.