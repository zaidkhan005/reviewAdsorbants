# Better BibTeX export audit — 2026-10-29

## Scope and outcome

## Important coverage correction — all bibliography entries are not processed

The previous DOI-to-key crosswalk compared the export only against the **100-row project screening register** and the nine existing Section 2.3 claim-ledger rows. It did **not** mean that the full 164-entry bibliography had undergone screening or evidence extraction.

A second, entry-by-entry inventory was therefore added: [`bibtex_full_corpus_processing_queue_2026-10-29.csv`](bibtex_full_corpus_processing_queue_2026-10-29.csv). It compares every exported key against the live candidate register and master evidence rows.

| Status across all 164 BibTeX entries | Entry count | Meaning |
|---|---:|---|
| Registered; evidence rows already present | 90 | Some structured evidence exists for the candidate; this does not prove all claims/metrics in the paper have been extracted or checked |
| Registered; evidence present but duplicate BibTeX item | 4 | These are the two duplicate DOI/title groups (two records each); merge only after preserving attachments/notes |
| Not in screening register or evidence | 69 | The item has not yet been registered/screened in this project workflow; it requires triage, not automatic inclusion |
| Registered but likely scope false-positive | 1 | CORP-062 is about proximity to protected areas/community adaptation, not antibiotic adsorption. Adjudicate the existing candidate record; do not spend extraction effort unless a documented scope rationale is found |
| **Total exported entries** | **164** | |

The 69 unregistered entries receive a **title-only triage signal**, not a final screening decision: **56 potential core adsorption/material papers** are the highest-priority screening queue; **9 contextual/mechanistic sorption papers** need a scope check first; and **4 likely reviews/background sources** should be used for citation discovery, not as primary quantitative evidence. The title signal must be confirmed with abstract/full text. Do not infer inclusion or exclusion from a BibTeX record or title alone.

One registered paper, CORP-023, is represented in the export by a preprint DOI while the project evidence is attached to its published-version candidate record; the queue therefore counts evidence by linked candidate ID rather than incorrectly declaring the paper unextracted because the DOI/version differs. CORP-019 also has a year mismatch that must be fixed in Zotero and re-exported.



Audited the uploaded `full ++.bib` export (SHA-256: `e8275eb705f3e1d3c85ba0acdc6caeda37f8ffe6c1ea5000f69c1d72c85f16ec`) against the live claim-to-source ledger and checked selected metadata gaps against publisher/index records.

- 164 BibTeX entries: 163 `@article`, 1 `@misc`.
- 164 distinct citation keys; no duplicate key strings.
- 161 entries have a DOI; these resolve to 159 unique DOI values.
- Two duplicate DOI/title groups are present. In both groups, the only differing BibTeX field is the local Zotero attachment path (`file`), which means they appear to be duplicate reference records carrying separate attachment paths. Do not delete or merge until Zotero's notes, attachments and annotations have been checked.
- Three records have no DOI; two lack year, journal and DOI; one has year and journal but no DOI.
- One `@misc` entry is a Research Square preprint for an article that also appears in the corpus as a published journal article; prefer the published version for ordinary manuscript citation, after checking that it is the same work.

## Claim-ledger DOI matches

The nine seed rows in `manuscript/CLAIM_TO_SOURCE_CITATION_LEDGER.md` reduce to three verified DOI/title matches against the uploaded export. The ledger now contains the exact exported Better BibTeX keys for these references.

| Claim IDs | Repository candidate | DOI | Better BibTeX key in export | Export metadata |
|---|---|---|---|---|
| S23-001–S23-004 | DISC-025 | 10.1016/j.jwpe.2025.109355 | `sousaFixedbedAdsorptionAntibiotics2026` | Sousa et al., 2026 |
| S23-005–S23-006 | CORP-020 | 10.1016/j.biortech.2023.128593 | `nguyenPhosphoricAcidactivatedBiochar2023` | Nguyen et al., 2023 |
| S23-007–S23-009 | DISC-028 | 10.1016/j.scitotenv.2023.169035 | `gaoDyeingSludgederivedBiochar2024` | Gao et al., 2024 |

**Citation insertion is still pending.** The key is now grounded in the actual export, but the target journal citation style has not been selected and Zotero-generated citations have not yet been rendered in a submission document. Do not replace the `CITATION_PENDING` cells with manually typed citations.

### Sousa publication year

The Better BibTeX export gives 2026. The publisher's ScienceDirect record lists the article in *Journal of Water Process Engineering*, volume 81, January 2026, article 109355, with DOI `10.1016/j.jwpe.2025.109355`. Therefore the 2026 publication year is supported; the year embedded in the DOI string is not the citation year. [Publisher record](https://www.sciencedirect.com/science/article/pii/S2214714425024286).

## Screening-register DOI crosswalk

I also compared the 100 candidate rows in `data/corpus-screening-register.csv` with the uploaded export:

- **87** candidates have exactly one DOI match and one exported citation key.
- **2** candidates have matching DOI but two duplicate BibTeX entries, so the citation key remains ambiguous until those duplicate Zotero items are merged.
- **4** candidates have a title-level match but not a valid one-to-one DOI match: one is represented only by a preprint, and three records lack required DOI/year/journal/author metadata.
- **7** candidates are not represented by DOI or exact-title match in this export: **DISC-022 and DISC-031–DISC-036**. This is a bibliography-inventory result only; it does not alter the screening status. In particular, DISC-022 remains deferred, not screened or excluded.

