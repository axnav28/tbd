"""Shared API dependencies and deterministic demo projections."""

from app.data.synthetic.generate import generate_dataset


def demo_data() -> dict[str, object]:
    """Return the explicitly synthetic dataset used by Phase 4 endpoints."""
    return generate_dataset()
