import numpy as np


def p2(ind0, ind1):
    _len = ind0.shape[0]
    end = np.random.randint(_len) + 1
    start = np.random.randint(end)
    return np.hstack((ind0[:start], ind1[start:end], ind0[end:]))
