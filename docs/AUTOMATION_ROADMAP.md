# $0-first research automation roadmap

## Principle

Keep the research workflow dependent on free tools and features already in use. Do not make n8n, a paid automation platform, or a paid research subscription a requirement. Automate repeatable bookkeeping and structural checks; keep scientific judgments human-verified.

The workflow should still be useful if every optional automation is turned off.

## What is already automated in this repository

- GitHub Actions runs `scripts/validate_research_register.py` when research-register CSVs or the validator workflow change.
- The validator checks required columns, unique candidate IDs, year formatting, source links, and whether a claimed `Q1` label includes a ranking provider, year, subject category, and verification URL.
- The validator checks structure and required evidence fields. It does not independently verify journal quartiles or scientific claims.

## Free-first workflow

### 1. GitHub as the project record

Use the existing repository for:
- dated session logs and decisions;
- screening register and evidence CSVs;
- one issue per unresolved research question or paper requiring follow-up;
- manuscript outline, drafts, and claim/citation rules.

Use the existing paper-candidate issue template rather than adding an external form service. GitHub Actions should remain limited to useful checks, and usage should stay within the account's available free quota.

### 2. Zotero and Better BibTeX

- Keep full-text PDFs and reading notes in Zotero or another appropriate licensed repository.
- Better BibTeX is a free Zotero desktop extension for citation keys and bibliography export.
- Initially export a `.bib` file manually into `references/` when references materially change. This is a simple, transparent step; do not build an automated sync until there is a real need.
- Commit bibliographic metadata only where useful and permitted. Do not commit copyrighted publisher PDFs unless the licence or publisher terms permit it.

### 3. Free metadata lookup

- Resolve missing DOI metadata through publisher records and public metadata services such as Crossref or OpenAlex when appropriate.
- Use public metadata to help normalize title, authors, year, journal, DOI and landing-page URL.
- Record the source used. Metadata lookup does not verify study findings, mechanism claims, or Q1 status.
- Respect service rate limits and terms. Do not depend on a service remaining available indefinitely.

### 4. Literature discovery and full-text verification

- Use whatever free access is currently available through Consensus, SciSpace, publisher open-access pages, institutional access, and repositories.
- Track usage limits and switch to source reading/manual metadata lookup when a free research service is capped.
- Use original research papers to verify experimental values and mechanisms. Reviews are useful for field mapping and reference discovery.
- Do not use scraping to bypass paywalls or access controls.

## Explicitly out of scope

- **n8n:** not part of the planned workflow because hosting or paid usage may introduce costs and operational overhead. Do not assume an n8n instance exists.
- Paid API subscriptions or paid automation services are not prerequisites.
- No service should automatically mark a paper as Q1 verified, accept a study, validate a fitted `qmax`, or approve a mechanistic explanation.

A future tool can be reconsidered only if it has a clear benefit and a confirmed zero-cost way to run within the user's constraints. No such tool is needed to proceed now.

## Minimum stack

**GitHub + GitHub Actions (within available free quota) + Zotero + Better BibTeX + freely available discovery/metadata sources.**

## Next useful steps

1. Reconcile Zotero metadata and stable citation keys for the core papers.
2. Add DOI and primary-source URLs for screening candidates.
3. Fill evidence fields after checking methods, tables, figures and supplements in the original papers.
4. Keep mechanism evidence distinct from authors' proposed explanations and from catalytic degradation.
5. Add further automation only when a specific manual bottleneck appears and a $0 option is confirmed.
