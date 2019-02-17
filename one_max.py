import numpy as np

from pyind import pyind as pi
from pyind import defaults as df


IND = 100
POP = 300


def evl(ind):
    return ind.sum()


if __name__ == "__main__":
    pop = np.random.randint(2, size=(POP, IND))

    conf = df.CONF
    conf["eval"]["func"] = evl
    conf["goal_ind"] = np.ones(IND)

    res = pi.Pyind(pop, conf).start(1000)

    print(res)
