# Zotero intake — one full corpus, no manual reorganisation

**Goal:** Build one inventory of all downloaded candidate papers, including the original seven. Do not sort papers into material-specific collections or spend time retagging them before screening.

## Your only Zotero preparation task

1. Create one collection called **Antibiotic Adsorption Review — Full Corpus**.
2. Add the original seven seed papers and every other downloaded paper that might be relevant. If an item already lives in another collection, add it to this collection; do not delete it from its existing collection.
3. Import any relevant PDFs that are only sitting in a local folder and are not yet in Zotero.
4. Do not manually assign material categories, processing stages, Q1 status, or section tags. We'll screen and classify those from the sources.

## Export the whole collection once

1. Right-click **Antibiotic Adsorption Review — Full Corpus** → **Export Collection…**.
2. Choose **Better BibTeX**.
3. Uncheck **Export Notes**, **Export Files**, and **Include Annotations**.
4. Uncheck **Use Journal Abbreviation** so full journal names remain available to check.
5. Leave **Keep updated** unchecked for this first handoff.
6. Save as **`review-corpus.bib`** and upload it directly in the chat.

If Better BibTeX is unavailable, export with Zotero's built-in BibTeX or RIS and tell me which format you used.

## What happens next

1. Audit the entire bibliography for duplicates, missing metadata and suspect records.
2. Create one unified screening register; the user does not need to sort every paper by material class.
3. Screen the full list using title, abstract and legitimate metadata/full-text access where available.
4. Prioritise actual PDFs for small-batch reading. Begin by rechecking the original seven studies as a calibration batch; their previous evidence values are leads, not assumed verified results.
5. Extract evidence with page/table/figure locations, verify values and mechanisms, and then draft against the preserved outline.

## Important distinction

`review-corpus.bib` is a reference inventory, **not the PDFs themselves**. These export settings do not include attachments. Abstracts may or may not be included, so inspect the actual exported file rather than assuming they are present. Zotero's local attachments do not automatically appear in chat.

Full text can be uploaded here in small, coherent batches or reached from a DOI/publisher URL when a complete version is legitimately accessible. If a full text cannot be accessed, we'll mark it `FULLTEXT-NEEDED` rather than inventing study details. Keep publisher PDFs in Zotero or another appropriate licensed location; only put PDFs in GitHub if the relevant licence permits it.

## Project files

- `docs/CORPUS_RESET_AND_RESTART.md` — restart plan and rules
- `data/corpus-screening-template.csv` — starting columns for the unified screening register
- `data/master-evidence-detailed.csv` and `data/source-caveats.csv` — retained historical seed data to re-verify, not automatically accepted evidence

No automatic Zotero-to-GitHub synchronisation is configured or required. Manual export is enough to begin.


## Latest Better BibTeX export audit

- [2026-10-29 export audit](BBT_EXPORT_AUDIT_2026-10-29.md)
- [Full 164-entry processing queue](bibtex_full_corpus_processing_queue_2026-10-29.csv) — shows which bibliography entries have candidate records/evidence, which still need screening, and priority based on title-only relevance signals.
- [100-candidate DOI-to-key crosswalk](bibtex_candidate_key_crosswalk_2026-10-29.csv) — exact DOI matches, duplicate-key ambiguities, title-only matches and candidates not represented in this export. — the uploaded `full ++.bib` was audited: 164 entries, 159 unique DOI values, two duplicate DOI/title groups, four records/version issues requiring Zotero cleanup, and one DOI-matched publication-year conflict requiring correction. The claim ledger has been populated with the three verified DOI-to-key mappings used by its nine seed claims.
- Downloadable parsed reference inventory audit: keep the local file `bibtex_reference_inventory_audit.csv` as a working QA artifact; it is not a substitute for the Better BibTeX export.
- After resolving duplicate Zotero items and metadata gaps, re-export the collection and refresh claim-to-key mappings. The target journal citation style remains to be chosen; final in-text citations and bibliography must be rendered through Zotero or the selected citation processor rather than typed by hand.
