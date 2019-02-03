import numpy as np

from pyind import Pyind


IND = 100
POP = 300
MUT = 0.05


def evl(ind):
    return ind.sum()
    # return pop.sum(axis=1)


def main():
    pop = np.random.randint(2, size=(POP, IND))
    pi = Pyind(pop, evl)
    pi.set_final_ind(np.ones(IND))
    pi.start(1000)
    #print(pop, evl(), gene)
    #idxs = np.argsort(evl())
    #print(pop[idxs])


if __name__ == "__main__":
    main()
