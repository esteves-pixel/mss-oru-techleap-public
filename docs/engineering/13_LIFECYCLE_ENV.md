# 13 — Lifecycle Environments & Survival (Transport → EOM)

**Status:** First consolidated lifecycle analysis **12 Aug 2026**  
**Honest limit:** Prior work covered phases in ConOps, hold paths, SWaP/thermal, and radiation **assumptions** separately. This document **unifies** them. It is **not** a finished ICD-driven LCA (LV and FFR orbit still TBD). It is the rigorous baseline for Phase 1 claims and Phase 2 verification.

**Related:** `11_SWAP_THERMAL_POWER.md`, `12_ENV_SAFETY_EMI.md`, `01_CONOPS.md`, D-01  

---

## 1. Technical Guidelines — what is actually said (harsh reading)

| Guideline theme | What is published | What is **not** published | Our precision rule |
|-----------------|-------------------|---------------------------|--------------------|
| Radiation | Survive **LEO** thermal and radiation for mission duration; **TID not available** — state your own assumptions | Orbit, inclination, duration, solar cycle, TID/SEE spectra, shielding maps | Split **TID** vs **SEE**; never say only “radiation hardened” |
| Thermal | Survive LEO thermal; **isolated from bus** (no conduction); manage within IF power | Hot/cold case sink temps, orbit | MLI + heaters + isolation; power-gap = no heaters |
| Mechanical / launch | Survive launch loads | Exact LV, PSD, shock, acoustic | Bounding rideshare-class until LV ICD |
| Transport / ground | Implicit in range/LV compliance | Ground transport g, handling loads | Logistics cases A-LC-* |
| Debris / EOM | No debris hazard; retain deployables | Host disposal plan details | Passivation + no free parts |
| Power | Interface ratings; bus off before arm on | Gap duration | Dual-rail POWER_GAP/SAFE |

**Harsh truth:** Broad phrases like “survive radiation” are **not a design basis**. We treat them as **requirement shells** we must fill with **A-RAD / A-STR / A-LC** assumptions and burn them down when ICDs arrive.

---

## 2. Radiation — precise (not “radiation” as one blob)

### 2.1 Environment class

| Item | Assumption | Tag |
|------|------------|-----|
| Regime | **LEO** only (not GEO/MEO/HEO) | A-RAD-01 |
| Orbit | Altitude/inclination **TBD** with FFR | A-RAD-01b |
| Duration for design | **≤ 1 year** equivalent LEO exposure for Phase 1 design envelope (actual demo may be shorter) | A-RAD-02d |

### 2.2 Effects we design for (split)

| Mechanism | What it does | Design response |
|-----------|--------------|-----------------|
| **TID** (total ionizing dose) — cumulative trapped e⁻/p⁺ (and secondary) | Gradual parametric shift, oxide damage | Design TID **≤ 5 krad(Si)** behind **~2–3 mm Al-eq** (ASSUMPTION A-RAD-02); derating; spot shield on edge compute if needed |
| **SEE — SEU** (single-event upset) | Bit flips in memory/logic | EDAC / scrub; critical state in NVM; CRC products |
| **SEE — SEL** (single-event latch-up) | Destructive or high-current state | Current limit; power-cycle recovery; watchdog |
| **SEE — SEFI** | Functional interrupt | FDIR → DEGRADED/SAFE; restart |
| **DDD** (displacement damage) | Sensor/opto degradation | Prefer robust sensors; monitor BIT; accept reduced performance in DEGRADED |
| **Solar particle events** | Rare high flux | Not sized as primary design driver for short LEO demo; SAFE hold if host commands (A-RAD-08) |

**We do not claim:** full rad-hard parts list, GEO survival, or “immune to radiation.”

### 2.3 Lifecycle radiation exposure (qualitative)

| Phase | Radiation relevance | Response |
|-------|---------------------|----------|
| Ground transport / storage | Negligible space dose; ESD/humidity dominate | Handling controls (A-EMI ESD) |
| Launch / ascent | Short; not TID driver | Survive vibe/shock (A-STR-*) |
| LEO ops (installed + reconfig) | **Primary TID + SEE window** | A-RAD-02…07; DEGRADED/SAFE |
| Power gap (bus off / arm off) | SEE can still occur; no active cooling/heaters | Cold-safe; NVM state; no false MONITOR |
| End of mission / safed remove | Residual dose already accumulated | Passivation; no new emitters |

