# Original PDF batch integrity audit — 2026-10-31

## Purpose and boundary

This audit continues the original user-supplied PDF work in batches 01–20. It does not replace those papers with web-discovered candidates and does not merge the separate 28 October upload sets into the original batch counts. The broad review and the separate semester-paper evidence remain distinct. Journal quartiles are not an input to the semester-paper workstream.

## Repository evidence confirmed

- All 20 original batch extraction notes are present in `evidence/`: Batch 01–03 dated 25 October; Batch 04–14 dated 26 October; Batch 15–20 dated 27 October 2026.
- Each note describes three PDF records: 60 batch paper records in total. This includes reviews and one full-text-confirmed out-of-scope record; it does not mean 60 accepted primary studies.
- The canonical `data/corpus-evidence.csv` contains 305 original-batch evidence rows with IDs EV-B01–EV-B20. The per-batch row counts are: B01 19, B02 20, B03 10, B04 19, B05 18, B06 17, B07 19, B08 18, B09 22, B10 15, B11 18, B12 5, B13 13, B14 15, B15 13, B16 15, B17 13, B18 12, B19 13, B20 11.
- These 305 records resolve to 59 distinct DOI identities. Batch 03 includes one unrelated full-text-confirmed exclusion (CORP-062), which correctly has no adsorption evidence row.
- The 28 October upload wave is separate: 32 paper records and 177 source-linked evidence rows, with its own retained staging files and consolidation crosswalk.

## Master CSV integrity repair

A field-position audit identified five malformed original-batch rows. Their content had been shifted left, leaving a trailing blank cell and causing source locations, evidence statuses or caveats to appear in the wrong columns. The master CSV schema remained 15 columns, so simple width validation alone had not detected the issue.

The following rows were repaired by restoring the missing field label/value and shifting the existing content into its intended column. Existing evidence statements, values, source pinpoints, statuses and caveats were preserved:

| Evidence ID | Repair |
|---|---|
| EV-B03-005 | Restored continuum-stage value: Stage 2 — natural and modified clays / clay-based composites. Moved “Practical application and techno-economics” into Evidence domain. |
| EV-B08-005 | Restored Evidence domain: Regeneration and limited DNA-fluorescence safety assay. |
| EV-B08-006 | Restored Evidence domain: Preparation cost and spent-media disposal. |
| EV-B09-022 | Restored Evidence domain: Regeneration/reuse performance and separate broad-target screening. |
| EV-B11-011 | Restored Evidence domain: Regeneration and five-cycle capacity retention. |

GitHub commit: `6b8cac03bb473bed457684627501ee0e77f60234`.

Post-write re-fetch validation:
- 505 total master evidence rows retained.
- All 305 EV-B01–EV-B20 rows remain present with 15 columns.
- The five corrected rows now have source pinpoints in the source-location field, appropriate evidence statuses, and their original caveats in the caveat field.
- No other original-batch rows were missing an identifiable PDF/table/figure/section pinpoint under the current source-location check. This is a structural check, not a full scientific re-read of all 60 papers.

## Attachment filename matches confirmed in ChatGPT Library

The following stored PDF attachments were matched to the titles in their original batch notes by the indexed full-text title/DOI content. These filenames are Library attachment names, not filenames inferred from DOI patterns.

### Batch 03
| Paper | DOI | Library PDF filename | Treatment |
|---|---|---|---|
| Hacıosmanoğlu et al. (2022), natural and modified clay review | 10.1016/j.jenvman.2022.115397 | `1-s2.0-S0301479722009707-main.pdf` | Secondary review; retain for taxonomy/citation discovery. |
| Wang et al. (2010), CIP–montmorillonite cation exchange | 10.1016/j.jhazmat.2010.07.025 | `1-s2.0-S0304389410009106-main.pdf` | Primary mechanistic study; retain with high-feed concentration caveat. |
| Gillespie & Penny (2022), protected areas/community adaptation | 10.1016/j.jenvman.2021.113805 | `1-s2.0-S0301479721018673-main.pdf` | Full-text-confirmed exclusion; unrelated social-science paper. |

