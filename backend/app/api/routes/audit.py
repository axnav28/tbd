"""Read-only audit API and integrity status."""

from fastapi import APIRouter
from app.api.deps import audit_log

router = APIRouter(prefix="/audit", tags=["audit"])


@router.get("")
def audit_events() -> dict[str, object]:
    return {"events": [event.__dict__ for event in audit_log.events()], "chain_valid": audit_log.verify()}
