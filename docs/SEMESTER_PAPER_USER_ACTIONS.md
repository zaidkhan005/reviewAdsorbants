# User action tracker — semester paper

**Status as of 29 October 2026: NO ACTION REQUIRED FROM THE USER RIGHT NOW.**

The user has explicitly said they are not downloading any more papers for the time being. The work must proceed from existing Library PDFs, the repository's 505 source-linked broad-corpus evidence rows and legitimate accessible source text. Do not ask for new downloads or uploads unless the user later reopens that option.

## Current semester-paper state

- Approved title: **Assessing the Low-Cost Potential of Non-Conventional Engineered Adsorbents for Ciprofloxacin and Tetracycline Removal from Aqueous Media**.
- Approved materials: selected graphene-based adsorbents (GO/rGO and functionalized forms) plus selected graphene-bearing composites; not every graphene composite automatically qualifies.
- Target antibiotics: ciprofloxacin (CIP) and tetracycline (TC), keeping related antibiotics distinct.
- Candidate register: **44 rows, 43 unique DOI-defined works**; SEM-041 is a duplicate alias of SEM-026.
- Dedicated semester evidence CSV: **27 evidence records**.
- Main-corpus crosswalk: `data/semester-main-corpus-crosswalk.csv`, linking semester candidates to broad-corpus candidates, already extracted evidence IDs and Better BibTeX inventory matches.
- Reused broad evidence: SEM-016 ↔ CORP-024; SEM-032 ↔ CORP-015; SEM-038 ↔ CORP-031. Evidence is cross-referenced instead of duplicated.
- Added existing-source candidates: SEM-020 (CIP on graphene; abstract-level), SEM-039 (TC on CNF/GO aerogel; publisher full text), and SEM-040 (TC on graphene in a mixed low-concentration system; publisher full text). Evidence IDs EV-SEM-014–EV-SEM-016 preserve source-status and metric caveats.
- Additional full-text evidence: EV-SEM-025/SEM-027 (GO/Ca-alginate–PAM beads, fitted qₘ=6.846 mg/g, no direct qe/reuse extracted, 50 mL vs 55 mL method flag); EV-SEM-026/SEM-029 (GO/PVA/alginate CIP beads, 7.15 mg/g observed qe max, conflicting model outputs and 100× experimental-vs-cost dose basis); EV-SEM-027/SEM-034 (GO/Co–Fe TC, 94.1% vs 93.94% removal discrepancy, fitted qₘ=64.10 mg/g at 50°C, no quantitative cost).
- Reference target: approximately 50 distinct works actually cited, subject to screening and the strength of evidence; this count is not yet established.
- The broad review remains separate and retains its original processing–cost–performance continuum and material classes.

## Work that will continue without new files

1. Review existing accessible Library PDFs and the existing corpus records for any in-scope graphene/CIP/TC studies not yet incorporated.
2. Use indexed or abstract-only text when that is all that is available, label its limits, and do not present unavailable table values as fully verified.
3. Keep fitted qmax, measured qe, model-fitted qe, removal %, and column metrics separate; preserve mass-balance and source inconsistencies.
4. Deduplicate candidates and link reused master evidence through the crosswalk rather than creating duplicate evidence rows.
5. Build the source-backed comparisons and original table/figure plan, and continue the citation/provenance audit.

- Current GO–alginate study is canonicalized as SEM-026 with evidence EV-SEM-020; SEM-041 is a retained duplicate alias and must not be counted twice. SEM-042 (chitin/nGO continuous-flow CIP), SEM-043 (GO for CIP/SMX, SMX separate), and SEM-044 (MgO/chitosan/GO for CIP/NOR, NOR separate) remain distinct records with EV-SEM-021–EV-SEM-023.
  
- SEM-024 (Gao et al., 2012, GO for TC) now has EV-SEM-024 from the primary PubMed abstract. The 313 mg/g qmax and kinetic constant are abstract-level; full conditions and cost/regeneration are unavailable.
- SEM-001's full PLOS text is re-audited; the temperature-specific Langmuir values (322.43, 101.87 and 73.53 mg/g at 298, 303 and 308 K, respectively) are recorded with a consistency caveat, not used as an unqualified temperature trend.

## Known limitations, not user requests

- SEM-020 has publisher-abstract-only evidence for the 323 mg/g fitted Langmuir value; full-text conditions/table/figure validation remains pending. Keep it out of final quantitative ranking.
- SEM-039 now has a method-level publisher-text audit: preparation, general batch conditions, ten-cycle NaOH regeneration and the q_e/q_m/removal distinctions are documented. The exact Fig. 7 feed concentration is not specified in the caption, PDF pagination is not verified, and no cost inventory is reported.
- SEM-040 has publisher HTML reviewed; the exact TC removal percentage is figure-based and was not guessed. The experiment is a mixed-antibiotic test, not a single-solute TC isotherm.

- SEM-006, the DTPA-functionalized magnetic GO study for CIP and TC, has indexed primary methods/text but not a complete verifiable numeric table/figure audit in this session.
- SEM-037, the GO–alginate hydrogel-bead permeable reactive barrier study for CIP groundwater, has accessible abstract/indexed details, but the actual cost/lifetime values and complete column conditions remain unavailable.
- Those limitations remain recorded. The workflow proceeds with other evidence; neither item is a current request for the user.


## Recent integrity work (29 October 2026)

- Duplicate DOI 10.1016/j.jcis.2016.08.068 has been resolved in project data: SEM-026 is canonical, EV-SEM-020 is linked to SEM-026, and SEM-041 is an alias for traceability only.
- EV-SEM-010 and EV-SEM-013 had fields misassigned against the CSV headers. The rows have been corrected; do not reuse their prior shifted fields from any old export.
- No user action is required. The user has paused new downloads/uploads.


## SEM-042 source-validation update (29 October 2026)

SEM-042’s accepted-manuscript methods, isotherm text and dynamic tables have been reviewed from an accessible CONICET-hosted PDF. The repository evidence row records the details. A 100-g column charge conflicts with the stated 1.0-cm-ID × 1.5-cm bed volume (1.178 cm³; implied density ~84.9 g/cm³). That source value was not silently corrected; dynamic columns and all Thomas q₀/Yoon–Nelson τ figures are quarantined from final ranking pending a reliable correction. No new file/download is needed from the user.


## New full-text additions — EV-SEM-025–027 (29 October 2026)

The new evidence rows are committed and linked to candidate IDs. The candidate register remains 44 rows / 43 DOI-defined works; the evidence CSV now has 27 unique records. A separate crosswalk refresh was committed for SEM-027, SEM-029, SEM-034 and SEM-042. None of the new source gaps require user files. Continue with primary-source validation and condition-matched synthesis; do not ask the user for downloads.