### Batch 08
| Paper | DOI | Library PDF filename | Treatment |
|---|---|---|---|
| Kar et al. (2025), activated wood-apple-shell carbon for enrofloxacin | 10.1016/j.hazadv.2025.100666 | `1-s2.0-S2772416625000786-main.pdf` | Primary study; cost, cycle and DNA assay caveats retained. |
| Sompornpailin et al. (2024), GAC treatment of secondary hospital effluents | 10.1016/j.scitotenv.2024.172095 | `ac 1.pdf` | Primary real-effluent/fixed-bed study. |
| Al-sareji et al. (2024), banana-peel activated carbon | 10.3390/ma17051032 | `ac 2.pdf` | Primary study; amoxicillin is antibiotic endpoint, carbamazepine is not. |

### Additional identity match
The Batch 12 MWCNT-E paper by Oliveira et al. (2024), DOI 10.1016/j.jclepro.2024.142414, is present in Library as `cnt 1.pdf`.

## Batch 03, 08 and 12 quality decisions

- **Batch 03:** three paper identities align with the batch extraction note and screening dispositions. The incorrect association between the protected-areas DOI and the clay review lead is explicitly corrected in the screening record.
- **Batch 08:** all 18 evidence records are present (6 per paper). A separate targeted review confirms the GAC paper's low-concentration real-matrix evidence is not mixed with high-concentration batch qmax metrics. Amoxicillin is separated from carbamazepine in the banana-peel-carbon paper. Two shifted rows (EV-B08-005/006) were repaired in the master CSV.
- **Batch 12:** five records are intentionally allocated 3/1/1: MWCNT-E primary adsorption (three rows), iron-modified-biochar review synthesis (one row), and UiO-66/CNT membrane rejection/self-cleaning (one row). The membrane paper is correctly not treated as an adsorption-capacity study.

## Limits and remaining audit work

- The original 20 batch notes preserve paper titles, DOIs, extracted results and PDF source pinpoints, but they do not consistently preserve the exact uploaded attachment filename for every PDF.
- The complete 60-paper filename-to-paper mapping is now recorded in `data/original-pdf-batch-attachment-crosswalk.csv`; the earlier Batch 03/08/12 subset listed above is retained as illustrative detail, not as the full extent of the completed mapping.
- All 60 paper records have not yet been independently re-read in this continuation. A candidate having evidence rows, or a batch note saying “reviewed”, is not by itself proof that every possible evidence domain is complete.
- The blank 300-slot `data/new-paper-upload-batch-tracker.csv` is a separate future-upload tracker introduced on 28 October. It is not the historical register for original Batches 01–20 and must not be used to infer that those batches were not processed.
- No scientific result, inclusion decision, manuscript claim or quartile entry was changed in this audit. Only the five malformed master evidence rows were structurally repaired; the subsequent 60-paper crosswalk adds provenance metadata without altering evidence.


## Complete original PDF attachment crosswalk — 2026-10-31

The file `data/original-pdf-batch-attachment-crosswalk.csv` now provides the paper-level mapping for all 60 paper records in original Batches 01–20. Each row records the batch and paper slot, candidate ID, title, DOI of the uploaded version, Library attachment filename(s), match status, source-batch master evidence IDs, evidence-row count, extraction-note path and disposition caveat.

Validation:
- 60 paper records mapped to 60 distinct batch slots.
- 60/60 attachment identities matched by indexed Library PDF title/DOI evidence.
- 305 original batch-specific evidence IDs mapped to the corresponding 60 paper records.
- The total per-batch evidence counts in the crosswalk reconcile exactly to the canonical master table: B01 19, B02 20, B03 10, B04 19, B05 18, B06 17, B07 19, B08 18, B09 22, B10 15, B11 18, B12 5, B13 13, B14 15, B15 13, B16 15, B17 13, B18 12, B19 13 and B20 11.
- All 305 evidence IDs are unique in the crosswalk; no evidence row is mapped twice.
- The one paper with zero evidence rows is CORP-062 (Gillespie & Penny, 2022), which is explicitly documented as a full-text-confirmed unrelated exclusion in Batch 03. It has no adsorption evidence row by design.
- Candidate DISC-026 is now linked to the Adu-Poku 2024 acid-activated coconut-husk/amoxicillin PDF in Batch 15.
- Two similar Bioresource Technology PIIs have been distinguished: Batch 02 Jiao et al. (2024), DOI 10.1016/j.biortech.2024.130394, is `1-s2.0-S096085242400097X-main.pdf`; Batch 04 Na et al. (2024), DOI 10.1016/j.biortech.2023.130281, is `1-s2.0-S0960852423017091-main.pdf`. They are separate studies and separate attachments.
- Duplicate Library copies of some papers are listed in the filename field when confirmed. They do not represent additional studies or add evidence counts.

