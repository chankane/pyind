import numpy as np
import matplotlib.pyplot as plt

from . import util
# import util


def flip_bit(pop, pb):
    mask = _cre_mask(pop, pb)
    return np.logical_xor(pop, mask)


def boundary(pop, pb, delta):
    mask = _cre_mask(pop, pb)
    r = np.random.ranf(pop.shape) * 2 - 1
    return pop + r * delta * mask


def _cre_mask(pop, pb):
    return np.random.ranf(pop.shape) < pb


class Mutation:
    def __init__(self, conf):
        self._func = conf["func"]
        self._args = util.cre_args(self._func, conf, exclusion=("pop",))

    def mut(self, pop):
        return self._func(pop, *self._args)


if __name__ == "__main__":
    pop = np.arange(1, 13).reshape((2, -1))
    conf = {
        "func": boundary,
        "pb": 0.1,
        "delta": 1
    }
    m = Mutation(conf)
    print(m.mut(pop))
