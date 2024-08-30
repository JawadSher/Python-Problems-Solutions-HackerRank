import numpy as np

arr_A = np.array(input().split(), int)
arr_B = np.array(input().split(), int)

print(np.inner(arr_A, arr_B))
print(np.outer(arr_A, arr_B))
