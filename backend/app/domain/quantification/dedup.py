"""Aggregate mitigation impact without double-counting shared attack nodes.

Each contribution represents the loss reduction attributed to one graph node.
For a node appearing in several scenarios, the maximum scenario attribution is
used once. This is conservative for overlapping paths and makes the invariant
explicit: aggregate reduction is a function of unique graph nodes, not path
count. Production calibration can replace this attribution policy with an
atomic exposure decomposition while preserving the same unique-node contract.
"""

from dataclasses import dataclass
from collections.abc import Mapping, Sequence


@dataclass(frozen=True)
class RiskContribution:
    node_id: str
    reduction: float


def deduplicate_reduction(scenarios: Mapping[str, Sequence[RiskContribution]]) -> float:
    """Return the sum of each shared node's largest valid reduction once."""
    by_node: dict[str, float] = {}
    for contributions in scenarios.values():
        for contribution in contributions:
            if contribution.reduction < 0:
                raise ValueError("risk reduction cannot be negative")
            by_node[contribution.node_id] = max(by_node.get(contribution.node_id, 0.0), contribution.reduction)
    return sum(by_node.values())
