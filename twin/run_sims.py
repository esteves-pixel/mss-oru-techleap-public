"""
Run SIM-01…SIM-07 and write docs/engineering/SIM_RESULTS.md

Usage (from repo root):
  python -m twin.run_sims
"""

from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

import numpy as np

from twin.config import ASSUMPTIONS, DEFAULT, TwinConfig
from twin.edge_ai import EdgePipeline, Mode
from twin.kinematics import ArmKinematics
from twin.sensors import SensorSimulator


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "engineering" / "SIM_RESULTS.md"


def _ok(flag: bool) -> str:
    return "PASS" if flag else "FAIL"


def run_all(cfg: TwinConfig | None = None) -> Dict[str, Any]:
    cfg = cfg or DEFAULT
    kin = ArmKinematics(cfg)
    sens = SensorSimulator(cfg)
    edge = EdgePipeline(cfg)
    g = cfg.geometry
    results: Dict[str, Any] = {
        "meta": {
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "twin_version": "0.1.0",
            "interfaces": cfg.interfaces,
            "mass_design_kg": cfg.mass_power.mass_design_kg,
            "power_monitor_w": cfg.mass_power.power_monitor_avg_w,
            "power_peak_w": cfg.mass_power.power_diag_peak_w,
        },
        "sims": {},
    }

    # SIM-01 Grapple
    path01, cap01 = kin.grapple_approach(g.delivery_hold, approach_error_m=0.005)
    sim01_pass = path01.clear and path01.within_reach and cap01.success
    results["sims"]["SIM-01"] = {
        "name": "Grapple approach & capture",
        "pass": sim01_pass,
        "path_clear": path01.clear,
        "within_reach": path01.within_reach,
        "max_range_m": round(path01.max_range_m, 4),
        "capture_success": cap01.success,
        "pos_error_m": cap01.pos_error_m,
        "att_error_deg": cap01.att_error_deg,
        "collisions": path01.collisions,
        "notes": path01.notes + cap01.notes,
        "criteria": "No collision with keep-outs; capture within tolerance",
    }

    # SIM-02 Transfer
    path02 = kin.transfer_to_site(g.site_a_issi)
    sim02_pass = path02.clear and path02.within_reach
    results["sims"]["SIM-02"] = {
        "name": "Transfer path delivery → deck",
        "pass": sim02_pass,
        "path_clear": path02.clear,
        "within_reach": path02.within_reach,
        "max_range_m": round(path02.max_range_m, 4),
        "collisions": path02.collisions,
        "notes": path02.notes,
        "criteria": "Continuous clear path under assumptions",
    }

    # SIM-03 Mate iSSI
    mate = kin.mate_issi(g.site_a_issi)
    results["sims"]["SIM-03"] = {
        "name": "Mate to deck interface (iSSI)",
        "pass": mate.success,
        "lateral_error_m": mate.lateral_error_m,
        "tilt_error_deg": mate.tilt_error_deg,
        "notes": mate.notes,
        "criteria": "Alignment within capture envelope (A-SIM-03)",
    }

    # SIM-04 Power-on
    seq = edge.power_on_sequence()
    sim04_pass = seq == ["INIT", "BASELINE", "MONITOR"]
    results["sims"]["SIM-04"] = {
        "name": "Power-on sequence",
        "pass": sim04_pass,
        "mode_sequence": seq,
        "notes": ["Mode machine INIT→BASELINE→MONITOR"],
        "criteria": "Mode INIT→BASELINE (then MONITOR ready)",
    }

    # Establish quiet baseline for anomaly detection
    quiet = sens.generate()
    edge.process(quiet, establish_baseline=True)

    # SIM-05 Anomaly injection
    anom_batch = sens.generate(inject={"vibration": 0.8, "thermal": 4.0})
    prod5 = edge.process(anom_batch)
    explain_ok = (
        "top_features" in prod5.explainability
        and "channel_ids" in prod5.explainability
        and "confidence" in prod5.explainability
    )
    sim05_pass = prod5.is_anomaly and explain_ok
    results["sims"]["SIM-05"] = {
        "name": "Anomaly injection (vib/thermal)",
        "pass": sim05_pass,
        "is_anomaly": prod5.is_anomaly,
        "anomaly_score": round(prod5.anomaly_score, 3),
        "mode": prod5.mode,
        "explainability": prod5.explainability,
        "packet_bytes": prod5.packet_bytes,
        "injected": anom_batch.anomalies_injected,
        "criteria": "Flag + explainability fields present",
    }

    # SIM-06 Channel loss
    edge.mode = Mode.MONITOR
    deg_batch = sens.generate(disabled=["visual_proxy"])
    # re-baseline not required; process with missing channel
    prod6 = edge.process(deg_batch)
    sim06_pass = prod6.mode == "DEGRADED" and len(prod6.channels_used) >= 1 and prod6.packet_bytes > 0
    results["sims"]["SIM-06"] = {
        "name": "Channel loss (visual disabled)",
        "pass": sim06_pass,
        "mode": prod6.mode,
        "channels_used": prod6.channels_used,
        "packet_bytes": prod6.packet_bytes,
        "product_continues": prod6.packet_bytes > 0,
        "notes": prod6.notes,
        "criteria": "DEGRADED mode; product continues",
    }

    # SIM-07 Remove & reinstall site B
    path07 = kin.remove_and_reinstall(g.site_a_issi, g.site_b_issi)
    mate_b = kin.mate_issi(g.site_b_issi, lateral_err_m=0.005, tilt_err_deg=2.5)
    # After reinstall, sensing still works
    edge.mode = Mode.MONITOR
    post = edge.process(sens.generate())
    sim07_pass = path07.clear and path07.within_reach and mate_b.success and post.packet_bytes > 0
    results["sims"]["SIM-07"] = {
        "name": "Remove & reinstall site B",
        "pass": sim07_pass,
        "path_clear": path07.clear,
        "within_reach": path07.within_reach,
        "max_range_m": round(path07.max_range_m, 4),
        "mate_site_b": mate_b.success,
        "post_install_product_bytes": post.packet_bytes,
        "collisions": path07.collisions,
        "notes": path07.notes + mate_b.notes + ["UC-03 multi-site reconfiguration"],
        "criteria": "UC-03 complete in script (remove A → install B + sense)",
    }

    results["summary"] = {
        "total": 7,
        "passed": sum(1 for s in results["sims"].values() if s["pass"]),
        "failed": [k for k, s in results["sims"].items() if not s["pass"]],
        "all_pass": all(s["pass"] for s in results["sims"].values()),
    }
    results["assumptions"] = ASSUMPTIONS
    results["budget_check"] = {
        "mass_design_kg": cfg.mass_power.mass_design_kg,
        "mass_team_max_kg": cfg.mass_power.mass_team_max_kg,
        "mass_ok": cfg.mass_power.mass_design_kg <= cfg.mass_power.mass_team_max_kg,
        "monitor_w": cfg.mass_power.power_monitor_avg_w,
        "peak_w": cfg.mass_power.power_diag_peak_w,
        "nte_w": cfg.mass_power.power_nte_w,
        "power_ok": cfg.mass_power.power_diag_peak_w <= cfg.mass_power.power_nte_w,
    }
    return results


