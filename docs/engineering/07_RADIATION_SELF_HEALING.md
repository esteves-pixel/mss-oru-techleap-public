# 07 — Radiation Hardening + Self-Healing / Anti-Fragile

## Mandatory: radiation tolerance & environment survival

MSS-ORU shall be designed for LEO-class hosted flight under **stated assumptions** (orbit TBD by flight provider). Design includes:

| Measure | Intent |
|---------|--------|
| Parts selection | Prefer rad-tolerant / screened COTS with derating |
| EDAC / watchdog / brownout | Soft-error and SEFI recovery |
| Shielding where mass-effective | Reduce total dose on compute |
| Thermal-vac design | Survival extremes |
| EMI / ESD practices | Host compatibility |
| Graceful degradation | FR-07, FR-08 |

**Mission success does not require zero faults** — it requires predictable degraded service and clear telemetry.

## Design goals: anti-fragile posture

1. **Graceful degradation** of sensing/compute  
2. **Localized damage tolerance** of outer structure/skin  
3. **Modularity** — replace ORU rather than entire host  
4. **Learning path** — post-flight materials coupons if flown  

## Self-healing / materials exploration (not sole success path)

Exploration targets (literature / lab path; TRL honesty required in Phase 1):

| Family | Why interesting | Risk |
|--------|-----------------|------|
| Self-healing PDMS | Soft skin, puncture recovery concepts | Space environment durability |
| Poly(urea)urethanes | Intrinsic heal chemistry | Outgassing, thermal |
| Microcapsule systems | Autonomous fill of microcracks | One-shot heal, manufacturing |
| Dynamic impact polymers | Energy dissipation | Qualification unknowns |
| “Harnessing Harshness” approaches | Use environment (thermal cycles, radiation-assisted chemistry) as heal driver | Research-stage |

### Framing for judges

- **Primary:** rad-aware electronics + FDIR + modular replaceability  
- **Secondary / innovative:** materials coupons or non-critical outer layer concepts that **explore** self-healing  
- Do **not** base critical load paths or primary interfaces on unproven self-heal  

## Test implications

- Radiation: analysis + parts pedigree + optional facility test later phases  
- Materials: coupon characterization on ground; optional flight exposure  
- Fault injection in software-in-the-loop for degraded modes  

## Traceability

FR-07, FR-08, FR-09; UC-05.
