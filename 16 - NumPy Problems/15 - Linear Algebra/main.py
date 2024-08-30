import numpy as np

N = int(input().strip())
arr_A = [list(map(float, input().split())) for _ in range(N)]

print(round(np.linalg.det(arr_A), 3))
