"""Section 3: High-Tc Discovery — 190–203 K Superconductivity

The central experimental result: a second superconducting state with
Tc ~ 190 K (arXiv) / 203 K (Nature) found via a distinct high-temperature
pressurization route.
"""

from gaia.lang import claim, deduction, support

from .background import diamond_anvil_cell

# ---------------------------------------------------------------------------
# Claims — High-Tc discovery
# ---------------------------------------------------------------------------

high_tc_discovery = claim(
    "A second superconducting state with Tc ~ 190 K (arXiv v1) / 203 K "
    "(Nature) is found by applying pressure P > 150 GPa at temperatures "
    "T > 220 K (high-temperature route). This Tc has weak pressure "
    "dependence — qualitatively different from the low-T route.",
    title="High-Tc Discovery at 190–203 K",
    figure="artifacts/images/fig2-pressure-tc-phase-diagram.png",
    caption=(
        "Fig. 2b | Higher Tc ~ 190 K found when P > 150 GPa was applied "
        "at 220–300 K. Wine points show the accompanying 30 K step. "
        "Red point is Tc for D₂S sample."
    ),
)

high_tc_not_predicted = claim(
    "The high-Tc state (Tc ~ 190 K) is NOT seen or predicted in the "
    "Li et al. calculations for H₂S. The requirement of high temperature "
    "(T > 220 K) during pressurization suggests a chemical transformation "
    "(decomposition of H₂S) is involved in reaching this state.",
    title="High-Tc Not Predicted for H₂S",
)

deduction(
    premises=[high_tc_discovery],
    conclusion=high_tc_not_predicted,
    reason=(
        "The high-Tc state (@high_tc_discovery) requires T > 220 K during "
        "pressurization, suggesting a thermally-activated process. Since Li "
        "et al. calculated only pure H₂S structures and the low-T route "
        "agrees with those predictions, the high-Tc state must originate "
        "from a different phase formed by decomposition."
    ),
    prior=0.90,
)

accompanying_30k_step = claim(
    "The 190 K superconducting step is frequently accompanied by a "
    "second step at Tc ~ 30 K, which disappears with time (>1 day) "
    "or further pressure application while the 190 K step sharpens. "
    "R(T) oscillations with a period of 25–30 K are observed in "
    "multiple runs.",
    title="Accompanying 30 K Step and Oscillations",
    figure="artifacts/images/ext-fig3-190k-step-evolution.png",
    caption=(
        "Extended Data Fig. 3 | Transformation of the superconducting "
        "state in H₂S with pressure, temperature and time. The step "
        "at ~180 K developed at the cooling line, became more "
        "pronounced with time (15 hours)."
    ),
)

support(
    premises=[accompanying_30k_step],
    conclusion=high_tc_not_predicted,
    reason=(
        "The transient 30 K step (@accompanying_30k_step) that disappears "
        "with time while the 190 K step sharpens is consistent with a "
        "kinetically-controlled chemical transformation producing the "
        "high-Tc phase — supporting the conclusion that H₂S decomposition "
        "is involved."
    ),
    prior=0.75,
)

# ---------------------------------------------------------------------------
# Claims — Resistivity proof
# ---------------------------------------------------------------------------

resistivity_proof = claim(
    "The minimum resistance in the high-Tc state corresponds to "
    "resistivity ρ ≤ 10⁻¹¹ Ω·m — about two orders of magnitude less "
    "than pure copper at the same temperature. At 144 K specifically: "
    "ρ = 1.7×10⁻¹⁰ Ω·m, which is 50 times lower than copper "
    "(ρ_Cu = 70×10⁻¹⁰ Ω·m at 150 K).",
    title="Resistivity Far Below Copper",
    figure="artifacts/images/ext-fig3-190k-step-evolution.png",
    caption=(
        "Extended Data Fig. 3 | Minimum resistance R = 1.7×10⁻⁶ Ω at "
        "144 K (inset). Corresponding resistivity ρ ~ 1.7×10⁻¹⁰ Ω·m, "
        "~50× lower than copper."
    ),
)

# ---------------------------------------------------------------------------
# Claims — Magnetic field proof
# ---------------------------------------------------------------------------

magnetic_field_proof = claim(
    "Tc shifts to lower temperatures with magnetic field up to 7 Tesla "
    "for both superconducting states. Extrapolation using "
    "Hc(T) = Hc0·(1 − (T/Tc)²) gives estimated upper critical fields: "
    "Hc2 ~ 25 T for the Tc ~ 60 K state and Hc2 ~ 70 T for the "
    "Tc ~ 185 K state. The high Hc2 is characteristic of a type-II "
    "superconductor.",
    title="Magnetic Field Suppression of Tc",
    figure="artifacts/images/fig3-magnetic-field-dependence.png",
    caption=(
        "Fig. 3 | Temperature dependence of resistance at different "
        "magnetic fields. (a) ~60 K step at 155 GPa. (b) ~185 K step "
        "at 195 GPa. (c) Extrapolation of Hc2(T) to estimate critical "
        "fields ~25 T and ~70 T."
    ),
)

# ---------------------------------------------------------------------------
# Claims — Isotope effect proof
# ---------------------------------------------------------------------------

isotope_effect = claim(
    "Deuterium substitution (D₂S) shows a strong isotope effect: "
    "H₂S Tc ~ 60 K → D₂S Tc ~ 30 K, and H₂S Tc ~ 185 K → D₂S "
    "Tc ~ 90 K. The isotope exponent α ≈ 0.5, matching the BCS "
    "prediction Tc ∝ M^(−α) with α = 0.5 for the phonon mechanism. "
    "This confirms phonon-mediated (conventional BCS) superconductivity.",
    title="Strong Isotope Effect in D₂S",
    figure="artifacts/images/ext-fig4-d2s-isotope.png",
    caption=(
        "Extended Data Fig. 4 | Electrical measurements of sulfur "
        "deuteride at 163 GPa. R(T) measured at decreasing temperature "
        "showing Tc ~ 90 K, about half the H₂S value of ~185 K."
    ),
)

# ---------------------------------------------------------------------------
# Conclusion — Superconductivity confirmed
# ---------------------------------------------------------------------------

superconductivity_confirmed = claim(
    "The observed resistance drops represent genuine superconducting "
    "transitions, confirmed by three independent lines of evidence: "
    "(1) resistivity far below copper, (2) magnetic field suppression "
    "of Tc, and (3) a strong isotope effect consistent with BCS theory. "
    "The high-Tc state at ~190–203 K is a conventional (phonon-mediated) "
    "superconductor.",
    title="Superconductivity Confirmed by Three Proofs",
)

deduction(
    premises=[resistivity_proof, magnetic_field_proof, isotope_effect],
    conclusion=superconductivity_confirmed,
    background=[diamond_anvil_cell],
    reason=(
        "Three independent tests confirm superconductivity: "
        "(1) ρ ≤ 10⁻¹¹ Ω·m is far below copper (@resistivity_proof), "
        "ruling out a normal metallic state; "
        "(2) Tc decreases with field up to 7 T (@magnetic_field_proof), "
        "the hallmark of superconductivity; "
        "(3) BCS isotope exponent α ≈ 0.5 from D₂S (@isotope_effect) "
        "identifies the phonon mechanism. Together these exclude "
        "artifacts such as filamentary conduction or measurement errors."
    ),
    prior=0.95,
)
