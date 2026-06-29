# SAI Risk Assessment Model

## A Scoring Framework for Stratospheric Aerosol Injection Risk Evaluation

This document defines a simplified risk assessment model for Stratospheric Aerosol Injection (SAI).

The purpose is not to predict the real climate system.

The purpose is to provide a transparent, modular, and extensible scoring framework that highlights the hidden risk categories often excluded when SAI is treated only as a sunlight-reflection method.

---

## 1. Core Principle

SAI should not be evaluated only by expected radiative forcing or global mean temperature reduction.

It must also be evaluated as an intervention into:

```text
existing atmospheric particle systems
wet deposition and rainfall cleaning
surface particle fixation
resuspension from dry surfaces
cloud formation
rainfall distribution
water-cycle stability
soil moisture
evapotranspiration
agriculture
human health
ocean systems
governance
termination shock
natural cooling feedbacks
```

The model therefore treats SAI risk as a multi-factor system score.

---

## 2. Risk Categories

The model uses ten risk dimensions.

Each dimension is scored from 0.0 to 1.0.

```text
0.0 = low risk or well-controlled
0.5 = moderate risk or uncertain control
1.0 = high risk or severe uncertainty
```

### R1. Existing Atmospheric Particle Load

Measures whether the atmosphere is already highly loaded with particles such as dust, smoke, soot, PM2.5, pollen, sea salt, and mixed aerosols.

### R2. Vertical Layering Uncertainty

Measures uncertainty about how existing particle layers interact with proposed SAI layers in the upper troposphere and stratosphere.

### R3. Wet Deposition Weakening

Measures whether rainfall and wet deposition are weakened, localized, or insufficient to remove atmospheric particles.

### R4. Surface Fixation Loss

Measures loss of natural particle traps such as moist soils, wetlands, forests, rivers, lakes, oceans, humus, and vegetated surfaces.

### R5. Resuspension Risk

Measures the likelihood that deposited particles are lifted again from dry soils, roads, bare land, degraded fields, and urban surfaces.

### R6. Cloud and Rainfall Disruption

Measures the risk that added aerosols alter cloud microphysics, rainfall distribution, monsoon behavior, drought patterns, or regional hydrology.

### R7. Outgoing Heat and Infrared Interaction Risk

Measures whether particle layers may alter outgoing longwave radiation, atmospheric heating, cloud radiative effects, or heat release pathways.

### R8. Natural Cooling Feedback Damage

Measures whether SAI fails to restore or may worsen soil moisture, evapotranspiration, rainfall, wetland recovery, forest cooling, and ocean-atmosphere exchange.

### R9. Governance and Regional Conflict Risk

Measures deployment governance, consent, monitoring, liability, international coordination, and geopolitical conflict risk.

### R10. Termination Shock Risk

Measures the risk of rapid warming if SAI is stopped after masking warming for a period of time.

---

## 3. Weighted Risk Score

A weighted total risk score is calculated as:

```text
Total Risk Score = Σ(weight_i × risk_i)
```

Default weights:

```text
R1 Existing Atmospheric Particle Load: 0.10
R2 Vertical Layering Uncertainty: 0.08
R3 Wet Deposition Weakening: 0.12
R4 Surface Fixation Loss: 0.10
R5 Resuspension Risk: 0.10
R6 Cloud and Rainfall Disruption: 0.14
R7 Outgoing Heat Interaction Risk: 0.08
R8 Natural Cooling Feedback Damage: 0.14
R9 Governance and Regional Conflict Risk: 0.12
R10 Termination Shock Risk: 0.12
```

Weights sum to 1.00.

Cloud/rainfall risk and natural cooling feedback damage are weighted highly because this framework treats cooling as the restoration of planetary circulation, not merely the reduction of incoming sunlight.

---

## 4. Risk Classes

```text
0.00 - 0.20 = Low apparent risk
0.20 - 0.40 = Moderate risk
0.40 - 0.60 = High risk
0.60 - 0.80 = Severe risk
0.80 - 1.00 = Critical risk
```

A high or severe score does not prove that SAI will fail.

It indicates that the system is too uncertain or too degraded to justify treating SAI as a simple cooling intervention.

---

## 5. Cooling Credit Eligibility Filter

Even if a scenario shows apparent temperature reduction, it must pass the Cooling Credit filter.

An intervention is ineligible for Cooling Credit if it fails to restore:

```text
water circulation
soil moisture
evapotranspiration
rain-based atmospheric cleaning
wet deposition
surface particle fixation
forests and wetlands
rivers and oceans
natural cooling feedbacks
```

This filter is binary in the simplified model:

```text
passes_filter = True / False
```

If `passes_filter = False`, the scenario is classified as:

```text
Shading intervention, not Cooling Credit eligible
```

---

## 6. Simulation Scenarios

The simulation uses five default scenarios:

### Scenario A: Low-Risk Research Baseline

A hypothetical scenario with strong monitoring, low particle load, stable rainfall, and no deployment.

### Scenario B: Moderate SAI Research Scenario

Small-scale modeling or observation scenario with no open-air deployment but incomplete knowledge.

### Scenario C: Limited SAI Deployment Scenario

A hypothetical limited deployment under uncertain atmospheric particle and rainfall conditions.

### Scenario D: High-Drying Planet Scenario

A world with strong warming, soil drying, forest loss, wetland loss, weakened rainfall, and high resuspension.

### Scenario E: Poor Governance Deployment Scenario

A scenario with unilateral deployment, weak monitoring, high uncertainty, and high termination shock risk.

---

## 7. Interpretation

The model is intentionally conservative.

It is designed to ask:

```text
What happens if the atmosphere is already particle-loaded?
What happens if rain-cleaning is weakened?
What happens if dry surfaces resuspend particles?
What happens if SAI reduces sunlight but does not restore water-cycle cooling?
What happens if governance fails or deployment stops abruptly?
```

The model does not claim to replace climate models.

It acts as a warning-layer model that identifies missing evaluation dimensions.

---

## 8. Model Limitations

This is a conceptual and educational simulation model.

It does not calculate real atmospheric chemistry, radiative transfer, cloud microphysics, regional circulation, or global climate dynamics.

It should not be used for deployment decisions.

Its role is to clarify that any serious SAI evaluation must include atmospheric particle context, rainfall cleaning, resuspension, natural cooling feedbacks, and governance risk.

---

## 9. Core Warning

> A reduction in incoming sunlight is not equivalent to the restoration of Earth's cooling system.

> Shading is not cooling.  
> Cooling means restoring planetary circulation.

---

## License

CC BY 4.0
