# Civil Space Shortfalls — Traceability & Gap-Closure Role of MSS-ORU

**Document type:** Requirements-grade traceability (treat shortfalls as **needs we support closing**)  
**Source:** [2026 Civil Space Shortfalls](https://www.nasa.gov/wp-content/uploads/2026/03/2026-civil-space-shortfalls.pdf) (Released 12 January 2026)  
**Challenge call-outs:** SF16, SF27, SF28, SF31, SF32  
**Extended needs (owner priority):** 1.06, 2.07, 6.01, 8.06, 14.01, 15.03, **all of Shortfall 28**  
**Date:** 11 Aug 2026  

---

## 0. How to read this document

| Term | Meaning here |
|------|----------------|
| **Primary** | Flight demo **directly** exercises this need |
| **Enabling** | Architecture is a **building block** for this need |
| **Analog / transfer** | LEO/FFR demo is an **analog** for lunar/Mars wording |
| **Out of scope** | Honest non-claim |
| **Gap we force into view** | Need **under-served** in the shortfall list — **physical / in-situ AI** — that MSS-ORU makes explicit |

**Scoring key for support strength:** ●●● strong · ●● partial · ● light · ○ none

---

## 1. Executive view — challenge shortfalls

| Shortfall | Title (2026) | Support | One-line role of MSS-ORU |
|-----------|--------------|---------|---------------------------|
| **SF28** | Autonomously monitor, inspect, maintain, and repair space assets | ●●● | **Core mission:** edge physical-AI health cell + robotic install/reconfig |
| **SF27** | Emplace and maintain large, stable space platforms and observatories | ●● | External health monitoring + robotic emplace/relocate of ORU-class assets |
| **SF31** | Provide space technology demonstration environments | ●●● | **Uses FFR** as on-orbit demo environment (31.04 class) |
| **SF32** | Develop an affordable and resilient supply chain for space exploration | ●● | Modular ORU/cell logistics; remove/replace without EVA; multi-cell growth |
| **SF16** | Provide surface mobility and logistics *(challenge list says “surface and planetary mobility and cargo operations”)* | ● | **Transfer analog:** robotic relocate of modular cargo/ORU — not surface driving |

**Primary story for judges:** SF28 + SF31, with SF27/SF32 as modular platform logistics, SF16 as light analog only.

---

## 2. Shortfall 28 — full need set (super focus)

**Shortfall title:** *Autonomously monitor, inspect, maintain, and repair space assets.*

| Need ID | Need statement (from 2026 shortfalls) | Support | How MSS-ORU contributes | Demo evidence |
|---------|----------------------------------------|---------|-------------------------|---------------|
| **28.01** | Implement space-based manufacturing techniques for in-situ repairs and replacement of hardware components | ● | **Replacement path**, not manufacturing: arm **remove/replace cell**; pattern for modular repair logistics | D-06, D-09, multi-cell path |
| **28.02** | Provide robotic systems capable of inspection, maintenance, and repair operations that function autonomously and as part of a human-robot team | ●●● | Motiv arm (robot) + **payload autonomy** (inspect products) + ops (human team) closed loop; TASK_REQUEST = robot tasking input | D-01…D-07, FDM-9 |
| **28.03** | Provide environmentally robust robotic, imaging, and sensing components with sufficient performance for challenging exploration missions | ●●● | Visual + thermal + vibration suite; LEO rad/thermal design; launch vibe plan | Sensors + env docs |
| **28.04** | Autonomously monitor systems and crew that support human exploration including during Mars-distance delays and blackouts | ●● | **Autonomous MONITOR** without ground-in-the-loop per sample; store-and-forward; power-gap SAFE | FDM-3, FDM-5, power-gap design |
| **28.05** | Autonomously detect and diagnose off-nominal conditions and events; safe, reliable autonomous control; automated safing sequences | ●●● | Edge anomaly detect + DEGRADED/SAFE FDIR + POWER_GAP safing | FDM-6, FDM-7, FM tables |
| **28.06** | Provide software platforms that can analyze data and make decisions autonomously while providing **explainable reasoning** or inspection capabilities necessary to establish trust | ●●● | Explainability metadata on every flag; TASK_REQUEST with cause codes; no black-box-only alerts | FR-06, FDM-5, physical-AI section |

### Shortfall 28 — gap-closure narrative (paste-ready)

> MSS-ORU is aimed squarely at **Shortfall 28**. It is an ORU-class **sensing + physical-AI cell** that the FFR arm robotically **installs, repositions, and removes**, while the payload **autonomously monitors** multi-modal external state, **detects/diagnoses** off-nominal conditions, **safes** itself through power gaps and faults, and emits **explainable** health products that operators (and later autonomy layers) can trust. Maintenance is demonstrated as **modular replace/relocate** rather than EVA repair. Manufacturing (28.01) is out of scope; **replacement logistics** are in scope.

---

## 3. Other challenge-listed shortfalls

### SF27 — Emplace and maintain large, stable space platforms and observatories

| Need ID | Statement (abridged) | Support | MSS-ORU |
|---------|----------------------|---------|---------|
| 27.01 | Precise attitude control for ultra-stable observatories | ○ | Out of scope |
| 27.02 | Reduce spacecraft exposure to vibration for pointing | ● | We **sense** vib at interfaces; we are not the quiet-platform actuator |
| 27.03 | Structural accuracy/stability for large space structures | ● | External health monitoring supports **maintain** |
| 27.04 | Robotically upgrade large space observatory instruments/avionics | ●● | **Pattern analog:** robotically install/replace modular unit |
| 27.05 | Create/evolve systems beyond launch size limits | ● | Multi-cell skin growth (assemble capability over time) |

**Narrative:** Large platforms need **continuous external awareness** and **robotic ORU logistics**. MSS-ORU demos both on FFR.

### SF31 — Provide space technology demonstration environments

| Need ID | Statement (abridged) | Support | MSS-ORU |
|---------|----------------------|---------|---------|
| 31.01 | Surface-based demo platforms | ○ | Not surface |
| 31.02 | Environmental simulators / test sites | ● | Ground twin + SIL before flight |
| 31.03 | Astronaut micro-g proficiency platforms | ○ | — |
| **31.04** | **On-orbit platforms and interfaces for tech/ops demos** | ●●● | **FFR + CrossLink + iSSI** is the environment; we are the demo payload |
| 31.05–31.06 | Higher altitude / LV accommodations | ● | Delivery vehicle path |

**Narrative:** We **consume** SF31 (FFR as demo environment) and **prove** a reusable demo class (health cell).

### SF32 — Affordable and resilient supply chain

| Need ID | Statement (abridged) | Support | MSS-ORU |
|---------|----------------------|---------|---------|
| 32.01 | Low-cost mass-efficient large components | ● | SWaP discipline ≤12.5 kg; COTS-heavy |
| 32.02 | Low SWaP-C deep-space comm | ○ | Hosted data path; no deep-space radio baselined |
| 32.03 | Radioisotope power conversion | ○ | Out of scope |
| **32.04** | Domestic suppliers for space-qualified systems in lead time | ●● | Modular ORU cells → **replaceable units** in logistics chain; ISAM-aligned |

**Narrative:** Resilient supply chain for exploration includes **ORU-class health cells** that can be stocked, robotically installed, and swapped—reducing unique one-off EVA logistics.

### SF16 — Surface mobility and logistics *(challenge wording varies)*

| Support | ● light analog |
|---------|----------------|
| What we are | **Not** a rover or cargo crane on a planetary surface |
| What we still show | Robotic **relocate** of modular cargo-like ORU between interfaces; logistics without EVA |
| Honesty | Do **not** claim SF16 closure; claim **transferable ISAM logistics pattern** |

---

## 4. Owner-priority needs (beyond challenge shortlist)

### 1.06 — In-situ decision support for EVA hazards (lunar)

> *Provide in-situ decision support tools to address identified EVA hazards and risks on the lunar surface.*

| Support | ●● analog |
|---------|-----------|
| Direct | Lunar surface EVA tools — **not** our flight domain |
| Transfer | **In-situ** explainable products that help decide whether EVA is needed **now** vs defer — same decision class as FM-OPS-3 (joint anomaly → EVA) |
| Physical AI role | Onboard assessment **without waiting for Earth** (delay analog even in LEO ops gaps) |

### 8.06 — In-situ decision support for EVA hazards (Martian)

Same pattern as 1.06 for Mars wording. **●● analog** — decision-support **class**, not Mars surface hardware.

### 2.07 — High-performance computing in extreme temperature, high radiation, dusty environments

| Support | ●● partial |
|---------|------------|
| We do | Edge compute in **LEO thermal isolation + radiation assumptions**; power-gap survival |
| We do not | Lunar dust, multi-kWe HPC, or full ESDMD #0201 envelope |
| Story | **Edge physical-AI** under constrained SWaP/thermal/rad is a **step** toward robust in-situ compute |

### 6.01 — Robust low-mass power management for long-duration extreme environments

| Support | ●● |
|---------|-----|
| Dual-rail PWR_BUS / PWR_ARM, break-before-make, power-gap SAFE | Directly exercises **robust PMAD** under sequencing stress |
| ≤12.5 kg mass discipline | Low-mass |
| Heaters inside IF rating + isolation | Extreme thermal self-management |

### 14.01 — Miniaturize sensors and instrumentation on small spacecraft

| Support | ●●● |
|---------|-----|
| Multi-modal suite in **≤12.5 kg** ORU | Miniaturized sensing cell |
| Not cubesat-only — ORU-class small asset | Fits “small spacecraft / small asset” intent |

### 15.03 — Safe efficient human-robot interaction; secure C2 over high-latency/bandwidth-limited nets; reliable automated safing

| Support | ●●● |
|---------|-----|
| Human-robot | Ops + Motiv arm + payload TASK_REQUEST |
| Bandwidth-limited | ≤4 kB events; store-and-forward; no raw video baseline |
| Automated safing | POWER_GAP, DEGRADED, SAFE, capture interlocks |

---

## 5. The missing shortfall: in-situ physical AI (we make it visible)

### Observation

The 2026 list strongly covers **robotics, autonomy, monitoring, explainability (28.06), HPC in extremes (2.07)** — but it does **not** cleanly name:

> **Physical AI:** onboard models that interpret **real sensor physics** (vib/thermal/visual structure state) and **act** (mode change, product priority, task requests) **in situ**, as distinct from (a) ground analytics, (b) generative text AI, or (c) pure GNC autonomy.

That omission is a problem for ISAM: **manipulation without perception-understanding** is incomplete; **perception without on-asset decision** reverts to ground-heavy ops (exactly FM-OPS-6).

### How MSS-ORU forces the need into the open

| Layer | What we demonstrate | Maps into shortfalls |
|-------|---------------------|----------------------|
| Sense physics | Multi-modal external state | 28.03, 14.01 |
| Think in situ | Edge anomaly / residual model | 28.04–28.06, 2.07 |
| Act on asset | FDIR modes + product priority | 28.05, 15.03 |
| Act on robot tasking | TASK_REQUEST → arm reconfig/DIAG | 28.02, 15.03 |
| Explain | Metadata for trust | **28.06** |
| Delay-tolerant | No ground loop per sample | 28.04, 15.03 |

### Paste-ready “missing need” paragraph

> Beyond mapping to published shortfalls, MSS-ORU explicitly demonstrates **in-situ physical AI**: models that run **on the hardware**, on **physical sensor streams**, producing **explainable** decisions and **manipulation task requests** without a ground loop per sample. We treat this as a necessary complement to SF28 (monitor/inspect/maintain/repair) and 28.06 (explainable autonomous analysis). If the shortfall catalog under-names physical AI, this flight still **operationalizes** it as an ISAM building block—“sense where you serve,” onboard.

---

## 6. Coverage matrix (compact)

| Need / shortfall | ●●● | ●● | ● | ○ |
|------------------|-----|----|---|---|
| **28.02, 28.03, 28.05, 28.06** | ✓ | | | |
| **28.04, 14.01, 15.03, 31.04, 6.01** | | ✓/●●● | | |
| **28.01, 27.04, 32.04, 2.07, 1.06/8.06** | | ✓ | | |
| **SF16 surface mobility** | | | ✓ analog | |
| **27.01 attitude control, 32.03 RPS** | | | | ✓ |

---

## 7. Requirements we accept from shortfalls (internal REQ IDs)

| REQ | Statement | Parent |
|-----|-----------|--------|
| **REQ-SF-28** | Payload shall autonomously monitor multi-modal external state and produce explainable anomaly products without ground-in-the-loop per sample | SF28 / 28.04–28.06 |
| **REQ-SF-28-SAFE** | Payload shall implement automated safing (DEGRADED/SAFE/POWER_GAP) | 28.05, 15.03 |
| **REQ-SF-28-ROBOT** | Flight demo shall require robotic arm physical interaction for install/reconfig; passive carriage invalid | 28.02 + challenge |
| **REQ-SF-31** | Design shall be compatible with FFR as on-orbit technology demonstration platform | SF31 / 31.04 |
| **REQ-SF-27** | Design shall support robotic emplace/relocate of modular external sensing for platform maintenance narrative | SF27 |
| **REQ-SF-32** | Design shall be ORU/cell modular to enable logistics replaceability | SF32 / 32.04 |
| **REQ-PAI-01** | Edge physical-AI shall sense→think→act on ORU and emit TASK_REQUEST for arm | Owner gap-fill |
| **REQ-ENV-01** | Survive launch + LEO thermal/rad per stated assumptions | Additional reqs |
| **REQ-DEB-01** | No debris hazard; deployables retained | Additional reqs |
| **REQ-EMI-01** | Reasonable EMC; no host interference | Additional reqs |

---

## 8. Application paste blocks

### 8.1 Shortfalls paragraph (Technology Alignment)

> MSS-ORU addresses NASA’s **2026 Civil Space Shortfalls** with primary alignment to **SF28** (autonomously monitor, inspect, maintain, and repair space assets)—including needs **28.02–28.06** (robotic inspection as human-robot team element, robust sensing, delay-tolerant monitoring, autonomous detect/diagnose/safing, and **explainable** autonomous analysis). It uses **SF31** (FFR on-orbit technology demonstration environment, need **31.04**) as the flight venue; supports **SF27** via robotic emplacement/relocation of external health capability for large platforms; and supports **SF32** via modular, replaceable ORU/cells in an ISAM logistics pattern. **SF16** is treated only as a light logistics analog (robotic relocate of modular units), not surface mobility. Owner-priority needs **14.01** (miniaturized sensing), **15.03** (human-robot interaction, bandwidth-limited products, automated safing), **6.01** (robust low-mass power management under power sequencing), and EVA decision-support analogs **1.06/8.06** are supported at the decision-product layer. We additionally call out **in-situ physical AI** as an operational capability that SF28 implies but does not fully name.

### 8.2 What we do **not** claim

- Closing SF16 surface mobility  
- Manufacturing in space (28.01 full scope)  
- Observatory attitude control (27.01)  
- Lunar dust-tolerant HPC (full 2.07)  
- Mars surface EVA tools as flight hardware (1.06/8.06 direct)

---

## 9. Source

- NASA, *2026 Civil Space Shortfalls*, released 12 January 2026:  
  https://www.nasa.gov/wp-content/uploads/2026/03/2026-civil-space-shortfalls.pdf  

Local engineering package maps: demo plan, physical AI, interfaces D-01, env/safety `12_ENV_SAFETY_EMI.md`.  
