"""Compliance crosswalk API routes."""

from fastapi import APIRouter
from app.domain.compliance.crosswalk import crosswalk

router = APIRouter(prefix="/compliance", tags=["compliance"])


@router.get("")
def compliance_status() -> dict[str, object]:
    mappings = crosswalk()
    return {"status": "curated_subset", "frameworks": sorted({item.framework for item in mappings}), "mappings": [item.__dict__ for item in mappings], "implemented": True}
