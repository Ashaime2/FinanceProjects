import numpy as np
import pytest

from src.portfolio import Portfolio, Position


# Position

def test_long_call_payoff():
    position = Position(kind="call", strike=100.0, quantity=2.0, premium=5.0)

    assert position.payoff(120.0) == pytest.approx(40.0)


def test_long_put_payoff():
    position = Position(kind="put", strike=100.0, quantity=2.0, premium=5.0)

    assert position.payoff(80.0) == pytest.approx(40.0)


def test_short_position_has_negative_payoff():
    position = Position(kind="call", strike=100.0, quantity=-2.0, premium=5.0)

    assert position.payoff(120.0) == pytest.approx(-40.0)


def test_long_position_has_positive_initial_cost():
    position = Position(kind="call", strike=100.0, quantity=2.0, premium=5.0)

    assert position.initial_cost() == pytest.approx(10.0)


def test_short_position_has_negative_initial_cost():
    position = Position(kind="put", strike=100.0, quantity=-2.0, premium=5.0)

    assert position.initial_cost() == pytest.approx(-10.0)


@pytest.mark.parametrize("invalid_kind", ["stock", "Call", ""])
def test_invalid_kind_is_rejected(invalid_kind):
    with pytest.raises(ValueError):
        Position(kind=invalid_kind, strike=100.0, quantity=1.0, premium=5.0)


def test_negative_strike_is_rejected():
    with pytest.raises(ValueError):
        Position(kind="call", strike=-1.0, quantity=1.0, premium=5.0)


def test_negative_premium_is_rejected():
    with pytest.raises(ValueError):
        Position(kind="call", strike=100.0, quantity=1.0, premium=-1.0)


def test_zero_quantity_is_rejected():
    with pytest.raises(ValueError):
        Position(kind="call", strike=100.0, quantity=0.0, premium=5.0)


# Portfolio

def test_add_position():
    portfolio = Portfolio()
    position = Position(kind="call", strike=100.0, quantity=1.0, premium=5.0)

    portfolio.add_position(position)

    assert portfolio.positions == [position]


def test_add_position_rejects_invalid_object():
    portfolio = Portfolio()

    with pytest.raises(TypeError):
        portfolio.add_position("not a position")


def test_portfolio_initial_cost_total():
    portfolio = Portfolio()
    portfolio.add_position(
        Position(kind="call", strike=100.0, quantity=2.0, premium=5.0)
    )
    portfolio.add_position(
        Position(kind="put", strike=90.0, quantity=-1.0, premium=3.0)
    )

    assert portfolio.initial_cost_total() == pytest.approx(7.0)


def test_portfolio_payoff_total():
    portfolio = Portfolio()
    portfolio.add_position(
        Position(kind="call", strike=100.0, quantity=2.0, premium=5.0)
    )
    portfolio.add_position(
        Position(kind="put", strike=110.0, quantity=1.0, premium=4.0)
    )

    assert portfolio.payoff_total(spot_price=105.0) == pytest.approx(15.0)


def test_portfolio_profit_total():
    portfolio = Portfolio()
    portfolio.add_position(
        Position(kind="call", strike=100.0, quantity=2.0, premium=5.0)
    )
    portfolio.add_position(
        Position(kind="put", strike=110.0, quantity=1.0, premium=4.0)
    )

    expected_profit = 15.0 - 14.0 * np.exp(0.05 * 2.0)

    assert portfolio.profit_total(
        rate=0.05,
        spot_price=105.0,
        maturity=2.0,
    ) == pytest.approx(expected_profit)


def test_empty_portfolio_returns_zero():
    portfolio = Portfolio()

    assert portfolio.initial_cost_total() == pytest.approx(0.0)
    assert portfolio.payoff_total(spot_price=100.0) == pytest.approx(0.0)
    assert portfolio.profit_total(
        rate=0.05,
        spot_price=100.0,
        maturity=2.0,
    ) == pytest.approx(0.0)