import numpy as np


a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [5, 6, 8, 8],
    [9, 10, 11, 12]
])
fin_a = np.array([5, 6, 7, 8])

b = np.array([
    [[1, 2], [2, 3], [3, 4], [4, 5]],
    [[1, 2], [2, 3], [3, 4], [9, 5]],
    [[1, 2], [2, 3], [3, 4], [4, 4]],
])

fin_b = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])


def cont(pop):
    goal_ind = fin_a
    #print(pop == goal_ind)
    return np.all(pop == goal_ind, axis=0)

print(b.shape)
print(cont(a))
#cont(b)
