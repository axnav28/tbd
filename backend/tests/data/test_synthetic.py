from app.data.synthetic.generate import generate_dataset


def test_dataset_is_structurally_realistic_and_explicitly_synthetic() -> None:
    data = generate_dataset()
    assert data["synthetic"] is True
    assert len(data["assets"]) == 34
    assert len(data["vulnerabilities"]) == 16
    assert sum(item["cisa_kev"] for item in data["vulnerabilities"]) >= 3
    assert any(item["confidence"] == "Configured" and not item["verified"] for item in data["controls"])
