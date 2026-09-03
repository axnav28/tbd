"""Monte Carlo sampling over scenario losses derived from graph paths."""

from collections.abc import Sequence

import numpy as np

from app.domain.graph.models import AttackScenario


def simulate_annual_losses(scenarios: Sequence[AttackScenario], runs: int = 10_000, seed: int = 7) -> np.ndarray:
    """Sample aggregate annual loss using Poisson event counts per scenario."""
    if runs <= 0:
        raise ValueError("runs must be positive")
    generator = np.random.default_rng(seed)
    result = np.zeros(runs, dtype=float)
    for scenario in scenarios:
        if scenario.annual_frequency < 0 or scenario.loss_magnitude < 0:
            raise ValueError("scenario inputs must be non-negative")
        result += generator.poisson(scenario.annual_frequency, runs) * scenario.loss_magnitude
    return result


def value_at_risk(losses: np.ndarray, percentile: float = 0.95) -> float:
    """Return the loss percentile used as a transparent VaR estimate."""
    if not 0 < percentile < 1 or losses.size == 0:
        raise ValueError("percentile must be between 0 and 1 and losses cannot be empty")
    return float(np.quantile(losses, percentile))
