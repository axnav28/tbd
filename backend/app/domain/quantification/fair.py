"""Small FAIR-inspired loss model.

FAIR separates event frequency from probable loss magnitude. Expected annual
loss (EAL) is the product of annualized loss event frequency and loss
magnitude; keeping the factors separate prevents a score from being mistaken
for a currency amount.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class AnnualLoss:
    frequency: float
    magnitude: float

    @property
    def expected_annual_loss(self) -> float:
        if self.frequency < 0 or self.magnitude < 0:
            raise ValueError("frequency and magnitude must be non-negative")
        return self.frequency * self.magnitude


def cve_likelihood(epss: float, cisa_kev: bool) -> float:
    """Convert live exploit signals into a bounded annual event likelihood.

    EPSS is a 0–1 probability for exploitation within 30 days. KEV membership
    is a strong observed-exploitation signal, so it raises the modeled factor
    while the result remains bounded at one. This is a transparent heuristic,
    not a claim that EPSS itself is an annual frequency.
    """
    if not 0 <= epss <= 1:
        raise ValueError("EPSS must be between 0 and 1")
    return min(1.0, epss * (1.25 if cisa_kev else 1.0))
