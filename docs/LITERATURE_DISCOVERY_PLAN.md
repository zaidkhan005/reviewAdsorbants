# Literature discovery plan — completing the bibliography

## Boundary condition

The user's Zotero Better BibTeX export currently contains **31 downloaded reference records**. These are a starting corpus, not the complete bibliography. The review's bibliography must be completed by additional structured searches, backward/forward citation chasing, and full-text screening.

The original outline controls the scope. Keep the processing-and-cost continuum and its core material classes:
1. Raw/unrefined lignocellulosic biomass.
2. Natural clays and unmodified biopolymers.
3. Standard biochar and chemically modified biochars.
4. Precision-engineered/atomic-site-doped biochars, activated carbon, and nano-engineered carbons (CNTs/GO).

Mechanisms are treated in a standalone section in the working outline. Cross-cutting dimensions include kinetics, isotherms, antibiotic speciation, adsorption mechanisms, regeneration, real-water effects, continuous-flow operation, energy/cost, secondary waste and scale-up.

## Initial metadata-only gap map

This is a preliminary diagnosis based on titles and available bibliography metadata, not final study inclusion:

- **Raw biomass / natural waste:** Several candidate primary studies are present, including raw rice husk, sawdust/timber waste, pine bark/ash/mussel shell, and forestry/agro-food by-products. Verify source values and look for stronger comparable conditions.
- **Natural clays:** Two promising primary-study records are present (raw/activated Tunisian clays and calcium montmorillonite). More clays/mineral sorbents and comparable reference studies may be needed.
- **Unmodified biopolymers:** The current list has reviews and composite studies; clearly classified primary studies of unmodified chitosan/cellulose/alginate appear sparse. Search for them explicitly.
- **Standard/pristine biochar:** Reviews are present, but dedicated primary studies on pristine biochar need to be identified and separated from chemically activated, iron-modified or catalytically active biochars.
- **Chemically modified biochar:** One strong candidate record concerns phosphoric-acid-activated sunflower-seed-husk biochar; add additional independent primary studies and compare activation routes.
- **Atomically doped biochar:** No clear adsorption-only primary study is obvious from the current titles. This is a priority gap, and must be separated from catalytic oxidation/electron-transfer degradation.
- **Activated carbon:** Two relevant records exist, including hospital effluent treated with GAC and biomass-derived activated carbon; expand evidence on commercial PAC/GAC, breakthrough/bed life and regeneration.
- **Nano-engineered carbons:** Several CNT/GO/N-rGO primary studies are present. Confirm their source data and look for independent replications and realistic matrix/operating conditions.
- **Mechanisms:** Existing reviews can guide search terms, but mechanism claims need primary-study evidence with characterization, controls or other direct support. A kinetic-model fit alone does not prove a unique mechanism.
- **Cost/energy and scale-up:** The current metadata does not show enough comparable process-energy, synthesis-yield, lifecycle-cost or normalized cost-per-mass-removed data. These may require a cross-cutting search and may reveal that evidence is sparse.
- **Real water and continuous flow:** GAC hospital-effluent evidence is a key lead; locate further real-water, fixed-bed and column studies. Keep membrane rejection and catalytic degradation separate.

Revisit this gap map after reading the relevant review papers and completing full-text screens. Do not treat the counts above as final evidence.

## Search sources

Use a free-first mix and record the database/search date:
- Open-access and institutional-access publisher pages for full text.
- Google Scholar or the user's available scholarly search systems for discovery and citation chaining.
- Crossref/OpenAlex for DOI and bibliographic metadata.
- Consensus/SciSpace within available free usage limits.
- Reference lists of high-quality recent reviews and “cited by” trails to discover original studies.
- Official journal-ranking records (e.g., Clarivate JCR or SCImago/SJR) for quartile verification, with exact year/category/provider recorded.

No single search engine is assumed to cover the full field. Don't present the search as systematic/comprehensive until the queries, dates, screening decisions and source coverage are recorded.

## Search-query framework

Run targeted searches for each stage/material class and each key cross-cutting condition. Start with combinations such as:

