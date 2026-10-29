# Better BibTeX export audit — 2026-10-29

## Scope and outcome

## Full-bibliography processing coverage — updated 2026-10-29

The initial DOI-to-key crosswalk compared the export with the 100-row project screening register and the nine existing Section 2.3 claim-ledger rows. That was **not** a screening or extraction audit of all 164 bibliography entries. The full inventory is recorded in [`bibtex_full_corpus_processing_queue_2026-10-29.csv`](bibtex_full_corpus_processing_queue_2026-10-29.csv).

A first processing wave has now registered **11 previously unregistered papers** as candidates `DISC-069`–`DISC-079` and added **16 provisional online-source evidence rows** to the master evidence file. These provisional rows are visibly flagged for original-PDF page/table/figure and SI verification.

| Current status across all 164 BibTeX entries | Entry count | Meaning |
|---|---:|---|
| Previously registered; evidence rows already present | 90 | Some structured evidence exists, but this does not prove all useful claims/metrics have been extracted or verified |
| Existing registered duplicate BibTeX records with evidence | 4 | Two DOI/title pairs with duplicate Zotero entries; preserve attachments/notes before merging |
| Newly registered with provisional online-source evidence rows | 5 | DISC-069, 071, 072, 077 and 079; PDF pagination/SI checks remain pending |
| Newly registered; title/abstract screen only, evidence extraction pending | 6 | DISC-070, 073–076 and 078; full-text evidence extraction still required |
| Still not in screening register or evidence corpus | 58 | Needs title/abstract screening; bibliography presence alone is not inclusion |
| Registered but likely scope false-positive | 1 | CORP-062 concerns protected-area proximity/community adaptation, not antibiotic adsorption; adjudicate before spending extraction effort |
| **Total exported entries** | **164** | |

The remaining 58 unregistered entries have a provisional title-only triage signal: **45 potential core adsorption/material papers**, **9 contextual/mechanistic sorption papers**, and **4 likely review/background sources**. These are prioritization labels only. Title and abstract screening may change them; no final inclusion or exclusion may be inferred from a BibTeX record or title.

The five newly extracted papers do **not** count as final page-verified extraction: accessible publisher full-text HTML or indexed excerpts were used where available, with the original PDF page locator explicitly left pending. The six abstract-only records still need full-text extraction. CORP-023 is represented in the export by a preprint DOI while the registered published-version candidate already has evidence; count evidence by the linked candidate, not by the preprint DOI alone. CORP-019 has a separate year conflict that must be corrected in Zotero.

The structured corpus currently contains **111 candidate records** and **505 evidence rows**, including the 16 provisional rows from this first wave. The full step-by-step note is [`evidence/2026-10-29-bibtex-initial-screening.md`](../evidence/2026-10-29-bibtex-initial-screening.md).

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

I compared the initial 100-candidate register with the export, then appended the 11 newly registered DOI matches in the first processing wave. The updated crosswalk now contains 111 candidate rows:

- **97** candidates have exactly one DOI match and one exported citation key (86 initial exact matches plus 11 new registrations).
- **2** existing candidates match DOI but have duplicate BibTeX entries, so their key remains ambiguous until duplicate Zotero items are merged.
- **4** candidates have a title-level or version/metadata problem: one is represented only by a preprint, two records have incomplete metadata, and one record lacks its DOI.
- **7** candidates remain absent by DOI or exact-title match in this export: **DISC-022 and DISC-031–DISC-036**. This is a bibliography-inventory result only; it does not alter the screening status. In particular, DISC-022 remains deferred, not screened or excluded.

Year audit: **101** candidate years match the export year, **1** DOI-matched record conflicts, and **9** rows have no reliable year comparison because the export record is incomplete or no item was found. The conflict is CORP-019 and is detailed below.

The full 111-row machine-readable crosswalk is committed at [`references/bibtex_candidate_key_crosswalk_2026-10-29.csv`](bibtex_candidate_key_crosswalk_2026-10-29.csv). The crosswalk status records DOI/key linkage only; it does not determine scientific inclusion or Q1 eligibility.

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


## Addendum — latest exported BibTeX integrity check (2026-10-30)

The user-supplied `full ++ check again.bib` contains 173 entries with 173 unique keys. There are 170 DOI fields and 168 unique DOI values, with **two duplicate-DOI groups** confirmed. The keys and visible metadata are otherwise distinct where present; these four records should be manually checked in Zotero before merging/deleting because the export shows different PDF attachment paths.

| DOI | Exported keys | Matching visible metadata | PDF attachment paths |
|---|---|---|---|
| `10.1016/j.envres.2021.111091` | `ashiqCarbonbasedAdsorbentsFluoroquinolone2021a`; `ashiqCarbonbasedAdsorbentsFluoroquinolone2021b` | Same title, authors, year (2021), journal, volume/pages, and abstract: *Carbon-Based Adsorbents for Fluoroquinolone Removal from Water and Wastewater: A Critical Review*. | `.../RK5GGKHE/Ashiq et al. - 2021 - Carbon-based adsorbents for fluoroquinolone removal from water and wastewater A critical review.pdf`; `.../Z78VWDL6/Ashiq et al. - 2021 - Carbon-based adsorbents for fluoroquinolone removal from water and wastewater A critical review.pdf` |
| `10.1016/j.ijbiomac.2024.133382` | `rostamiSurfaceModifiedChitosan2024a`; `rostamiSurfaceModifiedChitosan2024b` | Same title, authors, year (2024), journal, volume/pages, and abstract: *Surface Modified of Chitosan by TiO2@MWCNT Nanohybrid for the Efficient Removal of Organic Dyes and Antibiotics*. | `.../NXCTLSHY/Rostami et al. - 2024 - Surface modified of chitosan by TiO2@MWCNT nanohybrid for the efficient removal of organic dyes and.pdf`; `.../4S8REVCG/Rostami et al. - 2024 - Surface modified of chitosan by TiO2@MWCNT nanohybrid for the efficient removal of organic dyes and.pdf` |

**Disposition:** These look like duplicate Zotero records by DOI and visible bibliographic metadata, but no merge/delete was performed. Compare attached PDFs, notes, tags, child notes, annotations and collection membership in Zotero; choose a master item and preserve unique content before merging. Neither DOI is in the current semester manuscript's 15 cited works. This new 173-entry export is a newer snapshot; the existing broad-review processing queue remains a dated 164-entry snapshot and has not been silently mixed with the separate semester-paper candidate register.
