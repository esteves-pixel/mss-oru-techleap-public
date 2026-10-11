# 12 — Environment, Structural Loads, Debris/Safety, EMI/EMC

**Status:** Application-grade assumptions **11 Aug 2026**  
**Authority:** TechLeap additional requirements text; LEO practice; **14 CFR Part 450** (payload-relevant slices); NASA OD mitigation norms  
**Related:** `11_SWAP_THERMAL_POWER.md`, demo D-01…D-09, D-01 interfaces  

---

## 1. Official additional requirements (paraphrased with force)

| # | Requirement | MSS-ORU response (summary) |
|---|-------------|----------------------------|
| A | Survive **launch loads** and **LEO thermal + radiation** for mission duration | Structural + thermal + rad design cases; assumptions stated |
| B | **TID figure not available** — assume LEO; **communicate own radiation assumptions** | A-RAD-* table below |
| C | **No debris hazard**; deployables **tethered or retained** | No free deployables; retention design |
| D | Comply with **range safety** and **LV requirements** for delivery vehicle | Support LV operator / Part 450 payload determination with design data |
| E | **No interference** with FFR or other payloads; **EMI/EMC not published** — assume reasonable compliance and explain | A-EMI-* + design accommodations |

---

## 2. Launch loads, vibration, harmonics, and how the payload is held

### 2.1 Holding architecture (explicit)

MSS-ORU is never “loose mass” in any phase:

| Phase | How it is held | Load path |
|-------|----------------|-----------|
| **On delivery vehicle (stowed)** | Vehicle-provided ORU restraint / launch locks per LV ICD (ASSUMPTION A-STR-01: hard-mounted to vehicle structure via published ORU/adapter interfaces — final ICD Phase 2) | Vehicle → adapter → ORU chassis |
| **Arm grapple / transfer** | **Passive CrossLink ×2** mated to arm **active CrossLink EE**; capture BIT before release from vehicle | Arm EE → CrossLink → chassis |
| **Installed on FFR** | Preferred **iSSI** separable interface (mechanical dock + power/data); arm released after install BIT | Deck IF → iSSI → chassis |
| **Reconfig / DIAG** | CrossLink re-grapple; break-before-make power (see power gap) | Arm EE → CrossLink |
| **End of demo** | Arm demate to stow/return path or remain seated under host rules | Same as above |

**No secondary grasp** (challenge rule): all free-flight-relative handling is CrossLink-only.

### 2.2 Launch / mechanical environments (assumptions — SOURCE TBD by LV)

Exact launch vehicle not frozen. We state **bounding LEO rideshare-class** assumptions until LV ICD arrives, then re-verify:

| ID | Assumption | Design implication |
|----|------------|--------------------|
| **A-STR-01** | Stowed restraint is **positive lock** to vehicle (no rattling free play beyond ICD tolerances) | Interface stiffness; no debris from fasteners |
| **A-STR-02** | Quasi-static design loads (ASSUMPTION): **±10 g** axial / **±6 g** lateral (TBR vs LV ICD) | Structure sized with ≥1.25 yield factor (ASSUMPTION A-STR-07) |
| **A-STR-03** | Random vibration (ASSUMPTION): NASA GEVS-like or LV-provided PSD; design-to **14 gRMS** protoflight envelope class until ICD (TBR) | Board staking, connector strain relief, sensor isolators as needed |
| **A-STR-04** | Sine vibration / harmonics: avoid structural modes coupling to LV or FFR known bands once published; first mode **> 50 Hz** target for primary structure (ASSUMPTION A-STR-08) | FEA modal survey; mass placement |
| **A-STR-05** | Shock (ASSUMPTION): pyrotechnic/separation shock per LV ICD; design shock isolation at sensors | Soft mounts for camera/IMU-class sensors |
| **A-STR-06** | Acoustic: fairing acoustic levels per LV ICD; no fragile open mechanisms | Covers on optics until commissioned |

