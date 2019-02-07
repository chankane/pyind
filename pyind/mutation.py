import numpy as np
import matplotlib.pyplot as plt


def flip_bit(pop, mut_pb):
    flip = np.random.ranf(pop.shape) < mut_pb
    return np.logical_xor(pop, flip)


def boundary(pop, mut_pb, delta):
    mask = np.random.ranf(pop.shape) < mut_pb
    r = np.random.ranf(pop.shape) * 2 - 1
    return pop + r * delta * mask


def main():
    pop = np.concatenate([
        np.zeros((1000, 1)), np.ones((1000, 1))
    ])
    #print(pop)
    plt.plot(boundary(pop, 0.005, 1))
    #print(boundary(pop, 0.1, 0.1))
    plt.show()
    # pop = boundary(pop, 0.1)
    #print(pop)

if __name__ == "__main__":
    main()
