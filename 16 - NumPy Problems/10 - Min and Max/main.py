import numpy as np

N, M = map(int, input().split())

np_array = np.array([[*map(int, input().split())] for _ in range(N)])

min_num = np.min(np_array, axis=1)
max_num = np.max(min_num)
print(max_num)
