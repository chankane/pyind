from benchmarker import Benchmarker

from test import *


try:
    xrange
except NameError:
    xrange = range       # for Python3


loop = 10
with Benchmarker() as bench:
    @bench("mt")
    def _(bm):
        for _ in xrange(loop):
            main()
