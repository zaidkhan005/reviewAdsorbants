# Reference target and acquisition plan

## Live status overlay (2026-10-29)

- Broad corpus: 111 candidate records, 505 evidence rows, 41 journal-audit records, and 164 entries in the current Better BibTeX processing queue. The 505 rows are findings, not studies or accepted citations, and some evidence remains provisional/staged.
- The 250-row planned discovery pool in `data/planned-download-pool.csv` already exists. Do not calculate a current discovery deficit by simply subtracting the 111-row register from 250; the pool and register have different composition and need DOI/title crosswalking.
- Broad-review targets remain about **60 distinct works actually cited** for the semester version and **150 actually cited** for the journal version; the final bibliography count is not audited.
- Separate semester paper: approximately **50 distinct works actually cited**, locked to selected graphene-based adsorbents/composites for CIP and TC. Its register has 40 candidates and its dedicated evidence CSV has 16 rows. Do not merge its reference target into the broad-review targets.
- No new download/upload is being requested from the user. Continue using existing files, evidence and legitimate accessible source text.


## Objective

The user's supervisor suggested about 60 references for a semester publication and around 150 for the journal version. For the current broad review, use **~150 distinct, relevant works actually cited** as a provisional journal-manuscript target—not a universal publisher requirement. Check the eventual target journal's current author instructions and review-article type before submission.

A reference-count target is not permission to pad. If the evidence supports a smaller number, continue discovery or revise the target transparently rather than adding weak/irrelevant citations.

## Current status

As of 2026-10-27, the canonical `data/corpus-screening-register.csv` contains **68 candidate rows**. The master evidence file has records for 59 distinct candidate IDs, but it mixes primary-study and review/background evidence and therefore is not a bibliography count. The previous screening checkpoint had 61/62 candidates full-text screened. After the first documented discovery pass, the register now has 68 rows: those 61 prior full-text screens remain, `DISC-022` remains deferred/not screened/not excluded, and six new candidates are at discovery stage awaiting full-text/source review. Final retain/exclude decisions and journal-eligibility rules remain provisional. The `references/` folder currently contains export instructions, not a current `review-corpus.bib` file, and manuscript citation conversion is pending. Therefore, **the number of distinct works actually cited in the final bibliography has not yet been audited**; do not report either reference target as achieved from the candidate count alone.

## Historical reference-count dashboard — 2026-10-27 (superseded by live status overlay)

| Measure | Current status | Interpretation |
|---|---:|---|
| Semester manuscript target | **~60 distinct cited works** | Target from the supervisor; not confirmed as met because the final in-text citation/bibliography count has not been generated. |
| Publisher/journal-version target | **~150 distinct cited works** | Working target, subject to the eventual journal's article type and author instructions. |
| Historical screening inventory at 2026-10-27 checkpoint | **68 candidates** | Accurate for that dated snapshot; current register has 111 candidates. Candidate rows are not accepted papers or cited bibliography entries. |
| Evidence register coverage | **59 distinct candidate IDs** | Includes primary studies and review/background evidence; not a unique accepted-paper count. |
| Final bibliography count | **Not audited** | No current `review-corpus.bib` export is stored in `references/`, and in-text citation conversion is pending. |
| Candidate-pool planning range for the ~150-reference version | **220–250 records** | Planning funnel to allow for duplicates, exclusions, inaccessible full texts, ranking rules and evidence quality. |
| Historical estimate of candidate gap | **~152–182** | Estimate made from the 68-row register on 2026-10-27; not a live count and not recalculated by subtracting current register rows from pool size. |

The 60-reference checkpoint and the 150-reference journal target must be tracked as **distinct works actually cited**, not as PDFs uploaded, candidates screened, evidence rows, or papers mentioned only inside other reviews. A source may be discovered or extracted and still not belong in the final bibliography if it is irrelevant, duplicative or unsupported.

## A practical acquisition funnel

To end with ~150 defensible citations, build a pool of roughly **220–250 candidate references** through targeted searching and citation chasing, then screen it down. This range is a planning estimate, not a guarantee: actual acceptance may be lower or higher depending on relevance, access, evidence quality, Q1 eligibility, duplicates, and target-journal rules.

At the 2026-10-27 checkpoint, the 68-row register led to the historical estimate of **152–182 additional candidate records** to reach the 220–250 pool. That estimate is superseded by the populated 250-row pool and later intake; reconcile pool/register DOI/title matches rather than using simple subtraction. Every search must answer a defined gap in the outline.

## Provisional makeup of a 150-reference bibliography

These buckets are for coverage planning only. Assign each distinct work one main counting role, while allowing multiple topical tags. A source cited in two sections still counts as one reference.

