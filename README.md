# Quantitative Finance Learning Projects

A collection of quantitative finance projects developed during my self-directed training in financial mathematics, stochastic processes, derivatives pricing, portfolio theory, and risk management.

The objective is not only to apply financial models, but to understand their mathematical foundations, assumptions, implementation, validation, and limitations.

Whenever possible, the main algorithms are implemented from scratch in Python before being compared with standard libraries.

## Learning approach

Each chapter follows the same progression:

1. Study the mathematical and financial foundations.
2. Implement the main concepts from scratch.
3. Validate the implementation with unit tests.
4. Apply the concepts in a standalone mini-project.
5. Analyse the results, assumptions, and limitations.

## Projects

| Chapter | Project | Status |
|---|---|---|
| 1 | [Option strategies and no-arbitrage](projects/chapter_01_option_strategies) | Completed |
| 2 | Probability foundations | Planned |
| 3 | Brownian motion and stochastic processes | Planned |
| 4 | Ito calculus, SDEs and geometric Brownian motion | Planned |
| 5 | Portfolio theory | Planned |
| 6 | Monte Carlo simulation and risk | Planned |
| 7 | Black-Scholes and option pricing | Planned |

## Repository organisation

Each project is self-contained and contains its own:

- source code
- unit tests
- notebooks
- data
- figures
- documentation

## Installation

    git clone https://github.com/Ashaime2/FinanceProjects.git
    cd FinanceProjects
    python -m pip install -r requirements.txt

## Running Chapter 1 tests

    cd projects/chapter_01_option_strategies
    python -m pytest -v

## Technologies

- Python
- NumPy
- pandas
- Matplotlib
- SciPy
- Jupyter Notebook
- pytest
- Git and GitHub

## About me

I am a final-year engineering student at Centrale Lille, specialising in Data Science. This repository is part of my preparation for quantitative finance, risk modelling, and financial data science roles.

## Disclaimer

This repository is intended for educational purposes only. Its contents do not constitute financial advice.
