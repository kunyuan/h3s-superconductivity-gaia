# Module: background

### bcs_theory

**QID:** `github:h3s_superconductivity::bcs_theory`
**Type:** setting
**Role:** setting
**Content:** Bardeen-Cooper-Schrieffer (BCS) theory: phonon-mediated electron-electron attraction leads to Cooper pairing. The Eliashberg formulation puts no apparent bounds on Tc. High Tc requires: (1) high-frequency phonons, (2) strong electron-phonon coupling, (3) high density of states.

### cuprate_record

**QID:** `github:h3s_superconductivity::cuprate_record`
**Type:** setting
**Role:** setting
**Content:** Prior to this work, the highest superconducting transition temperatures were in cuprates: Tc = 133 K at ambient pressure (HgBa₂Ca₂Cu₃O₈₊δ) and 164 K under high pressure. Cuprate superconductivity is unconventional — its mechanism remains undisclosed.

### conventional_tc_limit

**QID:** `github:h3s_superconductivity::conventional_tc_limit`
**Type:** setting
**Role:** setting
**Content:** The highest Tc achieved through conventional (BCS-type) superconductor search prior to this work was 39 K in MgB₂. A common preconception held that Tc ~ 30 K is the maximum achievable in conventional superconductors.

### diamond_anvil_cell

**QID:** `github:h3s_superconductivity::diamond_anvil_cell`
**Type:** setting
**Role:** setting
**Content:** Diamond anvil cell (DAC) enables static high-pressure experiments up to hundreds of GPa. The sample (diameter ~10 μm, thickness ~1 μm) is clamped in a metallic gasket between diamond anvils. Resistance is measured by four-probe Van der Pauw method with sputtered Ti/Au electrodes insulated from the gasket by Teflon or NaCl.

### ashcroft_hydrogen

**QID:** `github:h3s_superconductivity::ashcroft_hydrogen`
**Type:** claim
**Role:** independent
**Content:** Ashcroft (1968) predicted that metallic hydrogen would be a high-temperature superconductor due to: (1) very high vibrational frequencies from the light hydrogen atom, (2) strong electron-phonon interaction, and (3) covalent bonding. Subsequent calculations predict Tc = 100–240 K for molecular hydrogen and 300–350 K for the atomic phase at 500 GPa.
**Prior:** 0.95
**Belief:** 0.95
**prior:** 0.95
**prior_justification:** Widely cited prediction (1968); supported by decades of calculations.
**Referenced by:** deduction -> `github:h3s_superconductivity::hydrogen_dominant_alloys`; deduction -> `github:h3s_superconductivity::hydrogen_materials_prospect`

### hydrogen_dominant_alloys

**QID:** `github:h3s_superconductivity::hydrogen_dominant_alloys`
**Type:** claim
**Role:** derived
**Content:** Ashcroft (2004) proposed that hydrogen-dominant metallic alloys (covalent hydrides such as SiH₄, SnH₄) could also be high-Tc superconductors: they share hydrogen's high Debye temperature while requiring lower metallization pressures than pure hydrogen. Heavier elements may additionally contribute low-frequency modes that enhance electron-phonon coupling.
**Belief:** 0.97
**Derived from:** deduction
**Premises:** `github:h3s_superconductivity::ashcroft_hydrogen`
**gaia:** {'provenance': {'referenced_claims': ['ashcroft_hydrogen', 'bcs_theory']}}
**Referenced by:** deduction -> `github:h3s_superconductivity::h2s_chosen_for_study`

### h2s_theory_prediction

**QID:** `github:h3s_superconductivity::h2s_theory_prediction`
**Type:** claim
**Role:** independent
**Content:** Li et al. (2014) predicted from ab initio calculations that H₂S metallizes at ~96 GPa and becomes a superconductor with Tc ~ 80 K at 160 GPa. At P > 130 GPa, new stable structures were found. Precipitation of sulfur was predicted to be 'very unlikely.'
**Prior:** 0.80
**Belief:** 0.72
**prior:** 0.8
**prior_justification:** Ab initio DFT prediction; structure search may miss lower-energy phases.
**Referenced by:** deduction -> `github:h3s_superconductivity::h2s_chosen_for_study`; support -> `github:h3s_superconductivity::low_tc_agrees_with_theory`; deduction -> `github:h3s_superconductivity::h2s_decomposition_not_to_h2`

### silane_tc

**QID:** `github:h3s_superconductivity::silane_tc`
**Type:** claim
**Role:** independent
**Content:** Prior to this work, only moderate Tc ~ 17 K had been observed experimentally in hydrogen-dominant materials (superconductivity in silane, SiH₄, by Eremets et al. 2008), far below theoretical predictions of Tc = 100–235 K for various hydrides.
**Prior:** 0.90
**Belief:** 0.90
**prior:** 0.9
**prior_justification:** Published result (Eremets 2008); some debate on whether SiH₄ was pure phase.
**Referenced by:** deduction -> `github:h3s_superconductivity::h2s_chosen_for_study`

### sulfur_sc

**QID:** `github:h3s_superconductivity::sulfur_sc`
**Type:** claim
**Role:** independent
**Content:** Elemental sulfur becomes metallic above 95 GPa and is a superconductor, but with a low Tc (measured values shown in Fig. 2a as dark yellow points). Sulfur superconductivity alone cannot explain the high Tc observed in H₂S samples.
**Prior:** 0.95
**Belief:** 0.91
**figure:** artifacts/images/fig2-pressure-tc-phase-diagram.png
**caption:** Fig. 2 | Pressure dependence of critical superconducting temperature Tc on pressure. Dark yellow points are Tc of pure sulfur, far below the H₂S/D₂S values.
**prior:** 0.95
**prior_justification:** Well-established; measured independently by multiple groups.
**Referenced by:** support -> `github:h3s_superconductivity::sulfur_tc_too_low`

### h2s_chosen_for_study

**QID:** `github:h3s_superconductivity::h2s_chosen_for_study`
**Type:** claim
**Role:** derived
**Content:** H₂S was selected as the experimental target because: (1) it is relatively easy to handle, (2) it transforms to metal at a comparatively low pressure of ~100 GPa, and (3) the predicted Tc = 80 K is high enough to motivate experimental verification.
**Belief:** 0.81
**Derived from:** deduction
**Premises:** `github:h3s_superconductivity::hydrogen_dominant_alloys`, `github:h3s_superconductivity::h2s_theory_prediction`, `github:h3s_superconductivity::silane_tc`
**gaia:** {'provenance': {'referenced_claims': ['h2s_theory_prediction', 'hydrogen_dominant_alloys', 'silane_tc']}}

### main_question

**QID:** `github:h3s_superconductivity::main_question`
**Type:** question
**Role:** question
**Content:** Can sulfur hydride (H₂S) under high pressure achieve superconducting transition temperatures significantly beyond those predicted by Li et al. (Tc ~ 80 K), and if so, what mechanism underlies the enhancement?
