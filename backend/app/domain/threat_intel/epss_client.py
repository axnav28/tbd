"""Client for FIRST's public EPSS API."""

from dataclasses import dataclass
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen


@dataclass(frozen=True)
class EpssScore:
    cve: str
    score: float
    percentile: float
    source: str = "FIRST EPSS API"


class EpssClient:
    endpoint = "https://api.first.org/data/v1/epss"

    def fetch(self, cve: str) -> EpssScore:
        """Fetch the current 30-day exploitation probability for one CVE."""
        query = urlencode({"cve": cve.upper()})
        request = Request(f"{self.endpoint}?{query}", headers={"Accept": "application/json", "User-Agent": "tbd-cyber-risk/0.1"})
        with urlopen(request, timeout=10) as response:
            payload = json.load(response)
        rows = payload.get("data", [])
        if not rows:
            raise LookupError(f"EPSS score not found for {cve}")
        row = rows[0]
        return EpssScore(cve.upper(), float(row["epss"]), float(row["percentile"]))
