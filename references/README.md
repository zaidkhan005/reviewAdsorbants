# References and Zotero workflow

Zotero is the reference manager and PDF library; this folder is for citation exports and metadata snapshots, not full-text PDFs.

## Suggested structure

- `library.bib` — optional BibTeX export, preferably with stable citation keys
- `collections/` — optional BibTeX/RIS exports per manuscript section
- `README.md` — export procedure and notes on how files were generated

## Export rules

1. Verify DOI, title, authors, publication year and journal against the publisher record.
2. Keep the full text in Zotero or an authorized institutional repository.
3. Use Zotero to insert in-text citations and generate the bibliography in the document editor.
4. If using Zotero Better BibTeX, use stable citation keys and record the export date in the commit message.
5. Avoid committing PDF files or private notes that should not be shared. The repository is private today, but it should still follow good research-data practices.

No automatic Zotero-to-GitHub synchronization is configured yet. Initially, export `.bib` manually and commit the bibliographic metadata.