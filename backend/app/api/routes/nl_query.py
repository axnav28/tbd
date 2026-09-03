"""Constrained query route with node/path citations."""

from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(prefix="/query", tags=["query"])


class QueryRequest(BaseModel):
    question: str = Field(min_length=1)


@router.post("")
def query(request: QueryRequest) -> dict[str, object]:
    return {"answer": f"The query was constrained to the synthetic attack graph: {request.question}", "citations": [{"type": "path", "id": "S1", "nodes": ["asset-01", "asset-02"]}], "synthetic": True}
