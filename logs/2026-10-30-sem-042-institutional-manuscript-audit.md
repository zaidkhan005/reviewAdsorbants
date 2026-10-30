# SEM-042 institutional-manuscript re-audit — 2026-10-30

## Candidate and decision

**SEM-042:** González et al. (2018), “Continuous flow adsorption of ciprofloxacin by using a nanostructured chitin/graphene oxide hybrid material,” *Carbohydrate Polymers* 188, 213–220. DOI: [10.1016/j.carbpol.2018.02.021](https://doi.org/10.1016/j.carbpol.2018.02.021).

**Decision:** Retain provisionally for the batch CIP adsorption evidence and chitin/GO composite design. Keep all quantitative continuous-flow/packed-bed results quarantined. Do not alter the manuscript's reported mass by assumption.

## Primary-source route checked

- Authors' institutional repository (CONICET), accepted-manuscript PDF: https://ri.conicet.gov.ar/bitstream/11336/87000/11/CONICET_Digital_Nro.b2e52671-05bf-40a5-9fe0-525a5cfb6f21_J.pdf
- Official publisher record/preview: https://www.sciencedirect.com/science/article/pii/S0144861718301590
- The accepted manuscript's text was inspected for Methods §§2.4.1–2.4.2, the column-model equations, Results §3.3 and Tables 1–2. The publisher preview confirms the article identity and Sips-model result but does not expose a corrected packed mass. No erratum/correction was found on the publisher page checked in this audit.
- The PDF text could be inspected, but a rendered-page screenshot could not be retrieved in this session. Therefore this is a text-level primary-source audit, not a visual verification of the PDF page layout.

## Column mass-balance / geometry check

The accepted manuscript's Methods §2.4.2 explicitly states **100 g** of Chi:nGO (3:1) packed in a glass column with:

- internal diameter: **1.0 cm**;
- overall column height: **10 cm**;
- reported adsorbent-bed height: **1.5 cm**.

The bed volume implied by the dimensions is:

\[
V_{bed}=\pi(0.5\,\mathrm{cm})^2(1.5\,\mathrm{cm})=1.178\,\mathrm{cm^3}
\]

The implied packed density is:

\[
\rho_{implied}=\frac{100\,\mathrm{g}}{1.178\,\mathrm{cm^3}}\approx84.9\,\mathrm{g\,cm^{-3}}
\]

This is physically incompatible with a chitin/graphene-oxide hybrid packed bed. The overall 10 cm column height does not change the 1.5 cm bed-volume calculation. A possible unit/transcription error is plausible, but **the intended value is not established by the sources checked**. In particular, do not silently substitute 100 mg for 100 g.

## Quantitative-use decisions

### Batch evidence retained with metric labels

- Batch protocol: 10 mg adsorbent in 2 mL CIP solution; pH 6.30; 25 °C; 120 rpm; initial concentration range 4–850 mg/L.
- The article reports the Sips equation as the best overall batch isotherm fit.
- Langmuir-fitted comparison values: nGO **q_m = 282 ± 11 mg/g**; Chi:nGO (3:1) **q_m = 73 ± 3 mg/g**. These are model-derived parameters, not observed q_e values. Keep their model identity and test context attached.

### Column / continuous-flow evidence held

Do not use the following as validated performance, capacity, service-life or application-comparison evidence until the packed mass and method are independently corrected:

- Thomas-model q_0 results across flow rate, pH, sodium concentration and water hardness;
- Yoon–Nelson breakthrough-time (τ) results;
- real-water column results for Buenos Aires tap water and Chascomús/Macachín well water.

The manuscript describes the real-water samples as **CIP-spiked** samples. Do not describe them as untreated CIP-contaminated groundwater or field validation. The existence of a flow-through experiment may be mentioned only with an explicit note that its packing mass is internally impossible and its numerical column results are withheld.

## Cost and mechanism guardrails

The paper's “low-cost” characterization is not a verified comparable process-cost result. The extraction identifies no auditable cost per gram of sorbent, treated volume or CIP mass removed, and no complete inventory for Hummers reagents, CaCl2/methanol use, washing, heating, sonication energy, eluent or waste treatment. Do not claim low-cost performance from the material identity alone.

The paper's pH/electrostatic, hydrogen-bonding and π–π explanations remain author-proposed interpretations; do not present them as independently quantified interaction contributions.

## Repository actions

- Updated `data/semester-paper-candidate-register.csv` with the institutional source provenance and full column geometry.
- Updated `data/semester-study-inclusion-shortlist.csv` with the source audit and explicit column-metric hold.
- Updated `data/semester-evidence-readiness-audit.csv` to clarify the accepted-manuscript source and unavailable rendered-page verification.
- Reused existing evidence record **EV-SEM-021**; no duplicate evidence ID was created.
- Existing batch-vs-column endpoint separation is preserved.

## What would resolve the hold

A corrected version of record, publisher erratum, author correction, or written author confirmation explicitly establishing the packed mass and matching column-table calculations. Until then, preserve the source's 100 g statement, label the contradiction, and keep column metrics out of quantitative synthesis.
