import numpy as np

from . import defaults as df
from .selection import Selection as Sel
from .crossover import Crossover as Xovr
from .mutation import Mutation as Mut


class Pyind:
    def __init__(self, pop, conf):
        if type(pop) == list:
            raise TypeError("pyind only supports ndarray (numpy)")
        self._pop = pop
        self._eval_func = conf["eval"]["func"]
        self._sel = Sel(pop.shape[0], conf["sel"])
        self._xovr = Xovr(conf["xovr"])
        self._mut = Mut(conf["mut"])
        self._goal_ind = conf["goal_ind"]

    def _contains_goal_ind(self):
        return np.any(np.all(
            (self._pop == self._goal_ind).reshape(self._pop.shape[0], -1),
            axis=1
        ))

    def _get_best(self):
        ftns = np.array([self._eval_func(e) for e in self._pop])
        return self._pop[np.argsort(ftns)[-1]]

    def start(self, end_gen=df.END_GEN):
        print("\rgen: {0:d}".format(0), end="")
        for i in range(end_gen):
            print("\rgen: {0:d}".format(i + 1), end="")
            if self._contains_goal_ind():
                print("\ngoal")
                return self._goal_ind
            ftns = np.array([self._eval_func(e) for e in self._pop])
            parents = self._sel.sel(self._pop, ftns)
            self._pop = self._xovr.xovr(parents, ftns.shape[0])
            self._pop = self._mut.mut(self._pop)
        print()
        return self._get_best()