This closes the original batch-level **attachment-to-evidence mapping**. It does not mean every original article has been independently re-read again in this continuation. The full-text extraction notes, 305 source-pinned rows and their caveats remain the scientific extraction record. The remaining substantive work is targeted paper-level completeness/claim QA, not locating the original 20 batches or recreating their evidence.


## Post-crosswalk master evidence QA — 2026-10-31

A further field-level audit of the 305 EV-B01–EV-B20 rows, after the five repairs, found:
- 305/305 rows have the expected 15 columns.
- Zero blank values in Evidence domain, Experimental design / conditions, Reported result, Value / units, Model / metric, Source location, Evidence status or Caveat / follow-up.
- Zero missing recognizable PDF-page/table/figure/section source pinpoints.
- One long Evidence domain label and one long source-location field are valid descriptive values, not shifted cells.
- No further malformed row was identified. Two domain labels flagged by a simple unit-text heuristic (“High-concentration capacity” and “HWW adsorption case-study map”) were examined and are normal labels, not misplaced data.

No further evidence-cell repairs were made in this pass.


## Targeted extraction-note ↔ master-evidence reconciliation

### Batch 14 — complete representation, source caveats preserved
- The 15 EV-B14 rows map to all three uploaded papers: Gopal & Mukherjee (5 rows), Delmond et al. (5 rows), and Shaha et al. (5 rows).
- The source notes' key limits are carried into the master records: Gopal dose/LOD/LOQ inconsistencies and adsorption-plus-transformation boundary; Delmond's 12,179.5 mg/g fitted qmax remains quarantined against observed ≈2.8–4 mg/g uptake; Shaha's observed qe is distinguished from its 1000 µmol/g fitted qmax and the isotherm concentration window is separately recorded.
- The longer source location in EV-B14-012 is intentional: it lists multiple printed page/table/figure locations, not a shifted field.
- No missing master evidence row or further correction identified.

### Batch 15 — complete representation, high-priority caveats preserved
- The 13 EV-B15 rows map to Li et al. (2019) (3 rows), Adu-Poku et al. (2024) (4 rows), and Li et al. (2025) (6 rows).
- Li et al. (2019): TMP is retained as the antibiotic endpoint and DCF remains explicitly non-antibiotic; the rendered-table µg units and low-concentration observed qe are distinguished from fitted isotherm Qm.
- Adu-Poku et al. (2024): the abstract 0.5–2.5 mg/L versus Methods/Results 20–70 mg/L conflict and the kinetic qe mass-balance inconsistency are represented in the structured rows. DISC-026 is the correct candidate ID.
- Li et al. (2025): the multi-step PGOT@GEL processing burden, high-concentration optimization, fitted qmax, binary CIP–Cu²⁺ effects, water-matrix results and seven-cycle performance are represented with separate metrics and limitations.
- No missing master evidence row or further correction identified.

### Batch 20 — complete representation; version comparison remains open
- The 11 EV-B20 rows map to Liang et al. (2024) (4 rows), Pinheiro et al. (uploaded preprint v1; 3 rows), and Sousa et al. (2025) review (4 rows).
- Liang et al.: reported removal, fitted qmax, four-cycle decline, magnetic recovery and the metal-salt/autoclave processing burden are represented separately. The missing SI table remains a source limitation.
- Pinheiro et al.: the crosswalk records the uploaded Research Square DOI 10.21203/rs.3.rs-4331760/v1, while candidate CORP-023 retains the subsequent published DOI 10.1007/s11356-024-35293-4. The batch note and screening record correctly say the uploaded preprint was reviewed and the published abstract/headline capacities were cross-checked, but the published full methods/tables/supplement were not fully assessed. Keep all detailed kinetic/isotherm results as preprint-version evidence until this comparison is completed.
- Sousa et al. remains review-level evidence; compiled values are not treated as independent primary observations.
- No missing master evidence row or further correction identified.

These are targeted note-to-register checks, not an independent second full-text reading of all 60 PDFs. All unresolved source disagreements and version limitations remain visible rather than being silently harmonized.


