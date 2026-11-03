# Figure 1. Scope and adsorbents considered

**Figure caption:** Adsorbents considered and eligibility boundaries for the evidence synthesis of ciprofloxacin (CIP) and tetracycline (TC) adsorption.

```mermaid
flowchart TB
    A["Review question<br/>Aqueous adsorption of CIP and TC"] --> B["Adsorbents considered"]

    B --> B1["Graphene oxide (GO)"]
    B --> B2["Reduced graphene oxide (rGO)"]
    B --> B3["Surface-functionalized GO/rGO"]
    B --> B4["Magnetic GO/rGO composites"]
    B --> B5["Chemically functionalized magnetic graphene"]
    B --> B6["Graphene–polymer/cellulose<br/>and immobilized graphene composites"]
    B --> B7["Selected graphene–metal-oxide composites<br/>where adsorption is separable from catalysis"]

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
    F --> F1["Observed equilibrium and<br/>time-specific uptake"]
    F --> F2["Fitted maximum capacities<br/>and kinetic-model uptake"]
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

**Interpretation note:** Each graphene-bearing composite is considered individually. A standalone MOF, mineral or polymer remains outside the core scope unless it contains an eligible graphene-based adsorbent. The figure is a scope map, not a claim that every screened study is included.
