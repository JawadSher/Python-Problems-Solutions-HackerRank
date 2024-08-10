<h1 align='center'>Check - Strict - Superset</h1>

## Problem Statement

**Problem URL :** [Check Strict Superset](https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/e48d68a3-5146-4f3b-be53-e993d3139a2b)
![image](https://github.com/user-attachments/assets/7b561fbd-b9b6-4941-8b2d-aa08a8d8a2fc)


## Problem Solution
```py

set_A = set(map(int, input().split()))
n = int(input())

is_subset = True

for _ in range(n):
    other_set = set(map(int, input().split()))
    if not set_A.issuperset(other_set) and len(set_A) > len(other_set):
        is_subset = False
        break
        
print(is_subset)
```

## Problem Solution Explanation

Let's break down the provided code and understand its functionality in detail, along with examples.

#### 1. Reading Input and Initialization

```python
set_A = set(map(int, input().split()))
n = int(input())
```
- **`set_A`**: Reads the first line of input, splits it into individual elements, converts them to integers, and creates a set `set_A`.
- **`n`**: Reads the number of subsequent sets.

**Example Input:**
```
1 2 3
2
4 5 1 2
1 2
```
- **`set_A`** will be `{1, 2, 3}`.
- **`n`** will be `2` (indicating there are 2 sets to check).

#### 2. Checking Superset Condition

```python
is_subset = True

for _ in range(n):
    other_set = set(map(int, input().split()))
    if not set_A.issuperset(other_set) and len(set_A) > len(other_set):
        is_subset = False
        break
```
- **`is_subset`**: Initialized to `True`. This flag will indicate if `set_A` is a superset of all other sets.

- **For each set (from `n` sets)**:
  - **`other_set`**: Reads each line of input, splits it, converts to integers, and creates a set `other_set`.
  - **Condition Check**:
    ```python
    if not set_A.issuperset(other_set) and len(set_A) > len(other_set):
    ```
    - **`set_A.issuperset(other_set)`**: Checks if `set_A` contains all elements of `other_set`.
    - **`len(set_A) > len(other_set)`**: Checks if `set_A` is larger than `other_set` in terms of the number of elements.
    - **Combined Condition**: If `set_A` is not a superset of `other_set` and `set_A` has more elements than `other_set`, it implies that `set_A` should contain more elements than `other_set` but still fails to include all elements of `other_set`.

  - **If the condition is met**:
    - **`is_subset = False`**: Sets `is_subset` to `False`.
    - **`break`**: Exits the loop early as we already found one set that `set_A` is not a superset of.

#### 3. Printing the Result

```python
print(is_subset)
```
- Prints `True` if `set_A` is a superset of all other sets, otherwise `False`.

### Example Walkthrough

**Example 1:**

Input:
```
1 2 3
2
4 5 1 2
1 2
```

**Execution:**
1. **Initial Values**:
   - `set_A` = `{1, 2, 3}`
   - `n` = `2`

2. **Processing Each Set**:
   - **First Set**:
     - `other_set` = `{1, 2, 4, 5}`
     - `set_A.issuperset(other_set)` = `False` (because `set_A` does not contain `4` and `5`).
     - `len(set_A) > len(other_set)` = `True` (because `3 > 4` is `False`).
     - Since the condition is not met, continue to the next set.
   - **Second Set**:
     - `other_set` = `{1, 2}`
     - `set_A.issuperset(other_set)` = `True` (because `set_A` contains `1` and `2`).
     - `len(set_A) > len(other_set)` = `True` (because `3 > 2` is `True`).
     - The condition is not met here as well.

3. **Final Output**: Since no set failed the condition, `is_subset` remains `True`. 

Output:
```
True
```

**Example 2:**

Input:
```
1 2 3
3
4 5 1 2
1 2
2 3
```

**Execution:**
1. **Initial Values**:
   - `set_A` = `{1, 2, 3}`
   - `n` = `3`

2. **Processing Each Set**:
   - **First Set**:
     - `other_set` = `{1, 2, 4, 5}`
     - `set_A.issuperset(other_set)` = `False`
     - `len(set_A) > len(other_set)` = `False` (since `3` is not greater than `4`).
     - The condition is not met.
   - **Second Set**:
     - `other_set` = `{1, 2}`
     - `set_A.issuperset(other_set)` = `True`
     - `len(set_A) > len(other_set)` = `True` (since `3 > 2` is `True`).
     - The condition is not met.
   - **Third Set**:
     - `other_set` = `{2, 3}`
     - `set_A.issuperset(other_set)` = `True`
     - `len(set_A) > len(other_set)` = `True` (since `3 > 2` is `True`).
     - The condition is not met.

3. **Final Output**: Since all sets failed the condition, `is_subset` will be `False`.

Output:
```
False
```

### Summary

- The code checks if `set_A` is a superset of all given sets based on the condition.
- The check involves not only verifying if `set_A` is a superset but also ensuring that `set_A` is larger than the `other_set` in size.
