import numpy as np
import pytest

from src.rates import (
    future_value_continuous,
    present_value_continuous,
    future_value_discrete,
    present_value_discrete,
)


# Continuous compounding

def test_future_value_continuous():
    result = future_value_continuous(
        present_value=100.0,
        rate=0.05,
        maturity=2.0,
    )
    expected = 100.0 * np.exp(0.05 * 2.0)

    assert result == pytest.approx(expected)


def test_present_value_continuous():
    result = present_value_continuous(
        future_value=110.0,
        rate=0.05,
        maturity=2.0,
    )
    expected = 110.0 * np.exp(-0.05 * 2.0)

    assert result == pytest.approx(expected)


def test_continuous_round_trip():
    initial_value = 100.0

    future_value = future_value_continuous(
        initial_value,
        rate=0.05,
        maturity=2.0,
    )
    recovered_value = present_value_continuous(
        future_value,
        rate=0.05,
        maturity=2.0,
    )

    assert recovered_value == pytest.approx(initial_value)


# Discrete compounding

def test_future_value_discrete():
    result = future_value_discrete(
        present_value=100.0,
        rate=0.05,
        maturity=2.0,
    )

    assert result == pytest.approx(110.25)


def test_present_value_discrete():
    result = present_value_discrete(
        future_value=110.25,
        rate=0.05,
        maturity=2.0,
    )

    assert result == pytest.approx(100.0)


def test_discrete_round_trip():
    initial_value = 100.0

    future_value = future_value_discrete(
        initial_value,
        rate=0.05,
        maturity=2.0,
    )
    recovered_value = present_value_discrete(
        future_value,
        rate=0.05,
        maturity=2.0,
    )

    assert recovered_value == pytest.approx(initial_value)


# Boundary cases

@pytest.mark.parametrize(
    "function",
    [
        future_value_continuous,
        present_value_continuous,
        future_value_discrete,
        present_value_discrete,
    ],
)
def test_zero_maturity_returns_unchanged_value(function):
    assert function(100.0, 0.05, 0.0) == pytest.approx(100.0)


@pytest.mark.parametrize(
    "function",
    [
        future_value_continuous,
        present_value_continuous,
        future_value_discrete,
        present_value_discrete,
    ],
)
def test_negative_maturity_is_rejected(function):
    with pytest.raises(ValueError):
        function(100.0, 0.05, -1.0)


@pytest.mark.parametrize(
    "function",
    [
        future_value_discrete,
        present_value_discrete,
    ],
)
@pytest.mark.parametrize("invalid_rate", [-1.0, -1.5])
def test_invalid_discrete_rate_is_rejected(function, invalid_rate):
    with pytest.raises(ValueError):
        function(100.0, invalid_rate, 2.0)