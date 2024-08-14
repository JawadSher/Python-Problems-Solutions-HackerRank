from collections import defaultdict

n, m = map(int, input().split())

d = defaultdict(list)

for i in range(n):
    d['first'].append(input()) 

for i in range(m):
    d['second'].append(input())
    
for i in d['second']:
    result = []
    for j in range(len(d['first'])):
        if i == d['first'][j]:
            result.append(str(j+1))
    
    if len(result) == 0:
        result.append(str(-1))
    print(' '.join(result))
