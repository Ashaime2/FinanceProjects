from src.portfolio import Position, Portfolio


def long_call(strike: float, premium: float, quantity: float = 1.0) -> Portfolio:
    if quantity <= 0:
        raise ValueError("quantity must be strictly positive")
    
    portfolio = Portfolio()
    position = Position(kind="call", strike=strike, quantity=quantity, premium=premium)
    portfolio.add_position(position)
    return portfolio


def long_put(strike: float, premium: float, quantity: float = 1.0) -> Portfolio:
    if quantity <= 0:
        raise ValueError("quantity must be strictly positive")

    portfolio = Portfolio()
    position = Position(kind="put", strike=strike, quantity=quantity, premium=premium)
    portfolio.add_position(position)

    return portfolio


def bull_call_spread(
    lower_strike: float,
    lower_premium: float,
    upper_strike: float,
    upper_premium: float,
    quantity: float = 1.0
) -> Portfolio:
    if quantity <= 0:
        raise ValueError("quantity must be strictly positive")
    if lower_strike >= upper_strike:
        raise ValueError("lower_strike must be lower than upper_strike")

    portfolio = Portfolio()
    long_position = Position(kind="call", strike=lower_strike, quantity=quantity, premium=lower_premium)
    short_position = Position(kind="call", strike=upper_strike, quantity=-quantity, premium=upper_premium)

    portfolio.add_position(long_position)
    portfolio.add_position(short_position)

    return portfolio


def bear_put_spread(
    lower_strike: float,
    lower_premium: float,
    upper_strike: float,
    upper_premium: float,
    quantity: float = 1.0
) -> Portfolio:
    if quantity <= 0:
        raise ValueError("quantity must be strictly positive")
    if lower_strike >= upper_strike:
        raise ValueError("lower_strike must be lower than upper_strike")

    portfolio = Portfolio()

    long_position = Position(kind="put", strike=upper_strike, quantity=quantity, premium=upper_premium)
    short_position = Position(kind="put", strike=lower_strike, quantity=-quantity, premium=lower_premium)

    portfolio.add_position(long_position)
    portfolio.add_position(short_position)

    return portfolio


def long_straddle(strike: float, call_premium: float, put_premium: float, quantity: float = 1.0) -> Portfolio:
    if quantity <= 0:
        raise ValueError("quantity must be strictly positive")

    portfolio = Portfolio()

    call_position = Position(kind="call", strike=strike, quantity=quantity, premium=call_premium)
    put_position = Position(kind="put", strike=strike, quantity=quantity, premium=put_premium)

    portfolio.add_position(call_position)
    portfolio.add_position(put_position)

    return portfolio