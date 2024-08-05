from itertools import combinations

s = "HACK 2"

chars = s.split()[0]
n = int(s.split()[1])

sorted_chars = sorted(chars)

possible_combinations = combinations(sorted_chars, n)

for i in range(1, n+1):
    possible_combinations = combinations(sorted_chars, i)
    for comb in possible_combinations:
        print(''.join(comb))
