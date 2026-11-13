# Computational Mathematics Lab

**Ritik Saroj** | Mathematics | Scientific Python | Statistics | Optimization

I built these small studies to explore practical mathematical questions with Python: fitting a model to imperfect measurements, allocating limited resources, estimating uncertainty, solving nonlinear equations, and checking mathematical reasoning. I have tried to keep each example readable and to include checks rather than relying on a printed answer alone.

All datasets and scenarios in this repository are synthetic and reproducible. These are portfolio exercises, not claims of paid AI-training work, peer-reviewed research, or production software.

## Studies

| Study | Main question | Methods |
|---|---|---|
| [01 Regression and conditioning](studies/s01_regression/README.md) | What line best describes noisy measurements, and how sensitive is the fit? | Least squares, residuals, condition number |
| [02 Resource allocation](studies/s02_optimization/README.md) | How should limited capacity be allocated? | Linear programming, feasibility checks |
| [03 Statistical inference](studies/s03_statistics/README.md) | What can a small sample tell us about its population mean? | Standard error, t confidence interval |
| [04 Root finding](studies/s04_roots/README.md) | How do two numerical solvers compare? | Bisection, Newton's method |
| [05 Mathematical answer review](studies/s05_answer_review/README.md) | How can an incorrect solution be detected? | Reference answer, rubric, error checks |

## Run locally

Python 3.10+ recommended.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python run_all.py
python -m unittest discover -s tests -v
```

## Structure

```text
computational-mathematics-lab/
├── README.md
├── Computational_Mathematics_Lab.ipynb
├── requirements.txt
├── run_all.py
├── data/
├── studies/
└── tests/
```

## My approach

1. State the mathematical question and assumptions.
2. Select a method that fits the problem.
3. Check results independently using residuals, constraints, or a reference calculation.
4. Explain what the result does not establish.

## Background

I completed a B.Sc. (Hons.) in Mathematics at the University of Delhi and have experience teaching mathematics. This repository is intended to show my current practice with mathematical reasoning and Python-based computation.

GitHub: https://github.com/ritiksaroj7318
