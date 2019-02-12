import numpy as np

from . import defaults as df
from .selection import Selection as Sel
from .crossover import Crossover as Xovr
from .mutation import Mutation as Mut


class Pyind:
    """
    @staticmethod
    def _add_default(conf):
        if "eval_func" not in conf:
            raise ValueError("Should define conf['eval']['func']")
        conf.setdefault("sel_rate", df.SEL_RATE)
        conf.setdefault("xovr_pb", df.XOVR_PB)
        conf.setdefault("mut_pb", df.MUT_PB)
        conf.setdefault("sel_func", df.SEL_FUNC)
        conf.setdefault("xovr_func", df.XOVR_FUNC)
        conf.setdefault("mut_func", df.MUT_FUNC)
        conf.setdefault("goal_ind", None)

        return conf
    """

    def __init__(self, pop, conf):
        #conf = Pyind._add_default(conf)
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

    def start(self, end_gen=df.END_GEN):
        for i in range(end_gen + 1):
            print("gen: " + str(i))
            # print(self._pop)
            if self._contains_goal_ind():
                break
            ftns = np.array([self._eval_func(e) for e in self._pop])
            parents = self._sel.sel(self._pop, ftns)
            self._pop = self._xovr.xovr(parents, ftns.shape[0])
            self._pop = self._mut.mut(self._pop)
            # print()
        print("best ind: ")
        print(self._goal_ind)
