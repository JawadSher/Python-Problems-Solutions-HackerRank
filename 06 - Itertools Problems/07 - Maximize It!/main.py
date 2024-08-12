from itertools import product

def calculateMax(m, k, lst):
    result = 0
    
    for combo in product(*lst):
        sums = sum(x**2 for x in combo)
        result = max(sums % k, result)
        
    return result
    
m, k = map(int, input().split())
lists = [list(map(int, input().split()[1:])) for _ in range(m)]

s = calculateMax(m, k, lists)
print(s)
        
