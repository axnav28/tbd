"""Executable hand-check for the shared-node risk-reduction invariant.

Graph sketch:

    Internet ──> Shared VPN ──> Payments DB      (scenario S1: 100 loss)
    Laptop  ────> Shared VPN ──> HR DB            (scenario S2:  80 loss)

Both scenarios depend on the same VPN choke point. A VPN fix is credited as
40 units once in the aggregate, not 40 + 40 = 80 by summing path outputs.
The two endpoint-specific fixes remain independent and are credited separately.
"""

from app.domain.quantification.dedup import RiskContribution, deduplicate_reduction


def test_shared_node_reduction_is_credited_once() -> None:
    scenarios = {
        "S1": [RiskContribution("shared-vpn", 40.0), RiskContribution("payments-db", 20.0)],
        "S2": [RiskContribution("shared-vpn", 40.0), RiskContribution("hr-db", 10.0)],
    }

    assert deduplicate_reduction(scenarios) == 70.0
