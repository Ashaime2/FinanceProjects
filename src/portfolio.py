from src.payoffs import call_payoff, put_payoff
from src.rates import future_value_continuous

class Position:
    def __init__(self, kind: str, strike: float, quantity: float, premium : float):
        if kind not in {"call", "put"}:
            raise ValueError('kind must be either "call" or "put"')
        if strike < 0:
            raise ValueError("strike must be non-negative")
        if premium < 0 :
            raise ValueError('premium must be non-negative')
        if quantity == 0 : 
            raise ValueError('quantity cannot be equal to 0')
        self.strike = strike
        self.quantity = quantity
        self.kind = kind
        self.premium = premium


    def payoff(self, spot_price: float) -> float:
        if self.kind == "call":
            return self.quantity * call_payoff(spot_price, self.strike)
        else :
            return self.quantity * put_payoff(spot_price, self.strike)
        
    def initial_cost(self) -> float :
        return self.quantity * self.premium


class Portfolio:
    def __init__(self):
        self.positions : list[Position] = []

    def add_position(self, position: Position) -> None:
        if not isinstance(position, Position) :
            raise TypeError('position must be a Position object')
        self.positions.append(position)

    def payoff_total(self, spot_price: float) -> float:
        return sum(position.payoff(spot_price) for position in self.positions)

    def initial_cost_total(self) -> float :
        return sum(position.initial_cost() for position in self.positions)
    
    def profit_total(self, rate : float, spot_price : float, maturity : float) -> float :
        return self.payoff_total(spot_price=spot_price) - future_value_continuous(self.initial_cost_total(), rate, maturity)