### Stage 1 — raw/unrefined biomass
- antibiotic adsorption wastewater raw agricultural waste adsorbent
- tetracycline/ciprofloxacin/sulfamethoxazole adsorption raw biomass husk bark sawdust
- antibiotic adsorption forestry waste agro-food residues low concentration

### Stage 2 — natural clays and unmodified biopolymers
- antibiotic adsorption bentonite montmorillonite kaolinite sepiolite cation exchange
- tetracycline adsorption natural clay pH desorption real water
- amoxicillin/ciprofloxacin/tetracycline adsorption unmodified chitosan cellulose alginate
- antibiotics adsorption biopolymer beads unmodified control versus crosslinked/modified

### Stage 3 — biochar
- antibiotics adsorption pristine biochar pyrolysis feedstock without activation
- antibiotic adsorption biochar pyrolysis temperature surface chemistry pH
- antibiotics adsorption KOH activated biochar acid modified biochar
- antibiotic adsorption phosphoric acid activated biomass biochar regeneration real water

### Stage 4 — precision-engineered/nano-carbon
- antibiotics adsorption Fe/N doped biochar without oxidant adsorption-only
- tetracycline/ciprofloxacin adsorption atomically engineered biochar heteroatom doped
- antibiotic adsorption granular activated carbon hospital wastewater fixed bed breakthrough
- ciprofloxacin adsorption carbon nanotubes graphene oxide reduced graphene oxide real water

### Cross-cutting mechanisms and process performance
- antibiotic adsorption mechanism spectroscopic evidence controls biochar/clay/biopolymer/carbon
- antibiotic adsorption regeneration desorption multiple cycles capacity loss
- antibiotics activated carbon fixed-bed column breakthrough wastewater
- antibiotic adsorption synthesis energy life cycle assessment techno-economic analysis
- adsorbent antibiotic cost per mass removed chemical consumption yield secondary waste

Use synonyms and individual antibiotic names; don't rely only on “antibiotic adsorption” because older studies may use target names and “sorption”.

## Screening rules

For every candidate:
1. Deduplicate by DOI and normalized title.
2. Confirm title, authors, year, journal and article type against publisher/DOI metadata.
3. Read the abstract and determine preliminary relevance. If abstracts are missing, locate them from a legitimate source.
4. Assign a preliminary material category and processing stage; the user does not need to classify papers manually.
5. Distinguish original research from reviews and preprints.
6. Separate adsorption-only studies from catalytic degradation, AOP/peroxymonosulfate activation, photocatalysis and membrane rejection.
7. Verify full text before extracting quantitative evidence.
8. Verify the journal's quartile independently and record provider, ranking year, subject category, quartile and source URL. Do not infer Q1 from impact factor.
9. Record exclusion reasons rather than silently dropping papers.

Reviews are useful for mapping and citation chasing; numerical capacity/mechanism evidence should come from the original study. A study can be useful as background even if it does not satisfy a Q1-only shortlist preference, but its status must be labelled honestly.

## Practical execution order

**Pass A — inventory:** audit the uploaded review-corpus.bib and make the canonical register.

**Pass B — review-led search:** identify the best recent reviews covering all stages and use their references to discover primary studies that are missing from the user's downloads.

**Pass C — gap searches:** prioritize unmodified biopolymers, pristine biochar, adsorption-only atomically doped biochar, activated-carbon continuous flow, cost/energy/LCA, and real-water studies.

**Pass D — verify Q1:** check quartiles only after the candidate metadata are clean; retain exact sources and flag uncertain cases.

**Pass E — full-text batch reading:** read a small coherent batch, extract evidence with PDF page/table/figure references, validate values, update caveats and GitHub, then draft the corresponding manuscript passage.

## Reporting transparency

At the end of each search pass, record:
- date and database/platform;
- exact queries and filters;
- number of records returned and screened where available;
- duplicates removed;
- included/excluded/pending counts and reasons;
- categories still thin or lacking credible studies;
- any access limitations.

Do not invent “comprehensive coverage”, a PRISMA count, Q1 status, qmax, cost values or mechanistic certainty.
