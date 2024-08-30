import numpy as np

P = list(map(float, input().split()))
X = int(input())

print(np.polyval(P, X))
