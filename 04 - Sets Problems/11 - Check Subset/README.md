<h1 align='center'>Check - Subset</h1>

## Problem Statement

**Problem URL :** [Check Subset](https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/0e0626d3-c1e3-4b50-be30-8a398b5d4feb)
![image](https://github.com/user-attachments/assets/616068e8-0ba4-4572-98a5-f7202424b8a7)


## Problem Explanation

To solve the problem of determining whether one set is a subset of another for multiple test cases, follow these steps:

1. **Input Reading**: Read the number of test cases.
2. **Processing Each Test Case**:
   - Read the number of elements in the first set and then the elements themselves.
   - Read the number of elements in the second set and then the elements themselves.
   - Convert the lists of elements into sets.
   - Check if the first set is a subset of the second set using the `issubset` method.
3. **Output**: Print `True` if the first set is a subset of the second set; otherwise, print `False`.


## Problem Solution

```py
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
```

## Problem Solution Explanation
The code is designed to check whether one set (set_A) is a subset of another set (set_B) for multiple test cases. Here's a detailed explanation:

```python
test_cases = int(input())
```
- **Input**: Reads the number of test cases. This is the total number of times the subsequent block of code will run.
- **Example**: If the input is `3`, it means there are 3 test cases to process.

```python
for _ in range(test_cases):
    A = int(input())
    set_A = set(input().split())
    B = int(input())
    set_B = set(input().split())
```
- **Loop**: The `for` loop iterates through each test case. The variable `_` is used because the loop variable is not needed in this case.
- **Input Reading**:
  - `A` and `B` are the sizes of `set_A` and `set_B`, respectively. These values are read but are not actually used in the code.
  - `set_A = set(input().split())` reads the elements for set_A, splits them by spaces, converts them to integers, and creates a set.
  - `set_B = set(input().split())` reads the elements for set_B in the same way.

### Checking Subset

```python
if set_A.union(set_B) == set_B:
    print(True)
else:
    print(False)
```
- **Union Operation**: `set_A.union(set_B)` computes the union of `set_A` and `set_B`. The union of two sets includes all unique elements from both sets.
- **Subset Check**: `set_A.union(set_B) == set_B` checks if the union of `set_A` and `set_B` is equal to `set_B`. This means that all elements of `set_A` must be present in `set_B` for `set_A` to be a subset of `set_B`.
  - **If True**: It means `set_A` is a subset of `set_B`, and the code prints `True`.
  - **If False**: It means `set_A` is not a subset of `set_B`, and the code prints `False`.

### Example Walkthrough

Let's walk through an example with specific inputs to understand how the code works:

#### Example Input

```
2
3
1 2 3
5
3 2 1 4 5
4
2 4 6 8
6
8 6 5 4 3 2
```

#### Detailed Execution

**Test Case 1:**
1. **Input Reading:**
   - `A = 3` (Size of set_A)
   - `set_A = {1, 2, 3}`
   - `B = 5` (Size of set_B)
   - `set_B = {1, 2, 3, 4, 5}`
2. **Union Operation:**
   - `set_A.union(set_B) = {1, 2, 3, 4, 5}`
3. **Subset Check:**
   - `set_A.union(set_B) == set_B` evaluates to `{1, 2, 3, 4, 5} == {1, 2, 3, 4, 5}`, which is `True`.
   - Print `True`.

**Test Case 2:**
1. **Input Reading:**
   - `A = 4` (Size of set_A)
   - `set_A = {2, 4, 6, 8}`
   - `B = 6` (Size of set_B)
   - `set_B = {2, 3, 4, 5, 6, 8}`
2. **Union Operation:**
   - `set_A.union(set_B) = {2, 3, 4, 5, 6, 8}`
3. **Subset Check:**
   - `set_A.union(set_B) == set_B` evaluates to `{2, 3, 4, 5, 6, 8} == {2, 3, 4, 5, 6, 8}`, which is `True`.
   - Print `True`.

**Final Output:**

```
True
True
```

### Summary

- The code reads the number of test cases and processes each one to determine if one set is a subset of another.
- It uses the union operation to help with the subset check.
- It then prints `True` if the first set is a subset of the second, and `False` otherwise.
