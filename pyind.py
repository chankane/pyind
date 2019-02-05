import numpy as np

import default as df


class Pyind:
    @staticmethod
    def _add_default(conf):
        if "eval_func" not in conf:
            raise ValueError("Should define 'eval_func' in conf")
        conf.setdefault("sel_rate", df.SEL_RATE)
        conf.setdefault("xovr_pb", df.XOVR_PB)
        conf.setdefault("sel_func", df.SEL_FUNC)
        conf.setdefault("xovr_func", df.XOVR_FUNC)
        conf.setdefault("mut_func", df.MUT_FUNC)
        conf.setdefault("mut_func", None)

        return conf

    def __init__(self, pop, conf):
        conf = Pyind._add_default(conf)
        self._pop = pop
        self._sel_rate = conf["sel_rate"]
        self._xovr_pb = conf["xovr_pb"]
        self._eval_func = conf["eval_func"]
        self._sel_func = conf["sel_func"]
        self._xovr_func = conf["xovr_func"]
        self._mut_func = conf["mut_func"]
        self._goal_ind = conf["goal_ind"]

    def _sel(self):
        fitness = np.array([self._eval_func(e) for e in self._pop])
        sel_num = int(self._pop.shape[0] * self._sel_rate)
        idxs = np.argsort(fitness)[-sel_num:][::-1]
        return self._pop[idxs]

    def _xovr(self, elites):
        _len = elites.shape[0]
        children = np.array([
            self._xovr_func(
                elites[np.random.randint(_len)],
                elites[np.random.randint(_len)],
            )
            for i in range(self._pop.shape[0] - _len)
        ])
        # print("gem")
        # print(children)
        # print(np.xncatenate((elites, children)))
        self._pop = np.xncatenate((elites, children))

    def _in_goal_ind(self):
        np.any()
        return np.sum(self._goal_ind == ind) == ind.shape[0]

    def start(self, end_gen=df.END_GEN):
        for i in range(end_gen + 1):
            print("gen: " + str(i))
            # print(self._pop)
            if self._is_goal_ind(sel[0]):
                break
            sel = self._sel()
            self._xovr(sel)
            print()
        print("best: " + str(self._sel()[0]))
