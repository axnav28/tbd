"""Budget-constrained mitigation selection with a hard Gordon–Loeb cap.

The LP maximizes quantified risk reduction with fractional action deployment,
subject to spend <= min(user budget, protected expected loss / e). The second
constraint is the Gordon–Loeb bound: under the model's assumptions, rational
security investment should not exceed roughly 37% of the expected loss it is
protecting. It is enforced in the solver, not merely displayed as guidance.
"""

from dataclasses import dataclass
from math import e

import pulp


@dataclass(frozen=True)
class Mitigation:
    id: str
    cost: float
    risk_reduction: float


@dataclass(frozen=True)
class OptimizationResult:
    selected: dict[str, float]
    spend: float
    risk_reduction: float
    max_allowed_spend: float


def optimize_investment(mitigations: list[Mitigation], expected_loss: float, budget: float) -> OptimizationResult:
    """Select action fractions that maximize reduction under both hard bounds."""
    if expected_loss < 0 or budget < 0:
        raise ValueError("expected_loss and budget must be non-negative")
    if any(action.cost < 0 or action.risk_reduction < 0 for action in mitigations):
        raise ValueError("mitigation cost and reduction must be non-negative")

    bound = min(budget, expected_loss / e)
    problem = pulp.LpProblem("bounded_cyber_risk_investment", pulp.LpMaximize)
    fractions = {action.id: pulp.LpVariable(action.id, lowBound=0.0, upBound=1.0) for action in mitigations}
    problem += pulp.lpSum(action.risk_reduction * fractions[action.id] for action in mitigations)
    problem += pulp.lpSum(action.cost * fractions[action.id] for action in mitigations) <= bound
    status = problem.solve(pulp.PULP_CBC_CMD(msg=False))
    if pulp.LpStatus[status] != "Optimal":
        raise RuntimeError(f"investment optimization failed: {pulp.LpStatus[status]}")

    selected = {action_id: float(variable.value() or 0.0) for action_id, variable in fractions.items() if (variable.value() or 0.0) > 1e-9}
    spend = sum(action.cost * selected.get(action.id, 0.0) for action in mitigations)
    reduction = sum(action.risk_reduction * selected.get(action.id, 0.0) for action in mitigations)
    return OptimizationResult(selected, spend, reduction, bound)
