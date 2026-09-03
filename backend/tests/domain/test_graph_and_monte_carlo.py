from app.domain.graph.builder import build_graph
from app.domain.graph.models import AttackScenario, NodeKind, RiskNode
from app.domain.quantification.monte_carlo import simulate_annual_losses, value_at_risk


def test_graph_preserves_stable_node_ids_and_simulation_is_reproducible() -> None:
    graph = build_graph([RiskNode("vpn", NodeKind.CONTROL, "Shared VPN")], [])
    assert graph.nodes["vpn"]["name"] == "Shared VPN"
    scenarios = [AttackScenario("s1", ("vpn",), 1.0, 100.0)]
    first = simulate_annual_losses(scenarios, runs=100, seed=3)
    second = simulate_annual_losses(scenarios, runs=100, seed=3)
    assert (first == second).all()
    assert value_at_risk(first) >= 0
