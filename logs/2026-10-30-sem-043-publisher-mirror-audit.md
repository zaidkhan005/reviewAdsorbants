# SEM-043 publisher-preview and full-text-mirror audit — 2026-10-30

## Candidate

**SEM-043:** Chen, H., Gao, B. & Li, H. (2015). “Removal of sulfamethoxazole and ciprofloxacin from aqueous solutions by graphene oxide.” *Journal of Hazardous Materials* 282, 201–207. DOI: [10.1016/j.jhazmat.2014.03.063](https://doi.org/10.1016/j.jhazmat.2014.03.063). PMID: 24755346.

**Semester-paper scope:** retain CIP results only. SMX is a distinct co-target and its metrics must not be pooled with CIP.

## Source audit and provenance decision

### Official publisher and bibliographic records

- Official ScienceDirect article preview: https://www.sciencedirect.com/science/article/pii/S0304389414002490
- PubMed record: https://pubmed.ncbi.nlm.nih.gov/24755346/
- ScienceDirect preview was fetched and inspected on 30 October 2026. It exposes metadata, abstract, introduction, selected section snippets (Materials, surface functional groups, Conclusion) and reference list. Its page explicitly offers access through an organization or purchase for the full article.
- The publisher independently confirms: journal/year/volume/pages and DOI; single-layer GO; manufacturer-reported Hummers preparation; 1–5 μm lateral diameter; 0.8–1.2 nm thickness; abstract maximum sorption capacities of 379 mg/g for CIP and 240 mg/g for SMX; electrostatic CIP interpretation; pH and ionic-strength effects; and CIP-induced GO aggregation at pH 2.
- PubMed independently confirms the bibliographic metadata and abstract-level findings.
- No author- or institutional-hosted full-text copy was located in the searches conducted for this audit.

### Non-publisher full-text mirror

- DockSci mirror of the 7-page in-press manuscript: https://d.docksci.com/removal-of-sulfamethoxazole-and-ciprofloxacin-from-aqueous-solutions-by-graphene_5ae44a5bd64ab21f94eddefe.html
- The mirror text contains the full in-press manuscript including Methods §§2.1–2.3, Results §§3.2–3.6, figures 2–7 and Table 1. It identifies the text as an ARTICLE IN PRESS copy.
- The mirror's abstract, article title, GO materials description and conclusions agree with the official publisher preview. This corroborates the transcription but does **not** make the mirror an official publisher or author source.
- Detailed experimental conditions and Table 1 values therefore remain **mirror-derived**. Do not describe these detailed values as independently verified from the final publisher PDF.

## CIP methods and conditions (mirror-derived)

### Kinetic experiment

- Vessel: 15 mL PTFE centrifuge tube.
- 5 mL GO suspension at 20 mg/L + 5 mL CIP solution at 20 mg/L, pH 5.
- After equal-volume mixing: final mixture contains 10 mg/L GO and 10 mg/L CIP.
- Sampling: 0.25, 0.5, 1, 2, 4, 8, 12, 24 and 48 h.
- CIP filtration: 0.1 μm PTFE membrane.
- The authors report CIP filter-system recovery of 93 ± 2% and state that filtered CIP concentrations were adjusted for all sorption experiments.
- Adsorption temperature is not stated in the manuscript text inspected.

### Isotherm experiment

- 5 mL GO at 20 mg/L + 5 mL CIP feed solutions at 1, 2, 4, 6, 8, 10 and 20 mg/L.
- pH 5; 48 h to reach equilibrium.
- Because the two solutions are mixed in equal volumes, final nominal CIP concentrations are half of the stated CIP feed-solution concentrations. Preserve the source's feed-solution basis when transcribing; do not silently relabel it as final C0.
- The highest CIP feed concentration (20 mg/L before mixing) becomes 10 mg/L in the 10 mL final mixture.

## Table 1: CIP-specific results (mirror-derived)

### Kinetic model fits

| Model | Parameter(s) | Fitted qe | R² |
|---|---|---:|---:|
| Pseudo-first-order | k1 = 0.894 h⁻¹ | 327 mg/g | 0.920 |
| Pseudo-second-order | k2 = 0.004 g mg⁻¹ h⁻¹ | 345 mg/g | 0.975 |
| Elovich | α = 5721 mg/g; β = 0.0243 mg/g | — | 0.978 |

These are **kinetic-model-fitted qe parameters**, not observed equilibrium uptake and not isotherm qmax.

### Isotherm model fits

| Model | Parameter(s) | Capacity parameter | R² |
|---|---|---:|---:|
| Langmuir | K = 1.04 L/mg | Smax = 379 mg/g | 0.968 |
| Freundlich | Kf = 182 (source units); n = 0.361 | No Langmuir-type saturation capacity | 0.996 |

The abstract's “maximum sorption capacity” of 379 mg/g corresponds to the **Langmuir-fitted Smax** in Table 1. The Freundlich model has the higher R² (0.996 vs 0.968); do not call Langmuir the best-fitting isotherm.

### Mass-balance plausibility check

For the kinetic run, the 5 mL CIP solution at 20 mg/L contains 0.10 mg CIP; the 5 mL GO suspension at 20 mg/L contains 0.10 mg GO. The finite-feed ceiling is therefore 0.10 mg / 0.00010 g = **1000 mg/g**. The kinetic fitted qe values of 327 and 345 mg/g do not exceed this ceiling.

For the highest isotherm feed (20 mg/L before equal-volume mixing), the same 0.10 mg CIP and 0.10 mg GO basis applies, giving the same nominal 1000 mg/g finite-feed ceiling. The fitted Langmuir Smax of 379 mg/g does not exceed this simple bound. This check does not establish that model fit extrapolation is experimentally observed uptake.

## CIP chemistry and qualitative results (abstract/publisher corroboration plus mirror detail)

- About 74% of total CIP removal occurred within the first hour; pseudo-equilibrium was approached around 48 h.
- At pH 2, CIP sorption declines and the spent GO suspension forms aggregates.
- At pH 9, CIP sorption remains strong; the mirror reports an approximately 18% decline relative to pH 5.
- Both NaCl and CaCl2 suppress CIP sorption, with stronger suppression at higher ionic strength. The mirror reports that 3 mM CaCl2 can depress CIP sorption comparably to 200 mM NaCl.
- Authors identify electrostatic attraction involving CIP and charged GO surface functional groups as the main CIP interaction. Treat this as the paper's interpretation, not a direct quantitative partition of binding forces.
- The mirror reports no adsorption–desorption regeneration cycles, no real-water or wastewater experiment, and no measured cost/yield/energy inventory. GO was purchased commercially; the Hummers preparation is a manufacturer-reported provenance, not a synthesis process costed by this study.
- Aggregation at pH 2 may assist separation/handling, but it is not evidence of regeneration or repeated-use performance.

## Decision for the semester paper

**Retain provisionally as a CIP-specific graphene oxide batch study.** Use it for condition-labelled discussion of pH/salt sensitivity and for a careful example of model/metric separation. Do not use a single 379 mg/g value as a general observed uptake or best-fit model ranking. Keep SMX entirely out of the CIP comparison.

**Evidence quality:** publisher-confirmed abstract/material/qualitative findings; mirror-derived methods/table detail. Not full-text publisher-verified. The next source upgrade requires the final publisher PDF or an author/institutional copy, not another copy of the same mirror.

## Repository updates

- Updated `data/semester-paper-candidate-register.csv` to split publisher-confirmed findings from mirror-derived detail.
- Updated `evidence/semester-paper/SEMESTER_CORE_EVIDENCE_EXTRACTION.csv` EV-SEM-022 with the official publisher URL and explicit provenance qualification.
- Updated `data/semester-evidence-readiness-audit.csv`.
- Updated `data/semester-study-inclusion-shortlist.csv`.
- Reused existing candidate SEM-043 and evidence ID EV-SEM-022. No duplicate candidate/evidence row created.
