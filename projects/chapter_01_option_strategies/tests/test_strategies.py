import pytest

from src.portfolio import Portfolio
from src.strategies import (
    long_call,
    long_put,
    bull_call_spread,
    bear_put_spread,
    long_straddle,
)


# ============================================================
# Long call
# ============================================================

def test_long_call_returns_portfolio():
    portfolio = long_call(
        strike=100,
        premium=5,
    )

    assert isinstance(portfolio, Portfolio)


def test_long_call_contains_correct_position():
    portfolio = long_call(
        strike=100,
        premium=5,
        quantity=2,
    )

    assert len(portfolio.positions) == 1

    position = portfolio.positions[0]

    assert position.kind == "call"
    assert position.strike == 100
    assert position.quantity == 2
    assert position.premium == 5


def test_long_call_default_quantity():
    portfolio = long_call(
        strike=100,
        premium=5,
    )

    assert portfolio.positions[0].quantity == 1.0


def test_long_call_payoff():
    portfolio = long_call(
        strike=100,
        premium=5,
        quantity=2,
    )

    assert portfolio.payoff_total(90) == pytest.approx(0)
    assert portfolio.payoff_total(100) == pytest.approx(0)
    assert portfolio.payoff_total(120) == pytest.approx(40)


def test_long_call_initial_cost():
    portfolio = long_call(
        strike=100,
        premium=5,
        quantity=2,
    )

    assert portfolio.initial_cost_total() == pytest.approx(10)


def test_long_call_rejects_non_positive_quantity():
    with pytest.raises(ValueError):
        long_call(
            strike=100,
            premium=5,
            quantity=0,
        )

    with pytest.raises(ValueError):
        long_call(
            strike=100,
            premium=5,
            quantity=-1,
        )


# ============================================================
# Long put
# ============================================================

def test_long_put_returns_portfolio():
    portfolio = long_put(
        strike=100,
        premium=6,
    )

    assert isinstance(portfolio, Portfolio)


def test_long_put_contains_correct_position():
    portfolio = long_put(
        strike=100,
        premium=6,
        quantity=3,
    )

    assert len(portfolio.positions) == 1

    position = portfolio.positions[0]

    assert position.kind == "put"
    assert position.strike == 100
    assert position.quantity == 3
    assert position.premium == 6


def test_long_put_payoff():
    portfolio = long_put(
        strike=100,
        premium=6,
        quantity=2,
    )

    assert portfolio.payoff_total(120) == pytest.approx(0)
    assert portfolio.payoff_total(100) == pytest.approx(0)
    assert portfolio.payoff_total(80) == pytest.approx(40)


def test_long_put_initial_cost():
    portfolio = long_put(
        strike=100,
        premium=6,
        quantity=2,
    )

    assert portfolio.initial_cost_total() == pytest.approx(12)


def test_long_put_rejects_non_positive_quantity():
    with pytest.raises(ValueError):
        long_put(
            strike=100,
            premium=6,
            quantity=0,
        )

    with pytest.raises(ValueError):
        long_put(
            strike=100,
            premium=6,
            quantity=-2,
        )


# ============================================================
# Bull call spread
# ============================================================

def test_bull_call_spread_contains_correct_positions():
    portfolio = bull_call_spread(
        lower_strike=90,
        lower_premium=12,
        upper_strike=110,
        upper_premium=4,
        quantity=2,
    )

    assert len(portfolio.positions) == 2

    long_call_position = portfolio.positions[0]
    short_call_position = portfolio.positions[1]

    assert long_call_position.kind == "call"
    assert long_call_position.strike == 90
    assert long_call_position.quantity == 2
    assert long_call_position.premium == 12

    assert short_call_position.kind == "call"
    assert short_call_position.strike == 110
    assert short_call_position.quantity == -2
    assert short_call_position.premium == 4


def test_bull_call_spread_initial_cost():
    portfolio = bull_call_spread(
        lower_strike=90,
        lower_premium=12,
        upper_strike=110,
        upper_premium=4,
        quantity=2,
    )

    # Achat : 2 × 12 = 24
    # Vente : -2 × 4 = -8
    # Coût net : 16
    assert portfolio.initial_cost_total() == pytest.approx(16)


def test_bull_call_spread_payoff_below_lower_strike():
    portfolio = bull_call_spread(
        lower_strike=90,
        lower_premium=12,
        upper_strike=110,
        upper_premium=4,
    )

    assert portfolio.payoff_total(80) == pytest.approx(0)


def test_bull_call_spread_payoff_between_strikes():
    portfolio = bull_call_spread(
        lower_strike=90,
        lower_premium=12,
        upper_strike=110,
        upper_premium=4,
    )

    assert portfolio.payoff_total(100) == pytest.approx(10)


def test_bull_call_spread_payoff_above_upper_strike():
    portfolio = bull_call_spread(
        lower_strike=90,
        lower_premium=12,
        upper_strike=110,
        upper_premium=4,
    )

    assert portfolio.payoff_total(130) == pytest.approx(20)


