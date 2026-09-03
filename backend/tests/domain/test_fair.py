from app.domain.quantification.fair import AnnualLoss


def test_fair_expected_annual_loss_is_frequency_times_magnitude() -> None:
    assert AnnualLoss(frequency=0.2, magnitude=500_000).expected_annual_loss == 100_000
