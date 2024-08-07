M = int(input().strip())
A = set(map(int, input().split()))
N = int(input().strip())
B = set(map(int, input().split()))

new_list = []
new_list.extend(A.difference(B))
new_list.extend(B.difference(A))
new_list.sort()

for i in new_list:
    print(i)
