from benchmarker import Benchmarker

import deap_test
import pyind_test


try:
    xrange
except NameError:
    xrange = range       # for Python3


loop = 1
with Benchmarker() as bench:
    @bench("deap")
    def _(bm):
        for _ in xrange(loop):
            deap_test.main()

    @bench("pyind")
    def _(bm):
        for _ in xrange(loop):
            pyind_test.main()
