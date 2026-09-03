"""Conservative equivalence checks for cross-framework evidence."""

from dataclasses import dataclass
from collections.abc import Iterable

from app.domain.compliance.crosswalk import Mapping


@dataclass(frozen=True)
class EquivalenceDecision:
    accepted: bool
    reason: str
    mappings: tuple[str, ...]


def evaluate_equivalence(evidence_objective: str, mappings: Iterable[Mapping], exclusive_framework: str | None = None) -> EquivalenceDecision:
    """Accept evidence only when its objective matches and exclusivity is respected."""
    candidates = tuple(item for item in mappings if item.objective == evidence_objective)
    if not candidates:
        return EquivalenceDecision(False, "no mapping has the same control objective", ())
    if exclusive_framework and any(item.framework != exclusive_framework for item in candidates):
        return EquivalenceDecision(False, "exclusive framework evidence cannot be substituted across frameworks", tuple(item.reference for item in candidates))
    return EquivalenceDecision(True, "same-objective evidence accepted; framework obligations remain separately traceable", tuple(item.reference for item in candidates))
