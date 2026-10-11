# 08 — Interface Constraints

## Authority documents

1. NASA TechLeap RMPC Technical Guidelines — https://rmpc.nasatechleap.org/technical-guidelines/  
2. Motiv Space Systems, *FFR Data for Tech Leap v1*, April 2026 — `docs/references/FFR_Data_for_Tech_Leap_v1.pdf`  
3. Flight provider ICDs (when assigned)  

## Mechanical

| Interface | Role for MSS-ORU | Notes from FFR pack |
|-----------|------------------|---------------------|
| **Passive CrossLink Cleat** | Grapple by arm active CrossLink EE | Units in inches on drawing; bolt pattern subject to change |
| **FuseBlox** | Candidate deck install / power-mechanical | Active FuseBlox shown; M4 patterns on related drawings |
| **iSSI** | Candidate deck install | Active/passive; bolt pattern subject to change |
| ORU envelope | Overall form factor | Must match published ORU geometry |

### Baseline recommendation (pending D-01 lock)

- **Grapple:** Passive CrossLink (non-negotiable for arm EE).  
- **Deck install:** Prefer the separable interface that FFR uses for “3rd party” ORU placement in nominal Con-Ops; confirm against CAD.  
- Provide **two** CrossLink passive locations if matching Motiv ORU reference architecture.

## Electrical / power

- Arm can supply **power and data** to grappled ORU through end effector (guidelines).  
- Host deck power when installed — limits **TBD** from FFR docs / provider.  
- Design dual-path awareness: `POWER_HOST` vs `POWER_ARM`.  
- Inrush limiting, reverse protection, isolation as needed.

## Data

- Protocol stack: **TBD** from FFR software architecture notes / later ICDs.  
- Design abstract `Interface Manager` so transport can be swapped.  
- Prefer compact CCSDS-like or host-specified packets; store-and-forward buffer.

## Thermal

- Conductive path through deck interface + radiation to space.  
- State assumptions if host sink temp unknown.

## Software / ops interfaces

- Compatible with FFR software architecture at integration phase (Phase 2/3 criteria).  
- Mode commands for MONITOR / DIAG_GRAPPLE / SAFE.  
- Time sync strategy TBD (host time, free-running with later correlation).

## Constraints checklist for design reviews

- [ ] Grapple faces clear of snag hazards  
- [ ] Mass properties CG within arm handling assumptions (state if unknown)  
- [ ] No sharp edges in arm workspace  
- [ ] Connector mate/demate robotic-friendly  
- [ ] Launch lock strategy if required (Motiv pack shows launch locks on deck)  
- [ ] Patterns marked “subject to change” tracked as risk  

## Assumption log (interfaces)

| ID | Assumption | Impact if wrong |
|----|------------|-----------------|
| A-IF-01 | CrossLink grapple geometry matches published drawing within tolerance | Adapter redesign |
| A-IF-02 | Power available on install interface sufficient for MONITOR mode | Duty cycle down |
| A-IF-03 | Arm EE power path available for DIAG_GRAPPLE | UC-04 becomes host-only |
| A-IF-04 | Downlink intermittent / limited | Onboard prioritization mandatory |
