from . import crossover as xovr
from . import mutation as mut
from . import selection as sel


CONF = {
    "eval": {
        #"func": None,
    },
    "sel": {
        "func": sel.elite,
        # "func": sel.roulette
        "rate": 0.05,
        "num": 10
    },
    "xovr": {
        "func": xovr.p2,
        "pb": 0.875
    },
    "mut": {
        "func": mut.flip_bit,
        "pb": 0.0075
    },
    "goal_ind": None
}

END_GEN = 40