| Main role for the source | Approximate target | What belongs here |
|---|---:|---|
| Primary adsorption studies across the eight material classes | 75–85 | Raw biomass; natural clays; unmodified biopolymers; pristine biochar; modified biochars; atomically doped biochars; activated carbon; CNT/graphene-based carbons |
| Cross-cutting experimental evidence not counted above | 15–20 | Real-water matrices, mixed contaminants, low-concentration tests, regeneration, column/fixed-bed operation, breakthrough and scale-up |
| Mechanism, kinetics, isotherm, speciation and modelling foundations | 15–20 | Directly relevant primary studies and foundational methods supporting interpretation; avoid treating model fits as molecular proof |
| Processing, cost, energy, lifecycle and sustainability evidence | 10–15 | Preparation yield, activation chemicals, process energy, cost normalization, life-cycle assessment, residuals and end-of-life |
| Occurrence, ecotoxicology, wastewater treatment and policy/context | 10–15 | Reliable background sources that directly support the introduction and implementation discussion |
| High-quality reviews used for field mapping and future directions | 10–15 | Recent reviews for reference chasing and synthesis; do not use reviews as the sole source for exact experimental claims |
| **Total planning range** | **135–170** | Target ~150 after screening; the buckets are flexible and not independent hard quotas |

A paper can support multiple themes, but count each distinct DOI/work only once. If a category has few strong adsorption-only studies (especially atomically engineered biochar), report that gap honestly; do not manufacture a quota.

## Search sources — university access available

Do not restrict the search to open-access/free sources. The user can download most papers through university access, so prioritise coverage, relevance and study quality across:

- **Scopus and Web of Science** through the university library for structured, exportable queries, de-duplication and citation chasing.
- **Publisher platforms** (Elsevier/ScienceDirect, SpringerLink, Wiley, ACS, RSC, MDPI and other relevant publishers) for original article text, supporting information, methods and tables.
- **Google Scholar** and cited-by/reference-list trails as supplementary discovery routes.
- **Crossref/OpenAlex** for metadata normalization, not as a substitute for reading the paper.
- **Consensus/SciSpace** where useful and available, with source verification against the original study.
- **JCR/SJR** for separate journal quartile verification.

I cannot automatically enter the user's institutional credentials or view a university-authenticated browser session. Where a subscription PDF is needed, identify the citation and have the user download it through the university and upload the PDF. Do not ask for passwords or bypass access restrictions.

## Search effort by outline

Use the original outline and the working manuscript's separately numbered mechanisms section as the search map.

1. **Section 1 — Introduction:** antibiotic occurrence, environmental concentration ranges, ecotoxicity/resistance risks, wastewater-treatment removal limitations, and appropriate context sources.
2. **Section 2.1 — Raw biomass:** raw or minimally processed husks, bark, sawdust, timber waste, and agro-food/forestry residues.
3. **Section 2.2 — Natural clays and unmodified biopolymers:** bentonite/montmorillonite, kaolinite, sepiolite/stevensite, unmodified chitosan/cellulose/alginate; distinguish modified polymers/composites.
4. **Section 2.3 — Standard and chemically modified biochar:** studies with clearly documented pyrolysis/feedstock, pristine controls, acid/base activation, pore/functionality changes and reagent burdens.
5. **Section 2.4 — Precision-engineered/nano-carbons:** adsorption-focused atomically/heteroatom-doped biochars, activated carbon (PAC/GAC/commercial and waste-derived), CNTs, GO/rGO. Keep catalysis and membrane rejection separate.
6. **Section 3 — Kinetics, isotherms and solution chemistry:** ensure original experimental evidence for conditions and model validity; capture low-concentration performance as well as high-concentration isotherms.
7. **Section 4 — Mechanisms:** primary sources with characterization, controls, spectroscopy, competition/pH experiments or other support. Separate evidence from author interpretation.
8. **Section 5 — Techno-economics, energy and regeneration:** quantify chemicals, washing/neutralization, yield, energy, regeneration cycles, cost per mass removed, life-cycle boundary and spent material.
9. **Section 6 — Practical implementation:** real wastewater versus synthetic water, natural organic matter, competing ions, mixtures, continuous flow, breakthrough, scale-up, and integration.
10. **Sections 7–8 — Challenges and conclusions:** synthesize genuinely demonstrated gaps and future work rather than adding papers just to fill space.

## Search channels and reproducible process