### 2.3 Vibration & harmonics plan (what we will do)

| Activity | When | Purpose |
|----------|------|---------|
| FEA modal + random vibe prediction | Phase 2 | Show no destructive resonance in stowed config |
| Notching strategy | With LV | Protect over-test without hiding real modes |
| Protoflight / qual vibe test | Phase 2/3 | Workmanship + design verification |
| Sine sweep survey | Qual | Harmonic peaks vs arm/FFR keep-out if provided |
| On-orbit vib sensing | Flight (payload function) | Same sensors used for **health products** also self-monitor install interface |
| Installed stiffness check | After iSSI mate | Install BIT includes coarse vib/thermal sanity |

### 2.4 Failure modes (structural / hold)

| ID | Failure mode | Mitigation |
|----|--------------|------------|
| **FM-STR-01** | Launch restraint failure → free object | Dual fasteners/safety wire or LV-standard capture; design review with LV |
| **FM-STR-02** | CrossLink partial mate under load | Capture BIT; no vehicle release without confirm |
| **FM-STR-03** | Harmonic amplification damages optics | Isolators; first-mode target; covers |
| **FM-STR-04** | Fatigue at deck IF over mission | Margin on iSSI loads; limited reconfig cycles in demo plan |
| **FM-STR-05** | Loose fastener → debris | Captive hardware; threadlocker; FOD control |

---

## 3. LEO thermal and radiation survival

Thermal isolation and power gap: **`11_SWAP_THERMAL_POWER.md`** (do not restate full tables).

### 3.1 Radiation assumptions (TID not published — we state ours)

| ID | Assumption | Basis |
|----|------------|-------|
| **A-RAD-01** | Mission environment = **LEO** (altitude/inclination TBD with FFR) | Challenge text |
| **A-RAD-02** | Design TID (ASSUMPTION): **≤ 5 krad(Si)** behind **~2–3 mm Al-eq** shielding for **≤ 1 year** LEO equivalent (TBR when orbit known) | Conservative smallsat LEO order-of-magnitude; **not** GEO/MEO |
| **A-RAD-03** | SEE: use **SEL latch-up protection** (current limit / power cycle), EDAC on critical memory, watchdog | FR-07/08 |
| **A-RAD-04** | Prefer **auto-grade / industrial** parts with derating; rad-hard only where mass/power budget allows critical nodes | SWaP 12.5 kg |
| **A-RAD-05** | Spot shielding on edge compute if needed | Mass line M-12 |
| **A-RAD-06** | Graceful degradation under SEU: DEGRADED/SAFE modes; no silent fail | FDIR |
| **A-RAD-07** | When official TID/orbit published, **re-run** dose analysis and update parts list | Phase 2 |

**Application sentence:**  
*A total ionizing dose figure is not provided by the challenge. MSS-ORU assumes LEO operation with a design TID of ≤5 krad(Si) behind ~2–3 mm Al-equivalent for up to one year class exposure (TBR), with SEE mitigation via EDAC, watchdogs, latch-up control, and graceful degradation. Assumptions will be updated when FFR orbit is defined.*

---

## 4. Debris hazard, deployables, passivation, conjunction

### 4.1 Debris / deployables (official)

> Payloads must **not** present a debris hazard. Any deployable elements must be **tethered or otherwise retained**.

| Design rule | MSS-ORU |
|-------------|---------|
| Free-flying parts | **Forbidden** |
| Large deployables | **None baselined** (V_deployed = V_stowed) |
| Covers / small releases | If any: **captive** (hinge + tether or retained spring; no jettison) |
| Fasteners | Captive / safety design |
| Failure: demate incomplete | Arm retains via CrossLink; host safing — **no free-flyer** (FR-11, FM-MSN-1/2) |

### 4.2 Passivation (end of useful mission / anomaly)

Though FFR host owns spacecraft-level OD plan, the **payload** shall be passivatable on command or safe-timeout:

