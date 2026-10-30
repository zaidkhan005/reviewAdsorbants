# SEM-015 targeted source, mass-balance and mechanism audit (2026-10-31)

## Candidate and source

Sikri et al. (2025), “Graphene oxide/layered double hydroxide composite as highly efficient and recyclable adsorbent for removal of ciprofloxacin from aqueous phase,” *Frontiers in Nanotechnology* 7:1578620, DOI 10.3389/fnano.2025.1578620. The official Frontiers full text was inspected.

## 1. Headline condition and mass-balance check

Methods §2.5 (20 mL batch) defines CIP concentration and adsorbent dose in mg/L. The pH/dose/concentration studies report the key point at:
- C0 = 1 mg/L CIP
- solution volume = 20 mL
- GO–ZnAlNi LDH dose = 10 mg/L
- pH = 7
- contact time = 60 min
- stirring = 180 rpm.

The 20 mL batch therefore contains 0.020 mg CIP and 0.00020 g adsorbent. The feed-limited uptake ceiling is **100 mg/g**.

The reported removal is **84.84%**. Applying the paper's own (q=(C_0-C_t)V/W) equation gives a derived uptake of **84.84 mg/g**. This is calculated from removal, volume, concentration and dose; it is not separately measured as a reported qe.

## 2. Three different capacity numbers

The article presents three distinct figures around the same headline condition:
1. §3.2.1 reports **97.43 mg/g** alongside **84.84% removal** at pH 7. These two quantities are arithmetically inconsistent if they refer to the same C0, 20 mL solution and 10 mg/L dose; 97.43 mg/g would imply 97.43% removal under that basis.
2. Table 1 gives pseudo-first-order fitted (q_e=106.96) mg/g (R²=0.949). The abstract reports equilibrium capacity 106.97 mg/g.
3. Table 3 explicitly lists **106.9 mg/g** for the present GO–ZnAlNi LDH study at **1 mg/L CIP, 10 mg/L adsorbent, pH 7 and 60 min**. This is a comparison-table endpoint, not an isotherm-derived Langmuir (q_{max}).

The Table 1/abstract/Table 3 value of ~106.9–106.97 mg/g exceeds the **100 mg/g** feed ceiling under the condition explicitly identified in Table 3. The 97.43 mg/g prose value is below the ceiling but does not agree with 84.84% removal on the same stated basis. No defensible corrected capacity can be reconstructed from the article's published values. The only defensible performance endpoint to retain is **84.84% removal under the exact condition stated**; the derived ~84.84 mg/g can be shown solely as an arithmetic cross-check, never as a source-quoted measured qe. Keep all three source capacity values visibly distinct and excluded from quantitative capacity ranking.

## 3. Kinetics and isotherms

- Table 1 gives pseudo-first-order fitted qe=106.96 mg/g, R²=.949; Elovich R²=.945; intraparticle-diffusion R²=.88. The article says pseudo-second-order fit was poor. The ~106.96 mg/g value cannot be treated as measured uptake and exceeds the same-condition feed ceiling if it is intended for the 1 mg/L / 10 mg/L / pH7 / 60 min point.
- Table 2 (isotherms) reports Freundlich n=1.29, Kf=244.32, R²=.95 and Temkin R²=.90; the text says Langmuir did not fit significantly. Do not interpret the Freundlich fit alone as proof of a unique multilayer molecular mechanism.
- The article says the process appears to involve initial surface adsorption followed by pore diffusion. This is a descriptive transport interpretation, not evidence of one exclusive bond.

## 4. Mechanistic interpretation

The article provides before/after adsorption FTIR comparisons, pH-response measurements and a reported drop in BET surface area (36.069 to 31.836 m²/g) and pore volume (0.098 to 0.086 cc/g) after adsorption. Together these observations support a **M2 — supportive, convergent but non-exclusive** mechanism grade for CIP association with the composite.

The authors propose hydrogen bonding involving hydroxyl groups, possible π–π association, pH-dependent electrostatic contributions, pore/transport effects and possible LDH/metal-site interactions. Keep these as candidate pathways. FTIR changes do not quantify individual contributions or uniquely prove π–π bonding. The article places CIP in its zwitterionic region at pH 6.1–8.7; the pH-7 optimum therefore must not be reduced to a simplistic net-charge attraction explanation. The pH trend and spectral changes do not establish a single dominant mechanism or prove chemisorption.

## 5. Reuse and practical limits

The article reports five cycles, but CIP removal falls from **80.4% in cycle 1 to 27% in cycle 5**. The conclusion should not describe this as robust retained performance. The authors explicitly state that real-time wastewater/co-contaminant and scale-up testing, plus techno-economic/lifecycle assessment, remain necessary. No normalized process-cost inventory is reported. The source's data availability statement says original contributions are in the article/Supplementary Material and further inquiries can be directed to the authors; do not say that data are unavailable in this paper.

## Repository propagation

Updated without adding a new evidence ID:
- `evidence/semester-paper/SEMESTER_CORE_EVIDENCE_EXTRACTION.csv` — EV-SEM-005 capacity distinctions, feed ceiling, mechanism notes and reuse caveat.
- `data/semester-condition-labelled-comparison.csv` — separated removal-derived uptake, prose capacity and Table 1/Table 3 values.
- `data/semester-evidence-readiness-audit.csv` — removal-only use and all capacity holds.
- `data/semester-mechanism-evidence-matrix.csv` — SEM-015 M2 evidence grade and boundaries.
- `data/semester-remaining-work-register.csv` — targeted QA closed; citation key remains pending.
- `data/semester-paper-candidate-register.csv` — screening action refreshed.

## Citation status and scope

The paper is not among the 15 primary-study citations in the integrated manuscript. DOI lookup did not find a matching entry in the last checked 173-entry Zotero export, so no citation key was invented and no manuscript citation was inserted. Journal quartiles were not used.
