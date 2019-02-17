# Traveling salesman problem

import numpy as np
import matplotlib.pyplot as plt

from pyind import pyind as pi
from pyind import crossover as xovr
from pyind import mutation as mut
from pyind import defaults as df


CITY_CNT = 15
POP_CNT = 200
END_GEN = 500

cities = np.random.rand(CITY_CNT * 2).reshape((-1, 2))


def evl(ind):
    total = 0
    for i in range(1, ind.shape[0]):
        total += np.linalg.norm(cities[ind[i]] - cities[ind[i - 1]])
    return -total


def solve(pop):
    conf = df.CONF
    conf["eval"]["func"] = evl
    conf["xovr"]["func"] = xovr.ox
    conf["mut"]["func"] = mut.swap_idx
    conf["mut"]["pb"] = 0.05
    best = pi.Pyind(pop, conf).start(END_GEN)
    return best


if __name__ == "__main__":
    t = cities.T

    # Create pop
    pop = np.tile(np.arange(CITY_CNT), (POP_CNT, 1))
    for e in pop:
        np.random.shuffle(e)

    # Plot gen 0
    idx = pop[0]
    plt.plot(t[0, idx], t[1, idx], label="gen 0", marker="o")

    best = solve(pop)
    print("best ind: " + str(best))

    # Plot gen END_GEN
    idx = best
    plt.plot(t[0, idx], t[1, idx], label="gen " + str(END_GEN), marker="o")

    plt.legend()
    plt.show()
