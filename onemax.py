# Onemax Problem
import numpy as np

from pyind import pyind as pi
from pyind import defaults as df


IND_LEN = 100
POP_LEN = 100


def evl(ind):
    return ind.sum()


if __name__ == "__main__":
    pop = np.random.randint(2, size=(POP_LEN, IND_LEN))

    conf = df.CONF
    conf["eval"]["func"] = evl
    conf["goal_ind"] = np.ones(IND_LEN)

    best = pi.Pyind(pop, conf).run()

    print("best ind: ")
    print(best)
