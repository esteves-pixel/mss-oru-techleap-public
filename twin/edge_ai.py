"""Edge physical-AI pipeline stub.

Sensor → Conditioning → Features → Edge model → Explainability → Interface manager
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional

import numpy as np

from twin.config import TwinConfig
from twin.sensors import SensorBatch


class Mode(str, Enum):
    INIT = "INIT"
    BASELINE = "BASELINE"
    MONITOR = "MONITOR"
    ANOMALY = "ANOMALY"
    DEGRADED = "DEGRADED"
    SAFE = "SAFE"
    DIAG_GRAPPLE = "DIAG_GRAPPLE"


@dataclass
class HealthProduct:
    mode: str
    anomaly_score: float
    is_anomaly: bool
    features: Dict[str, float]
    explainability: Dict[str, Any]
    packet_bytes: int
    channels_used: List[str]
    notes: List[str] = field(default_factory=list)


class EdgePipeline:
    def __init__(self, cfg: TwinConfig):
        self.cfg = cfg
        self.mode = Mode.INIT
        self._baseline: Dict[str, Dict[str, float]] = {}

    def power_on_sequence(self) -> List[str]:
        seq = []
        self.mode = Mode.INIT
        seq.append(self.mode.value)
        self.mode = Mode.BASELINE
        seq.append(self.mode.value)
        self.mode = Mode.MONITOR
        seq.append(self.mode.value)
        return seq

    def condition(self, batch: SensorBatch) -> Dict[str, np.ndarray]:
        out = {}
        for ch, x in batch.data.items():
            if np.all(np.isnan(x)):
                out[ch] = x
                continue
            # simple demean for vib/visual; thermal keep absolute
            if ch == "thermal":
                out[ch] = x.copy()
            else:
                m = np.nanmean(x)
                out[ch] = x - m
        return out

    def features(self, conditioned: Dict[str, np.ndarray]) -> Dict[str, float]:
        feats: Dict[str, float] = {}
        for ch, x in conditioned.items():
            if np.all(np.isnan(x)):
                continue
            finite = x[np.isfinite(x)]
            if finite.size == 0:
                continue
            feats[f"{ch}_mean"] = float(np.mean(finite))
            feats[f"{ch}_std"] = float(np.std(finite))
            feats[f"{ch}_rms"] = float(np.sqrt(np.mean(finite**2)))
            feats[f"{ch}_p2p"] = float(np.ptp(finite))
        return feats

    def set_baseline_from_features(self, feats: Dict[str, float]) -> None:
        # store mean/std proxies: use feature values as quiet baseline centers
        self._baseline = {k: {"mu": v, "sigma": max(abs(v) * 0.05, 1e-3)} for k, v in feats.items()}

    def score(self, feats: Dict[str, float]) -> tuple[float, Dict[str, float]]:
        if not self._baseline:
            # cold start: use feature stds as self-ref
            return 0.0, {}
        zmap: Dict[str, float] = {}
        for k, v in feats.items():
            b = self._baseline.get(k)
            if not b:
                continue
            zmap[k] = abs(v - b["mu"]) / b["sigma"]
        if not zmap:
            return 0.0, {}
        # max z as anomaly score (simple residual detector)
        return float(max(zmap.values())), zmap

    def process(
        self,
        batch: SensorBatch,
        force_mode: Optional[Mode] = None,
        establish_baseline: bool = False,
    ) -> HealthProduct:
        conditioned = self.condition(batch)
        feats = self.features(conditioned)
        channels_used = [c for c in batch.data if not np.all(np.isnan(batch.data[c]))]
        notes: List[str] = []

        if len(channels_used) < len(self.cfg.sensors.channels):
            self.mode = Mode.DEGRADED
            notes.append("channel_loss_detected")
        elif force_mode:
            self.mode = force_mode

        if establish_baseline:
            self.set_baseline_from_features(feats)
            notes.append("baseline_established")

        anomaly_score, zmap = self.score(feats)
        thr = self.cfg.edge.anomaly_threshold
        is_anom = anomaly_score >= thr and not establish_baseline

        if is_anom and self.mode not in (Mode.DEGRADED, Mode.SAFE):
            self.mode = Mode.ANOMALY

        # explainability: top features by z
        top = sorted(zmap.items(), key=lambda kv: kv[1], reverse=True)[:5]
        explain = {
            "top_features": [{"name": k, "z": round(v, 3)} for k, v in top],
            "channel_ids": channels_used,
            "confidence": round(min(anomaly_score / (thr + 1e-9), 1.5) / 1.5, 3),
            "threshold": thr,
            "anomaly_score": round(anomaly_score, 3),
            "mode": self.mode.value,
        }

        # packet size estimate
        if is_anom:
            pkt = self.cfg.edge.packet_anomaly_bytes
        elif feats:
            pkt = self.cfg.edge.packet_feature_bytes
        else:
            pkt = self.cfg.edge.packet_hk_bytes
        if self.mode == Mode.DEGRADED:
            pkt = min(pkt, self.cfg.edge.packet_feature_bytes)

        return HealthProduct(
            mode=self.mode.value,
            anomaly_score=anomaly_score,
            is_anomaly=is_anom,
            features={k: round(v, 6) for k, v in feats.items()},
            explainability=explain,
            packet_bytes=pkt,
            channels_used=channels_used,
            notes=notes + batch.anomalies_injected,
        )
