import numpy as np
import crossover as xovr
import mutation as mut


IND = 100
POP = 300


def evl(ind):
    return ind.sum()


def main():
    min_conf = {
        "pop": np.random.randint(2, size=(POP, IND)),
        "eval_func": evl,
    }
    conf = {
        "pop": np.random.randint(2, size=(POP, IND)),
        "sel_rate": 0.01,
        "xovr_pb": 0.5,
        "eval_func": evl,
        "sel_func": None,
        "xovr_func": x.p2,
        "mut_func": mut.flip_bit,
    }


if __name__ == "__main__":
    main()
