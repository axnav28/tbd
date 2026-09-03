from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_risk_summary_tags_all_figures() -> None:
    body = client.get("/api/v1/risk/summary").json()
    assert body["synthetic"] is True
    assert body["eal"]["confidence"] == "Estimated"
    assert body["var"]["confidence"] == "Estimated"


def test_optimizer_never_exceeds_gordon_loeb_bound() -> None:
    body = client.post("/api/v1/optimizer", json={"budget": 999_999_999, "expected_loss": 100}).json()
    assert body["spend"]["value"] <= body["gordon_loeb_limit"]["value"] + 1e-6


def test_query_contains_graph_citation() -> None:
    body = client.post("/api/v1/query", json={"question": "what is exposed?"}).json()
    assert body["citations"][0]["type"] == "path"


def test_compliance_route_returns_curated_mappings() -> None:
    body = client.get("/api/v1/compliance").json()
    assert body["implemented"] is True
    assert len(body["mappings"]) >= 8
