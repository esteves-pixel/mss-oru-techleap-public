# FFR Tech Leap Inputs pack — what it actually is

**File:** [FFR_Data_for_Tech_Leap_v1.pdf](https://rmpc.nasatechleap.org/wp-content/uploads/2026/05/FFR_Data_for_Tech_Leap_v1.pdf)  
**Local:** `docs/references/FFR_Data_for_Tech_Leap_v1.pdf`  
**Meta:** Motiv Space Systems · Tech Leap Inputs · NSSC 80NSSC25C0423 · **14 Apr 2026** · **10 pages** · “FOR UNRESTRICTED DISTRIBUTION”

---

## Bottom line

This pack is **mostly CAD / mechanical interface drawings + conceptual ConOps slides**.  

It is **not**:
- A full flight ICD  
- A radiation or thermal environment document  
- Published arm DH / workspace / force limits  
- A mission duration or orbit definition  
- A qualification test specification  

**Harsh rule for the application:** Treat this PDF as **geometry + interface family + nominal ConOps storyboard**. Everything else stays **assumption IDs** until Phase 2 freezes.

---

## Page-by-page content

| Page | Content | Design use |
|------|---------|------------|
| **1** | Title: FFR SBIR Phase 3 · Tech Leap Inputs · Motiv + partner logos | Context only |
| **2** | **Active FuseBlox** mechanical drawing (mm), 4× M4×0.7 ↓10 mm | Alternate park IF geometry |
| **3** | **Active/Passive iSSI** drawing (mm), **“Bolt pattern subject to change”**, iSSI V7 envelope | **Preferred park IF** — adapters mandatory |
| **4** | **Passive CrossLink Cleat** (inches), **“Bolt pattern subject to change”** | **Grapple face** on ORU |
| **5** | Overview render: deck, CrossLink arm, separable IFs, ORU module | Visual for form PDF |
| **6** | **Nominal Con-Ops** steps i–x (launch → grapple → 3rd party install → re-position → walk → Guest Roboticist ops **Details TBD**) | Align our demo to **this** sequence |
| **7** | **Post ORU Move** deck map: Passive CrossLink (ORU launch location), **iSSI** (ORU location after move), FuseBlox passive, launch locks (7 places), solar array brackets, camera cal board | Confirms **ORU ends at iSSI** in Motiv story |
| **8** | Arm + cleats + ORU callouts: CrossLink Passive **(2 places)** on ORU, iSSI Active + bracket, FuseBlox Passive | Matches D-01 dual CrossLink + iSSI |
| **9** | ORU CAD only | Envelope reference |
| **10** | Simulation render | Not flight evidence |

---

## Nominal Con-Ops (page 6) — map to MSS-ORU

| Motiv step | Meaning | Our demo |
|------------|---------|----------|
| i | Launch configuration | L1 stow / launch locks |
| ii | Arm commissioning | Host ops |
| iii | Arm above CrossLink on ORU | Approach |
| iv | Grapple CrossLink on ORU | D-01 |
| v | Release ORU from deck CrossLink | Leave launch seat |
| vi | Place on **3rd party interface** and secure | **iSSI preferred** (page 7 shows ORU at iSSI) |
| vii | Arm releases ORU and re-positions | After install |
| viii | Arm attaches empty CrossLink (walk) | Host mobility demo |
| ix | Arm releases base | Host |
| x | Guest Roboticist ops (**Details TBD**) | **Our** sensing / reconfig / TASK_REQUEST demo lives here |

---

## What the CAD pack *does* lock for us

1. **Interface families:** FuseBlox, iSSI, Passive CrossLink — same three as guidelines.  
2. **ORU concept:** box with **2× Passive CrossLink** + path to **iSSI** post-move.  
3. **Bolt patterns may change** → **late-binding adapters** (already in risk register).  
4. **ConOps storyboard** is grapple → 3rd party install → further arm work — not “carry and drop.”  
5. **Units mixed** (mm on FuseBlox/iSSI, **inches** on CrossLink) → careful CAD work.

---

## What it does *not* give (do not invent from CAD)

| Missing | Our response |
|---------|----------------|
| Arm DH, reach, force/torque | Parameterized twin assumptions |
| TID / radiation | Own LEO TID/SEE assumptions |
| Thermal sinks | Isolation + heaters/MLI |
| Mass limit | **12.5 kg** from guidelines page, not this PDF |
| Power ratings | Separable Interfaces brief / guidelines tables |
| Mission duration / inclination | Hosted flight “not available — assume” |
| Guest ops details | **We** define demo plan |

---

## Implication for form language

- Prefer **iSSI** park: **supported by Motiv post-move diagram (ORU at iSSI)**, not just our preference.  
- **Passive CrossLink ×2:** shown on ORU callout page.  
- Say explicitly: *interface drawings are CAD-class; bolt patterns subject to change; full env ICD TBD.*  
- Visual PDF pages 5–8 of this pack are fair reference art (unrestricted distribution).

---

## Twin honesty

Our SIM-01…07 is **our** digital twin of ConOps steps, **not** Motiv’s page-10 “Simulation” slide as evidence of their flight software.

---

**Traceability:** D-01, Overview form text, `TECHNICAL_GUIDELINES_COMPLIANCE.md`  
