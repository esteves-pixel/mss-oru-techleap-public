# MSS-ORU / TechLeap

**Modular Sensing Skin — Orbital Replacement Unit**  
NASA TechLeap Prize · Robotically Manipulated Payload Challenge (5th TechLeap)

| Field | Value |
|-------|--------|
| **Owner** | Gonçalo Esteves |
| **GitHub** | [esteves-pixel](https://github.com/esteves-pixel) |
| **Status** | Phase 1 **submitted 12 Aug 2026** · Locked baseline · Engineering package + digital twin |
| **Scope of this public copy** | Engineering package and digital twin only. The submission forms and outreach drafts are not included. |
| **KB date** | 27 July 2026 |
| **Registration deadline** | 29 July 2026, 5:00 p.m. ET |
| **Submission deadline** | 12 August 2026 |

---

## One-line concept

A modular **sensing skin** ORU that the FFR (Motiv) robotic arm can grapple, install, reposition, and remove — delivering continuous external sensing and early anomaly detection for in-space robotic systems (**physical AI + external sensing**).

Robotic manipulation is **essential**, not peripheral: value depends on on-orbit place / reorient / remove cycles that only the arm provides.

---

## Why this exists

Canadarm2 operational history (25+ years vs ~15-year design life; wrist joint failure; LEE wear replacements; micrometeoroid strike) is evidence of a persistent **ISAM inspection / health-monitoring gap**. Future systems need continuous, repositionable external sensing and more autonomy — not only EVA or offline inspection.

Maps to Civil Space Shortfalls (2026), especially **SF28** (advanced robotics, automation, autonomy) and related ISAM shortfalls.

---

## Repository map

```
mss-oru-techleap/
├── README.md
├── requirements.txt                   ← numpy for twin
├── twin/                              ← digital twin (SIM-01…07)
├── docs/
│   ├── LOCKED_BASELINE.md             ← start here
│   ├── FULL_PROJECT_KNOWLEDGE_BASE.md
│   ├── STATUS_AND_OPEN_ACTIONS.md
│   ├── engineering/
│   │   ├── 01…09 SE package
│   │   ├── D01_INTERFACE_DECISION.md  ← CrossLink + iSSI
│   │   ├── 10_BUDGETS.md              ← refined mass/power
│   │   ├── SIM_RESULTS.md             ← 7/7 PASS
│   │   ├── RISK_REGISTER.md
│   │   ├── VERIFICATION_MATRIX.md
│   │   └── TEST_PLAN_SUMMARY.md
└── docs/references/FFR_Data_for_Tech_Leap_v1.pdf
```

### Quick run — digital twin

```bash
pip install -r requirements.txt
python -m twin.run_sims
```

---

## Official challenge links

| Resource | URL |
|----------|-----|
| Registration | https://rmpc.awardsplatform.com/ |
| Technical guidelines | https://rmpc.nasatechleap.org/technical-guidelines/ |
| Evaluation criteria | https://rmpc.nasatechleap.org/evaluation-criteria/ |
| FFR data (Motiv, Apr 2026) | [docs/references/FFR_Data_for_Tech_Leap_v1.pdf](docs/references/FFR_Data_for_Tech_Leap_v1.pdf) |

### Phase 1 scoring (1–5 each)

1. Technology Alignment  
2. Potential Impact  
3. Technical Design  
4. Project Plan  

---

## How to work in this repo

1. Read **`docs/LOCKED_BASELINE.md`** first (owner-locked intent, ConOps, FRs, mass/power).  
2. Read `docs/FULL_PROJECT_KNOWLEDGE_BASE.md` for full program context.  
3. Treat `docs/engineering/` as the detailed SE source of truth; refine against official FFR limits.  
4. Do **not** treat robotic manipulation as optional — judges require it to be central.

---

## Related work (same owner)

- `footprint-space-system` — Footprint vs Reality methodology (upstream pivot path)  
- `aether-dynamics` — space product / web strength benchmark work  

This TechLeap package is a **flight-challenge engineering track**, not a marketing-site track.

---

## License / distribution

Engineering drafts for competition use. FFR reference PDF is Motiv Space Systems material (unrestricted distribution per document header). Do not redistribute proprietary third-party materials beyond challenge terms.
