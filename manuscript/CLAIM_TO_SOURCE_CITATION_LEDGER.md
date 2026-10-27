# Claim-to-source and citation-key audit ledger

**Purpose:** Keep every manuscript claim traceable from its location in prose or a table to a repository evidence ID, the original source location, the exact Zotero item / Better BibTeX citation key, and the final in-text citation and bibliography entry.

**Status:** Ledger schema created; sample rows populated from the current Section 2.3 biochar working draft. Zotero citation keys and final author–date strings are intentionally marked **PENDING — verify in Zotero/Better BibTeX**. Do not invent a key based on a candidate ID or guess author-name formatting. Candidate DOI links in manuscript drafts remain temporary research locators.

## Required workflow

1. Assign a stable claim ID to each factual sentence and each table row that reports evidence. A sentence containing multiple independent results may need to be split into separate claim IDs.
2. Record the manuscript path and subsection/paragraph or table/row.
3. Record candidate ID and one or more evidence IDs. For multi-source synthesis, list each source that directly supports the clause it is attached to; do not add a citation simply because a paper is thematically relevant.
4. Confirm that the cited evidence points to the **original primary source** for measured values. Review articles may support field mapping or contextual synthesis, but a value compiled by a review must be traced to the original study before quantitative use.
5. Record the pinpoint location exactly as available: PDF page plus printed page when they differ, and table/figure/equation/section. If not reported, use “not recorded” or “not accessible”; never guess.
6. Match the candidate to the exact Zotero item by DOI and then verify author order/spelling, publication year, title, journal, volume/pages or article number and DOI. Record the Better BibTeX key exported by the actual Zotero item.
7. Insert the final citation using Zotero / Better BibTeX rather than hand-typing it as a finished bibliography record. Use the style required by the eventual target journal.
8. Audit the final render: every factual claim has support; every in-text citation resolves to exactly one correct bibliography entry; all cited references are in the bibliography; uncited bibliography entries are intentional; no temporary candidate-ID/DOI links remain where formal citations are required.

## Status vocabulary

- **PENDING_SOURCE_CHECK** — evidence record exists but source pinpoint or conditions need rechecking.
- **SOURCE_LOCATED** — original-source page/table/figure is recorded; scientific caveats remain visible.
- **ZOTERO_MATCH_PENDING** — Zotero item not matched/verified for this ledger row.
- **KEY_PENDING** — Better BibTeX key not yet read from the actual export.
- **CITATION_PENDING** — final style-specific in-text citation has not been inserted.
- **READY_FOR_FINAL_AUDIT** — source, key, citation and bibliography mapping all verified.
- **HOLD** — the specific numerical claim is quarantined due to unresolved inconsistency; do not use as a quantitative conclusion.

## Seed ledger

