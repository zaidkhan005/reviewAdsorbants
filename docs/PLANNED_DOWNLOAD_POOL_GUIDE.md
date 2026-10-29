# Planned literature download pool — 27 October 2026

## Current status note (2026-10-29)

This file is a discovery/screening pool, not a list of items the user must download now. The user has paused new downloads/uploads. Continue from existing Library PDFs, current registers and legitimate accessible source text; revisit user download requests only if the user explicitly reopens them.


## What this file is

`data/planned-download-pool.csv` contains **250 planning-pool records**: 67 existing, relevant/pending records taken from the current screening register, plus 183 newly surfaced discovery leads. The only existing-register row deliberately left out is `CORP-062`, which is already marked as unrelated/out of scope. This is a *discovery and download plan*, not a final bibliography or 250 accepted papers.

- Existing records retain their current IDs and status. Do not redownload full texts that are already present and reviewed.
- `DISC-022` remains **deferred** pending the user's full-text PDF. It is not screened or excluded.
- New rows have DOI/publisher links. Where a valid PMC identifier was supplied by the search index, the file includes a PMC full-text page; otherwise use the DOI landing page and AMU institutional access where available.
- New items are based on indexed paper titles/abstracts and DOI metadata. Publication year and journal were left blank rather than guessed where the search index did not return reliable values; verify them at the landing page or in the downloaded PDF.
- Quartiles are **not audited for new records**. Do not assume Q1 from impact factor, title, or a current journal profile. Apply the project's publication-year/category/provider audit later.
- A candidate may study adsorption alongside degradation, oxidation, membranes, or disinfection. The row's cross-cutting tags flag some such cases; extract adsorption-only results separately and reject items that do not fit the scope.
- Exact DOI and normalized-title deduplication were performed against the current register before selection. A final bibliographic de-duplication pass is still required after the Better BibTeX export.

## How to work through the file

Open/filter the CSV in Excel or another spreadsheet. Start with **Batch 1 — first 30**, then **Batch 2 — next 50**; Batch 3 is the remaining 103 new leads. Within the batch, `P1` indicates the highest-value candidate score based on title/abstract signals, but it is not a screening decision. Download PDFs from legal publisher/open-access sources available to you; do not upload only the abstract page. When uploading to ChatGPT, use small named batches and preserve the paper title/DOI in the filename or accompanying manifest.

For each new paper, the screening workflow remains: verify full text and adsorption-only scope → extract source-pinned evidence → record the page/table/figure → audit journal quartile for the relevant year/category/provider → cite through Zotero/Better BibTeX only when the manuscript actually uses it.

## Target interpretation

The planned pool size is now **250 records**. The 60-reference semester target and 150-reference publisher/journal target refer to distinct, relevant works actually cited in the manuscript, not downloads or candidate rows. Screening will likely reject some pool items, and the final bibliography count must be measured from the Zotero/Better BibTeX export after citation conversion. Expand the pool if screening leaves too few eligible and useful works.

## Coverage notes

The new discovery set was searched across biochar, raw biomass, natural clays, biopolymers, activated/advanced carbon, real-matrix/fixed-bed/regeneration/cost applications, and cross-cutting mechanisms. Classification is provisional. Particularly check the distinction between natural clay and acid/alkali-activated clay; unmodified biopolymer and polymer composite; pristine biochar and chemically/metal-modified biochar; adsorption and degradation; synthetic water and real wastewater.

Search record metadata: DOI / PubMed / PMC links are preserved row by row in the CSV. Search index excerpts are discovery aids, not a replacement for the original source.
