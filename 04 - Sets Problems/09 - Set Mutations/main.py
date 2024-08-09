nums_of_elemnts = int(input())
list_of_elemnts = set(map(int, input().split()))
nums_of_sets = int(input())

for _ in range(nums_of_sets):
    compt_cmd = input().split()
    cmd = compt_cmd[0]
    
    if cmd == 'intersection_update':
        value = set(map(int, input().split()))
        list_of_elemnts.intersection_update(value)
    elif cmd == 'update':
        value = set(map(int, input().split()))
        list_of_elemnts.update(value)
    elif cmd == 'symmetric_difference_update':
        value = set(map(int, input().split()))
        list_of_elemnts.symmetric_difference_update(value)
    elif cmd == 'difference_update':
        value = set(map(int, input().split()))
        list_of_elemnts.difference_update(value)

total = sum(list_of_elemnts)
print(total)
