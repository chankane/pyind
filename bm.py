from benchmarker import Benchmarker

import test

with Benchmarker(100, cycle=100, extra=5) as bench:
    @bench('goal')
    def insertion(bm):
        for i in bm:
            test.goal

    @bench('nogoal')
    def insertion(bm):
        for i in bm:
            test.no_goal
