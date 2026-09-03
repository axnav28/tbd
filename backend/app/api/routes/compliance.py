"""Compliance crosswalk API routes."""

from fastapi import APIRouter
from app.domain.compliance.crosswalk import crosswalk
from pydantic import BaseModel
from app.api.deps import audit_log

router = APIRouter(prefix="/compliance", tags=["compliance"])


class ControlStateMutation(BaseModel):
    control_id: str
    state: str
    confidence: str


@router.get("")
def compliance_status() -> dict[str, object]:
    mappings = crosswalk()
    return {"status": "curated_subset", "frameworks": sorted({item.framework for item in mappings}), "mappings": [item.__dict__ for item in mappings], "implemented": True}


@router.post("/control-state")
def mutate_control_state(mutation: ControlStateMutation) -> dict[str, object]:
    event = audit_log.append("control_state.updated", mutation.control_id, mutation.model_dump())
    return {"control": mutation.model_dump(), "audit_sequence": event.sequence}