| Claim ID | Manuscript location | Claim / table item (short description) | Candidate ID | Evidence ID(s) | Original source pinpoint | Caveat / allowed interpretation | Zotero item key / item identity | Better BibTeX key | Final in-text citation | Bibliography entry / audit status |
|---|---|---|---|---|---|---|---|---|---|---|
| S23-001 | `manuscript/SECTION_2_3_BIOCHAR_V1.md` §2.3.1 ¶2 | Brewery-residue biochar preparation, 23% yield and BET area | DISC-025 | EV-B07-011 | Source PDF pp. 2, 4; §2.2, §3.1, Table S2 referenced | Standard/unactivated biochar, but acid wash, neutralisation and drying are part of process; SI inventory unavailable | PENDING — verify DOI 10.1016/j.jwpe.2025.109355 in Zotero | KEY_PENDING | CITATION_PENDING | Zotero/BibTeX crosswalk pending |
| S23-002 | `manuscript/SECTION_2_3_BIOCHAR_V1.md` §2.3.1 ¶3 | Brewery biochar batch capacities and filtered/autoclaved real-effluent matrix effect | DISC-025 | EV-B07-012; EV-B07-013 | Source PDF pp. 3–6; §§2.5–3.2; Figs. 1–2; supplemental tables referenced | q_m is fitted and in μmol/g; do not label effluent untreated or native-contaminant removal | PENDING — same Zotero DOI match | KEY_PENDING | CITATION_PENDING | Verify published year/metadata against actual item |
| S23-003 | `manuscript/SECTION_2_3_BIOCHAR_V1.md` §2.3.1 ¶4 | Fixed-bed q_TH, breakthrough and mixture/matrix effects | DISC-025 | EV-B07-014–EV-B07-017 | Source PDF pp. 6–10; Figs. 3–5; Tables 2–4 | q_TH, q_Y, q_s, treated volume and breakthrough time are distinct; no cross-class rank | PENDING — same Zotero DOI match | KEY_PENDING | CITATION_PENDING | In-text and bibliography audits pending |
| S23-004 | `manuscript/SECTION_2_3_BIOCHAR_V1.md` §2.3.1 ¶5–6 | 600 °C regeneration, production LCA hotspots and missing boundary | DISC-025 | EV-B07-018; EV-B07-019 | Source PDF pp. 10–12; Figs. 6–7; SI Table S4 referenced | Capacity ratio >100% is not desorption; LCA is production-only; total SI impacts unavailable | PENDING — same Zotero DOI match | KEY_PENDING | CITATION_PENDING | Do not describe as full lifecycle comparison |
| S23-005 | `manuscript/SECTION_2_3_BIOCHAR_V1.md` §2.3.2 ¶1 | Sunflower-husk SF-600 vs phosphoric-acid-activated PSF fitted capacities | CORP-020 | EV-B11-012; EV-B11-013 | Source PDF pp. 4–6; Table 2 | Fitted q_m only; not observed low-concentration uptake; ibuprofen excluded from antibiotic-only synthesis | PENDING — verify DOI 10.1016/j.biortech.2023.128593 in Zotero | KEY_PENDING | CITATION_PENDING | Figure 2 condition-caption mismatch disclosed in draft |
| S23-006 | `manuscript/SECTION_2_3_BIOCHAR_V1.md` §2.3.2 ¶2 | Sunflower study condition-label caveat and missing cost/reuse/real-water evidence | CORP-020 | EV-AUD-007; EV-B11-015–EV-B11-018 | Source PDF pp. 4–6; Fig. 2 caption; evidence-note locations | Preserve discrepancy; do not infer panel conditions from mismatched caption | PENDING — same Zotero DOI match | KEY_PENDING | CITATION_PENDING | Negative claim is limited to the extracted source record |
| S23-007 | `manuscript/SECTION_2_3_BIOCHAR_V1.md` §2.3.2 ¶3 | KSC-8 activation route, BET area inconsistency and temperature mismatch | DISC-028 | EV-B01-012; EV-B01-013 | Source PDF pp. 2, 4–7; Table 2; §§2.2–3.1 | 1178.4 vs 1078.4 m²/g discrepancy; methods 298 K vs conclusion 278 K; batch dose unclear | PENDING — verify DOI 10.1016/j.scitotenv.2023.169035 in Zotero | KEY_PENDING | CITATION_PENDING | No silent reconciliation |
| S23-008 | `manuscript/SECTION_2_3_BIOCHAR_V1.md` §2.3.2 ¶4 | KSC-8 fitted q_max and observed uptake values in separate experiments | DISC-028 | EV-B01-013; EV-B01-014 | Source PDF pp. 6–7; Table 1; Figs. 3–4 | Fitted q_max 1081.3 mg/g not pooled with observed 305.99 mg/g; dose missing for a full balance check | PENDING — same Zotero DOI match | KEY_PENDING | CITATION_PENDING | Quantitative comparison status: HOLD for ranking |
| S23-009 | `manuscript/SECTION_2_3_BIOCHAR_V1.md` §2.3.2 ¶5–6 | KSC-8 fixed-bed threshold capacity, regeneration labels and author cost estimate | DISC-028 | EV-B01-016–EV-B01-019 | Source PDF pp. 3, 7–8; Fig. 4f; Fig. 5; Fig. 6 | 543.46 mg/g threshold-specific is separate from disputed 1124.2 mg/g; regeneration labels conflict; ~$9/kg is preliminary, boundary-limited estimate | PENDING — same Zotero DOI match | KEY_PENDING | CITATION_PENDING | Numerical ranking HOLD; cost claim can only be reported with full caveat |

## Final audit checklist

- [ ] Every paragraph is split into auditable claims where needed.
- [ ] Every numeric manuscript claim maps to one or more evidence IDs.
- [ ] Original-source page, table, figure, equation or section is recorded.
- [ ] Source location agrees with the exact PDF/version used.
- [ ] Dose, concentration, volume, units, pH, temperature, matrix, time, and model are recorded wherever available.
- [ ] Caveat text is reflected in the manuscript claim/table note.
- [ ] Better BibTeX keys are copied from an actual Zotero export, not guessed.
- [ ] Final citations use the target journal style and are inserted through the citation workflow.
- [ ] Every final in-text citation has exactly one matching bibliography entry.
- [ ] Every bibliography entry is cited or intentionally included as background.
- [ ] No unresolved candidate-ID DOI links remain in the submission manuscript.
- [ ] DISC-022 remains deferred until the user supplies the full-text PDF.

## Scope note

This ledger is a working control document, not proof that citations are already final. The Zotero library itself is not embedded in GitHub, and this pass did not have a verified current Better BibTeX export to read stable citation keys from. Citation conversion remains pending until the actual Zotero records/export and target style are available.

**Deferred-item guardrail:** DISC-022 stays deferred, not screened or excluded, until the user supplies its full-text PDF.
