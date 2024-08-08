n = int(input().strip())
nums_list = list(map(int, input().split()))
nums = set(nums_list[::-1])
cmds = int(input())

for _ in range(cmds):
    cmd = input().strip().split()
    
    prompt = cmd[0]
    
    if prompt == 'remove':
        elemnt = int(cmd[1])
        if elemnt in nums:
            nums.remove(elemnt)
    elif prompt == 'discard':
        elemnt = int(cmd[1])
        nums.discard(elemnt)
    elif prompt == 'pop':
        if nums:
            nums.pop()

print(sum(nums))