### Batch 06 — primary study and two reviews correctly separated
- The 17 EV-B06 rows divide into Zhu et al. primary fermentation-residue biochar (7 rows), Yan et al. tetracycline/biochar review (4 rows), and Zango et al. systematic review (6 rows).
- Zhu's main-text observations are separated from fitted qmax values and missing SI fit tables. The printed qe/removal equation sign error, missing SI optimization/kinetic/isotherm parameters, high mg/L concentrations, and ambiguity in the five-cycle reuse table remain explicit.
- Both reviews' compiled values and source counts are labelled secondary. Zango's 5,601→3,054→632→359→305/162 flow discrepancy and non-parenthesized displayed search logic remain flagged; its historical prices are not treated as current comparable quotations.
- The structured rows cover the main study and the review synthesis; no missing master evidence row or source-pinpoint defect identified.

### Batch 10 — trace-level graphene-derived study and raw biomass study reconciled
- The 15 EV-B10 rows divide into Jiao et al. (2025) review (3 rows), Zhang & Wu (2022) N-rGO primary study (6 rows), and Atta et al. (2023) raw rice-husk/LEV primary study (6 rows).
- N-rGO is correctly classified as graphene-derived engineered carbon, not biochar. The 80 mL antibiotic feed + 20 mL N-rGO dispersion basis is retained with the qe mass-balance ambiguity; large Langmuir q_m values are model fits and held out of capacity ranking pending concentration/dose reconciliation. Eight-cycle reuse and humic-acid/ion effects are separately represented.
- Atta et al.'s 2.47 mg/g fitted qmax is kept separate from percentage removal and the 5–120 g/L dose range; high dose is a practical limitation, not hidden behind the headline 99% removal.
- Jiao et al.'s co-removal review remains review-only; its compilation is not added as new primary experimental measurements.
- No missing master evidence row or source-pinpoint defect identified.


### Batch 01 — three uploaded primary studies reconciled
- The 19 EV-B01 rows map as Yao et al. Fe/N-co-doped biochar (6), Jaria et al. waste-derived GAC in municipal wastewater fixed beds (5), and Gao et al. KOH-activated dyeing-sludge biochar (8).
- Antibiotic scope is correctly isolated: SMX is the antibiotic endpoint in Jaria et al.; CBZ/PAR are non-antibiotic pharmaceuticals. Yao's Cu(II) is retained as a co-contaminant, separate from CIP. Gao's four-antibiotic removal, fixed-bed, Fenton-regeneration and cost estimates are recorded with the paper's inconsistencies.
- Fitted qmax, observed batch uptake and integrated column qtotal are kept distinct. The Gao cost figure is not treated as a complete comparable TEA.
- No missing master evidence row or source-pinpoint defect identified.

### Batch 02 — three uploaded primary studies reconciled
- The 20 EV-B02 rows map as Jiao et al. molecularly imprinted magnetic biochar (6), Mosaffa et al. cellulose-char/chitosan-PEI beads (7), and Masrura et al. solvent-modified sewage-sludge biochar in diluted/spiked human urine (7).
- The corrected Library attachment mapping distinguishes Jiao et al. (DOI 10.1016/j.biortech.2024.130394) from the separate Na et al. macadamia-biochar paper in Batch 04 (DOI 10.1016/j.biortech.2023.130281).
- Jiao's Table/body capacity mismatch and 11.97 mg/g OTC result versus the stated mass-balance ceiling remain flagged; Mosaffa's abstract/body removal difference, high-feed capacity and conflicting regeneration-cycle claims remain distinct; Masrura's negative/unusable fitted capacities and urine-matrix/regeneration limitations remain explicit.
- No missing master evidence row or source-pinpoint defect identified.


### Batch 04 — three primary studies reconciled
- The 19 EV-B04 rows map to Du et al. (2025) cotton-husk phosphoric-acid-activated biochar (9), Na et al. (2024) pristine macadamia-nutshell biochar (4), and Zhou et al. (2024) sepiolite/montmorillonite microwave-regeneration study (6).
- Du's observed Qe and fitted Qm values are separated; the abstract/Table 3 mismatch, COD/TOC-only real-water outcome (no target-specific CIP residual), unresolved regeneration-agent mapping and preliminary cost boundary remain explicit.
- Na's four-antibiotic study preserves mmol/kg units and the high 8 g/L dose. Its DOI/file identity remains distinct from the B02 Jiao paper.
- Zhou's observed uptake and fitted isotherm Qmax remain separate; regeneration ratio is not equated with desorbed TC mass, and no actual energy/cost or real-water validation is claimed.
- No missing master evidence row or source-pinpoint defect identified.

