# Semester manuscript citation and methods quality-control pass (2026-10-31)

## Scope

Quality-control follow-through after the 19-claim evidence audit. This pass checks manuscript citation command rendering, linkages to the curated BibTeX file, basic reference metadata completeness, and transparency of the search-method description. It does not re-open all primary PDFs and is not a source-level re-verification of every scientific statement.

## Citation and bibliography checks

- The manuscript contains 35 `\\cite{...}` commands and 83 individual citekey mentions.
- There are 19 distinct citekeys in the manuscript.
- The curated cited-reference BibTeX file contains 19 entries.
- All 19 used citekeys resolve to exactly one entry in the curated bibliography; no bibliography entry is unused.
- All 19 entries contain author, title, year, journal and DOI fields.
- No duplicate DOI was detected within the 19-entry curated bibliography.
- No citation command remains inside an inline-code span after the final N-rGO citation-markup repair.
- Citation-key completeness is not equivalent to final reference-style rendering. The target journal or university style is still unspecified, so the bibliography remains in working citation notation.

## Search-method transparency check

The manuscript records 11 query formulations and dated focused discovery/search passes on 28, 30 and 31 October 2026. It also records the main source/index families identified in the project log and the source-access hierarchy.

The manuscript appropriately discloses the following limitations rather than inventing missing method details:
- The exact general discovery search-engine/platform name was not captured.
- Formal searches in Scopus and Web of Science are not documented as completed.
- No reconciled record counts by source, deduplication counts, title/abstract exclusions, full-text exclusion reasons or final systematic-review inclusion flow are available.
- The draft therefore describes a focused public-web discovery and narrative evidence synthesis, not a completed systematic review or PRISMA-compliant search.

The 51 candidate rows / 50 DOI-defined works count in the manuscript is a candidate-register snapshot after one known alias is excluded. It is not a PRISMA count and must not be presented as the final included-study total. The 15 primary-study records in the current synthesis are an editorial working set, not a fully reconciled formal inclusion flow.

## Current QC disposition

- Citation-key linkage: PASS.
- Curated bibliography core metadata presence: PASS.
- Duplicate DOI check within the cited bibliography: PASS.
- Citation command markup: PASS after repairing one inline-code citation in the N-rGO paragraph.
- Search-method transparency: PASS WITH LIMITATIONS — disclosures are accurate, but unavailable historic search details cannot be reconstructed without the original search log/history.
- Submission style and final rendered bibliography: PENDING target style selection.
- PRISMA/systematic-review flow: NOT CLAIMED; missing source-wise screening counts remain a blocker if the paper is later positioned as a systematic review.

## Remaining tasks

1. Preserve the current narrative-review positioning unless the original screening/search records can support a complete reproducible search flow.
2. Select the required university/journal reference style and render the bibliography accordingly.
3. Reconcile the 15-study empirical synthesis set against the current candidate register and evidence-readiness matrix before freezing the final included-study table.
4. Consolidate the six humic-acid matrix-chemistry staging records into the master evidence CSV when convenient; keep them explicitly contextual and outside the graphene adsorption comparison.
5. Run a final table/figure cross-reference, units, abbreviations and copy-edit pass only after the scientific content is frozen.

## Files checked

- `manuscript/SEMESTER_MANUSCRIPT_WORKING_V1.md`
- `references/semester-manuscript-cited-references.bib`
- `data/semester-manuscript-claim-evidence-audit.csv`
