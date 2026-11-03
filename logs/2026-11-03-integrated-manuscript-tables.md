# Integrated manuscript tables — production record

**Date:** 3 November 2026  
**Repository branch:** main  
**Successful build commit:** 8ad688e1b355c932ff1e3f60a442fc939ade9197  
**GitHub Actions run:** [41593950973](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41593950973) — completed successfully  
**Artifact ID:** 13211670732

## Current manuscript structure

- **Table 1A–1B:** literature search queries and sources.
- **Table 2A–2I:** condition-labelled comparison of 15 primary studies and related endpoint/practical-feasibility panels.
- **Table 3:** selected-reference evidence coverage for all 49 works, with a compact index followed by study-level source/evidence qualifications.

## Source files

- Main editable manuscript: manuscript/SEMESTER_MANUSCRIPT_ASSEMBLED_SOURCE_V2.md.
- Table 1 source: manuscript/SEMESTER_TABLE_1_SEARCH_STRATEGY_SOURCE.md.
- Table 3 source: manuscript/SEMESTER_TABLE_3_EVIDENCE_COVERAGE_SOURCE.md.
- Table 2 content is maintained in the assembled V2 manuscript; the old standalone SEMESTER_TABLE_1_CORE_STUDY_COMPARISON_V1.md remains a historical V1 comparison source.
- Build script: scripts/build_semester_manuscript.py.
- Workflow: .github/workflows/build-semester-manuscript.yml.

## Build and quality checks

- GitHub Actions successfully generated the integrated manuscript DOCX and PDF.
- Table 3 source contains 49 selected study records and 49 distinct citation keys; the keys were checked against the consolidated manuscript bibliography.
- The build script validates all 49 study entries and keeps each study heading with its title and opening metadata in DOCX pagination.
- The generated DOCX/PDF are in the GitHub Actions artifact for run 41593950973; they are not committed as binary files to the repository.

## Superseded arrangement

The former separate files SEMESTER_SUPPLEMENTARY_TABLE_S1_49_REFERENCE_COVERAGE.md and SEMESTER_SUPPLEMENTARY_TABLE_S2_SEARCH_STRATEGY.md were removed after integration. Their current content is represented by manuscript Tables 3 and 1, respectively. Current manuscript-facing text contains no “Supplementary Table” labels.