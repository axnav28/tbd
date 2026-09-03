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
