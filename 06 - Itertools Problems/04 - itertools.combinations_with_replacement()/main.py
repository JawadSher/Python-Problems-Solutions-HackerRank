from itertools import combinations_with_replacement
input_data = input().split()
string = input_data[0]
k = int(input_data[1])

result = list(combinations_with_replacement(sorted(string), k))

for i in result:
    print(''.join(i))
