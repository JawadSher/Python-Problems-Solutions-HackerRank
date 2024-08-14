<h1 align='center'>DefaultDict - Tutorial</h1>

## Problem Statement

**Problem URL :** [DefaultDict Tutorial](https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/71cbca9c-8ac4-400e-a4c4-768dbb4fdb0f)
![image](https://github.com/user-attachments/assets/636364c9-6e0d-44c9-b820-3116bc6400a0)
![image](https://github.com/user-attachments/assets/9a423c76-1ceb-4a4e-8d0a-3ada44019498)



## Problem Solution

```py
from collections import defaultdict

n, m = map(int, input().split())

d = defaultdict(list)


for i in range(n):
    d['first'].append(input()) 

for i in range(m):
    d['second'].append(input())
    
for i in d['second']:
    result = []
    for j in range(len(d['first'])):
        if i == d['first'][j]:
            result.append(str(j+1))
    
    if len(result) == 0:
        result.append(str(-1))
    print(' '.join(result))
```


## Problem Solution Explanation

Let's break down this code step by step:

```python
from collections import defaultdict
```
- This line imports the `defaultdict` class from the `collections` module. A `defaultdict` is a type of dictionary that provides a default value for missing keys, which can be very useful for organizing data.

```python
n, m = map(int, input().split())
```
- This line reads a single line of input, splits it into two parts, and converts those parts into integers. These integers are assigned to the variables `n` and `m`.
- `n` represents the number of elements in the first list.
- `m` represents the number of elements in the second list.

```python
d = defaultdict(list)
```
- This line initializes `d` as a `defaultdict` with lists as default values. This means that if a key is not found in `d`, it will automatically be initialized with an empty list.

```python
for i in range(n):
    d['first'].append(input())
```
- This loop runs `n` times. Each time, it reads a line of input and appends it to the list associated with the key `'first'` in the `defaultdict` `d`.
- After this loop, `d['first']` will contain `n` strings from the input.

```python
for i in range(m):
    d['second'].append(input())
```
- This loop runs `m` times. Each time, it reads a line of input and appends it to the list associated with the key `'second'` in the `defaultdict` `d`.
- After this loop, `d['second']` will contain `m` strings from the input.

```python
for i in d['second']:
    result = []
    for j in range(len(d['first'])):
        if i == d['first'][j]:
            result.append(str(j+1))
    
    if len(result) == 0:
        result.append(str(-1))
    print(' '.join(result))
```
- This block of code processes each element in `d['second']`. For each element `i` in `d['second']`:
  - An empty list `result` is initialized.
  - A loop iterates over the indices of `d['first']`.
  - For each index `j`, it checks if the element `i` from `d['second']` is equal to the element at index `j` in `d['first']`.
  - If a match is found, the index (adjusted by adding 1, to convert from zero-based to one-based index) is added to the `result` list as a string.
  - If no matches are found (`result` is still empty), `-1` is added to `result`.
  - Finally, the `result` list is converted to a space-separated string and printed.

### Summary
1. The code initializes a dictionary with lists to store two sets of inputs.
2. It reads `n` lines into the first list and `m` lines into the second list.
3. For each element in the second list, it checks if it exists in the first list.
4. It prints the indices of all occurrences of the element from the second list in the first list. If no occurrences are found, it prints `-1`.

The purpose of this code is to find and display the 1-based indices of elements from the second list in the first list.
