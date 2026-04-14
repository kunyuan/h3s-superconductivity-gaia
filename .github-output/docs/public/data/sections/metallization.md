# Module: metallization

### h2s_metallization

**QID:** `github:h3s_superconductivity::h2s_metallization`
**Type:** claim
**Role:** independent
**Content:** H₂S starts to conduct at P ~ 50 GPa (semiconductor with photoconductivity). At 90–100 GPa, the temperature dependence becomes metallic and photoconductivity disappears. H₂S is a poor metal: resistivity ρ ~ 3×10⁻⁵ Ω·m at 110 GPa, decreasing to ρ ~ 3×10⁻⁷ Ω·m at ~200 GPa.
**Prior:** 0.95
**Belief:** 0.94
**figure:** artifacts/images/ext-fig2-low-tc-resistance.png
**caption:** Extended Data Fig. 2 | Temperature dependence of resistance (superconducting steps). Corresponding Tc values are shown by blue points in Fig. 2.
**prior:** 0.95
**prior_justification:** Direct resistance and photoconductivity measurements in DAC.
**Referenced by:** deduction -> `github:h3s_superconductivity::low_tc_onset`

### low_tc_onset

**QID:** `github:h3s_superconductivity::low_tc_onset`
**Type:** claim
**Role:** derived
**Content:** When the metallic H₂S phase is cooled to 4 K at ~100 GPa, the resistance drops abruptly by 3–4 orders of magnitude at Tc ~ 23 K, indicating the onset of superconductivity.
**Belief:** 0.97
**Derived from:** deduction
**Premises:** `github:h3s_superconductivity::h2s_metallization`
**figure:** artifacts/images/fig1-resistance-vs-temperature.png
**caption:** Fig. 1a | Temperature dependence of resistance of sulfur hydride at growing pressures. Bottom: resistance plots near zero showing the superconducting transition.
**gaia:** {'provenance': {'referenced_claims': ['h2s_metallization']}}
**Referenced by:** deduction -> `github:h3s_superconductivity::low_tc_pressure_dependence`

### low_tc_pressure_dependence

**QID:** `github:h3s_superconductivity::low_tc_pressure_dependence`
**Type:** claim
**Role:** derived
**Content:** In the low-temperature route (pressure applied at 100–150 K), Tc increases with pressure from ~23 K at 100 GPa, with sharp growth approaching 200 GPa, reaching up to ~150 K at ~200 GPa.
**Belief:** 0.98
**Derived from:** deduction
**Premises:** `github:h3s_superconductivity::low_tc_onset`
**figure:** artifacts/images/fig2-pressure-tc-phase-diagram.png
**caption:** Fig. 2a | Pressure dependence of Tc for the low-temperature route. Black points from Fig. 1a, blue from other runs, red for D₂S, grey stars from Li et al. calculations.
**gaia:** {'provenance': {'referenced_claims': ['diamond_anvil_cell', 'low_tc_onset']}}
**Referenced by:** support -> `github:h3s_superconductivity::low_tc_agrees_with_theory`

### low_tc_agrees_with_theory

**QID:** `github:h3s_superconductivity::low_tc_agrees_with_theory`
**Type:** claim
**Role:** derived
**Content:** The low-temperature route Tc values (up to ~150 K at ~200 GPa) are in reasonable agreement with Li et al.'s prediction of Tc ~ 80 K for H₂S. The experimental values exceed the prediction, and the pressure dependence differs (no predicted drop of Tc at 160 GPa), but the overall scale and trend are consistent with H₂S-phase superconductivity.
**Belief:** 0.71
**Derived from:** support
**Premises:** `github:h3s_superconductivity::low_tc_pressure_dependence`, `github:h3s_superconductivity::h2s_theory_prediction`
**gaia:** {'provenance': {'referenced_claims': ['h2s_theory_prediction', 'low_tc_pressure_dependence']}}
