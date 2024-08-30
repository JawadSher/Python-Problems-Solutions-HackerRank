import numpy as np

N, M = map(int, input().split())

np_array = np.array([[*map(int, input().split())] for i in range(N)])

mean_values = np.mean(np_array, axis=1)
var_values = np.var(np_array, axis=0)
std_value = np.std(np_array, axis=None)

print(mean_values)
print(var_values)
print(round(std_value, 11))
