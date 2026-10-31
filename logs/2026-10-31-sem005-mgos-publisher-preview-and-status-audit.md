# SEM-005 MGOS publisher-preview and article-status audit — 31 October 2026

## Study identity
Yu, B., Bai, Y., Ming, Z., Yang, H., Chen, L., Hu, X., Feng, S. and Yang, S.-T. (2017), “Adsorption behaviors of tetracycline on magnetic graphene oxide sponge,” *Materials Chemistry and Physics* 198, 283–290. DOI: 10.1016/j.matchemphys.2017.05.042.

Primary publisher page: https://www.sciencedirect.com/science/article/pii/S025405841730411X
Crossref DOI record: https://api.crossref.org/works/10.1016/j.matchemphys.2017.05.042
ORCID author publication listing: https://orcid.org/0000-0001-6795-8879

The official ScienceDirect preview and the Crossref DOI metadata were live-fetched/inspected on 31 October 2026. The page exposes the article title, abstract, highlights, introduction and selected section snippets (Preparation of MGOS; Characterization of MGOS; Conclusion), but directs readers to institutional access or purchase for the full article. Exact Methods, isotherm/kinetic tables and numerical operating conditions remain unavailable in the accessible primary preview. The existing Library search did not locate this paper's full PDF. No additional user PDF batch is assumed.

## Article-status check — third-party anomaly not confirmed
A third-party academic-library search result for a query containing “magnetic graphene oxide” showed the Turkish label “Geri Çekilmiş” (withdrawn/retracted) adjacent to a result that appeared to correspond to this paper. However, the underlying record was access-gated; its publication identifier, status rationale and any linked notice could not be inspected.

Counter-checks on 31 October 2026:
1. The official ScienceDirect page continues to present a normal article page with the published title, abstract, issue data, authors, and section snippets, as well as ordinary institutional-access and purchase options. It is not replaced by a retraction/withdrawal notice.
2. A live Crossref DOI API response for 10.1016/j.matchemphys.2017.05.042 reports status “ok” and an empty `relation` object; no `update-to`/retraction relationship was present in the retrieved record.
3. The ORCID page for author Sheng-Tao Yang lists this as a 2017 journal article with its DOI and Scopus EID.
4. Targeted web searches for an official publisher retraction, withdrawal, erratum or correction notice did not locate one.

The lack of a Crossref update relationship or an official notice located in this search is not absolute proof that no update exists, because update metadata coverage depends on publisher deposits. Nevertheless, the accessible evidence does **not** substantiate a formal retraction. Record the third-party label as an unresolved status anomaly, not as a confirmed retraction or exclusion decision. Crossref documents how corrections/retractions can be linked to original DOI metadata; see https://www.crossref.org/documentation/register-maintain-records/maintaining-your-metadata/registering-updates/ and https://www.crossref.org/crossmark/.

## What the publisher primary preview supports
The abstract/highlights say:
- Material: magnetic graphene oxide sponge (MGOS), prepared by lyophilizing a dispersion of Fe3O4 nanoparticles and graphene oxide (GO).
- The reported tetracycline adsorption capacity is 473 mg/g, described as around 50% higher than GO.
- Adsorption is “moderately fast” and is described by a pseudo-second-order kinetic model.
- Thermodynamic interpretation: endothermic adsorption and entropy increase as driving force.
- pH has a mild influence; ionic strength has nearly no impact.
- The introduction says isotherms were examined with Langmuir, Freundlich and Temkin models, and kinetics with pseudo-first-order, pseudo-second-order and intraparticle-diffusion models.

The preview does **not** expose whether 473 mg/g is a directly observed equilibrium qe, a fitted Langmuir qmax or another model-defined capacity. Do not assign it to one of those metric categories without Table/Methods verification.

## Material preparation and structure snippets
- Citrate-coated Fe3O4 nanoparticles were prepared by co-precipitation of Fe2+ and Fe3+ with OH− in the presence of sodium citrate, following a cited prior method with modifications.
- GO was prepared by a modified Hummers method following earlier reports; this paper's accessible snippet does not reproduce the full GO recipe.
- To prepare MGOS, Fe3O4 and GO were mixed at a 1:40 mass ratio and lyophilized.
- The authors report very low bulk density, 4.6 mg/cm3, due to the porous sponge architecture.
- Characterization methods listed include TEM, SEM, XPS, XRD, IR spectroscopy and magnetometry.
- The abstract says Fe3O4 nanoparticles attach to GO sheets and enable magnetic response; the authors attribute enhanced adsorption to small Fe3O4 particle size/negative charge, GO oxidation degree and lyophilization.

This is enough to retain the material-architecture and magnetic-separability context. It is not enough to reproduce the detailed synthesis, estimate composite yield, identify precise citrate:iron stoichiometry or calculate processing cost.

## Unavailable quantitative evidence
The following remain hidden behind full-text access and are not recoverable from the current primary preview:
- initial TC concentration (C0) and concentration range;
- solution volume and adsorbent mass/dose;
- exact pH, temperature and contact-time condition associated with 473 mg/g;
- observed equilibrium concentration and directly measured qe;
- Langmuir/Freundlich/Temkin parameters and model-fit statistics;
- pseudo-first-order/pseudo-second-order/intraparticle-diffusion fitted parameters;
- detailed pH and ionic-strength test ranges and numerical outcomes;
- magnetic separation efficiency and any Fe leaching;
- desorption/regeneration procedure and cycle-resolved reuse results;
- GO/MGOS yield, energy, solvent/water consumption, reagent recovery, monetary cost, real-water trials or full LCA/TEA.

Do not fill these gaps using secondary sources or by deriving a condition vector from adjacent studies. Do not call the 473 mg/g figure “Langmuir qmax” or “observed qe”.

## Semester-paper decision
Retain SEM-005 / EV-SEM-019 for qualitative discussion of MGOS architecture, citrate-coated Fe3O4 loading at Fe3O4:GO=1:40, lyophilization, low bulk density and magnetic separation. Keep 473 mg/g as an **abstract-reported but metric-unresolved adsorption capacity**, explicitly excluded from condition-matched numeric rankings pending the complete primary Methods/table.

No claim of regeneration, actual wastewater performance, leaching safety or low-cost production is supported by the accessible preview. The possible third-party withdrawn label should remain an unverified flag; do not mark the paper as retracted or excluded without a verifiable publisher notice.

## Citation workflow
The latest inspected Zotero/citation exports had no matched Better BibTeX key. Do not invent a key or insert a citation into the manuscript until the actual Zotero key is verified.

## Repository updates
Updated in place:
- data/semester-remaining-work-register.csv
- data/semester-paper-candidate-register.csv
- data/semester-evidence-readiness-audit.csv (EV-SEM-019)
- README.md

No row was added to the condition-labelled comparison because the article preview lacks a numeric TC endpoint with matched operating conditions. No duplicate SEM evidence ID was created.
