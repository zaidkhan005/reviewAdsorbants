# Semester paper — final 50-reference selection freeze

**Decision date:** 31 October 2026  
**Project:** Antibiotic Adsorption Review — semester paper only  
**Status:** Candidate selection frozen; manuscript citation integration remains in progress.

## Decision

The semester paper will use **all 50 distinct DOI-defined works** in the existing semester candidate shortlist. No further candidate discovery or literature-pool expansion is required for the semester submission. The original broad-review project remains separate.

The source shortlist has 51 rows because SEM-041 is a duplicate alias of SEM-026 (same work/DOI). SEM-041 is not a 51st distinct study and is excluded from the count. The 50 selected records are listed in `data/semester-final-50-reference-selection.csv`.

## How all 50 will be used

- **47 empirical primary-study references:** retained in the evidence synthesis, with their source-access tier and scientific caveats preserved. Not every one supplies a condition-complete numerical endpoint.
- **SEM-013 — theory/mechanism context:** may support a clearly labelled theoretical discussion only; it is not an experimental adsorption study.
- **SEM-022 — review/background context:** may support field mapping/background only; it is not counted as a primary experiment.
- **SEM-036 — scope-boundary near-miss:** may be cited only to explain why GO-like biomass-derived carbon nanosheets without verified GO/rGO identity are outside the core material scope. It must not be presented as a core graphene adsorbent.

This is a decision to cite all 50 works in appropriate roles, **not** a decision to treat all 50 as equally strong evidence or to place all 50 in a quantitative comparison table.

## Citation state

- 50 distinct candidate works selected.
- 15 of those 50 are already cited in the current manuscript with verified Better BibTeX keys.
- 35 selected candidate works remain to be cited and need exact-DOI lookup in Zotero, followed by Better BibTeX export. The new queue is `references/semester-final-35-doi-import-queue.txt`.
- The current manuscript also contains four contextual works outside the 50-candidate pool. Keeping those four would produce **54 distinct references total** (50 selected candidate works + 4 contextual references). They can remain because they support general adsorption, carbon-nanomaterial, CIP speciation and dissolved-organic-matter context. Do not misstate the 50 selected candidate count as the total bibliography count while those four remain.
- SEM-041 remains an alias only; do not cite/count it separately.

## Scientific safeguards retained

1. Keep observed uptake, removal percentage, fitted isotherm (q_{max}), kinetic-model outputs and column metrics separate.
2. Keep CIP separate from other fluoroquinolones and TC separate from CTC/OTC/doxycycline unless the source reports them as a defined mixture; use target-specific results only.
3. Abstract-only, preview-only, mirror-derived and indexed-text records must be labelled at their actual source-access level.
4. Quarantined mass-balance or unit-conflicted values remain excluded from rankings; do not silently repair them.
5. Cost claims remain author-reported or unverified unless the process boundary, inputs and functional unit can be reconstructed.
6. No journal-quartile filter applies to the semester paper.
7. The 15-study comparison table remains a selected quantitative synthesis, not a claim that all 50 works have matched operating conditions.

## Immediate remaining work

1. Resolve Zotero records/Better BibTeX keys for the 35 not-yet-cited selected works using the exact-DOI queue.
2. Add each citation to the appropriate manuscript paragraph/table only where the source supports the claim.
3. Expand contextual/mechanistic and composite/application discussion to cover the selected set without creating unsupported quantitative comparisons.
4. Reconcile the final bibliography (50 selected candidates + retained context references), manuscript citations, tables and figure callouts.
5. Complete the final scientific and formatting audit.

## Original batch provenance

The exact DOI cross-match against the original PDF batch crosswalk confirms three selected semester studies were supplied in user batches:
- SEM-016 / CORP-024 — Batch 14, Paper 3 (`graphene 1.pdf`).
- SEM-032 / CORP-015 — Batch 15, Paper 3 (`graphene 2.pdf`).
- SEM-038 / CORP-031 — Batch 10, Paper 2 (`ato eng 2.pdf`).

The crosswalk and evidence IDs remain the provenance source; the evidence must not be re-extracted or duplicated.

## Source-of-truth files

- `data/semester-final-50-reference-selection.csv` — final selected 50, roles, caveats, evidence IDs, batch provenance and citation-key status.
- `references/semester-final-35-doi-import-queue.txt` — exact DOI lookup/import queue for the 35 not-yet-cited works.
- `data/semester-study-inclusion-shortlist.csv` — original candidate-level scientific disposition; retained unchanged.
- `data/semester-bibtex-citation-linkage-audit.csv` — citation-key provenance; retained unchanged.
- `data/original-pdf-batch-attachment-crosswalk.csv` — original batch provenance; retained unchanged.
