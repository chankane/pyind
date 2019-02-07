import numpy as np


def p2(ind0, ind1):
    _len = ind0.shape[0]
    end = np.random.randint(_len) + 1
    start = np.random.randint(end)
    return np.hstack((ind0[:start], ind1[start:end], ind0[end:]))


def uniform(ind0, ind1):
    mask = np.random.randint(2, size=ind0.shape[0])
    return ind0 * mask + ind1 * np.logical_not(mask)

if __name__ == "__main__":
    ind0 = np.zeros(30, dtype=int)
    ind1 = np.ones(30, dtype=int)
    print(uniform(ind0, ind1))
