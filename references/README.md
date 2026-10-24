# References and Zotero workflow

Zotero is the reference manager and PDF library; this folder is for citation exports and metadata snapshots, not full-text PDFs.

## Next action: export the seven core papers

Create or use a Zotero collection called **Antibiotic Adsorption Review — Core 7** and place the seven initial core papers in it:

- Atta et al. (2023)
- Alidadi et al. (2018)
- Delmond et al. (2023)
- Conde-Cid et al. (2021)
- Míguez-González et al. (2023)
- Li et al. (2019)
- Mohammed-Ridha & Abdul-Ahad (2014; verify publication year against the original record)

Then export that collection:

1. Install the free [Zotero Better BibTeX extension](https://retorque.re/zotero-better-bibtex/) if it is not already installed.
2. In Zotero, right-click **Antibiotic Adsorption Review — Core 7** → **Export Collection…**.
3. Choose **Better BibTeX** as the format and save it as `core-papers.bib`.
4. For the first handoff, leave **Keep updated** unchecked unless you are exporting directly into a locally cloned repository folder. That option updates the local export file; it does not by itself upload changes to GitHub.
5. Upload the exported `core-papers.bib` here in the chat for review, or upload it to this folder in the GitHub web interface.

After receiving the file, check the exported metadata for missing DOIs, duplicated records, title/year inconsistencies and citation keys before treating it as the reference snapshot.

## Suggested structure

- `core-papers.bib` — stable citation export for the initial seven core papers
- `library.bib` — optional broader bibliography export once the core workflow is working
- `collections/` — optional section-specific exports
- `README.md` — export procedure and notes on how files were generated

## Export rules

1. Verify DOI, title, authors, publication year and journal against the publisher/original article record.
2. Keep full text in Zotero or another appropriate licensed repository.
3. Use Zotero to insert in-text citations and generate the bibliography in the document editor.
4. If using Better BibTeX, use stable citation keys and record the export date in the commit message.
5. A `.bib` export is bibliographic metadata, not a full-library backup and not a substitute for keeping the Zotero library.
6. Avoid committing PDFs or private notes that should not be shared. The repository is private today, but it should still follow good research-data practices.

No automatic Zotero-to-GitHub synchronization is configured. Begin with a manual export and upload; this is free, transparent and sufficient for the current project.
