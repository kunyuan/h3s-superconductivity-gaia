# h3s-superconductivity-gaia

Gaia knowledge package: Conventional superconductivity at 203 K in sulfur hydride (Drozdov et al., Nature 525, 73, 2015; arXiv:1412.0460)

<!-- badges:start -->
<!-- badges:end -->

## Overview

> [!TIP]
> **Reasoning graph information gain: `1.0 bits`**
>
> Total mutual information between leaf premises and exported conclusions — measures how much the reasoning structure reduces uncertainty about the results.

```mermaid
---
config:
  flowchart:
    rankSpacing: 80
    nodeSpacing: 30
---
graph TB
    ashcroft_hydrogen["Ashcroft Hydrogen Hypothesis\n(0.95 → 0.95)"]:::premise
    h2s_theory_prediction["Li et al. H₂S Tc Prediction\n(0.80 → 0.72)"]:::premise
    sulfur_sc["Sulfur Superconductivity\n(0.95 → 0.91)"]:::premise
    high_tc_discovery["High-Tc Discovery at 190–203 K\n(0.90 → 0.93)"]:::premise
    accompanying_30k_step["Accompanying 30 K Step and Oscillations\n(0.85 → 0.85)"]:::premise
    resistivity_proof["Resistivity Far Below Copper\n(0.95 → 0.95)"]:::premise
    magnetic_field_proof["Magnetic Field Suppression of Tc\n(0.90 → 0.90)"]:::premise
    isotope_effect["Strong Isotope Effect in D₂S\n(0.92 → 0.92)"]:::premise
    superconductivity_confirmed["★ Superconductivity Confirmed by Three Proofs\n(0.50 → 0.89)"]:::exported
    no_h2_vibron["No H₂ Vibron in Raman\n(0.90 → 0.90)"]:::premise
    duan_prediction["Duan et al. H₃S Prediction\n(0.75 → 0.75)"]:::premise
    raman_phase_transition["Raman Phase Transition at 180 GPa\n(0.85 → 0.85)"]:::premise
    high_tc_is_h3s["★ High-Tc Phase Identified as H₃S\n(0.50 → 0.77)"]:::exported
    conventional_sc_above_200k["★ Conventional SC Above 200 K\n(0.50 → 0.84)"]:::exported
    hydrogen_materials_prospect["★ Prospect for Hydrogen-Based Superconductors\n(0.50 → 0.90)"]:::exported
    strat_0(["infer\n0.21 bits"]):::weak
    accompanying_30k_step --> strat_0
    duan_prediction --> strat_0
    h2s_theory_prediction --> strat_0
    high_tc_discovery --> strat_0
    no_h2_vibron --> strat_0
    raman_phase_transition --> strat_0
    sulfur_sc --> strat_0
    strat_0 --> high_tc_is_h3s
    strat_1(["infer\n0.29 bits"]):::weak
    ashcroft_hydrogen --> strat_1
    conventional_sc_above_200k --> strat_1
    strat_1 --> hydrogen_materials_prospect
    strat_2(["infer\n0.20 bits"]):::weak
    high_tc_is_h3s --> strat_2
    superconductivity_confirmed --> strat_2
    strat_2 --> conventional_sc_above_200k
    strat_3(["infer\n0.26 bits"]):::weak
    isotope_effect --> strat_3
    magnetic_field_proof --> strat_3
    resistivity_proof --> strat_3
    strat_3 --> superconductivity_confirmed

    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef exported fill:#d4edda,stroke:#28a745,stroke-width:2px,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```

## Conclusions

| Label | Content | Prior | Belief |
|-------|---------|-------|--------|
| conventional_sc_above_200k | Conventional (phonon-mediated, BCS-type) superconductivity has been demonstra... | 0.50 | 0.84 |
| high_tc_is_h3s | The high-Tc superconductivity at ~190–203 K is attributed to H₃S (trihydrogen... | 0.50 | 0.77 |
| hydrogen_materials_prospect | Since H₂S has only a moderate hydrogen content, high-Tc superconductivity can... | 0.50 | 0.90 |
| superconductivity_confirmed | The observed resistance drops represent genuine superconducting transitions, ... | 0.50 | 0.89 |

<!-- content:start -->
<!-- content:end -->
