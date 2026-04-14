# Module: implications

### conventional_sc_above_200k

**QID:** `github:h3s_superconductivity::conventional_sc_above_200k`
**Type:** claim
**Role:** derived
**Content:** Conventional (phonon-mediated, BCS-type) superconductivity has been demonstrated above 190 K (arXiv) / 203 K (Nature) — the highest Tc for any superconductor at the time of publication. This breaks the long-standing preconception that BCS superconductors are limited to Tc ~ 30 K and surpasses even the cuprate record of 164 K under pressure.
**Belief:** 0.84
**Derived from:** deduction
**Premises:** `github:h3s_superconductivity::superconductivity_confirmed`, `github:h3s_superconductivity::high_tc_is_h3s`
**gaia:** {'provenance': {'referenced_claims': ['high_tc_is_h3s', 'superconductivity_confirmed']}}
**Referenced by:** deduction -> `github:h3s_superconductivity::hydrogen_materials_prospect`

### hydrogen_materials_prospect

**QID:** `github:h3s_superconductivity::hydrogen_materials_prospect`
**Type:** claim
**Role:** derived
**Content:** Since H₂S has only a moderate hydrogen content, high-Tc superconductivity can be expected in a wide range of hydrogen-containing materials. Candidates include carbon-based materials (fullerenes, aromatic hydrocarbons, graphanes) which could potentially be turned superconducting by doping or gating instead of extreme pressure. Hydrogen atoms are essential for providing high-frequency phonon modes and strong electron-phonon coupling.
**Belief:** 0.90
**Derived from:** deduction
**Premises:** `github:h3s_superconductivity::conventional_sc_above_200k`, `github:h3s_superconductivity::ashcroft_hydrogen`
**gaia:** {'provenance': {'referenced_claims': ['ashcroft_hydrogen', 'bcs_theory', 'conventional_sc_above_200k']}}
