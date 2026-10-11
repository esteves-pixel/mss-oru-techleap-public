# 10 — Mass & Power Budgets (Refined)

**Date:** 27 July 2026; **SWaP rebaseline 11 Aug 2026**  
**Baseline:** `docs/LOCKED_BASELINE.md` + `docs/engineering/11_SWAP_THERMAL_POWER.md`  
**Interfaces:** D-01 (CrossLink grapple + iSSI install)  
**Official mass max (SOURCE):** **12.5 kg** — supersedes prior 15–25 kg team band for claims.

---

## Source legend

| Tag | Meaning |
|-----|---------|
| **SOURCE** | From TechLeap guidelines, Motiv FFR pack text, or owner locked baseline |
| **ASSUMPTION** | Engineering judgment; assumption ID required |
| **DERIVED** | Calculated from other rows |

---

## 1. Envelope & ceilings

| Parameter | Value | Tag | Notes |
|-----------|-------|-----|-------|
| **Official max payload mass** | **12.5 kg** | **SOURCE** | Challenge SWaP — **hard NTE** |
| **Design-point mass (CBE + margin)** | **11.10 kg** | DERIVED | See §2 rebaseline; residual 1.4 kg to ceiling |
| Mass growth margin (held) | ~15% of CBE **inside** 12.5 kg | ASSUMPTION A-B-02 | Never claim above 12.5 |
| Max CBE target | **≤ 11.0 kg** | DERIVED | 9.65 kg CBE current allocation |
| Team peak power ceiling | ≤ 50–80 W | ASSUMPTION | Owner legacy; **interface rating wins** |
| **iSSI continuous hard cap (SOURCE)** | **24 V × 3 A = 72 W** | SOURCE | Official separable IF rating — **wins when seated on iSSI** |
| CrossLink RA rail cap | 28 V × 3 A = 84 W | SOURCE | Grappled / CrossLink path |
| **Design-point peak** | **65 W** | ASSUMPTION A-B-03 | Below iSSI 72 W cap |
| Team average sensing | ≤ 20–40 W | ASSUMPTION | Owner legacy |
| **Design-point MONITOR avg** | **28 W** | ASSUMPTION A-B-04 | Under 72 W; heaters extra duty-cycled |
| FFR host max continuous power | Unknown | ASSUMPTION A-B-05 | Duty-cycle if host < 28 W |
| FFR ORU max mass (official) | **12.5 kg** | **SOURCE** | A-B-06 closed by challenge SWaP text |
| Stowed cross-section | Within **proposed IF** max cross-section | SOURCE | Prefer iSSI; confirm FFR CAD |
| Height | Limited by **passive CrossLink** vs arm workspace | SOURCE | Coupled constraint |
| Deployed volume | State max; limits TBD | SOURCE | Baseline: V_deployed = V_stowed |
| Thermal | **Isolated from bus** (no conduction) | SOURCE | `11_SWAP_THERMAL_POWER.md` |
| Power gap | Bus **OFF** before arm pass-through **ON** | SOURCE | Unknown duration unpowered |
| Arm EE power/data when grappled | Available (capability stated) | SOURCE | Only after bus off + gap |
| Downlink daily volume | Unknown | ASSUMPTION A-B-07 | Store-and-forward; event packets |

### Compatibility check

| Check | Design point | Ceiling | Result |
|-------|--------------|---------|--------|
| Mass total | **11.10 kg** | **12.5 kg SOURCE** | **PASS** |
| Peak power | 65 W | 72 W iSSI | **PASS** |
| MONITOR average | 28 W | 72 W iSSI | **PASS** (heaters duty-managed) |

---

## 2. Mass budget (design point **11.10 kg** incl. margin) — **≤ 12.5 kg SOURCE**

### Allocation philosophy

- **Hard NTE:** **12.5 kg** (challenge SOURCE).  
- **CBE** = sum of line items; **margin ~15% of CBE held inside ceiling**.  
- **Canonical detail:** `11_SWAP_THERMAL_POWER.md`  
- **Obsolete:** 15–25 kg band and ~15 kg design claims — **do not use in application**.

| ID | Item | CBE (kg) | Tag / basis |
|----|------|----------|-------------|
| M-01 | Primary structure / chassis | 2.40 | Lightweight hybrid |
| M-02 | Passive CrossLink ×2 + hardware | 1.40 | Dual face retained |
| M-03 | iSSI assembly + bracket | 1.20 | Preferred park IF |
| M-04 | FuseBlox | **0.00** | Not on flight unit mass |
| M-05 | Visual camera + lens + baffle | 0.45 | |
| M-06 | Thermal IR | 0.35 | |
| M-07 | Vibration suite | 0.30 | |
| M-08 | Harness / connectors | 0.65 | Dual power path |
| M-09 | Edge compute | 0.40 | MCU-class preferred |
| M-10 | Power conditioning + hold-up | 0.85 | Bus/arm + **power-gap** shutdown |
| M-11 | Thermal (MLI / isolation / heaters) | 0.90 | **Bus-isolated** thermal |
| M-12 | Rad provisions | 0.25 | Spot only |
| M-13 | Fasteners / misc | 0.30 | |
| M-14 | Self-heal coupons | **0.00** | Off mass-critical path |
| M-15 | Launch covers | 0.20 | |
| | **CBE subtotal** | **9.65** | |
| M-16 | **System margin (~15%)** | **1.45** | Inside 12.5 kg |
| | **Total design mass** | **11.10** | |
| | **Official max** | **12.5** | Residual +1.40 kg |

