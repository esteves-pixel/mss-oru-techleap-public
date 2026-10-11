# 04 — Use Cases (UC-01 … UC-06)

## UC-01 — Robotic transfer and first install

**Actor:** FFR arm, MSS-ORU, delivery vehicle, FFR deck  
**Trigger:** Delivery vehicle in capture range; ops go for transfer  
**Flow:** Arm grapples CrossLink → vehicle release → transfer → install on deck interface → power-on → baseline sense  
**Success:** ORU secured; first health product generated  
**Manipulation role:** Essential (cannot self-transfer)

## UC-02 — Continuous external health monitoring

**Actor:** MSS-ORU (installed), ground/guest ops  
**Trigger:** Commissioning complete  
**Flow:** Periodic sensing → feature extraction → anomaly check → store/prioritize downlink  
**Success:** Continuous coverage without EVA for the monitoring period  
**Manipulation role:** Indirect (install enabled by arm); sets up UC-03

## UC-03 — Multi-site reconfiguration (inspection geometry)

**Actor:** FFR arm, MSS-ORU  
**Trigger:** Command to relocate monitoring to second interface / pose  
**Flow:** Arm grapples → remove from site A → install at site B → re-baseline → compare features A vs B  
**Success:** Second-site products valid; demonstrates reconfigurable ISAM monitoring  
**Manipulation role:** Essential

## UC-04 — Arm-powered diagnostic grapple

**Actor:** FFR arm end effector (power/data through EE), MSS-ORU  
**Trigger:** Ops requests powered interaction while grappled  
**Flow:** Arm grapples; power/data path active; MSS-ORU runs accelerated diagnostic suite  
**Success:** Diagnostic package produced while grappled  
**Manipulation role:** Essential (and differentiates from fixed host power only)

## UC-05 — Graceful degradation under channel loss

**Actor:** MSS-ORU onboard FDIR  
**Trigger:** Sensor channel or compute subunit failure (radiation, wear, impact)  
**Flow:** Detect fault → isolate → degrade mode → continue reduced product with flag  
**Success:** No silent failure; operators see mode change  
**Manipulation role:** Optional recovery (arm replace ORU if hard fail)

## UC-06 — End-of-demo remove and safing

**Actor:** FFR arm, host ops  
**Trigger:** Demo complete or contingency  
**Flow:** Arm removes ORU → stow or return path → safing  
**Success:** Deck free; ORU safe  
**Manipulation role:** Essential for modular logistics story

## Mapping to challenge example demos

| Challenge example | MSS-ORU mapping |
|-------------------|-----------------|
| Robotic inspection and diagnostics | UC-02, UC-04 |
| Modular payload swapping | UC-03, UC-06 |
| Sensor deployment | UC-01 (place sensing asset) |
| Material processing | Optional coupon on skin (explore) |
