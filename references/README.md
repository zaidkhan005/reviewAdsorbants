# References and Zotero workflow

Zotero is the reference manager and PDF library; this folder is for citation exports and metadata snapshots, not full-text PDFs.

## Immediate next step: inventory the full downloaded collection

Do not limit the first inventory to the initial seven core papers. The goal is to discover and screen all relevant papers already downloaded, then prioritise which ones deserve full-text evidence extraction.

### 1. Create/confirm Zotero collections

- **Antibiotic Adsorption Review — Unscreened**: all papers downloaded that might be relevant to this review.
- **Antibiotic Adsorption Review — Core 7**: retain the original seven seed papers as a distinct reference group.
- Optional later: section-specific collections for raw biomass, clays/biopolymers, biochar, engineered/nano-carbon, and excluded papers.

In Zotero, an item can belong to more than one collection. Preserve the Core 7 classification while also including these items in the Unscreened collection if they are part of the broader corpus. Do not move or delete papers just to make the inventory export work.

If PDFs are not yet in Zotero, drag them into the Unscreened collection or import them in batches. Let Zotero retrieve metadata where possible; manually inspect records with missing or incorrect titles, authors, year, journal, or DOI.

### 2. Export the broader corpus

1. Right-click **Antibiotic Adsorption Review — Unscreened** → **Export Collection…**.
2. Choose **Better BibTeX**.
3. Uncheck **Export Notes**, **Export Files**, and **Include Annotations** to keep the export focused on bibliographic records. Uncheck **Use Journal Abbreviation** so journal names are easier to verify. Leave **Keep updated** unchecked for this manual handoff.
4. Save as `review-corpus.bib`.
5. Upload that exported file into this chat for an initial metadata audit.

If Better BibTeX export is unavailable, use Zotero's built-in BibTeX/RIS export. We can inspect the resulting format too.

### 3. Inventory first; extract evidence second

The bibliography export is an inventory, not the papers themselves. Use it to:
- detect duplicate or near-duplicate records;
- find missing DOIs and incomplete metadata;
- sort papers by year, journal, and material category where the metadata permit;
- identify records needing abstract/full-text screening.

Abstracts may or may not be included in the export; we will inspect the actual file instead of assuming they are present.

After the metadata pass, obtain the actual PDFs for the highest-priority papers. Keep PDFs in Zotero or another appropriately licensed location. Upload readable full texts in coherent batches for extraction, or provide DOI/landing-page links so accessible full texts can be checked. A DOI or citation alone is not proof that the full paper has been read.

### 4. Use simple screening statuses

Use Zotero tags or the GitHub screening register with a small set of states:
- `SCREEN-NEW`
- `FULLTEXT-NEEDED`
- `FULLTEXT-RECEIVED`
- `EVIDENCE-EXTRACTED`
- `EVIDENCE-VERIFIED`
- `EXCLUDED`

Record why a paper is excluded (e.g. degradation-only, not an antibiotic, not an adsorption study, duplicate, outside scope). Don't label a paper Q1 verified until its provider, ranking year, category, quartile, and source URL have been checked independently.

## Suggested repository files

- `review-corpus.bib` — the broader set of candidate references; add to GitHub only after a quick check for sensitive fields
- `core-papers.bib` — optional export of the original seven core papers
- `collections/` — optional later section-specific exports
- `README.md` — instructions and export date

## Export rules

1. Verify DOI, title, authors, publication year and journal against the publisher/original article record.
2. Keep full text in Zotero or another appropriate licensed repository.
3. Use Zotero to insert in-text citations and generate the bibliography in the document editor.
4. If using Better BibTeX, use stable citation keys and record the export date in the commit message.
5. A `.bib` export is bibliographic metadata, not a full-library backup and not a substitute for keeping the Zotero library.
6. Avoid committing PDFs or private notes that should not be shared. The repository is private today, but it should still follow good research-data practices.

No automatic Zotero-to-GitHub synchronization is configured. Begin with a manual export and upload; this is free, transparent and enough for now.
