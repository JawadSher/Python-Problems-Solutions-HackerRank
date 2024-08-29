import numpy as np

N, M = map(int, input().split())

np_array_A = np.array([[*map(int, input().split())] for _ in range(N)])
np_array_B = np.array([[*map(int, input().split())] for _ in range(N)])

print(np.add(np_array_A, np_array_B))
print(np.subtract(np_array_A, np_array_B))
print(np.multiply(np_array_A, np_array_B))
print(np.floor_divide(np_array_A, np_array_B))
print(np.mod(np_array_A, np_array_B))
print(np.power(np_array_A, np_array_B))
