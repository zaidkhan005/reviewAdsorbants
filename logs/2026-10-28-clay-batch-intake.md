# BATCH-20261028-CLAY — PDF intake and source review (2026-10-28)

## Why this batch has a unique ID
The standard `batch-01-*` staging paths were already occupied by another three-paper upload (different papers, including a Zhao et al. 2011 goethite study). No existing files were overwritten. This batch is therefore staged under the unique ID `BATCH-20261028-CLAY` so parallel chats do not overwrite each other's evidence. The shared tracker remains unchanged in this branch and should be updated centrally during consolidation.

## Uploaded files processed
1. `1-s2.0-S014181302408365X-main.pdf` — Sharma et al. (2024), “Polysaccharide-based biopolymeric magnetic hydrogels for remediation of antibiotics from aqueous solution,” *International Journal of Biological Macromolecules* 283 (2024), article 137555. DOI: 10.1016/j.ijbiomac.2024.137555. 17 pages; review.
2. `1-s2.0-S0021979712000240-main.pdf` — Yan, Hu and Jing (2012), “Enrofloxacin sorption on smectite clays: Effects of pH, cations, and humic acid,” *Journal of Colloid and Interface Science* 372 (2012), 141–147. DOI: 10.1016/j.jcis.2012.01.016. 7 pages; primary experimental sorption/mechanism study.
3. `1-s2.0-S0021979715303374-main.pdf` — Aristilde et al. (2016), “Enhanced interlayer trapping of a tetracycline antibiotic within montmorillonite layers in the presence of Ca and Mg,” *Journal of Colloid and Interface Science* 464 (2016), 153–159. DOI: 10.1016/j.jcis.2015.11.027. 7 pages; primary experimental sorption/mechanism study.

## Repository matching / duplicate check
- Checked the current 68-row `data/corpus-screening-register.csv`: none of the three DOI/title records is already present there.
- All three already exist as leads in `data/planned-download-pool.csv`: review = POOL-103; montmorillonite/OTC = POOL-153; smectite/ENR = POOL-159. These are existing planned-pool records, not new discoveries, and no duplicate pool rows were added.
- No rows were appended to the shared screening/evidence/quartile/tracker files. Stable candidate and evidence IDs must be assigned centrally after cross-chat reconciliation.

## Screening disposition
- Sharma et al. (2024): full-text reviewed; **background / citation-discovery only**. It is a narrative review, not an original experiment. Table 1 (PDF p.10) is useful for locating original studies but includes fluvastatin and diclofenac, which are not antibiotics despite the broad table title. Do not take capacity/reuse values from the review as primary evidence.
- Yan et al. (2012): full-text reviewed; **provisional retain as primary mineral-sorption/mechanism evidence**, subject to the agreed journal-year/provider/category eligibility rule. Extracted conditions, Freundlich fit parameters, pH/speciation trends, cation order, ionic-strength effect, clay comparison, ATR–FTIR and XRD interpretation.
- Aristilde et al. (2016): full-text reviewed; **provisional retain as primary mineral-sorption/mechanism evidence**, subject to quartile/category audit. It tests oxytetracycline on Na-montmorillonite with Ca/Mg and uses FTIR, solid-state NMR and XRD to test a mechanistic hypothesis. It is not a real-water treatment demonstration.

## Evidence notes
- Nine staging evidence rows are recorded. The review contributes two background/citation-discovery notes; the ENR paper contributes five condition/performance/mechanism notes; the OTC paper contributes three notes (one methods, one response, one mechanism).
- ENR Freundlich values retain the original K_F units (mg^(1−n) L^n g^−1); K_F is not q_max. Source: Table 1, PDF p.3. Main conditions are PDF p.2, Section 2.2; pH effects are Fig.2 PDF p.3; cation/clay comparisons are Figs.3–4 PDF p.4; spectroscopic and interlayer evidence is PDF pp.5–6.
- For Yan et al., the reported >85% sorption at pH 6.5–7.5 belongs to the study pH-edge setup (C0=18 mg/L); the surface-protonation explanation is proposed, not proven. Humic acid had only a marginal impact at the tested concentrations and solution composition.
- For Aristilde et al., increases of up to 80% at pH 6 and 120% at pH 8 refer to relative increases in clay-associated OTC under equimolar Ca/Mg:OTC conditions, not removal percentages and not q_max. Figure 1B is PDF p.2; methods are PDF p.3; Figs.2–3 and mechanism sections are PDF pp.4–6.
- Yan et al. used 1–24 mg/L ENR in isotherms, which is far above the ng/L-to-low-μg/L environmental occurrence range discussed in its introduction. Do not imply that the experiment directly establishes performance at trace environmental concentrations.
- Aristilde et al. used 320 μM OTC, 20 mg Na-MONT in 20 mL and pH 4/6/8 over 40 h. This is controlled model-clay evidence, not column, regeneration or actual-wastewater validation.
- Supplementary information referenced by both primary studies was not included in the uploaded PDFs; SI-only clay properties/speciation/model tables remain unavailable.
- Journal quartiles were not audited; do not infer Q1 from journal reputation. Better BibTeX keys remain pending because no current Zotero export was provided.

## Staging outputs
- Evidence: `data/batch-extractions/2026-10-28-clay-batch-evidence.csv`
- Screening: `data/batch-extractions/2026-10-28-clay-batch-screening.csv`
- This log: `logs/2026-10-28-clay-batch-intake.md`

## Central consolidation steps
1. Check this unique batch ID and all DOIs against every completed branch, not only the current master screening register.
2. Allocate stable candidate IDs without collision, replace proposed IDs in staging rows, and assign permanent evidence IDs.
3. Add validated rows to the master evidence/screening/adjudication files only after checking current SHAs and sibling batch outputs.
4. Update the three planned-pool rows as downloaded/processed and update the shared new-paper batch tracker centrally.
5. Audit the applicable journal quartiles by the agreed publication-year/provider/category rule before final Q1-only inclusion.
6. Keep DISC-022 deferred until the user supplies its full-text PDF.