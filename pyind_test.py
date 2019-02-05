import numpy as np

from pyind import Pyind


IND = 15
POP = 300


def evl(ind):
    return ind.sum()


def main():
    pop = np.random.randint(2, size=(POP, IND))
    conf = {
        "eval_func": evl,
        "goal_ind": np.ones(IND)
    }

    Pyind(pop, conf).start(1000)


if __name__ == "__main__":
    main()
