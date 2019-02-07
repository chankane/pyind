import numpy as np

from . import defaults as df


class Pyind:
    @staticmethod
    def _add_default(conf):
        if "eval_func" not in conf:
            raise ValueError("Should define 'eval_func' in conf")
        conf.setdefault("sel_rate", df.SEL_RATE)
        conf.setdefault("xovr_pb", df.XOVR_PB)
        conf.setdefault("mut_pb", df.MUT_PB)
        conf.setdefault("sel_func", df.SEL_FUNC)
        conf.setdefault("xovr_func", df.XOVR_FUNC)
        conf.setdefault("mut_func", df.MUT_FUNC)
        conf.setdefault("goal_ind", None)

        return conf

    def __init__(self, pop, conf):
        conf = Pyind._add_default(conf)
        self._pop = pop
        self._sel_rate = conf["sel_rate"]
        self._xovr_pb = conf["xovr_pb"]
        self._mut_pb = conf["mut_pb"]
        self._eval_func = conf["eval_func"]
        self._sel_func = conf["sel_func"]
        self._xovr_func = conf["xovr_func"]
        self._mut_func = conf["mut_func"]
        self._goal_ind = conf["goal_ind"]

    def _xovr(self, parents):
        _len = parents.shape[0]
        chil = np.array([
            self._xovr_func(
                parents[np.random.randint(_len)],
                parents[np.random.randint(_len)],
            )
            for i in range(self._pop.shape[0] - _len)
        ])
        self._pop = np.concatenate([parents, chil])

    def _contains_goal_ind(self):
        return np.any(np.all(
            (self._pop == self._goal_ind).reshape(self._pop.shape[0], -1),
            axis=1
        ))

    def start(self, end_gen=df.END_GEN):
        for i in range(end_gen + 1):
            print("gen: " + str(i))
            # print(self._pop)
            parents = self._sel_func(
                self._pop, self._sel_rate, self._eval_func
            )
            if self._contains_goal_ind():
                break
            self._xovr(parents)
            self._pop = self._mut_func(self._pop, self._mut_pb)
            print()
        print("best: " + str(parents[0]))
