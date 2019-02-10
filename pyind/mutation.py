import numpy as np
import matplotlib.pyplot as plt


def flip_bit(pop, mut_pb):
    mask = _cre_mask(pop, mut_pb)
    return np.logical_xor(pop, mask)


def boundary(pop, mut_pb, delta):
    mask = _cre_mask(pop, mut_pb)
    r = np.random.ranf(pop.shape) * 2 - 1
    return pop + r * delta * mask


"""
def swap_idx(pop, mut_pb):
    #r = np.random.ranf(pop.shape)
    r = np.array([
        [3, 1, 6, 2, 4, 5],
        [4, 1, 2, 3, 5, 6],
    ]) * 0.1 - 0.01
    a = np.argsort(r, axis=1)
    #print(a)
    for j, row in enumerate(a):
        for i, col in enumerate(row):
            #print(r[j, col])
            if r[j, col] >= mut_pb:
                break
            #print("x")
            #print(col)
            #print("y")
            #print(a[j, -i-1])
            o = a[j, -i-1]
            pop[j, col], pop[j, o] = pop[j, o], pop[j, col]
    print(pop)

    
    def _mutShuffleIndexes(individual, indpb):
    size = len(individual)
    for i in range(size):
        if np.random.random() < indpb:
            swap_indx = np.random.randint(0, size - 2)
            if swap_indx >= i:
                swap_indx += 1
            individual[i], individual[swap_indx] = \
                individual[swap_indx], individual[i]
            print("swap!")
    
    return individual
"""


def _cre_mask(pop, mut_pb):
    return np.random.ranf(pop.shape) < mut_pb


def main():
    pop = np.arange(1, 13).reshape((2, -1))
    #print(pop)
    swap_idx(pop, 1)
    #print(pop)
    #print("\n")
    #print(np.where(pop % 5 == 0, pop[:, ::-1], pop))
    #print(pop[:, ::-1])
    #print(swap_idx(pop, 0.1))
    #plt.plot(swap_idx(pop, 0.1))
    #print(_mutShuffleIndexes(pop, 0.1))
    #plt.show()
    # pop = boundary(pop, 0.1)
    #print(swap_idx(pop, 0.2))
    # tmp = np.arange(pop.shape[1])
    # print(tmp.shape, tmp.shape[::-1])
    s = np.tile(np.random.shuffle(np.arange(pop.shape[1])), (pop.shape[0], 1))
    # print(s)

if __name__ == "__main__":
    main()
