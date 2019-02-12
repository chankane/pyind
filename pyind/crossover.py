import numpy as np


def p2(ind0, ind1):
    _len = ind0.shape[0]
    end = np.random.randint(_len) + 1
    start = np.random.randint(end)
    return np.hstack((ind0[:start], ind1[start:end], ind0[end:]))


def uniform(ind0, ind1):
    mask = np.random.randint(2, size=ind0.shape[0])
    return ind0 * mask + ind1 * np.logical_not(mask)


class Crossover:
    def __init__(self, conf):
        self._func = conf["func"]
        self._pb = conf["pb"]  # Not use now

    def xovr(self, par, pop_len):
        par_len = par.shape[0]
        chil = np.array([
            self._func(
                par[np.random.randint(par_len)],
                par[np.random.randint(par_len)],
            )
            for i in range(pop_len - par_len)
        ])
        return np.concatenate([par, chil])


if __name__ == "__main__":
    ind0 = np.zeros(20, dtype=int)
    ind1 = np.ones(20, dtype=int)
    # pop = np.concatenate((ind0, ind1))
    par = np.array([ind0, ind1])
    conf = {
        "func": p2,
        "pb": 0.95
    }
    c = Crossover(conf)
    print(par)
    print(c.xovr(par, 10))
