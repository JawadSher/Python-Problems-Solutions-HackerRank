from collections import Counter

n = int(input().strip())

x = [input() for _ in range(n)]
print(len(Counter(x)))
print(*Counter(x).values())
