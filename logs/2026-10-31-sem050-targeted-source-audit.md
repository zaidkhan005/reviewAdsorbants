# SEM-050 targeted source audit — 31 October 2026

## Study identity and source
Lemaoui et al. (2026), “Surface assembled graphene oxide–deep eutectic solvent based nanocomposite for multimodal adsorption-driven drug sequestration.” Advanced Composites and Hybrid Materials 9, article 260. DOI: 10.1007/s42114-026-01808-5.

Publisher full text: https://link.springer.com/article/10.1007/s42114-026-01808-5

The open publisher page confirms the article and links three supplementary files (ESM1 Python, ESM2 DOCX, ESM3 XLSX). Main text and previously inspected ESM2/ESM3 are used for this targeted QA. This is an empirical adsorption study, not a catalytic degradation paper.

## Evidence retained
- Lead adsorbent: GO–TOPO:LevA, with a 1:1 molar TOPO:levulinic-acid DES phase.
- The main-text benchmark reports TET removal 90.8 ± 2.5% and qe 22.7 ± 0.6 mg/g for GO–TOPO:LevA, compared with GO 56.4% and 14.1 mg/g.
- Batch qe 22.7 mg/g is not admissible for quantitative ranking yet. The SI baseline feed case (10 mg/L in 10 mL with 10 mg adsorbent) has a maximum available-feed ceiling of 10 mg/g. The precise Figure 1 run-specific C0, volume and adsorbent mass needed to reconcile the reported qe were not pinned in the accessible supporting detail. Preserve the source value but quarantine it; do not silently alter it.
- Fitted Langmuir qmax is 323.6 mg/g for GO–TOPO:LevA and 134.5 mg/g for GO. These are fitted model parameters, not observed batch uptake. The main text notes that the Freundlich model has lower RMSE for GO–TOPO:LevA than Langmuir, reinforcing that qmax should not be presented as the measured capacity.
- Real-matrix membrane testing used municipal wastewater collected in Abu Dhabi and prefiltered through a 0.45 μm PES membrane. The matrix was deliberately spiked: 5 mg/L TET in the single-solute test; a separate four-drug cocktail included SMX, TRI, TET and ERY at equal initial concentrations.
- Single-solute spiked MWW membrane test: TET qe 17.3 ± 0.5 mg/g. Separate low-concentration single-solute tests at 500 and 1000 μg/L reported 97.8% and 95.4% TET removal, with qe 2.45 and 4.77 mg/g.
- Four-drug co-spiked MWW: TET removal 85.4 ± 1.8%, qe 16.9 mg/g; corresponding capacities were 13.3 (SMX), 15.8 (TRI), and 18.7 mg/g (ERY). Keep these results separate from the single-solute case.
- Six 0.1 M NaOH regeneration cycles: GO–TOPO:LevA performance 65.4 ± 0.9% after cycle six vs 30.4 ± 1.2% for pristine GO; first-cycle regeneration 99.1 ± 1.3%.
- TOC-based leaching tests: static 24 h 1.02 ± 0.06%; dynamic DI-water passage 0.64 ± 0.03% initially and 0.49 ± 0.02% after cycle six. These are specific test results, not proof of zero long-term release in field operation.

## Cost and environmental boundary
- Estimated active-layer material cost: USD 2.5–6.8/m², derived from approximate bulk prices for GO, LevA and TOPO, composition (46.8 wt% GO / 53.2 wt% DES) and loading (~124 g/m²).
- Estimated active-layer cradle-to-gate footprint: 14–59 kg CO2-eq/m².
- Normalized footprint 0.02–0.08 kg CO2-eq/m³ assumes two years of operation at 50 LMH (~800 m³/m²); NaOH regeneration adds an estimated 1–3 g CO2-eq/m³.
- These are first-order estimates, not measured financial operating costs, not a complete module cost, and not a full system LCA/TEA. The comparison does not fully price support, fabrication, pumping/pressure drop, maintenance, replacement, spent-membrane handling or all end-of-life burdens. Do not call this “USD per m³ treated.”

## Interpretation for the semester paper
This is a high-value process-boundary case because it connects a GO composite to membrane operation, spiked real municipal wastewater, multi-solute competition, regeneration, leaching and an explicit active-layer cost/carbon estimate. It is not evidence of treatment of native unspiked wastewater, and the powder-batch qe of 22.7 mg/g should not enter rankings until the feed denominator is reconciled. Emphasize measured membrane/matrix evidence and the limited scope of the cost estimate.

## Citation workflow
The latest uploaded 173-entry Zotero export did not contain an exact DOI or normalized-title match. No Better BibTeX key has been invented. Add/verify the Zotero metadata only if the study is selected for citation, then use the actual generated key.

## Repository updates
Updated:
- data/semester-remaining-work-register.csv
- data/semester-paper-candidate-register.csv
- data/semester-evidence-readiness-audit.csv

Journal quartile is deliberately not assessed, per the user's semester-paper instruction.
