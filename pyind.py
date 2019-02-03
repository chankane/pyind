import numpy as np

import crossover as co


DEFAULT_END_GEN = 40
# DEFAULT_END_GEN = 1
DEFAULT_SEL_NUM = 3


class Pyind:
    def __init__(self, pop, eval_func):
        self._pop = pop
        self._eval_func = eval_func
        self._co_func = co.p2
        self._final_ind = None
        self._sel_num = DEFAULT_SEL_NUM

    def set_sel_num(self, sel_num):
        self._co_func = sel_num

    def set_crossover_func(self, func):
        self._co_func = func

    def set_final_ind(self, ind):
        self._final_ind = ind

    def _sel(self):
        fitness = np.array([self._eval_func(e) for e in self._pop])
        idx = np.argsort(fitness)[-self._sel_num:][::-1]
        return self._pop[idx]

    def _co(self, elites):
        _len = elites.shape[0]
        children = np.array([
            self._co_func(
                elites[np.random.randint(_len)],
                elites[np.random.randint(_len)],
            )
            for i in range(self._pop.shape[0] - elites.shape[0])
        ])
        # print("gem")
        # print(children)
        # print(np.concatenate((elites, children)))
        self._pop = np.concatenate((elites, children))

    def _is_final_ind(self, ind):
        return np.sum((self._final_ind == ind) == ind.shape[0])

    def start(self, end_gen=DEFAULT_END_GEN):
        for i in range(end_gen + 1):
            print("gen: " + str(i))
            # print(self._pop)
            sel = self._sel()
            if self._is_final_ind(sel[0]):
                break
            self._co(sel)
            print()
        print("best: " + str(self._sel()[0]))
