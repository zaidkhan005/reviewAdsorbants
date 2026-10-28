# BATCH-02 intake and evidence extraction — 2026-10-28

## Scope and inputs

This chat received three main-text PDFs and read the full text of each. BATCH-01 is already assigned to another chat for different papers; these uploads are recorded as **BATCH-02** to avoid overwriting that work.

| Slot | Uploaded filename | Paper / DOI | Planned pool match | Existing screening-register match |
|---|---|---|---|---|
| Paper 1 | `1-s2.0-S0013935121003856-main.pdf` | Ashiq et al. (2021), “Carbon-based adsorbents for fluoroquinolone removal from water and wastewater: A critical review,” *Environmental Research* 197, 111091. DOI `10.1016/j.envres.2021.111091`. | POOL-115 | No exact DOI/title record found |
| Paper 2 | `1-s2.0-S0013935122002560-main.pdf` | Hamadeen & Elkhatib (2022), “New nanostructured activated biochar for effective removal of antibiotic ciprofloxacin from wastewater: Adsorption dynamics and mechanisms,” *Environmental Research* 210, 112929. DOI `10.1016/j.envres.2022.112929`. | POOL-088 | No exact DOI/title record found |
| Paper 3 | `1-s2.0-S0013935122009483-main.pdf` | Cela-Dablanca et al. (2022), “Potential of low-cost bio-adsorbents to retain amoxicillin in contaminated water,” *Environmental Research* 213, 113621. DOI `10.1016/j.envres.2022.113621`. | POOL-124 | No exact DOI/title record found |

These titles and DOIs matched rows in `data/planned-download-pool.csv`, but no exact match was found in `data/corpus-screening-register.csv`. The planned-pool download/upload status must be updated centrally after consolidation; this batch branch does not edit shared master/tracker files.

## Paper 1 — Ashiq et al. (2021): critical review

**Provisional role:** supporting review and citation-discovery source, not a primary adsorption study. The abstract and conclusions identify π–π electron donor–acceptor interactions, electrostatic interactions and pore filling as prominent mechanisms across the reviewed carbon/clay literature, and state that graphene had the highest performance within the review's assembled comparison. It also discusses partition coefficient alongside adsorption capacity.

The review's Tables 3–6 (PDF pp. 5, 8–10) provide useful source discovery across activated carbon, biochar, graphene and CNTs. Values from these tables must be traced to original papers before adding any numeric row to the primary-study comparison matrix; the review's rankings are not a common-condition experiment.

**Evidence staging rows:** STAGE-BATCH-02-P1-E01–E02.

## Paper 2 — Hamadeen & Elkhatib (2022): phosphoric-acid-activated nanosized pomegranate-peel biochar

**Provisional role:** retain as primary adsorption evidence. This is a chemically activated/nanosized biochar, not pristine biochar. Preparation starts with washed/dried pomegranate peel, 800 °C pyrolysis for 2 h and a reported 78% pre-activation char yield; subsequent processing includes 85 wt% H3PO4 activation, additional 800 °C treatment, washing/drying and ball milling to <100 nm. Reported BET area is 1149.62 m²/g. Langmuir-fitted CIP qmax is reported as 142.86 mg/g.

**Caveats kept visible:**
- Bulk comparator qmax differs across the paper: 5.32 mg/g in Table 1 vs 5.92 mg/g in Table 4.
- Time statements do not align: text selects 90 min as optimum, discusses equilibrium at 240 min, and Table 4 lists 420 min for the conditions associated with the qmax value.
- Removal in filtered, CIP-spiked wastewater (89.94% batch; 84.74% packed bed) is lower than in CIP-spiked distilled water (96.31%; 94.39%). This is not native-antibiotic monitoring in untreated wastewater.
- After five adsorption cycles, the paper reports 81.27% removal and approximately 15% CIP released in the desorption test.
- Supplementary material referenced by the paper was not among the uploads, so detailed wastewater/analytical information is not all available here.

**Evidence staging rows:** STAGE-BATCH-02-P2-E01–E04.

## Paper 3 — Cela-Dablanca et al. (2022): low-cost amoxicillin biosorbents

**Provisional role:** retain as primary batch adsorption/desorption evidence for low-cost forestry/food-industry by-products. Tests use 0.5 g sorbent in 10 mL solution with 0.005 M CaCl2, nominal added AMX concentrations 2.5–50 μmol/L, 48 h in dark, triplicate measurements. The measured highest initial concentration in Table 1 is 52.07 μmol/L. The five sorbents have different native pH and chemical character.

At measured C0 = 52.07 μmol/L, Table 1 gives loading/removal: pine needles 1001.32 μmol/kg / 100%; wood ash 934.21 μmol/kg / 89.71%; eucalyptus leaves 762.56 μmol/kg / 76.15%; mussel shell 501.46 μmol/kg / 48.15%; pine bark 294.23 μmol/kg / 29.38%. These are observed values under one tested condition, not fitted qmax values. No release was detected in the reported desorption test at the maximum added concentration.

**Caveats kept visible:**
- The authors state the Langmuir model is invalid because fit errors are high; eucalyptus leaves and pine needles do not fit the listed models adequately. Do not force a single qmax ranking across all five sorbents.
- Pine-bark removal is non-monotonic: 38.73% at C0 = 38.62 μmol/L but 29.38% at C0 = 52.07 μmol/L.
- Mussel-shell pH appears as 9.39 in one discussion passage and 9.04 elsewhere in the main text. Supplementary Table S1, which is cited for characterization, was not supplied; do not silently reconcile it.

**Evidence staging rows:** STAGE-BATCH-02-P3-E01–E02.

## Screening and quartile status

- Paper 1 is a review for background/citation discovery, not an independent primary adsorption study.
- Papers 2 and 3 are provisionally relevant primary adsorption papers with the source caveats above.
- All three are in *Environmental Research*. This batch did **not** assign paper-level Q1 eligibility. During central consolidation, cross-check the existing journal audit against the agreed provider/year/category rule.
- Zotero/Better BibTeX keys were not invented; match against the user's actual library/export during citation conversion.
- Full article texts were supplied; supplementary materials referenced by papers 2 and 3 were not included in this upload.

## Staging files created

- `data/batch-extractions/batch-02-evidence.csv` — eight source-pinned evidence rows.
- `data/batch-extractions/batch-02-screening.csv` — three screening rows.
- This batch intake note.

All IDs remain provisional because candidate/evidence IDs are assigned centrally after cross-branch de-duplication. No shared master evidence, screening, decision, journal-quartile or batch-tracker file was edited here.

## Central consolidation checklist

1. Fetch this note and both staging CSVs; validate headers against current master files.
2. Recheck DOI/title against the latest screening register and any sibling branch staging rows.
3. Allocate final global candidate IDs; remap the provisional candidate/evidence IDs.
4. Merge into master screening/evidence without overwriting prior rows.
5. Update the shared tracker and planned-pool download/upload status centrally.
6. Audit Q1 eligibility and Zotero citation keys separately.
7. Keep DISC-022 deferred until the user supplies its full-text PDF.
