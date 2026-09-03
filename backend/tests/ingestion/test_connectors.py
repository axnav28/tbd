from pathlib import Path

from app.ingestion.connectors import CsvConnector


def test_csv_connector_normalizes_export(tmp_path: Path) -> None:
    source = tmp_path / "assets.csv"
    source.write_text("id,name\na-1,Loan App\n", encoding="utf-8")
    records = list(CsvConnector(source, "asset").records())
    assert records[0].record_id == "a-1"
    assert records[0].payload == {"name": "Loan App"}
