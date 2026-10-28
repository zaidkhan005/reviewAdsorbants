# Full-text extraction — Upload batches from 2026-10-28

## What was processed

Today’s uploaded PDFs were grouped into 11 staging sets under `data/batch-extractions/`. Source-pinpoint extraction records were created for each paper and consolidated into the project’s master evidence database. The original staging CSVs are retained unchanged so that all batch-level IDs and review notes remain auditable. This report includes the central candidate IDs and key source caveats for each paper; the CSVs hold the line-by-line evidence.

- **32 paper records** were registered with central candidate IDs **DISC-037–DISC-068**.
- **177 source-linked evidence rows** were consolidated into `data/corpus-evidence.csv`.
- The master screening, candidate-decision audit, adjudication and journal-quartile tables were updated in parallel.
- The staging-to-master mapping is preserved in `data/batch-extractions/consolidation-crosswalk-2026-10-28.csv`.

## Paper-by-paper extraction summary

The table below gives the identity and working treatment of every paper. Exact conditions, findings, page/table/figure pinpoints and caveats are in the linked master evidence rows and retained staging CSVs.

| Candidate | Paper / citation | Working treatment |
|---|---|---|
| DISC-037 | Sharma et al. (2024), polysaccharide-based magnetic hydrogels | Review only; use for taxonomy/citation chasing. It includes non-antibiotic pollutants in its summary tables; no review-level capacities count as primary measurements. |
| DISC-038 | Yan, Hu & Jing (2012), enrofloxacin sorption on smectite clays | Controlled model-clay sorption/speciation study. Freundlich (K_F) is not (q_{max}); supporting information was not supplied; not actual wastewater. |
| DISC-039 | Aristilde et al. (2016), tetracycline interlayer trapping in montmorillonite | Mechanistic model-clay study at controlled conditions and high feed concentration; interlayer expansion supports, but does not alone prove, the proposed mechanism. No column or regeneration study. |
| DISC-040 | Zhao et al. (2011), tetracycline on goethite with cations/humic substances | Contextual mechanism evidence; goethite is synthetic iron oxyhydroxide, not the core clay/carbon/biochar classes. No real-wastewater, regeneration or column test. |
| DISC-041 | Peng et al. (2015), ciprofloxacin on ordered mesoporous and bamboo-based carbons | Provisional core adsorption evidence; quantitative (q_{max}) values are on hold because the abstract/body/tables disagree. “Virgin” bamboo carbon was already acid-treated and pyrolysed. |
| DISC-042 | Wang et al. (2022), two-step pyrolysis agro-waste biochar | Provisional core biochar evidence. Key supplementary figures/tables are absent; headline capacities must not be automatically called fitted Langmuir (q_{max}). Tested lake water/seawater are not municipal wastewater. |
| DISC-043 | Ashiq et al. (2021), critical review of carbon-based adsorbents for fluoroquinolones | Review only; use for framework and citations, not as primary capacity measurements. |
| DISC-044 | Hamadeen & Elkhatib (2022), nanostructured activated biochar for ciprofloxacin | Provisional primary candidate; use only with original source pinpoints and its conditions/caveats. |
| DISC-045 | Cela-Dablanca et al. (2022), low-cost bio-adsorbents retaining amoxicillin | Provisional primary candidate; retain its material preparation and condition-specific limits. |
| DISC-046 | Poddar et al. (2023), techno-economic doxycycline recovery using rice-straw biochar | Cross-cutting processing/cost evidence; keep recovery endpoints separate from ordinary wastewater-removal studies. |
| DISC-047 | Conde-Cid et al. (2020), competitive adsorption/desorption of tetracyclines | Soil/bio-sorbent competitive-system evidence; do not rank directly against wastewater capacities. |
| DISC-048 | Minaei et al. (2024), acid-modified activated-sludge biochar for SMX/LIN | Modified biochar; preserve preparation conditions and single/binary-system distinctions. |
| DISC-049 | Putra et al. (2009), bentonite vs activated carbon for amoxicillin | Cross-material batch comparison. Fitted Langmuir capacities are distinct from kinetic (q_e); wastewater comparison is one high-concentration test. |
| DISC-050 | Shimabuku et al. (2016), biochar for SMX in multiple waters | Environmental-concentration real-matrix application evidence. `Dose75%` is a dose endpoint, not (q_{max}) or (q_e). |
| DISC-051 | Du et al. (2023), [paper as listed in Batch 05 screening CSV](../data/batch-extractions/batch-05-screening.csv) | Provisional primary candidate; inspect its master row and source-pinned evidence before quantitative use. |
| DISC-052 | Nguyen et al. (2023), [paper as listed in Batch 05 screening CSV](../data/batch-extractions/batch-05-screening.csv) | Provisional primary candidate; preserve metric/model differences recorded in the extraction. |
| DISC-053 | Soares et al. (2019), [paper as listed in Batch 05 screening CSV](../data/batch-extractions/batch-05-screening.csv) | Provisional modified-biopolymer/magnetic-material candidate; not a pristine biopolymer control. |
| DISC-054 | Ranjbari et al. (2020), TCMA-functionalized chitosan hydrogel beads | Modified biopolymer candidate; preserve preparation and source-level endpoint caveats. |
| DISC-055 | Bouaziz et al. (2023), bentonite–chitosan composite for antibiotics | Composite/clay candidate; quantitative use remains provisional pending cross-checks. |
| DISC-056 | Rostami et al. (2024), TiO₂@MWCNT-modified chitosan | Engineered nanohybrid candidate; dyes and antibiotics must remain distinct targets. |
| DISC-057 | Gu et al. (2007), tetracycline–humic acid complexation | Supporting solution-chemistry evidence, not a conventional solid-adsorbent capacity study. |
| DISC-058 | Masrura et al. (2022), antibiotics release during urine nutrient recovery with biochar | Relevant multi-solute matrix and desorption study; spiked/diluted urine conditions and preparation discrepancies remain explicit caveats. |
| DISC-059 | Alawa et al. (2025), agricultural-waste biochar for ciprofloxacin | Provisional primary biochar candidate; use extracted isotherm/kinetic/thermodynamic evidence with the recorded caveats. |
| DISC-060 | Xiang et al. (2022), lignin-impregnated biochar for tetracycline | Provisional biochar candidate; preserve feedstock-modification and matrix context. |
| DISC-061 | Zhao et al. (2023), alkaline-modified biochar for livestock wastewater antibiotics | Application candidate; retain livestock-wastewater context and source-specific values. |
| DISC-062 | Mohammadzadeh et al. (2025), pilot-scale magnetite–pine-bark adsorption | Pilot-scale wastewater evidence; keep real-effluent removal, material comparisons and biotoxicity endpoints distinct from batch (q_{max}). |
| DISC-063 | Thao et al. (2025), learning-assisted sorption of fluoroquinolones/sulfonamides on algal biochar | Provisional primary candidate; inspect source-specific conditions and avoid treating statistical associations as mechanisms. |
| DISC-064 | Ahmed et al. (2015), review of antibiotic removal from water/wastewater | Review only; background/citation discovery, not primary evidence. |
| DISC-065 | Chen et al. (2020), positively charged MnFe₂O₄@CAC hybrid | Engineered composite candidate; retain its specific adsorption-affinity interpretation and material-preparation context. |
| DISC-066 | Raissouni et al. (2025), sulfadiazine removal with clay/polymer/biochar hydrogel beads | Keep the reported mass-balance/“>100% adsorption” discrepancy explicit; stated solute inventory is not a validated fitted (q_{max}). SI was not supplied. |
| DISC-067 | Speksnijder et al. (2025), long-term pharmaceutical adsorption in flow-through tertiary wastewater | 45-week column application evidence. Biofilm/biodegradation may contribute; antibiotic-specific details in missing SI must not be invented. |
| DISC-068 | Pereira et al. (2026), magnetic regenerable sludge-derived activated carbon for SMX | Relevant low-concentration/filtered-effluent and regeneration evidence. Model-derived effluent capacity, reported arithmetic inconsistency and absence of LCA/TEA are retained caveats. |

