"""Section 5: Implications for Hydrogen-Based Superconductors

Broader conclusions about the prospect of high-Tc superconductivity
in hydrogen-containing materials.
"""

from gaia.lang import claim, deduction

from .background import ashcroft_hydrogen, bcs_theory
from .discovery import superconductivity_confirmed
from .interpretation import high_tc_is_h3s

# ---------------------------------------------------------------------------
# Conclusions — Implications
# ---------------------------------------------------------------------------

conventional_sc_above_200k = claim(
    "Conventional (phonon-mediated, BCS-type) superconductivity has been "
    "demonstrated above 190 K (arXiv) / 203 K (Nature) — the highest Tc "
    "for any superconductor at the time of publication. This breaks the "
    "long-standing preconception that BCS superconductors are limited to "
    "Tc ~ 30 K and surpasses even the cuprate record of 164 K under "
    "pressure.",
    title="Conventional SC Above 200 K",
)

deduction(
    premises=[superconductivity_confirmed, high_tc_is_h3s],
    conclusion=conventional_sc_above_200k,
    reason=(
        "The isotope effect confirms BCS phonon mechanism "
        "(@superconductivity_confirmed) and the material is identified "
        "as H₃S (@high_tc_is_h3s). Together these establish that "
        "a conventional superconductor has reached ~200 K."
    ),
    prior=0.90,
)

hydrogen_materials_prospect = claim(
    "Since H₂S has only a moderate hydrogen content, high-Tc "
    "superconductivity can be expected in a wide range of "
    "hydrogen-containing materials. Candidates include carbon-based "
    "materials (fullerenes, aromatic hydrocarbons, graphanes) which "
    "could potentially be turned superconducting by doping or gating "
    "instead of extreme pressure. Hydrogen atoms are essential for "
    "providing high-frequency phonon modes and strong electron-phonon "
    "coupling.",
    title="Prospect for Hydrogen-Based Superconductors",
)

deduction(
    premises=[conventional_sc_above_200k, ashcroft_hydrogen],
    conclusion=hydrogen_materials_prospect,
    background=[bcs_theory],
    reason=(
        "The successful demonstration of ~200 K conventional SC in H₃S "
        "(@conventional_sc_above_200k) validates Ashcroft's hypothesis "
        "(@ashcroft_hydrogen) that hydrogen-rich materials can achieve "
        "extremely high Tc via BCS mechanism (@bcs_theory). Since H₂S "
        "has only moderate hydrogen content, materials with higher "
        "hydrogen fraction could reach even higher temperatures."
    ),
    prior=0.70,
)
