"""Leaf claim priors — package input interface.

Each entry maps a leaf claim (not derived by any strategy) to its
prior probability and a one-line justification. These are injected
into claim metadata by ``gaia compile`` and read by the lowering
layer during inference.
"""

from .background import (
    ashcroft_hydrogen,
    h2s_theory_prediction,
    silane_tc,
    sulfur_sc,
)
from .discovery import (
    accompanying_30k_step,
    high_tc_discovery,
    isotope_effect,
    magnetic_field_proof,
    resistivity_proof,
)
from .interpretation import (
    duan_prediction,
    no_h2_vibron,
    raman_phase_transition,
)
from .metallization import h2s_metallization

PRIORS: dict = {
    # Foundational claims — well-established physics
    ashcroft_hydrogen: (
        0.95,
        "Widely cited prediction (1968); supported by decades of calculations.",
    ),

    # Theoretical predictions
    h2s_theory_prediction: (
        0.80,
        "Ab initio DFT prediction; structure search may miss lower-energy phases.",
    ),
    duan_prediction: (
        0.75,
        "Predicted Tc ~ 190 K for H₃S; structure search state-of-art but not exhaustive.",
    ),

    # Experimental observations — direct measurements
    h2s_metallization: (
        0.95,
        "Direct resistance and photoconductivity measurements in DAC.",
    ),
    high_tc_discovery: (
        0.90,
        "Resistance drops to sub-copper levels; reproduced in multiple runs. "
        "Sample inhomogeneity and pressure gradients add some uncertainty.",
    ),
    resistivity_proof: (
        0.95,
        "ρ = 1.7×10⁻¹⁰ Ω·m, 50× below copper; measurement well-calibrated.",
    ),
    magnetic_field_proof: (
        0.90,
        "Clear Tc shift with field up to 7 T; Hc2 extrapolation adds uncertainty.",
    ),
    isotope_effect: (
        0.92,
        "α ≈ 0.5 matches BCS; D₂S purity 97% introduces slight uncertainty.",
    ),
    accompanying_30k_step: (
        0.85,
        "Observed in multiple runs; transient nature makes systematic study difficult.",
    ),

    # Spectroscopic evidence
    no_h2_vibron: (
        0.90,
        "Sensitive spectrometer + ultralow-luminescence anvils; absence is definitive "
        "for bulk but cannot rule out trace amounts.",
    ),
    raman_phase_transition: (
        0.85,
        "Clear spectral changes at 180 GPa; pressure determination via diamond edge "
        "scale has ~5 GPa uncertainty.",
    ),

    # Background facts
    silane_tc: (
        0.90,
        "Published result (Eremets 2008); some debate on whether SiH₄ was pure phase.",
    ),
    sulfur_sc: (
        0.95,
        "Well-established; measured independently by multiple groups.",
    ),
}