### Batch 05 — primary studies and secondary review reconciled
- The 18 EV-B05 rows map to Usama et al. (2025) waste-PET activated carbon (9), Fraiha et al. (2024) clay/pharmaceutical review (3), and Yaqubi et al. (2021) leached carbon-black waste/chitosan beads (6).
- Usama's reported q/removal inconsistencies, missing SI parameters, Dxy/Ntx/SDN target-identity caveats, use-stage/end-of-life omissions in LCA and preliminary local cost model remain visible.
- Fraiha is labelled secondary review, includes non-antibiotic pharmaceuticals and does not provide a reproducible systematic search method; its table values are not elevated to primary evidence.
- Yaqubi's BET-area conflict, diluted-volume/dose ambiguity, poor fixed-bed model fit, residual-metal question and missing unit cost/regeneration evidence remain flagged.
- No missing master evidence row or source-pinpoint defect identified.


### Batch 07 — two primary studies and one review reconciled
- The 19 EV-B07 rows map to Sumariva et al. (2024) clay honeycomb monoliths (5), Nugraha et al. (2025) hospital-wastewater adsorption review (5), and Sousa et al. (2026) brewery-residue biochar fixed-bed study (9).
- Sumariva's powder, monolith/recirculation and temperature/light/air configurations are kept distinct; post-use thermal transformation is not labelled adsorption. No once-through trace-level pilot result is claimed.
- Nugraha's HWW concentration ranges and treatment examples remain secondary evidence; the 10 mg/L spiked-HWW example is separated from ng/L occurrence examples, and municipal/hospital-connected effluent is not conflated with pure HWW.
- Sousa's filtered/autoclaved real secondary WWTP effluent, controlled 20 μmol/L feeds, fixed-bed model outputs, experimental q_s, single/ternary mixtures, regeneration ratio above 100%, and process-LCA stage contributions are distinguished. The total environmental impacts are SI-dependent and no cradle-to-grave or spent-media result is claimed.
- No missing master evidence row or source-pinpoint defect identified.

### Batch 09 — three primary studies reconciled
- The 22 EV-B09 rows map to Alidadi et al. (2018) modified sawdust (7), García-Criado et al. (2025) purified stevensite (8), and Li et al. (2026) ball-milled/N-doped biochar (7).
- Alidadi's 98.40% RSM output is correctly identified as predicted rather than measured validation; Freundlich is preferred by AIC; the 88% figure is water volume reclaimed, not TC desorption; single-stage regeneration and the 0.25 mg/L hospital-wastewater non-detect with absent LOD are preserved.
- García-Criado's abstract/method concentration mismatch, likely kinetic unit typo, >200,000 mg/g narrative qmax versus Table 2 and experimental qe ~1–1.6 mg/g, possible degradation at extreme pH, and spiked-matrix design remain explicit. Implausible qmax values are held out of quantitative rankings.
- Li's abstract pore-volume discrepancy (276 cm³/g vs detailed main text 0.2951 cm³/g) is retained with the detailed main-text value and the abstract error flagged; 155–400 mg/g Langmuir Qm remains fitted; six-cycle removal loss to 40.6% is correctly characterized as a major regeneration weakness.
- No missing master evidence row or source-pinpoint defect identified.


### Batch 11 — three primary adsorption studies reconciled
- The 18 EV-B11 rows map to Kurczewska & Cegłowski (2025) halloysite/MIP alginate beads (6), Guesmi et al. (2025) magnetic Se-MOF/chitosan-alginate beads (5), and Nguyen et al. (2023) phosphoric-acid-activated sunflower-husk biochar (7).
- Kurczewska's observed-versus-fitted capacities, the 277.6 mg/g reported uptake above the stated 250 mg/g feed ceiling, high-concentration spiked-water tests, soil results and five-cycle retention are kept distinct.
- Guesmi's BBD “Yield (mmol/g)” label versus elsewhere-reported mg/g capacity, paper's “recovery” term for spiked wastewater, five-cycle decline, and absence of Se/Fe leaching/toxicity or process-cost evidence remain explicit. The repaired EV-B11-011 now correctly labels the regeneration domain.
- Nguyen's ibuprofen comparator is not counted as an antibiotic; fitted Langmuir q_m, fitted kinetic q_e and measured removal remain separate. No product yield, full cost or deployment evidence is inferred from waste feedstock origin.
- No missing master evidence row or source-pinpoint defect identified.