Year audit: **90** candidate register years align with the matched export year, **1** DOI-matched record conflicts, and **9** rows have no reliable year comparison because the export record is incomplete or no item was found. The conflict is CORP-019 and is detailed below.

The full 100-row machine-readable crosswalk is committed at [`references/bibtex_candidate_key_crosswalk_2026-10-29.csv`](bibtex_candidate_key_crosswalk_2026-10-29.csv). The crosswalk status records DOI/key linkage only; it does not determine scientific inclusion or Q1 eligibility.

## Duplicate records requiring Zotero cleanup

1. DOI `10.1016/j.envres.2021.111091`: keys `ashiqCarbonbasedAdsorbentsFluoroquinolone2021a` and `ashiqCarbonbasedAdsorbentsFluoroquinolone2021b`. Title: “Carbon-Based Adsorbents for Fluoroquinolone Removal from Water and Wastewater: A Critical Review.” The exported bibliographic fields are identical; only the file paths differ.
2. DOI `10.1016/j.ijbiomac.2024.133382`: keys `rostamiSurfaceModifiedChitosan2024a` and `rostamiSurfaceModifiedChitosan2024b`. Title: “Surface Modified of Chitosan by TiO2@MWCNT Nanohybrid for the Efficient Removal of Organic Dyes and Antibiotics.” The exported bibliographic fields are identical; only the file paths differ.

**Action:** merge duplicate Zotero items after checking that attachments, notes and annotations are preserved. Then re-export Better BibTeX and refresh any ledger keys that change. Do not manually strip the `a/b` suffixes.

## Additional DOI-matched year conflict

- **CORP-019 — levofloxacin on barley husks and eggshells:** the DOI matches, but the export key `mohammed-ridhaAdsorptionLevofloxacineAntibacterial2023` and exported year say 2023. The journal's own record states the article was published on 1 December 2014 in *Journal of Engineering*, volume 20, issue 12, pages 88–104. Correct the year in Zotero, then re-export Better BibTeX; the generated key may change. [Journal record](https://joe.uobaghdad.edu.iq/index.php/main/article/view/2591/version/2126).

## Incomplete or inconsistent records

### 1. Chlortetracycline / kaolin–alginate beads — metadata missing

Export key: `liuSustainableWastewaterDecontamination`. The exported record lacks year, journal and DOI and omits an author listed in the publisher/index metadata.

Verified public metadata: Liu et al.; 2025; *Royal Society Open Science*, 12(10), article 250439; DOI `10.1098/rsos.250439`. The indexed author list includes Yongbing Zhang. Confirm and correct the Zotero item itself, then re-export. Sources: [PubMed record](https://pubmed.ncbi.nlm.nih.gov/41063724/) and [publisher DOI](https://doi.org/10.1098/rsos.250439).

### 2. Activated bentonite / ciprofloxacin — metadata missing

Export key: `magedCharacterizationActivatedBentonite`. The exported record lists only Ali Maged and lacks year, journal and DOI.

Verified public metadata: Maged, Kharbish, Ismael and Bhatnagar; 2020; *Environmental Science and Pollution Research*, 27(26), 32980–32997; DOI `10.1007/s11356-020-09267-1`. Confirm and correct the Zotero item itself, then re-export. Sources: [Springer record](https://link.springer.com/article/10.1007/s11356-020-09267-1) and [PubMed record](https://pubmed.ncbi.nlm.nih.gov/32524402/).

### 3. Biochar review on tetracycline removal — DOI missing

Export key: `yanRemovalTetracyclineWater2024`. The export has year 2024 and the journal *Journal of Water Process Engineering* but no DOI and an incomplete author list.

Verified public metadata: Yan, Song, Miao, Ma, Zhao and Yin; 2024; *Journal of Water Process Engineering*, 60, article 105215; DOI `10.1016/j.jwpe.2024.105215`. Add the DOI and verify all authors in Zotero. Source: [ScienceDirect record](https://www.sciencedirect.com/science/article/pii/S2214714424004471).

### 4. Amoxicillin chitosan–alginate composite beads — preprint vs published version

Export key: `pinheiroAdsorptionAmoxicillinChitosan2024` is a `@misc` record with Research Square DOI `10.21203/rs.3.rs-4331760/v1` and no journal. The corpus already contains the journal publication under candidate CORP-023, DOI `10.1007/s11356-024-35293-4`. The public record indicates the Research Square version preceded the journal publication. Verify that these are the same work and normally cite the peer-reviewed journal version only, while preserving any meaningful version-specific material. Source: [version history / published record](https://sciety.org/articles/activity/10.1007/s11356-024-35293-4).

## Citation workflow from here

1. Fix the four Zotero records/version issue and merge the two duplicate pairs without losing attachments or notes.
2. Export the full collection again as Better BibTeX. Keep the keys from the real export as the authority; never infer them from candidate IDs.
3. Map repository claim IDs and evidence IDs to keys by DOI, with title/author/year as a secondary check. Ambiguous or DOI-less matches remain pending until manually verified.
4. Choose the target journal's citation style. Insert citations with Zotero in Word (or use a deliberate Markdown/Pandoc route if the manuscript remains Markdown) and generate the bibliography from the same reference library.
5. Audit the rendered manuscript: every factual claim has direct source support, every in-text citation resolves to one correct bibliography entry, each cited entry appears in the bibliography, and temporary candidate-ID/DOI hyperlinks are not standing in for formal citations.

The uploaded `.bib` file itself is not stored in GitHub. The key audit above records the results needed for the repository workflow; keep licensed full-text PDFs in Zotero or another appropriate storage location.
