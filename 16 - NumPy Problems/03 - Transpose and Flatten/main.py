import numpy as np

N, M = map(int, input().split())
arr = []

while N > 0:
    arr.append(list(map(int, input().split())))
    N -= 1

np_array = np.array(arr, int)

print(np.transpose(np_array))
print(np_array.flatten())
