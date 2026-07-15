def call_payoff(S, K):
    """European call payoff."""
    return max(S - K, 0)


def put_payoff(S, K):
    """European put payoff."""
    return max(K - S, 0)


if __name__ == "__main__":
    print(call_payoff(120, 100))
    print(call_payoff(80, 100))
    print(put_payoff(120, 100))
    print(put_payoff(80, 100))