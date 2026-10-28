# Semester-paper targeted screening starter

**Date opened:** 2026-10-28  
**Purpose:** Implement the user-approved scope recorded in `SEMESTER_PAPER_SCOPE_PROPOSAL.md`. This is a discovery/screening aid, not a list of accepted papers.

## 1. First-pass screen of the existing project pool

The planned-download pool contains 250 candidates, but it was built for the broader antibiotic-adsorption review and is not pre-filtered for the semester-paper scope. The following examples illustrate the scope filter.

| Candidate | Metadata-level description | First-pass disposition | Reason / next action |
|---|---|---|---|
| POOL-024 | Sulfonated graphene oxide for ciprofloxacin (2025) | **High-priority candidate** | Family A + target CIP. Verify primary record, full text, conditions, adsorption endpoint, regeneration details and journal metadata. |
| POOL-174 | Ciprofloxacin adsorption on graphene and granular activated carbon | **Potential candidate** | Include graphene results if separately reported; treat granular activated carbon only as a labelled benchmark. Verify whether the source is primary and obtain full metadata. |
| POOL-241 | Thiourea-dioxide-reduced magnetic graphene oxide for tetracycline removal | **Potential candidate** | Family B + target TC. Verify exact material synthesis, target-specific results and whether removal is adsorption-only. |
| POOL-168 | Amino-functionalized mesoporous silica–magnetic graphene oxide composite for oxytetracycline | **Outside core target as listed** | Oxytetracycline is not tetracycline for the core comparison. Retain only as contextual/near-miss evidence unless target scope is explicitly changed later. |
| POOL-022 | Green multi-walled carbon nanotubes for ciprofloxacin/ofloxacin | **Exclude from core** | Standalone CNT material is outside the selected two families. |
| POOL-063 | Alginate/carboxymethyl chitosan hydrogel microbeads for CIP and TC | **Exclude from core** | No graphene component in the listed material. |
| POOL-121 | Amine-functionalized magnetic bamboo-based activated carbon for CIP/norfloxacin | **Exclude from core** | Activated carbon without a graphene component is outside the core material scope. |

All dispositions above are provisional metadata screening only. Do not treat them as final inclusion decisions, full-text audits, or verified quartile claims.

## 2. External discovery anchors found in the initial focused web search

These papers demonstrate that the selected combination has an existing primary-study literature. They are **screening anchors, not automatic inclusions**; retrieve and examine the full text, primary figures/tables and eligibility before extracting performance values.

