from src.payoffs import (
    call_payoff,
    put_payoff,
    Position,
    Portfolio,
)


def test_call_payoff():
    assert call_payoff(120, 100) == 20
    assert call_payoff(80, 100) == 0


def test_put_payoff():
    assert put_payoff(80, 100) == 20
    assert put_payoff(120, 100) == 0


def test_long_call_position():
    position = Position("call", 100, 2)

    assert position.payoff(120) == 40
    assert position.payoff(80) == 0


def test_short_call_position():
    position = Position("call", 100, -1)

    assert position.payoff(120) == -20


def test_portfolio_payoff():
    portfolio = Portfolio()
    portfolio.add_position(Position("call", 100, 1))
    portfolio.add_position(Position("call", 120, -1))

    assert portfolio.payoff(80) == 0
    assert portfolio.payoff(110) == 10
    assert portfolio.payoff(130) == 20