import numpy as np

### ERRORS ###

def _validate_maturity(maturity : float) -> None :
    if maturity < 0 :
        raise ValueError('Maturity ne peut pas être négatif')
    
def _validate_rate(rate : float) -> None :
    if rate <= -1 :
        raise ValueError("rate doit être strictement supérieur à -1")
    
### Core functions ###

def future_value_continuous(present_value: float, rate: float, maturity: float) -> float:
    _validate_maturity(maturity)
    return present_value * np.exp(rate*maturity)


def present_value_continuous(future_value: float, rate: float, maturity: float) -> float:
    _validate_maturity(maturity)
    return future_value * np.exp(-rate*maturity)


def future_value_discrete(present_value: float, rate: float, maturity: float) -> float:
    _validate_maturity(maturity)
    _validate_rate(rate)
    return present_value * (1+rate)**maturity


def present_value_discrete(future_value: float, rate: float, maturity: float) -> float:
    _validate_maturity(maturity)
    _validate_rate(rate)
    return future_value / ((1+rate)**maturity)