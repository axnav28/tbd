"""Graph query and what-if API routes."""

from fastapi import APIRouter, HTTPException

from app.api.deps import demo_data

router = APIRouter(prefix="/graph", tags=["graph"])


@router.get("")
def graph_snapshot() -> dict[str, object]:
    data = demo_data()
    nodes = [{"id": item["id"], "label": item["name"], "kind": item["type"], "confidence": "Configured"} for item in data["assets"]]
    return {"synthetic": True, "nodes": nodes, "edges": [{"source": "asset-01", "target": "asset-02", "confidence": "Estimated"}]}


@router.get("/nodes/{node_id}")
def graph_node(node_id: str) -> dict[str, object]:
    match = next((item for item in demo_data()["assets"] if item["id"] == node_id), None)
    if match is None:
        raise HTTPException(status_code=404, detail="graph node not found")
    return {"node": match, "citations": [{"type": "node", "id": node_id}]}


@router.post("/what-if/{node_id}")
def graph_what_if(node_id: str) -> dict[str, object]:
    if not any(item["id"] == node_id for item in demo_data()["assets"]):
        raise HTTPException(status_code=404, detail="graph node not found")
    return {"node_id": node_id, "resolved_scenarios": ["S1"], "risk_reduction": {"value": 125_000.0, "currency": "INR", "confidence": "Estimated"}, "synthetic": True}
