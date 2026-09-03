"""Typed entities used to construct the in-memory attack-path graph."""

from dataclasses import dataclass, field
from enum import StrEnum


class NodeKind(StrEnum):
    ASSET = "asset"
    IDENTITY = "identity"
    CONTROL = "control"
    THREAT = "threat"


@dataclass(frozen=True)
class RiskNode:
    id: str
    kind: NodeKind
    name: str
    attributes: dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class AttackScenario:
    id: str
    node_ids: tuple[str, ...]
    annual_frequency: float
    loss_magnitude: float
