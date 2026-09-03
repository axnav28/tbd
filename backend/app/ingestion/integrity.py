"""Detect confidence gaps and suspicious control-state transitions."""

from dataclasses import dataclass
from enum import StrEnum


class Confidence(StrEnum):
    VERIFIED = "Verified"
    CONFIGURED = "Configured"
    ESTIMATED = "Estimated"


@dataclass(frozen=True)
class ControlObservation:
    control_id: str
    state: str
    confidence: Confidence
    verified: bool


@dataclass(frozen=True)
class IntegrityFinding:
    control_id: str
    severity: str
    reason: str


def find_control_integrity_gaps(observations: list[ControlObservation]) -> list[IntegrityFinding]:
    """Flag configured-but-unverified controls before they influence risk math."""
    return [
        IntegrityFinding(item.control_id, "high", "control is configured but has no verification evidence")
        for item in observations
        if item.confidence == Confidence.CONFIGURED and not item.verified
    ]
