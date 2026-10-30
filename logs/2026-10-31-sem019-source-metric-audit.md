# SEM-019 targeted source and metric audit (2026-10-31)

## Candidate and source

SEM-019 — Lily et al., “EDTA-functionalized magnetic graphene oxide for rapid and efficient removal of tetracycline from aqueous media,” *Desalination and Water Treatment* 328 (2026), 101889. DOI: 10.1016/j.dwt.2026.101889. The full article text was inspected from the ResearchGate-hosted full-text copy, with title/abstract/data-availability metadata cross-checked against the official Elsevier ScienceDirect record. The publisher record identifies the article as open access and reports the same headline outcome and model claims.

## 1. Initial concentration / solution-volume basis

Methods §2.7 (printed pp. 3–4) state a total solution volume of 20 mL, prepared using 18 mL DI water plus 2 mL TC stock solution to achieve final initial concentrations from 0.2 to 5 mg/L. Thus the 0.2 mg/L value is the stated prepared initial concentration, not a 2 mL stock concentration to be diluted again by a factor of ten.

At the Figure 3 / Fig. 4 conditions:
- C0 = 0.2 mg/L
- V = 20 mL = 0.020 L
- adsorbent dose = 0.10 g/L, so m = 0.002 g
- pH = 5; T = 25°C; agitation = 250 rpm
- contact time = 5 min for the 93.23% removal optimum; Fig. 4 kinetics cover 1–60 min under the same C0/dose/pH/T/agitation basis.

Available TC mass = 0.2 mg/L × 0.020 L = 0.004 mg. The absolute feed-mass ceiling is 0.004 mg / 0.002 g = **2.0 mg/g**. The reported 93.23% removal implies a derived uptake of (0.2 × 0.020 × 0.9323) / 0.002 = **1.8646 mg/g**. This is a calculation from the reported removal and stated condition; it is not a source-reported experimental qe.

## 2. Kinetic model integrity

Table 2 (printed p. 8) reports:
- Pseudo-first-order fitted qe = 3.65672 mg/g; k1 = 0.0266 min−1; R² = 0.62776.
- Pseudo-second-order fitted qe = 0.01937 mg/g; k2 = 0.50176 g mg−1 min−1; R² = 1.
- Elovich and Weber–Morris parameters are also reported.

The Fig. 4 caption confirms the kinetic curves use mGO/EDTA = 0.1 g/L, t = 1–60 min, pH = 5, C0 = 0.2 mg/L, T = 25°C and 250 rpm. On this stated basis, the PFO fitted qe exceeds the 2.0 mg/g feed ceiling, while the PSO fitted qe is about 96 times lower than the removal-derived ~1.865 mg/g. The high PSO R² does not make its fitted qe physically consistent and does not establish chemisorption. Preserve both fits as source-reported model outputs; do not invent a corrected value or use them as measured uptake.

The article's Data availability statement says: “The authors do not have permission to share data.” The discrepancy cannot be reconstructed from the underlying raw measurements using the materials available for this audit.

## 3. Isotherm-model selection

Table 3 (printed p. 9) reports:
- Langmuir: qmax = 31.32 mg/g, R² = 0.69125 at 25°C; 28.22 mg/g, R² = 0.4795 at 35°C; 10.79 mg/g, R² = 0.98312 at 45°C.
- Freundlich: R² = 0.94957 at 25°C; 0.87252 at 35°C; 0.79037 at 45°C.

Freundlich has the higher reported R² at 25°C and 35°C, but Langmuir has the higher R² at 45°C. The abstract and discussion describe Freundlich as the best overall model. Preserve the temperature-specific table results and qualify the blanket summary. The 25°C Langmuir qmax=31.32 mg/g comes from a weak fit (R²=.69125) and is not a robust best-fit capacity. Do not use it as an observed or condition-matched uptake.

## 4. Mechanistic interpretation

- pHpzc = 4.1, determined by solid addition in 0.01 M KCl (Methods/§3.1.3, printed p. 4).
- TC is described by the authors as cationic below pH 3.3, zwitterionic from pH 3.3–7.68 and anionic above pH 7.68. The optimum pH is 5, where their own assignment makes TC predominantly zwitterionic while mGO/EDTA is slightly negatively charged.
- The prepared composite FTIR spectrum identifies oxygen- and nitrogen-containing groups. XRD/SEM/EDX support GO/Fe3O4/EDTA composite formation. The inspected paper does not show post-adsorption FTIR/XPS evidence that directly identifies the TC-bound groups or quantify the contribution of individual pathways.
- Hydrogen bonding, π–π association, Fe-site complexation/bridging, electrostatic effects and pore/physical adsorption remain plausible author-proposed contributors; their individual shares are not established.
- Grade this source **M1**: the pHpzc and pH-response data support pH relevance, but the molecular mechanism is interpretive. Do not convert PSO R²=1 into proof of chemisorption.

## 5. Recovery, cost and data transparency

The authors report eight adsorption–desorption cycles with removal declining from about 94% to 90.50%. Recovery is by magnetic separation, three methanol washes under ultrasonic agitation, and drying at 60°C. This should be described as author-reported laboratory reuse, not a monetized regeneration process. No normalized cost, yield, energy or solvent-recovery inventory is provided. Data availability: authors do not have permission to share the data.

## Repository changes

Updated, without creating a new evidence ID:
- `data/semester-mechanism-evidence-matrix.csv`: new SEM-019 M1 mechanism row.
- `evidence/semester-paper/SEMESTER_CORE_EVIDENCE_EXTRACTION.csv`: EV-SEM-028 source, model and mechanism caveats expanded.
- `data/semester-evidence-readiness-audit.csv`: EV-SEM-028 quantitative hold and permitted use updated.
- `data/semester-condition-labelled-comparison.csv`: SEM-019 condition and model caveats updated.
- `data/semester-remaining-work-register.csv`: targeted data QA closed; remaining citation status remains pending actual Zotero Better BibTeX key.
- `data/semester-study-inclusion-shortlist.csv`: numeric use and remaining action aligned to source audit.

## Scope boundary

SEM-019 is not among the 15 primary-study citations in the current integrated manuscript. It remains a candidate/evidence record only until selected for citation and a verified Better BibTeX key exists. It has not been added to the curated manuscript bibliography. Journal quartiles were not consulted or used.
