# Critical scientific-hold visibility check — 3 November 2026

## Purpose

Following the final 94-claim manuscript integration and successful formula-corrected build, five high-risk source records were checked directly in the reader-facing manuscript to confirm that integration had not silently promoted held values into observed results, condition-matched rankings or unqualified process claims.

## Hold-by-hold result

| Candidate | Critical hold | Reader-facing treatment checked | Outcome |
|---|---|---|---|
| **SEM-010 — Yasmin et al. (2024), GO/CIP** | 99% removal does not reconcile with experimental kinetic (q_e=78.82) mg/g under the nominal 40 mL/20 mg/L dose; PSO-fitted (q_e=79.36) mg/g is a separate model output; conclusion says 20 g/L while main text says 20 mg/L. A 25.1 mg/L effective dose is only a derived possibility. | Section 3.1 and Table 2B/2C/2D/2E carry the 99%, experimental and fitted endpoints separately, show the mass-balance calculation and keep the conclusion's unit conflict visible. The note says not to invent a correction. | **Retained; not ranked as a single reconciled uptake result.** |
| **SEM-038 — Zhang and Wu (2022), N-rGO/TC** | Stated feed and N-rGO mass imply an 80 mg/g TC ceiling in Figure 2a, whereas Table 1 says 90.21 mg/g; Figure 2c has a more pronounced feed-basis issue. The 1,265.82 mg/g abstract maximum belongs to clindamycin (CLI), not TC; TC Langmuir (q_m=662.25) mg/g is fitted. | Section 3.2 explicitly keeps the finite-feed mismatch, labels the 662.25 mg/g TC (q_m) as fitted and assigns 1,265.82 mg/g to CLI. Tables distinguish TC from CLI and mark held uptake. Sections 4.2/4.3 and 5.3 call ion/HA tests simulated matrices, not native water. | **Retained; held TC uptake excluded from ranking.** |
| **SEM-046 — Tekle Tegie et al. (2026), ZrO₂–Fe₃O₄/GO/CIP** | Pharmaceutical-effluent concentration falls 8.37→2.01 mg/L, which calculates to 76.0% removal rather than 90.75% stated. Eight-cycle value differs between body (85.7%) and abstract (85.45%). Synthetic-water optimum and the single effluent sample are distinct. | Section 3.6.4 reports the calculated 76.0%, contrasts it with 90.75%, and notes the cycle-value discrepancy. Section 5.3 treats the sample as one pharmaceutical-effluent result, not common real-water validation. | **Retained; no unsupported real-effluent performance claim.** |
| **SEM-050 — Lemaoui et al. (2026), GO–TOPO:LevA membrane** | Municipal wastewater was PES-prefiltered (0.45 µm) and deliberately spiked. The membrane results are not native unspiked wastewater performance. Powder-batch (q_e=22.7pm0.6) mg/g remains held because its precise feed/mass denominator is unresolved. USD 2.5–6.8/m² is active-layer material cost, and 14–59 kg CO₂-eq/m² is environmental footprint—not financial cost per m³. | Section 3.6.4 and 5.3 state prefiltration and spiking; the powder-batch uptake is explicitly quarantined; membrane results are separated by single-solute/four-drug/low-concentration tests. Sections 3.6.4 and 5.4 keep the USD/m² and carbon-footprint units separate from financial cost per treated volume. | **Retained; no native wastewater or full-system cost overclaim.** |
| **SEM-051 — Saheed et al. (2026), CMC/GO beads/TC** | The author-reported USD 1.95/g estimate uses linear Langmuir (q_{max}=277.78) mg/g despite Hill being the better fit, and a 1 g/L treatment scenario above the tested 250 mg/L initial concentration. Methods state 0.1 M acid/base while Results/Fig. 10 use 1.0 M. The 83.9% NaOH result is desorption efficiency, not cycle capacity retention. No real-water/flow trial. | Section 3.6.4 preserves the cost model/feed assumptions, acid concentration discrepancy and desorption-versus-retention distinction. Section 5.4 labels USD 1.95/g as an author-reported, not independently validated estimate. No real-water/flow validation is claimed. | **Retained; cost and regeneration claims remain qualified.** |

## Conclusion

All five holds remain visible in the final integrated manuscript. No held value was converted into an observed capacity, added to a condition-matched capacity ranking, or used to claim verified low-cost/real-water operation. The manuscript continues to distinguish:
- observed or source-reported uptake from fitted isotherm/kinetic parameters and calculated mass-balance checks;
- synthetic water, controlled ion/HA additions, prefiltered-and-spiked municipal wastewater and a single pharmaceutical-effluent sample;
- adsorption/removal efficiency, capacity retention and desorption efficiency;
- USD/kg adsorbent, USD/g antibiotic removed, USD/m² active-layer cost and kg CO₂-eq footprint.

This is a hold-visibility check, not resolution of the primary-source contradictions. The corresponding original evidence records remain authoritative.

## Production context

The latest formula-corrected Word/PDF outputs are from [GitHub Actions run 41691972025](https://github.com/zaidkhan005/reviewAdsorbants/actions/runs/41691972025), artifact ID `13258235067`. The 94-claim integration totals remain 49 selected references, 53 bibliography entries and 53 resolved manuscript citation keys.