### Mass interpretation

| Metric | Value | Notes |
|--------|-------|-------|
| CBE | 9.65 kg | Current best estimate |
| CBE + margin | **11.10 kg** | Application design mass |
| Official max | **12.5 kg SOURCE** | **PASS** |
| Residual to ceiling | 1.40 kg | Adapter / ICD growth only |

> **Application statement:** Maximum mass **≤ 12.5 kg**; design total **≈ 11.1 kg** including margin.

---

## 3. Power budget

### Modes

| Mode | Description | Avg (W) | Peak (W) | Duty notes |
|------|-------------|---------|----------|------------|
| **SAFE** | Watchdog, minimal HK | **3** | 5 | ASSUMPTION A-P-01 |
| **INIT / BASELINE** | Sensor warm-up, cal | **20** | 40 | Short duration A-P-02 |
| **MONITOR** | Periodic sense + light features | **28** | 45 | Design-point avg A-B-04 |
| **INFERENCE_BURST** | Edge model run | **35** (during burst) | **55** | ≤10% duty in MONITOR hour A-P-03 |
| **DIAG_GRAPPLE** | Arm-powered diagnostic suite | **40** | **65** | Peak at design-point peak A-B-03 |
| **Not-to-exceed** | Hard stop | — | **80** | SOURCE team ceiling |

### MONITOR mode breakdown (28 W average)

| Subsystem | Avg (W) | Tag |
|-----------|---------|-----|
| Visual (duty-cycled imaging) | 8.0 | A-P-10 |
| Thermal sensor | 2.5 | A-P-11 |
| Vibration acquisition | 1.5 | A-P-12 |
| Edge compute idle + feature extract | 6.0 | A-P-13 |
| Inference amortized | 3.5 | A-P-14 (bursts averaged) |
| Power conversion loss (~15%) | 3.5 | A-P-15 |
| Comms / interface manager | 2.0 | A-P-16 |
| Margin in mode | 1.0 | A-P-17 |
| **Total** | **28.0** | DERIVED |

### Peak stack-up (DIAG_GRAPPLE / worst case)

| Contributor | W | Notes |
|-------------|---|-------|
| All sensors on | 18 | Continuous |
| Compute full | 20 | SOM class |
| Conversion loss | 8 | |
| Heaters contingency | 10 | Cold case only |
| **Peak** | **56–65** | Within 80 W; heaters optional |

### Power compatibility

| Condition | Response |
|-----------|----------|
| Host continuous < 28 W (A-B-05) | Reduce visual FPS; MONITOR target 18–22 W |
| Arm EE only (grappled) | DIAG_GRAPPLE profile; no heaters |
| Peak limited to 50 W | Cap compute; descope simultaneous full-rate visual |

---

## 4. Data / energy products (for twin & Phase 1 metrics)

| Product | Typical size | Tag |
|---------|--------------|-----|
| Housekeeping packet | 64–128 B | A-D-01 |
| Feature vector summary | 0.5–2 kB | A-D-02 |
| Anomaly event + explainability | 1–4 kB | A-D-03 |
| Raw visual snippet (rare) | 50–200 kB | A-D-04 only if downlink allows |

---

## 5. Assumption register (budgets)

| ID | Statement |
|----|-----------|
| A-B-01 | Early midpoints (18 kg / 15.01 kg) **obsolete**; design total **≈11.1 kg** under official **12.5 kg** NTE |
| A-B-02 | Hold ~15% mass margin on CBE **inside** 12.5 kg ceiling |
| A-B-03 | Design peak 65 W; iSSI continuous hard cap 72 W wins when seated |
| A-B-04 | MONITOR average ~28 W; heaters duty-managed inside IF power |
| A-B-05 | Host continuous power may be below 28 W — duty cycle required |
| A-B-06 | Official max **12.5 kg** from challenge SWaP — closed; CAD bolt patterns still TBR |
| A-B-07 | Downlink limited — compact products mandatory |
| A-M-01…15 | Line-item masses are pre-CAD estimates |
| A-P-01…17 | Power line items pre-breadboard |
| A-ARM-01 | Lower mass preferred until arm handling limits published |
| A-IF-* | See D-01 |

---

## 6. Open verification actions

1. Pull numeric ORU mass/CG and power pins from FFR CAD / later ICD → replace A-B-06.  
2. Confirm iSSI power pins capability for 28 W continuous.  
3. Update CBE after first CAD pass (Phase 2).  
4. Feed design-point values into digital twin config (`twin/config.py`).  

---

## 7. One-line summary for proposals

> MSS-ORU design mass is **≈ 11.1 kg including margin** (CBE ≈ 9.65 kg), under the official **12.5 kg** maximum; MONITOR average **~28 W** and peak **≤65 W**, continuous **≤72 W** on iSSI; thermal **bus-isolated**; **power gap** between bus off and arm pass-through on is designed for (SAFE/NVM).
