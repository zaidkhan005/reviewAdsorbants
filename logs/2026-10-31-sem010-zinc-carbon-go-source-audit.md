# SEM-010 Zn–C battery-derived GO source audit — 31 October 2026

## Identity and source
Yasmin et al. (2024), “Efficient removal of ciprofloxacin from aqueous solution using Zn–C battery derived graphene oxide enhanced by hydrogen bonding, electrostatic and π-π interaction,” *Heliyon* 10(12), e33317. DOI: 10.1016/j.heliyon.2024.e33317.
- Primary open full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC11253669/
- Publisher: https://www.sciencedirect.com/science/article/pii/S2405844024093484
- Official supplement: mmc1.docx, 627.6 KB, inspected; DFT/computational content only, no experimental adsorption raw data resolving the discrepancy.

## Material and synthesis burden
Graphite/carbon rods were manually recovered from spent Zn–C batteries, wiped/washed to remove MnO2/NH4Cl/carbon residue, dried at60°C for24h and crushed. Pretreatment: HCl:HNO3 (3:1) at60°C for2h, centrifuge/wash, dry60°C for48h. Improved Hummers oxidation: 1g recovered graphite in H2SO4:H3PO4 (9:1 v/v; total acid volume not specified), add6g KMnO4,50°C for12h; quench with400g ice+3mL30%H2O2; centrifuge3500rpm; wash DI,30%HCl,DI,ethanol; vacuum dry45°C for48h.
Characterization: C/O=1.42; BET61.083426m²/g; mean pore width3.84nm; pore volume.0926cm³/g.
Waste graphite reduces feedstock dependence but route still consumes mixed acids, HCl/HNO3, strong oxidant, H2O2, ethanol, wash water and long drying. Acid volumes, GO yield, recovery, energy and unit costs are absent. The “economical” statement is not a quantified TEA/LCA.

## Batch operating conditions and mass balance
Methods §2.5 specifies40mL CIP solution, concentrations determined by LC-MS/MS, and qe=(C0−Ce)V/m. Abstract/Fig3/§3.6.3 optimum: C0=2.0mg/L, GO=20mg/L, pH5.7,20min,230rpm,30°C.
- CIP feed mass=2mg/L×0.040L=0.080mg.
- GO mass=20mg/L×0.040L=0.80mg=0.00080g.
- Feed ceiling=100mg/g.
- 99% removal implies qe=99mg/g.
But Table4/§3.6.6 reports experimental kinetic qe=78.82mg/g under its matching Fig5 caption conditions (C0=2ppm, GO20mg/L,pH5.7,230rpm,30°C). Under the same40mL basis that qe implies78.82% removal. The difference is20.18 percentage points and is not rounding. PSO fitted qe=79.36mg/g similarly implies79.36% removal.
The authors do not explain whether the 99% optimum and Table4 kinetic qe come from different aliquots or whether one endpoint is erroneous. Preserve both, show the mass balance, and exclude the 99% endpoint from condition-matched ranking pending author clarification/raw data.

## Dosage-unit conflict
Abstract, Fig3 and §3.6.3 specify20mg/L. Conclusion §4 says20g/L (1000× higher). If20g/L were literal at C0=2mg/L, the feed ceiling would be0.1mg/g, incompatible with qe78.82–99mg/g. Preserve both source statements and do not silently correct the unit.

## Isotherm and kinetic model outputs
Table1 reports Langmuir as best among four isotherms. Nonlinear Langmuir q_m=419.62/434.56/441.44mg/g at30/40/50°C (R²=.9800/.9844/.9814); linear Langmuir q_m=400.00/416.67/434.78mg/g (R²=.9966/.9959/.9989). Nonlinear Freundlich R²=.9438/.9443/.9018. These are model asymptotes, not the kinetic qe or observed removal. Fig4 conditions: pH5.7,GO20mg/L,20min,230rpm,30/40/50°C. Methods do not give the precise C0 range for the isotherm series in the extracted text.
Table4: experimental qe78.82mg/g; PSO fitted qe79.36mg/g (linear R²=1.0000; nonlinear R²=.8584); PFO fitted qe3.26mg/g linear (R²=.4363) and77.99mg/g nonlinear (R²=.5500). Elovich a_e=2.28×10^16,b_e=.5185,R²=.7806; intraparticle-diffusion is two-stage with slopes2.2176/.0337, R²=.9352/.0584, intercepts68.53/78.46mg/g. PSO fit superiority does not independently prove chemisorption.
Thermodynamics: ΔH=+16.18kJ/mol; ΔS=+0.144kJ mol−1K−1; ΔG=−27.48/−28.92/−30.37kJ/mol at303/313/323K.

## pH and mechanism
GO pHpzc=2.0; CIP pKa values6.1 and8.7; pH optimum5.7. Authors propose electrostatic attraction between negative GO and cationic CIP above pHpzc, plus π–π and hydrogen bonding; hydrophobic interactions may contribute. FTIR changes and DFT H-bond geometries support hypotheses, but mechanism contributions are not quantitatively apportioned.

## Regeneration — confirmed
§3.6.9 reports methanol regeneration over seven consecutive cycles; after cycle seven the GO reportedly still removes92% CIP (Fig8). This corrects the previous record that reuse data were not located. The 92% figure is removal efficiency, not adsorption-capacity retention; the accessible text does not give cycle-specific qe, full matched test conditions, methanol volume or solvent recovery.

## Practical boundary and disposition
No actual wastewater/river-water test, no quantified leaching, no GO yield, normalized cost, treatment cost/m³, energy inventory, solvent recovery or full TEA/LCA. Retain as a caveated waste-precursor GO case and mechanism/reuse example, not as a validated low-cost winner.
For manuscript use: (1) quote 99% only as author-reported and immediately qualify with Table4 qe78.82mg/g implying78.82% on the same stated basis; (2) keep PSO qe79.36 and fitted Langmuir qm separate; (3) preserve20mg/L vs20g/L; (4) report seven methanol cycles and92% removal after cycle7, not capacity retention; (5) note absence of real-water and cost evidence.

## Repository
Updated in place: remaining-work register, candidate register, evidence-readiness audit (EV-SEM-004), condition-labelled comparison and README. No duplicate evidence ID created. Existing Zotero citation key remains verified.
