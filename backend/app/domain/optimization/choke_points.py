"""Identify graph nodes that sit on many attack paths."""

import networkx as nx


def rank_choke_points(graph: nx.DiGraph) -> list[tuple[str, float]]:
    """Return nodes ordered by normalized betweenness centrality."""
    scores = nx.betweenness_centrality(graph, normalized=True)
    return sorted(scores.items(), key=lambda item: (-item[1], item[0]))
