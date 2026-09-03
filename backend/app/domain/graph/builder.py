"""Build a directed attack graph from normalized domain records."""

import networkx as nx

from app.domain.graph.models import RiskNode


def build_graph(nodes: list[RiskNode], edges: list[tuple[str, str]]) -> nx.DiGraph:
    """Create a graph whose node IDs are stable references for later citations."""
    graph = nx.DiGraph()
    graph.add_nodes_from((node.id, {"kind": node.kind, "name": node.name, **node.attributes}) for node in nodes)
    graph.add_edges_from(edges)
    return graph
