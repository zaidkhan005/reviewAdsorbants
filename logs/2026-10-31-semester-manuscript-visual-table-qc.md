# Semester manuscript table and figure cross-reference QC (2026-10-31)

## Scope

Check the manuscript's internal figure/table links and the separate 15-study comparison table after the inclusion-set reconciliation.

## Results

- All **8 local links** found in the main manuscript resolve to existing repository files: Figures 1–4, Working Table 1, the condition-labelled comparison CSV, the mechanism-evidence matrix and the practical-feasibility matrix.
- First figure callouts now appear in numeric order: Figure 1, Figure 2, Figure 3, Figure 4. Figure 2's process-boundary callout was moved into Section 3.5, before the mechanism and feasibility figures, rather than leaving a later-numbered figure cited first.
- Working Table 1 contains **15 study rows**, **15 distinct SEM candidate IDs** and **15 active citation commands**.
- Citation commands in the table are no longer wrapped as inline code, so they can be processed as citations rather than rendered as literal code.
- SEM-038 now reports the TC-specific Table 1 experimental q_e=90.21 mg/g and separately labels kinetic-fit q_e values and the fitted Langmuir q_m=662.25 mg/g. The row also records the more severe Figure 2c feed-mass discrepancy; these numerical capacity endpoints remain held from comparative ranking.
- The main manuscript already links Working Table 1 and all four figure source files. The existing link wording was retained.

## Disposition

Internal references are present and the figure sequence is structurally ordered. This is a repository/Markdown cross-reference check, not a final journal figure export or proof of publisher-style rendering. The Mermaid diagrams and markdown table still need to be rendered into the final document format once the target style/template is known.

## Files changed

- `manuscript/SEMESTER_TABLE_1_CORE_STUDY_COMPARISON_V1.md`
- `manuscript/SEMESTER_MANUSCRIPT_WORKING_V1.md`