## Batch mapping

| Staging set | Master candidate IDs | Evidence rows |
|---|---:|---:|
| Clay batch | DISC-037–DISC-039 | 10 |
| Batch 01 | DISC-040–DISC-042 | 15 |
| Batch 02 | DISC-043–DISC-045 | 8 |
| Batch 03 | DISC-046–DISC-047 | 15 |
| Batch 04 | DISC-048–DISC-050 | 15 |
| Batch 05 | DISC-051–DISC-053 | 15 |
| Batch 06 | DISC-054–DISC-056 | 18 |
| Chemosphere upload set | DISC-057–DISC-059 | 31 |
| Upload set A | DISC-060–DISC-062 | 16 |
| Upload set B | DISC-063–DISC-065 | 16 |
| JEnvMan upload set | DISC-066–DISC-068 | 18 |
| **Total** | **32 candidates** | **177** |

## Where the evidence lives

- **Structured record (for filtering, synthesis, and tables):** [`data/corpus-evidence.csv`](../data/corpus-evidence.csv)
- **Candidate metadata, provisional screening decisions and DOI mapping:** [`data/corpus-screening-register.csv`](../data/corpus-screening-register.csv)
- **Candidate audit / quantitative-use guardrails:** [`data/candidate-decision-audit.csv`](../data/candidate-decision-audit.csv)
- **Provisional scope and eligibility adjudication:** [`data/screening-decision-adjudication-v1.csv`](../data/screening-decision-adjudication-v1.csv)
- **Journal-ranking checks:** [`data/journal-quartile-audit.csv`](../data/journal-quartile-audit.csv)
- **Batch-level CSVs and full crosswalk:** [`data/batch-extractions/`](../data/batch-extractions/)

## Interpretation and safeguards

This is an **evidence extraction and consolidation record, not final inclusion approval**. Candidate records remain provisional. Journal Q1 eligibility is not inferred from journal prestige or a current quartile alone; it must match the requested ranking system, publication year and subject category.

Review articles are marked as background/citation-discovery sources and their reported tables are not treated as primary experimental measurements. Context-specific endpoints are kept separate: fitted isotherm (q_{max}), observed kinetic/equilibrium uptake, removal percentage, dose required for a target removal, column breakthrough/bed-volume results, and soil or other non-wastewater systems are not interchangeable. When a paper reports conflicting equations, conditions, captions, model fits or arithmetic, the source caveat is preserved rather than silently “corrected”. Missing supplementary information is not assumed available.

## Important correction to the repository layout

The evidence **was initially left only in the CSV staging directory**, which made it appear absent from the project’s main `evidence/` folder. This note fixes that discoverability gap. The evidence folder contains narrative, human-readable batch reports; `data/corpus-evidence.csv` remains the structured master database. Future PDF batches should update both: one narrative Markdown report under `evidence/` plus the corresponding source-pinned rows and crosswalk in `data/`.

## Status

- Structured rows merged: **177 / 177** (per the staged crosswalk).
- Candidate IDs assigned: **DISC-037–DISC-068**.
- Original staging records retained: **yes**.
- Final Q1 eligibility and manuscript inclusion decisions: **pending separate adjudication**.
