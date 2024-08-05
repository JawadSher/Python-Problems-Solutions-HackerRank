from itertools import product
A = input().strip().split()
B = input().strip().split()

certesian = product(A, B)

print(" ".join(f"({a}, {b})" for a, b, in certesian))
