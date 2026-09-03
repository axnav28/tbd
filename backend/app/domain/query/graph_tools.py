"""Function-style tools over the attack graph.

The query layer is deliberately narrow: intent selection chooses one of these
domain functions, rather than allowing a free-floating model to invent facts.
Each tool returns citation IDs that resolve to graph nodes or paths.
"""

from dataclasses import dataclass
import networkx as nx


@dataclass(frozen=True)
class QueryResult:
    answer: str
    citations: list[dict[str, object]]


def _graph() -> nx.DiGraph:
    graph = nx.DiGraph()
    graph.add_edges_from([
        ("internet", "vpn-gateway"), ("endpoint-pool", "vpn-gateway"),
        ("vpn-gateway", "loan-app"), ("loan-app", "payment-adjacent"),
        ("vpn-gateway", "hr-system"),
    ])
    return graph


def highest_leverage_node() -> QueryResult:
    graph = _graph()
    node = max(nx.betweenness_centrality(graph), key=nx.betweenness_centrality(graph).get)
    return QueryResult("The VPN gateway is the highest-leverage shared node in the current model.", [{"type": "node", "id": node, "label": "VPN gateway"}])


def exposed_paths() -> QueryResult:
    graph = _graph()
    paths = list(nx.all_simple_paths(graph, "internet", "payment-adjacent"))
    return QueryResult(f"The model contains {len(paths)} internet-to-payment attack path(s).", [{"type": "path", "id": "internet-to-payment", "nodes": paths[0]}])


def answer_question(question: str) -> QueryResult:
    """Select a whitelisted graph function using transparent intent rules."""
    normalized = question.casefold()
    if any(term in normalized for term in ("shared", "choke", "leverage", "fix")):
        return highest_leverage_node()
    return exposed_paths()
