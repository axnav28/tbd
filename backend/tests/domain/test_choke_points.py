"""Hand-check for candidate choke-point ranking."""

import networkx as nx

from app.domain.optimization.choke_points import rank_choke_points


def test_shared_gateway_ranks_above_leaf_nodes() -> None:
    # Two paths share gateway: ingress -> gateway -> database and
    # endpoint -> gateway -> database. Gateway is the expected choke point.
    graph = nx.DiGraph([
        ("ingress", "gateway"),
        ("endpoint", "gateway"),
        ("gateway", "database"),
    ])

    ranking = rank_choke_points(graph)

    assert ranking[0][0] == "gateway"
    assert ranking[0][1] > ranking[-1][1]
