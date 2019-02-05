import numpy as np

from pyind import Pyind


IND = 100
POP = 300


def evl(ind):
    return ind.sum()


def main():
    pop = np.random.randint(2, size=(POP, IND))

    pi = Pyind(pop, evl)
    pi.set_final_ind(np.ones(IND))
    pi.start(1000)


if __name__ == "__main__":
    main()
