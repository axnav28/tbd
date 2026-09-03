"""Client for CISA's authoritative Known Exploited Vulnerabilities catalog."""

import json
from urllib.request import Request, urlopen


class KevClient:
    endpoint = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"

    def is_known_exploited(self, cve: str) -> bool:
        """Return whether CISA currently lists the CVE as exploited in the wild."""
        request = Request(self.endpoint, headers={"Accept": "application/json", "User-Agent": "tbd-cyber-risk/0.1"})
        with urlopen(request, timeout=15) as response:
            payload = json.load(response)
        return any(item.get("cveID") == cve.upper() for item in payload.get("vulnerabilities", []))