For each outline section:
1. Run 3–6 distinct targeted searches with material names, antibiotic names, and the key condition (e.g., real wastewater, regeneration, column, lifecycle cost).
2. Search recent high-quality reviews for backward citation chasing.
3. Use "cited by" trails to find important older and newer primary studies.
4. Check open-access repositories, publisher pages and institutional access for full texts; do not bypass paywalls.
5. Deduplicate by DOI and normalized title before counting.
6. Record database/platform, exact query, date, filters and screened/included/excluded counts.
7. Screen titles/abstracts before requesting full PDFs.
8. Extract full-text evidence with PDF page/table/figure locations and log unresolved data.
9. Verify journal quartiles independently. Do not infer Q1 from impact factor or reputation.

Metadata-only candidates in the current register are not considered read, included, or Q1-verified. Citation chains from reviews are a discovery tool, not a substitute for checking original study data.

## Quality filters

- The main experimental comparison should be dominated by relevant original studies; reviews support context and map the literature.
- If a Q1-only eligibility rule is adopted for a particular subset, record the ranking provider, year, category, quartile and source URL for every included item. Do not silently apply one quartile system to another.
- Foundational methods, environmental standards, regulatory documents and seminal papers may not be journal articles or may not have relevant quartile data; identify their role explicitly rather than mislabelling them Q1.
- Exclude or clearly separate studies whose removal pathway is catalytic oxidation, PMS activation, photocatalysis or membrane rejection instead of adsorption.
- Distinguish antibiotics from other pharmaceuticals (for example, diclofenac is an NSAID) and tag mixed-target studies accurately.
- Count distinct works cited in the manuscript, not downloaded PDFs, search result hits, duplicate versions or references inside review bibliographies that are not actually cited.

## Milestones

- **M1 — Inventory:** audit the currently downloaded 31-reference export and normalize metadata (done as preliminary inventory).
- **M2 — Candidate pool:** grow the register toward 220–250 records through documented gap searches and citation chasing.
- **M3 — Screened evidence base:** decide retain/exclude/pending based on relevance, study type, article metadata, full-text access and journal rules.
- **M4 — Verified evidence:** re-read the original seven and each retained study; validate capacities, conditions, mechanisms and practical claims.
- **M5 — ~150-reference draft:** target around 150 distinct citations distributed across the outline. Only count references that are actually cited and support a claim.
- **M6 — Target-journal adaptation:** check the actual journal's word/reference limits and adjust the final number without weakening evidence quality.

## Execution plan — how the two targets will be reached

### Stage A: reach the semester manuscript target (~60 works actually cited)

1. **Reconcile the current library and manuscript.** Export the Zotero collection as `review-corpus.bib` using the instructions in `references/README.md`. This is a bibliography export, not a request for another PDF batch. Deduplicate DOI/title variants and map existing manuscript claims to sources. The repository currently does not contain a current `.bib` export, so the actual unique-citation count is not yet known.
2. **Historical step (2026-10-27): audit the then-current 68 candidates.** That checkpoint is now superseded by the 111-row register and current crosswalk work. `DISC-022` remains deferred in the broad review, but the user has paused downloads; do not ask for that PDF while the pause is active. Candidate rows are not accepted references.
3. **Use an initial 60-reference coverage plan** (main counting role per distinct work; secondary thematic tags can overlap): 32 primary adsorption studies; 8 cross-cutting experiments (real-water matrices, regeneration, mixed feeds and columns); 7 kinetics/isotherm/speciation/mechanism foundations; 5 process-cost/energy/LCA sources; 4 occurrence/risk/treatment-context sources; and 4 high-quality reviews. This is a planning allocation, not a forced quota. If screening produces fewer than 60 genuinely useful sources, search the gaps rather than padding.
4. **Check whether the manuscript actually cites them.** A retained paper counts toward 60 only if it is used in the manuscript to support a statement/table row. Count each distinct DOI/work once, even if it appears in several sections. Duplicate preprint/published versions count as one work unless they contain materially distinct records and there is a justified reason to cite both.

### Stage B: grow the source pool for the journal version (~150 works actually cited)

Build and reconcile a deduplicated pool of **220–250 candidates** and screen it down to approximately 150 relevant works actually cited. The 250-row planned pool is present; use the crosswalk and screening decisions to resolve overlap rather than treating the historical 152–182 figure as a current net-new target. The funnel is a planning estimate, not an obligation to retain weak papers.

Use these source-acquisition passes, in order:

