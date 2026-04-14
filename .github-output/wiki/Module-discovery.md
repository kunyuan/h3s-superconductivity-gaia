# Module: discovery

### high_tc_discovery

**QID:** `github:h3s_superconductivity::high_tc_discovery`
**Type:** claim
**Role:** independent
**Content:** A second superconducting state with Tc ~ 190 K (arXiv v1) / 203 K (Nature) is found by applying pressure P > 150 GPa at temperatures T > 220 K (high-temperature route). This Tc has weak pressure dependence — qualitatively different from the low-T route.
**Prior:** 0.90
**Belief:** 0.93
**prior:** 0.9
**prior_justification:** Resistance drops to sub-copper levels; reproduced in multiple runs. Sample inhomogeneity and pressure gradients add some uncertainty.
**Referenced by:** deduction -> `github:h3s_superconductivity::high_tc_not_predicted`

### high_tc_not_predicted

**QID:** `github:h3s_superconductivity::high_tc_not_predicted`
**Type:** claim
**Role:** derived
**Content:** The high-Tc state (Tc ~ 190 K) is NOT seen or predicted in the Li et al. calculations for H₂S. The requirement of high temperature (T > 220 K) during pressurization suggests a chemical transformation (decomposition of H₂S) is involved in reaching this state.
**Belief:** 0.98
**Derived from:** deduction
**Premises:** `github:h3s_superconductivity::high_tc_discovery`
**Derived from:** support
**Premises:** `github:h3s_superconductivity::accompanying_30k_step`
**gaia:** {'provenance': {'referenced_claims': ['accompanying_30k_step', 'high_tc_discovery']}}
**Referenced by:** deduction -> `github:h3s_superconductivity::h3s_formation_hypothesis`

### accompanying_30k_step

**QID:** `github:h3s_superconductivity::accompanying_30k_step`
**Type:** claim
**Role:** independent
**Content:** The 190 K superconducting step is frequently accompanied by a second step at Tc ~ 30 K, which disappears with time (>1 day) or further pressure application while the 190 K step sharpens. R(T) oscillations with a period of 25–30 K are observed in multiple runs.
**Prior:** 0.85
**Belief:** 0.85
**prior:** 0.85
**prior_justification:** Observed in multiple runs; transient nature makes systematic study difficult.
**Referenced by:** support -> `github:h3s_superconductivity::high_tc_not_predicted`

### resistivity_proof

**QID:** `github:h3s_superconductivity::resistivity_proof`
**Type:** claim
**Role:** independent
**Content:** The minimum resistance in the high-Tc state corresponds to resistivity ρ ≤ 10⁻¹¹ Ω·m — about two orders of magnitude less than pure copper at the same temperature. At 144 K specifically: ρ = 1.7×10⁻¹⁰ Ω·m, which is 50 times lower than copper (ρ_Cu = 70×10⁻¹⁰ Ω·m at 150 K).
**Prior:** 0.95
**Belief:** 0.95
**prior:** 0.95
**prior_justification:** ρ = 1.7×10⁻¹⁰ Ω·m, 50× below copper; measurement well-calibrated.
**Referenced by:** deduction -> `github:h3s_superconductivity::superconductivity_confirmed`

### magnetic_field_proof

**QID:** `github:h3s_superconductivity::magnetic_field_proof`
**Type:** claim
**Role:** independent
**Content:** Tc shifts to lower temperatures with magnetic field up to 7 Tesla for both superconducting states. Extrapolation using Hc(T) = Hc0·(1 − (T/Tc)²) gives estimated upper critical fields: Hc2 ~ 25 T for the Tc ~ 60 K state and Hc2 ~ 70 T for the Tc ~ 185 K state. The high Hc2 is characteristic of a type-II superconductor.
**Prior:** 0.90
**Belief:** 0.90
**prior:** 0.9
**prior_justification:** Clear Tc shift with field up to 7 T; Hc2 extrapolation adds uncertainty.
**Referenced by:** deduction -> `github:h3s_superconductivity::superconductivity_confirmed`

### isotope_effect

**QID:** `github:h3s_superconductivity::isotope_effect`
**Type:** claim
**Role:** independent
**Content:** Deuterium substitution (D₂S) shows a strong isotope effect: H₂S Tc ~ 60 K → D₂S Tc ~ 30 K, and H₂S Tc ~ 185 K → D₂S Tc ~ 90 K. The isotope exponent α ≈ 0.5, matching the BCS prediction Tc ∝ M^(−α) with α = 0.5 for the phonon mechanism. This confirms phonon-mediated (conventional BCS) superconductivity.
**Prior:** 0.92
**Belief:** 0.92
**prior:** 0.92
**prior_justification:** α ≈ 0.5 matches BCS; D₂S purity 97% introduces slight uncertainty.
**Referenced by:** deduction -> `github:h3s_superconductivity::superconductivity_confirmed`

### superconductivity_confirmed

**QID:** `github:h3s_superconductivity::superconductivity_confirmed`
**Type:** claim
**Role:** derived
**Content:** The observed resistance drops represent genuine superconducting transitions, confirmed by three independent lines of evidence: (1) resistivity far below copper, (2) magnetic field suppression of Tc, and (3) a strong isotope effect consistent with BCS theory. The high-Tc state at ~190–203 K is a conventional (phonon-mediated) superconductor.
**Belief:** 0.89
**Derived from:** deduction
**Premises:** `github:h3s_superconductivity::resistivity_proof`, `github:h3s_superconductivity::magnetic_field_proof`, `github:h3s_superconductivity::isotope_effect`
**gaia:** {'provenance': {'referenced_claims': ['isotope_effect', 'magnetic_field_proof', 'resistivity_proof']}}
**Referenced by:** deduction -> `github:h3s_superconductivity::conventional_sc_above_200k`
