"""Simplified kinematic sequence model for MSS-ORU manipulation.

Does NOT use unpublished Motiv DH parameters. Paths are waypoint-based
in a deck frame with reach and keep-out checks (ASSUMPTIONS).
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List, Optional, Sequence, Tuple

from twin.config import GeometryConfig, TwinConfig


Vec3 = Tuple[float, float, float]


def dist(a: Vec3, b: Vec3) -> float:
    return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(3)))


def lerp(a: Vec3, b: Vec3, t: float) -> Vec3:
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, a[2] + (b[2] - a[2]) * t)


def add(a: Vec3, b: Vec3) -> Vec3:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


@dataclass
class PathResult:
    name: str
    waypoints: List[Vec3]
    samples: List[Vec3]
    clear: bool
    collisions: List[str]
    within_reach: bool
    max_range_m: float
    notes: List[str]


@dataclass
class CaptureResult:
    success: bool
    pos_error_m: float
    att_error_deg: float
    notes: List[str]


@dataclass
class MateResult:
    success: bool
    lateral_error_m: float
    tilt_error_deg: float
    notes: List[str]


class ArmKinematics:
    def __init__(self, cfg: TwinConfig):
        self.cfg = cfg
        self.g: GeometryConfig = cfg.geometry

    def sample_path(self, waypoints: Sequence[Vec3], n_per_seg: int = 20) -> List[Vec3]:
        if len(waypoints) < 2:
            return list(waypoints)
        out: List[Vec3] = []
        for i in range(len(waypoints) - 1):
            for k in range(n_per_seg):
                t = k / n_per_seg
                out.append(lerp(waypoints[i], waypoints[i + 1], t))
        out.append(waypoints[-1])
        return out

    def check_keepouts(self, samples: Sequence[Vec3]) -> List[str]:
        hits: List[str] = []
        for p in samples:
            for j, (cx, cy, cz, r) in enumerate(self.g.keepouts):
                # horizontal distance to cylinder axis
                d_xy = math.hypot(p[0] - cx, p[1] - cy)
                if d_xy < r and p[2] >= cz - 0.01:
                    hits.append(f"keepout_{j}@({p[0]:.3f},{p[1]:.3f},{p[2]:.3f})")
        # unique preserve order
        seen = set()
        uniq = []
        for h in hits:
            key = h.split("@")[0]
            if key not in seen:
                seen.add(key)
                uniq.append(h)
        return uniq

    def check_reach(self, samples: Sequence[Vec3], base: Vec3 = (0.0, 0.0, 0.2)) -> Tuple[bool, float]:
        max_r = 0.0
        for p in samples:
            max_r = max(max_r, dist(base, p))
        return max_r <= self.g.arm_reach_m, max_r

    def evaluate_path(self, name: str, waypoints: Sequence[Vec3]) -> PathResult:
        samples = self.sample_path(waypoints)
        collisions = self.check_keepouts(samples)
        within, max_r = self.check_reach(samples)
        notes = [
            f"waypoints={len(waypoints)} samples={len(samples)}",
            f"A-ARM-02 reach_limit={self.g.arm_reach_m} m max_range={max_r:.3f} m",
        ]
        if collisions:
            notes.append(f"collisions={collisions}")
        return PathResult(
            name=name,
            waypoints=list(waypoints),
            samples=samples,
            clear=len(collisions) == 0,
            collisions=collisions,
            within_reach=within,
            max_range_m=max_r,
            notes=notes,
        )

    def grapple_approach(self, target: Vec3, approach_error_m: float = 0.005) -> Tuple[PathResult, CaptureResult]:
        hover = add(target, self.g.grapple_hover_offset)
        # slight lateral offset then correct (simulates approach)
        offset_approach = (target[0] + approach_error_m, target[1], hover[2])
        wps = [
            self.g.delivery_hold,
            (self.g.delivery_hold[0], self.g.delivery_hold[1], hover[2]),
            offset_approach,
            hover,
            target,
        ]
        path = self.evaluate_path("SIM-01_grapple_approach", wps)
        pos_err = approach_error_m  # residual at capture command
        att_err = 1.0  # deg ASSUMPTION
        ok = (
            path.clear
            and path.within_reach
            and pos_err <= self.g.capture_pos_tol_m
            and att_err <= self.g.capture_att_tol_deg
        )
        cap = CaptureResult(
            success=ok,
            pos_error_m=pos_err,
            att_error_deg=att_err,
            notes=[
                f"capture_tol_pos={self.g.capture_pos_tol_m} m att={self.g.capture_att_tol_deg} deg",
                "A-IF-01 CrossLink capture modeled as tolerance check only",
            ],
        )
        return path, cap

    def transfer_to_site(self, site: Vec3) -> PathResult:
        start = self.g.delivery_hold
        mid_high = (0.5 * (start[0] + site[0]), 0.5 * (start[1] + site[1]), 0.40)
        hover = add(site, self.g.grapple_hover_offset)
        wps = [start, mid_high, hover, site]
        return self.evaluate_path("SIM-02_transfer", wps)

    def mate_issi(self, site: Vec3, lateral_err_m: float = 0.004, tilt_err_deg: float = 2.0) -> MateResult:
        ok = lateral_err_m <= self.g.mate_lateral_tol_m and tilt_err_deg <= self.g.mate_tilt_tol_deg
        return MateResult(
            success=ok,
            lateral_error_m=lateral_err_m,
            tilt_error_deg=tilt_err_deg,
            notes=[
                f"A-SIM-03 envelope lateral≤{self.g.mate_lateral_tol_m} m tilt≤{self.g.mate_tilt_tol_deg} deg",
                "D-01 primary deck install = iSSI",
            ],
        )

    def remove_and_reinstall(self, site_a: Vec3, site_b: Vec3) -> PathResult:
        hover_a = add(site_a, self.g.grapple_hover_offset)
        hover_b = add(site_b, self.g.grapple_hover_offset)
        mid = (0.0, 0.0, 0.40)
        wps = [site_a, hover_a, mid, hover_b, site_b]
        return self.evaluate_path("SIM-07_reinstall_B", wps)
