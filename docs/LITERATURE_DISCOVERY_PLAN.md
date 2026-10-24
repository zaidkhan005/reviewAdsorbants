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


## First discovery pass — 2026-10-24

The initial targeted search was run to test the metadata-only gap map. It found these candidate leads that were not in the 31-record download export. They have been added to the unified corpus screening register as DISC-001 through DISC-007. None is automatically accepted and none has verified quartile status yet.

1. **Pristine biochar:** Na, P. T. L. et al., “Sorption of four antibiotics onto pristine biochar derived from macadamia nutshell,” Bioresource Technology (2024), DOI [10.1016/j.biortech.2023.130281](https://doi.org/10.1016/j.biortech.2023.130281). This directly addresses the need for unmodified/pristine biochar evidence and covers ciprofloxacin, ofloxacin, sulfamethoxazole and trimethoprim. Source: [PubMed record](https://pubmed.ncbi.nlm.nih.gov/38181996/).
2. **Natural clays and regeneration:** Zhou et al., “Effective microwave regeneration of natural sepiolite and montmorillonite as adsorbents for tetracycline removal and mechanism insight,” Separation and Purification Technology (2024), DOI [10.1016/j.seppur.2024.127767](https://doi.org/10.1016/j.seppur.2024.127767). Candidate for the clay/regeneration comparison. The publisher page's abstract and conclusion snippets appear to reverse the order of the two clay capacity values, so the original tables must be checked before any value is copied. Source: [publisher record](https://www.sciencedirect.com/science/article/pii/S1383586624015065).
3. **Clay and flow operation:** Sumariva et al., “Use of clay honeycomb monoliths for the removal of tetracycline antibiotic from water,” Journal of Water Process Engineering (2024), DOI [10.1016/j.jwpe.2024.106381](https://doi.org/10.1016/j.jwpe.2024.106381). A structured clay monolith and flow-rate study; the paper also discusses subsequent filter cleaning/contaminant breakdown, which must be kept separate from the adsorption results. An open-access copy is listed by the [University of Cádiz repository](https://rodin.uca.es/handle/10498/33839).
4. **Modified biochar in a complex matrix:** Masrura et al., “Selective adsorption of antibiotics from human urine using biochar modified by dimethyl sulfoxide, deep eutectic solvent, and ionic liquid,” Environmental Pollution (2024), DOI [10.1016/j.envpol.2024.124588](https://doi.org/10.1016/j.envpol.2024.124588). Useful for functionalization and selectivity, but human urine is an adjacent matrix rather than a direct substitute for municipal/hospital effluent. Source: [PubMed record](https://pubmed.ncbi.nlm.nih.gov/39033844/).
5. **Biopolymer–biochar beads:** Mosaffa et al., “Bacterial cellulose microfilament biochar-architectured chitosan/polyethyleneimine beads for enhanced tetracycline and metronidazole adsorption,” International Journal of Biological Macromolecules (2024), DOI [10.1016/j.ijbiomac.2024.132953](https://doi.org/10.1016/j.ijbiomac.2024.132953). Relevant across the biopolymer/biochar boundary; full-text tables must resolve differences between rounded capacity summaries on indexed pages. Source: [PubMed record](https://pubmed.ncbi.nlm.nih.gov/38944566/).
6. **Functional biopolymer composite beads:** Gopal and Mukherjee, “Adsorptive removal of norfloxacin from aqueous solutions by Fe/Cu CNS-embedded alginate-carboxymethyl cellulose-chitosan beads,” RSC Advances (2024), DOI [10.1039/d4ra01971g](https://doi.org/10.1039/d4ra01971g). Relevant to matrix/functionalized biopolymer adsorption; source abstract reports 86% removal under its stated batch conditions and a Langmuir capacity, both to be verified from full text before synthesis. Source: [PubMed record](https://pubmed.ncbi.nlm.nih.gov/38756850/).
7. **Clay–biopolymer comparison and dynamic test:** Liu et al., “Sustainable wastewater decontamination from chlortetracycline using kaolin-alginate beads: adsorption mechanisms and practical applications,” Royal Society Open Science (2025), DOI [10.1098/rsos.250439](https://doi.org/10.1098/rsos.250439). Candidate compares the clay, composite and activated-carbon controls and includes dynamic experiments. Verify test conditions, water matrix, and journal quartile before deciding how it is used. Source: [PubMed record](https://pubmed.ncbi.nlm.nih.gov/41063724/).

### Metadata corrections from the downloaded export

- The Pinheiro et al. chitosan/alginate amoxicillin record was exported as a Research Square preprint with no journal. A published version appears in Environmental Science and Pollution Research (2024), DOI [10.1007/s11356-024-35293-4](https://doi.org/10.1007/s11356-024-35293-4). The screening register uses the journal version while retaining a note about the alternate preprint record. Source: [PubMed record](https://pubmed.ncbi.nlm.nih.gov/39466532/).
- The Mohammed-Ridha and Abdul-Ahad levofloxacin study is listed in the Zotero export as 2023, but the official Journal of Engineering page says it was published on 1 December 2014 in Volume 20, Issue 12. The screening register now uses 2014. Source: [official journal record](https://www.joe.uobaghdad.edu.iq/index.php/main/article/view/2591).

### Next discovery priorities

Continue the discovery pass against gaps in the outline—especially unmodified biopolymers, additional pristine biochar, adsorption-only atomically doped biochars, commercial activated carbon in fixed-bed/real-water settings, and direct cost/energy/life-cycle evidence. Verify journal quartiles separately; no source above is designated Q1 here solely from journal reputation.


## Second discovery pass — 2026-10-24

A second targeted search focused on the two thinnest technical areas from the first pass: adsorption-only engineered/doped biochars and direct cost/lifecycle evidence. Six further leads were added as DISC-008 through DISC-013; none has an accepted or Q1-verified status yet.

8. **Fe/N co-doped biochar adsorption:** “Simultaneous adsorption of ciprofloxacin and Cu2+ using Fe and N co-doped biochar: Competition and selective separation,” Waste Management (2023), DOI [10.1016/j.wasman.2023.06.014](https://doi.org/10.1016/j.wasman.2023.06.014). Particularly useful because the abstract describes co-adsorption rather than an oxidant-driven degradation process. Source: [PubMed](https://pubmed.ncbi.nlm.nih.gov/37348381/).
9. **Nitrogen-doped porous biochar from fermentation residue:** “Effective removal of tetracycline antibiotics from water by in-situ nitrogen-doped porous biochar derived from waste antibiotic fermentation residues,” Journal of Environmental Chemical Engineering (2024), DOI [10.1016/j.jece.2024.114433](https://doi.org/10.1016/j.jece.2024.114433). Verify that data used in the manuscript reflect adsorption, not other unreported treatment pathways. Source: [publisher result](https://www.sciencedirect.com/science/article/pii/S2213343724025648/pdf).
10. **Selective magnetic biochar:** “Selective removal of oxytetracycline by molecularly imprinted magnetic biochar,” Bioresource Technology (2024), DOI [10.1016/j.biortech.2024.130394](https://doi.org/10.1016/j.biortech.2024.130394). Relevant to selectivity/interference and magnetic recovery. Source: [publisher record](https://www.sciencedirect.com/science/article/pii/S096085242400097X).
11. **Activated carbon plus lifecycle/cost analysis:** “Waste plastic derived activated carbon for simultaneous removal of hazardous antibiotics: Multiscale modelling and life cycle analysis,” Separation and Purification Technology (2025), DOI [10.1016/j.seppur.2025.132487](https://doi.org/10.1016/j.seppur.2025.132487). This may be one of the strongest direct leads for the review's economic/environmental comparison. Verify system boundaries, assumptions, target identity and cost basis from the source. Source: [publisher record](https://www.sciencedirect.com/science/article/pii/S1383586625010846).
12. **Ball-milled, nitrogen-doped biochar:** “Optimization of Biochar Adsorption Performance through Ball Milling and Nitrogen Doping: Mechanisms and Performance in Tetracycline Removal,” ACS Omega (2026), DOI [10.1021/acsomega.5c07456](https://doi.org/10.1021/acsomega.5c07456). Publisher record states it appeared online in April 2026. Useful for contemporary engineered adsorption, but process energy and capacity claims still need full-text extraction. Source: [ACS Publications](https://pubs.acs.org/doi/10.1021/acsomega.5c07456).
13. **Biochar review for citation chasing:** “Removal of tetracycline from water by adsorption with biochar: A review,” Journal of Water Process Engineering (2024), DOI [10.1016/j.jwpe.2024.105215](https://doi.org/10.1016/j.jwpe.2024.105215). Use the review's bibliography to discover primary work on pristine/modified biochar, adsorption mechanisms and regeneration; cite original studies for quantitative findings. Source: [publisher record](https://www.sciencedirect.com/science/article/abs/pii/S2214714424004471).

The corpus register now has 31 downloaded records plus 13 externally discovered leads (44 total candidate records). This count is not a count of included studies, verified full texts, or Q1 papers. Continue searches and citation chasing until the scope and evidence coverage are defensible, and log the search dates/queries so completeness is not claimed prematurely.
