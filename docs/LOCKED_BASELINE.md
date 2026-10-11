# MSS-ORU — Locked Starting Baseline

**Status:** LOCKED for Phase 1 engineering  
**Date:** 27 July 2026  
**Owner:** Gonçalo Esteves  
**Registration:** Phase 1 **complete** (confirmed by owner)

Treat this document as the **authoritative starting point**. Refine numbers only against official FFR limits; do not change intent without an explicit decision record.

---

## Project Intent

Design a modular ORU-style **“sensing skin”** that the FFR robotic arm can **grapple, install, reposition, and remove**.

The payload:

- Senses external conditions (**visual + thermal + vibration** minimum) on the arm or platform  
- Runs an **edge physical-AI** model  
- Produces **explainable** health assessments and anomaly detections  

This addresses a real operational gap evidenced by **>25 years of Canadarm2** experience and aligns with **2026 Civil Space Shortfalls** (especially autonomous inspection / maintenance / repair — SF28 class).

**Hard rule:** Robotic manipulation is **essential**, not peripheral.

---

## Concept of Operations

1. Arm grapples the MSS-ORU using a published FFR interface (CrossLink, FuseBlox, or iSSI — see interface note below).  
2. Arm transfers and installs it.  
3. Payload receives power/data, starts sensing + edge physical-AI model.  
4. Generates explainable health / anomaly outputs.  
5. Arm can later reposition or remove it.  

### Interface note (precision)

| Role | Interface | Notes |
|------|-----------|--------|
| **Grapple (arm EE)** | **Passive CrossLink** | Motiv arm end effectors are **active CrossLink** — grapple path is CrossLink |
| **Deck install** | FuseBlox **or** iSSI **or** CrossLink | Choose one primary install baseline (open decision D-01) |

Saying “grapples using CrossLink, FuseBlox, or iSSI” is fine at concept level; for design freeze, **grapple = CrossLink**, **install = pick one deck interface**.

---

## Functional Requirements

**FR-01 … FR-11** as defined in `docs/engineering/03_FUNCTIONAL_REQUIREMENTS.md`:

| ID | One-line |
|----|----------|
| FR-01 | Passive CrossLink grapple compatibility |
| FR-02 | Separable deck install without EVA |
| FR-03 | Transfer + remove/reinstall (reconfiguration) |
| FR-04 | External sensing (visual + thermal + vibration minimum) |
| FR-05 | Edge processing → compact features + anomaly indicators |
| FR-06 | Explainability metadata |
| FR-07 | Radiation / environment tolerance + graceful design |
| FR-08 | Graceful degradation on partial failure |
| FR-09 | Explore self-healing materials (non-critical path) |
| FR-10 | Mass / volume / power within FFR limits + team targets |
| FR-11 | Safety / no free-flyer hazard / host constraints |

---

## Physical & Software Architecture Baseline

| Element | Locked baseline |
|---------|-----------------|
| Form factor | **ORU-class** module |
| Sensor suite (minimum) | **Visual + thermal + vibration** |
| Compute | **Edge compute** (physical AI pipeline) |
| Software chain | Sensor → Conditioning → Features → Edge model → Explainability → Interface manager |

### Resource targets (official SWaP + interface — 11 Aug 2026)

| Parameter | Locked target | Status |
|-----------|---------------|--------|
| **Mass** | **≤ 12.5 kg** hard NTE; design ≈ **11.1 kg** with margin | **SOURCE** challenge SWaP |
| **Stowed envelope** | Within **proposed interface** max cross-section; height vs CrossLink/arm workspace | SOURCE |
| **Deployed volume** | State max; baseline **= stowed** (no large deployables) | SOURCE + team choice |
| **Peak power** | ≤ **65 W** design; ≤ **72 W** continuous on iSSI (24 V × 3 A) | SOURCE IF rating |
| **MONITOR average** | **~28 W** (heaters duty-cycled inside IF rating) | ASSUMPTION inside SOURCE cap |
| **Thermal** | **Isolated from bus** (no conduction); self-manage with MLI/heaters inside IF power | SOURCE |
| **Power sequencing** | **Bus OFF before arm pass-through ON**; unknown-duration **power gap** | SOURCE |

Canonical detail: `docs/engineering/11_SWAP_THERMAL_POWER.md`. Official limits win over legacy 15–25 kg language.

---

## What this baseline is *not*

- Not a final flight ICD  
- Not a claim that self-healing is flight-proven  
- Not a fixed sensor box that never needs the arm after launch  

---

## Canonical package map

| Need | File |
|------|------|
| This locked baseline | `docs/LOCKED_BASELINE.md` |
| Full conversation + program context | `docs/FULL_PROJECT_KNOWLEDGE_BASE.md` |
| Engineering detail | `docs/engineering/01…09_*.md` |
| Phase 1 writing | `docs/phase1/*.md` |
| **Mandatory Grok Build prompt** | `prompts/GROK_BUILD_MASTER_PROMPT.md` |
| FFR reference | `docs/references/FFR_Data_for_Tech_Leap_v1.pdf` |

---

## Confirmation checklist

- [x] Project intent matches sensing-skin ORU + physical AI  
- [x] ConOps has grapple → install → sense/AI → reposition/remove  
- [x] Manipulation essential  
- [x] FR-01…11 package exists  
- [x] Visual + thermal + vibration minimum suite  
- [x] Mass **≤ 12.5 kg** SOURCE; design ≈ 11.1 kg  
- [x] Thermal isolation + power-gap sequencing documented  
- [x] Phase 1 registration complete (owner confirmed)  
- [x] Deck install interface baselined (**D-01: CrossLink grapple + iSSI install**)  
- [x] Budgets: ~28 W MONITOR, ≤65 W peak, ≤72 W iSSI continuous 
- [x] Digital twin + SIM-01…07 (7/7 PASS)  
- [ ] Official FFR mass/power limits extracted from CAD and compared (A-B-06)  
