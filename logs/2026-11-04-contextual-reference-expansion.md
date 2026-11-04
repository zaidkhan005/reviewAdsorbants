# Contextual reference expansion — 4 November 2026

## Purpose

The current manuscript bibliography contained 53 works. The earlier supervisor guidance for the semester paper was a target of approximately 60 references. Seven additional sources were therefore selected to close that gap with relevant contextual and methodological literature, not to pad the list or expand the frozen empirical selection.

## Current reference architecture

- 49 selected works remain frozen: 46 empirical primary studies plus three theoretical, review or scope-context roles.
- 11 additional contextual references are now listed separately.
- Total bibliography: 60 unique records.
- The condition-labelled comparison remains 15 primary studies; the 49-study selected-reference coverage in Table 3 is unchanged.
- None of the seven added works is promoted into the selected empirical set or used to supply CIP/TC adsorption-capacity data.

## Seven additions and their bounded use

| New reference | Why included | Intended role in the manuscript |
|---|---|---|
| Mnguni and Nomngongo (2026), DOI [10.1007/s11356-026-37527-z](https://doi.org/10.1007/s11356-026-37527-z) | Reviews cost-estimation methods for magnetic nanoadsorbents and shows heterogeneity in the denominator and included cost items. | Section 1.4: cost-method heterogeneity; not a GO/antibiotic performance study. |
| Pryce et al. (2022), DOI [10.3390/w14121919](https://doi.org/10.3390/w14121919) | Compares life-cycle costs of graphene-based adsorbent configurations for emerging-contaminant removal. | Sections 1.4 and 5.4: adjacent system-level graphene cost benchmark; not CIP/TC-specific. |
| Gkika et al. (2025), DOI [10.1021/acsomega.5c04090](https://doi.org/10.1021/acsomega.5c04090) | Reports activity-based cost comparison for rGO synthesis routes and the influence of process simplification. | Section 5.1: material-manufacture cost example; not water-treatment cost per volume or antibiotic removed. |
| Tzatzadakis et al. (2026), DOI [10.1021/acsomega.5c09672](https://doi.org/10.1021/acsomega.5c09672) | Quantifies laboratory-scale energy and environmental indicators for GO and chemically reduced rGO production. | Section 5.1: production-burden context; environmental indicators are not monetary costs. |
| Ge et al. (2021), DOI [10.15244/pjoes/144372](https://doi.org/10.15244/pjoes/144372) | Compares life-cycle impacts of hydrothermal and annealing production routes for N-rGO. | Section 5.1: route-dependent N-rGO production context; not an adsorption-performance source. |
| Viegas et al. (2020), DOI [10.3390/w12010033](https://doi.org/10.3390/w12010033) | Reports pilot-scale pharmaceutical-water treatment and a system-level PAC/ceramic-microfiltration cost estimate. | Section 5.4: conventional process comparator; not a graphene, CIP or TC cost estimate. |
| Wurzer et al. (2023), DOI [10.1016/j.envpol.2022.120532](https://doi.org/10.1016/j.envpol.2022.120532) | Examines end-of-life hydrothermal treatment of spent carbon adsorbents loaded with pharmaceuticals. | Section 5.2: spent-media management context; the biochar findings are explicitly not transferred to GO/rGO. |

## Manuscript edits made

- Abstract: revised the additional-context reference count from four to eleven.
- Section 1.4: added the cost-method distribution reported by Mnguni and Nomngongo and introduced Pryce et al. as a system-level graphene cost comparison.
- Section 2.3 and Figure 2: updated the number and scope of additional contextual references; the diagram now identifies eleven additional context references separately.
- Section 5.1: added the bounded rGO synthesis-cost example and GO/rGO/N-rGO production-burden context.
- Section 5.2: added an explicitly qualified spent-biochar end-of-life example.
- Section 5.4: added adjacent graphene and PAC/ceramic-microfiltration system-level cost benchmarks, with an explicit warning that their process boundaries and assumptions are not directly comparable to the manuscript's laboratory estimates.

## Integrity checks before rebuild

- New records were checked against the existing bibliography: no repeated DOI among the 60 entries.
- Each of the seven new citation keys is used in the manuscript.
- The current manuscript has 60 unique cited keys; the BibTeX file has 60 unique records and 60 unique DOI values.
- Pre-build linkage check: zero missing and zero unused keys.
- The original 49 selected-study records, evidence values, condition-labelled comparison and critical scientific holds were not changed.

## Build input

The current bibliography input is now:
`semester-manuscript-cited-references-49-selected-plus-11-context.bib`.

The build script and GitHub Actions workflow were updated to use this filename. A new production build and output QA are required before the 60-reference manuscript can replace the prior verified artifact as the current deliverable.
