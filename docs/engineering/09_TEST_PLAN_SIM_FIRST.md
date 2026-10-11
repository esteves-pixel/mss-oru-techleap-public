# 09 — Verification & Test Plan (Simulation-First)

## Strategy

**Simulation-first** reduces cost and schedule risk before hardware freeze:

1. Digital twin / kinematics of grapple–transfer–install (using published CAD assumptions)  
2. Sensor/algorithm SIL (software-in-the-loop)  
3. Breadboard sensors + edge compute  
4. Mechanical interface fit checks (3D print / plate)  
5. Environmental tests later (Phase 2/3)  

## Verification matrix (excerpt)

| FR | Method | Early evidence | Later evidence |
|----|--------|----------------|----------------|
| FR-01 CrossLink | Inspection + CAD fit | Print/fit check | Flight hardware |
| FR-02 Install | Sim + fit | Digital twin sequence | Robotic ground demo if available |
| FR-03 Reconfig | Sim + ops script | Twin multi-site | Ground manipulator demo |
| FR-04 Sensing | Test | Lab noise floor | TVAC if required |
| FR-05 Edge AI | Test | SIL anomaly inject | Flight-like data |
| FR-06 Explainability | Test | Unit tests | Ops review |
| FR-07 Rad | Analysis | Parts + analysis | Facility (as funded) |
| FR-08 Degraded | Test | Fault inject SIL | Hardware fault inject |
| FR-09 Self-heal explore | Analysis/test | Coupon lab | Optional flight coupon |
| FR-10 Budgets | Analysis | Spreadsheet vs FFR limits | Mass properties report |
| FR-11 Safety | Analysis/review | Hazard list | Provider review |

## Simulation scenarios (first set)

| ID | Scenario | Pass criteria |
|----|----------|---------------|
| SIM-01 | Grapple approach & capture (kinematic) | No collision with stated keep-outs |
| SIM-02 | Transfer path delivery → deck | Continuous clear path under assumptions |
| SIM-03 | Mate to deck interface | Alignment within capture envelope |
| SIM-04 | Power-on sequence | Mode INIT→BASELINE |
| SIM-05 | Anomaly injection (vib/thermal) | Flag + explainability fields present |
| SIM-06 | Channel loss | DEGRADED mode; product continues |
| SIM-07 | Remove & reinstall site B | UC-03 complete in script |

## Ground test pyramid

```
        /\
       /E2E\      (robotic interface demo — when resources allow)
      /------\
     /  HWIL  \
    /----------\
   /  SIL / twin \
  /--------------\
 / unit & analysis \
```

## Phase alignment

| Competition phase | Test focus |
|-------------------|------------|
| Phase 1 (now) | Sim-first plan, analysis, budgets, risk mitigations |
| Phase 2 | Final design, interface compatibility evidence, early prototype |
| Phase 3 | Full build, flight-condition testing, risk mitigations live |

## Metrics for “test success” (feeds Potential Impact)

- SIM scenarios SIM-01…07 pass under baselined assumptions  
- Edge model detects injected anomalies with quantified TPR/FPR on ground dataset  
- Degraded mode demonstrated with ≥N channels removed  
- Mass/power within limits with documented margin  
