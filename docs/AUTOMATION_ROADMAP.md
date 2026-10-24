# Automation roadmap

## Principle

Automate repeatable bookkeeping and metadata handling; keep scientific judgments human-verified. Automation may discover candidates, normalize metadata, remind us of missing fields, and flag inconsistencies. It must not automatically assert that a paper is Q1, accept a mechanism claim, or treat a fitted qmax as validated.

## What is now automated in this repository

- GitHub Actions runs `scripts/validate_research_register.py` when research-register CSVs or the validator workflow change.
- The validator checks required columns, unique candidate IDs, year formatting, source links, and that any `Q1` label is accompanied by provider, year, category and verification URL.
- The validator does not independently verify the ranking result or scientific claims.

## Suggested next automation steps

### 1. GitHub Issues as a review queue
Use one issue per work block or unresolved question. Suggested labels:
- `candidate-paper`
- `full-text-needed`
- `q1-pending`
- `evidence-check`
- `citation-needed`
- `ready-to-draft`
- `resolved`

A paper should move from candidate to accepted only after full text, quartile verification and evidence extraction have been checked.

### 2. Zotero export
Keep PDFs and notes inside Zotero. Consider Zotero Better BibTeX (a Zotero desktop extension, not a ChatGPT connector) to maintain stable citation keys and export a `.bib` file. Commit bibliographic metadata/BibTeX only where useful and permitted; do not put PDFs in GitHub. Decide whether the exported bibliography is updated by manual export initially or by a later script.

### 3. n8n for metadata enrichment (optional, later)
If an n8n instance is running and accessible, a workflow could:
1. Trigger on a new GitHub issue or manual form submission.
2. Fetch DOI metadata from Crossref/OpenAlex.
3. Populate title, authors, year, journal, DOI and publisher URL in a draft record.
4. Open a pull request or comment with the proposed metadata.
5. Leave quartile, paper inclusion, extracted capacity and mechanisms as `PENDING` until verified by a human against trusted sources.

Do not assume that the public `n8n` repository means an automation server is running. No credentials or tokens should be stored in the repo; use GitHub Actions secrets or an appropriately secured credential store.

### 4. Citation and source checks
- Use Consensus for discovery when available; track its usage limit.
- Use SciSpace for a second discovery/extraction pass when accessible.
- A citation-context tool such as Scite can help determine whether later papers support or contradict a key claim; this is a secondary check, not a replacement for reading the source.
- Firecrawl can be useful for extracting relevant public publisher/journal pages, but obey access restrictions and do not use it to bypass paywalls or copy copyrighted full text.
- DOI metadata services can help resolve citations, but they cannot certify Q1 quartiles.

## Recommended minimum stack

**GitHub + GitHub Actions + Zotero + Better BibTeX + Consensus/SciSpace.** Add n8n only after the manual process is stable and the specific trigger/action is clear. Use GitHub as the project record so we do not split decisions across competing notebooks.

## Current opportunities

1. Add DOI-based metadata enrichment from Crossref/OpenAlex.
2. Export a stable Zotero bibliography into `references/`.
3. Add a GitHub issue template for candidate-paper submissions.
4. Add a simple evidence-note template and validate required fields.
5. Only after these work, consider scheduled searches or repository notifications.