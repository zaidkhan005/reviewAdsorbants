# BATCH-03 intake and evidence extraction — 2026-10-28

## Why this chat is BATCH-03

The first two batch staging namespaces are already occupied in GitHub by different upload sets: BATCH-01 and BATCH-02 have existing evidence, screening and log files. I did not overwrite them. This chat's three uploads are recorded under **BATCH-03**, the next unused namespace. The shared batch tracker is intentionally not edited from this branch; the central/master chat will update its BATCH-03 slots during consolidation.

## Uploaded files

1. `1-s2.0-S004565352301771X-main.pdf` — 13 pages.
2. `1-s2.0-S0013935120309002-main.pdf` — 10 pages.
3. `1-s2.0-S0013935121003856-main (1).pdf` — 20 pages.

All three files opened successfully, their text was extracted, and a contact sheet from rendered pages was inspected.

## DOI/title matching and duplicate handling

Compared against the current `data/corpus-screening-register.csv`, `data/planned-download-pool.csv` and existing batch staging files.

| Slot | Paper | DOI | Planned-pool match | Status |
|---|---|---|---|---|
| 1 | Poddar et al. (2023), “Techno-economic assessment of doxycycline recovery using rice straw biochar: A circular economic execution,” *Chemosphere* 338, 139504 | 10.1016/j.chemosphere.2023.139504 | POOL-077 | New candidate for screening; no exact DOI row in the 68-row master screening register or existing BATCH-01/BATCH-02 evidence |
| 2 | Conde-Cid et al. (2020), “Competitive adsorption and desorption of three tetracycline antibiotics on bio-sorbent materials in binary systems,” *Environmental Research* 190, 110003 | 10.1016/j.envres.2020.110003 | POOL-076 | New candidate for screening; no exact DOI row in the master register or existing BATCH-01/BATCH-02 evidence |
| 3 | Ashiq et al. (2021), “Carbon-based adsorbents for fluoroquinolone removal from water and wastewater: A critical review,” *Environmental Research* 197, 111091 | 10.1016/j.envres.2021.111091 | POOL-115 | **Duplicate of an already processed review in BATCH-02**; do not create another candidate or duplicate the existing review evidence |

The review in slot 3 was already processed in `data/batch-extractions/batch-02-evidence.csv` and `data/batch-extractions/batch-02-screening.csv`, with details in `logs/2026-10-28-batch-02-intake.md`. The “(1)” suffix in this chat's filename does not indicate a different publication. I did not duplicate its evidence rows. This reading independently flags an apparent internal inconsistency in its performance-ranking section: the review states a PC-based order “graphene > carbon nanotubes > biochar > carbon composite > nano-sorbents > activated carbon > clay-based sorbents,” but nearby text also calls the Co-carbon composite's PC (69.68 L/g) the highest and then describes graphene as the highest-PC class. Please reconcile that caveat with the already existing BATCH-02 evidence during central consolidation; do not duplicate the paper.

## Staged outputs

- `data/batch-extractions/batch-03-evidence.csv` — 15 source-linked evidence/caveat rows covering the two new primary studies only. IDs are staging IDs, not permanent master evidence IDs.
- `data/batch-extractions/batch-03-screening.csv` — two proposed screening rows for the two distinct new papers. IDs `PROPOSED-BATCH-03-PAPER-01` and `PROPOSED-BATCH-03-PAPER-02` are temporary; allocate global candidate IDs at consolidation.
- This log: `logs/2026-10-28-batch-03-intake.md`.

Nothing was added to the shared evidence, screening, quartile or tracker files from this batch branch.

## Paper 1 — Poddar et al. (2023), rice-straw biochar / doxycycline

- **Primary experimental paper plus techno-economic scenario analysis.** Provisional scope fit for processing–performance–cost analysis.
- Evidence staged for: comparative feedstock/pyrolysis screen; RSM optimum; kinetic time and observed/modelled q_e; fitted isotherm q_max; high-load natural-water matrix tests; ethanol desorption/recovery and reuse decline; author-modelled process economics; characterization/mechanism.
- **Crucial caveats preserved:** the “real-life” tests are distilled/tap/river/pond/seawater matrices at high initial Dox load, not a validated untreated-wastewater demonstration. The supplied main text references supplementary Table S1/S2 and Figs. S1/S3/S4 that were not uploaded. Do not mix observed q_e, fitted q_max, percent removal, desorption and reuse decline. The non-ionic/covalent mechanism is the authors' interpretation; thermodynamic units in Table 4 should be verified. The cost analysis is a scenario, not plant-level validation.

## Paper 2 — Conde-Cid et al. (2020), competitive tetracycline sorption on waste by-products

- **Primary experimental batch adsorption/desorption study.** Provisional relevance for competition, solution chemistry and low-cost waste-derived sorbents; contextual fit is agricultural-soil retention/amendment, not direct wastewater-plant performance.
- Evidence staged for: binary assay conditions; pH and organic matter of the three adsorbents; simple and binary adsorption trends; competition differences; desorption behavior; model fitting and proposed mechanism.
- Conditions: one antibiotic fixed at 200 µmol/L, the second varied up to 600 µmol/L; 1 g in 40 mL of 0.005 M CaCl₂; 24 h adsorption and 24 h desorption. Pine bark showed the strongest/least-competitive behavior; oak ash showed stronger competition; mussel shell showed lower retention and high desorption. Some ternary comparison data were reused from prior work.
- Do not compare these removal percentages directly with wastewater adsorption studies under different matrices or doses.

## Quartile and citation status

- `Chemosphere` was not found as a row in the current quartile audit in this pass; paper-year/category eligibility needs a separate central audit.
- `Environmental Research` has a partially resolved journal-level row, but its current/2024 Q1 signals do not establish 2020- or 2021-paper eligibility under the project's final rule. No final Q1 decision was made.
- No Zotero/Better BibTeX keys were invented. Keys remain pending until a verified export is available.

## Central consolidation checklist

1. Merge only the two new primary papers from this batch after fetching the newest register and checking for collisions; global IDs should be assigned after reconciling all batch branches.
2. Replace the 15 staging evidence IDs with unique permanent evidence IDs; do not duplicate the BATCH-02 Ashiq review.
3. Reconcile the additional review-inconsistency note with the already staged BATCH-02 review record.
4. Check and update BATCH-03 in the shared tracker centrally.
5. Audit Chemosphere and publication-year/category eligibility for all new candidates under the agreed Q1 rule.
6. Leave Zotero citation keys pending until the actual export is verified.
7. Keep `DISC-022` deferred; this batch did not screen or exclude it.
