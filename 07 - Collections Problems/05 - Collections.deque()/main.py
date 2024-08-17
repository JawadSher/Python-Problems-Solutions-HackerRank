from collections import deque

d = deque()
nums_operations = int(input().strip())

for _ in range(nums_operations):
    cmd = input().split(" ")
    prompt = cmd[0]
    
    if prompt == 'append':
        value = int(cmd[1])
        d.append(value)
    elif prompt == 'appendleft':
        value = int(cmd[1])
        d.appendleft(value)
    elif prompt == 'pop':
        d.pop()
    elif prompt == 'popleft':
        d.popleft()

for i in d:
    print(i, end=' ')
    
