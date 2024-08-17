from collections import deque

t_testcases = int(input().strip())

for _ in range(t_testcases):
    _ = int(input().strip())
    d = deque(map(int, input().split()))
    
    top_cube = float('inf')
    
    while d:
        bottom_cube =  d.popleft() if d[0] > d[-1] else d.pop()
        
        if(bottom_cube <= top_cube):
            top_cube = bottom_cube
        else:
            break
    
    print("No" if d else "Yes")