### Batch 13 — two reviews and one primary adsorption/desorption study reconciled
- The 13 EV-B13 rows map to Li et al. (2024) magnetic-biochar review (3), Jia et al. (2024) biochar antibiotic-removal review (3), and Conde-Cid et al. (2021) primary pine-bark/oak-ash/mussel-shell sulfonamide study (7).
- Both review sources are retained as secondary synthesis/citation-discovery only; reported capacity ranges and regeneration examples are not treated as new primary measurements or standardized rankings.
- Conde-Cid's low molar adsorption amounts, µmol/kg units, strongly unequal sorbent doses, source text discrepancies (<40 vs <45%; <10 vs <15%), desorption as a one-step reversibility test (not multi-cycle regeneration), and Kd/Freundlich constants distinct from qmax are retained.
- No missing master evidence row or source-pinpoint defect identified.


### Batch 16 — two primary studies and one review reconciled
- The 15 EV-B16 rows map to Míguez-González et al. (2023) primary forestry/agro-food sorbents (5), Cuevas et al. (2019) primary mineral/TCA sorption study (5), and Abd El-Monaem et al. (2022) chitosan-composite review (5).
- Míguez-González's pine bark/oak ash/mussel shell retention and single CaCl2 release test are not described as wastewater column removal or repeated regeneration. The TMP/pine-bark fitted qmax exceeds the accessible mass-balance loading and remains excluded from ranking.
- Cuevas's high-loading mg/L experiments, observed uptake, CEC-related fitted Cm values and mineral-specific mechanism interpretations are distinguished. No trace-level wastewater or column performance is claimed.
- The chitosan review's compiled TC/CIP capacities and mixed adsorption/degradation endpoint are retained as secondary-only evidence; its 1111 mg/g MgO/chitosan/GO value and AMX/Cd redox pathway require primary-paper verification.
- No missing master evidence row or source-pinpoint defect identified.

### Batch 17 — one systematic review and two primary studies reconciled
- The 13 EV-B17 rows map to Mirizadeh et al. (2025) chitosan batch/dynamic systematic review (4), Mohammed-Ridha & Abdul-Ahad barley husk/eggshell/LEV primary study (4), and Hamdi et al. (2024) raw/activated Tunisian clay/TC primary study (5).
- Mirizadeh's 74-study review flow and impact-factor exclusion criterion are recorded as review-method context; compiled batch and dynamic-column q0 values are not merged with primary batch qmax.
- Mohammed-Ridha's PDF imprint (December 2014) overrides the filename's 2023 label. The 125.735 mg/g fitted barley-husk q_m and several kinetic q_e estimates exceed the simple mass-balance ceilings implied by stated feed/dose; they remain explicitly flagged, not accepted as measured capacities.
- Hamdi's raw-versus-activated comparison preserves the high mg/L test range and the finding that activation is not necessarily beneficial. A single low CaCl2 desorption value is not treated as destruction or repeated regeneration; unusual EC values remain as printed pending source verification.
- No missing master evidence row or source-pinpoint defect identified.


### Batch 18 — three review sources reconciled as secondary evidence
- The 12 EV-B18 rows map to Nguyen et al. (2025) biochar-derived adsorbents review (5), Singh et al. (2026) TC-specific AC/biochar review (3), and Ajala et al. (2023) biomass/biochar antibiotic-adsorption review (4).
- All three are correctly labelled review-level evidence. Their qmax examples, mechanism statements, and processing routes are not treated as new primary measurements or comparable rankings.
- Nguyen's Table 3 BPA (bisphenol A) entry is explicitly recognized as a non-antibiotic; the exceptionally high TC examples remain secondary and require primary-source verification.
- Singh's TC-focused search and missing PRISMA/count reporting are retained as method limitations; its 1357.5 mg/g example is flagged because the same cited source is said to fit Freundlich better than Langmuir.
- Ajala's emphasis on COD versus target-specific antibiotic measurements, synthetic versus real water, and heterogeneous metrics remains contextual rather than a newly harmonized dataset.
- No missing master evidence row or source-pinpoint defect identified.

