import numpy as np


def elite(pop, sel_rate, eval_func):
    ftns = _calc_ftns(pop, eval_func)
    sel_num = _calc_sel_num(pop, sel_rate)
    print(ftns)
    idxs = np.argsort(ftns)[-sel_num::][::-1]
    return pop[idxs]


def roulette(pop, sel_rate, eval_func):
    ftns = _calc_ftns(pop, eval_func)
    sel_num = _calc_sel_num(pop, sel_rate)
    r = np.random.rand(sel_num) * ftns.sum()
    return pop[(ftns.cumsum()[:, np.newaxis] < r).sum(axis=0)]


# 2 times slower than "roulette"
def _roulette_simple(pop, sel_rate, eval_func):
    ftns = _calc_ftns(pop, eval_func)
    sel_num = _calc_sel_num(pop, sel_rate)
    w = ftns / ftns.sum()
    return pop[np.random.choice(pop.shape[0], sel_num, p=w)]


def _calc_sel_num(pop, sel_rate):
    return int(pop.shape[0] * sel_rate)


def _calc_ftns(pop, eval_func):
    return np.array([eval_func(e) for e in pop])


def evl(ind):
    return ind.sum()


if __name__ == "__main__":
    pop = np.array([
        [0, 1, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        [1, 1, 1, 1],
    ])

    # print(roulette(pop, 0.3, evl))
    ar = np.array([0, 0, 0, 0, 0])
    for i in range(10000):
        t = roulette(pop, 0.3, evl).sum()
        # print(t)
        ar[t] += 1
    print(ar/1000)

    ar = np.array([0, 0, 0, 0, 0])
    for i in range(10000):
        t = _roulette_simple(pop, 0.3, evl).sum()
        # print(t)
        ar[t] += 1
    print(ar/1000)
