import numpy as np

N, M = map(int, input().split())

np_array = np.array([[*map(int, input().split())] for _ in range(N)])

sum_array = np.sum(np_array, axis=0)
prod_array = np.prod(sum_array, axis=0)
print(prod_array)
