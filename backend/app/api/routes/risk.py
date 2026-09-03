"""Executive risk projections with explicit confidence provenance."""

from fastapi import APIRouter
from datetime import datetime, timezone

from app.api.deps import demo_data
from app.api.deps import audit_log
from pydantic import BaseModel, Field
from app.domain.quantification.fair import cve_likelihood
from app.domain.threat_intel.epss_client import EpssClient
from app.domain.threat_intel.kev_client import KevClient

router = APIRouter(prefix="/risk", tags=["risk"])


class RiskScoreMutation(BaseModel):
    value: float = Field(ge=0)
    confidence: str


@router.get("/summary")
def risk_summary() -> dict[str, object]:
    """Return a synthetic, clearly labelled executive risk summary."""
    data = demo_data()
    eal = {"value": 1_250_000.0, "currency": "INR", "confidence": "Estimated"}
    var = {"value": 3_100_000.0, "currency": "INR", "percentile": 0.95, "confidence": "Estimated"}
    return {"organization": data["organization"], "synthetic": True, "eal": eal, "var": var, "scenarios": 2}


@router.get("/live-feed")
def live_feed() -> dict[str, object]:
    """Return the minute-refresh feed envelope used by the command center."""
    return {"refreshed_at": datetime.now(timezone.utc).isoformat(), "source": "TBD model refresh", "synthetic": True, "events": [
        {"time": "now", "severity": "critical", "title": "Shared choke point under review", "detail": "VPN gateway intersects 2 modeled attack scenarios", "confidence": "Estimated"},
        {"time": "2m", "severity": "high", "title": "KEV signal retained", "detail": "CVE-2021-44228 remains in the Northstar synthetic inventory", "confidence": "Verified"},
        {"time": "7m", "severity": "watch", "title": "Control evidence gap", "detail": "Patch deployment is configured but not verified", "confidence": "Configured"},
    ]}


@router.get("/likelihood/{cve}")
def cve_risk_likelihood(cve: str) -> dict[str, object]:
    """Expose live EPSS and KEV signals with their calculation provenance."""
    epss = EpssClient().fetch(cve)
    kev = KevClient().is_known_exploited(cve)
    return {"cve": cve.upper(), "epss": {"value": epss.score, "confidence": "Verified", "source": epss.source}, "cisa_kev": {"value": kev, "confidence": "Verified", "source": "CISA KEV Catalog"}, "likelihood": {"value": cve_likelihood(epss.score, kev), "confidence": "Configured", "source": "EPSS + CISA KEV"}}


@router.post("/score")
def mutate_risk_score(mutation: RiskScoreMutation) -> dict[str, object]:
    event = audit_log.append("risk_score.updated", "organization", mutation.model_dump())
    return {"risk_score": mutation.model_dump(), "audit_sequence": event.sequence}
