# Older GO-baseline source-pin continuation — 3 November 2026

## Scope

This pass continues the existing 46-group V2 source audit. It disaggregates the six older-study claims bundled in Section 3.6.1 into six study-specific entries (CLM-47–CLM-52). The source of truth remains the selected-reference set, existing source/evidence rows and the consolidated Better BibTeX export. No full-text re-extraction was repeated where a prior source audit already exists.

## Individual source pins and permitted use

### CLM-47 — Ghadim et al. (2013), DOI 10.1371/journal.pone.0079254

- **Source:** official PLOS ONE full-text HTML: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0079254
- **Pins:** Methods §§2.2–3; kinetic Fig. 5/Table 1; isotherm Fig. 6/Table 2; thermodynamic Table 3; release Results and Conclusion.
- **Key verified:** `ghadimAdsorptionPropertiesTetracycline2013`.
- **Audit:** Table 2 gives Langmuir-fitted q_m=322.43, 101.87 and 73.53 mg/g at 298, 303 and 308 K; D–R q_m is a distinct fitted result. The source refers to five temperatures in a Results sentence and the thermodynamic section but Table 2 contains three isotherm rows. Kinetics has a separate 298/308/318 K set. Table 1 labels k_2 as 1/min, while the equation defines g/(mg·min). Up to 99.8% TC release is not multicycle regeneration.
- **Disposition:** keep as a historical GO–TC model baseline; do not convert fitted q_m/q_2 into observed q_e or infer missing fits.

The official PLOS article separately labels its kinetic and isotherm figures/tables and states the three isotherm temperatures and reported q_m values. Its thermodynamic discussion gives a separate five-temperature series. This independently supports preserving the temperature-series qualification. 

### CLM-48 — Gao et al. (2012), DOI 10.1016/j.jcis.2011.11.015

- **Source:** official ScienceDirect abstract/Highlights and selected publisher snippets; PubMed abstract cross-check.
- **Key verified:** `gaoAdsorptionRemovalTetracycline2012`.
- **Pin/limit:** abstract-level Langmuir theoretical q_max=313 mg/g; pH/Na+ sensitivity. Full Methods, tables and SI are unavailable in the current source set.
- **Audit:** abstract and publisher Highlights disagree over whether Temkin or Freundlich is the second reported model. The maximum is not a directly verified observed q_e.
- **Disposition:** qualitative or explicitly abstract-level model context only; no condition-matched numeric comparison.

### CLM-49 — Rostamian and Behnejad (2018), DOI 10.1016/j.ecoenv.2017.08.019

- **Source:** official ScienceDirect abstract/Highlights and PubMed abstract; no full-text PDF located in the current source set.
- **Key verified:** `rostamianComprehensiveAdsorptionStudy2018`.
- **Pins:** abstract states separate testing of tetracycline, doxycycline and ciprofloxacin; fitted-capacity order CPN ≫ DCN > TCN; headline maximum up to 173.4 mg/g belongs to CPN.
- **Disposition:** qualitative target-dependence context only. Do not assign 173.4 mg/g to TC or interpolate a missing TC capacity.

### CLM-50 — Yadav et al. (2018), DOI 10.1007/s11356-017-0596-8

- **Source:** author-uploaded primary full text; PubMed abstract; official erratum https://pubmed.ncbi.nlm.nih.gov/29460240/
- **Key verified:** `yadavRemovalFluoroquinoloneAqueous2018`.
- **Pins:** GO synthesis and batch Methods; Table 2 CIP isotherm parameters; Table 4 CIP kinetic fits; pH/dose/concentration/time Results. The official erratum (DOI 10.1007/s11356-018-1381-z) explicitly replaces original Figs. 10–13 (Langmuir, Freundlich, PFO and PSO plots).
- **Audit:** keep CIP, NOR and OFL separate. Langmuir q_max=18.65 mg/g and kinetic PSO/PFO q_e=9.25/1.22 mg/g are fitted parameters, not directly tabulated observed uptake. The kinetic feed ceiling is 10 mg/g, so the PSO fitted value is below it. Use corrected figures only for plot-based interpretation.
- **Disposition:** partial primary-author-copy evidence with erratum control; no direct observed CIP q_e/removal value, reuse, real-water or cost claim is established.

