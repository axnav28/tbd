"""Bounded optimizer API route."""

from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.domain.optimization.optimizer import Mitigation, optimize_investment

router = APIRouter(prefix="/optimizer", tags=["optimizer"])


class OptimizeRequest(BaseModel):
    budget: float = Field(ge=0)
    expected_loss: float = Field(default=1_250_000.0, ge=0)


@router.post("")
def optimize(request: OptimizeRequest) -> dict[str, object]:
    result = optimize_investment([Mitigation("control-mfa-admin", 100_000, 400_000), Mitigation("control-patch-deployment", 180_000, 500_000)], request.expected_loss, request.budget)
    return {"selected": result.selected, "spend": {"value": result.spend, "currency": "INR", "confidence": "Estimated"}, "risk_reduction": {"value": result.risk_reduction, "currency": "INR", "confidence": "Estimated"}, "gordon_loeb_limit": {"value": result.max_allowed_spend, "currency": "INR", "confidence": "Configured"}}
