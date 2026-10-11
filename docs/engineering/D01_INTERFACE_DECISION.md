# D-01 — Interface Baseline Decision Record

**Status:** BASELINED (Phase 1 engineering) — **refreshed 11 Aug 2026** with official FFR separable-interface power/data ratings  
**Owner:** Gonçalo Esteves  
**Authority:** FFR Payload Separable Interfaces (challenge text); Motiv *FFR Data for Tech Leap*; TechLeap technical guidelines  

---

## Hard rules from challenge (non-negotiable)

1. **Arm ↔ payload only through CrossLink.**  
   There is **no secondary grasping** point. The Motiv arm interfaces with a payload **only** via its **active CrossLink** end effector. Therefore the payload **must** provide **Passive CrossLink** for every grapple, transfer, reorient, diagnostic hold, and remove.

2. **Separable deck interface is mandatory** for mechanical docking to FFR and for the hosted power/data path when installed. NASA provides **one of** CrossLink Cleat (passive) / **iSSI** / FuseBlox (passive). Teams may **prefer**; **final assignment is Phase 2** (preference + NASA assessment).

3. **Passive interfaces do not initiate docking** (CrossLink Cleat, FuseBlox). Docking is driven by the mating **active** side — account for this in the demonstration plan.

4. **Power-draw limit** on a given interface = that interface’s **documented power rating** (below).

5. **Optional payload arm/actuators** are allowed if described. **MSS-ORU choice: none** — no extra arm; keeps mass, failure modes, and safing simple. Actuation = interface mate/demate + internal sensor/BIT only.

6. Delivery-vehicle interface: select a stow/capture approach; **no separate docking structure required** for the delivery vehicle beyond challenge norms — we use **Passive CrossLink** geometry consistent with arm capture from the vehicle.

---

## Decision (what we prefer and why)

| Role | Interface | On payload | Why |
|------|-----------|------------|-----|
| **Grapple / manipulation (mandatory)** | **Passive CrossLink Cleat ×2** | Yes (primary + secondary face) | Only legal arm attachment; enables D-01…D-09 demos; dual face reduces single-point grapple geometry risk |
| **Deck install (preferred — ask NASA)** | **iSSI (active on ORU side as needed)** | Yes | Gigabit Ethernet + regulated 24 V for continuous MONITOR + edge AI; does **not** consume the scarce deck CrossLink reserved for the arm; clean split **manipulate vs park** |
| **Deck alternate (if NASA assigns)** | **FuseBlox (passive)** | Design-ready alternate | Also Gigabit Ethernet; keep as Phase 2 fallback |
| **Deck non-preferred** | CrossLink Cleat as **park** primary | Avoid as sole park path | Only **one** free deck CrossLink (one always reserved for arm); data = **RS422 only** — too thin for vision/AI products; blurs arm walking reservation vs guest ORU |

### Locked statement for application

> **MSS-ORU preferred interfaces:**  
> (1) **Passive CrossLink** for all robotic arm interaction (mandatory, non-substitutable; Motiv CAD shows **×2** on ORU).  
> (2) **iSSI** as preferred FFR **separable deck** interface — Motiv Tech Leap CAD **post-ORU-move** diagram places the ORU at **iSSI**; power/data for continuous sensing.  
> (3) **FuseBlox** retained as alternate if Phase 2 assignment differs.  
> (4) **No** payload-borne robotic arm or external actuators beyond interface mating.  
> Final deck interface per NASA Phase 2 assignment; design holds adapters (CAD notes **bolt patterns subject to change**).

---

## Official interface card (SOURCE — challenge text)

| | **CrossLink Cleat (passive)** | **iSSI (active)** | **FuseBlox (passive)** |
|--|-------------------------------|-------------------|------------------------|
| Deck footprint | 172 × 111 mm | 145 × 49 mm | 100 × 100 × 40 mm |
| Deck positions | **2** ( **1 reserved for arm always** ) | **1** | **1** |
| Mates with | Active CrossLink (arm EE) | iSSI passive or active | FuseBlox active |
| Power | **28 V @ 3 A** (RA) ≈ **84 W**; heater 24–32 V @ 3 A; chassis GND | **24 V @ 3 A** ≈ **72 W**; heater 24–32 V @ 3 A | **24–32 V unregulated @ 3 A** |
| Data | **2× RS422** + ESTOP | **Gigabit Ethernet** | **Gigabit Ethernet** |
| Docking | Passive — does not initiate | Active system | Passive — does not initiate |
| **MSS role** | **Grapple only** (on ORU); not preferred as sole park | **Preferred park / install** | **Alternate park** |

