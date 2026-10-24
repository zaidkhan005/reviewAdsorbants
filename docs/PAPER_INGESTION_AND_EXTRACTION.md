# Paper ingestion and evidence extraction protocol

## Purpose

This document defines how a paper moves from a citation in Zotero to verified evidence that can be used in the review manuscript. A citation export is an inventory of records; it is not full text and is not evidence extraction.

## 1. Identify the paper

For each item, capture:
- stable Zotero/BibTeX citation key;
- title, authors, year, journal and DOI;
- publisher or trusted landing-page URL;
- manuscript section/material category it may support;
- current status: `METADATA-ONLY`, `FULLTEXT-NEEDED`, `FULLTEXT-RECEIVED`, `EVIDENCE-EXTRACTED`, `EVIDENCE-VERIFIED`, `ACCEPTED`, or `EXCLUDED`.

Do not infer that a paper has been read from its presence in Zotero, a .bib export, a search result, an abstract, or a GitHub PDF listing.

## 2. Obtain readable full text

Use the first available route:
1. User uploads the PDF in the chat.
2. User provides the DOI or publisher URL and the complete paper is available through legitimate open access or another accessible full-text source.
3. User retrieves the paper through AMU/institutional access or another lawful source and uploads the PDF for analysis.

If only an abstract is accessible, record that the abstract was reviewed and set the full-text status to `FULLTEXT-NEEDED`. Do not extract unreported experimental values from search snippets or infer values from another review. Do not bypass paywalls or access controls.

The assistant cannot automatically see the user's local Zotero attachments. The current GitHub file-reading connection also does not itself read binary PDFs merely because they are in the repository. When the PDF has been uploaded or accessible full text has been retrieved, inspect the text and relevant rendered pages when tables, charts, equations or scanned text need visual checking.

## 3. Extract the study evidence

Use the original paper's Methods, Results, tables, figures, captions, and supplementary information when supplied. Record the precise source location (PDF page and table/figure/supplement identifier) for each important value.

For each adsorbent–antibiotic pairing, capture when reported:
- adsorbent identity, material class, feedstock and preparation/modification route;
- target antibiotic and whether the study is genuinely adsorption-focused;
- initial concentration, pH, temperature, adsorbent dose, contact time, particle size, agitation, solution volume, matrix and competing species;
- observed uptake and removal percentage separately;
- fitted `qmax` separately from observed uptake, with isotherm model, fitting conditions and fit quality if available;
- kinetic model, rate parameters, transport analysis and limits of interpretation;
- pKa/speciation and surface charge/pHpzc context where available;
- proposed mechanism and the experimental evidence used to support it;
- desorption method, desorption efficiency and number of regeneration cycles;
- synthetic versus spiked real-water versus untreated real-water testing;
- batch versus continuous-flow/fixed-bed testing and any breakthrough information;
- preparation chemicals, energy, yield, cost, leaching, end-of-life, and scale-up findings;
- the authors' stated limitations and any data inconsistencies.

Use `Not reported`, `Not accessible`, or `Unclear in source` where appropriate. Do not fill gaps with guessed numbers.

## 4. Validate before accepting an extracted value

For every consequential number:
1. Read the methods and the relevant original table/figure together.
2. Confirm units and distinguish mg/g, mg/L, percentage removal, equilibrium uptake, and fitted `qmax`.
3. Check adsorbent dose, initial concentration, pH, time and matrix before comparing performance with other studies.
4. Recalculate conversions only when the underlying inputs support it; record the calculation.
5. Flag contradictions between abstract, narrative, table, figure or supplementary information.
6. Mark uncertain values `Needs verification`; do not quietly choose whichever number looks most plausible.

For a mechanism, distinguish direct experimental evidence (e.g., supported characterization/control evidence) from an author's suggested interpretation. A fitted kinetic/isotherm model alone is not proof of a unique molecular mechanism.

Separate adsorption from catalytic oxidation, peroxymonosulfate activation, photocatalysis, contaminant transformation and membrane rejection. Such studies must not be counted as adsorption-only evidence without separating the processes.

## 5. Write a source-linked evidence note

Each paper note should include:
- complete citation and DOI;
- file/access status;
- a short study-design summary;
- extracted values with units and page/table/figure locations;
- mechanism evidence and limitations;
- contradictions and unresolved questions;
- which manuscript claim(s) the paper supports and which it does not support;
- confidence/status of the extraction.

The structured CSV evidence register is the comparative index; the paper note preserves context and the audit trail. Neither replaces the original paper.

## 6. Commit to GitHub

Store metadata, source URLs, extracted evidence, status and caveats in GitHub. Keep full-text PDFs in Zotero or another appropriate licensed repository; only store PDFs in GitHub where the applicable terms permit it. Do not include private notes or credentials inadvertently.

For each evidence batch:
1. Process a small, coherent batch (typically 2–4 papers from one material category).
2. Extract values and note source locations.
3. Recheck the highest-risk numbers and inconsistencies.
4. Update the screening register, evidence CSV and source-caveat register.
5. Run the repository validator.
6. Log the changes and outstanding gaps.
7. Only draft the section once there is enough verified evidence to support its claims.

## 7. Handle papers not yet uploaded

A DOI/title is sufficient to start identifying a candidate and finding legitimate full-text options. It is not sufficient to assert that the full paper has been read. If a complete, accessible version cannot be found, leave the item in `FULLTEXT-NEEDED` and ask the user to upload a copy they can lawfully access.

## 8. Journal quartiles are a separate check

Full-text reading and Q1 status are independent. Confirm the ranking provider, year, subject category, quartile and source URL separately. Do not infer a quartile from the journal's impact factor, reputation or the paper's citation count.
