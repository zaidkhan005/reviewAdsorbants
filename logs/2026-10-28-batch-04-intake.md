# BATCH-04 intake and evidence extraction — 2026-10-28

## Why BATCH-04 was used
The existing BATCH-01 and BATCH-02 staging namespaces were already occupied; a parallel branch had also populated BATCH-03 with different papers after an earlier check. I inspected that BATCH-03 content and left it untouched. BATCH-04 paths were checked and unused before creating this batch.

## Uploaded PDFs and matching pool IDs

| Uploaded file | Paper | DOI | Pool ID | Proposed record |
|---|---|---|---|---|
| `1-s2.0-S030147972400728X-main.pdf` (13 pages) | Minaei et al. (2024), *Journal of Environmental Management* 358, 120742 | `10.1016/j.jenvman.2024.120742` | POOL-161 | `PROPOSED-BATCH-04-PAPER-01` |
| `1-s2.0-S0043135409001468-main.pdf` (12 pages) | Putra et al. (2009), *Water Research* 43, 2419–2430 | `10.1016/j.watres.2009.02.039` | POOL-078 | `PROPOSED-BATCH-04-PAPER-02` |
| `1-s2.0-S0043135416301749-main.pdf` (10 pages) | Shimabuku et al. (2016), *Water Research* 96, 236–245 | `10.1016/j.watres.2016.03.049` | POOL-117 | `PROPOSED-BATCH-04-PAPER-03` |

All three exact DOI/title records were in the planned download pool but absent from the master screening register when first checked. Proposed IDs are temporary. The central consolidation must allocate permanent IDs after reconciling all branch staging files.

## Paper 1 — acid-modified activated-sludge biochar
- Preparation: H3PO4 modification + microwave pyrolysis under N2; reported optimum 800 W, 8 min, ~2.6 M H3PO4; wash to neutral pH and dry at 105 °C overnight. PDF pp. 2–4; §2.2; Table 1; §3.1.
- PBC BET area 365 m²/g vs 5 raw biomass; pore volume 0.79 vs 0.09 cm³/g; mean pore size 1.3 vs 15 nm. PDF p. 4, §3.2; Fig. 1 p. 5.
- Batch tests at 2 g/L, 100 mg/L target, 25 °C: stated equilibration ~24 h SMX and ~48 h LIN. Pseudo-second-order fitted qe single SMX/LIN 40.01/28.10 mg/g; binary 27.24/9.1 mg/g. PDF p. 7/Table 2/Fig. 4a.
- Major discrepancy: abstract maximums 45.6 mg/g SMX and 26.6 mg/g LIN conflict with Table 3 Langmuir qmax single 67.52/34.42 and binary 37.51/10.97 mg/g. PDF pp. 1, 8. Do not silently reconcile; SI not supplied.
- pH highest SMX uptake at pH 4; LIN uptake rises with pH 3–10; pHpzc 4.78; NaCl effect not significant (p > 0.05). Proposed hydrogen bonding/π–π interactions. PDF p. 9/Fig. 6/§3.6.
- Column: 0.7 g PBC-B, 1.5 mL/min, feed spiked at 200 mg/L. Table 4 Thomas qT water 43.6/39.2 and wastewater 37.92/34.42 mg/g, while text separately reports experimental wastewater uptake 2.85/3.64 mg/g and breakpoints 4.7/2.7 h. PDF p. 10/Table 4/Fig. 7. Methods say 22 ± 2 °C but Table 4 says 25 °C. Preserve separate endpoints.
- Five cycles report capacity loss ~30% SMX and ~40% LIN; acetonitrile desorption lasted 24 h. PDF p. 11/Fig. 8/§3.8 and Methods §2.4 p. 3. Solvent recovery, energy and cost not quantified.

