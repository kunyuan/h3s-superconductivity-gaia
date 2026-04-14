# Narrative Outline

Auto-generated from the coarse reasoning graph. Sections are grouped by connectivity (high cohesion, low coupling) and ordered by topological layer. Use this as the backbone for writing narrative summaries.

## High-Tc Discovery at 190–203 K

1. **Li et al. H₂S Tc Prediction** (prior: 0.80 → belief: 0.72)
   - → supports: high_tc_is_h3s

2. **Duan et al. H₃S Prediction** (prior: 0.75 → belief: 0.75)
   - → supports: high_tc_is_h3s

3. **Accompanying 30 K Step and Oscillations** (prior: 0.85 → belief: 0.85)
   - → supports: high_tc_is_h3s

4. **Raman Phase Transition at 180 GPa** (prior: 0.85 → belief: 0.85)
   - → supports: high_tc_is_h3s

5. **No H₂ Vibron in Raman** (prior: 0.90 → belief: 0.90)
   - → supports: high_tc_is_h3s

6. **Sulfur Superconductivity** (prior: 0.95 → belief: 0.91)
   - → supports: high_tc_is_h3s

7. **High-Tc Discovery at 190–203 K** (prior: 0.90 → belief: 0.93)
   - → supports: high_tc_is_h3s

## Resistivity Far Below Copper

8. **Magnetic Field Suppression of Tc** (prior: 0.90 → belief: 0.90)
   - → supports: superconductivity_confirmed

9. **Strong Isotope Effect in D₂S** (prior: 0.92 → belief: 0.92)
   - → supports: superconductivity_confirmed

10. **Resistivity Far Below Copper** (prior: 0.95 → belief: 0.95)
   - → supports: superconductivity_confirmed

## Ashcroft Hydrogen Hypothesis

11. **Ashcroft Hydrogen Hypothesis** (prior: 0.95 → belief: 0.95)
   - → supports: hydrogen_materials_prospect

## Superconductivity Confirmed by Three Proofs

12. **High-Tc Phase Identified as H₃S ★** (prior: 0.50 → belief: 0.77)
   - ← infer(accompanying_30k_step, duan_prediction, h2s_theory_prediction, high_tc_discovery, no_h2_vibron, raman_phase_transition, sulfur_sc) [0.21 bits]
   - → supports: conventional_sc_above_200k

13. **Superconductivity Confirmed by Three Proofs ★** (prior: 0.50 → belief: 0.89)
   - ← infer(isotope_effect, magnetic_field_proof, resistivity_proof) [0.26 bits]
   - → supports: conventional_sc_above_200k

## Conventional SC Above 200 K

14. **Conventional SC Above 200 K ★** (prior: 0.50 → belief: 0.84)
   - ← infer(high_tc_is_h3s, superconductivity_confirmed) [0.20 bits]
   - → supports: hydrogen_materials_prospect

## Prospect for Hydrogen-Based Superconductors

15. **Prospect for Hydrogen-Based Superconductors ★** (prior: 0.50 → belief: 0.90)
   - ← infer(ashcroft_hydrogen, conventional_sc_above_200k) [0.29 bits]
