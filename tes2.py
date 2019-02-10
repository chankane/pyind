from benchmarker import Benchmarker
import numpy as np
from pyind import selection as sel


loop = 100000
pop = np.array([
    [0, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
])


def evl(ind):
    return ind.sum()


with Benchmarker(loop) as bench:

    @bench('simple')
    def default_sort(bm):
        for i in bm:
            sel._roulette_simple(pop, 0.3, evl)

    @bench('me')
    def insertion(bm):
        for i in bm:
            sel.roulette(pop, 0.3, evl)
