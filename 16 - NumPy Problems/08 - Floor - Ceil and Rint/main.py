import numpy as np
np.set_printoptions(legacy='1.13')

np_array = np.array(input().split(), float)

print(np.floor(np_array), np.ceil(np_array), np.rint(np_array), sep="\n")
