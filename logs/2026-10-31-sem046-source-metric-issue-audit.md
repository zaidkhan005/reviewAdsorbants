# SEM-046 targeted source, issue-metadata and mechanism audit (2026-10-31)

## Candidate and primary source

Tegie, T. T., Workie, Y. A., Mekonnen, M. L. & Tessema, D. A. (2026). “Optimization of ciprofloxacin adsorption onto zirconium-modified magnetic graphene oxide: Response surface methodology.” *Bulletin of the Chemical Society of Ethiopia*, **40(5)**, 1147–1171. DOI: 10.4314/bcse.v40i5.15.

The existing AJOL-linked primary PDF text extraction was reused; no duplicate PDF/evidence extraction was created. The official AJOL article page and issue archive were checked again on 31 October 2026. Both identify Vol. 40 No. 5 (2026), and the DOI itself contains `v40i5`. AJOL records publication on 6 March 2026. The AJOL issue record is the canonical bibliographic metadata for this project.

- Official article record: https://www.ajol.info/index.php/bcse/article/view/318556
- Official issue record: https://www.ajol.info/index.php/bcse/issue/view/27293
- DOI: https://doi.org/10.4314/bcse.v40i5.15

## 1. Optimized synthetic-water point: mass balance

Source-stated optimized condition:
- C0 = 30 mg/L CIP
- V = 100 mL = 0.1 L
- adsorbent mass = 0.3 g (3 g/L)
- pH = 7
- contact time = 45 min
- stirring = 180 rpm.

Initial CIP mass = 30 mg/L × 0.1 L = 3 mg. The absolute feed-limited uptake ceiling is 3 mg / 0.3 g = **10 mg/g**.

The source reports 93.92% removal and separately associates the optimized point with qe = 20.11 mg/g. Applying the reported removal to the stated batch gives a derived qe of 3 × 0.9392 / 0.3 = **9.392 mg/g**. Thus, 20.11 mg/g cannot be the observed uptake for this same condition. Preserve both source-reported values, label 9.392 mg/g as a calculated mass-balance check, and hold 20.11 mg/g from quantitative use pending an author clarification or corrected source.

The paper reports Langmuir-fitted q_m = 313.48 mg/g (elsewhere 313.8 mg/g). This is a model-fitted parameter, not an observed qe. It must remain separate from the removal percentage and mass-balance calculation.

## 2. Real pharmaceutical-effluent arithmetic

The extracted primary PDF reports real-effluent CIP concentration changing from 8.37 mg/L to 2.01 mg/L, while the abstract/body elsewhere state 90.75% removal. The concentration pair gives:

`(8.37 - 2.01) / 8.37 × 100 = 76.0%`

The 76.0% result is calculated directly from the printed concentrations; it does not support 90.75% for that same sample pair. Retain the source's 90.75% claim as conflicting, but do not use it as a validated real-water performance endpoint. The study remains useful as a pharmaceutical-effluent application example because a real composite sample is described; the exact percentage needs clarification.

## 3. Reuse, model and cost boundaries

- Eight reuse cycles are reported. The abstract gives 85.45% after cycle eight, while the body reports 93.73% to 85.7%. Keep the abstract/body values distinct.
- Freundlich is reported as the better isotherm model and pseudo-second-order as the better kinetic model. The PSO fit does not prove chemisorption.
- No monetized synthesis cost, product yield, energy inventory, wash-water balance, solvent recovery or cost per mass CIP removed is reported.
- The preparation route includes Hummers GO chemistry, Fe/Zr precursors, heating, stirring/sonication, repeated washing and vacuum drying. Regeneration includes repeated DI-water, acetone and methanol rinsing. Do not convert the presence of waste-derived or magnetic materials into an assumed low-cost claim.

## 4. Mechanism evidence grade

The source reports pHpzc by salt-addition method, pH-dependent RSM experiments, and FTIR/XRD characterization of GO oxygen functionality and Fe–O/Zr–O phases. Authors propose electrostatic, π–π and hydrogen-bond interactions. The current extracted evidence supports the relevance of pH/surface chemistry and makes those pathways plausible, but does not quantify their contributions or prove one unique/dominant mechanism.

**Grade: M1 — plausible multi-pathway interpretation; evidence supportive but non-exclusive.** Do not infer chemisorption from a pseudo-second-order fit alone. Preserve the separate mass-balance caveats when interpreting the response data.

## 5. Journal issue / PDF visual-verification discrepancy

The existing parsed PDF text reported an internal running footer “40(6)” on some pages, while the AJOL article page, official Vol. 40 No. 5 issue listing, article page range and DOI all identify **40(5)**. The exact AJOL PDF route was retrieved from the page's Download PDF control:
https://www.ajol.info/index.php/bcse/article/download/318556/299750

The download endpoint returned an application/pdf response with HTTP 200 in the browser-interaction check. However, the dedicated web PDF viewer returned HTTP 403 when opened, so I could not perform the required visual screenshot check of the PDF footer in this session. Keep the “40(6)” text extraction note as an unverified internal running-footer discrepancy; do not change the bibliographic citation to issue 6. Canonical citation remains 40(5), 1147–1171.

## 6. Zotero / citation status

The latest uploaded `full ++ check again(1).bib` file was directly inspected again: 173 BibTeX entries were detected, but no record contained DOI 10.4314/bcse.v40i5.15. The existing candidate-level citation-linkage row also records no exact DOI/title match. No Better BibTeX key was guessed and no manuscript citation was inserted. SEM-046 remains a candidate/evidence record until selected for citation and a real Zotero key is available.

## Repository changes

Updated without creating a duplicate evidence ID:
- `data/semester-mechanism-evidence-matrix.csv`: SEM-046 mechanism grade adjusted to M1.
- `evidence/semester-paper/SEMESTER_CORE_EVIDENCE_EXTRACTION.csv`: EV-SEM-042 source, issue and mechanism caveats expanded.
- `data/semester-evidence-readiness-audit.csv`: metric conflicts, issue metadata and remaining citation step updated.
- `data/semester-condition-labelled-comparison.csv`: added a condition-labelled SEM-046 record with observed removal, derived qe, fitted q_m and real-effluent conflicts separated.
- `data/semester-remaining-work-register.csv`: scientific audit closed; citation remains pending and PDF footer visual check remains blocked.
- `data/semester-paper-candidate-register.csv`: disposition and next action updated.
- `README.md`: semester condition-labelled comparison count updated from 28 to 29.

Journal quartiles were not consulted or used for any SEM-046 decision.
