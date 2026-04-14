"""Section 4: Interpretation — H₃S Formation from H₂S Decomposition

Interprets the high-Tc state as arising from H₃S formed by H₂S
decomposition under pressure, supported by theoretical calculations
of Duan et al. and Raman spectroscopy evidence.
"""

from gaia.lang import claim, deduction, support

from .background import h2s_theory_prediction, sulfur_sc
from .discovery import high_tc_not_predicted

# ---------------------------------------------------------------------------
# Claims — Ruling out alternatives
# ---------------------------------------------------------------------------

no_h2_vibron = claim(
    "The strong characteristic vibron of molecular H₂ was never observed "
    "in Raman spectra despite using a sensitive spectrometer and ultralow "
    "luminescence synthetic diamond anvils. This rules out simple "
    "decomposition H₂S → H₂ + S.",
    title="No H₂ Vibron in Raman",
    figure="artifacts/images/ext-fig1-raman-spectra.png",
    caption=(
        "Supplementary Fig. 1 | Raman spectra of sulfur hydride at "
        "different pressures. (a) H₂S spectra at increasing pressure. "
        "(b) D₂S Raman spectra. No H₂ vibron peak is observed."
    ),
)

h2s_decomposition_not_to_h2 = claim(
    "The decomposition reaction H₂S → H₂ + S is ruled out by two "
    "independent lines of evidence: (1) no H₂ vibron observed in Raman, "
    "and (2) Li et al. calculations showed this reaction is 'energetically "
    "very unfavorable.'",
    title="H₂S Does Not Decompose to H₂ + S",
)

deduction(
    premises=[no_h2_vibron, h2s_theory_prediction],
    conclusion=h2s_decomposition_not_to_h2,
    reason=(
        "The absence of H₂ Raman vibron (@no_h2_vibron) provides direct "
        "spectroscopic evidence against H₂ formation, while Li et al.'s "
        "thermodynamic calculations (@h2s_theory_prediction) independently "
        "show H₂S → H₂ + S is energetically unfavorable."
    ),
    prior=0.92,
)

sulfur_tc_too_low = claim(
    "Elemental sulfur precipitates from H₂S at P > 27 GPa. While sulfur "
    "is metallic and superconducting above 95 GPa, its Tc values (measured "
    "in this work, Fig. 2a dark yellow points) are far too low to explain "
    "the 190 K transition. Sulfur alone cannot be the source of the high-Tc "
    "state.",
    title="Sulfur Tc Too Low",
)

support(
    premises=[sulfur_sc],
    conclusion=sulfur_tc_too_low,
    reason=(
        "Direct measurements of elemental sulfur Tc (@sulfur_sc) under "
        "comparable pressure conditions show values well below 190 K, "
        "ruling out sulfur as the sole source of the high-Tc phase."
    ),
    prior=0.95,
)

# ---------------------------------------------------------------------------
# Claims — H₃S hypothesis
# ---------------------------------------------------------------------------

h3s_formation_hypothesis = claim(
    "The dissociation of H₂S under high pressure and temperature produces "
    "higher sulfur hydrides HₙS (n > 2) rather than H₂ + S. Proposed "
    "reactions: 2H₂S → H₄S + S, or 3H₂S → H₆S + S. These are plausible "
    "because sulfur has valency 2, 4, and 6; H₄S and H₆S are "
    "thermodynamically unstable but kinetically stable at ambient pressure, "
    "and high pressure may stabilize them.",
    title="H₃S Formation Hypothesis",
)

deduction(
    premises=[high_tc_not_predicted, h2s_decomposition_not_to_h2, sulfur_tc_too_low],
    conclusion=h3s_formation_hypothesis,
    reason=(
        "Since the high-Tc state is not explained by H₂S (@high_tc_not_predicted), "
        "simple H₂ + S decomposition is excluded (@h2s_decomposition_not_to_h2), "
        "and sulfur alone has too low Tc (@sulfur_tc_too_low), the material "
        "must be a higher hydride HₙS (n > 2) formed from H₂S decomposition."
    ),
    prior=0.80,
)

# ---------------------------------------------------------------------------
# Claims — Theoretical support from Duan et al.
# ---------------------------------------------------------------------------

duan_prediction = claim(
    "Duan et al. (2014) studied the van der Waals compound (H₂S)₂H₂ and "
    "predicted: (1) above 111 GPa, H₃S molecular units form; (2) above "
    "180 GPa, sulfur coordination number reaches 6; (3) Tc ~ 160 K and "
    "~190 K for these two phases. These predictions closely match the "
    "experimental observations.",
    title="Duan et al. H₃S Prediction",
)

raman_phase_transition = claim(
    "Raman measurements of the sample with Tc ~ 190 K show a phase "
    "transformation at ~180 GPa upon pressure release. This matches the "
    "predicted structural transition in Duan et al.'s calculations and "
    "is distinct from elemental sulfur's phase transition at ~160 GPa.",
    title="Raman Phase Transition at 180 GPa",
    figure="artifacts/images/ext-fig5-raman-sulfur-comparison.png",
    caption=(
        "Extended Data Fig. 5 | Raman spectra of sulfur hydride compared "
        "with elemental sulfur. (a) Elemental sulfur at different "
        "pressures. (b) Sulfur hydride at high pressures, showing "
        "apparent phase transition at ~180 GPa distinct from sulfur's "
        "transition at ~160 GPa."
    ),
)

# ---------------------------------------------------------------------------
# Conclusion — H₃S identified
# ---------------------------------------------------------------------------

high_tc_is_h3s = claim(
    "The high-Tc superconductivity at ~190–203 K is attributed to H₃S "
    "(trihydrogen sulfide) formed by dissociation of H₂S under pressure. "
    "This identification is supported by: (1) theoretical predictions from "
    "Duan et al. matching both the Tc values and structural transitions, "
    "(2) Raman evidence of a phase transition at 180 GPa consistent with "
    "H₃S, and (3) elimination of alternative explanations (pure H₂S, "
    "elemental sulfur, H₂ + S decomposition).",
    title="High-Tc Phase Identified as H₃S",
)

deduction(
    premises=[h3s_formation_hypothesis, duan_prediction, raman_phase_transition],
    conclusion=high_tc_is_h3s,
    reason=(
        "The hypothesis that HₙS (n > 2) forms from H₂S decomposition "
        "(@h3s_formation_hypothesis) is confirmed by Duan et al.'s "
        "prediction of Tc ~ 190 K for H₃S (@duan_prediction) matching "
        "the observation, and Raman evidence of a phase transition at "
        "180 GPa (@raman_phase_transition) matching the predicted "
        "structural transition. The convergence of elimination reasoning, "
        "theoretical prediction, and spectroscopic evidence identifies "
        "the high-Tc phase as H₃S."
    ),
    prior=0.80,
)
