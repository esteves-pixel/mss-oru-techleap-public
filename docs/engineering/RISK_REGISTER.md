# Risk Register — MSS-ORU / TechLeap

**Date:** 27 July 2026  
**Owner:** Gonçalo Esteves  
**Scale:** Likelihood / Impact = L (Low) · M (Medium) · H (High)  
**Residual:** After planned mitigations  

| ID | Risk | L | I | Mitigation | Owner | Residual | Related |
|----|------|---|---|------------|-------|----------|---------|
| R-01 | iSSI / CrossLink bolt patterns change (FFR drawings mark subject to change) | M | H | Adapter plates; late-binding mounts; track Motiv revisions; D-01 dual-path note | GE | M | D-01, FR-01/02 |
| R-02 | Mass exceeds **12.5 kg** official max | M | H | Design 11.1 kg; descope ladder; no FuseBlox on unit | GE | L | SWaP SOURCE |
| R-19 | Thermal isolation + unknown hot/cold cases | M | H | MLI + heaters inside IF power; LEO bounding; no bus conduction claim | GE | M | A-TH-* |
| R-20 | **Power gap** bus-off before arm-on (duration unknown) | H | H | Dual rail break-before-make; SAFE/NVM; hold-up seconds only; demo not during gap | GE | M | A-PG-* |
| R-03 | Arm workspace / force / CG limits unpublished — demo infeasible | M | H | Parameterized twin; stay mid-mass; state A-ARM assumptions; conservative paths | GE | M | SIM-01…03 |
| R-04 | Host continuous power < MONITOR budget | M | M | Duty-cycle visual; sleep modes; 18–22 W fallback profile | GE | L | A-B-05 |
| R-05 | Arm EE power/data path not available for DIAG_GRAPPLE | L | M | UC-04 becomes host-only; still pass install/reconfig demos | GE | L | A-IF-05 |
| R-06 | Downlink too small for useful products | M | M | Feature/anomaly packets ≤4 kB; store-and-forward; no raw-stream baseline | GE | L | A-B-07, FR-05 |
| R-07 | False alarms / missed anomalies on orbit | M | M | Conservative thresholds; explainability; ground twin calibration; human-in-loop | GE | M | FR-05/06 |
| R-08 | Radiation SEU / SEFI upsets edge compute | M | M | Watchdog, EDAC, SAFE mode, graceful degradation FR-08 | GE | M | FR-07/08 |
| R-09 | Schedule pressure (solo/small team) to 12 Aug + later phases | H | H | Sim-first; COTS; freeze D-01; Phase 1 vs 2 scope cut lines | GE | M | Project plan |
| R-10 | Self-healing claims overreach TRL | M | M | Exploration/coupons only; mission success independent of self-heal | GE | L | FR-09 |
| R-11 | Interface snag / collision during grapple | L | H | Twin keep-outs; approach corridor; edge radius; ops procedures | GE | L | SIM-01, FR-11 |
| R-12 | Free-flyer hazard after release failure | L | H | Positive capture confirmation; safing interlocks; provider rules | GE | L | FR-11 |
| R-13 | Sensor channel hard fail | M | M | Multi-modal suite; DEGRADED mode continues products | GE | L | FR-08, SIM-06 |
| R-14 | Thermal design insufficient (unknown sink) | M | M | Passive thermal; optional heaters within peak; assumption log | GE | M | A-P heaters |
| R-15 | Cannot complete multi-site reconfig in ops time | M | H | Scripted SIM-07; minimum one remove+install; pre-declare alternate reorient-only | GE | M | FDM-4, UC-03 |
| R-16 | Competition scoring: manipulation seen as peripheral | L | H | ConOps + metrics force arm-causal value; never fixed-only story | GE | L | Evaluation criteria |
| R-17 | Partner/vendor delay on mechanical interfaces | M | M | 3D-print fit checks; dual-source fasteners; early drawing package | GE | M | Phase 2 |
| R-18 | Budget overrun post-award | M | M | COTS sensors; 15% cost contingency; descope FuseBlox/coupons | GE | M | Project plan |

## Top risks (watch list)

1. **R-09** Schedule / team capacity  
2. **R-02 / R-03** Unknown official FFR limits & arm handling  
3. **R-01** Interface pattern volatility  
4. **R-15** Multi-site demo ops feasibility  
5. **R-07** On-orbit anomaly performance  

## Risk burndown actions (near term)

| Action | Closes toward | When |
|--------|---------------|------|
| Extract FFR CAD mass/power pins | R-02, R-03 | This week |
| Run twin SIM-01…07 (done in repo) | R-03, R-11, R-15 | Now |
| Freeze D-01 in proposal text | R-01, R-16 | Phase 1 submit |
| Breadboard power measurement | R-04, R-07 | Phase 2 start |
