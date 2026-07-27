# Quantitative Finance Learning Projects

A collection of quantitative finance projects developed during my self-directed training in financial mathematics, stochastic processes, derivatives pricing, portfolio theory, and risk management.

The objective of this repository is not only to apply existing models, but to understand their mathematical foundations, assumptions, implementation, and limitations.

Whenever possible, the main algorithms are implemented from scratch in Python before being compared with standard libraries.

## Learning approach

Each chapter follows the same progression:

1. Study the mathematical and financial foundations.
2. Implement the main concepts from scratch.
3. Validate the implementation with unit tests and simulations.
4. Apply the concepts in a small standalone project.
5. Analyse the results, assumptions, and limitations.

## Progress

| Chapter | Topic | Main concepts | Status |
|---|---|---|---|
| 1 | Financial foundations | Payoffs, long and short positions, portfolios, interest rates, no-arbitrage | In progress |
| 2 | Probability foundations | Random variables, conditional expectation, convergence, Monte Carlo foundations | In progress |
| 3 | Stochastic processes | Martingales, Brownian motion, reflection principle | Completed |
| 4 | Itô calculus and SDEs | Itô integral, Itô's lemma, stochastic differential equations, geometric Brownian motion | In progress |
| 5 | Portfolio theory | Diversification, Markowitz optimisation, CAPM, factor models | Planned |
| 6 | Simulation and risk | Monte Carlo methods, Value at Risk, Expected Shortfall | Planned |
| 7 | Option pricing | Black–Scholes model, risk-neutral pricing, Greeks, implied volatility | Planned |

> This repository is actively evolving as I progress through the curriculum.  
> “Completed” refers to the theoretical chapter; associated code and projects may still be under development.

## Current implementations

### Option payoffs and portfolios

The first implementation provides:

- European call and put payoff functions;
- long and short option positions;
- portfolios composed of multiple option positions;
- input validation;
- unit tests with `pytest`.

Source code:

- [`payoffs.py`](chapitres/chapitre01_fondations/code/payoffs.py)
- [`test_payoffs.py`](tests/test_payoffs.py)

## Repository structure

```text
FinanceProjects/
├── chapitres/       # Chapter-specific code and learning material
├── projets/         # Standalone quantitative finance projects
├── notebooks/       # Numerical experiments and visualisations
├── src/             # Reusable Python modules
├── tests/           # Unit tests
├── donnees/         # Data used in experiments
├── figures/         # Generated figures and results
└── bibliotheque/    # Personal references and notes
```

## Running the tests

Clone the repository and move into the project directory:

```bash
git clone https://github.com/Ashaime2/FinanceProjects.git
cd FinanceProjects
```

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

Run the test suite:

```bash
python -m pytest -v
```

Current test suite: **5 passing tests**.

## Technologies

- Python
- NumPy
- pandas
- Matplotlib
- SciPy
- Jupyter Notebook
- pytest
- Git and GitHub

The exact dependencies will evolve as new projects are added.

## Planned projects

The repository will progressively include projects such as:

- construction and visualisation of option payoff strategies;
- simulation and statistical analysis of Brownian motion;
- numerical simulation of stochastic differential equations;
- geometric Brownian motion calibration and diagnostics;
- portfolio optimisation under practical constraints;
- Monte Carlo pricing and risk estimation;
- Black–Scholes pricing implemented from first principles;
- implied volatility and Greeks analysis.

## About me

I am a final-year engineering student at Centrale Lille, specialising in Data Science. I am developing this repository as part of an in-depth preparation for quantitative finance, risk modelling, and financial data science roles.

My focus is on connecting mathematical theory, financial intuition, numerical implementation, and critical analysis.

## Disclaimer

This repository is intended for educational purposes only. Its contents do not constitute financial advice.