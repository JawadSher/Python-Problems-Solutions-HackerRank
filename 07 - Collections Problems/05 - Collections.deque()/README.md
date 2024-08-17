<h1 align='center'>Collections - .Deque()</h1>

## Problem Statement

**Problem URL :** [Collecitons.deque()](https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/8f89d1ca-d497-4e82-b7a5-b0e6463e7b75)
![image](https://github.com/user-attachments/assets/103f1493-a28e-4eb6-8dca-ff3f52768132)
![image](https://github.com/user-attachments/assets/d294a281-9401-44a9-8b3b-0697c1a91544)

## Problem Solution
```py
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
```

## Problem Solution Explanation
Let's break down the code line by line and explain each part in detail, including how it would work with an example.

```python
from collections import deque
```
- **Importing deque:** This line imports the `deque` class from the `collections` module. `deque` (short for "double-ended queue") is a data structure that allows you to append and pop elements from both ends efficiently.

```python
d = deque()
```
- **Creating a deque object:** This initializes an empty `deque` named `d`. You can think of `deque` as a flexible list where you can efficiently add or remove elements from both ends.

```python
nums_operations = int(input().strip())
```
- **Taking the number of operations as input:** This line reads the total number of operations that the user intends to perform on the deque. It converts the input into an integer and stores it in the variable `nums_operations`.
- Example: If the user inputs `4`, then `nums_operations` will hold the value `4`.

```python
for _ in range(nums_operations):
```
- **Looping through operations:** This loop runs exactly `nums_operations` times. The underscore `_` is used as a loop variable because we don’t need to use it inside the loop. The loop will execute the block of code inside it for each operation.
- Example: If `nums_operations` is `4`, this loop will iterate 4 times.

```python
    cmd = input().split(" ")
```
- **Reading and splitting the command:** This line reads a string input for each operation, splits it by spaces, and stores the parts as a list in `cmd`.
- Example: If the input is `append 10`, `cmd` will become `['append', '10']`.

```python
    prompt = cmd[0]
```
- **Extracting the operation name:** This line assigns the first element of `cmd` (the operation name) to the variable `prompt`.
- Example: If `cmd` is `['append', '10']`, `prompt` will be `'append'`.

```python
    if prompt == 'append':
        value = int(cmd[1])
        d.append(value)
```
- **Handling the `append` operation:** If the operation is `'append'`, the second element of `cmd` (which is the value) is converted to an integer and stored in `value`. Then, this value is appended to the right end of the deque `d`.
- Example: If `prompt` is `'append'` and `cmd[1]` is `'10'`, the deque will have `10` added to its right end.

```python
    elif prompt == 'appendleft':
        value = int(cmd[1])
        d.appendleft(value)
```
- **Handling the `appendleft` operation:** If the operation is `'appendleft'`, the value is converted to an integer and then appended to the left end of the deque.
- Example: If `prompt` is `'appendleft'` and `cmd[1]` is `'20'`, the deque will have `20` added to its left end.

```python
    elif prompt == 'pop':
        d.pop()
```
- **Handling the `pop` operation:** If the operation is `'pop'`, the rightmost (last) element of the deque is removed.
- Example: If the deque is `[10, 20]` and `prompt` is `'pop'`, after this operation, the deque will become `[10]`.

```python
    elif prompt == 'popleft':
        d.popleft()
```
- **Handling the `popleft` operation:** If the operation is `'popleft'`, the leftmost (first) element of the deque is removed.
- Example: If the deque is `[10, 20]` and `prompt` is `'popleft'`, after this operation, the deque will become `[20]`.

```python
for i in d:
    print(i, end=' ')
```
- **Printing the contents of the deque:** After all operations are performed, this loop prints each element in the deque separated by a space. The `end=' '` argument ensures that the output is in a single line with space separation.
- Example: If the deque is `[20, 30, 40]`, the output will be `20 30 40`.

### Example Walkthrough

Let’s say the user provides the following inputs:
```
4
append 10
appendleft 20
append 30
pop
```

Here’s how the code would execute:

1. **Initialization:** 
    - `d` is an empty deque: `deque([])`.
    - `nums_operations` is `4`.

2. **First Operation (`append 10`):**
    - `cmd = ['append', '10']`
    - `prompt = 'append'`
    - `value = 10`
    - `d.append(10)` -> deque becomes: `deque([10])`

3. **Second Operation (`appendleft 20`):**
    - `cmd = ['appendleft', '20']`
    - `prompt = 'appendleft'`
    - `value = 20`
    - `d.appendleft(20)` -> deque becomes: `deque([20, 10])`

4. **Third Operation (`append 30`):**
    - `cmd = ['append', '30']`
    - `prompt = 'append'`
    - `value = 30`
    - `d.append(30)` -> deque becomes: `deque([20, 10, 30])`

5. **Fourth Operation (`pop`):**
    - `cmd = ['pop']`
    - `prompt = 'pop'`
    - `d.pop()` -> deque becomes: `deque([20, 10])`

6. **Printing the Deque:**
    - The deque `d` is `[20, 10]`.
    - The final output will be `20 10`.

This detailed walkthrough should help clarify how the code works step by step!
