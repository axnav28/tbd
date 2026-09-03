from app.domain.compliance.crosswalk import crosswalk
from app.domain.compliance.equivalence import evaluate_equivalence


def test_crosswalk_contains_all_required_frameworks() -> None:
    frameworks = {item.framework for item in crosswalk()}
    assert frameworks == {"ISO 27001:2022", "NIST CSF 2.0", "CIS Controls v8", "RBI IT Governance Directions 2023", "SEBI CSCRF"}


def test_exclusive_sebi_evidence_is_not_silently_substituted() -> None:
    mappings = crosswalk()
    decision = evaluate_equivalence("identity and access governance", mappings, exclusive_framework="SEBI CSCRF")
    assert decision.accepted is False


def test_same_objective_evidence_is_traceable() -> None:
    decision = evaluate_equivalence("vulnerability and patch management", crosswalk())
    assert decision.accepted is True
    assert "A.8.8" in decision.mappings
