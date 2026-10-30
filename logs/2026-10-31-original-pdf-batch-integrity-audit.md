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
- The attachment checks above confirm file availability and identity for Batch 03 and Batch 08 (plus one Batch 12 item), not all 60 batch PDFs. The exact filename-to-paper mapping for the remaining batches is still open and must be built from the Library attachments, not guessed.
- All 60 paper records have not yet been independently re-read in this continuation. A candidate having evidence rows, or a batch note saying “reviewed”, is not by itself proof that every possible evidence domain is complete.
- The blank 300-slot `data/new-paper-upload-batch-tracker.csv` is a separate future-upload tracker introduced on 28 October. It is not the historical register for original Batches 01–20 and must not be used to infer that those batches were not processed.
- No scientific result, inclusion decision, manuscript claim or quartile entry was changed in this audit. Only the five malformed master evidence rows were structurally repaired.
