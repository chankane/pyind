import numpy as np


def flip_bit(pop, mut_pb):
    flip = np.random.ranf(pop.shape) < mut_pb
    return np.logical_xor(pop, flip)


def main():
    pop = np.concatenate([
        np.zeros((5, 5), dtype=bool), np.ones((5, 5), dtype=bool)
    ])
    print(pop)
    pop = flip_bit(pop, 0.1)
    #print()
    print(pop)

if __name__ == "__main__":
    main()
