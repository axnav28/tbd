"""Pluggable normalized telemetry connectors."""

from dataclasses import dataclass
from pathlib import Path
import csv
from collections.abc import Iterator


@dataclass(frozen=True)
class TelemetryRecord:
    source: str
    record_type: str
    record_id: str
    payload: dict[str, str]


class CsvConnector:
    """Read a CSV export into a stable connector-neutral record shape."""

    def __init__(self, path: Path, record_type: str) -> None:
        self.path = path
        self.record_type = record_type

    def records(self) -> Iterator[TelemetryRecord]:
        with self.path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            if not reader.fieldnames or "id" not in reader.fieldnames:
                raise ValueError("CSV connector requires an id column")
            for row in reader:
                record_id = row.pop("id") or ""
                if not record_id:
                    raise ValueError("CSV record id cannot be empty")
                yield TelemetryRecord(str(self.path), self.record_type, record_id, row)


class MockConnector:
    """Yield explicitly synthetic records for deterministic tests and demos."""

    def __init__(self, records: list[TelemetryRecord]) -> None:
        self._records = records

    def records(self) -> Iterator[TelemetryRecord]:
        yield from self._records