def to_markdown(results: Dict[str, Any]) -> str:
    m = results["meta"]
    s = results["summary"]
    lines: List[str] = [
        "# SIM Results — MSS-ORU Digital Twin",
        "",
        f"**Generated (UTC):** {m['timestamp_utc']}  ",
        f"**Twin version:** {m['twin_version']}  ",
        f"**Interfaces:** grapple={m['interfaces']['grapple']}; install={m['interfaces']['deck_install']}  ",
        f"**Mass design:** {m['mass_design_kg']} kg · **MONITOR:** {m['power_monitor_w']} W · **Peak:** {m['power_peak_w']} W  ",
        "",
        "## Summary",
        "",
        f"| Total | Passed | All pass | Failed |",
        f"|-------|--------|----------|--------|",
        f"| {s['total']} | {s['passed']} | **{_ok(s['all_pass'])}** | {', '.join(s['failed']) if s['failed'] else '—'} |",
        "",
        "## Budget check (config)",
        "",
        f"- Mass design ≤ team max: **{_ok(results['budget_check']['mass_ok'])}** "
        f"({results['budget_check']['mass_design_kg']} ≤ {results['budget_check']['mass_team_max_kg']} kg)",
        f"- Peak ≤ NTE: **{_ok(results['budget_check']['power_ok'])}** "
        f"({results['budget_check']['peak_w']} ≤ {results['budget_check']['nte_w']} W)",
        "",
        "## Scenario results",
        "",
    ]
    for sid, sim in results["sims"].items():
        lines += [
            f"### {sid} — {sim['name']}",
            "",
            f"**Result:** {_ok(sim['pass'])}  ",
            f"**Criteria:** {sim['criteria']}",
            "",
            "```json",
            json.dumps({k: v for k, v in sim.items() if k not in ("name", "criteria")}, indent=2, default=str),
            "```",
            "",
        ]

    lines += [
        "## Geometric / power assumptions (explicit)",
        "",
        "These are **not** Motiv-published DH parameters. Unknown arm details are parameterized.",
        "",
    ]
    for aid, text in results["assumptions"].items():
        lines.append(f"- **{aid}:** {text}")

    lines += [
        "",
        "## How to reproduce",
        "",
        "```bash",
        "cd mss-oru-techleap",
        "python -m twin.run_sims",
        "```",
        "",
        "## Interpretation for Phase 1",
        "",
        "- SIM-01…03 and SIM-07 show **robotic manipulation is central** to install and multi-site value.",
        "- SIM-04…06 show edge physical-AI mode machine, anomaly explainability, and graceful degradation.",
        "- Paths are kinematic waypoints with keep-out cylinders; replace with CAD-derived corridors when available.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    results = run_all()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(to_markdown(results), encoding="utf-8")
    # also dump json next to markdown for tooling
    json_path = OUT.with_suffix(".json")
    json_path.write_text(json.dumps(results, indent=2, default=str), encoding="utf-8")
    print(f"Wrote {OUT}")
    print(f"Wrote {json_path}")
    print(f"Summary: {results['summary']['passed']}/{results['summary']['total']} PASS")
    if not results["summary"]["all_pass"]:
        print("FAILED:", results["summary"]["failed"])
        raise SystemExit(1)


if __name__ == "__main__":
    main()
