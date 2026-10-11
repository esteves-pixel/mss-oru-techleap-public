# MSS-ORU Digital Twin (scaffold)

Simulation-first twin for the NASA TechLeap MSS-ORU payload.

## What it models

1. **Kinematic sequence** (waypoint-based, **not** official Motiv DH): grapple → transfer → iSSI mate → remove → reinstall site B  
2. **Sensors:** visual proxy + thermal + vibration with injectable anomalies  
3. **Edge pipeline:** conditioning → features → residual anomaly score → explainability → packet size  
4. **SIM-01…SIM-07** campaign → `docs/engineering/SIM_RESULTS.md`

## Interfaces (D-01)

- Grapple: Passive CrossLink ×2  
- Deck install: iSSI  
- Optional: FuseBlox Passive  

## Run

From repo root (`mss-oru-techleap`):

```bash
python -m twin.run_sims
```

Requires: Python 3.10+, `numpy`.

```bash
pip install numpy
```

## Layout

| File | Role |
|------|------|
| `config.py` | Mass/power/geometry assumptions (IDs) |
| `kinematics.py` | Paths, keep-outs, capture/mate checks |
| `sensors.py` | Time-series + anomaly inject |
| `edge_ai.py` | Physical AI stub + modes |
| `run_sims.py` | SIM-01…07 runner + report writer |

## Important limitations

- Arm reach and keep-outs are **ASSUMPTIONS** (`A-ARM-02`, `A-SIM-01`).  
- Does not replace CAD collision analysis or flight software.  
- Use results as Phase 1 **simulation evidence**, then refine with official FFR CAD.
