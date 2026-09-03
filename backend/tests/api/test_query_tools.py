from fastapi.testclient import TestClient

from app.main import app


def test_query_routes_to_graph_function_and_cites_node() -> None:
    body = TestClient(app).post('/api/v1/query', json={'question': 'Which shared fix has leverage?'}).json()
    assert body['tool'] == 'graph_query'
    assert body['citations'][0]['type'] == 'node'
    assert body['citations'][0]['id'] == 'vpn-gateway'


def test_query_routes_unknown_intent_to_exposed_paths() -> None:
    body = TestClient(app).post('/api/v1/query', json={'question': 'What is exposed from the internet?'}).json()
    assert body['citations'][0]['type'] == 'path'
    assert body['citations'][0]['nodes'][0] == 'internet'
