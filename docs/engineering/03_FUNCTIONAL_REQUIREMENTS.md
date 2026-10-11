# 03 — Functional Requirements (FR-01 … FR-11)

**Status:** Draft for Phase 1. Refine numbers when FFR limits are locked.  
**Traceability:** Each FR maps to ConOps phases and to verification methods in `09_TEST_PLAN_SIM_FIRST.md`.

| ID | Requirement | Rationale | Priority |
|----|-------------|-----------|----------|
| **FR-01** | MSS-ORU shall provide a **passive CrossLink** grapple interface compatible with the FFR arm active CrossLink end effector. | Arm grapple is mandatory for challenge ConOps. | Must |
| **FR-02** | MSS-ORU shall be installable on at least one FFR **separable deck interface** (FuseBlox, iSSI, or CrossLink as baselined) without EVA. | On-orbit install is core value. | Must |
| **FR-03** | The system shall support arm **transfer from delivery vehicle to FFR** and subsequent **remove / reinstall** at a second location (or equivalent reconfiguration demo). | Proves reconfigurability; manipulation essential. | Must |
| **FR-04** | While installed (and when powered via host or arm path), MSS-ORU shall acquire **external sensing data** relevant to structural/thermal/vibratory health of the host or local interface region. | Continuous external sensing need. | Must |
| **FR-05** | The payload shall run an **onboard edge processing chain** producing compact features and anomaly indicators (not raw-only streaming as sole product). | Unknown downlink; early detection. | Must |
| **FR-06** | Anomaly outputs shall include **explainability metadata** (e.g., contributing features, sensor channel IDs, confidence). | Operator trust; ISAM ops. | Should |
| **FR-07** | MSS-ORU shall tolerate the **radiation and space environment** expected for LEO-class hosted flight per stated assumptions, with design for **graceful degradation**. | Survival + reliability. | Must |
| **FR-08** | On partial sensor or compute failure, the system shall continue to provide **reduced-capability health products** rather than hard fail-silent where feasible. | Anti-fragile / graceful degradation. | Must |
| **FR-09** | Design shall **explore** self-healing or damage-tolerant material options for non-critical outer layers without basing primary mission success solely on unproven self-heal. | Innovation + honesty on TRL. | Should / Explore |
| **FR-10** | Mass, volume, power, and data interfaces shall remain within **FFR/ORU published limits** and team-stated assumptions; exceedances require documented waiver path. | Compatibility. | Must |
| **FR-11** | Safety: payload shall not present uncontrolled free-flying hazard after release; shall support arm safing and host constraints for force/thermal/EMI as required by flight provider. | Integration & safety. | Must |

## Derived / quantitative requirements

| Parameter | Locked working target | Source to lock / verify |
|-----------|----------------------|-------------------------|
| Mass (kg) | **≤ 12.5 kg** (SOURCE challenge SWaP); design ≈ 11.1 kg | Official max; CAD confirm envelope |
| Volume / envelope | Match ORU form factor in FFR pack | FFR CAD |
| Average power — sensing (W) | **≤ 20–40 W** (team baseline) | Host + arm EE power capability |
| Peak power (W) | **≤ 50–80 W** (team baseline) | Same |
| Sensor suite (minimum) | **Visual + thermal + vibration** | FR-04 |
| Data rate | Event-driven + periodic summary | Downlink unknown → store-and-forward |
| Lifetime (demo) | Mission duration TBD — design for months-class LEO | Flight provider |

> If official FFR limits are tighter than team targets, **official limits win**.

## Non-functional qualities

- **Modularity:** ORU-class, replaceable  
- **Observability:** health of sensors themselves (BIT)  
- **Assumptions transparency:** all TBD orbit parameters listed in application  
- **SE rigor:** requirements → architecture → verification traceability  
