# Figure 4. Evidence framework for assessing practical low-cost potential

**Figure caption:** Four linked evidence dimensions for assessing whether a graphene-based CIP/TC adsorbent has practical low-cost potential. The framework is qualitative and evidence-led; no composite receives a score or rank unless comparable data support it.

```mermaid
flowchart TB
    A["Candidate graphene-based adsorbent<br/>and target antibiotic"] --> B["1. Adsorption performance"]
    A --> C["2. Preparation and material burden"]
    A --> D["3. Recovery and regeneration"]
    A --> E["4. Water-matrix and operating validation"]

    B --> B1["Observed qe / qt<br/>and condition labels"]
    B --> B2["Fitted qmax / kinetic qe<br/>kept separate"]
    B --> B3["Removal % and column<br/>results kept separate"]

    C --> C1["Precursor and product yield"]
    C --> C2["Reagents, solvents,<br/>washing and neutralization"]
    C --> C3["Energy, drying and<br/>scale-up operations"]

    D --> D1["Magnetic / physical<br/>separation efficiency"]
    D --> D2["Cycle retention and<br/>adsorbent loss"]
    D --> D3["Regenerant recovery,<br/>eluate and spent-media handling"]

    E --> E1["Real wastewater vs<br/>synthetic or spiked water"]
    E --> E2["Competing ions, NOM<br/>and co-contaminants"]
    E --> E3["Flow, breakthrough,<br/>leaching and stability"]

    B1 --> F["Evidence integration"]
    B2 --> F
    B3 --> F
    C1 --> F
    C2 --> F
    C3 --> F
    D1 --> F
    D2 --> F
    D3 --> F
    E1 --> F
    E2 --> F
    E3 --> F

    F --> G["Comparable cost boundary<br/>and functional unit"]
    G --> G1["Cost per m³ treated"]
    G --> G2["Cost per mass CIP/TC removed"]
    G --> H["Qualified conclusion on low-cost potential:<br/>supported, not supported,<br/>or insufficient evidence"]
```

**Evidence anchors:** Endpoint conflicts and fitted/observed separation are visible in the battery-derived GO/CIP, sulfonated-GO/CIP and GO/alginate-bead studies `\cite{yasminEfficientRemovalCiprofloxacin2024,shahaExploringAdsorptionEfficiency2025,hossainRemovalCiprofloxacinAqueous2026}`. Magnetic recovery and cycle decline are reported in magnetic GO/cellulose and GO/Co–Fe systems `\cite{dangIntegrationMagneticGraphene2025,dipannitaCarboxymethylcelluloseFunctionalizedMagnetic2025,hossainUltrafastSimultaneousRemoval2024}`. Matrix, trace-mixture and flow-through evidence varies across N-rGO, graphene/GAC benchmarking and alginate/GO PRB work `\cite{zhangAdsorptionCharacteristicsNrGO2022,zhuCiprofloxacinAdsorptionGraphene2015a,zhaoSodiumAlginateGraphene2018}`.

**Interpretation note:** The framework does not convert unreported values into estimates. A material can have strong laboratory adsorption data but weak cost evidence; magnetic recovery can reduce separation difficulty but add reagents and fabrication steps; high percentage removal at high dose does not alone establish low cost. A cost claim requires a stated system boundary, a defined functional unit, product yield, input quantities, energy, replacement/regeneration, and residual-stream handling.
