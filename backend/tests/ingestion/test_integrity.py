from app.ingestion.integrity import Confidence, ControlObservation, find_control_integrity_gaps


def test_configured_but_unverified_control_is_high_severity_finding() -> None:
    findings = find_control_integrity_gaps([ControlObservation("patch", "enabled", Confidence.CONFIGURED, False)])
    assert [(item.control_id, item.severity) for item in findings] == [("patch", "high")]
