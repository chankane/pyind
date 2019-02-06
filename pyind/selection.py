import numpy as np


def elite(pop, sel_rate, eval_func):
    ftns = _calc_ftns(pop, eval_func)
    sel_num = _calc_sel_num(pop, sel_rate)
    idxs = np.argsort(ftns)[-sel_num:][::-1]
    return pop[idxs]


def _calc_sel_num(pop, sel_rate):
    return int(pop.shape[0] * sel_rate)


def _calc_ftns(pop, eval_func):
    return np.array([eval_func(e) for e in pop])