### Compatibility with MSS power design

| Mode | Design draw | vs iSSI 72 W | vs CrossLink RA 84 W | vs FuseBlox ~72–96 W |
|------|-------------|--------------|----------------------|----------------------|
| MONITOR avg | ~28 W | **OK** (margin) | OK | OK |
| Peak design | ≤65 W | **OK** | OK | OK |
| Team NTE | 80 W | **Over iSSI 72 W** if ever hit | OK on CrossLink rail | Depends regulation |

**Action:** hard-cap continuous draw **≤ 24 V × 3 A (72 W)** when on iSSI; peak bursts duty-cycled; heater rail separate for thermal. Update budgets so **interface rating wins over team NTE 80 W** when installed on iSSI.

---

## Why iSSI is preferred for “keep all function working”

MSS-ORU functions that must stay alive when **installed**:

| Function | Needs | Best interface support |
|----------|-------|------------------------|
| Visual sensing + feature products | Bandwidth | **GbE (iSSI / FuseBlox)** — not RS422 |
| Thermal + vibration streams | Modest BW + continuous power | All; Ethernet preferred for time-sync products |
| Edge physical-AI think/act | Continuous compute power ~28 W avg | iSSI 72 W continuous OK |
| Explainable event packets store-and-forward | Host data path | GbE |
| Multi-site reconfig demo | Arm grapple **while** deck interface free for re-mate | CrossLink grapple **independent** of iSSI park |
| Multi-cell growth later | Multiple park sites without stealing arm’s CrossLink | iSSI/FuseBlox style deck slots |

**CrossLink-as-park would starve the product:** RS422 cannot honestly carry vision-class health products; and using the only free deck CrossLink competes with arm mobility architecture.

**Split architecture is the key to all functions:**

```
MANIPULATION path:  Arm active CrossLink  ↔  ORU Passive CrossLink
PARK / SENSE path:  Deck iSSI (preferred) ↔  ORU iSSI side
DIAG path:          Arm EE power/data while grappled (when available)
```

If either path fails, the other still supports a degraded demo (see failure modes).

---

## Comparison matrix (selection)

| Criterion | CrossLink park | **iSSI park** | FuseBlox park |
|-----------|----------------|---------------|---------------|
| Arm grapple | Required anyway | Required anyway | Required anyway |
| Continuous vision/AI products | **Weak** (RS422) | **Strong** (GbE) | **Strong** (GbE) |
| Power headroom vs 28 W MONITOR | Strong (84 W) | Strong (72 W) | Strong if regulated |
| Power regulation | RA 28 V | 24 V regulated | **Unregulated** — more PSU risk |
| Deck scarcity | **High** (1 free) | One dedicated guest slot | One dedicated guest slot |
| Multi-cell later | **Poor** | Better | Better |
| Passive docking caveat | Yes | Active system | Yes |
| Aligns prior D-01 / Motiv 3rd-party story | Partial | **Yes** | Partial |
| **Phase 1 preference** | No | **Yes** | Alternate |

---

## Failure modes driven by interface choice

### Shared (any deck choice)

| ID | Failure mode | Keep-function response |
|----|--------------|------------------------|
| **FM-IF-01** | Grapple CrossLink miss / incomplete mate | Capture BIT interlock; no vehicle release (D-01) |
| **FM-IF-02** | Single grapple geometry blocked | Second Passive CrossLink face; alternate approach |
| **FM-IF-03** | Bolt pattern / ICD change | Adapter plates; late bind Phase 2 |
| **FM-IF-04** | Arm EE power/data absent while grappled | DIAG_GRAPPLE degraded; park path carries MONITOR |
| **FM-IF-05** | Phase 2 NASA assigns non-preferred deck IF | Ship dual-ready (iSSI primary + FuseBlox alternate) |
| **FM-IF-06** | No secondary grasp (rule) | Never design “handle” demos; all demos CrossLink-legal |

