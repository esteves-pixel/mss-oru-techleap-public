# MSS-ORU / TechLeap — Full Project Knowledge Base

**Date:** 27 July 2026  
**Owner:** Gonçalo Esteves  
**Status:** Phase 1 registered | Engineering package drafted | Outreach prepared  
**Repo:** `mss-oru-techleap` (esteves-pixel)

---

## A. Project Origin & Evolution (Conversation Trail)

1. Started from the need for a **monetizable space-sector product**.
2. Pivoted to space digital arbitrage / website strength, then to **Footprint vs Reality**.
3. Shifted to **NASA TechLeap Robotically Manipulated Payload Challenge** after identifying the open call and tight deadline (registration **29 July 2026**).
4. **Core insight:** use real operational experience of **Canadarm2** (25+ years, joint failures, end-effector wear, micrometeoroid strike) as evidence of a persistent **ISAM gap**.
5. Concept crystallized as a modular **“sensing skin” ORU** that the FFR arm can place and remove — **physical AI + external sensing**.
6. **Starcloud** (Philip Johnston; Starcloud-1 / first H100 GPU in space, Nov 2025) identified as a relevant collaboration target because they already flew a compute “box”.
7. Systems-engineering structure defined:  
   **ConOps → Requirements → Physical Architecture → Software/Physical AI → Radiation & Self-healing → Test Plan**.

---

## B. Program Context — NASA TechLeap

| Item | Detail |
|------|--------|
| Challenge | Robotically Manipulated Payload Challenge (5th TechLeap Prize) |
| Platform | Fly Foundational Robots (FFR) with Motiv Space Systems robotic arm |
| Registration deadline | 29 July 2026, 5:00 p.m. ET |
| Submission deadline | 12 August 2026 |
| Registration | https://rmpc.awardsplatform.com/ |
| Technical guidelines | https://rmpc.nasatechleap.org/technical-guidelines/ |
| Evaluation criteria | https://rmpc.nasatechleap.org/evaluation-criteria/ |

### Phase 1 scoring criteria (1–5 each)

1. **Technology Alignment** — ISAM gap + robotic manipulation essential  
2. **Potential Impact** — field advancement + measurable success metrics  
3. **Technical Design** — sound design, FFR compatibility, SE best practices, risks  
4. **Project Plan** — feasible path, milestones, experience, budget, margin  

### Key requirement (non-negotiable)

> Robotic manipulation by the FFR arm must be **essential**, not peripheral.  
> Passively carrying an instrument from A to B is **not** sufficient.

### Official ConOps (challenge)

1. Delivery vehicle with winning payloads rendezvous with FFR already on orbit.  
2. Arm transfers payload from delivery vehicle and installs on FFR via separable interface.  
3. Arm interacts with / manipulates / reconfigures payload per team demonstration plan.  
4. Arm end effectors: **active CrossLink cleats**; can supply **power and data** to a grappled ORU.  

### Nominal Motiv Con-Ops (FFR data pack, Apr 2026)

Launch config → arm commissioning → grapple CrossLink on ORU → release from deck → place on 3rd-party interface → release → re-position → attach to empty CrossLink → release base (mobility) → guest ops (TBD).

### Timeline (published assumptions)

- FFR expected launch: late 2027  
- TechLeap payloads: early 2028 rendezvous mission  
- Inclination, duration, ground contact, daily downlink: **TBD** — state assumptions and design for robustness  

---

## C. Key External References

### FFR / Motiv documentation

- Interfaces: **CrossLink Passive Cleat**, **FuseBlox**, **iSSI**  
- ORU form factor and Con-Ops (grapple → transfer → install → release)  
- Document: `docs/references/FFR_Data_for_Tech_Leap_v1.pdf` (Motiv Space Systems, April 2026)  
- Source URL: https://rmpc.nasatechleap.org/wp-content/uploads/2026/05/FFR_Data_for_Tech_Leap_v1.pdf  

### Civil Space Shortfalls (2026)

Released context used in team narrative (Jan / Mar 2026 publications). Most relevant:

| ID / area | Relevance to MSS-ORU |
|-----------|----------------------|
| **SF28** | Advanced robotics, automation, autonomy |
| **SF27** | Emplace and maintain large platforms / observatories |
| **SF31** | Space technology demonstration environments |
| **SF32** | Affordable, resilient supply chain (modular ORUs) |
| Category 28 / autonomous monitor–inspect–maintain–repair | Core mission of sensing skin |
| 4.03 / 12.06 assembly | Modular reconfiguration |
| 15.03 / 15.04 human–robot / cooperative tasks | Reduce EVA dependence |