| Anchor study | Why it is useful for screening | Link |
|---|---|---|
| Li et al. (2018), *Performance of magnetic graphene oxide/diethylenetriaminepentaacetic acid nanocomposite for the tetracycline and ciprofloxacin adsorption in single and binary systems* | One magnetic, functionalized graphene-oxide composite directly tests both target antibiotics, including single and binary systems. | [PubMed record](https://pubmed.ncbi.nlm.nih.gov/29567603/) · DOI: 10.1016/j.jcis.2018.03.003 |
| Bruckmann et al. (2024), *Adsorption of ciprofloxacin from aqueous solution and fresh synthetic urine by graphene oxide* | Family A study with CIP in aqueous solution and a more complex synthetic-urine matrix. | [Publisher record](https://www.sciencedirect.com/science/article/pii/S1385894724019715) · DOI: 10.1016/j.cej.2024.150484 |
| Tri et al. (2024), *The adsorption of tetracycline, ciprofloxacin on reduced graphene oxide surfaces: Role of intermolecular interaction* | Directly considers both targets on rGO; inspect how theory and experiments are combined and what is experimentally measured. | [Publisher record](https://www.sciencedirect.com/science/article/pii/S0301010424000363) · DOI: 10.1016/j.chemphys.2024.112207 |
| *A comprehensive adsorption study and modeling of antibiotics as a pharmaceutical waste by graphene oxide nanosheets* (2018 issue; online 2017) | Tests GO nanosheets with TC and CIP as well as another antibiotic; target-specific data may support the core tables if separable. | [PubMed record](https://pubmed.ncbi.nlm.nih.gov/28841526/) · DOI: 10.1016/j.ecoenv.2017.08.019 |
| *Adsorption of tetracycline with reduced graphene oxide decorated with MnFe₂O₄ nanoparticles* (2018) | Magnetic rGO composite with explicit separation/recovery motivation. | [Open full-text record](https://pmc.ncbi.nlm.nih.gov/articles/PMC6281545/) · DOI: 10.1186/s11671-018-2814-9 |
| *Adsorption behaviors of tetracycline on magnetic graphene oxide sponge* (2017) | Structured magnetic GO material for TC; useful for comparing recovery/structure with sheet-like material. | [Publisher record](https://www.sciencedirect.com/science/article/pii/S025405841730411X) · DOI: 10.1016/j.matchemphys.2017.05.042 |
| *A DFT theoretical and experimental study about tetracycline adsorption onto magnetic graphene oxide* (2022) | Directly studies TC on magnetic GO; useful for modification ratio and reuse questions. | [Publisher record](https://www.sciencedirect.com/science/article/abs/pii/S0167732222003749) · DOI: 10.1016/j.molliq.2022.118837 |
| Dang et al. (2025), *Integration of magnetic graphene oxide and office waste paper-derived fibrillated cellulose into a composite adsorbent for effective tetracycline elimination* | Selected graphene–cellulose composite with preparation, adsorption, and five-cycle reuse data; waste-derived cellulose is incidental to material eligibility, not the paper's theme. | [Open publisher record](https://pubs.rsc.org/en/content/articlehtml/2025/ra/d5ra00877h) · DOI: 10.1039/D5RA00877H |
| *EDTA-functionalized magnetic graphene oxide for rapid and efficient removal of tetracycline from aqueous media* (2026) | Current discovery lead for functionalized magnetic GO and TC; full-text details, cost evidence and journal metadata need verification. | [Publisher record](https://www.sciencedirect.com/science/article/pii/S1944398626002638) · DOI: 10.1016/j.dwt.2026.101889 |
| *Adsorptive removal of ciprofloxacin from aqueous medium by magnetic guar gum grafted graphene oxide nano composite* (2023) | Potential graphene–polymer composite for CIP; examine polymer/GO mass ratio, preparation steps and whether any cost claim is quantified. | [Publisher record](https://www.sciencedirect.com/science/article/abs/pii/S2213343723015051) · DOI: 10.1016/j.jece.2023.110766 |
| *Removal of ciprofloxacin and cephalexin antibiotics in water environment by magnetic graphene oxide nanocomposites; optimization using response surface methodology* (2023) | Potential magnetic GO composite; include CIP only if the target-specific adsorption result is separable and no degradation process confounds it. | [Open-access publisher record](https://doi.org/10.1016/J.RINENG.2023.101507) · DOI: 10.1016/j.rineng.2023.101507 |

## 3. Search strings for the next reproducible pass

Run across suitable scholarly indexes, then deduplicate by DOI and normalized title.

### Family A
- `("graphene oxide" OR "reduced graphene oxide" OR graphene OR "functionalized graphene oxide") AND (ciprofloxacin OR tetracycline) AND adsorption`
- `("sulfonated graphene oxide" OR "functionalized graphene") AND (ciprofloxacin OR tetracycline) AND adsorption`
- `("graphene oxide" OR "reduced graphene oxide") AND ("aqueous solution" OR wastewater OR "real water") AND adsorption AND (ciprofloxacin OR tetracycline)`

### Family B
- `("magnetic graphene oxide" OR "magnetic reduced graphene oxide" OR "Fe3O4/GO" OR "Fe3O4/rGO") AND (ciprofloxacin OR tetracycline) AND adsorption`
- `("graphene oxide composite" OR "graphene-based composite" OR "graphene polymer composite" OR "graphene cellulose composite") AND (ciprofloxacin OR tetracycline) AND adsorption`
- `("magnetic graphene" OR "graphene oxide sponge" OR "immobilized graphene oxide") AND (ciprofloxacin OR tetracycline) AND (regeneration OR reuse OR recovery OR "real water")`

Search records should retain query, database/index, date searched, DOI, publication year, full-text availability, target drug, material family, study type, adsorption-only status, eligibility decision and reason. Do not report a database search as exhaustive until the platforms and exact search dates/strings are logged.

## 4. Extraction fields for each potentially eligible paper

- Citation, DOI, journal, year, verified journal category/quartile source and date checked.
- Family A/B, exact material name, synthesis and functionalization route, component ratios, reagents, temperature/time, wash/neutralization, drying or freeze-drying, yield if reported.
- Target drug, single or mixture, initial concentration, pH, adsorbent dose, contact time, temperature, ionic strength, coexisting ions/DOM, matrix type.
- Observed uptake/removal and exact source location; qmax model and fit separately; uncertainty and fitting quality.
- Evidence for mechanism (spectroscopy, control experiments, pH/speciation, surface charge, computational work); label inferred mechanisms as inferred.
- Recovery method, regeneration chemistry, number of cycles, capacity retained, leaching/stability, and real-water/column results.
- Cost/energy inputs and system boundary; explicitly mark absent data.
- Study limitations, possible overlap with another record, and final eligibility reason.

## 5. Eligibility decision vocabulary

Use one of: **Include**, **Exclude**, **Await full text**, **Needs clarification**, **Context only**. Every Exclude decision must carry a reason. A candidate that is on-theme but lacks separable adsorption evidence is not automatically included.

The next deliverable should be a deduplicated candidate register and a first-pass eligibility table—not a polished narrative or an unsupported performance ranking.