### Batch 19 — two primary studies and one review reconciled
- The 13 EV-B19 rows map to Liu et al. (2025) kaolin–alginate CTC beads (5), Maged et al. (2020) natural/purified and acid-activated bentonite for CIP (5), and Hamid et al. (2025) waste-based biochar review (3).
- Liu's observed and fitted uptake, unequal-dose comparison, four-cycle reuse, 5 mg/L spiked water/20-bed-volume column results, and author cost estimate are separately represented. The unusual electricity-price unit (US$/g) remains flagged; this is not treated as a complete plant-level TEA/LCA.
- Maged's “natural” bentonite is correctly described as laboratory-purified rather than wholly untreated. Batch qmax/observed uptake, salt inhibition and column qbed are separate metrics; the Table 6 three-cycle sum (187.11 mg/g) versus conclusion value (178.11 mg/g) discrepancy remains open.
- Hamid's review is supporting literature only; its 88-paper narrative count and compiled capacities are not treated as a reproducible systematic search or new primary data.
- No missing master evidence row or source-pinpoint defect identified.


### Batch 03 — clay review, primary mechanistic study and exclusion reconciled
- The 10 EV-B03 rows map to Hacıosmanoğlu et al. (2022) clay review (5) and Wang et al. (2010) CIP–montmorillonite primary study (5); CORP-062 remains the full-text-confirmed unrelated exclusion.
- The clay review's 82-paper review-method count, material taxonomy and capacity examples remain secondary. Supplementary Tables S1–S6 were not included; its quantitative examples require tracing to primary sources before numerical synthesis.
- Wang's 330 mg/g Langmuir/reported capacity is distinguished from ~292 mg/g observed uptake at the cited 3,000 mg/L feed. The near-1:1 cation-release/CIP-uptake relationship, Ca²⁺ release and XRD/FTIR changes provide direct support for cation exchange under the tested high-concentration conditions.
- The very high feed range and lack of real-water, competition, reuse or column tests are preserved. No missing master evidence row or source-pinpoint defect identified.

### Batch 08 — two primary studies and one real-effluent/fixed-bed study reconciled
- The 18 EV-B08 rows map to Kar et al. (2025) activated wood-apple-shell carbon for ENF (6), Sompornpailin et al. (2024) hospital-effluent GAC/resistome study (6), and Al-sareji et al. (2024) banana-peel activated carbon (6).
- Kar's no-external-N-doping recipe, 1.76 cm³/g micropore-volume anomaly, conflicting dose ranges, severe ΔG arithmetic/unit inconsistency, limited DNA-fluorescence assay and author-reported INR 239.22/kg cost boundary are retained. Its 81.47% after four cycles is not broad proof of water safety.
- Sompornpailin's low-µg/L real secondary hospital effluent/fixed-bed outcomes are kept distinct from high-mg/L batch qmax. The paper's “SMZ” label is preserved pending confirmation; E. coli growth is not broad ecotoxicity clearance; ARG/ARB accumulation in used GAC is retained as a spent-media risk.
- Al-sareji's amoxicillin is the antibiotic endpoint; carbamazepine remains a non-antibiotic comparator. Fitted Qmax, matrix-specific removal and seven-cycle decline are separate.
- The two malformed master rows EV-B08-005 and EV-B08-006 were repaired in the evidence-domain column; no further missing row identified.

### Batch 12 — primary MWCNT study, secondary review and adjacent membrane technology reconciled
- The five EV-B12 rows map to Oliveira et al. (2024) eucalyptus-functionalized commercial MWCNTs (3), Yang et al. (2025) iron-modified-biochar review (1), and Yin et al. (2024) electroactive UiO-66/CNT membrane (1).
- Oliveira's single/binary CIP/OFL uptake is retained in mmol/g; no unsupported unit conversion was made. Commercial CNT feedstock means “green” refers to functionalization, not the CNT precursor. No real wastewater, reuse, fixed-bed, leaching or LCA evidence is claimed.
- Yang remains secondary-only; adsorption and catalytic degradation are not merged.
- Yin is a primary adjacent membrane-rejection study, not an adsorption-capacity paper. Rejection %, permeability and electro-cleaning results are excluded from mg/g adsorption rankings.
- The five-row allocation is intentional (3/1/1), not evidence of incomplete extraction. No missing master evidence row or source-pinpoint defect identified.


## Scientific evidence-gap triage — first pass

A ranked register has been created at `data/original-corpus-scientific-gap-register.csv`. It records 19 issues, with P0 items capable of changing quantitative conclusions and P1 items to resolve when the corresponding claim is used.

