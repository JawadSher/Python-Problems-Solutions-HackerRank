import numpy as np

arr_elemnts = input().split()
x = np.array(arr_elemnts, int)
updated_arr = np.reshape(x, (3, 3))
print(updated_arr)
