# 11 — SWaP, Thermal Isolation, and Power Sequencing

**Status:** SOURCE-aligned rebaseline **11 Aug 2026**  
**Authority:** Challenge SWaP text + interface power ratings + thermal/power sequencing notes  
**Supersedes:** prior team mass band 15–25 kg and design mass ~15 kg for **flight envelope claims**

---

## 1. Size, weight, and power (SWaP) — official

| Requirement | Official statement | MSS-ORU design response |
|-------------|--------------------|-------------------------|
| **Cross-section** | Must fall within **maximum cross-sections** for the **proposed interface** (FFR Payload Separable Interfaces doc) | Prefer **iSSI**: stowed envelope designed inside iSSI allowable cross-section; confirm CAD with FFR before freeze |
| **Height** | Allowable height depends on **ORU passive CrossLink Cleat placement** vs **arm workspace** | CrossLink faces + height envelope treated as coupled constraint; twin keep-outs; Phase 2 FFR confirmation |
| **Mass** | **Maximum payload mass = 12.5 kg** | **Hard not-to-exceed: 12.5 kg.** Design CBE + margin ≤ 12.5 kg. Prior 15–25 kg team band is **obsolete for claims**. |
| **Min volume / smallest dim** | **Not specified** | No artificial min volume; optimize for mass and interfaces |
| **Volume limit** | Applies to **stowed configuration only** | State **stowed volume** and **max deployed volume** separately |
| **Deployables** | During demonstration, may exceed stowed volume if deployables; **precise limits not yet defined** | Prefer **minimal/no deployables** for Phase 1 risk; if any (e.g. baffle, coupon panel), declare max deployed volume and accept FFR confirmation |
| **Confirmation** | Winning teams confirm configuration with FFR team before final design | Explicit assumption A-SWaP-01: Phase 2 FFR configuration review |

### Stowed vs deployed (application language)

| State | Definition | MSS-ORU intent |
|-------|------------|----------------|
| **Stowed** | Delivery-vehicle / pre-demo envelope | Entire unit within iSSI max cross-section + height allowed by CrossLink placement; **mass ≤ 12.5 kg** |
| **Deployed (demo)** | After arm install / any mechanism motion | **Baseline: no volume growth** (no large deployable boom). Optional micro-features (lens cover release) only; **max deployed volume = stowed volume** unless later approved |
| **Max deployed volume (stated)** | Required by challenge | **V_deployed_max = V_stowed** (no deployable growth) for this application — revisable only with FFR written agreement |

---

## 2. Mass budget rebaseline (≤ 12.5 kg SOURCE)

### Philosophy

- **Hard ceiling:** 12.5 kg (SOURCE) — no waiver language in Phase 1 claims.  
- **Margin:** ≥ 10% of CBE held at system level **inside** 12.5 kg (not above it).  
- **Target:** Total (CBE + margin) ≤ **12.5 kg**; CBE target ≤ **11.0 kg**.  
- **Descopes first:** FuseBlox off flight unit, self-heal coupons off, secondary CrossLink lightened carefully, structure lightweighted.

### Allocation (design point)

| ID | Item | CBE (kg) | Notes |
|----|------|----------|-------|
| M-01 | Primary structure / chassis | 2.40 | Light composite/Al hybrid; cut from 3.40 |
| M-02 | Passive CrossLink ×2 + hardware | 1.40 | Keep dual face; lighter mounts |
| M-03 | iSSI assembly + bracket | 1.20 | Prefer iSSI; no FuseBlox on unit |
| M-04 | FuseBlox | **0.00** | **Not on flight mass** — alternate kit if assigned (separate allocation) |
| M-05 | Visual camera + lens + baffle | 0.45 | |
| M-06 | Thermal IR | 0.35 | |
| M-07 | Vibration suite | 0.30 | |
| M-08 | Harness / connectors | 0.65 | Dual power path + sequencing relays |
| M-09 | Edge compute | 0.40 | MCU-class preferred for mass/power |
| M-10 | Power conditioning + **hold-up** | 0.85 | Dual bus (host/arm) + gap survival (see §4) |
| M-11 | Thermal (MLI / isolation / heaters) | 0.90 | **Isolated from bus** — more self-thermal mass |
| M-12 | Rad provisions | 0.25 | Spot only |
| M-13 | Fasteners / misc | 0.30 | |
| M-14 | Self-heal coupons | **0.00** | Off critical mass; optional later if mass free |
| M-15 | Launch covers | 0.20 | |
| | **CBE subtotal** | **9.65** | |
| M-16 | **System margin (~15% of CBE)** | **1.45** | Held inside ceiling |
| | **Total design mass** | **11.10 kg** | |
| | **Official max** | **12.5 kg** | **1.40 kg residual to ceiling** |

| Check | Value | Result |
|-------|-------|--------|
| Design total vs 12.5 kg | 11.10 ≤ 12.5 | **PASS** |
| Residual growth to ceiling | +1.40 kg | Interface/adapter growth only |
| Prior claim ~15 kg | — | **SUPERSEDED — do not use in application** |

