import numpy as np

input_nums = list(map(int, input().split()))
zeros_arr = np.zeros(input_nums, dtype=np.int)
ones_arr = np.ones(input_nums, dtype=np.int)

print(zeros_arr)
print(ones_arr)
