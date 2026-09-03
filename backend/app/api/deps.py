"""Shared API dependencies and deterministic demo projections."""

from app.data.synthetic.generate import generate_dataset
from app.persistence.audit_log import AuditLog

audit_log = AuditLog()


def demo_data() -> dict[str, object]:
    """Return the explicitly synthetic dataset used by Phase 4 endpoints."""
    return generate_dataset()
