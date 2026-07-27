def call_payoff(spot_price: float, strike: float) -> float:
    return max(spot_price - strike, 0.0)


def put_payoff(spot_price: float, strike: float) -> float:
    return max(strike - spot_price, 0.0)


class Position:
    def __init__(self, kind: str, strike: float, quantity: float):
        self.strike = strike
        self.quantity = quantity
        self.kind = kind
        if kind not in {"call", "put"}:
            raise ValueError('kind must be either "call" or "put"')
        if strike < 0:
            raise ValueError("strike must be non-negative")


    def payoff(self, spot_price: float) -> float:
        if self.kind == "call":
            return self.quantity * call_payoff(spot_price, self.strike)
        elif self.kind == "put":
            return self.quantity * put_payoff(spot_price, self.strike)


class Portfolio:
    def __init__(self):
        self.positions = []

    def add_position(self, position: Position) -> None:
        self.positions.append(position)

    def payoff(self, spot_price: float) -> float:
        return sum(position.payoff(spot_price) for position in self.positions)