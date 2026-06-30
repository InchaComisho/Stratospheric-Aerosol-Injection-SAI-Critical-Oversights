#!/usr/bin/env python3
"""
SAI Four-Circulation Destruction Risk Simulation
================================================

A simplified conceptual risk-scoring model for Stratospheric Aerosol
Injection (SAI), remapped through Master / InchaComisho's four-circulation
planetary failure definition.

This script is not a climate model.
It does not simulate real atmospheric chemistry, radiative transfer,
cloud microphysics, ocean dynamics, biosphere response, or global circulation.

It is a transparent conceptual scoring tool for comparing SAI scenarios
across overlooked risk dimensions and for mapping those risks to four
planetary circulation-destruction categories:

    1. Water phase-transition circulation damage
    2. Atmospheric circulation damage
    3. Ocean circulation damage
    4. Food and organic matter circulation damage

Core principle:
    Shading is not cooling.
    Cooling means restoring planetary circulation.
    A measure that suppresses sunlight while damaging circulation is not
    equivalent to natural cooling restoration.

License: CC BY 4.0
Author: Master / inchacomusho / InchaComisho
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict, List
import csv


# -----------------------------------------------------------------------------
# R1-R10: Original risk dimensions
# -----------------------------------------------------------------------------
# These weights represent the direct risk contribution of each dimension.
# They must sum to 1.0.
RISK_WEIGHTS: Dict[str, float] = {
    "existing_particle_load": 0.10,          # R1
    "vertical_layering_uncertainty": 0.08,   # R2
    "wet_deposition_weakening": 0.12,        # R3
    "surface_fixation_loss": 0.10,           # R4
    "resuspension_risk": 0.10,               # R5
    "cloud_rainfall_disruption": 0.14,       # R6
    "outgoing_heat_interaction": 0.08,       # R7
    "natural_cooling_feedback_damage": 0.14, # R8
    "governance_conflict_risk": 0.12,        # R9
    "termination_shock_risk": 0.12,          # R10
}

RISK_DIMENSION_LABELS: Dict[str, str] = {
    "existing_particle_load": "R1 Existing particle load",
    "vertical_layering_uncertainty": "R2 Vertical layering uncertainty",
    "wet_deposition_weakening": "R3 Wet deposition weakening",
    "surface_fixation_loss": "R4 Surface fixation loss",
    "resuspension_risk": "R5 Particle resuspension risk",
    "cloud_rainfall_disruption": "R6 Cloud and rainfall disruption",
    "outgoing_heat_interaction": "R7 Outgoing heat interaction uncertainty",
    "natural_cooling_feedback_damage": "R8 Natural cooling feedback damage",
    "governance_conflict_risk": "R9 Governance and conflict risk",
    "termination_shock_risk": "R10 Termination shock risk",
}


# -----------------------------------------------------------------------------
# Four-circulation mapping
# -----------------------------------------------------------------------------
# Each circulation score is calculated as a weighted average of R1-R10.
# The values below are conceptual mapping coefficients, not empirical constants.
# They express how strongly each SAI risk dimension can damage each circulation.
FOUR_CIRCULATION_MAPPING: Dict[str, Dict[str, float]] = {
    "water_phase_transition_damage": {
        "existing_particle_load": 0.20,
        "vertical_layering_uncertainty": 0.30,
        "wet_deposition_weakening": 0.90,
        "surface_fixation_loss": 0.40,
        "resuspension_risk": 0.45,
        "cloud_rainfall_disruption": 1.00,
        "outgoing_heat_interaction": 0.45,
        "natural_cooling_feedback_damage": 0.85,
        "governance_conflict_risk": 0.15,
        "termination_shock_risk": 0.25,
    },
    "atmospheric_circulation_damage": {
        "existing_particle_load": 0.85,
        "vertical_layering_uncertainty": 0.90,
        "wet_deposition_weakening": 0.65,
        "surface_fixation_loss": 0.25,
        "resuspension_risk": 0.70,
        "cloud_rainfall_disruption": 0.95,
        "outgoing_heat_interaction": 0.75,
        "natural_cooling_feedback_damage": 0.80,
        "governance_conflict_risk": 0.25,
        "termination_shock_risk": 0.35,
    },
    "ocean_circulation_damage": {
        "existing_particle_load": 0.25,
        "vertical_layering_uncertainty": 0.30,
        "wet_deposition_weakening": 0.45,
        "surface_fixation_loss": 0.35,
        "resuspension_risk": 0.35,
        "cloud_rainfall_disruption": 0.55,
        "outgoing_heat_interaction": 0.70,
        "natural_cooling_feedback_damage": 0.75,
        "governance_conflict_risk": 0.20,
        "termination_shock_risk": 0.45,
    },
    "food_organic_matter_circulation_damage": {
        "existing_particle_load": 0.20,
        "vertical_layering_uncertainty": 0.20,
        "wet_deposition_weakening": 0.55,
        "surface_fixation_loss": 0.90,
        "resuspension_risk": 0.80,
        "cloud_rainfall_disruption": 0.65,
        "outgoing_heat_interaction": 0.35,
        "natural_cooling_feedback_damage": 0.85,
        "governance_conflict_risk": 0.30,
        "termination_shock_risk": 0.35,
    },
}

CIRCULATION_LABELS: Dict[str, str] = {
    "water_phase_transition_damage": "Water phase-transition circulation damage",
    "atmospheric_circulation_damage": "Atmospheric circulation damage",
    "ocean_circulation_damage": "Ocean circulation damage",
    "food_organic_matter_circulation_damage": "Food and organic matter circulation damage",
}


@dataclass
class Scenario:
    """A single SAI risk scenario.

    All risk inputs should be between 0.0 and 1.0.

    0.0 = low apparent risk or well controlled
    0.5 = moderate risk or uncertain control
    1.0 = severe risk or high uncertainty
    """

    name: str
    description: str
    existing_particle_load: float
    vertical_layering_uncertainty: float
    wet_deposition_weakening: float
    surface_fixation_loss: float
    resuspension_risk: float
    cloud_rainfall_disruption: float
    outgoing_heat_interaction: float
    natural_cooling_feedback_damage: float
    governance_conflict_risk: float
    termination_shock_risk: float
    restores_natural_cooling_feedbacks: bool


def clamp(value: float) -> float:
    """Clamp a risk value to the 0.0-1.0 range."""
    return max(0.0, min(1.0, value))


def weighted_average(values: Dict[str, float], weights: Dict[str, float]) -> float:
    """Calculate a weighted average using normalized supplied weights."""
    total_weight = sum(weights.values())
    if total_weight <= 0:
        raise ValueError("Total weight must be positive.")
    return sum(clamp(values[key]) * weight for key, weight in weights.items()) / total_weight


def scenario_risk_values(scenario: Scenario) -> Dict[str, float]:
    """Return clamped R1-R10 risk values from a scenario."""
    data = asdict(scenario)
    return {key: clamp(float(data[key])) for key in RISK_WEIGHTS}


def calculate_base_risk_score(scenario: Scenario) -> float:
    """Calculate the original direct weighted risk score."""
    values = scenario_risk_values(scenario)
    return round(sum(values[key] * weight for key, weight in RISK_WEIGHTS.items()), 4)


def calculate_circulation_damage_scores(scenario: Scenario) -> Dict[str, float]:
    """Map R1-R10 risks to four-circulation destruction scores."""
    values = scenario_risk_values(scenario)
    scores: Dict[str, float] = {}
    for circulation, mapping_weights in FOUR_CIRCULATION_MAPPING.items():
        scores[circulation] = round(weighted_average(values, mapping_weights), 4)
    return scores


def calculate_circulation_coupling_pressure(circulation_scores: Dict[str, float]) -> float:
    """Estimate multi-circulation coupling pressure.

    This uses a complement-product formula:

        1 - Π(1 - damage_i)

    It rises rapidly when multiple circulations are damaged at the same time.
    This is a conceptual coupling indicator, not an empirical climate equation.
    """
    remaining_resilience = 1.0
    for score in circulation_scores.values():
        remaining_resilience *= 1.0 - clamp(score)
    return round(1.0 - remaining_resilience, 4)


def calculate_amplification_multiplier(
    scenario: Scenario, circulation_scores: Dict[str, float]
) -> float:
    """Calculate a conceptual multiplier for coupled circulation failure.

    The multiplier increases when:
    - several planetary circulations are damaged together;
    - all four circulations are damaged at the same time;
    - governance conflict and termination shock risks are high.
    """
    coupling_pressure = calculate_circulation_coupling_pressure(circulation_scores)
    weakest_recovery_point = min(circulation_scores.values())

    systemic_multiplier = 1.0
    systemic_multiplier += 0.50 * coupling_pressure
    systemic_multiplier += 0.25 * weakest_recovery_point
    systemic_multiplier += 0.20 * clamp(scenario.governance_conflict_risk)
    systemic_multiplier += 0.20 * clamp(scenario.termination_shock_risk)

    return round(systemic_multiplier, 4)


def calculate_four_circulation_risk_score(scenario: Scenario) -> float:
    """Calculate final amplified four-circulation risk score.

    The final score is capped to 1.0 for classification stability.
    The uncapped pressure is separately available through the multiplier.
    """
    base_score = calculate_base_risk_score(scenario)
    circulation_scores = calculate_circulation_damage_scores(scenario)
    multiplier = calculate_amplification_multiplier(scenario, circulation_scores)
    return round(clamp(base_score * multiplier), 4)


def classify_risk(score: float) -> str:
    """Classify risk score into qualitative classes."""
    if score < 0.20:
        return "Low apparent risk"
    if score < 0.40:
        return "Moderate risk"
    if score < 0.60:
        return "High risk"
    if score < 0.80:
        return "Severe risk"
    return "Critical risk"


def cooling_credit_status(scenario: Scenario) -> str:
    """Evaluate simplified Cooling Credit eligibility."""
    if scenario.restores_natural_cooling_feedbacks:
        return "Potentially eligible if measured and verified"
    return "Not eligible: shading intervention, not natural cooling restoration"


def default_scenarios() -> List[Scenario]:
    """Return illustrative default scenarios.

    These values are conceptual placeholders and should be replaced
    with expert-assessed or measured values for real research discussion.
    """
    return [
        Scenario(
            name="Research baseline",
            description="No deployment; monitoring and modeling only.",
            existing_particle_load=0.20,
            vertical_layering_uncertainty=0.30,
            wet_deposition_weakening=0.20,
            surface_fixation_loss=0.20,
            resuspension_risk=0.20,
            cloud_rainfall_disruption=0.20,
            outgoing_heat_interaction=0.20,
            natural_cooling_feedback_damage=0.20,
            governance_conflict_risk=0.20,
            termination_shock_risk=0.10,
            restores_natural_cooling_feedbacks=False,
        ),
        Scenario(
            name="Moderate research uncertainty",
            description="Research with incomplete atmospheric particle and rainfall data.",
            existing_particle_load=0.40,
            vertical_layering_uncertainty=0.50,
            wet_deposition_weakening=0.40,
            surface_fixation_loss=0.35,
            resuspension_risk=0.40,
            cloud_rainfall_disruption=0.45,
            outgoing_heat_interaction=0.40,
            natural_cooling_feedback_damage=0.45,
            governance_conflict_risk=0.35,
            termination_shock_risk=0.30,
            restores_natural_cooling_feedbacks=False,
        ),
        Scenario(
            name="Limited deployment",
            description="Hypothetical limited deployment under uncertain hydrological conditions.",
            existing_particle_load=0.55,
            vertical_layering_uncertainty=0.60,
            wet_deposition_weakening=0.55,
            surface_fixation_loss=0.50,
            resuspension_risk=0.55,
            cloud_rainfall_disruption=0.65,
            outgoing_heat_interaction=0.55,
            natural_cooling_feedback_damage=0.65,
            governance_conflict_risk=0.55,
            termination_shock_risk=0.60,
            restores_natural_cooling_feedbacks=False,
        ),
        Scenario(
            name="High-drying planet",
            description="Strong drying, forest loss, wetland loss, weakened rainfall, and high resuspension.",
            existing_particle_load=0.75,
            vertical_layering_uncertainty=0.70,
            wet_deposition_weakening=0.80,
            surface_fixation_loss=0.80,
            resuspension_risk=0.85,
            cloud_rainfall_disruption=0.75,
            outgoing_heat_interaction=0.65,
            natural_cooling_feedback_damage=0.85,
            governance_conflict_risk=0.60,
            termination_shock_risk=0.70,
            restores_natural_cooling_feedbacks=False,
        ),
        Scenario(
            name="Poor governance deployment",
            description="Unilateral deployment with weak monitoring, high uncertainty, and high termination risk.",
            existing_particle_load=0.65,
            vertical_layering_uncertainty=0.75,
            wet_deposition_weakening=0.65,
            surface_fixation_loss=0.60,
            resuspension_risk=0.65,
            cloud_rainfall_disruption=0.80,
            outgoing_heat_interaction=0.70,
            natural_cooling_feedback_damage=0.80,
            governance_conflict_risk=0.95,
            termination_shock_risk=0.95,
            restores_natural_cooling_feedbacks=False,
        ),
        Scenario(
            name="Natural cooling restoration alternative",
            description="Non-SAI pathway focused on rain, soil moisture, wetlands, forests, organic matter, and water-cycle recovery.",
            existing_particle_load=0.35,
            vertical_layering_uncertainty=0.20,
            wet_deposition_weakening=0.25,
            surface_fixation_loss=0.20,
            resuspension_risk=0.25,
            cloud_rainfall_disruption=0.20,
            outgoing_heat_interaction=0.20,
            natural_cooling_feedback_damage=0.10,
            governance_conflict_risk=0.25,
            termination_shock_risk=0.05,
            restores_natural_cooling_feedbacks=True,
        ),
    ]


def run_simulation(output_csv: str = "sai_risk_simulation_results.csv") -> List[Dict[str, str]]:
    """Run the default scenario simulation and write results to CSV."""
    results: List[Dict[str, str]] = []

    for scenario in default_scenarios():
        base_score = calculate_base_risk_score(scenario)
        circulation_scores = calculate_circulation_damage_scores(scenario)
        coupling_pressure = calculate_circulation_coupling_pressure(circulation_scores)
        amplification_multiplier = calculate_amplification_multiplier(scenario, circulation_scores)
        final_score = calculate_four_circulation_risk_score(scenario)

        result = {
            "scenario": scenario.name,
            "description": scenario.description,
            "base_weighted_risk_score": f"{base_score:.4f}",
            "water_phase_transition_damage": f"{circulation_scores['water_phase_transition_damage']:.4f}",
            "atmospheric_circulation_damage": f"{circulation_scores['atmospheric_circulation_damage']:.4f}",
            "ocean_circulation_damage": f"{circulation_scores['ocean_circulation_damage']:.4f}",
            "food_organic_matter_circulation_damage": f"{circulation_scores['food_organic_matter_circulation_damage']:.4f}",
            "circulation_coupling_pressure": f"{coupling_pressure:.4f}",
            "amplification_multiplier": f"{amplification_multiplier:.4f}",
            "four_circulation_risk_score": f"{final_score:.4f}",
            "risk_class": classify_risk(final_score),
            "cooling_credit_status": cooling_credit_status(scenario),
        }
        results.append(result)

    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(results[0].keys()))
        writer.writeheader()
        writer.writerows(results)

    return results


def print_results(results: List[Dict[str, str]]) -> None:
    """Print results in a readable console format."""
    print("SAI Four-Circulation Destruction Risk Simulation Results")
    print("=" * 96)
    for result in results:
        print(f"Scenario: {result['scenario']}")
        print(f"Description: {result['description']}")
        print(f"Base weighted risk score: {result['base_weighted_risk_score']}")
        print("Four-circulation damage scores:")
        print(f"  Water phase-transition: {result['water_phase_transition_damage']}")
        print(f"  Atmospheric circulation: {result['atmospheric_circulation_damage']}")
        print(f"  Ocean circulation: {result['ocean_circulation_damage']}")
        print(f"  Food / organic matter: {result['food_organic_matter_circulation_damage']}")
        print(f"Coupling pressure: {result['circulation_coupling_pressure']}")
        print(f"Amplification multiplier: {result['amplification_multiplier']}")
        print(f"Final four-circulation risk score: {result['four_circulation_risk_score']}")
        print(f"Risk class: {result['risk_class']}")
        print(f"Cooling Credit status: {result['cooling_credit_status']}")
        print("-" * 96)


if __name__ == "__main__":
    simulation_results = run_simulation()
    print_results(simulation_results)
