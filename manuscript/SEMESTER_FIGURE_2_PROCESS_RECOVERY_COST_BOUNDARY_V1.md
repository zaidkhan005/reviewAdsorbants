# Figure 2. Preparation-to-recovery process boundary for graphene-based CIP/TC adsorbents

**Figure caption:** Conceptual process boundary for evaluating the practical and low-cost potential of selected graphene-based adsorbents. The flow consolidates alternative preparation, treatment, recovery and regeneration operations reported across the reviewed studies; it is not a single standardized synthesis or treatment protocol.

```mermaid
flowchart TB
    A["Graphenic feedstock and precursor"] --> B["GO formation or procurement"]
    B --> B1["Commercial GO / rGO"]
    B --> B2["Graphite oxidation<br/>(Hummers or modified-Hummers routes)"]
    B2 --> C["Washing, neutralization,<br/>separation and drying"]

    B1 --> D["Surface modification /<br/>composite assembly"]
    C --> D
    D --> D1["Reduction or functionalization<br/>(e.g. sulfonation, N-doping)"]
    D --> D2["Magnetic phase addition<br/>(e.g. Fe3O4)"]
    D --> D3["Polymer/cellulose immobilization<br/>(fibers, beads, aerogels, hydrogels)"]
    D --> D4["Selected metal-oxide or<br/>coordination-framework composites"]

    D1 --> E["Characterized adsorbent"]
    D2 --> E
    D3 --> E
    D4 --> E

    E --> F["Aqueous treatment feed<br/>CIP and/or TC"]
    F --> G["Adsorption operation"]
    G --> H["Loaded adsorbent + treated water"]
    H --> I["Solid–liquid separation"]
    I --> I1["External magnet<br/>(magnetic composites)"]
    I --> I2["Filtration / centrifugation<br/>(dispersed powders)"]
    I --> I3["Physical recovery of<br/>fibers, beads or monoliths"]

    I1 --> J["Regeneration / desorption"]
    I2 --> J
    I3 --> J
    J --> J1["Reuse in another cycle"]
    J --> J2["Spent adsorbent /<br/>unrecoverable material"]
    J --> J3["Concentrated regenerant<br/>requiring recovery or treatment"]

    K["Whole-process cost boundary"] --- B
    K --- C
    K --- D
    K --- G
    K --- I
    K --- J
    K --> L["Report: yield, reagents,<br/>water, energy, solvent use,<br/>adsorbent loss and cycle decline"]
    L --> M["Normalize to a functional unit:<br/>cost per m³ treated and/or<br/>cost per mass CIP/TC removed"]
```

**Evidence anchors:** Graphite-derived GO and battery-carbon routes are reported by Yasmin et al. (2024) `\cite{yasminEfficientRemovalCiprofloxacin2024}`; sulfonated GO and DMF/HCl regeneration by Shaha et al. (2025) `\cite{shahaExploringAdsorptionEfficiency2025}`; magnetic GO/cellulose and magnetic recovery by Dang et al. (2025) and Dipannita et al. (2025) `\cite{dangIntegrationMagneticGraphene2025,dipannitaCarboxymethylcelluloseFunctionalizedMagnetic2025}`; GO/cellulose aerogel and alkaline regeneration by Yao et al. (2017) `\cite{yao3DAssemblyBased2017}`; hydrogel functionalization and methanol regeneration by Li et al. (2025) `\cite{liThreedimensionalGrapheneOxidebased2025}`; GO/polymer/alginate bead synthesis and its cost-basis discrepancy by Hossain et al. (2026) `\cite{hossainRemovalCiprofloxacinAqueous2026}`; and magnetic GO/Co–Fe recovery by Hossain et al. (2024) `\cite{hossainUltrafastSimultaneousRemoval2024}`.

**Interpretation note:** A waste-derived feedstock does not remove the costs of purification, oxidation, washing, neutralization or drying. Magnetic separation and immobilization can improve handling but may add metal salts, crosslinkers, solvents and fabrication steps. Regeneration can transfer antibiotic mass into a concentrated liquid stream; recovery of the solid alone does not demonstrate destruction or safe disposal of the antibiotic. The functional unit and all input/output balances must be stated before any system can be described as low-cost.
