# First processing wave from the full BibTeX bibliography — 2026-10-29

## Why this note exists

The uploaded `full ++.bib` contains 164 bibliographic entries, but many had not been entered into the project screening register or evidence database. This note documents the first wave of remediation: eleven previously unregistered papers have now been added as provisional candidates `DISC-069` through `DISC-079`.

## What changed

- Added **11 candidate records** to `data/corpus-screening-register.csv`, `data/candidate-decision-audit.csv`, and `data/screening-decision-adjudication-v1.csv`.
- Added **16 provisional evidence rows** to `data/corpus-evidence.csv`, covering five papers: DISC-069 (2), DISC-071 (4), DISC-072 (4), DISC-077 (3), and DISC-079 (3).
- Updated the full-corpus processing queue and the DOI-to-Better-BibTeX crosswalk.
- No candidate has received final inclusion approval or final Q1 eligibility.

## Candidate-by-candidate status

| Candidate | Paper/topic | Current progress | Evidence IDs |
|---|---|---|---|
| DISC-069 | Acid-treated sawdust for rifampicin | Preliminary removal/property findings from published abstract and indexed conclusion; PDF pin pending | EV-BIB-069-001–002 |
| DISC-070 | Competitive sulfonamide/chloramphenicol sorption on functionalized biochar | Abstract screen only; full-text extraction pending | — |
| DISC-071 | Magnetic Fe-modified activated carbon; ciprofloxacin and ibuprofen | Provisional online full-text extraction of conditions, fitted isotherm parameters, matrix effect and single-cycle regeneration; PDF/SI pin pending | EV-BIB-071-001–004 |
| DISC-072 | Magnetic buckwheat-peel biochar; tetracycline and Zn(II) | Provisional online full-text extraction of material characteristics, single/competitive capacities, stability and regeneration | EV-BIB-072-001–004 |
| DISC-073 | Clay–biochar composites for tetracycline; pH and specific-ion effects | Abstract screen only; full-text extraction pending | — |
| DISC-074 | Agricultural-waste biochars with iron-oxide variants | Abstract screen only; full-text extraction pending | — |
| DISC-075 | pH-dependent sorption of sulfonamides on biochars | Abstract screen only; full-text extraction pending | — |
| DISC-076 | Nanocomposite ceramic adsorbent, pharmaceutical wastewater and fixed-bed/regeneration | Abstract/figure-description screen only; exact full-text metrics need verification | — |
| DISC-077 | Antibiotic association with smectite and organoclays | Provisional contextual/mechanistic extraction; individual AMX isotherms showed no observed plateau, so fitted qmax is extrapolative | EV-BIB-077-001–003 |
| DISC-078 | Biochar in swine wastewater | Abstract/metadata screen only; real-wastewater evidence extraction pending | — |
| DISC-079 | Kaolinite–coconut-husk hybrid biochar; ciprofloxacin and tetracycline | Provisional online full-text extraction of preparation conditions, fitted qmax and reported kinetic trend; ESI/PDF pagination pending | EV-BIB-079-001–003 |

## Scientific safeguards

The 16 new rows are **provisional extraction records**, not fully page-verified final evidence. The publisher full-text HTML or indexed full-text excerpts were available for some papers, but the corresponding original PDF pagination has not yet been independently verified. Where supplementary Tables S1–S2 or other SI are cited by the paper but were not directly checked, that limitation is recorded.

Key differences are preserved:

- DISC-069's 13% and 65% values are removal efficiencies at high dose/contact time, not adsorption capacities.
- DISC-071's Langmuir fitted (q_m), Freundlich (K_F), wastewater matrix effect, and electro-regeneration metrics are distinct. Ibuprofen is a co-contaminant, not an antibiotic; the study reports only one adsorption–regeneration cycle.
- DISC-072's single-component tetracycline capacity and mixed tetracycline/Zn(II) capacity must remain separate; the paper reports mutual promotion and a pH stability window due to iron leaching.
- DISC-077 is contextual/environmental-fate and organoclay-mechanism evidence, not a direct treatment-performance ranking source. The authors state that no plateau was observed in the individual amoxicillin isotherms; the fitted qmax is therefore extrapolative.
- DISC-079's KCB, acid-activated KCB-A and alkali-activated KCB-B are different materials. The capacities are fitted isotherm parameters; the cited supplementary model tables were not independently inspected.

## What remains

Six of the eleven newly registered papers have only received title/abstract screening so far: DISC-070, DISC-073, DISC-074, DISC-075, DISC-076 and DISC-078. They still need full-text evidence extraction. For the other five, original PDF page/table/figure verification and SI checks remain. The other **58 BibTeX entries still do not match a registered candidate** and remain in the processing queue for title/abstract screening.

## Project links

- [Master evidence database](../data/corpus-evidence.csv)
- [Screening register](../data/corpus-screening-register.csv)
- [Candidate decision audit](../data/candidate-decision-audit.csv)
- [Screening adjudication](../data/screening-decision-adjudication-v1.csv)
- [All-entry processing queue](../references/bibtex_full_corpus_processing_queue_2026-10-29.csv)
- [Candidate DOI-to-key crosswalk](../references/bibtex_candidate_key_crosswalk_2026-10-29.csv)
- [Citation-key audit and overall progress](../references/BBT_EXPORT_AUDIT_2026-10-29.md)
