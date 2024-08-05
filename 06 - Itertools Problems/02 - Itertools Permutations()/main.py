from itertools import permutations

s = input()

chars = s.split()[0]
n = int(s.split()[1])
possible_per = permutations(sorted(chars, key=str.upper), n)
for per in possible_per:
    print(''.join(per))
