from studies.s01_regression.solution import run as a
from studies.s02_optimization.solution import run as b
from studies.s03_statistics.solution import run as c
from studies.s04_roots.solution import run as d
from studies.s05_answer_review.solution import run as e

if __name__ == "__main__":
    for name, fn in [("Regression", a), ("Optimization", b), ("Statistics", c),
                     ("Root finding", d), ("Answer review", e)]:
        print("\\n" + "=" * 60 + "\\n" + name)
        fn()
