"""Compliance route boundary; curated crosswalk arrives in Phase 6."""

from fastapi import APIRouter

router = APIRouter(prefix="/compliance", tags=["compliance"])


@router.get("")
def compliance_status() -> dict[str, object]:
    return {"status": "scaffolded", "frameworks": ["ISO 27001", "NIST CSF", "CIS Controls", "RBI", "SEBI CSCRF"], "implemented": False}
