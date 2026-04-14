"""Section 2: Metallization and Low-Tc Superconductivity

Experimental observations of H₂S metallization and the low-temperature
route to superconductivity (Tc up to ~150 K), broadly consistent with
theoretical predictions.
"""

from gaia.lang import claim, deduction, support

from .background import (
    diamond_anvil_cell,
    h2s_theory_prediction,
)

# ---------------------------------------------------------------------------
# Claims — H₂S metallization
# ---------------------------------------------------------------------------

h2s_metallization = claim(
    "H₂S starts to conduct at P ~ 50 GPa (semiconductor with "
    "photoconductivity). At 90–100 GPa, the temperature dependence "
    "becomes metallic and photoconductivity disappears. H₂S is a poor "
    "metal: resistivity ρ ~ 3×10⁻⁵ Ω·m at 110 GPa, decreasing to "
    "ρ ~ 3×10⁻⁷ Ω·m at ~200 GPa.",
    title="H₂S Metallization at 90 GPa",
)

# ---------------------------------------------------------------------------
# Claims — Low-Tc route
# ---------------------------------------------------------------------------

low_tc_onset = claim(
    "When the metallic H₂S phase is cooled to 4 K at ~100 GPa, the "
    "resistance drops abruptly by 3–4 orders of magnitude at "
    "Tc ~ 23 K, indicating the onset of superconductivity.",
    title="Low-Tc Onset at 23 K",
)

deduction(
    premises=[h2s_metallization],
    conclusion=low_tc_onset,
    background=[diamond_anvil_cell],
    reason=(
        "Once H₂S is metallic (@h2s_metallization), cooling reveals a "
        "sharp resistance drop at Tc ~ 23 K — the characteristic "
        "signature of a superconducting transition. The metallic state "
        "is a prerequisite for observing superconductivity."
    ),
    prior=0.95,
)

low_tc_pressure_dependence = claim(
    "In the low-temperature route (pressure applied at 100–150 K), Tc "
    "increases with pressure from ~23 K at 100 GPa, with sharp growth "
    "approaching 200 GPa, reaching up to ~150 K at ~200 GPa.",
    title="Low-Tc Pressure Dependence",
)

deduction(
    premises=[low_tc_onset],
    conclusion=low_tc_pressure_dependence,
    background=[diamond_anvil_cell],
    reason=(
        "Systematic measurements at increasing pressures "
        "(@low_tc_onset at each pressure step) reveal a monotonic "
        "increase of Tc with pressure, with sharp enhancement near "
        "200 GPa. Pressures were determined by the diamond edge scale "
        "(@diamond_anvil_cell)."
    ),
    prior=0.95,
)

low_tc_agrees_with_theory = claim(
    "The low-temperature route Tc values (up to ~150 K at ~200 GPa) "
    "are in reasonable agreement with Li et al.'s prediction of "
    "Tc ~ 80 K for H₂S. The experimental values exceed the prediction, "
    "and the pressure dependence differs (no predicted drop of Tc at "
    "160 GPa), but the overall scale and trend are consistent with "
    "H₂S-phase superconductivity.",
    title="Low-Tc Route Agrees with H₂S Theory",
)

support(
    premises=[low_tc_pressure_dependence, h2s_theory_prediction],
    conclusion=low_tc_agrees_with_theory,
    reason=(
        "The experimentally observed Tc range (@low_tc_pressure_dependence) "
        "is broadly consistent with the ab initio prediction of Tc ~ 80 K "
        "(@h2s_theory_prediction), supporting that the low-Tc route "
        "represents conventional superconductivity in H₂S phases."
    ),
    prior=0.80,
)
