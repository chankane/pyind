import numpy as np

from pyind import pyind as pi


IND = 100
POP = 300


def evl(ind):
    return ind.sum()


def main():
    pop = np.random.randint(2, size=(POP, IND), dtype=bool)
    conf = {
        "eval_func": evl,
        "goal_ind": np.ones(IND)
    }

    pi.Pyind(pop, conf).start(1000)


if __name__ == "__main__":
    main()
