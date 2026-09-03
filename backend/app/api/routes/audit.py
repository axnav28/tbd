"""Read-only audit route boundary."""

from fastapi import APIRouter

router = APIRouter(prefix="/audit", tags=["audit"])


@router.get("")
def audit_events() -> dict[str, object]:
    return {"events": [], "status": "not_mutating_in_phase_4"}
