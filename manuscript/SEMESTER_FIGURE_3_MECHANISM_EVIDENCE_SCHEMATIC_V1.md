# Figure 3. Candidate interaction pathways for CIP/TC adsorption on graphene-based surfaces

**Figure caption:** Evidence-weighted conceptual schematic of candidate interactions and transport processes in CIP/TC adsorption on GO/rGO and selected graphene-bearing composites. The diagram is not an atomistic structure and does not imply that all pathways act simultaneously or are present in every material.

```mermaid
flowchart LR
    A["Aqueous CIP or TC"] --> B["Solution chemistry"]
    B --> B1["pH and antibiotic<br/>speciation"]
    B --> B2["Competing ions<br/>and ionic strength"]
    B --> B3["Natural organic matter<br/>and co-solutes"]

    C["Graphenic adsorbent surface"] --> C1["sp2 aromatic domains"]
    C --> C2["O-containing groups<br/>(GO)"]
    C --> C3["N-dopant or other<br/>functional groups"]
    C --> C4["Magnetic/metal sites<br/>or composite interfaces"]
    C --> C5["Accessible pores and<br/>interconnected networks"]

    B1 --> D["Adsorption affinity<br/>and transport"]
    B2 --> D
    B3 --> D
    C1 --> D
    C2 --> D
    C3 --> D
    C4 --> D
    C5 --> D

    D --> E["Candidate molecular<br/>interactions"]
    E --> E1["π–π association"]
    E --> E2["Hydrogen bonding"]
    E --> E3["Electrostatic attraction<br/>or repulsion"]
    E --> E4["Metal coordination /<br/>cation-mediated effects"]
    E --> E5["Pore filling and<br/>surface association"]

    D --> F["Mass-transfer steps"]
    F --> F1["External-film transfer"]
    F --> F2["Surface association"]
    F --> F3["Intraparticle / pore<br/>diffusion"]

    E1 --> G["Observed aqueous<br/>concentration change"]
    E2 --> G
    E3 --> G
    E4 --> G
    E5 --> G
    F1 --> G
    F2 --> G
    F3 --> G

    G --> H["Sorbate remains on the<br/>solid until desorbed,<br/>transformed or managed"]
```

**Evidence anchors:** π–π interaction is proposed in graphene/CIP and graphene/antibiotic studies and examined using computational/surrogate approaches `\cite{pengAdsorptionAntibioticsGraphene2016,yasminEfficientRemovalCiprofloxacin2024}`. pH/surface-charge and functional-group evidence is reported across GO/Co–Fe, PGOT@GEL, magnetic GO/cellulose and CMC-functionalized magnetic GO systems `\cite{hossainUltrafastSimultaneousRemoval2024,liThreedimensionalGrapheneOxidebased2025,dangIntegrationMagneticGraphene2025,dipannitaCarboxymethylcelluloseFunctionalizedMagnetic2025}`. Multi-step diffusion and porous-composite behaviour are discussed for SGO mixtures and CNF/GO aerogel `\cite{shahaKineticIsothermThermodynamic2026,yao3DAssemblyBased2017}`. Matrix and competition effects are examined for N-rGO and multi-fluoroquinolone SGO tests `\cite{zhangAdsorptionCharacteristicsNrGO2022,shahaKineticIsothermThermodynamic2026}`.

**Interpretation note:** The arrows represent candidate influences, not measured force directions or universal mechanisms. Spectral changes, pH/ion response, surrogate probes and DFT can support an interaction hypothesis but rarely quantify each pathway's share. A pseudo-second-order fit, Langmuir fit or D–R energy parameter alone does not establish chemisorption, a homogeneous monolayer or one unique molecular interaction. Matrix composition can alter both speciation and apparent adsorption. Adsorption reduces the aqueous concentration but does not by itself demonstrate destruction or mineralization of the antibiotic.