Challenge site also lists SF16, SF27, SF28, SF31, SF32 as illustrative ISAM-related shortfalls.

### Canadarm2 operational evidence (problem statement)

| Fact | Implication |
|------|-------------|
| Designed ~15 years; now **>25 years** on ISS | Longevity outruns original inspection model |
| **May 2026** wrist-joint failure → spacewalk | Failures still drive EVA |
| **2017–2018** Latching End Effector replacements (wear) | Contact interfaces degrade; need better monitoring |
| **2021** micrometeoroid strike | External environment damages hardware unpredictably |
| Increasing ground control; need more autonomy | Future arms need onboard sensing + AI assist |

### Starcloud

| Item | Detail |
|------|--------|
| Contact | Philip Johnston, CEO |
| Starcloud-1 | Nov 2025 — first Nvidia H100 GPU in space |
| Why relevant | Operated high-power compute box in orbit; lessons for edge AI / thermal / power |
| Outreach | X, LinkedIn, website form — drafts in `outreach/STARCLOUD_MESSAGES.md` |

---

## D. Formal Engineering Package (Index)

Canonical files under `docs/engineering/`:

| # | Document | File |
|---|----------|------|
| 1 | Concept of Operations | `01_CONOPS.md` |
| 2 | High-level capability need | `02_CAPABILITY_NEED.md` |
| 3 | Functional requirements FR-01…FR-11 | `03_FUNCTIONAL_REQUIREMENTS.md` |
| 4 | Use cases UC-01…UC-06 | `04_USE_CASES.md` |
| 5 | Physical architecture | `05_PHYSICAL_ARCHITECTURE.md` |
| 6 | Software / Physical AI | `06_SOFTWARE_PHYSICAL_AI.md` |
| 7 | Radiation + self-healing / anti-fragile | `07_RADIATION_SELF_HEALING.md` |
| 8 | Interface constraints | `08_INTERFACE_CONSTRAINTS.md` |
| 9 | Verification & test plan (sim-first) | `09_TEST_PLAN_SIM_FIRST.md` |

**Capability need (summary):** Continuous, repositionable external sensing + early anomaly detection on robotic systems, reducing dependence on EVAs and offline inspection.

**Physical AI pipeline:**  
Sensor → Conditioning → Feature Extraction → Edge Model → Explainability → Interface Manager  

**Self-healing exploration targets:** self-healing PDMS, poly(urea)urethanes, microcapsule systems, dynamic impact polymers, “Harnessing Harshness” approaches.

---

## E. Outreach Status

Three message versions prepared (see `outreach/STARCLOUD_MESSAGES.md`):

1. X (reply/DM) — references specific post Philip liked  
2. LinkedIn  
3. Website contact form  

**Target:** Philip Johnston / Starcloud — lessons from operating a compute box in orbit.  
**Action:** send if not already done (track in `STATUS_AND_OPEN_ACTIONS.md`).

---

## F. GitHub / Repository Context

| Item | Detail |
|------|--------|
| User | esteves-pixel |
| Related repos | `footprint-space-system`, Aether Dynamics work |
| This package | **Dedicated repo** `mss-oru-techleap` (not mixed into Footprint marketing track) |

---

## G. What Still Needs to Be Produced

- [x] Full Project Knowledge Base in repo  
- [x] Engineering core package scaffold  
- [x] Exact Grok Build master prompt  
- [x] Potential Impact draft with measurable metrics  
- [x] Registration complete (owner confirmed)  
- [x] **D-01** interface baseline (CrossLink grapple + iSSI install)  
- [x] Refined mass/power budgets (team targets; official FFR CAD still TBD)  
- [x] Digital twin scaffold + **SIM-01…07 (7/7 PASS)**  
- [x] Risk register + V&V matrix + test plan summary  
- [ ] Technical Design section polished for formal Phase 1 application  
- [ ] Project Plan section polished for formal Phase 1 application  
- [ ] Re-verify mass/power against **official FFR CAD** numeric limits (A-B-06)  
- [ ] Send Starcloud outreach if pending  

---

## H. Recommended Immediate Actions

1. Keep this KB as living source of truth; update after every decision.  
2. Run Grok Build with `prompts/GROK_BUILD_MASTER_PROMPT.md`.  
3. Continue Phase 1 writing: Potential Impact → Technical Design → Project Plan.  
4. Send Starcloud outreach.  
5. Baseline mechanical interface and lock preliminary mass/power assumptions with explicit TBD margins.
