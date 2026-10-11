# Status & Open Actions

**Last updated:** 11 August 2026 (ConOps + failure modes made explicit in Phase 1 submission text)

## Deadlines

| Milestone | When | Status |
|-----------|------|--------|
| Phase 1 registration | 29 Jul 2026, 17:00 ET | **Complete** (owner confirmed) |
| Phase 1 submission | 12 Aug 2026 | **Submitted** ✅ |
| FFR launch (program) | Late 2027 (expected) | External |
| TechLeap payload flight | Early 2028 (expected) | External |

## Decision log

| ID | Decision | Outcome | Owner | Status |
|----|----------|---------|-------|--------|
| **D-01** | Baseline FFR mechanical interfaces | **Grapple = Passive CrossLink ×2; Deck install = iSSI; FuseBlox optional** | GE | **BASELINED** — see `docs/engineering/D01_INTERFACE_DECISION.md` |
| **D-02** | Sensor suite baseline | **Visual + thermal + vibration** | GE | **Locked** (LOCKED_BASELINE) |
| D-03 | Edge compute class | MCU-class vs SOM with limited NN | GE | Open — 28 W MONITOR supports either |
| D-04 | Starcloud outreach | Send / hold | GE | Open |
| D-05 | Repo visibility | private vs public | GE | Private until submission |

### D-01 decision record (summary)

- **Grapple:** Passive CrossLink Cleat ×2 (arm EE is active CrossLink; Motiv ORU reference).  
- **Deck install:** **iSSI** (matches Motiv post-ORU-move / 3rd-party install story).  
- **Optional:** FuseBlox Passive (mass descope lever −0.8 kg CBE).  
- **Risks:** bolt patterns subject to change → adapter margin.  
- Full write-up: `docs/engineering/D01_INTERFACE_DECISION.md`

## Grok Build execution status (2026-07-27)

| Deliverable | Status | Path |
|-------------|--------|------|
| D-01 interface decision | Done | `docs/engineering/D01_INTERFACE_DECISION.md` |
| Mass/power budgets | Done | `docs/engineering/10_BUDGETS.md` |
| Physical architecture budgets | Updated | `docs/engineering/05_PHYSICAL_ARCHITECTURE.md` |
| Digital twin scaffold | Done | `twin/` |
| SIM-01…07 | **7/7 PASS** | `docs/engineering/SIM_RESULTS.md` |
| Risk register | Done | `docs/engineering/RISK_REGISTER.md` |
| V&V matrix | Done | `docs/engineering/VERIFICATION_MATRIX.md` |
| Test plan summary | Done | `docs/engineering/TEST_PLAN_SUMMARY.md` |
| Phase 1 form polish | **Done** (28 Jul 2026) | `docs/phase1/*` + `PHASE1_SUBMISSION_PACKAGE.md` |
| Explicit official ConOps + FM tables in paste text | **Done** (11 Aug 2026) | Alignment, Impact, Design, Plan, master package |
| SWaP 12.5 kg + thermal isolation + power gap | **Done** (11 Aug 2026) | `11_SWAP_THERMAL_POWER.md` |
| Env / vibe hold / debris / Part 450 / EMI | **Done** (11 Aug 2026) | `12_ENV_SAFETY_EMI.md` |
| Civil Space Shortfalls as requirements + physical AI gap | **Done** (11 Aug 2026) | `CIVIL_SPACE_SHORTFALLS_TRACEABILITY.md` |

### Refined design points

| Parameter | Value |
|-----------|-------|
| Mass | **≤ 12.5 kg** hard; design **≈ 11.1 kg** (CBE ≈ 9.65 kg) |
| MONITOR average | **~28 W** |
| Peak (design) | **≤65 W**; iSSI continuous **≤72 W** |
| Thermal | Bus-isolated; MLI + heaters inside IF power |
| Power gap | Bus OFF before arm ON; POWER_GAP/SAFE |

## Work queue (priority)

1. ~~Registration~~ **Done**  
2. ~~Mandatory Grok Build (interfaces, budgets, twin, SIM, risks)~~ **Done**  
3. ~~Polish Phase 1 form answers~~ **Done** — paste from `docs/phase1/`  
4. **P0** Fill owner bio / $ budget if form requires → **submit by 12 Aug 2026**  
5. **P1** Verify mass/power vs **official FFR CAD** limits (A-B-06 still open)  
6. **P2** Starcloud outreach  
7. **P2** Breadboard sensors + power measurement (Phase 2 path)

## Risks to watch

See full register: `docs/engineering/RISK_REGISTER.md`  
Top: schedule (R-09), unknown FFR limits (R-02/R-03), interface volatility (R-01), multi-site ops (R-15).

## Definition of done — Phase 1 package

- [x] All four criteria sections written to rubric 4–5 quality (polish 28 Jul)  
- [x] Robotic manipulation essentiality explicit in engineering package  
- [x] Success metrics drafted (Potential Impact) — FDM/QM locked numbers  
- [x] Interface compatibility baseline (D-01)  
- [x] Risks + mitigations documented  
- [x] Assumptions list for TBD orbit/ops parameters  
- [x] Sim-first evidence (SIM 7/7)  
- [x] Owner bio / currency budget filled if required by form  
- [x] **Submitted on awards platform** — confirmed by the operator 2026-08-22, before the
      12 Aug deadline. Corroborated by the 2026-08-19 commit *"land Phase 1 engineering
      package left uncommitted at submit"*. These two boxes had been left stale.  
