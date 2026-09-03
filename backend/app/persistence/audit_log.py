"""Append-only hash chain for auditable risk and control mutations."""

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import hashlib
import json


@dataclass(frozen=True)
class AuditEvent:
    sequence: int
    action: str
    subject_id: str
    payload: dict[str, object]
    timestamp: str
    previous_hash: str
    event_hash: str


class AuditLog:
    """In-memory Phase 9 chain; durable SQL persistence remains a later hardening step."""

    def __init__(self) -> None:
        self._events: list[AuditEvent] = []

    def append(self, action: str, subject_id: str, payload: dict[str, object]) -> AuditEvent:
        previous_hash = self._events[-1].event_hash if self._events else "GENESIS"
        timestamp = datetime.now(timezone.utc).isoformat()
        sequence = len(self._events) + 1
        material = {"sequence": sequence, "action": action, "subject_id": subject_id, "payload": payload, "timestamp": timestamp, "previous_hash": previous_hash}
        event_hash = hashlib.sha256(json.dumps(material, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        event = AuditEvent(**material, event_hash=event_hash)
        self._events.append(event)
        return event

    def events(self) -> list[AuditEvent]:
        return list(self._events)

    def verify(self) -> bool:
        previous = "GENESIS"
        for event in self._events:
            material = {"sequence": event.sequence, "action": event.action, "subject_id": event.subject_id, "payload": event.payload, "timestamp": event.timestamp, "previous_hash": previous}
            expected = hashlib.sha256(json.dumps(material, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
            if event.previous_hash != previous or event.event_hash != expected:
                return False
            previous = event.event_hash
        return True
