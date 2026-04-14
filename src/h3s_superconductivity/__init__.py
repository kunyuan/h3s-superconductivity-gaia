"""H₃S Superconductivity — Gaia Knowledge Package

Formalization of: Drozdov, A.P., Eremets, M.I., Troyan, I.A., Ksenofontov, V.
& Shylin, S.I. "Conventional superconductivity at 203 kelvin at high pressures
in the sulfur hydride system." Nature 525, 73–76 (2015).
arXiv: 1412.0460 [cond-mat.supr-con].

This package formalizes the reasoning graph for the discovery of high-temperature
superconductivity at ~200 K in H₃S under high pressure — the first demonstration
that BCS-type superconductivity can exceed the cuprate Tc record.
"""

# Section 1: Background and Theoretical Context
from .background import (
    ashcroft_hydrogen,
    bcs_theory,
    conventional_tc_limit,
    cuprate_record,
    diamond_anvil_cell,
    h2s_chosen_for_study,
    h2s_theory_prediction,
    hydrogen_dominant_alloys,
    main_question,
    silane_tc,
    sulfur_sc,
)

# Section 2: Metallization and Low-Tc Route
from .metallization import (
    h2s_metallization,
    low_tc_agrees_with_theory,
    low_tc_onset,
    low_tc_pressure_dependence,
)

# Section 3: High-Tc Discovery and Evidence
from .discovery import (
    accompanying_30k_step,
    high_tc_discovery,
    high_tc_not_predicted,
    isotope_effect,
    magnetic_field_proof,
    resistivity_proof,
    superconductivity_confirmed,
)

# Section 4: Interpretation — H₃S Formation
from .interpretation import (
    duan_prediction,
    h2s_decomposition_not_to_h2,
    h3s_formation_hypothesis,
    high_tc_is_h3s,
    no_h2_vibron,
    raman_phase_transition,
    sulfur_tc_too_low,
)

# Section 5: Implications
from .implications import (
    conventional_sc_above_200k,
    hydrogen_materials_prospect,
)

# Exported conclusions — cross-package interface
__all__ = [
    "superconductivity_confirmed",
    "high_tc_is_h3s",
    "conventional_sc_above_200k",
    "hydrogen_materials_prospect",
]
