# Material taxonomy (working version)

This taxonomy organizes paper screening. The material class and the processing stage are separate fields; do not infer a stage solely from the material’s natural origin or a Zotero tag.

## Section 2.1 — Raw biomass and natural waste

- Raw lignocellulosic biomass: sawdust, timber waste, rice husk, barley husk, pine bark, wood chippings, agricultural residues.
- Other untreated bio-derived materials: macroalgae and selected food/agro-industrial by-products.
- Record ordinary preparation (washing, drying, grinding, sieving) separately from chemical treatment or carbonization.

## Section 2.2 — Natural clays and biopolymers

### A. Natural clay minerals
Bentonite/montmorillonite, kaolinite, sepiolite, vermiculite, halloysite and other natural mineral sorbents.

### B. Unmodified biopolymers
Chitosan, cellulose, alginate, starch, lignin and relevant bio-derived polymers with no additional adsorption-specific modification. Record preparation history carefully.

### C. Modified biopolymers
Crosslinked chitosan, chemically functionalized cellulose, grafted or otherwise deliberately modified polymer adsorbents.

### D. Biopolymer-based composites
Clay–chitosan composites, polymer–carbon composites, and other hybrid architectures. Record all principal components and classify according to the intended comparison; cross-tag component materials.

The original Day 4 heading is “Natural clays & biopolymers”; it is not restricted to unmodified materials.

## Section 2.3 — Biochar and modified biochar

### A. Pristine biochar
Biomass-derived char produced by pyrolysis or another stated thermochemical route, without deliberate post-production modification.

### B. Physically activated biochar
Biochar physically treated (for example, by steam or CO₂ activation). Record exact processing conditions.

### C. Chemically modified biochar
Acid/base treatment, oxidation, chemical functionalization, or salt-based modification.

### D. Composite or loaded biochar
Magnetic/iron-loaded and other biochar hybrids. Record the component, loading/synthesis route, and whether the process combines adsorption with degradation.

**Boundary:** advanced atomic-site doping may be discussed in Section 2.4 when the novelty is deliberate atomic/electronic engineering; cross-tag the biochar origin. The Stage 3/4 boundary remains a working decision until the full outline and tags are reconciled.

## Section 2.4 — Engineered and nano-carbon adsorbents

### A. Activated carbon
Powdered activated carbon (PAC), granular activated carbon (GAC), commercial activated carbon, and biomass-derived activated carbon. Activated carbon is not automatically a nanomaterial; it is included as an engineered carbon benchmark.

### B. Carbon nanotubes (CNTs)
Single- or multi-walled CNTs, pristine or functionalized.

### C. Graphene-based materials
Graphene oxide (GO), reduced graphene oxide (rGO), and functionalized graphene-derived adsorbents.

### D. Atomically engineered and advanced nano-carbons
Heteroatom-doped carbon (N/S/P and other dopants), deliberately atomically engineered carbon, and relevant advanced carbon dots/nanofibres. Include only when the study is directly relevant to antibiotic adsorption; separately label catalytic degradation if present.

## Classification rules

- Record at least two fields: `material_category` and `processing_stage`.
- Record the original feedstock, preparation route, modification chemicals, temperature, energy-intensive steps and activation separately.
- A hybrid can carry multiple material tags, but each paper’s main evidence must be tied to the exact adsorbent tested.
- If the paper’s main removal pathway is catalytic oxidation, photodegradation or membrane rejection, do not report the removal percentage as adsorption performance.
- Current taxonomy conflict to resolve: the outline groups natural clays and biopolymers in Stage 2, but the Zotero vocabulary currently uses `STAGE-2-MODIFIED`. Until resolved, classify by explicit material and processing route rather than stage tag alone.