def test_bull_call_spread_rejects_invalid_strike_order():
    with pytest.raises(ValueError):
        bull_call_spread(
            lower_strike=110,
            lower_premium=4,
            upper_strike=90,
            upper_premium=12,
        )

    with pytest.raises(ValueError):
        bull_call_spread(
            lower_strike=100,
            lower_premium=8,
            upper_strike=100,
            upper_premium=6,
        )


def test_bull_call_spread_rejects_non_positive_quantity():
    with pytest.raises(ValueError):
        bull_call_spread(
            lower_strike=90,
            lower_premium=12,
            upper_strike=110,
            upper_premium=4,
            quantity=0,
        )


# ============================================================
# Bear put spread
# ============================================================

def test_bear_put_spread_contains_correct_positions():
    portfolio = bear_put_spread(
        lower_strike=90,
        lower_premium=3,
        upper_strike=110,
        upper_premium=11,
        quantity=2,
    )

    assert len(portfolio.positions) == 2

    long_put_position = portfolio.positions[0]
    short_put_position = portfolio.positions[1]

    assert long_put_position.kind == "put"
    assert long_put_position.strike == 110
    assert long_put_position.quantity == 2
    assert long_put_position.premium == 11

    assert short_put_position.kind == "put"
    assert short_put_position.strike == 90
    assert short_put_position.quantity == -2
    assert short_put_position.premium == 3


def test_bear_put_spread_initial_cost():
    portfolio = bear_put_spread(
        lower_strike=90,
        lower_premium=3,
        upper_strike=110,
        upper_premium=11,
        quantity=2,
    )

    # Achat : 2 × 11 = 22
    # Vente : -2 × 3 = -6
    # Coût net : 16
    assert portfolio.initial_cost_total() == pytest.approx(16)


def test_bear_put_spread_payoff_above_upper_strike():
    portfolio = bear_put_spread(
        lower_strike=90,
        lower_premium=3,
        upper_strike=110,
        upper_premium=11,
    )

    assert portfolio.payoff_total(120) == pytest.approx(0)


def test_bear_put_spread_payoff_between_strikes():
    portfolio = bear_put_spread(
        lower_strike=90,
        lower_premium=3,
        upper_strike=110,
        upper_premium=11,
    )

    assert portfolio.payoff_total(100) == pytest.approx(10)


def test_bear_put_spread_payoff_below_lower_strike():
    portfolio = bear_put_spread(
        lower_strike=90,
        lower_premium=3,
        upper_strike=110,
        upper_premium=11,
    )

    assert portfolio.payoff_total(70) == pytest.approx(20)


def test_bear_put_spread_rejects_invalid_strike_order():
    with pytest.raises(ValueError):
        bear_put_spread(
            lower_strike=110,
            lower_premium=11,
            upper_strike=90,
            upper_premium=3,
        )

    with pytest.raises(ValueError):
        bear_put_spread(
            lower_strike=100,
            lower_premium=5,
            upper_strike=100,
            upper_premium=7,
        )


def test_bear_put_spread_rejects_non_positive_quantity():
    with pytest.raises(ValueError):
        bear_put_spread(
            lower_strike=90,
            lower_premium=3,
            upper_strike=110,
            upper_premium=11,
            quantity=-1,
        )


# ============================================================
# Long straddle
# ============================================================

def test_long_straddle_contains_correct_positions():
    portfolio = long_straddle(
        strike=100,
        call_premium=6,
        put_premium=5,
        quantity=2,
    )

    assert len(portfolio.positions) == 2

    call_position = portfolio.positions[0]
    put_position = portfolio.positions[1]

    assert call_position.kind == "call"
    assert call_position.strike == 100
    assert call_position.quantity == 2
    assert call_position.premium == 6

    assert put_position.kind == "put"
    assert put_position.strike == 100
    assert put_position.quantity == 2
    assert put_position.premium == 5


def test_long_straddle_initial_cost():
    portfolio = long_straddle(
        strike=100,
        call_premium=6,
        put_premium=5,
        quantity=2,
    )

    assert portfolio.initial_cost_total() == pytest.approx(22)


def test_long_straddle_payoff_below_strike():
    portfolio = long_straddle(
        strike=100,
        call_premium=6,
        put_premium=5,
    )

    assert portfolio.payoff_total(80) == pytest.approx(20)


def test_long_straddle_payoff_at_strike():
    portfolio = long_straddle(
        strike=100,
        call_premium=6,
        put_premium=5,
    )

    assert portfolio.payoff_total(100) == pytest.approx(0)


def test_long_straddle_payoff_above_strike():
    portfolio = long_straddle(
        strike=100,
        call_premium=6,
        put_premium=5,
    )

    assert portfolio.payoff_total(125) == pytest.approx(25)


def test_long_straddle_rejects_non_positive_quantity():
    with pytest.raises(ValueError):
        long_straddle(
            strike=100,
            call_premium=6,
            put_premium=5,
            quantity=0,
        )

    with pytest.raises(ValueError):
        long_straddle(
            strike=100,
            call_premium=6,
            put_premium=5,
            quantity=-1,
        )