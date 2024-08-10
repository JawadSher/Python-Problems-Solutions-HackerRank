n, m = map(int, input().split())

elements_set = list(map(int, input().split()))

positive_set = set(map(int, input().split()))
negative_set = set(map(int, input().split()))

happiness = 0

for i in elements_set:
    if i in positive_set:
        happiness += 1
    elif i in negative_set:
        happiness -= 1
    
print(happiness)
