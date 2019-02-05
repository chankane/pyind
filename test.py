import numpy as np


a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [5, 6, 8, 8],
    [9, 10, 11, 12]
])
fin_a = np.array([5, 6, 7, 8])

b = np.array([
    [[1, 2], [2, 3], [3, 4], [7, 5]],
    [[1, 2], [2, 3], [3, 4], [9, 5]],
    [[1, 2], [2, 3], [3, 4], [4, 4]],
])

fin_b = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])


def cont(pop):
    goal_ind = fin_a
    return np.all(pop == goal_ind, axis=0)

#print(b == fin_b)
#print(np.all(b == fin_b, axis=1))
#print(np.sum(b, axis=1))
#print(cont(a))
#cont(b)
c = b.reshape((b.shape[0], -1))
#print(c)
fin = fin_b.reshape((fin_b.shape[0], -1))
#print(fin)
#print(np.all(c == fin, axis=1))
h = np.any(np.all((b == fin_b).reshape(b.shape[0], -1), axis=1))
print(h)