| Action | Intent |
|--------|--------|
| Discharge / isolate energy stores | Hold-up caps bleed; **no primary battery baselined** |
| Inhibit RF / high-power emitters | Radios default off; no intentional high-EIRP |
| Safe mechanical state | No stored energy in deployables (none free) |
| Power ports safe | High-Z / inhibited outputs on bus loss |
| Data | Optional final dump then SAFE |

**Application sentence:**  
*MSS-ORU is designed not to generate debris: no untethered deployables, captive hardware, and positive retention in stowed, grappled, and installed states. Passivation is supported by inhibiting emitters, bleeding hold-up energy, and entering SAFE with no free mechanical energy. Spacecraft-level orbital debris mitigation and disposal remain with the FFR / delivery-vehicle operators; the payload will supply mass properties, materials, and safing procedures for their OD plan.*

### 4.3 Conjunction / collision context (payload role)

| Layer | Owner | Payload contribution |
|-------|-------|----------------------|
| Launch/reentry collision avoidance screening | LV / reentry **operator** (e.g. 14 CFR **§450.169**) | Accurate mass, dimensions, timeline, no unexpected separation events |
| On-orbit conjunction assessment | FFR / SSA providers | Stable installed state; **no unplanned free-flyer**; reportable state changes (install/remove) via ops products |
| Payload-caused conjunction risk | Us | Design eliminates unplanned objects; reconfig only under arm control |

**Application sentence:**  
*MSS-ORU will not perform independent propulsive maneuvers. Conjunction risk is managed by host/LV operators; our contribution is a non-separating (except planned arm-handled) object with known mass properties and no debris-generating deployables. Planned reconfigurations are arm-controlled and scheduled with FFR ops.*

---

## 5. Range safety and launch vehicle requirements — Part 450 and honesty

### 5.1 What 14 CFR Part 450 is (correct framing)

**14 CFR Part 450** (*Launch and Reentry License Requirements*) primarily regulates **vehicle operators** seeking an FAA vehicle operator license—not payload developers as licensees.

Payload-relevant pieces typically include:

| Topic | Part 450 pointer (illustrative) | Payload developer duty |
|-------|----------------------------------|------------------------|
| Favorable **payload determination** | **§450.43** | Provide description, dimensions, mass, composition, function, hazards so operator can obtain determination |
| Policy / safety approvals | §§450.41, 450.45 (operator) | Design data packages; hazard reports |
| Collision avoidance analysis | **§450.169** | No surprise separations; accurate physical params |
| Toxic hazards | **§450.139** | MSS-ORU: **no toxic propellants** baselined |
| Flight safety systems | §450.145 etc. | N/A unless we host FSS elements (we do not) |

**We do not claim:** “MSS-ORU is Part 450 licensed” or “we single-handedly satisfy all of Part 450.”  
**We do claim:** design and documentation **support** the delivery vehicle operator’s compliance and **do not preclude** a favorable payload determination.

### 5.2 How we support range / LV compliance

| Area | Commitment |
|------|------------|
| ICD | Comply with **delivery vehicle** payload user’s guide / ICD (TBD Phase 2) |
| Mass properties | Deliver CG, inertia, mass ≤ 12.5 kg |
| Materials | Provide materials list; avoid prohibited materials per LV |
| Hazards | No pressure vessels baselined; no radioactive sources; no toxic propellant; Li chemistry only if later approved with LV rules |
| Frangibility / debris | No planned breakups; captive hardware |
| RF | Coordinate frequencies if any intentional radiator (baseline: **no** radiated RF for primary function; host data path) |
| Ground processing | ESD, FOD, lifting points per LV |

**Application sentence:**  
*MSS-ORU will comply with all range safety and launch vehicle requirements applicable to the delivery vehicle by flowing down the vehicle operator’s ICD and by providing the data needed for FAA **14 CFR Part 450** payload review (**§450.43**) and related operator analyses (including collision-avoidance inputs under **§450.169**). The payload contains no toxic propellants, no planned debris-generating deployments, and no independent propulsion. Final verification is joint with the LV provider and range.*

