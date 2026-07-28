from src.rates import(
    present_value_continuous
)

def actualized_strike(strike : float, rate : float, maturity : float) -> float :
    if maturity < 0 :
        raise ValueError('maturity must be non-negative')
    if strike < 0 :
        raise ValueError('strike must be non-negative')
    return present_value_continuous(strike, rate, maturity)

def arbitrage_gap(
        call_premium : float,
        put_premium : float,
        spot_price : float,
        strike : float,
        rate : float,
        maturity : float
) -> float :
    if maturity < 0 :
        raise ValueError('maturity must be non-negative')
    if spot_price < 0 :
        raise ValueError('spot_price must be non-negative')
    if strike < 0 :
        raise ValueError('strike must be non-negative')
    if call_premium < 0 or put_premium < 0 :
        raise ValueError('premiums must be non-negative')
    return call_premium - put_premium - spot_price + actualized_strike(strike, rate, maturity)

def opportunity_finder(
    call_premium: float,
    put_premium: float,
    spot_price: float,
    strike: float,
    rate: float,
    maturity: float,
    epsilon: float = 1e-8,
) -> float:
    if epsilon < 0:
        raise ValueError("epsilon must be non-negative")

    gap = arbitrage_gap(
        call_premium,
        put_premium,
        spot_price,
        strike,
        rate,
        maturity,
    )

    if abs(gap) <= epsilon:
        return 0.0

    return gap


def arbitrage_strategy(
    call_premium: float,
    put_premium: float,
    spot_price: float,
    strike: float,
    rate: float,
    maturity: float,
    epsilon: float = 1e-8,
) -> dict:
    gap = opportunity_finder(
        call_premium,
        put_premium,
        spot_price,
        strike,
        rate,
        maturity,
        epsilon,
    )

    if gap == 0.0:
        return {
            "opportunity": False,
            "gap": 0.0,
            "initial_profit": 0.0,
            "strategy": "No arbitrage found",
        }

    if gap < 0:
        strategy = (
            "Acheter le call, placer PV(K), vendre le put "
            "et vendre l'action à découvert"
        )
    else:
        strategy = (
            "Vendre le call, emprunter PV(K), acheter le put "
            "et acheter l'action"
        )

    return {
        "opportunity": True,
        "gap": gap,
        "initial_profit": abs(gap),
        "strategy": strategy,
    }