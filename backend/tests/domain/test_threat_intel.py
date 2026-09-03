import json
from io import BytesIO

from app.domain.quantification.fair import cve_likelihood
from app.domain.threat_intel.epss_client import EpssClient
from app.domain.threat_intel.kev_client import KevClient


class FakeResponse(BytesIO):
    def __enter__(self): return self
    def __exit__(self, *_): self.close()


def test_live_signals_raise_bounded_cve_likelihood() -> None:
    assert cve_likelihood(0.8, False) == 0.8
    assert cve_likelihood(0.8, True) == 1.0


def test_epss_client_parses_first_api(monkeypatch) -> None:
    monkeypatch.setattr("app.domain.threat_intel.epss_client.urlopen", lambda *args, **kwargs: FakeResponse(json.dumps({"data": [{"epss": "0.42", "percentile": "0.80"}]}).encode()))
    score = EpssClient().fetch("CVE-2021-44228")
    assert score.cve == "CVE-2021-44228" and score.score == 0.42


def test_kev_client_matches_cve(monkeypatch) -> None:
    payload = {"vulnerabilities": [{"cveID": "CVE-2021-44228"}]}
    monkeypatch.setattr("app.domain.threat_intel.kev_client.urlopen", lambda *args, **kwargs: FakeResponse(json.dumps(payload).encode()))
    assert KevClient().is_known_exploited("CVE-2021-44228") is True