### Mass descope ladder (if CBE creeps)

1. Drop secondary CrossLink face → single grapple face (−0.3 to −0.5 kg) — last resort for demo geometry  
2. Smaller visual camera  
3. MCU-only (no SOM)  
4. Thin structure further (with strength analysis)  
5. Never claim > 12.5 kg  

---

## 3. Thermal — NASA-sensitive (state assumptions explicitly)

### Official requirements (paraphrased with force)

1. **Assume thermal isolation from the spacecraft bus — no conduction path to the platform.**  
2. **Manage own thermal environment within the interface power-draw limit.** Hot/cold case temperatures **not available** (no orbit/vehicle selected). Assume **blanket and/or heaters** may be required to hold the required temperature range, **within interface power**. **State assumptions in the application.**  
3. (Power sequencing — §4.)

### Design assumptions (A-TH-*) — paste-ready

| ID | Assumption | Rationale |
|----|------------|-----------|
| **A-TH-01** | Payload is **thermally isolated** from FFR bus: **no designed conduction path** through structure to the platform (interface thermal break / isolation as required). | Challenge requirement 1 |
| **A-TH-02** | Heat rejection is **radiation-dominated** (MLI / coatings / radiator area on ORU exterior), not bus-sinking. | Follows A-TH-01 |
| **A-TH-03** | Hot- and cold-case sink temperatures **unknown**; design uses **bounding LEO-class** analysis cases until orbit is assigned, then re-verify. | Challenge: not available yet |
| **A-TH-04** | **MLI blanket** (or equivalent multi-layer insulation) is baseline for cold survival and hot protection. | Challenge allows blanket |
| **A-TH-05** | **Heaters** (survival + ops) are included in the power budget and **count against interface power rating** when that path is live. | Challenge requirement 2 |
| **A-TH-06** | Heater allocation when on **iSSI**: from heater rail if available (**24–32 V @ 3 A** per interface card) **and/or** from main 24 V @ 3 A budget by duty cycle — **never exceed published interface rating**. | Official IF ratings |
| **A-TH-07** | Component operating range (ASSUMPTION until parts freeze): electronics **−20 °C to +50 °C** ops; survival **−30 °C to +60 °C** with heaters/MLI — **TBR** at PDR. | Placeholder for application honesty |
| **A-TH-08** | During **power gap** (§4), **no heater power** is available; thermal inertia + MLI must bridge the gap or accept cold-safe non-op state. | Sequencing reality |
| **A-TH-09** | No claim of bus as thermal capacitor or heat sink. | Anti-bully clarity |

### Thermal architecture (keep function)

```
ORU internal dissipation (sensors, AI, PSU)
    → conduction within ORU only
    → radiation via outer surfaces / MLI openings
    ✗ no conduction to FFR bus (isolated)

Cold: MLI + survival heaters (when powered)
Hot:  coatings / radiator area + power duty-cycle (reduce visual first)
Gap:  unpowered; rely on thermal mass + MLI; SAFE state
```

### Thermal failure modes

| ID | Failure mode | Response |
|----|--------------|----------|
| **FM-TH-01** | Cold exceedance (no bus heat) | Heaters when powered; MLI; widen parts selection |
| **FM-TH-02** | Heater power starves MONITOR | Priority: survival heaters > MONITOR visual; duty-cycle sensing |
| **FM-TH-03** | Hot case, isolated ORU | Reduce dissipation; throttle AI/visual; coatings |
| **FM-TH-04** | Long power gap → cold soak | Design gap survival duration assumption A-PG-03; non-op cold-safe |
| **FM-TH-05** | Accidental thermal short to bus | Mechanical isolation design review; non-conformance if coupled |

---

## 4. Power sequencing — the “power out” trap (critical)

### Official requirement (clear language)

> **Bus power will need to be turned off before the arm power pass-through is turned on.**  
> Timing is **not known**. There will be **some amount of power off** required of the payload.

### What this means operationally

| Phase | Host/deck bus (e.g. iSSI) | Arm EE pass-through | Payload sees |
|-------|---------------------------|---------------------|--------------|
| Parked MONITOR | **ON** | OFF | Continuous power from bus |
| **Pre-grapple transition** | **OFF** (required) | Still OFF | **POWER GAP — unpowered** |
| Grappled DIAG / transfer assist | OFF | **ON** | Power from arm path only |
| **Pre-release / re-seat transition** | Still OFF or transitioning | **OFF** | **POWER GAP again** |
| Re-parked MONITOR | **ON** | OFF | Bus power restored |

**There is no seamless handoff.** Any design that assumes “always at least one of bus or arm is on” is **wrong**.

### Design rules (A-PG-* power gap)