## Paper 2 — amoxicillin on bentonite and activated carbon
- Natural bentonite from Pacitan, East Java versus commercial NORIT ROW 0.8 SUPRA GAC; both ground to 60/80 mesh. BET 91.627 vs 1092.951 m²/g; pHpzc 3.85 vs 4.91. PDF pp. 2–4; §§2.1/3.1; Figs. 1/4.
- Isotherms: 300 mg/L initial amoxicillin, dose 0.1–1.5 g/50 mL, 30 °C, 200 rpm; pH around 2, pHpzc and 7. Table 4 Langmuir qmax bentonite 47.37–53.93 mg/g; GAC 186.93–221.87 mg/g. PDF p. 7/Table 4/Fig. 6.
- Kinetic Table 6 experimental qe 18.749–20.517 mg/g bentonite and 24.745–25.055 mg/g GAC; pseudo-second-order R² > 0.99. PDF p. 11/Table 6. Different endpoint from qmax; pH values differ slightly across tables.
- Real pharmaceutical wastewater: initial 317 mg/L, dose 1.5 g/50 mL; final 38 mg/L on bentonite and 16.9 mg/L on GAC, reported removal 88.01% and 94.67%. PDF p. 11/Table 7. This is one high-concentration wastewater test and not direct evidence for trace concentration or column performance.
- Article gives amoxicillin pKa 2.68, 7.49 and 9.63; proposed bentonite cation exchange/site interactions and GAC pore/functional group mechanisms. PDF pp. 4–6, 8–11. These are author interpretations.

## Paper 3 — biochar sorbents for SMX in several water matrices
- Wood chars include TLUD pine 850 °C/20 min forced draft and 625 °C/45 min natural draft; retort eucalyptus 350 °C/96 h and pine 850 °C/8 h; sludge-derived materials at 850 °C/2 h. Selected BET: W-R-350 39, W-ND-625 172, W-R-850 362, W-FD-850 405, PAC 697 m²/g. PDF pp. 2–4; Table 1.
- Main metric is Dose75%: dose for 75% SMX removal at 60 min, initial SMX ~100 ng/L and pH 7.2. Across DI/surface/effluent/stormwater, PAC 10/40/70/60 mg/L, W-FD-850 10/80/150/150, B-R-850 45/225/300/450. PDF p. 4/Table 3. This is mg/L dose, not qmax/qe. Not-analyzed entries must remain missing, not zero.
- Water quality: surface water pH 7.0/DOC 15 mg-C/L; wastewater effluent pH 7.4/DOC 7.5; stormwater pH 7.5/DOC 5.0. PDF p. 4/Table 2. DOM lowered uptake for most sorbents; high-ash sludge chars showed less competition than lower-ash wood chars in the tested waters. PDF p. 6/Fig. 4.
- Within this data set the dose/surface-area relationship plateaus around AFM area ~400 m²/g; not a universal threshold. PDF pp. 5–6/Figs. 2–3. Selected equilibrium checks ran 7 days; in surface water relative removal was roughly stable at initial SMX 50–10,000 ng/L and changed at ≥100,000 ng/L under tested conditions. PDF pp. 7–8/Figs. 5–6.
- Companion LCA is cited as 'in prep', not completed. Supplementary figures/data are referenced but absent.

## Staging outputs
- `data/batch-extractions/batch-04-evidence.csv` — 15 source-pinned evidence rows.
- `data/batch-extractions/batch-04-screening.csv` — 3 provisional screening rows.
- `logs/2026-10-28-batch-04-intake.md` — this log.

Schemas match the current master evidence and screening headers. Shared master registers and the common tracker were not edited from this branch. Quartiles and Zotero/Better BibTeX keys remain pending.

## Consolidation checklist
1. Allocate final candidate/evidence IDs after checking all batch branches.
2. Deduplicate again against newest master register and pool.
3. Validate schemas and evidence-candidate references before merge.
4. Audit ranking provider/system, publication year and category separately; no Q1 claim made here.
5. Obtain SI for papers 1 and 3 if available.
6. Keep DISC-022 deferred until its full text is supplied.