"""Generate clearly labelled, structurally realistic Northstar demo telemetry."""

import json
from pathlib import Path
from random import Random


KEV_CVES = {"CVE-2021-44228", "CVE-2021-26855", "CVE-2023-34362", "CVE-2023-35078"}
CVE_CATALOG = [
    ("CVE-2021-44228", 10.0, 0.975), ("CVE-2021-26855", 9.8, 0.970),
    ("CVE-2023-34362", 9.8, 0.980), ("CVE-2023-35078", 10.0, 0.960),
    ("CVE-2022-26134", 9.8, 0.970), ("CVE-2021-41773", 7.5, 0.940),
    ("CVE-2022-1388", 9.8, 0.960), ("CVE-2020-1472", 10.0, 0.980),
    ("CVE-2019-0708", 9.8, 0.950), ("CVE-2023-23397", 9.8, 0.970),
    ("CVE-2024-3400", 10.0, 0.940), ("CVE-2024-21762", 9.8, 0.930),
    ("CVE-2024-27198", 10.0, 0.910), ("CVE-2022-30190", 7.8, 0.890),
    ("CVE-2021-21985", 9.8, 0.900), ("CVE-2022-42475", 9.8, 0.920),
]


def generate_dataset(seed: int = 26105) -> dict[str, object]:
    """Return deterministic synthetic records; no record is enterprise telemetry."""
    random = Random(seed)
    asset_types = ["app-server"] * 10 + ["database"] * 6 + ["laptop-pool"] * 2 + ["internal-system"] * 8 + ["network-service"] * 8
    assets = [{"id": f"asset-{index:02d}", "name": ("payment-gateway-adjacent-ledger" if index == 1 else f"northstar-{kind}-{index:02d}"), "type": kind, "synthetic": True} for index, kind in enumerate(asset_types, 1)]
    assets[0]["name"] = "loan-origination-web-app"
    vulnerabilities = [{"id": cve, "asset_id": assets[index % len(assets)]["id"], "cvss": cvss, "epss": epss, "cisa_kev": cve in KEV_CVES, "source": "public-demo-catalog"} for index, (cve, cvss, epss) in enumerate(CVE_CATALOG)]
    controls = [
        {"id": "control-mfa-admin", "name": "MFA on privileged accounts", "confidence": "Verified", "verified": True},
        {"id": "control-patch-deployment", "name": "Patch deployment status", "confidence": "Configured", "verified": False},
        {"id": "control-segmentation", "name": "Endpoint pool to payment-adjacent segmentation", "confidence": "Verified", "verified": True},
        {"id": "control-edr", "name": "Monitoring / EDR coverage", "confidence": "Estimated", "verified": False},
    ]
    return {"organization": "Northstar Finance (fictional)", "synthetic": True, "seed": seed, "assets": assets, "vulnerabilities": vulnerabilities, "identities": [{"id": f"user-{i}", "role": "admin" if i <= 3 else "standard"} for i in range(1, 9)], "controls": controls, "metadata": {"generated_by": "generate_dataset", "random_check": random.random()}}


def write_dataset(output: Path, seed: int = 26105) -> None:
    output.write_text(json.dumps(generate_dataset(seed), indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    write_dataset(Path("northstar-demo.json"))
