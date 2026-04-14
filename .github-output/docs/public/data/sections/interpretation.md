# Module: interpretation

### no_h2_vibron

**QID:** `github:h3s_superconductivity::no_h2_vibron`
**Type:** claim
**Role:** independent
**Content:** The strong characteristic vibron of molecular H₂ was never observed in Raman spectra despite using a sensitive spectrometer and ultralow luminescence synthetic diamond anvils. This rules out simple decomposition H₂S → H₂ + S.
**Prior:** 0.90
**Belief:** 0.90
**figure:** artifacts/images/ext-fig1-raman-spectra.png
**caption:** Supplementary Fig. 1 | Raman spectra of sulfur hydride at different pressures. (a) H₂S spectra at increasing pressure. (b) D₂S Raman spectra. No H₂ vibron peak is observed.
**prior:** 0.9
**prior_justification:** Sensitive spectrometer + ultralow-luminescence anvils; absence is definitive for bulk but cannot rule out trace amounts.
**Referenced by:** deduction -> `github:h3s_superconductivity::h2s_decomposition_not_to_h2`

### h2s_decomposition_not_to_h2

**QID:** `github:h3s_superconductivity::h2s_decomposition_not_to_h2`
**Type:** claim
**Role:** derived
**Content:** The decomposition reaction H₂S → H₂ + S is ruled out by two independent lines of evidence: (1) no H₂ vibron observed in Raman, and (2) Li et al. calculations showed this reaction is 'energetically very unfavorable.'
**Belief:** 0.82
**Derived from:** deduction
**Premises:** `github:h3s_superconductivity::no_h2_vibron`, `github:h3s_superconductivity::h2s_theory_prediction`
**gaia:** {'provenance': {'referenced_claims': ['h2s_theory_prediction', 'no_h2_vibron']}}
**Referenced by:** deduction -> `github:h3s_superconductivity::h3s_formation_hypothesis`

### sulfur_tc_too_low

**QID:** `github:h3s_superconductivity::sulfur_tc_too_low`
**Type:** claim
**Role:** derived
**Content:** Elemental sulfur precipitates from H₂S at P > 27 GPa. While sulfur is metallic and superconducting above 95 GPa, its Tc values (measured in this work, Fig. 2a dark yellow points) are far too low to explain the 190 K transition. Sulfur alone cannot be the source of the high-Tc state.
**Belief:** 0.91
**Derived from:** support
**Premises:** `github:h3s_superconductivity::sulfur_sc`
**gaia:** {'provenance': {'referenced_claims': ['sulfur_sc']}}
**Referenced by:** deduction -> `github:h3s_superconductivity::h3s_formation_hypothesis`

### h3s_formation_hypothesis

**QID:** `github:h3s_superconductivity::h3s_formation_hypothesis`
**Type:** claim
**Role:** derived
**Content:** The dissociation of H₂S under high pressure and temperature produces higher sulfur hydrides HₙS (n > 2) rather than H₂ + S. Proposed reactions: 2H₂S → H₄S + S, or 3H₂S → H₆S + S. These are plausible because sulfur has valency 2, 4, and 6; H₄S and H₆S are thermodynamically unstable but kinetically stable at ambient pressure, and high pressure may stabilize them.
**Belief:** 0.86
**Derived from:** deduction
**Premises:** `github:h3s_superconductivity::high_tc_not_predicted`, `github:h3s_superconductivity::h2s_decomposition_not_to_h2`, `github:h3s_superconductivity::sulfur_tc_too_low`
**gaia:** {'provenance': {'referenced_claims': ['h2s_decomposition_not_to_h2', 'high_tc_not_predicted', 'sulfur_tc_too_low']}}
**Referenced by:** deduction -> `github:h3s_superconductivity::high_tc_is_h3s`

### duan_prediction

**QID:** `github:h3s_superconductivity::duan_prediction`
**Type:** claim
**Role:** independent
**Content:** Duan et al. (2014) studied the van der Waals compound (H₂S)₂H₂ and predicted: (1) above 111 GPa, H₃S molecular units form; (2) above 180 GPa, sulfur coordination number reaches 6; (3) Tc ~ 160 K and ~190 K for these two phases. These predictions closely match the experimental observations.
**Prior:** 0.75
**Belief:** 0.75
**prior:** 0.75
**prior_justification:** Predicted Tc ~ 190 K for H₃S; structure search state-of-art but not exhaustive.
**Referenced by:** deduction -> `github:h3s_superconductivity::high_tc_is_h3s`

### raman_phase_transition

**QID:** `github:h3s_superconductivity::raman_phase_transition`
**Type:** claim
**Role:** independent
**Content:** Raman measurements of the sample with Tc ~ 190 K show a phase transformation at ~180 GPa upon pressure release. This matches the predicted structural transition in Duan et al.'s calculations and is distinct from elemental sulfur's phase transition at ~160 GPa.
**Prior:** 0.85
**Belief:** 0.85
**figure:** artifacts/images/ext-fig5-raman-sulfur-comparison.png
**caption:** Extended Data Fig. 5 | Raman spectra of sulfur hydride compared with elemental sulfur. (a) Elemental sulfur at different pressures. (b) Sulfur hydride at high pressures, showing apparent phase transition at ~180 GPa distinct from sulfur's transition at ~160 GPa.
**prior:** 0.85
**prior_justification:** Clear spectral changes at 180 GPa; pressure determination via diamond edge scale has ~5 GPa uncertainty.
**Referenced by:** deduction -> `github:h3s_superconductivity::high_tc_is_h3s`

### high_tc_is_h3s

**QID:** `github:h3s_superconductivity::high_tc_is_h3s`
**Type:** claim
**Role:** derived
**Content:** The high-Tc superconductivity at ~190–203 K is attributed to H₃S (trihydrogen sulfide) formed by dissociation of H₂S under pressure. This identification is supported by: (1) theoretical predictions from Duan et al. matching both the Tc values and structural transitions, (2) Raman evidence of a phase transition at 180 GPa consistent with H₃S, and (3) elimination of alternative explanations (pure H₂S, elemental sulfur, H₂ + S decomposition).
**Belief:** 0.77
**Derived from:** deduction
**Premises:** `github:h3s_superconductivity::h3s_formation_hypothesis`, `github:h3s_superconductivity::duan_prediction`, `github:h3s_superconductivity::raman_phase_transition`
**gaia:** {'provenance': {'referenced_claims': ['duan_prediction', 'h3s_formation_hypothesis', 'raman_phase_transition']}}
**Referenced by:** deduction -> `github:h3s_superconductivity::conventional_sc_above_200k`
