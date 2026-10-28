# BATCH-01 intake and evidence extraction — 2026-10-28

## Scope of this batch

Three newly uploaded main-text PDFs were fully read and checked against the current screening register and the planned download pool. No master evidence or screening CSV was changed from this batch context; this branch writes staging outputs for central consolidation.

## Uploaded files and matching

| Paper slot | Uploaded filename | Paper / DOI | Planned-pool match | Current screening-register match |
|---|---|---|---|---|
| Paper 1 | `1-s2.0-S002197971100631X-main.pdf` | Zhao et al. (2011), “Adsorption of tetracycline onto goethite in the presence of metal cations and humic substances,” DOI 10.1016/j.jcis.2011.05.051 | POOL-090 | No exact DOI/title record found |
| Paper 2 | `1-s2.0-S002197971530148X-main.pdf` | Peng et al. (2015), “Adsorption behavior and mechanisms of ciprofloxacin from aqueous solution by ordered mesoporous carbon and bamboo-based carbon,” DOI 10.1016/j.jcis.2015.08.050 | POOL-143 | No exact DOI record found; a generic title-substring false match to an unrelated record was rejected |
| Paper 3 | `1-s2.0-S004565352103928X-main.pdf` | Wang et al. (2022), “Two-step pyrolysis biochar derived from agro-waste for antibiotics removal: Mechanisms and stability,” DOI 10.1016/j.chemosphere.2021.133454 | POOL-164 | No exact DOI/title record found |

All three are original research articles with full main PDFs available. They were not treated as accepted Q1 sources; the relevant ranking system/year/category audit remains pending. The tracker should be updated only by the central consolidation chat.

## Staging records created

- `data/batch-extractions/batch-01-evidence.csv`: 15 source-linked evidence rows, using the current master evidence header and provisional IDs.
- `data/batch-extractions/batch-01-screening.csv`: one provisional screening row per paper, using the current screening-register header.
- This batch note records filenames, DOI/pool matches, findings, source caveats and next actions.

The candidate/evidence IDs use `PROPOSED-` / `STAGE-` prefixes intentionally. They must be assigned stable global IDs during central consolidation after checking sibling chat staging files; do not replace these prefixes independently in this branch.

## Paper 1 — goethite, TC, cations and humic acid

**Bibliography:** Zhao, Y., Geng, J., Wang, X., Gu, X., Gao, S. (2011). *Journal of Colloid and Interface Science* 361, 247–251. DOI 10.1016/j.jcis.2011.05.051.

**Provisional role:** Supporting/background mechanism source. The adsorbent is synthesized goethite (α-FeOOH), an iron oxyhydroxide mineral. This is not the same material as a natural clay and should not be placed in biomass-derived adsorbent rankings.

**Key extracted evidence:** BET surface area 63.53 m²/g and PZC ~8.2; batch setup uses 20 mg in 10 mL (2 g/L), TC 50 mg/L, 25 ± 0.5 °C and 24 h equilibrium for later experiments. Over 80% sorption occurs in the first 4 h; pseudo-second-order fitted (q_e=14.71) mg/g. Background Li+, Na+, K+, Ca2+ and Mg2+ at 0.01 M show little effect from pH 3–10; TC sorption rises from about 10 to 22 mmol/kg between pH 3 and 8. Cu2+ increases adsorption strongly: at pH 5.5, reported adsorbed TC rises from 16.2 mmol/kg without Cu to 30.4, 40.0 and 49.0 mmol/kg at 0.008, 0.040 and 0.100 mM Cu, respectively. HA at 5, 50 and 100 mg/L significantly enhances adsorption at pH <7, with the strongest response around pH 4.3; it has a slight effect above pH 7.

**Caveats:** The Cu-bridging and HA-bridging explanations are authors' mechanistic interpretations. This is a controlled synthetic-water study, with no real wastewater, column, regeneration or process-cost data.

## Paper 2 — ciprofloxacin on OMC and bamboo-based carbon

**Bibliography:** Peng, X., Hu, F., Lam, F. L.-Y., Wang, Y., Liu, Z., Dai, H. (2015). *Journal of Colloid and Interface Science* 460, 349–360. DOI 10.1016/j.jcis.2015.08.050.

**Provisional role:** Core adsorption study useful for comparing high-processing carbon routes, surface basicity, pH and ionic-strength effects.

