"""Section 1: Background and Theoretical Context

Establishes the BCS framework, Ashcroft's hydrogen hypothesis, and
theoretical predictions for H₂S that motivated the experimental study.
"""

from gaia.lang import claim, deduction, question, setting, support

# ---------------------------------------------------------------------------
# Settings — established frameworks and background
# ---------------------------------------------------------------------------

bcs_theory = setting(
    "Bardeen-Cooper-Schrieffer (BCS) theory: phonon-mediated electron-electron "
    "attraction leads to Cooper pairing. The Eliashberg formulation puts no "
    "apparent bounds on Tc. High Tc requires: (1) high-frequency phonons, "
    "(2) strong electron-phonon coupling, (3) high density of states.",
    title="BCS Theory",
)

cuprate_record = setting(
    "Prior to this work, the highest superconducting transition temperatures "
    "were in cuprates: Tc = 133 K at ambient pressure (HgBa₂Ca₂Cu₃O₈₊δ) "
    "and 164 K under high pressure. Cuprate superconductivity is "
    "unconventional — its mechanism remains undisclosed.",
    title="Cuprate Tc Record",
)

conventional_tc_limit = setting(
    "The highest Tc achieved through conventional (BCS-type) superconductor "
    "search prior to this work was 39 K in MgB₂. A common preconception "
    "held that Tc ~ 30 K is the maximum achievable in conventional "
    "superconductors.",
    title="Conventional Tc Limit Before This Work",
)

diamond_anvil_cell = setting(
    "Diamond anvil cell (DAC) enables static high-pressure experiments up to "
    "hundreds of GPa. The sample (diameter ~10 μm, thickness ~1 μm) is "
    "clamped in a metallic gasket between diamond anvils. Resistance is "
    "measured by four-probe Van der Pauw method with sputtered Ti/Au "
    "electrodes insulated from the gasket by Teflon or NaCl.",
    title="Diamond Anvil Cell Technique",
)

# ---------------------------------------------------------------------------
# Claims — Ashcroft's hydrogen hypothesis
# ---------------------------------------------------------------------------

ashcroft_hydrogen = claim(
    "Ashcroft (1968) predicted that metallic hydrogen would be a "
    "high-temperature superconductor due to: (1) very high vibrational "
    "frequencies from the light hydrogen atom, (2) strong electron-phonon "
    "interaction, and (3) covalent bonding. Subsequent calculations predict "
    "Tc = 100–240 K for molecular hydrogen and 300–350 K for the atomic "
    "phase at 500 GPa.",
    title="Ashcroft Hydrogen Hypothesis",
)

hydrogen_dominant_alloys = claim(
    "Ashcroft (2004) proposed that hydrogen-dominant metallic alloys "
    "(covalent hydrides such as SiH₄, SnH₄) could also be high-Tc "
    "superconductors: they share hydrogen's high Debye temperature while "
    "requiring lower metallization pressures than pure hydrogen. Heavier "
    "elements may additionally contribute low-frequency modes that enhance "
    "electron-phonon coupling.",
    title="Hydrogen-Dominant Alloy Prediction",
)

deduction(
    premises=[ashcroft_hydrogen],
    conclusion=hydrogen_dominant_alloys,
    background=[bcs_theory],
    reason=(
        "If metallic hydrogen is a high-Tc superconductor due to light-atom "
        "phonon frequencies and strong e-ph coupling (@ashcroft_hydrogen), "
        "then hydrogen-dominant compounds should retain these favorable "
        "properties while requiring lower pressures for metallization, "
        "following the BCS guide (@bcs_theory)."
    ),
    prior=0.90,
)

# ---------------------------------------------------------------------------
# Claims — Theoretical predictions for H₂S
# ---------------------------------------------------------------------------

h2s_theory_prediction = claim(
    "Li et al. (2014) predicted from ab initio calculations that H₂S "
    "metallizes at ~96 GPa and becomes a superconductor with Tc ~ 80 K "
    "at 160 GPa. At P > 130 GPa, new stable structures were found. "
    "Precipitation of sulfur was predicted to be 'very unlikely.'",
    title="Li et al. H₂S Tc Prediction",
)

# ---------------------------------------------------------------------------
# Claims — Prior experimental context
# ---------------------------------------------------------------------------

silane_tc = claim(
    "Prior to this work, only moderate Tc ~ 17 K had been observed "
    "experimentally in hydrogen-dominant materials (superconductivity in "
    "silane, SiH₄, by Eremets et al. 2008), far below theoretical "
    "predictions of Tc = 100–235 K for various hydrides.",
    title="Prior Hydride Tc Record",
)

sulfur_sc = claim(
    "Elemental sulfur becomes metallic above 95 GPa and is a "
    "superconductor, but with a low Tc (measured values shown in Fig. 2a "
    "as dark yellow points). Sulfur superconductivity alone cannot explain "
    "the high Tc observed in H₂S samples.",
    title="Sulfur Superconductivity",
)

# ---------------------------------------------------------------------------
# Claims — H₂S selected for study
# ---------------------------------------------------------------------------

h2s_chosen_for_study = claim(
    "H₂S was selected as the experimental target because: (1) it is "
    "relatively easy to handle, (2) it transforms to metal at a "
    "comparatively low pressure of ~100 GPa, and (3) the predicted "
    "Tc = 80 K is high enough to motivate experimental verification.",
    title="H₂S Selected for Experiment",
)

deduction(
    premises=[hydrogen_dominant_alloys, h2s_theory_prediction, silane_tc],
    conclusion=h2s_chosen_for_study,
    reason=(
        "The prediction that hydrogen-dominant compounds can be high-Tc "
        "superconductors (@hydrogen_dominant_alloys) combined with the "
        "specific prediction of Tc ~ 80 K for H₂S at accessible pressures "
        "(@h2s_theory_prediction) makes H₂S an attractive target — especially "
        "since prior hydride experiments only reached Tc ~ 17 K in SiH₄ "
        "(@silane_tc), far below theoretical predictions."
    ),
    prior=0.95,
)

# ---------------------------------------------------------------------------
# Question
# ---------------------------------------------------------------------------

main_question = question(
    "Can sulfur hydride (H₂S) under high pressure achieve "
    "superconducting transition temperatures significantly beyond those "
    "predicted by Li et al. (Tc ~ 80 K), and if so, what mechanism "
    "underlies the enhancement?",
    title="Main Question: High-Tc in Sulfur Hydride",
)
