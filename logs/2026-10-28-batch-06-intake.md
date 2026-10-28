# BATCH-06 intake — 2026-10-28

## Why this is BATCH-06
The upload context suggested the first batch, but the repository already contains staging files and an intake log for BATCH-01 using three different PDFs, as well as BATCH-02 through BATCH-05 staging files. To avoid overwriting sibling-chat work, the present three PDFs are recorded as **BATCH-06**. The shared tracker is left untouched here; central consolidation should update its BATCH-06 rows.

## Uploaded files and pool matches

| Slot | Uploaded filename | Identified paper | DOI | Pool ID | Proposed candidate ID |
|---|---|---|---|---|---|
| Paper 1 | `1-s2.0-S0141813020327744-main.pdf` | Ranjbari et al. (2020), “Efficient tetracycline adsorptive removal using tricaprylmethylammonium chloride conjugated chitosan hydrogel beads: Mechanism, kinetic, isotherms and thermodynamic study,” *International Journal of Biological Macromolecules* 155, 421–429 | `10.1016/j.ijbiomac.2020.03.188` | POOL-095 | PROPOSED-BATCH-06-PAPER-01 |
| Paper 2 | `1-s2.0-S0141813023020500-main.pdf` | Bouaziz et al. (2023), “Adsorption of antibiotics by bentonite-chitosan composite: Phenomenological modeling and physical investigation of the adsorption process,” *International Journal of Biological Macromolecules* 242, 125156 | `10.1016/j.ijbiomac.2023.125156` | POOL-118 | PROPOSED-BATCH-06-PAPER-02 |
| Paper 3 | `1-s2.0-S0141813024041874-main.pdf` | Rostami et al. (2024), “Surface modified of chitosan by TiO2@MWCNT nanohybrid for the efficient removal of organic dyes and antibiotics,” *International Journal of Biological Macromolecules* 274, 133382 | `10.1016/j.ijbiomac.2024.133382` | POOL-154 | PROPOSED-BATCH-06-PAPER-03 |

All three DOI/title checks found no match in the current master screening register or evidence table. The three DOIs were present in the planned pool as discovery leads, not previously screened candidates.

## Staging outputs
- Evidence: `data/batch-extractions/batch-06-evidence.csv` — 18 source-linked rows, IDs `STAGE-BATCH-06-P1-E01` through `STAGE-BATCH-06-P3-E18`.
- Screening: `data/batch-extractions/batch-06-screening.csv` — three full-text-reviewed provisional screening rows.
- This note: `logs/2026-10-28-batch-06-intake.md`.
- Master evidence/screening CSVs, quartile audit, and shared batch tracker were not edited from this batch pass.

## Main findings and caveats

### Paper 1 — modified chitosan / tetracycline
The ionic-liquid-impregnated chitosan beads are a modified biopolymer, not unmodified chitosan. Table 3 gives experimental maximum capacities 14.616, 16.585 and 20.854 mg/g at 25, 35 and 45 °C, while Langmuir-calculated capacities are 17.152, 17.985 and 22.421 mg/g. These remain separate. The dosage basis is inconsistent across sections and units, and Table 4 gives positive ΔG values (+5.764 to +2.796 kJ/mol) despite interpretation as increasing favourability; thermodynamic spontaneity wording is on hold. Four-cycle reuse with 0.01 M H2SO4 shows about a 10% decrease by cycle four. No real wastewater validation was identified.

### Paper 2 — bentonite–chitosan / three antibiotics
Table 3 reports experimental and fitted statistical-physics saturation quantities for doripenem, ampicillin and amoxicillin across 303.15–323.15 K. The paper's best fit is its one-site monolayer model (reported R² ~0.996–0.999). Composite preparation is referred to a cited earlier paper and not fully described; the current paper says atomic absorption spectrophotometry was used for antibiotic concentration. The printed mass range (0.4–5 g) is not mapped to each isotherm point, so the reported values cannot be independently mass-balance checked. The model-derived values are not conventional Langmuir qmax.

### Paper 3 — high-processing chitosan/TiO2@MWCNT / ciprofloxacin
The process includes DMF, solvothermal treatment at 190 °C for 24 h, washing and drying. BET area is reported as 236.45 m²/g and preparation cost as about US$450/kg. RSM text's stated optimized condition (pH 7, 0.03 g, 15 wt% MWCNT) is kept separate from a tabulated 96.11% actual CIP-removal run at pH 7, 0.05 g, 15 wt%. Fig. 8 legend labels CIP initial concentrations as mg/g while the prose/Table 6 use mg/L. Table 6 reports Qe 365 mg/g at stated 100 mg/L CIP; with a stated 0.03 g dose, the exact volume must be checked to validate mass balance. Table 7 gives CIP Langmuir qmax 2040.8 / 1510.5 / 1072.9 mg/g at 298 / 308 / 323 K, whereas abstract/conclusion highlight 1510.5 mg/g; table Qe at 323 K (2052.8 mg/g) exceeds its fitted qmax (1072.9 mg/g). These values are on hold for capacity ranking. Eight-cycle reuse retains >75% removal according to the paper; no actual wastewater validation was identified.

## Eligibility and citation controls
All three papers are provisionally retained as primary adsorption evidence, but no Q1/eligibility decision is made here. The agreed provider/year/category ranking rule must still be applied. No Zotero/Better BibTeX key has been invented. The evidence points to the uploaded PDFs and exact page/table/figure locations; actual citation-key mapping waits for the Zotero export.

## Central consolidation checklist
1. Check that these proposed candidate IDs are still free before allocating stable IDs.
2. Merge staging rows only after schema and duplicate checks; preserve all caveats.
3. Update the shared tracker for BATCH-06 centrally.
4. Audit journal quartile and publication-year/category eligibility separately.
5. Keep the capacity and thermodynamic claims flagged for follow-up before comparative synthesis.
