import numpy as np


def p2(ind0, ind1):
    """
    Two-point crossover

    Parameters
    ----------
    ind0 : ndarray
        Father
    ind1 : ndarray
        Mother

    Returns
    -------
    chil : ndarray
        Child
    """

    sta, end = _cre_sta_end(ind0.shape[0])
    return np.hstack((ind0[:sta], ind1[sta:end], ind0[end:]))


def uniform(ind0, ind1):
    """
    Uniform crossover

    Parameters
    ----------
    ind0 : ndarray
        Father
    ind1 : ndarray
        Mother

    Returns
    -------
    chil : ndarray
        Child
    """

    mask = np.random.randint(2, size=ind0.shape[0])
    return ind0 * mask + ind1 * np.logical_not(mask)


def ox(ind0, ind1):
    """
    Order-based crossover (OX)

    Parameters
    ----------
    ind0 : ndarray
        Father
    ind1 : ndarray
        Mother

    Returns
    -------
    chil : ndarray
        Child
    """

    sta, end = _cre_sta_end(ind0.shape[0])
    keep = ind0[sta:end]
    other = np.setdiff1d(ind0, keep)
    return np.concatenate((other[:sta], keep, other[sta:]))


def _cre_sta_end(_len):
    end = np.random.randint(_len) + 1
    sta = np.random.randint(end)
    return sta, end


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
