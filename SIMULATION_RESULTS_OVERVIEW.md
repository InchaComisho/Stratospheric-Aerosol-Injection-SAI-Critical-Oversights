# Simulation Results Overview

## Reading the SAI Risk Simulation Output

This document explains how to interpret the simplified SAI risk simulation model in this repository.

The simulation does not predict the real climate.

It provides a transparent conceptual framework for comparing risk profiles across scenarios.

---

## 1. Model Summary

The simulation evaluates ten risk categories:

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

Each category is scored between 0.0 and 1.0.

A weighted sum produces a total risk score.

---

## 2. Default Risk Classes

```text
0.00 - 0.20 = Low apparent risk
0.20 - 0.40 = Moderate risk
0.40 - 0.60 = High risk
0.60 - 0.80 = Severe risk
0.80 - 1.00 = Critical risk
```

---

## 3. Scenario Interpretation

### Research Baseline

This scenario represents monitoring and modeling without deployment.

Expected interpretation:

```text
Risk class: Low to moderate
Cooling Credit status: Not eligible, because no natural cooling restoration occurs
```

Even research-only activity does not become a Cooling Credit unless it directly restores cooling functions.

---

### Moderate Research Uncertainty

This scenario represents research or policy discussion with incomplete atmospheric particle and rainfall data.

Expected interpretation:

```text
Risk class: Moderate to high
Main warning: knowledge gaps are already significant
```

This scenario highlights the need for atmospheric particle inventory, rainfall cleaning assessment, and surface fixation analysis.

---

### Limited Deployment

This scenario represents hypothetical limited SAI deployment.

Expected interpretation:

```text
Risk class: High to severe
Main warning: even limited deployment can carry hydrological, particle, governance, and termination risks
```

Limited deployment should not be treated as low risk simply because the injected quantity is smaller.

---

### High-Drying Planet

This scenario represents a world with strong warming, dry soils, forest loss, wetland loss, weakened rainfall, and high resuspension.

Expected interpretation:

```text
Risk class: Severe
Main warning: adding aerosols to an already particle-loaded and drying atmosphere may increase systemic risk
```

This is the scenario most closely related to the Atmospheric Particle Saturation and Resuspension Loop.

---

### Poor Governance Deployment

This scenario represents unilateral or weakly governed deployment.

Expected interpretation:

```text
Risk class: Severe to critical
Main warning: governance and termination shock may dominate the risk profile
```

A globally active intervention cannot be treated as a narrow technical project.

---

### Natural Cooling Restoration Alternative

This scenario represents non-SAI restoration of rain, soil moisture, forests, wetlands, rivers, oceans, and water-cycle feedbacks.

Expected interpretation:

```text
Risk class: Low to moderate
Cooling Credit status: Potentially eligible if measured and verified
```

This scenario is included to show the difference between shading and restoration.

---

## 4. Example Output

A typical run may produce a table like this:

```text
Scenario                              Risk Class       Cooling Credit Status
Research baseline                     Low/Moderate     Not eligible
Moderate research uncertainty          Moderate/High    Not eligible
Limited deployment                     High/Severe      Not eligible
High-drying planet                     Severe           Not eligible
Poor governance deployment             Severe/Critical  Not eligible
Natural cooling restoration alternative Low/Moderate    Potentially eligible
```

Exact values depend on scenario parameters.

---

## 5. Why This Matters

A conventional SAI analysis may focus on:

```text
reduced incoming sunlight
aerosol optical depth
global mean temperature response
```

This risk model adds missing dimensions:

```text
existing particle load
rain-cleaning capacity
wet deposition
surface fixation
particle resuspension
cloud and rainfall disruption
outgoing heat interactions
natural cooling feedback damage
governance
termination shock
```

The model therefore asks a different question:

> Does SAI restore the Earth's cooling system, or does it merely shade a damaged system?

---

## 6. Cooling Credit Interpretation

The simulation includes a simplified Cooling Credit filter.

If a scenario does not restore natural cooling feedbacks, it is classified as:

```text
Not eligible: shading intervention, not natural cooling restoration
```

This is important because a temperature signal alone is not enough.

Cooling Credit requires restoration of measurable cooling functions such as:

```text
soil moisture
evapotranspiration
rainfall cleaning
wet deposition
surface particle fixation
forest cooling
wetland recovery
ocean circulation
water-cycle stability
natural cooling feedbacks
```

---

## 7. Limitations

This simulation is conceptual.

It does not replace:

```text
global climate models
regional climate models
cloud microphysics models
radiative transfer models
atmospheric chemistry models
health impact models
agricultural impact models
governance and legal assessments
```

Its purpose is to prevent SAI from being evaluated too narrowly.

---

## 8. Recommended Use

This model can be used as:

```text
a public explanation tool
a policy checklist
a scenario comparison framework
a Cooling Credit exclusion test
a preliminary risk-screening tool
a teaching model for climate intervention risks
```

It should not be used to justify deployment.

---

## 9. Core Conclusion

A scenario that reduces sunlight but fails to restore planetary circulation should not be called cooling.

SAI may be a shading intervention.

But shading is not cooling.

Cooling means restoring planetary circulation.

---

## License

CC BY 4.0
