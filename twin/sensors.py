"""Sensor time-series simulator with injectable anomalies."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional

import numpy as np

from twin.config import TwinConfig


@dataclass
class SensorBatch:
    t: np.ndarray
    data: Dict[str, np.ndarray]
    anomalies_injected: List[str]
    disabled: List[str]


class SensorSimulator:
    def __init__(self, cfg: TwinConfig, rng: Optional[np.random.Generator] = None):
        self.cfg = cfg
        self.rng = rng or np.random.default_rng(cfg.seed)

    def generate(
        self,
        inject: Optional[Dict[str, float]] = None,
        disabled: Optional[List[str]] = None,
    ) -> SensorBatch:
        """
        inject: channel -> anomaly amplitude multiplier (z-like bump)
        disabled: channels forced to NaN (failure)
        """
        inject = inject or {}
        disabled = disabled or []
        sc = self.cfg.sensors
        n = int(sc.fs_hz * sc.duration_s)
        t = np.arange(n) / sc.fs_hz
        data: Dict[str, np.ndarray] = {}
        injected: List[str] = []

        for ch in sc.channels:
            if ch in disabled:
                data[ch] = np.full(n, np.nan)
                continue
            noise = sc.noise[ch]
            if ch == "thermal":
                base = sc.thermal_baseline_k + 0.3 * np.sin(2 * np.pi * 0.05 * t)
                sig = base + self.rng.normal(0, noise, n)
            elif ch == "vibration":
                sig = self.rng.normal(0, noise, n) + 0.02 * np.sin(2 * np.pi * 12 * t)
            else:  # visual_proxy: scalar "scene residual" feature proxy
                sig = self.rng.normal(0, noise, n)

            if ch in inject:
                # mid-window step/bump anomaly
                amp = inject[ch]
                i0, i1 = n // 3, 2 * n // 3
                if ch == "thermal":
                    sig[i0:i1] += amp  # Kelvin step
                elif ch == "vibration":
                    sig[i0:i1] += amp * np.sin(2 * np.pi * 40 * t[i0:i1])
                else:
                    sig[i0:i1] += amp
                injected.append(f"{ch}:{amp}")

            data[ch] = sig

        return SensorBatch(t=t, data=data, anomalies_injected=injected, disabled=list(disabled))