The erratum's PubMed record identifies the correction as a published erratum and explicitly states that figures 10–13 must be replaced. It does not identify Tables 2 or 4 as replaced.

### CLM-51 — Da Silva Bruckmann et al. (2024), DOI 10.1016/j.cej.2024.150484

- **Source:** official ScienceDirect abstract, Highlights and selected publisher snippets; PubMed metadata/abstract cross-check.
- **Key verified:** `dasilvabruckmannAdsorptionCiprofloxacinAqueous2024`.
- **Pin/limit:** publisher source reports author-described maxima of 354.24 mg/g in aqueous medium (pH 5) and 291.39 mg/g in fresh synthetic urine (pH 6); full Methods/tables are not accessible.
- **Audit:** the accessible preview does not establish whether these are observed q_e, conventional q_max or statistical-physics saturation parameters. Keep the two matrices separate; fresh synthetic urine is simulated, not a clinical urine or wastewater sample.
- **Disposition:** provisional, not condition-matched numeric ranking.

### CLM-52 — Chen et al. (2015), DOI 10.1016/j.jhazmat.2014.03.063

- **Source:** official ScienceDirect/PubMed abstract and metadata; detailed text from a non-publisher DockSci mirror of the in-press manuscript.
- **Key verified:** `chenRemovalSulfamethoxazoleCiprofloxacin2015`.
- **Pins:** detailed Methods §§2.1–2.3, Results §§3.2–3.6, Figs. 2–7 and Table 1 come from the third-party mirror; official abstract confirms the study identity and abstract-level headline sorption capacities.
- **Audit:** keep CIP and SMX separate. The 379 mg/g CIP value is a Langmuir S_max; the mirror-derived Freundlich fit has a higher R². Kinetic fitted q_e values are not q_max or observed uptake. Preserve the non-publisher provenance for the detailed numeric/model table.
- **Disposition:** qualified; no condition-matched ranking pending publisher/author full text.

## Legacy key reconciliation

The exact DOI-to-Better-BibTeX matches in the post-merge `Untitled +++.bib` export have now replaced placeholder "key unresolved" fields for CLM-20–CLM-27:

| Claim | Candidate | Verified Better BibTeX key |
|---|---|---|
| CLM-20 | SEM-003 | `yadavRemovalFluoroquinoloneAqueous2018` |
| CLM-21 | SEM-011 | `sayaAdsorptiveRemovalCiprofloxacin2023` |
| CLM-22 | SEM-014 | `dasilvabruckmannDFTTheoreticalExperimental2022` |
| CLM-23 | SEM-021 | `yangDecontaminationTetracyclineThioureadioxidereduced2017` |
| CLM-24 | SEM-001 | `ghadimAdsorptionPropertiesTetracycline2013` |
| CLM-25 | SEM-027 | `choiPolyacrylamideFunctionalizedGraphene2022` |
| CLM-26 | SEM-028 | `wuAdsorptionCiprofloxacinBiocomposite2013` |
| CLM-27 | SEM-026 | `padmajaAdsorptiveRemovalCiprofloxacin2024` |

These values were copied from the existing DOI-matched citation-linkage crosswalk, not inferred from names or manuscript labels. The candidate register's stale "key not verified" notes for SEM-001, SEM-003, SEM-009 and SEM-024 were corrected to the corresponding verified keys.

## Integrity and manuscript effect

- Claim ledger: 46 → **52** distinct claim groups.
- Frozen selected set: 49 works, unchanged.
- Consolidated bibliography: 53 entries (49 selected + four contextual), unchanged.
- No source values, manuscript prose, citation callouts, selection decisions or ranking rules were changed.
- Section 3.6.1 already carries the appropriate metric and source-access qualifications; this pass strengthens traceability rather than rewriting the narrative.

## Next source-pin pass

Continue by splitting the multi-paper magnetic-derivative bundle (CLM-37/38) and polymer/immobilization bundle (CLM-39) in Sections 3.6.2–3.6.3 into source-specific claim records. Preserve source-access tiers; prioritize claims that rely on abstract-only, third-party-mirror or corrected-figure evidence.
