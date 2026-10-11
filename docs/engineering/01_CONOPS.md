# 01 — Concept of Operations (MSS-ORU)

## Mission statement

Demonstrate a **robotically manipulated modular sensing skin ORU** on FFR: the Motiv arm grapples, transfers, installs, powers, repositions, and removes the unit so that external sensing and edge anomaly detection can be placed where needed — proving that continuous ISAM health monitoring can be **reconfigured on orbit without EVA**.

## Actors

| Actor | Role |
|-------|------|
| FFR host spacecraft | Provides deck interfaces, power/data when installed, ops environment |
| Motiv CrossLink arm | Essential manipulator: grapple, transfer, install, reorient, remove |
| MSS-ORU payload | Sensing skin + edge AI ORU |
| Delivery vehicle | Brings ORU to FFR vicinity |
| Ground / guest ops | Command sequences, receive health products (as downlink allows) |

## Mission phases

### Phase 0 — Ground & launch

1. Integrate MSS-ORU with flight interfaces (CrossLink grapple faces + selected deck install interface).  
2. Environmental qualification (vibration, thermal-vac, EMI as required by flight provider).  
3. Launch on TechLeap delivery vehicle (early 2028 class mission).  

### Phase 1 — Arrival & transfer (robotic — essential)

1. Delivery vehicle rendezvous with FFR.  
2. Arm grapples **passive CrossLink** on MSS-ORU.  
3. Delivery vehicle releases ORU.  
4. Arm transfers ORU to FFR deck.  
5. Arm installs ORU on selected separable interface (FuseBlox / iSSI / CrossLink as baselined).  
6. Arm releases; ORU transitions to **installed sensing mode**.  

### Phase 2 — Commissioning

1. Power-on via host or arm-supplied path (as available).  
2. Sensor health check; baseline environmental characterization of install site.  
3. Edge model loads “quiet baseline” features.  
4. First health product generated (status + confidence).  

### Phase 3 — Demonstration sequence (manipulation essential)

| Demo step | Arm action | Sensing / AI action | ISAM value |
|-----------|------------|---------------------|------------|
| D1 | Install at site A | Continuous external sensing | Robotic placement of monitoring asset |
| D2 | Optional reorient / small pose adjust | Multi-aspect sensing | Inspection geometry control |
| D3 | Remove from A, install at site B | New baseline + compare | Reconfigurable monitoring without EVA |
| D4 | Grapple for powered diagnostic pass | Arm-powered / data-through-EE if available | Servicing-like interaction |
| D5 | Stow / return to storage interface | Safe state | Modular ORU logistics |

### Phase 4 — Ops / store-and-forward

1. Periodic sensing; anomaly flags with explainable features.  
2. Data volume managed for unknown downlink (compress, prioritize events).  
3. Graceful degradation if radiation or sensor channels fail.  

### Phase 5 — End of demonstration

1. Arm removes ORU if required by host.  
2. Final data dump / safing.  
3. Lessons for long-lived robotic arms and future ISAM platforms.  

## Success for ConOps (flight-test level)

- At least **one full cycle**: grapple → transfer → install → sense → remove (or reinstall at second site).  
- Manipulation is **causal** to value: sensing location changes only because the arm moved the ORU.  
- No EVA required for the demonstration sequence.  

## Explicit non-goals (Phase 1 proposal)

- Full Canadarm2 retrofit  
- Unlimited downlink / full video streaming as baseline  
- Claiming flight-qualified self-healing skin as TRL-9 — self-healing is **exploration** under radiation/graceful-degradation goals  

## Alignment to Motiv nominal Con-Ops

Maps cleanly onto published FFR sequence: grapple CrossLink on ORU → release from launch location → place on interface → release → re-position → further arm mobility demos. MSS-ORU **adds** sensing/AI payload function inside that manipulation chain.
