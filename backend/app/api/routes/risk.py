"""Executive risk projections with explicit confidence provenance."""

from fastapi import APIRouter

from app.api.deps import demo_data

router = APIRouter(prefix="/risk", tags=["risk"])


@router.get("/summary")
def risk_summary() -> dict[str, object]:
    """Return a synthetic, clearly labelled executive risk summary."""
    data = demo_data()
    eal = {"value": 1_250_000.0, "currency": "INR", "confidence": "Estimated"}
    var = {"value": 3_100_000.0, "currency": "INR", "percentile": 0.95, "confidence": "Estimated"}
    return {"organization": data["organization"], "synthetic": True, "eal": eal, "var": var, "scenarios": 2}
