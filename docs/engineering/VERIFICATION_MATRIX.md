# Verification Matrix — FR-01…FR-11

**Date:** 27 July 2026  
**Strategy:** Simulation-first (see `09_TEST_PLAN_SIM_FIRST.md`, `TEST_PLAN_SUMMARY.md`)

| FR-ID | Requirement (short) | Method | Procedure (Phase 1) | Pass criteria | Phase |
|-------|---------------------|--------|---------------------|---------------|-------|
| FR-01 | Passive CrossLink grapple | I, A, S | CAD/twin grapple geometry vs published cleat; SIM-01 | Capture success; no keep-out violation | 1→3 |
| FR-02 | Deck install (iSSI) | S, I | SIM-03 mate; drawing compliance checklist | Alignment within capture envelope A-SIM-03 | 1→3 |
| FR-03 | Transfer + reinstall site B | S | SIM-02, SIM-07 sequence scripts | Full cycle complete; arm-causal | 1→3 |
| FR-04 | Visual+thermal+vibration sense | T, S | Sensor models in twin; lab noise later | All three channels produce samples in MONITOR | 1→3 |
| FR-05 | Edge features + anomaly | T, S | SIL pipeline; SIM-05 | Anomaly score + compact product | 1→3 |
| FR-06 | Explainability metadata | T | Unit test on product schema; SIM-05 | channel_ids, top_features, confidence present | 1→2 |
| FR-07 | Rad / environment tolerance | A | Parts pedigree + analysis note | Documented assumption + approach | 1→3 |
| FR-08 | Graceful degradation | T, S | SIM-06 channel loss | DEGRADED mode; product continues | 1→3 |
| FR-09 | Self-heal exploration | A, T | Coupon plan only | No critical path dependence | 1→2 |
| FR-10 | Mass/volume/power limits | A | `10_BUDGETS.md` vs team + FFR when known | Mass ≤25 kg band; peak ≤80 W; margins held | 1→3 |
| FR-11 | Safety / no free-flyer | A, R | Hazard list; capture confirmation logic | Hazards identified; mitigations listed | 1→3 |

**Methods:** T=Test, A=Analysis, I=Inspection, S=Simulation/Demonstration, R=Review

## SIM cross-map

| SIM | Primary FRs |
|-----|-------------|
| SIM-01 | FR-01, FR-11 |
| SIM-02 | FR-03, FR-11 |
| SIM-03 | FR-02, FR-01 |
| SIM-04 | FR-04, FR-05 |
| SIM-05 | FR-05, FR-06 |
| SIM-06 | FR-08 |
| SIM-07 | FR-03, FR-02 |
