# Unique JEM upload set — intake log (2026-10-28)

## Upload receipt and existing pool matches

| Uploaded filename | Paper | DOI | Planned-pool match |
|---|---|---|---|
| `1-s2.0-S0301479724039392-main.pdf` | Raissouni et al. (2025), “Sulfadiazine removal with low-cost structured nano and micro-composite hydrogel beads on moroccan clays with alginate–CMC–biochar” | `10.1016/j.jenvman.2024.123952` | `POOL-148` |
| `1-s2.0-S0301479725033651-main.pdf` | Speksnijder et al. (2025), “Biochar potential for long-term pharmaceutical remediation in flow-through tertiary wastewater systems” | `10.1016/j.jenvman.2025.127389` | `POOL-152` |
| `1-s2.0-S0301479726002021-main.pdf` | Pereira et al. (2026), “Removal of sulfamethoxazole at relevant concentrations from wastewater by a magnetic regenerable waste-based activated carbon” | `10.1016/j.jenvman.2026.128742` | `POOL-081` |

## Why a unique upload label was used

Existing staging files were already present for `BATCH-01` and `BATCH-06` and contained different papers from other chats. Since multiple branched chats were active, numbered batch IDs were not safe to infer; no existing staging file was overwritten. This upload uses the unique path prefix `UPLOAD-JENV-20261028`. The central consolidation step must map this upload set to the appropriate row in `data/new-paper-upload-batch-tracker.csv` after confirming which numbered chat this conversation represents.

## Deduplication
- Exact DOI checks against `data/corpus-screening-register.csv` and `data/corpus-evidence.csv` found no active candidate/evidence record for these three works.
- All three are listed in `data/planned-download-pool.csv` under POOL-148, POOL-152 and POOL-081.
- Proposed candidate IDs use a unique upload-set prefix, not permanent IDs. No master evidence, screening, adjudication, quartile or batch-tracker file has been edited.

## Paper 1 — Raissouni et al. (2025)
- Scope: direct batch SDZ adsorption/desorption on two natural Moroccan clays and alginate/CMC/biochar hydrogel composites.
- Conditions: 0.5 g sorbent/10 mL, 24 h, 25±2 °C, 0–40 μmol/L SDZ, 0.005 M CaCl2. Biochar preparation is summarized in the main text as Mentha pulegium plant residue after essential-oil extraction, 550 °C/2 h, minimal oxygen.
- At 40 μmol/L the article reports SW 173.89 μmol/kg (21.7%); NSW 110.64 (13.83%); SW+AL 250.52; SW+AL+BC 237.88; NSW+AL 431.94 (53.99%); NSW+AL+BC 171.14; NSW+AL+CMC 387.25; SW+AL+CMC 800 μmol/kg (100%).
- Caveat: abstract says >100%, while method/results imply 100%. 40 μmol/L × 10 mL = 0.4 μmol; divided by 0.0005 kg = 800 μmol/kg. Thus 800 matches the complete starting solute inventory and is not evidence of a fitted saturation qmax. Conclusion's 'desorption less than 0%' wording is inconsistent with 0%/3.51%.
- Main PDF fully read (11 pages); selected figures on PDF pp. 5–8 rendered and visually checked. SI was not supplied.

## Paper 2 — Speksnijder et al. (2025)
- Scope: five-biochar packed-bed test on actual tertiary effluent, ~45 weeks and ~635 bed volumes at 12 mL/h; two regimes included 16 spiked pharmaceutical targets (100 μg/L) and 42 non-spiked targets.
- Antibiotic subset: main text identifies erythromycin, clindamycin and clarithromycin; Fig. 4 plots erythromycin breakthrough for SW and PS. Exact antibiotic fit parameters are in SI Table S5, not supplied.
- Aggregate result: SS and FB reported as high-retention char types; SP had complete breakthrough around 20 BV. Do not call the aggregate pharmaceutical result an antibiotic-only result.
- Caveats: authors' “>99% removal” is paired with `C/C0 > 0.01`, a sign inconsistency. Biofilm-associated biodegradation, fluctuating influent concentrations, competition and desorption/leakage may alter measured C/C0, so concentration decline cannot be attributed solely to adsorption.
- Main PDF fully read (11 pages); Fig. 4 on PDF p. 7 rendered and visually checked. SI was not supplied.

## Paper 3 — Pereira et al. (2026)
- Scope: SMX adsorption at 0.02–1 mg/L on KOH-activated magnetic paper-mill-sludge carbon (not pristine biochar). Preparation: KOH:sludge 1:5 w/w, 800 °C/20 min microwave pyrolysis, 1 M HCl wash, PAC:iron oxide 3:1 w/w.
- Batch tests: 250 mL, 25 °C, 500 rpm, triplicate. At 0.05 mg/L SMX, dose is 1 mg/L in ultrapure water vs 65 mg/L in effluent; equilibrium ~180 vs 60 min and experimental qe 20.3±0.8 vs 0.25±0.01 mg/g. Isotherms use 0.02–1 mg/L, 3 h contact.
- Langmuir qmax 54±2 mg/g (ultrapure) vs 6.2±0.3 mg/g (effluent); derived Kd 1296±170 vs 9.3±0.8 L/g. The effluent isotherm lacks a clear plateau, so qmax is model-derived. Authors' stated 83% decrease does not match 54→6.2 mg/g (about 88.5%); source arithmetic caveat preserved.
- Effluent was filtered 0.45 μm, pH 8.2, DOC 10.4±0.1 mg/L, one WWTP campaign. Regeneration is microwave 700 °C/20 min/N2; effluent removal 41±2% fresh and 26±6% at Regen-2; further cycles severely reduce surface area/porosity. The broad conclusion of satisfactory performance through two cycles is reported alongside this decline, not silently reconciled.
- No LCA/techno-economic assessment was performed in this paper; authors list these as future work. Main PDF fully read; Table 2 and figures on PDF pp. 5, 7–8 rendered/visually checked. SI not supplied.

## Output files
- `data/batch-extractions/upload-set-jenvman-20261028-evidence.csv`: 18 source-linked evidence/caveat rows using the master evidence schema.
- `data/batch-extractions/upload-set-jenvman-20261028-screening.csv`: three provisional screening records using the master register schema.
- `logs/2026-10-28-upload-set-jenvman-20261028-intake.md`: this log.

## Status / unresolved
- Full-text PDFs read: 3/3, each 11 pages; figures relevant to key claims were rendered and inspected.
- All three matched the planned download pool, none matched an active master candidate/evidence row, and no master table was updated in this upload set.
- Journal quartile for all three: not audited. Apply the agreed provider/year/category rule separately; do not infer Q1.
- Zotero/Better BibTeX keys: pending actual Zotero export; none invented.
- Central consolidation must assign stable candidate/evidence IDs, merge validated rows and map this unique upload set to the correct batch tracker row.
- `DISC-022` remains untouched and deferred until its full-text PDF is supplied.