test_cases = int(input())

for _ in range(test_cases):
    A = int(input())
    set_A = set(input().split())
    B = int(input())
    set_B = set(input().split())
    
    if set_A.union(set_B) == set_B:
        print(True)
    else:
        print(False)