| ID | Rule |
|----|------|
| **A-PG-01** | Payload implements **two mutually exclusive power inputs**: `PWR_BUS` (deck IF) and `PWR_ARM` (CrossLink EE pass-through), with **break-before-make** behavior matching host policy. |
| **A-PG-02** | On loss of input power, payload enters **POWER_GAP / SAFE** within hold-up time: stop non-essential loads, flush critical state to **non-volatile memory**, open outputs safe. |
| **A-PG-03** | **Gap duration unknown.** Design assumption for Phase 1: survive **≥ 5 minutes** unpowered without damage (cold-safe); re-acquire within **≤ 2 minutes** after power restore (TBR with FFR). Longer gaps → non-op survival only. |
| **A-PG-04** | **No heater power during gap.** Thermal design must not require continuous heat through the gap (A-TH-08). |
| **A-PG-05** | Hold-up energy (capacitors / short UPS) sized for **graceful shutdown only** (seconds class), **not** full MONITOR through the gap. |
| **A-PG-06** | After power restore (bus or arm), autonomous **INIT → BIT → last mode or SAFE** recovery; do not assume RAM state survived. |
| **A-PG-07** | Demo plan **never** schedules a measurement that requires power during the mandatory off window. |
| **A-PG-08** | TASK_REQUEST / arm cues generated **before** planned bus-off when possible; or after arm power is stable. |

### Power state machine (explicit)

```
MONITOR (PWR_BUS)
  → cmd: prepare grapple
  → BUS_OFF_WARNING (if provided) / detect undervoltage
  → POWER_GAP (unpowered SAFE)
  → PWR_ARM on
  → DIAG_GRAPPLE or TRANSFER_KEEPALIVE (if arm power present)
  → PWR_ARM off
  → POWER_GAP
  → PWR_BUS on
  → INIT → BIT → MONITOR or DEGRADED
```

### Power-gap failure modes

| ID | Failure mode | Mitigation |
|----|--------------|------------|
| **FM-PG-01** | Brownout corruption | Brownout detect; NVM flush; CRC configs |
| **FM-PG-02** | Gap longer than thermal survival | Cold-safe parts; accept non-op; no false MONITOR claims |
| **FM-PG-03** | Both sources on (forbidden overlap) | Break-before-make OR-ing; backfeed protection |
| **FM-PG-04** | Arm path never comes up after bus off | Timeout → remain SAFE; no thrash; wait bus restore |
| **FM-PG-05** | Demo script ignores gap | D-02/D-07 only when arm power stable; D-05 only when bus stable |

### Hold-up vs survival (do not confuse)

| Energy store | Purpose | Duration class |
|--------------|---------|----------------|
| Capacitance / short hold-up | Orderly shutdown, NVM write | **Seconds** |
| MLI + thermal mass | Temperature bridge unpowered | **Minutes** (assumed; TBR) |
| Battery | **Not baselined** (mass/safety) unless later approved | — |

---

## 5. Combined SWaP–thermal–power “keep function” summary

| Function | Constraint | How we keep it |
|----------|------------|----------------|
| Fit interface | Cross-section + CrossLink height | iSSI envelope + CrossLink workspace analysis |
| Mass | **≤ 12.5 kg** | 11.10 kg design with margin; FuseBlox off unit |
| Sense + AI when parked | iSSI ≤ 72 W; thermal self-managed | MONITOR ~28 W + heater duty inside rating |
| Sense when grappled | Arm path power; bus off | DIAG only on arm rail; reduced suite if needed |
| Survive transitions | **Power gap mandatory** | SAFE + NVM + thermal isolation survival |
| No bus heat sink | Isolation | MLI + heaters (when powered) |

---

## 6. Application paste block (NASA-clear)

**SWaP.** MSS-ORU stowed configuration will comply with the maximum cross-sections for the preferred **iSSI** separable interface and with height constraints imposed by **passive CrossLink Cleat** placement relative to the arm workspace. **Maximum mass ≤ 12.5 kg** (design total ≈ 11.1 kg including margin). No minimum volume is assumed. **Volume limit is applied to the stowed configuration**; **maximum deployed volume is stated equal to stowed volume** (no large deployables). Precise deployable exceedance limits are acknowledged as undefined; configuration will be confirmed with the FFR team before design freeze.

**Thermal.** The payload is designed as **thermally isolated from the spacecraft bus with no conduction path to the platform**. The team will manage the thermal environment **within the interface power-draw limit**. Because hot- and cold-case temperatures are not yet available, we assume LEO-class bounding cases, **MLI blanketing**, and **heaters** as required to hold the stated temperature range, with heater and electronics power **summed inside the iSSI (or assigned interface) rating**. Assumptions A-TH-01…09 are recorded in the engineering package.

**Power sequencing.** We design for the requirement that **bus power is turned off before arm power pass-through is turned on**, with an **unknown-duration power-off interval**. The payload implements dual power inputs with **break-before-make**, **POWER_GAP/SAFE** behavior, non-volatile state preservation, short hold-up for graceful shutdown only, and thermal survival without heaters during the gap. Demonstration steps that need power are scheduled only on a **stable** bus or arm rail—not during the mandatory off window.

---

## Traceability

- Phase 1: Technical Design, Alignment, Impact (mass numbers), Project Plan  
- Budgets: `10_BUDGETS.md` (align numbers to this file)  
- D-01 interfaces  
- Demo D-01…D-09 (power-stable gates)  
- Risk register: add FM-TH-*, FM-PG-*, mass 12.5  
