from src.payoffs import (
    call_payoff,
    put_payoff,
)


def test_call_payoff():
    assert call_payoff(120, 100) == 20
    assert call_payoff(80, 100) == 0


def test_put_payoff():
    assert put_payoff(80, 100) == 20
    assert put_payoff(120, 100) == 0