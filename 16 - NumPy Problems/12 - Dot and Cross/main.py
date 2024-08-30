import numpy as np
from numpy import matmul

N = int(input().strip())

np_arrA = np.array([[*map(int, input().split())] for _ in range(N)])
np_arrB = np.array([[*map(int, input().split())] for _ in range(N)])

result = matmul(np_arrA, np_arrB)
print(result)
