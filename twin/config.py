"""
MSS-ORU digital twin configuration.

All geometric and power parameters are ASSUMPTIONS unless noted.
Unpublished Motiv DH / force / workspace limits are parameterized — not claimed as facts.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Tuple


# --- Assumption IDs (mirror docs/engineering/10_BUDGETS.md & D-01) ---

ASSUMPTIONS: Dict[str, str] = {
    "A-ARM-01": "Arm handling prefers mass ≤20 kg; design ~15 kg",
    "A-ARM-02": "Simplified arm reach treated as spherical radius 1.2 m (NOT official DH)",
    "A-ARM-03": "Transfer path is piecewise-linear waypoints in deck frame (kinematic only)",
    "A-ARM-04": "Grapple capture tolerance ±15 mm position, ±5 deg attitude (ASSUMPTION)",
    "A-IF-01": "Passive CrossLink mates active CrossLink EE",
    "A-IF-02": "Primary deck install is iSSI (D-01)",
    "A-SIM-01": "Keep-out cylinders around solar array brackets and launch locks",
    "A-SIM-03": "iSSI capture envelope: 10 mm lateral, 5 deg tilt",
    "A-B-04": "MONITOR average power design point 28 W",
    "A-B-03": "Peak power design point 65 W, NTE 80 W",
    "A-D-03": "Anomaly event packet target 1–4 kB",
}


@dataclass
class MassPowerConfig:
    mass_cbe_kg: float = 13.05
    mass_margin_frac: float = 0.15
    mass_design_kg: float = 15.01
    mass_team_max_kg: float = 25.0
    power_safe_w: float = 3.0
    power_monitor_avg_w: float = 28.0
    power_inference_peak_w: float = 55.0
    power_diag_peak_w: float = 65.0
    power_nte_w: float = 80.0


@dataclass
class GeometryConfig:
    """Deck-frame meters. Origin = deck CSYS (Motiv pack)."""

    # Sites (ASSUMPTION — illustrative, not Motiv coordinates)
    delivery_hold: Tuple[float, float, float] = (0.80, 0.00, 0.35)
    site_a_issi: Tuple[float, float, float] = (0.15, 0.10, 0.05)
    site_b_issi: Tuple[float, float, float] = (-0.15, 0.10, 0.05)
    grapple_hover_offset: Tuple[float, float, float] = (0.0, 0.0, 0.12)

    # Keep-outs: (x, y, z, radius) cylinders along +Z (simplified)
    keepouts: List[Tuple[float, float, float, float]] = field(
        default_factory=lambda: [
            (0.40, 0.30, 0.0, 0.08),  # solar array bracket proxy
            (0.40, -0.30, 0.0, 0.08),
            (-0.40, 0.30, 0.0, 0.08),
            (-0.40, -0.30, 0.0, 0.08),
            (0.0, -0.35, 0.0, 0.06),  # launch lock cluster proxy
        ]
    )

    capture_pos_tol_m: float = 0.015
    capture_att_tol_deg: float = 5.0
    mate_lateral_tol_m: float = 0.010
    mate_tilt_tol_deg: float = 5.0
    arm_reach_m: float = 1.2  # A-ARM-02 — not official


@dataclass
class SensorConfig:
    fs_hz: float = 50.0
    duration_s: float = 10.0
    channels: Tuple[str, ...] = ("visual_proxy", "thermal", "vibration")
    # Quiet baseline noise (std)
    noise: Dict[str, float] = field(
        default_factory=lambda: {
            "visual_proxy": 0.02,
            "thermal": 0.15,  # K
            "vibration": 0.05,  # g
        }
    )
    thermal_baseline_k: float = 293.15


@dataclass
class EdgeConfig:
    anomaly_threshold: float = 3.0  # z-score-like
    packet_hk_bytes: int = 96
    packet_feature_bytes: int = 1024
    packet_anomaly_bytes: int = 2048


@dataclass
class TwinConfig:
    mass_power: MassPowerConfig = field(default_factory=MassPowerConfig)
    geometry: GeometryConfig = field(default_factory=GeometryConfig)
    sensors: SensorConfig = field(default_factory=SensorConfig)
    edge: EdgeConfig = field(default_factory=EdgeConfig)
    seed: int = 42
    interfaces: Dict[str, str] = field(
        default_factory=lambda: {
            "grapple": "Passive CrossLink x2",
            "deck_install": "iSSI",
            "optional": "FuseBlox Passive",
        }
    )


DEFAULT = TwinConfig()