1. **Material-class gaps:** targeted primary-study searches for raw/minimally processed biomass; natural clays; unmodified biopolymers; standard biochar; chemically modified biochar; adsorption-only doped/engineered biochar; commercial and waste-derived activated carbon; and CNT/GO/rGO. Current planning coverage within the 80 primary-study target is: raw biomass 8, natural clays 8, unmodified biopolymers 6, standard biochar 8, modified biochar 14, doped/engineered biochar 8, activated carbon 14, and nano-engineered carbons 14. These are provisional coverage aims, not minimum quotas; mark a genuine evidence gap instead of padding a thin class.
2. **Application evidence:** searches focused on real wastewater (and its pretreatment), low-concentration feeds, multi-antibiotic competition, natural organic matter/ions, regeneration/desorption, fixed-bed breakthrough, long runs, spent media and leaching.
3. **Mechanism and model validity:** primary studies with spectroscopy/controls, pH/speciation, cation exchange, surface charge, pore characterization, mass-transfer evidence, kinetic/isotherm fit-quality and experimental-versus-model cross-checks.
4. **Processing and sustainability:** preparation yield, pyrolysis/activation energy, acid/base/solvent inputs, wash water and neutralisation, normalized cost per treated volume or mass removed, regeneration energy, LCA boundary, residual waste and end-of-life.
5. **Context and field mapping:** reliable sources for antibiotic occurrence, environmental risk, treatment limitations and recent reviews. Use reviews to locate original studies; do not cite review tables as the original source for a specific measured capacity.
6. **Backward/forward citation chasing:** follow references and cited-by trails from the strongest directly relevant reviews and primary studies to discover seminal and newer papers missed by keyword searches. Deduplicate every lead before it increases the net candidate count.

### Search cadence and screening funnel

- For each material class or cross-cutting gap, run 3–6 focused search strings combining target antibiotic names/synonyms with `adsorption`/`sorption`, material/processing route, and a useful operating dimension (real wastewater, low concentration, regeneration, column, cost/LCA).
- Search Scopus/Web of Science through university access when available; complement with publisher pages, Google Scholar/cited-by trails, Crossref/OpenAlex metadata, and legitimate open repositories. Record database, exact query, date, filters, returned hits and net-new deduplicated candidates.
- Add candidates in documented search passes, then screen title/abstract and metadata first. Obtain/read full text only for relevant candidates. Subscription PDFs that cannot be accessed legitimately from the available session can be downloaded by the user through university access later; do not request the user's credentials.
- Keep the journal ranking system, year and category as separate metadata. Apply the final Q1 rule only after the required provider/year/category is agreed; do not use an unverified current SJR flag as a substitute for a publication-year JCR/SJR decision.
- Keep a running unique-work count by DOI/normalized title, candidate role, material class, source status, and whether it is actually cited in the current manuscript. Reconcile it to the Zotero export and final manuscript before claiming either target is met.

### Central target for the journal version

| Main counting role (mutually exclusive for counting) | Target distinct works |
|---|---:|
| Primary adsorption studies across eight material classes | 80 |
| Cross-cutting application evidence (matrix, regeneration, mixture, column) | 18 |
| Mechanism, kinetics, isotherm and speciation foundations | 17 |
| Processing, cost, energy, LCA and end-of-life | 12 |
| Occurrence, risk, wastewater treatment and policy/context | 11 |
| High-quality reviews for synthesis and citation discovery | 12 |
| **Total** | **150** |

These counts assign each work one main role solely to prevent double-counting. The paper can have multiple topical tags. The eventual target journal's instructions may change the final reference limit; evidence quality and relevance take precedence over the target count.

### Definition of done for each target

- **~60 semester target:** at least 60 distinct relevant works are cited in the semester manuscript; every citation matches a real Zotero item; no candidate-ID DOI placeholder remains where a formal citation is required; cited works map to claims/evidence; the bibliography and in-text citations reconcile.
- **~150 journal target:** the expanded manuscript has around 150 distinct relevant works actually cited across the outline, the source pool and screening decisions are documented, every experimental value uses an original-source citation, and the target journal's current rules and the agreed Q1 policy have been checked.
- **Neither target is complete** merely because the candidate register, evidence table or Zotero library reaches that number. The count is the distinct works actually cited in the current manuscript version.

## Planned download pool created (2026-10-27)

A 250-record planning pool is available at [`data/planned-download-pool.csv`](../data/planned-download-pool.csv), with usage notes in [`docs/PLANNED_DOWNLOAD_POOL_GUIDE.md`](PLANNED_DOWNLOAD_POOL_GUIDE.md). When it was created on 2026-10-27, it combined 67 then-relevant/pending register records and 183 newly surfaced leads; the live broad register now has 111 rows. `CORP-062` remains in the register for audit but is excluded from that target pool as unrelated. `DISC-022` remains deferred in the broad review, and the user's download pause is active. The 183 leads are not accepted studies: full-text scope, article type, metadata and journal quartile may still need verification. The pool is a discovery aid, not proof of the 60/150 citation targets.