**Key extracted evidence:** Four materials: virgin/modified bamboo-based carbon (BC) and virgin/modified ordered mesoporous carbon (OMC). BET areas are 509, 767, 1181 and 1746 m²/g; pHPZC values are 7.6, 8.5, 7.9 and 8.8 in that order. Isotherm tests used 30 mL CIP solutions at 20–100 mg/L and 0.03 g adsorbent. The source reports higher loading after ammonia treatment, and the fitted kinetic models are generally better described by pseudo-second-order fits. The source reports maximum adsorption around pH 6 and increasing adsorption with temperature between 25 and 45 °C; NaCl up to 1 M increases adsorption under the paper's test conditions, which the authors attribute partly to salting-out.

**Critical source caveats:** Table 5 reports Langmuir Qmax values of 153.17, 237.44, 281.47 and 369.34 mg/g, while the abstract/narrative/Table 6 report modified BC = 233.37 mg/g and modified OMC = 362.94 mg/g. This contradiction is preserved and the affected values are on HOLD for quantitative ranking. The paper's “virgin BC” was already phosphoric-acid impregnated (1:1) and heat-treated, so it is not untreated/raw bamboo charcoal. The kinetic-dose phrase is unclear in the text; the pH-study passage does not clearly restate the liquid volume, so certain reported capacity values need a mass-balance check. The study is lab water, not real wastewater; no regeneration or cost/LCA was identified in the main paper.

## Paper 3 — bagasse-derived biochar, SMX and TC

**Bibliography:** Wang, W., Kang, R., Yin, Y., Tu, S., Ye, L. (2022). *Chemosphere* 292, 133454. DOI 10.1016/j.chemosphere.2021.133454.

**Provisional role:** Core biochar study because it compares a low-temperature pristine reference with additional pyrolysis and washing/chemical-treatment routes, then reports matrix effects and reuse.

**Key extracted evidence:** PBC was made at 350 °C for 1 h under N2; BC was further pyrolysed at 950 °C for 3 h; BCA used a 60% acetone wash before 950 °C/3 h pyrolysis; BCN is BCA washed with 30% nitric acid. The text reports SMX maximal capacities for PBC/BC/BCA/BCN as 6.58/56.41/247.84/274.63 mg/g, and TC as 8.81/67.3/331.91/353.85 mg/g. Tests used 25 mg in 50 mL (0.5 g/L), initial concentrations 50–350 mg/L and pH tests spanning 2–8; HA was tested at 0.05–1.0 g/L. Filtered FuRong Lake freshwater and Baicheng Beach seawater were used as water matrices (0.22-µm filter). HA/real-water matrices reduced SMX adsorption by more than half but slightly enhanced TC adsorption. After four cycles without regeneration, capacity decreased by no more than 5%; separate solvent-regeneration tests used 80% methanol, 15% acetone and 5% acetic acid. Fourth-cycle removal efficiencies after regeneration are reported as BCA 23.52% (SMX)/29.87% (TC), BCN 29.73% (SMX)/32.11% (TC).

**Critical source caveats:** Supplementary Fig. S1a and Tables S1/S3/S4 are referenced but were not supplied, so the reported maximal capacities should not be silently labelled fitted Langmuir (q_{max}), and kinetic/model details remain pending. Real-water tests are filtered freshwater and seawater, not municipal wastewater or a native-contaminant removal study. The work is batch-only and the authors explicitly call for column studies. No cost/LCA is established in the main PDF.

## Consolidation and next actions

1. In the master chat, check that no other concurrently active branch staged the same DOIs before allocating stable candidate and evidence IDs.
2. Merge the evidence and screening staging rows only after schema validation. Keep the goethite paper as contextual/mechanism evidence unless the review scope explicitly covers mineral oxides.
3. Obtain supplementary files for the 2022 Chemosphere paper if available, especially Fig. S1a and Tables S1/S3/S4, before using its capacity values as model-fit parameters.
4. Resolve the 2015 paper's Table 5 vs abstract/body/Table 6 qmax conflict before any numeric rank. Also verify the ambiguous kinetic dose and pH-test liquid volume.
5. Add all three new journal records to the central quartile audit only during consolidation, with provider/system, publication year and relevant subject category verified separately.
6. Do not invent Better BibTeX keys; all three Zotero-key matches remain pending until a fresh Zotero export is available.
7. `DISC-022` remains deferred, not screened or excluded, until the user provides its full text.
