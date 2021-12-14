import itertools as it
import numpy as np

data = np.array([[3, 4, 5],
                 [3, 2, 7],
                 [3, 4, 9]])

# for i in it.combinations(data, 2):
#     print(i, end=' ')
# print(np.array([i for i in it.combinations(data.diagonal(), 2)]))
# print(type(it.combinations(data.diagonal(), 2)))
# print(np.array([i for i in it.permutations(data.diagonal(), 2)]))
print(np.linalg.norm(data))
print(np.linalg.eigh(data, UPLO='L')[1][2])
