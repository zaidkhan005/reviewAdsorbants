# Figure 1. Scope and material taxonomy

**Figure caption:** Scope and eligibility boundaries for the evidence synthesis of ciprofloxacin (CIP) and tetracycline (TC) adsorption by selected graphene-based adsorbents and graphene-bearing composites.

```mermaid
flowchart TB
    A["Review question<br/>Aqueous adsorption of CIP and TC"] --> B["Family A<br/>Graphene-based adsorbents"]
    A --> C["Family B<br/>Selected graphene-bearing composites"]

    B --> B1["Graphene oxide (GO)"]
    B --> B2["Reduced graphene oxide (rGO)"]
    B --> B3["Surface-functionalized GO/rGO"]

    C --> C1["Magnetic GO/rGO composites"]
    C --> C2["Chemically functionalized magnetic graphene"]
    C --> C3["Graphene–polymer/cellulose<br/>or immobilized graphene"]
    C --> C4["Selected graphene–metal-oxide<br/>composites, where adsorption<br/>is separable from catalysis"]

    A --> D["Eligibility gate"]
    D --> D1["Original research study"]
    D --> D2["Aqueous CIP- or TC-specific result"]
    D --> D3["Adsorption contribution<br/>separable from degradation"]
    D --> D4["Conditions sufficient to<br/>interpret the result"]

    D1 --> E["Core evidence synthesis"]
    D2 --> E
    D3 --> E
    D4 --> E

    E --> F["Compare condition-labelled<br/>observed and modelled endpoints"]
    F --> F1["Observed qₑ / qₜ"]
    F --> F2["Fitted qmax / qm<br/>and kinetic-model qe"]
    F --> F3["Removal percentage"]
    F --> F4["Column / breakthrough data"]

    X["Outside the core material scope"] --> X1["Standalone CNT, activated carbon<br/>or biochar"]
    X --> X2["Standalone clay, chitosan,<br/>alginate or other polymer"]
    X --> X3["Standalone MOF or mineral sorbent"]
    X --> X4["Other non-graphene materials"]

    Y["Target-specificity rule"] --> Y1["CIP is not pooled with<br/>norfloxacin or ofloxacin"]
    Y --> Y2["TC is not pooled with doxycycline,<br/>oxytetracycline or chlortetracycline"]
```

**Source and design note:** Author-generated taxonomy based on the approved scope proposal (`docs/SEMESTER_PAPER_SCOPE_PROPOSAL.md`). The eligibility gate is conjunctive: a candidate must satisfy the original-study, material, aqueous target-specificity, adsorption-separation and interpretability requirements. Reviews may support background or citation discovery but do not provide primary-study values in the core comparison.

**Interpretation note:** Family B does not automatically include every novel hybrid. Each graphene-bearing composite is assessed individually; a standalone MOF, mineral or polymer remains outside the core. The figure is a scope map, not a claim that every candidate in the screening register is finally included.
