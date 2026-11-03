# Semester manuscript — source and version index

**Index updated:** 3 November 2026  
**Repository:** [zaidkhan005/reviewAdsorbants](https://github.com/zaidkhan005/reviewAdsorbants)  
**Build snapshot:** generated from the latest source commit on `main`; see the linked successful Actions run below.  
**Branch:** main

GitHub is the project's source of truth. The links below point to current source files on main, unless a historical version is explicitly identified.

## 1. Canonical manuscript and integrated tables

| Manuscript component | Current version / status | GitHub source |
|---|---|---|
| Main assembled manuscript | **V2 — canonical manuscript source** | [SEMESTER_MANUSCRIPT_ASSEMBLED_SOURCE_V2.md](../manuscript/SEMESTER_MANUSCRIPT_ASSEMBLED_SOURCE_V2.md) |
| **Table 1A–1B** — search strategy, queries and search-source coverage | Current integrated table source | [SEMESTER_TABLE_1_SEARCH_STRATEGY_SOURCE.md](../manuscript/SEMESTER_TABLE_1_SEARCH_STRATEGY_SOURCE.md) |
| **Table 2A–2I** — condition-labelled comparison of 15 primary studies | Current table content is embedded in the assembled V2 manuscript source | [Open the V2 manuscript](../manuscript/SEMESTER_MANUSCRIPT_ASSEMBLED_SOURCE_V2.md) |
| Earlier standalone comparison | **V1 — historical/pre-integration source; not the current numbering** | [SEMESTER_TABLE_1_CORE_STUDY_COMPARISON_V1.md](../manuscript/SEMESTER_TABLE_1_CORE_STUDY_COMPARISON_V1.md) |
| **Table 3** — evidence coverage for all 49 selected references, including source tiers and numeric qualifications | Current integrated table source | [SEMESTER_TABLE_3_EVIDENCE_COVERAGE_SOURCE.md](../manuscript/SEMESTER_TABLE_3_EVIDENCE_COVERAGE_SOURCE.md) |

**Current numbering:** Table 1 = search strategy; Table 2 = the 15-study comparison; Table 3 = the 49-reference evidence-coverage table. The former standalone S1 and S2 source files were removed after integration. Do not use older references to “Supplementary Table S1/S2” as the current document structure.

## 2. Figures and editable figure sources

| Figure | Source file |
|---|---|
| Figure 1 — scope and adsorbents considered | [SEMESTER_FIGURE_1_SCOPE_TAXONOMY_V1.md](../manuscript/SEMESTER_FIGURE_1_SCOPE_TAXONOMY_V1.md) |
| Figure 2 — process, recovery and cost boundary | [SEMESTER_FIGURE_2_PROCESS_RECOVERY_COST_BOUNDARY_V1.md](../manuscript/SEMESTER_FIGURE_2_PROCESS_RECOVERY_COST_BOUNDARY_V1.md) |
| Figure 3 — mechanism evidence schematic | [SEMESTER_FIGURE_3_MECHANISM_EVIDENCE_SCHEMATIC_V1.md](../manuscript/SEMESTER_FIGURE_3_MECHANISM_EVIDENCE_SCHEMATIC_V1.md) |
| Figure 4 — performance, process, recovery and cost framework | [SEMESTER_FIGURE_4_PERFORMANCE_PROCESS_RECOVERY_COST_FRAMEWORK_V1.md](../manuscript/SEMESTER_FIGURE_4_PERFORMANCE_PROCESS_RECOVERY_COST_FRAMEWORK_V1.md) |

The assembled manuscript source remains the canonical placement/caption source for figures in the final manuscript.

## 3. Evidence database and comparison data

| Purpose | Current source |
|---|---|
| Core extracted semester evidence | [SEMESTER_CORE_EVIDENCE_EXTRACTION.csv](../evidence/semester-paper/SEMESTER_CORE_EVIDENCE_EXTRACTION.csv) |
| Core evidence notes and qualifications | [SEMESTER_CORE_EVIDENCE_NOTES.md](../evidence/semester-paper/SEMESTER_CORE_EVIDENCE_NOTES.md) |
| Condition-labelled study comparison | [semester-condition-labelled-comparison.csv](../data/semester-condition-labelled-comparison.csv) |
| Final selected-reference set — 49 works | [semester-final-49-reference-selection.csv](../data/semester-final-49-reference-selection.csv) |
| Candidate and screening register | [semester-paper-candidate-register.csv](../data/semester-paper-candidate-register.csv) |
| Evidence-readiness audit | [semester-evidence-readiness-audit.csv](../data/semester-evidence-readiness-audit.csv) |
| Manuscript claim-to-evidence audit | [semester-manuscript-claim-evidence-audit.csv](../data/semester-manuscript-claim-evidence-audit.csv) |
| Results/discussion claim-to-evidence audit | [semester-results-discussion-claim-evidence-audit.csv](../data/semester-results-discussion-claim-evidence-audit.csv) |
| Mechanism-evidence matrix | [semester-mechanism-evidence-matrix.csv](../data/semester-mechanism-evidence-matrix.csv) |
| Practical-feasibility matrix | [semester-practical-feasibility-matrix.csv](../data/semester-practical-feasibility-matrix.csv) |
| Remaining-work register | [semester-remaining-work-register.csv](../data/semester-remaining-work-register.csv) |
| Scientific source caveats | [source-caveats.csv](../data/source-caveats.csv) |

## 4. Bibliography and citation style

| Purpose | Current source |
|---|---|
| Consolidated manuscript bibliography (49 selected + 4 contextual references; 53 unique works) | [semester-manuscript-cited-references-49-selected-plus-4-context.bib](../semester-manuscript-cited-references-49-selected-plus-4-context.bib) |
| ACS 2026 citation style file | [american-chemical-society-2026.csl](../references/american-chemical-society-2026.csl) |
| Citation-linkage audit | [SEMESTER_CITATION_LINKAGE_AUDIT.md](SEMESTER_CITATION_LINKAGE_AUDIT.md) |
| Bibliography audit | [FINAL_SEMESTER_MANUSCRIPT_V2_BIBLIOGRAPHY_AUDIT.md](FINAL_SEMESTER_MANUSCRIPT_V2_BIBLIOGRAPHY_AUDIT.md) |

Zotero remains the reference manager; the repository bibliography is the manuscript-build citation input.

## 5. Build system and production records

| Purpose | Current source |
|---|---|
| Manuscript build script | [build_semester_manuscript.py](../scripts/build_semester_manuscript.py) |
| GitHub Actions build workflow | [build-semester-manuscript.yml](../.github/workflows/build-semester-manuscript.yml) |
| Manuscript assembly record | [SEMESTER_MANUSCRIPT_ASSEMBLY_RECORD.md](SEMESTER_MANUSCRIPT_ASSEMBLY_RECORD.md) |
| Claim-by-claim scientific audit | [SEMESTER_MANUSCRIPT_V2_CLAIM_BY_CLAIM_SCIENTIFIC_AUDIT.md](SEMESTER_MANUSCRIPT_V2_CLAIM_BY_CLAIM_SCIENTIFIC_AUDIT.md) |
| Successful integrated build run | [GitHub Actions run 41593950973](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41593950973) |

The successful Actions run above produced the integrated DOCX and PDF in its workflow artifact. These generated binary files are not stored as source files in the repository; use the run's **Artifacts** section to download them. The artifact follows GitHub Actions retention and expires after the retention window.

## 6. Version guidance

- **Use SEMESTER_MANUSCRIPT_ASSEMBLED_SOURCE_V2.md as the canonical editable manuscript source.**
- Use the Table 1 and Table 3 source files above for changes to their integrated content. Table 2 is currently maintained within the assembled V2 manuscript; the standalone Table 1 comparison file is the earlier V1 record.
- Treat SEMESTER_MANUSCRIPT_WORKING_V1.md, SEMESTER_INTRODUCTION_AND_SCOPE_V1.md, SEMESTER_RESULTS_AND_DISCUSSION_V1.md, and the standalone Table 1 comparison V1 as earlier working versions, not as the latest assembled manuscript.
- Earlier build/audit records may mention the old S1/S2 arrangement. The 3 November 2026 status update in the assembly record supersedes those production details.