---

## 6. EMI / EMC (no published FFR numbers — we assume)

### 6.1 Official

> No published EMI/EMC requirements. Assume **reasonable** compliance; **explain design accommodations**. Do not interfere with FFR or other payloads.

### 6.2 Our assumptions (A-EMI-*)

| ID | Assumption |
|----|------------|
| **A-EMI-01** | Host will eventually require **conducted and radiated emissions** limits similar in spirit to **MIL-STD-461G** platform-friendly levels **or** NASA/SMC smallsat EMC guidelines — exact limits TBR |
| **A-EMI-02** | **RE102 / CE102-class** control is a design goal for switching converters and clocks |
| **A-EMI-03** | **Susceptibility:** payload shall not upset at **RS103-class** fields expected for LEO platforms (TBR levels) |
| **A-EMI-04** | **ESD:** handling to **ANSI/ESD S20.20**; flight connectors protected |
| **A-EMI-05** | **No intentional RF transmitter** in baseline payload (data via IF wired paths: GbE / RS422 as assigned) — eliminates many coexistence issues |
| **A-EMI-06** | Switching frequencies chosen and filtered to avoid known GPS/S-band/X-band notches when host publishes keep-outs |
| **A-EMI-07** | Cable shields 360° terminated; partitioned power/analog/digital grounds carefully |
| **A-EMI-08** | Inrush current soft-start on bus connect so we do not brown out shared rails |
| **A-EMI-09** | During arm pass-through power, same EMC hygiene on EE power path |
| **A-EMI-10** | Pre-ship: **CE/RE precompliance** scan; formal test to host-specified limits in Phase 2/3 |

### 6.3 Design accommodations (how we prevent interference)

| Mechanism | Purpose |
|-----------|---------|
| Conducted filtering on `PWR_BUS` and `PWR_ARM` | Protect shared power |
| Soft-start / current limit | Avoid bus dips affecting other payloads |
| Shielded enclosures / compartmentalization | Contain digital noise from edge AI clocks |
| No baseline radio | No radiated carrier competition |
| Clock spread-spectrum (if MCU supports) | Lower peak RE |
| Default SAFE = lowest emissions | Power-gap and fault states quiet |
| Interface common-mode chokes on data lines | Protect GbE/RS422 neighbors |

### 6.4 EMI failure modes

| ID | Mode | Mitigation |
|----|------|------------|
| **FM-EMI-01** | Conducted noise trips host | Filters + soft-start; precompliance |
| **FM-EMI-02** | Radiated noise upsets neighbor | Shielding; no transmitter |
| **FM-EMI-03** | Host field upsets our AI/sensors | Watchdog; DEGRADED; filtering |
| **FM-EMI-04** | Ground loop via dual power paths | Break-before-make; isolation design |

**Application sentence:**  
*No FFR EMI/EMC limits are published. MSS-ORU assumes reasonable platform EMC (MIL-STD-461/NASA smallsat-class intent), implements conducted/radiated control, soft-start power, shielding, and **no intentional RF transmitter** in baseline, and will test to host-specified limits when provided so as not to interfere with FFR systems or co-manifested payloads.*

---

## 7. Application checklist (additional requirements)

- [x] Launch loads + vibe/harmonics + **hold path** described  
- [x] LEO thermal (isolation doc) + radiation **own assumptions**  
- [x] Debris: no free deployables; tether/retain policy  
- [x] Passivation + conjunction **payload role**  
- [x] Range/LV + **Part 450 correct framing** (§450.43 support, not false license claim)  
- [x] EMI/EMC assumptions + accommodations  

---

## Traceability

- Phase 1 Technical Design / master package  
- Shortfalls: `docs/CIVIL_SPACE_SHORTFALLS_TRACEABILITY.md`  
- FR-07, FR-08, FR-11  
