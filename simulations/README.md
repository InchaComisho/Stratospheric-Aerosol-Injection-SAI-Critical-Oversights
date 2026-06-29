# Simulations

## SAI Risk Scoring and Conceptual Scenario Simulation

This directory contains a simplified simulation model for evaluating the risk profile of Stratospheric Aerosol Injection (SAI) scenarios.

The simulation is not a climate model.

It is a transparent scoring tool designed to show that SAI cannot be evaluated only by expected sunlight reduction or global mean temperature change.

---

## Files

- [sai_risk_simulation.py](sai_risk_simulation.py)  
  Python script for calculating weighted SAI risk scores across multiple scenarios.

---

## What the Simulation Evaluates

The simulation scores ten risk dimensions:

```text
R1 Existing atmospheric particle load
R2 Vertical aerosol layering uncertainty
R3 Wet deposition weakening
R4 Surface fixation loss
R5 Particle resuspension risk
R6 Cloud and rainfall disruption
R7 Outgoing heat / infrared interaction risk
R8 Natural cooling feedback damage
R9 Governance and regional conflict risk
R10 Termination shock risk
```

Each risk dimension is scored from 0.0 to 1.0.

The weighted sum produces a total risk score between 0.0 and 1.0.

---

## Risk Classes

```text
0.00 - 0.20 = Low apparent risk
0.20 - 0.40 = Moderate risk
0.40 - 0.60 = High risk
0.60 - 0.80 = Severe risk
0.80 - 1.00 = Critical risk
```

---

## Default Scenarios

The script includes five scenarios:

```text
Research baseline
Moderate research uncertainty
Limited deployment
High-drying planet
Poor governance deployment
```

These scenarios are illustrative and should be replaced with real data or expert-assessed parameters if used for serious research discussion.

---

## How to Run

```bash
python sai_risk_simulation.py
```

The script prints scenario results to the console and writes:

```text
sai_risk_simulation_results.csv
```

---

## Required Packages

The script uses only the Python standard library.

No external dependencies are required.

---

## Interpretation

A high risk score does not prove that SAI will necessarily fail.

It indicates that the scenario contains major unresolved risks that should prevent SAI from being treated as a simple cooling solution.

The simulation also includes a Cooling Credit eligibility filter.

If a scenario does not restore natural cooling feedbacks, it is classified as:

```text
Shading intervention, not Cooling Credit eligible
```

---

## Core Principle

> Shading is not cooling.  
> Cooling means restoring planetary circulation.

---

## License

CC BY 4.0
