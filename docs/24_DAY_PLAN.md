# 24-day review-paper sprint

The original sprint rule remains: every workday ends with a visible deliverable; do not polish sentences while a section is incomplete. This plan tracks completed artifacts—not work that merely appears in a conversation.

## Current restart checkpoint (2026-10-27)

The intake stage has advanced substantially beyond the earlier 2026-10-24 checkpoint.

- **20 documented PDF-processing batches**, with detailed extraction notes through Batch 20.
- **310 source-linked evidence records** in `data/corpus-evidence.csv`. These are findings, not 305 distinct papers.
- **62 candidate/screening records** in `data/corpus-screening-register.csv`.
- **61 of 62** candidates have completed full-text screening; `DISC-022` is **deferred** until the user supplies its full-text PDF. It is not screened or excluded and is temporarily outside the active queue. `CORP-025` was screened using its open-access PubMed Central full text; a dose/capacity inconsistency is recorded.
- **64 source-caveat entries** in `data/source-caveats.csv`.
- The evidence CSV contains records for **59 distinct candidate IDs**; evidence records include primary studies and reviews, so this does not equal the final bibliography.
- The downloaded-PDF intake is complete for the files supplied through Batch 20. Do not assume additional user-held PDFs remain to be uploaded.
- **Journal-quartile verification has started**: first-pass entries are recorded for `CORP-025` (iScience; 2024 SJR Q1, Multidisciplinary; direct SCImago confirmation still pending) and `DISC-022` (Journal of Hazardous Materials; 2024 Scopus/SJR Q1 across relevant categories, source linked). Remaining candidates are still pending; this is not a full-corpus quartile audit.
- **Final include/exclude decisions, integrated cross-paper tables and substantive manuscript section drafts remain incomplete.** The database and batch reports are evidence infrastructure, not a completed review manuscript.

Current repository references:
- [Working manuscript outline](../manuscript/REVIEW_OUTLINE.md)
- [Master evidence register](../data/corpus-evidence.csv)
- [Screening register](../data/corpus-screening-register.csv)
- [Source-caveat register](../data/source-caveats.csv)
- [Research workflow](RESEARCH_WORKFLOW.md)
- [Current project checkpoint log](../logs/2026-10-27-project-checkpoint.md)

## Sprint status table

| Day | Planned work | End-of-day deliverable | Status in this workspace |
|---|---|---|---|
| 1 | Full-corpus intake, reference deduplication, and evidence system | Unified screening register plus a source-linked evidence record | **Substantially complete for supplied corpus:** 62 candidates, 20 batch reports, 310 evidence records. The only unresolved full-text screen is `DISC-022`, deferred until the user supplies the PDF; quartile checks for the other candidate journals continue separately. |
| 2 | Section 2.1 raw biomass literature | Evidence-screened subsection draft | Not complete; no verified finished section draft recorded. |
| 3 | Finish Section 2.1 | Complete rough draft of 2.1 | Not complete/verified. |
| 4 | Section 2.2: natural clays & biopolymers | 8–15 screened papers, evidence notes and rough draft | Taxonomy and evidence exist; final screening/Q1 check and full draft remain. |
| 5 | Finish/complete Section 2.2 biopolymer evidence | Complete rough draft of 2.2 | Not complete/verified. |
| 6 | Biochar and modified biochar | Evidence set and rough draft of 2.3 | Evidence set is growing; Q1 screen and draft remain. |
| 7 | Synthesize processing and modification comparisons | Comparative table and draft synthesis | Pending. |
| 8 | Engineered/nano-carbon adsorbents | Evidence set and rough draft of 2.4 | Evidence set is growing; final Q1 shortlist and draft remain. |
| 9 | Complete Section 2 and compare material classes | Integrated classification/synthesis | Pending. |
| 10 | Processing–cost–performance continuum | Core framework figure/table and narrative | Pending. |
| 11 | Kinetics | Kinetic-model analysis | Individual records extracted; integrated cross-paper analysis pending. |
| 12 | Isotherms | Isotherm analysis | Individual records extracted; integrated cross-paper analysis pending. |
| 13 | pH, speciation and mechanisms | Mechanism/speciation synthesis | Individual records extracted; evidence-weighted synthesis pending. |
| 14 | Techno-economics and energy | Cost/energy comparison | Data are uneven; comparative synthesis pending. |
| 15 | Regeneration and spent adsorbent | Regeneration/end-of-life synthesis | Individual caveats recorded; integrated synthesis pending. |
| 16 | Real-water matrix effects | Matrix-effects synthesis | Individual records extracted; integrated synthesis pending. |
| 17 | Practical applications, batch/fixed-bed/MBR/polishing | Application section | Column and adjacent-technology evidence exists; section draft pending. |
| 18 | Challenges | Evidence-backed challenges | Some gaps are documented; final synthesis pending. |
| 19 | Future perspectives | Prioritized future directions | Pending. |
| 20 | Introduction and conclusions | Rough drafts | Pending. |
| 21 | Figures and tables | Complete visual set | Pending; no final integrated figure/table set verified. |
| 22 | Citation audit | Verified reference list and in-text links | Pending; Q1 and citation-to-primary-source checks remain. |
| 23 | Scientific editing | Revised complete manuscript | Pending. |
| 24 | Final quality assurance | Submission-ready manuscript package | Pending. |

## Next execution sequence after intake

Do not continue routine batch intake unless a specific evidence gap requires a targeted source. The next workstream is:

1. **Close the remaining full-text screen** (`DISC-022`). `CORP-025` has been screened from its open-access full text, with dose/capacity conflicts flagged rather than resolved.
2. **Continue journal-quartile verification** for the remaining candidates, recording provider, ranking year, subject category, quartile and verification URL. Keep the ranking system and year consistent; do not substitute impact factor or reputation for a quartile record.
3. **Make explicit retain / exclude / background-only decisions** after screening and quartile checks. A review may be useful for context and citation discovery without entering the primary experimental comparison.
4. **Build the comparative evidence tables** from verified primary studies, separating observed uptake, fitted (q_{\max}), removal percentage, column capacity, desorption and degradation.
5. **Draft manuscript sections from those tables**, then verify each important numerical/mechanistic claim against its primary source and Zotero reference.

This is a planning record, not a claim that prior deliverables are fully finished. Mark a section complete only when the actual draft/artifact has been checked.
