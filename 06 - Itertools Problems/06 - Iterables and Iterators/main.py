from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

combine = list(combinations(letters, k))
count = 0

for i in combine:
    if 'a' in i :
        count += 1

print(count/len(combine))