### Priority 0 — resolve before quantitative synthesis
1. **Kar et al. (2025), DISC-024:** impossible ΔG arithmetic/unit values and inconsistent dose ranges.
2. **Jiao et al. (2024), DISC-010:** reported OTC uptake appears above the feed/dose mass-balance ceiling; table/body and SI-dependent protocol.
3. **Adu-Poku et al. (2024), DISC-026:** abstract versus Methods/Results initial-concentration conflict and kinetic mass-balance issue.
4. **Mohammed-Ridha & Abdul-Ahad, CORP-019:** fitted capacity/kinetic values exceed simple mass-balance ceilings; PDF publication imprint is 2014, not the uploaded filename's 2023.
5. **García-Criado et al. (2025), DISC-018:** narrative qmax above 200,000 mg/g conflicts with table and observed uptake around 1–1.6 mg/g; concentration/unit issues.
6. **Zhang & Wu (2022), CORP-031:** N-rGO dose/feed-volume basis and very large fitted Langmuir values require mass-balance reconstruction.

### Priority 1 — resolve if the claim is used
- **Gopal & Mukherjee (2024), DISC-006:** reported residual NOR may fall below the stated UV–vis LOQ.
- **Du et al. (2025), DISC-017:** distinguish target-specific CIP removal from COD/TOC proxies; reconcile observed/fitted values.
- **Li et al. (2026), DISC-012:** abstract versus main-text pore-volume discrepancy; retain severe six-cycle decline.
- **Liang et al. (2024), DISC-030:** missing SI and no complete yield/cost/leaching/LCA inventory.
- **Pinheiro et al. (2024), CORP-023:** uploaded preprint and later journal version have not been fully reconciled.
- **Kar et al. (2025), DISC-024:** author's INR 239.22/kg and 16.7× cost claim need boundary/yield reconstruction.
- **Maged et al. (2020), DISC-014:** fixed-bed three-cycle sum conflicts with conclusion (187.11 vs 178.11 mg/g).
- **Liu et al. (2025), DISC-007:** electricity-cost unit printed as US$/g is anomalous; four-cycle cost is not full TEA/LCA.

### Priority 2 — optional source strengthening or editorial boundary
- Hacıosmanoğlu review SI, Sompornpailin microbial/ARG SI, Wang high-feed transferability, and other secondary-source primary-paper tracing are optional unless a specific manuscript claim depends on them.
- Yin et al. is adjacent membrane rejection, not adsorption-capacity evidence. CORP-062 remains excluded as unrelated.

### Synthesis rules
- A source inconsistency may be retained as a caveat when no reliable correction is possible; it must not be silently normalized.
- Cost estimates are not comparable TEA/LCA unless system boundary, yield, reagent/energy/water inputs, denominator, currency/year, regeneration and spent-media management are defined.
- Do not mix fitted qmax, measured qe, removal percentage, fixed-bed qbed/qtotal and membrane rejection into one capacity ranking.
- The next execution sequence should start with the six P0 items.


## Primary-PDF verification of the first two P0 cases

The original Kar (2025) and Jiao (2024) PDFs were retrieved from the Library, rendered and visually checked. The evidence caveats and scientific gap register were updated from the original page images.

- **Kar, DOI 10.1016/j.hazadv.2025.100666:** Table 4/Fig. 9 on PDF p. 11 confirm ΔG° −3825 to −4089 under a kJ/mol axis/header. Methods pp. 4–5 define the Gibbs equations and units. The reported ΔH°/ΔS° imply +30.081 to +32.756 kJ/mol across the tabulated temperature interval, so the printed thermodynamic set is inconsistent. No corrected value was inferred.
- **Jiao, DOI 10.1016/j.biortech.2024.130394:** Fig. 4a on PDF p. 5 states C0 = 4 mg/L and dose = 0.5 g/L, but selectivity uptake is 11.97 mg/g (mass-balance ceiling 8 mg/g). Fig. 3a/Table 1 on PDF p. 4 state C0 = 2 mg/L and dose = 0.5 g/L, while the text/Table 1 report experimental/fitted kinetic qe around 12.07/10.84/12.55 mg/g (ceiling 4 mg/g). The adjacent prose also switches between mg/g and mg/L. Both reported uptake groups are now quarantined pending author clarification.
- The separate 67.89 mg/g Langmuir parameter in Jiao is from its 1–200 mg/L isotherm experiment, not the selectivity/kinetic conditions; it remains a model-fit result, not an observed low-feed uptake.

Detailed calculations and source-page references are in `logs/2026-10-31-p0-mass-balance-and-thermodynamic-checks.md`. Updated records: `data/corpus-evidence.csv` and `data/original-corpus-scientific-gap-register.csv`.
