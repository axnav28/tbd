from fastapi.testclient import TestClient

from app.api.deps import audit_log
from app.main import app


def test_mutations_append_to_auditable_chain() -> None:
    client = TestClient(app)
    client.post('/api/v1/risk/score', json={'value': 10, 'confidence': 'Estimated'})
    client.post('/api/v1/compliance/control-state', json={'control_id': 'mfa', 'state': 'enabled', 'confidence': 'Configured'})
    body = client.get('/api/v1/audit').json()
    assert len(body['events']) >= 2
    assert body['chain_valid'] is True
    assert audit_log.events()[-1].action == 'control_state.updated'
