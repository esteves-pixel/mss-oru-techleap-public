# 06 — Software / Physical AI Architecture

## Design principle

**Physical AI** here means: models that interpret **physical sensor streams** from the external environment and structure, not generative text. Outputs are **actionable health products** for operators and future autonomy loops.

## Pipeline

```
Sensors
   → Conditioning (filter, calibrate, time-sync)
   → Feature Extraction (domain features + light learned embeddings)
   → Edge Model (anomaly / state classifier or residual detector)
   → Explainability (top features, channel IDs, confidence, mode)
   → Interface Manager (host/arm protocol, prioritization, storage)
```

## Layer responsibilities

| Layer | Responsibility | Failure behavior |
|-------|----------------|------------------|
| Conditioning | Units, bias, sample integrity | Drop bad samples; flag |
| Feature extraction | Deterministic features preferred as baseline | Fall back to subset |
| Edge model | Anomaly score / discrete state | Conservative threshold; “unknown” class |
| Explainability | Why flagged | Always attach metadata when scoring |
| Interface manager | Packets, queues, modes | Store-and-forward; never block sensors forever |

## Model strategy (Phase 1 honesty)

1. **Baseline:** classical features (RMS, spectral bands, thermal rates, strain stats) + simple threshold / residual model.  
2. **Stretch:** tiny NN or isolation-style model if power/compute allow.  
3. **Training:** ground twin + simulated anomalies; limited on-orbit unsupervised baseline update.  
4. **No claim** of full unsupervised robot “self-awareness” without evidence path.

## Data products

| Product | Size intent | Use |
|---------|-------------|-----|
| Housekeeping | Tiny | Ops |
| Feature vector summary | Small | Science/ops |
| Anomaly event | Small + context window | Alert |
| Raw snippet (optional) | Medium, rare | Debug when downlink allows |

## Onboard software modes

- `INIT` → `BASELINE` → `MONITOR` → `ANOMALY` → `DEGRADED` → `SAFE`  
- Grappled diagnostic mode: `DIAG_GRAPPLE`

## Security / integrity (lightweight)

- Command authentication as required by host  
- CRC/hash on critical tables  
- No open debug ports on flight config  

## Traceability

Supports FR-04, FR-05, FR-06, FR-08 and UC-02…UC-05.
