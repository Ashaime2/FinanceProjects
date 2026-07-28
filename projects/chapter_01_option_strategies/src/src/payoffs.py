def call_payoff(spot_price: float, strike: float) -> float:
    return max(spot_price - strike, 0.0)


def put_payoff(spot_price: float, strike: float) -> float:
    return max(strike - spot_price, 0.0)