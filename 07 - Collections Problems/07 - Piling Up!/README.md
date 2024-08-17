<h1 align='center'>Piling - Up!</h1>

## Problem Statement

**Problem URL :** [Piling Up!](https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/6d0a292e-5d62-4b01-b291-392030ea1c4d)
![image](https://github.com/user-attachments/assets/5de07b21-2b40-469e-a5a3-0d61e5b65aee)

## Problem Solution

```py
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
```

## Problem Solution Explanation

This Python code checks whether it's possible to stack cubes in non-increasing order by always taking the largest cube from either end of a deque (double-ended queue). Let's break down the code step by step, along with an example for better understanding.


```python
from collections import deque
```
- **Importing the `deque` class:** This imports the `deque` class from Python's `collections` module. A deque is a double-ended queue that allows adding and removing elements from both ends efficiently.

```python
t_testcases = int(input().strip())
```
- **Reading the number of test cases:** This line reads an integer input that represents the number of test cases. The `strip()` function removes any leading or trailing whitespace.
- Example: If the user inputs `2`, then `t_testcases` will hold the value `2`.

```python
for _ in range(t_testcases):
    _ = int(input().strip())
    d = deque(map(int, input().split()))
```
- **Loop through each test case:**
  - `for _ in range(t_testcases)`: This loop will iterate once for each test case.
  - `_= int(input().strip())`: This reads the number of cubes in the current test case (but the value is not used, hence `_` is used as a dummy variable).
  - `d = deque(map(int, input().split()))`: This reads a line of space-separated integers, converts them to a list of integers, and initializes a deque `d` with these integers.
  - Example: If the input line is `4 3 2 1`, then `d` will be `deque([4, 3, 2, 1])`.

```python
top_cube = float('inf')
```
- **Initializing `top_cube`:** This initializes a variable `top_cube` with a value of positive infinity (`float('inf')`). This will represent the largest cube placed so far on top of the stack.

```python
while d:
    bottom_cube = d.popleft() if d[0] > d[-1] else d.pop()
    
    if(bottom_cube <= top_cube):
        top_cube = bottom_cube
    else:
        break
```
- **Processing the deque:**
  - `while d:`: This loop continues until the deque `d` is empty.
  - `bottom_cube = d.popleft() if d[0] > d[-1] else d.pop()`: This line selects the larger cube from either the left or right end of the deque. 
    - If the cube at the front (`d[0]`) is greater than the cube at the back (`d[-1]`), the cube at the front is removed and assigned to `bottom_cube`.
    - Otherwise, the cube at the back is removed and assigned to `bottom_cube`.
  - `if (bottom_cube <= top_cube):`: If the current `bottom_cube` can be placed on the stack (i.e., it's smaller than or equal to the `top_cube`), it becomes the new `top_cube`.
  - `else: break`: If the `bottom_cube` is larger than the `top_cube`, the process is stopped because the cubes can't be stacked in non-increasing order.

```python
print("No" if d else "Yes")
```
- **Checking the result:**
  - After the while loop, if the deque `d` is empty (`d` is falsy), it means all cubes were successfully stacked in non-increasing order, so "Yes" is printed.
  - If the deque is not empty (`d` is truthy), it means that at some point a cube couldn't be placed on top, so "No" is printed.

### Example Walkthrough

Let's say we have two test cases with the following inputs:

```
2
6
4 3 2 1 3 4
5
3 7 6 2 5
```

#### Test Case 1: `4 3 2 1 3 4`

1. Initial deque: `deque([4, 3, 2, 1, 3, 4])`
2. Choose the larger of `4` and `4`. Choose either, say the right: `4`. Deque: `deque([4, 3, 2, 1, 3])`, `top_cube = 4`.
3. Choose the larger of `4` and `3`. Choose `4`. Deque: `deque([3, 2, 1, 3])`, `top_cube = 4`.
4. Choose the larger of `3` and `3`. Choose either, say the right: `3`. Deque: `deque([3, 2, 1])`, `top_cube = 3`.
5. Choose the larger of `3` and `1`. Choose `3`. Deque: `deque([2, 1])`, `top_cube = 3`.
6. Choose the larger of `2` and `1`. Choose `2`. Deque: `deque([1])`, `top_cube = 2`.
7. Choose the remaining `1`. Deque: `deque([])`, `top_cube = 1`.
8. The deque is empty, so print "Yes".

#### Test Case 2: `3 7 6 2 5`

1. Initial deque: `deque([3, 7, 6, 2, 5])`
2. Choose the larger of `3` and `5`. Choose `5`. Deque: `deque([3, 7, 6, 2])`, `top_cube = 5`.
3. Choose the larger of `3` and `2`. Choose `3`. Deque: `deque([7, 6, 2])`, `top_cube = 3`.
4. Choose the larger of `7` and `2`. Choose `7`. Deque: `deque([6, 2])`, `top_cube = 7`.
5. The `bottom_cube` is `7`, which is larger than `top_cube` (3), so we break the loop.
6. The deque is not empty, so print "No".

### Summary

- The code checks if the cubes can be stacked from either end of a list in non-increasing order.
- It outputs "Yes" if the cubes can be stacked properly, and "No" otherwise.
