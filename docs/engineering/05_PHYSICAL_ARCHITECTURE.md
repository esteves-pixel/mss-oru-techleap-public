# 05 — Physical Architecture

## System context

```
[Delivery vehicle] --transfer--> [FFR Arm / CrossLink EE]
                                      |
                                      v
                              [MSS-ORU (ORU-class)]
                               /        |        \
              [CrossLink ×2 grapple] [iSSI install] [Sensing skin]
                                      |
                                      v
                              [FFR payload deck]
```

## ORU-class module breakdown

| Subsystem | Function | Notes |
|-----------|----------|-------|
| Structure / chassis | Primary load path, launch locks compatibility | Match FFR ORU envelope |
| Grapple interface | **Passive CrossLink ×2** | D-01; arm EE compatible |
| Deck install interface | **iSSI** primary; FuseBlox optional | D-01 |
| Power conditioning | Host and/or arm EE power | Input protection, sequencing |
| Data interface | Host/arm protocol as published | TBD exact stack from FFR docs |
| Sensor suite | **Visual + thermal + vibration** (minimum) | Low mass, LEO capable |
| Edge compute | Feature extraction + anomaly model | Power-aware; ~28 W MONITOR |
| Thermal control | Passive preferred | Active heaters only if required |
| Rad / fault tolerance | Shielding as practical, EDAC, watchdogs | Graceful degradation |
| Outer skin / coupons | Damage-tolerant / self-heal **exploration** | Non-critical; ~0.2 kg |

## Interface baseline (D-01)

| Role | Interface |
|------|-----------|
| Grapple | Passive CrossLink Cleat ×2 |
| Deck install | iSSI |
| Optional | FuseBlox Passive |

Detail: `docs/engineering/D01_INTERFACE_DECISION.md`

## Mass / power budgets (refined)

Full tables: **`docs/engineering/10_BUDGETS.md`**

| Parameter | Refined design point | Team ceiling | Status |
|-----------|---------------------|--------------|--------|
| **Mass (CBE + margin)** | **≈ 11.1 kg** (CBE ≈ 9.65 kg) | **≤ 12.5 kg SOURCE** | PASS — see `11_SWAP_THERMAL_POWER.md` |
| **MONITOR average power** | **~28 W** | 20–40 W | PASS |
| **Peak power** | **≤65 W** (NTE 80 W) | 50–80 W | PASS |
| **SAFE average** | ~3 W | — | Design |

### Mass allocation (CBE ~13.1 kg)

| Item | CBE (kg) |
|------|----------|
| Structure + CrossLink×2 + iSSI + FuseBlox opt. | ~7.5 |
| Sensors + harness | ~2.3 |
| Compute + power electronics | ~1.2 |
| Thermal + rad + misc + coupons | ~2.1 |
| **System margin 15%** | **~2.0** |
| **Total** | **≈11.1 kg design (≤12.5 kg NTE)** — see `10_BUDGETS.md` / `11_SWAP_THERMAL_POWER.md` |

### Power modes

| Mode | Avg (W) | Peak (W) |
|------|---------|----------|
| SAFE | 3 | 5 |
| INIT/BASELINE | 20 | 40 |
| MONITOR | 28 | 45 |
| INFERENCE_BURST | 35 | 55 |
| DIAG_GRAPPLE | 40 | 65 |

## Launch and on-orbit survival

- Design to LEO thermal cycling, vacuum, radiation (assumption table).  
- Launch loads: use flight provider envelope when assigned; interim rideshare-class assumptions flagged.  
- MMOD: sacrificial/self-heal coupons optional; electronics behind structure.

## Reliability / graceful degradation

1. Multi-modal sensing (visual / thermal / vibration).  
2. BIT per sensor class.  
3. FDIR: channel drop → DEGRADED → continue products.  
4. Watchdog, brownout, EDAC as applicable.  
5. Hard fail → arm removes/replaces ORU.

## Open architecture decisions

| ID | Status |
|----|--------|
| D-01 interfaces | **Baselined** |
| D-02 sensors | **Locked** visual+thermal+vibration |
| D-03 edge compute class | Open — power envelope supports SOM or strong MCU |
