"""Constrained query route with node/path citations."""

from fastapi import APIRouter
from pydantic import BaseModel, Field
from app.domain.query.graph_tools import answer_question

router = APIRouter(prefix="/query", tags=["query"])


class QueryRequest(BaseModel):
    question: str = Field(min_length=1)


@router.post("")
def query(request: QueryRequest) -> dict[str, object]:
    result = answer_question(request.question)
    return {"answer": result.answer, "citations": result.citations, "synthetic": True, "tool": "graph_query"}
