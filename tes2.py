from benchmarker import Benchmarker
import numpy as np
from pyind import selection as sel
from deap import tools


tools.selAutomaticEpsilonLexicase
tools.cxOnePoint
tools.cxBlend

loop = 100
"""
pop = np.array([
    [0, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
])
"""
pop = np.arange(10000000).reshape((100000, 100))


def evl(ind):
    return ind.sum()


with Benchmarker(loop) as bench:

    @bench('me')
    def insertion(bm):
        for i in bm:
            sel.roulette(pop, 0.3, evl)
