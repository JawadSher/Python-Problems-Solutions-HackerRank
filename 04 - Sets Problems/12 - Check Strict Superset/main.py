set_A = set(map(int, input().split()))
n = int(input())

is_subset = True

for _ in range(n):
    other_set = set(map(int, input().split()))
    if not set_A.issuperset(other_set) and len(set_A) > len(other_set):
        is_subset = False
        break
        
print(is_subset)
