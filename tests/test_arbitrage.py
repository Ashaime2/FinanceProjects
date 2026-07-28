import math

import pytest

from src.arbitrage import (
    actualized_strike,
    arbitrage_gap,
    arbitrage_strategy,
    opportunity_finder,
)


def test_actualized_strike():
    strike = 100.0
    rate = 0.05
    maturity = 2.0

    assert actualized_strike(strike, rate, maturity) == pytest.approx(
        strike * math.exp(-rate * maturity)
    )


def test_arbitrage_gap_when_put_call_parity_holds():
    spot_price = 100.0
    strike = 100.0
    rate = 0.05
    maturity = 1.0
    put_premium = 5.0
    call_premium = (
        put_premium
        + spot_price
        - strike * math.exp(-rate * maturity)
    )

    assert arbitrage_gap(
        call_premium,
        put_premium,
        spot_price,
        strike,
        rate,
        maturity,
    ) == pytest.approx(0.0)


def test_positive_arbitrage_gap():
    assert arbitrage_gap(
        call_premium=12.0,
        put_premium=2.0,
        spot_price=100.0,
        strike=100.0,
        rate=0.0,
        maturity=1.0,
    ) == pytest.approx(10.0)


def test_negative_arbitrage_gap():
    assert arbitrage_gap(
        call_premium=2.0,
        put_premium=12.0,
        spot_price=100.0,
        strike=100.0,
        rate=0.0,
        maturity=1.0,
    ) == pytest.approx(-10.0)


def test_opportunity_finder_returns_positive_gap():
    gap = opportunity_finder(
        call_premium=12.0,
        put_premium=2.0,
        spot_price=100.0,
        strike=100.0,
        rate=0.0,
        maturity=1.0,
    )

    assert gap == pytest.approx(10.0)


def test_opportunity_finder_returns_negative_gap():
    gap = opportunity_finder(
        call_premium=2.0,
        put_premium=12.0,
        spot_price=100.0,
        strike=100.0,
        rate=0.0,
        maturity=1.0,
    )

    assert gap == pytest.approx(-10.0)


@pytest.mark.parametrize("gap", [-1e-8, 0.0, 1e-8])
def test_opportunity_finder_ignores_gap_within_tolerance(gap):
    result = opportunity_finder(
        call_premium=5.0 + gap,
        put_premium=5.0,
        spot_price=100.0,
        strike=100.0,
        rate=0.0,
        maturity=1.0,
        epsilon=1e-8,
    )

    assert result == 0.0


def test_gap_just_above_tolerance_is_detected():
    result = opportunity_finder(
        call_premium=5.0 + 2e-8,
        put_premium=5.0,
        spot_price=100.0,
        strike=100.0,
        rate=0.0,
        maturity=1.0,
        epsilon=1e-8,
    )

    assert result == pytest.approx(2e-8)


def test_strategy_when_there_is_no_arbitrage():
    result = arbitrage_strategy(
        call_premium=5.0,
        put_premium=5.0,
        spot_price=100.0,
        strike=100.0,
        rate=0.0,
        maturity=1.0,
    )

    assert result == {
        "opportunity": False,
        "gap": 0.0,
        "initial_profit": 0.0,
        "strategy": "No arbitrage found",
    }


def test_strategy_for_positive_gap():
    result = arbitrage_strategy(
        call_premium=12.0,
        put_premium=2.0,
        spot_price=100.0,
        strike=100.0,
        rate=0.0,
        maturity=1.0,
    )

    assert result["opportunity"] is True
    assert result["gap"] == pytest.approx(10.0)
    assert result["initial_profit"] == pytest.approx(10.0)
    assert "Vendre le call" in result["strategy"]
    assert "emprunter PV(K)" in result["strategy"]


def test_strategy_for_negative_gap():
    result = arbitrage_strategy(
        call_premium=2.0,
        put_premium=12.0,
        spot_price=100.0,
        strike=100.0,
        rate=0.0,
        maturity=1.0,
    )

    assert result["opportunity"] is True
    assert result["gap"] == pytest.approx(-10.0)
    assert result["initial_profit"] == pytest.approx(10.0)
    assert "Acheter le call" in result["strategy"]
    assert "placer PV(K)" in result["strategy"]


@pytest.mark.parametrize(
    ("strike", "rate", "maturity"),
    [
        (-1.0, 0.05, 1.0),
        (100.0, 0.05, -1.0),
    ],
)
def test_actualized_strike_rejects_invalid_arguments(
    strike,
    rate,
    maturity,
):
    with pytest.raises(ValueError):
        actualized_strike(strike, rate, maturity)


@pytest.mark.parametrize(
    (
        "call_premium",
        "put_premium",
        "spot_price",
        "strike",
        "maturity",
    ),
    [
        (-1.0, 5.0, 100.0, 100.0, 1.0),
        (5.0, -1.0, 100.0, 100.0, 1.0),
        (5.0, 5.0, -1.0, 100.0, 1.0),
        (5.0, 5.0, 100.0, -1.0, 1.0),
        (5.0, 5.0, 100.0, 100.0, -1.0),
    ],
)
def test_arbitrage_gap_rejects_invalid_arguments(
    call_premium,
    put_premium,
    spot_price,
    strike,
    maturity,
):
    with pytest.raises(ValueError):
        arbitrage_gap(
            call_premium,
            put_premium,
            spot_price,
            strike,
            rate=0.05,
            maturity=maturity,
        )


def test_opportunity_finder_rejects_negative_epsilon():
    with pytest.raises(ValueError):
        opportunity_finder(
            call_premium=5.0,
            put_premium=5.0,
            spot_price=100.0,
            strike=100.0,
            rate=0.05,
            maturity=1.0,
            epsilon=-1e-8,
        )


def test_negative_interest_rate_is_allowed():
    result = actualized_strike(
        strike=100.0,
        rate=-0.02,
        maturity=1.0,
    )

    assert result == pytest.approx(100.0 * math.exp(0.02))