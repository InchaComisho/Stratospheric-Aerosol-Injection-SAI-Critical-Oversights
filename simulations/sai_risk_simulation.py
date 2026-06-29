#!/usr/bin/env python3
"""
SAI Risk Simulation
===================

A simplified risk-scoring model for Stratospheric Aerosol Injection (SAI).

This script is not a climate model.
It does not simulate real atmospheric chemistry, radiative transfer,
cloud microphysics, or global circulation.

It is a transparent conceptual scoring tool for comparing SAI scenarios
across overlooked risk dimensions such as existing aerosol load,
wet deposition weakening, surface fixation loss, particle resuspension,
cloud/rainfall disruption, governance, and termination shock.

Core principle:
    Shading is not cooling.
    Cooling means restoring planetary circulation.

License: CC BY 4.0
Author: Master / inchacomusho / InchaComisho
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict, List
import csv


# Risk weights must sum to 1.0.
RISK_WEIGHTS: Dict[str, float] = {
    "existing_particle_load": 0.10,
    "vertical_layering_uncertainty": 0.08,
    "wet_deposition_weakening": 0.12,
    "surface_fixation_loss": 0.10,
    "resuspension_risk": 0.10,
    "cloud_rainfall_disruption": 0.14,
    "outgoing_heat_interaction": 0.08,
    "natural_cooling_feedback_damage": 0.14,
    "governance_conflict_risk": 0.12,
    "termination_shock_risk": 0.12,
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


def calculate_risk_score(scenario: Scenario) -> float:
    """Calculate a weighted risk score for one scenario."""
    data = asdict(scenario)
    total = 0.0
    for key, weight in RISK_WEIGHTS.items():
        total += clamp(float(data[key])) * weight
    return round(total, 4)


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
            description="Non-SAI pathway focused on rain, soil moisture, wetlands, forests, and water-cycle recovery.",
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
        score = calculate_risk_score(scenario)
        result = {
            "scenario": scenario.name,
            "description": scenario.description,
            "risk_score": f"{score:.4f}",
            "risk_class": classify_risk(score),
            "cooling_credit_status": cooling_credit_status(scenario),
        }
        results.append(result)

    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "scenario",
                "description",
                "risk_score",
                "risk_class",
                "cooling_credit_status",
            ],
        )
        writer.writeheader()
        writer.writerows(results)

    return results


def print_results(results: List[Dict[str, str]]) -> None:
    """Print results in a readable console format."""
    print("SAI Risk Simulation Results")
    print("=" * 80)
    for result in results:
        print(f"Scenario: {result['scenario']}")
        print(f"Description: {result['description']}")
        print(f"Risk score: {result['risk_score']}")
        print(f"Risk class: {result['risk_class']}")
        print(f"Cooling Credit status: {result['cooling_credit_status']}")
        print("-" * 80)


if __name__ == "__main__":
    simulation_results = run_simulation()
    print_results(simulation_results)
