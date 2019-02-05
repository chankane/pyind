import numpy as np


def elite(pop, sel_rate):
    sel_num = int(self._pop.shape[0] * self._sel_rate)
    fitness = np.array([self._eval_func(e) for e in self._pop])
    idxs = np.argsort(fitness)[-sel_num:][::-1]
    return self._pop[idxs]
