"""The optimizer must fail closed at the Gordon–Loeb investment bound."""

from app.domain.optimization.optimizer import Mitigation, optimize_investment


def test_optimizer_caps_spend_at_one_over_e_of_expected_loss() -> None:
    # An unconstrained optimizer would spend 80 against a protected EAL of 100.
    # Gordon–Loeb bounds rational security spend at EAL / e ≈ 36.79.
    result = optimize_investment(
        [Mitigation("expensive-choke-point", cost=80.0, risk_reduction=100.0)],
        expected_loss=100.0,
        budget=100.0,
    )

    assert result.spend <= 100.0 / 2.718281828459045 + 1e-6
    assert result.spend < 80.0


def test_optimizer_respects_user_budget_when_budget_is_binding() -> None:
    result = optimize_investment(
        [
            Mitigation("mfa", cost=80.0, risk_reduction=90.0),
            Mitigation("patch", cost=80.0, risk_reduction=70.0),
        ],
        expected_loss=1_000.0,
        budget=100.0,
    )

    assert result.max_allowed_spend == 100.0
    assert result.spend <= 100.0 + 1e-6
    assert result.risk_reduction > 0


def test_optimizer_objective_is_quantified_reduction_not_rank_score() -> None:
    result = optimize_investment(
        [
            Mitigation("central-but-low-impact", cost=50.0, risk_reduction=10.0),
            Mitigation("less-central-high-impact", cost=50.0, risk_reduction=40.0),
        ],
        expected_loss=1_000.0,
        budget=50.0,
    )

    assert result.selected == {"less-central-high-impact": 1.0}