---

## 3. Lifecycle analysis (LCA) — phases and survival

### Lifecycle map

```
L0 Ground logistics (factory → range)
  → L1 Integration on delivery vehicle (stowed, launch locks)
    → L2 Launch / ascent / early orbit
      → L3 Rendezvous / arm transfer (CrossLink grapple)
        → L4 Install + commission (iSSI preferred)
          → L5 On-orbit MONITOR / reconfig / DIAG (ops)
            → L6 End of demo / passivation / remove or host dispose
```

| ID | Phase | Dominant environments | How MSS-ORU survives / complies |
|----|-------|----------------------|--------------------------------|
| **L0** | Transport & handling | Shock from shipping, ESD, temperature of logistics chain | Shipping container/foam per LV/user guide (TBR); captive hardware; ESD procedures; no loose covers |
| **L1** | Stowed on delivery vehicle | Launch locks, fairing thermal, pre-launch power-off or trickle per ICD | Positive restraint (A-STR-01); V_stowed within IF envelope; mass ≤12.5 kg; optics protected |
| **L2** | Launch & ascent | Quasi-static g, random vibe, sine, shock, acoustic | A-STR-02…06 bounding until LV ICD; first mode >50 Hz target; sensor isolation |
| **L3** | Arm transfer | Grapple loads, possible EE power/data, **bus off before arm on** (power gap) | Capture BIT; CrossLink only; POWER_GAP/SAFE + NVM; hold-up for graceful shutdown only |
| **L4** | Install & commission | Mate loads, bus power restore, thermal isolation starts “on orbit self-managed” | Install BIT gate; INIT→BASELINE→MONITOR; MLI/heaters within IF power |
| **L5** | Operations | LEO thermal cycling, TID/SEE, limited downlink, reconfig arm loads, power-gap on every bus↔arm switch | Dual rail; DEGRADED/SAFE; explainable products; multi-site reconfig; no free deployables |
| **L6** | End of operation | Host disposal / arm remove; passivation | Inhibit emitters; bleed hold-up; SAFE; captive hardware; support host OD plan |

### Was lifecycle analysis done before?

| Element | Before 12 Aug | Now |
|---------|---------------|-----|
| ConOps phases | Yes (01_CONOPS) | Mapped into L0–L6 |
| Hold / grapple / install paths | Yes (12_ENV §2) | Included |
| Launch load assumptions | Yes (bounding) | Included |
| Thermal isolation + power gap | Yes (11_SWAP) | Included |
| Radiation split TID/SEE | Partial (A-RAD table) | Expanded here |
| **Transport (L0) explicit** | **Weak** | Added |
| **Single end-to-end LCA table** | **No** | **This document** |
| ICD-final numbers | No | Still TBR Phase 2 |

---

## 4. Application language (harsh + precise)

**Radiation:**  
*The guidelines do not publish a TID. MSS-ORU does not treat “radiation” as a single checkbox. We design for LEO with (i) cumulative TID ≤5 krad(Si) behind ~2–3 mm Al-eq for a ≤1-year-class envelope (TBR when orbit is known), and (ii) SEE mitigation (EDAC, latch-up control, watchdogs, DEGRADED/SAFE). We do not claim GEO hardness or unlimited solar-particle survival.*

**Lifecycle:**  
*Survival is defined phase-by-phase from ground transport through launch stowage, ascent, arm transfer (including mandatory power-off gaps), installed operations, and end-of-demo passivation/remove—not a single “space environment” claim.*

---

## 5. Phase 2 burndown (to close assumptions)

1. LV ICD → replace A-STR bounding loads  
2. FFR orbit/duration → re-run TID  
3. Ground transport spec → L0 test cases  
4. Power-gap max duration from host → A-PG-03  
5. Qual/protoflight test matrix by lifecycle phase  

---

## Traceability

- Form: Overview “Meets” / Other considerations; Development status  
- FR-07, FR-08, FR-11  
- Demo D-01…D-09 (ops phases L3–L6)  
