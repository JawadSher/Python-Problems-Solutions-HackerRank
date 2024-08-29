import numpy as np

N, M, P = map(int, input().split())

arr1 = []
arr2 = []
while(N > 0):
    arr1.append(list(map(int, input().split())))
    N -= 1
while(M > 0):
    arr2.append(list(map(int, input().split())))
    M -= 1


np_array1 = np.array(arr1)
np_array2 = np.array(arr2)

print(np.concatenate((np_array1, np_array2), axis=(M+N)*P))