### iSSI-primary specific

| ID | Failure mode | Keep-function response |
|----|--------------|------------------------|
| **FM-IF-10** | iSSI mate incomplete | Install BIT; no MONITOR until pass; arm holds or retries |
| **FM-IF-11** | Exceed **72 W** continuous on iSSI | Hard power governor; visual duty-cycle; peak ≤65 W budgeted |
| **FM-IF-12** | GbE link down | Fall back compact RS-class summary if available via other path; else store onboard; raise TASK_DIAG / replace |
| **FM-IF-13** | iSSI active mechanism anomaly | Safe demate procedure; arm remove via CrossLink |

### If forced to FuseBlox

| ID | Failure mode | Keep-function response |
|----|--------------|------------------------|
| **FM-IF-20** | Unregulated bus sag/spike | Input conditioning; brownout DETECT → DEGRADED |
| **FM-IF-21** | Passive dock — mate driven by active side | Demo plan accounts for active mate drive; BIT on seat |

### If forced to CrossLink park (non-preferred)

| ID | Failure mode | Keep-function response |
|----|--------------|------------------------|
| **FM-IF-30** | Only one free deck CrossLink | Single-site park; multi-cell deferred; reconfig still via grapple+reseat |
| **FM-IF-31** | RS422 bandwidth starves vision products | Shift to heavy onboard feature compression; **accept product-class descope**; prefer re-negotiate iSSI/FuseBlox |
| **FM-IF-32** | Conflicts with arm’s reserved CrossLink | Ops keep-outs; never occupy arm-reserved seat |

---

## Alternatives considered (record)

| Option | Pros | Cons | Outcome |
|--------|------|------|---------|
| Deck park = CrossLink only | Same family as grapple; 84 W | RS422; scarce deck seat; blurs arm reservation | **Rejected as preferred** |
| Deck park = FuseBlox only | GbE; small | Unregulated power; passive dock | **Alternate** |
| Deck park = iSSI | GbE; 24 V; dedicated seat; 3rd-party story | 72 W hard cap; active IF complexity | **Preferred** |
| Payload-owned mini-arm | Could point sensors | Mass, safing, challenge complexity | **Rejected** — arm is Motiv’s |
| No CrossLink on ORU | — | Illegal — arm cannot manipulate | **Forbidden** |

---

## Assumptions (interface)

| ID | Assumption | If wrong |
|----|------------|----------|
| A-IF-01 | Active CrossLink EE mates published Passive CrossLink geometry | Adapter redesign |
| A-IF-02 | NASA accepts **iSSI preference** or assigns FuseBlox | Execute FuseBlox alternate kit |
| A-IF-03 | Two CrossLink passives fit envelope without collision | Drop to one + careful vector |
| A-IF-04 | Bolt patterns may change | Late-binding adapters |
| A-IF-05 | Arm EE power/data while grappled as guidelines state | DIAG uses host only |
| A-IF-06 | Installed MONITOR ≤ 28 W continuous on **24 V / 3 A** iSSI | Duty-cycle visual first |
| A-IF-07 | GbE available on iSSI/FuseBlox when seated | Feature-only products + store-and-forward |
| A-IF-08 | Delivery vehicle capture uses CrossLink-compatible geometry | Confirm Phase 2 vehicle ICD |

---

## Phase 1 application language (short)

**Preferred interface:** iSSI for FFR deck docking; Passive CrossLink Cleat (×2) for all Motiv arm manipulation.  
**Alternate:** FuseBlox if assigned.  
**Not preferred as park:** deck CrossLink Cleat (data + scarcity).  
**No** additional payload robotic arm.  
**Power:** respect interface ratings (iSSI continuous ≤ 72 W).  
**Demo:** measurement-gated mates on both CrossLink grapple and iSSI park; passive A→B carriage invalid.

---

## Traceability

- FR-01, FR-02, FR-03, FR-10, FR-11  
- UC-01, UC-03, UC-04, UC-06  
- Demo D-01…D-09  
- Phase 1: `docs/phase1/TECHNICAL_DESIGN.md`, `TECHNOLOGY_ALIGNMENT.md`  
- Budgets: `10_BUDGETS.md` (cap to interface rating)  
