# Figure rendering and visual QA record

**Date:** 31 October 2026
**Project:** Semester manuscript V2 — Antibiotic Adsorption Review

## Result

All four conceptual figure sources were rendered to compact, manuscript-proportioned vector outputs and visually inspected. Each figure is available as SVG, PDF and 240 dpi PNG, with an editable Graphviz DOT representation. The original Mermaid Markdown source files in the repository were left unchanged and remain the project's primary editable figure sources.

The Mermaid CLI was not available in the rendering environment, so Graphviz was used as a fallback renderer. The compact layouts group related concepts into panels to reduce width and preserve legibility. No scientific meaning was added by the renderer.

## Render dimensions

Dimensions below are the Graphviz SVG page dimensions in points. A point is 1/72 inch.

| Figure | SVG width × height | Visual QA |
|---|---:|---|
| Figure 1 — scope taxonomy | 452 × 492 pt | Passed — scope families, eligibility gate, endpoints, exclusions and target-specificity guardrails legible |
| Figure 2 — process/recovery/cost boundary | 495 × 642 pt | Passed — preparation and treatment columns; recovery and whole-process cost boundary legible |
| Figure 3 — mechanism evidence schematic | 452 × 512 pt | Passed — solution chemistry and adsorbent features converge on candidate interactions and transport |
| Figure 4 — performance/process/recovery/cost framework | 452 × 496 pt | Passed — four evaluation dimensions remain explicit within two grouped panels; no score/rank is implied |

## Content/claim safeguards retained

- Figure 1 remains a scope and eligibility map, not a PRISMA flow diagram.
- Figure 2 consolidates alternative preparation, treatment and recovery routes. It is not one standardized process or a measured mass balance.
- Figure 3 depicts candidate, non-exclusive, condition-dependent mechanisms. It does not assign quantitative contribution or prove a unique binding pathway.
- Figure 4 is a non-scoring decision framework. High adsorption performance alone does not demonstrate low cost.

## Source and output files

The four Mermaid source files remain in the manuscript/SEMESTER_FIGURE_1_SCOPE_TAXONOMY_V1.md through manuscript/SEMESTER_FIGURE_4_PERFORMANCE_PROCESS_RECOVERY_COST_FRAMEWORK_V1.md files.

The rendered SVG/PDF/PNG and DOT files, contact sheet, proposed captions and render manifest were delivered in the separate archive review_paper_figure_exports_2026-10-31.zip. The archive is an export artifact; it has not been committed as binary files to this repository.

## Still required before submission

The figures have not yet been inserted into the assembled Word/PDF manuscript. Final page-layout QA must check their actual placed size, caption numbering, in-text cross-references, pagination and consistency with the university's required format. Bibliography-style rendering and final manuscript proof also remain pending.