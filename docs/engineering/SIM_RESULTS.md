# SIM Results — MSS-ORU Digital Twin

**Generated (UTC):** 2026-08-12T05:36:41.787520+00:00  
**Twin version:** 0.1.0  
**Interfaces:** grapple=Passive CrossLink x2; install=iSSI  
**Mass design:** 15.01 kg · **MONITOR:** 28.0 W · **Peak:** 65.0 W  

## Summary

| Total | Passed | All pass | Failed |
|-------|--------|----------|--------|
| 7 | 7 | **PASS** | — |

## Budget check (config)

- Mass design ≤ team max: **PASS** (15.01 ≤ 25.0 kg)
- Peak ≤ NTE: **PASS** (65.0 ≤ 80.0 W)

## Scenario results

### SIM-01 — Grapple approach & capture

**Result:** PASS  
**Criteria:** No collision with keep-outs; capture within tolerance

```json
{
  "pass": true,
  "path_clear": true,
  "within_reach": true,
  "max_range_m": 0.8491,
  "capture_success": true,
  "pos_error_m": 0.005,
  "att_error_deg": 1.0,
  "collisions": [],
  "notes": [
    "waypoints=5 samples=81",
    "A-ARM-02 reach_limit=1.2 m max_range=0.849 m",
    "capture_tol_pos=0.015 m att=5.0 deg",
    "A-IF-01 CrossLink capture modeled as tolerance check only"
  ]
}
```

### SIM-02 — Transfer path delivery → deck

**Result:** PASS  
**Criteria:** Continuous clear path under assumptions

```json
{
  "pass": true,
  "path_clear": true,
  "within_reach": true,
  "max_range_m": 0.8139,
  "collisions": [],
  "notes": [
    "waypoints=4 samples=61",
    "A-ARM-02 reach_limit=1.2 m max_range=0.814 m"
  ]
}
```

### SIM-03 — Mate to deck interface (iSSI)

**Result:** PASS  
**Criteria:** Alignment within capture envelope (A-SIM-03)

```json
{
  "pass": true,
  "lateral_error_m": 0.004,
  "tilt_error_deg": 2.0,
  "notes": [
    "A-SIM-03 envelope lateral\u22640.01 m tilt\u22645.0 deg",
    "D-01 primary deck install = iSSI"
  ]
}
```

### SIM-04 — Power-on sequence

**Result:** PASS  
**Criteria:** Mode INIT→BASELINE (then MONITOR ready)

```json
{
  "pass": true,
  "mode_sequence": [
    "INIT",
    "BASELINE",
    "MONITOR"
  ],
  "notes": [
    "Mode machine INIT\u2192BASELINE\u2192MONITOR"
  ]
}
```

### SIM-05 — Anomaly injection (vib/thermal)

**Result:** PASS  
**Criteria:** Flag + explainability fields present

```json
{
  "pass": true,
  "is_anomaly": true,
  "anomaly_score": 202.345,
  "mode": "ANOMALY",
  "explainability": {
    "top_features": [
      {
        "name": "thermal_std",
        "z": 202.345
      },
      {
        "name": "vibration_std",
        "z": 104.699
      },
      {
        "name": "vibration_rms",
        "z": 104.699
      },
      {
        "name": "vibration_p2p",
        "z": 92.608
      },
      {
        "name": "thermal_p2p",
        "z": 65.339
      }
    ],
    "channel_ids": [
      "visual_proxy",
      "thermal",
      "vibration"
    ],
    "confidence": 1.0,
    "threshold": 3.0,
    "anomaly_score": 202.345,
    "mode": "ANOMALY"
  },
  "packet_bytes": 2048,
  "injected": [
    "thermal:4.0",
    "vibration:0.8"
  ]
}
```

### SIM-06 — Channel loss (visual disabled)

**Result:** PASS  
**Criteria:** DEGRADED mode; product continues

```json
{
  "pass": true,
  "mode": "DEGRADED",
  "channels_used": [
    "thermal",
    "vibration"
  ],
  "packet_bytes": 1024,
  "product_continues": true,
  "notes": [
    "channel_loss_detected"
  ]
}
```

### SIM-07 — Remove & reinstall site B

**Result:** PASS  
**Criteria:** UC-03 complete in script (remove A → install B + sense)

```json
{
  "pass": true,
  "path_clear": true,
  "within_reach": true,
  "max_range_m": 0.2345,
  "mate_site_b": true,
  "post_install_product_bytes": 1024,
  "collisions": [],
  "notes": [
    "waypoints=5 samples=81",
    "A-ARM-02 reach_limit=1.2 m max_range=0.235 m",
    "A-SIM-03 envelope lateral\u22640.01 m tilt\u22645.0 deg",
    "D-01 primary deck install = iSSI",
    "UC-03 multi-site reconfiguration"
  ]
}
```

## Geometric / power assumptions (explicit)

These are **not** Motiv-published DH parameters. Unknown arm details are parameterized.

- **A-ARM-01:** Arm handling prefers mass ≤20 kg; design ~15 kg
- **A-ARM-02:** Simplified arm reach treated as spherical radius 1.2 m (NOT official DH)
- **A-ARM-03:** Transfer path is piecewise-linear waypoints in deck frame (kinematic only)
- **A-ARM-04:** Grapple capture tolerance ±15 mm position, ±5 deg attitude (ASSUMPTION)
- **A-IF-01:** Passive CrossLink mates active CrossLink EE
- **A-IF-02:** Primary deck install is iSSI (D-01)
- **A-SIM-01:** Keep-out cylinders around solar array brackets and launch locks
- **A-SIM-03:** iSSI capture envelope: 10 mm lateral, 5 deg tilt
- **A-B-04:** MONITOR average power design point 28 W
- **A-B-03:** Peak power design point 65 W, NTE 80 W
- **A-D-03:** Anomaly event packet target 1–4 kB

## How to reproduce

```bash
cd mss-oru-techleap
python -m twin.run_sims
```

## Interpretation for Phase 1

- SIM-01…03 and SIM-07 show **robotic manipulation is central** to install and multi-site value.
- SIM-04…06 show edge physical-AI mode machine, anomaly explainability, and graceful degradation.
- Paths are kinematic waypoints with keep-out cylinders; replace with CAD-derived corridors when available.
