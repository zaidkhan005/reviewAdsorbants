# BATCH-05 intake and evidence extraction — 2026-10-28

## Scope and collision guard

This chat's three PDFs are staged as **BATCH-05** because shared GitHub already contained batch staging outputs for BATCH-01 through BATCH-04 with different files. Their files were left untouched. Candidate IDs are branch-specific proposed IDs (`PROPOSED-BATCH-05-PAPER-01` to `-03`); the central consolidation chat must allocate stable global IDs after checking all batches. No shared master evidence, screening, quartile or tracker file was edited from this branch.

## Uploaded files and matching

| Paper slot | Uploaded filename | Paper / DOI | Planned-pool match | Current screening-register match |
|---|---|---|---|---|
| Paper 1 | `1-s2.0-S0048969722069157-main.pdf` | Du et al. (2023), *A review of antibiotics and antibiotic resistance genes (ARGs) adsorption by biochar and modified biochar in water*, Science of the Total Environment 858, 159815. DOI 10.1016/j.scitotenv.2022.159815 | POOL-091 | No exact DOI/title record found |
| Paper 2 | `1-s2.0-S0048969723056309-main.pdf` | Nguyen et al. (2023), *Sorption of oxytetracycline to microsized colloids under concentrated salt solution: A perspective on terrestrial-to-ocean transfer of antibiotics*, Science of the Total Environment 905, 167005. DOI 10.1016/j.scitotenv.2023.167005 | POOL-107 | No exact DOI/title record found |
| Paper 3 | `1-s2.0-S0141813019347282-main.pdf` | Soares et al. (2019), *Magnetic nanosorbents with siliceous hybrid shells of alginic acid and carrageenan for removal of ciprofloxacin*, International Journal of Biological Macromolecules 139, 827–841. DOI 10.1016/j.ijbiomac.2019.08.030 | No exact title/DOI match found | No exact DOI/title record found |

## Paper-by-paper outcome

### 1. Du et al. (2023) — review

Provisional role is review-level mapping and citation discovery only. The abstract (PDF p. 1) covers biochar/modification, antibiotics and ARGs, molecular imprinting and aging, influencing factors, mechanisms and challenges. The contents (PDF p. 2) lists π–π electron-donor–acceptor interactions, electrostatic interaction, surface complexation, pore filling, hydrophobic interaction, hydrogen bonding and ion exchange; pH, temperature, initial concentration and coexisting substances are covered as factors.

Do not use this review as the original support for any capacity number. Trace numeric claims to the cited primary paper. Antibiotics and ARGs must remain distinct targets.

### 2. Nguyen et al. (2023) — OTC and mineral colloids under salinity

Provisional role is solution chemistry, clay/mineral interaction and environmental fate, not a conventional engineering adsorbent ranking.

Methods (PDF p. 2) describes suspensions at 1000 mg/L mineral solids and OTC at 0, 5, 10 and 20 mg/L with pH varied and ionic strength held at 0.01 M for surface-charge measurements. The salinity test used 0 or 10 mg/L OTC, deionized/fresh/brackish/seawater NaCl conditions of 0/0.035/0.35/3.5%, near-neutral pH and transmittance tracked for 6 h (PDF p. 2; Fig. 2, PDF p. 4).

The paper reports mineral-dependent surface-charge changes and proposes that high salinity alters aggregation and can promote release of sorbed OTC by competing at mineral exchange sites. This may support the manuscript's solution-chemistry/environmental-fate discussion but should not be used as an adsorbent qmax comparator.

**High-priority source caveat:** the abstract states a sorption-capacity order illitic > kaolinitic > lateritic soil clay; the bars in Fig. 2(c), visually inspected, appear to show kaolinitic > illitic > lateritic in both deionized water and seawater. Also, the main-text Methods do not clearly specify the direct assay/calculation behind the mg/kg bars; supplementary Table S1 is referenced but was not supplied. No exact bar values were extracted and no capacity ranking is accepted pending supplementary-source checking.

### 3. Soares et al. (2019) — magnetic alginate/carrageenan-silica nanosorbents for CIP

Provisional role is primary adsorption evidence for chemically modified biopolymer-based magnetic nanocomposites; it is not evidence for raw/unmodified biopolymer.

Preparation uses magnetite, silica (TEOS) and derivatized polysaccharides; alginic acid is first modified with tributylamine, and the polysaccharide derivative is coupled using ICPTES (PDF pp. 2–3). Table 1 (PDF p. 5) reports 50 ± 8 nm magnetite cores, shell thicknesses of 15 ± 2 nm (alginate-derived), 7 ± 1 nm (ι-carrageenan-derived) and 23 ± 3 nm (κ-carrageenan-derived), and BET areas 34.4, 16.1, 24.7 and 26.3 m²/g for bare magnetite, alginate-derived, ι-carrageenan-derived and κ-carrageenan-derived particles respectively.

- **pH profile:** at 50 mg/L CIP and 24 h, ι-carrageenan-derived particles reached about 95% removal at pH 3; alginate-derived particles reached about 85% near pH 5; κ-carrageenan-derived particles removed about 20% at pH 3 (PDF p. 7, Fig. 3).
- **Contact time:** 5 mg sorbent in 10 mL at 50/100/200 mg/L initial CIP, pH 5, 25 ± 2 °C and 30 rpm. Carrageenan-based particles reached a plateau after about 30 min; alginate-based particles required about 5 h at the lowest concentration and up to 24 h at higher concentrations (PDF pp. 3, 8; Fig. 4).
- **Fitted capacities:** isotherms used 1.5 mg sorbent in 3 mL, 50–1200 mg/L initial CIP, pH 5, 25 °C and 24 h. Table 2 gives 463.7 mg/g for alginate and 426.6 mg/g for ι-carrageenan as Langmuir qmax values; for κ-carrageenan it gives 1350.1 mg/g, and the body reports the Dubinin–Radushkevich model fit best (R² = 0.9694; Langmuir/Freundlich R² < 0.9) (PDF pp. 9–10 and 12, Table 2).
- **Reuse:** four adsorption/desorption cycles with 1 M KCl; alginate/ι-carrageenan cycle capacities are reported around 99–96 mg/g in cycle 1 and 97–90 mg/g after cycle 4, while κ-carrageenan falls from 133 to 106 mg/g after the first regeneration and is 101 mg/g after four cycles (PDF p. 12, Fig. 6).

**High-priority caveats:** the abstract gives 423 mg/g for ι-carrageenan; main-results prose gives 427; Table 2 gives 426.6 mg/g. Table 2 is transcribed as printed, with the discrepancy preserved. κ-carrageenan's value is model-dependent and is not directly comparable to the Langmuir-fitted values for the other two materials. Initial feeds reach 1200 mg/L, so these fitted maxima should not be presented as low-environmental-concentration performance. The supplied main PDF uses prepared aqueous CIP solutions; it provides no real wastewater test, harmonized preparation cost or LCA. Supporting model/FTIR tables and figures are referenced but were not supplied.

## Staging outputs created

- `data/batch-extractions/batch-05-evidence.csv` — 15 source-pinned evidence rows.
- `data/batch-extractions/batch-05-screening.csv` — 3 provisional screening rows.
- `logs/2026-10-28-batch-05-intake.md` — this batch record.

The shared screening register, evidence master, quartile audit and batch tracker remain unchanged from this branch. Central consolidation must check all parallel batch outputs, allocate stable IDs, merge only after schema/DOI/candidate checks, and run separate journal-year/provider/category quartile audits. `DISC-022` remains deferred until the user provides its full text.
