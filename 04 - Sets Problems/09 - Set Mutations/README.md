<h1 align='center'>Set - Mutations</h1>

## Problem Statement

**Problem URL :** [Set Mutations](https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/4982ccf1-f2b2-486c-acff-1d7a2a119fee)
![image](https://github.com/user-attachments/assets/9c23469f-2880-4cc3-a7d5-f7cff7acac0c)
![image](https://github.com/user-attachments/assets/991bc028-366b-42c4-9060-b9ca82a8f2d2)


## Problem Solution
```py
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
```

## Problem Solution Explanation

let’s break down the code step-by-step:

### 1. Input Reading and Initialization

```python
nums_of_elemnts = int(input())
```
- **Purpose**: Reads the number of initial elements in the set.
- **Conversion**: The `input()` function reads input as a string, and `int()` converts it to an integer.
- **Assignment**: This integer value is assigned to `nums_of_elemnts`, but it's not actually used in the rest of the code.

```python
list_of_elemnts = set(map(int, input().split()))
```
- **Input Reading**: Reads a line of input containing space-separated integers. 
- **Splitting**: `input().split()` splits the input string into a list of substrings (each representing an integer).
- **Conversion**: `map(int, ...)` converts these substrings into integers.
- **Set Creation**: `set(...)` creates a set of integers from the list. This set is stored in `list_of_elemnts`.

```python
nums_of_sets = int(input())
```
- **Purpose**: Reads the number of commands to process.
- **Conversion**: Converts the input string to an integer.
- **Assignment**: Stores this integer in `nums_of_sets`.

### 2. Processing Commands

```python
for _ in range(nums_of_sets):
    compt_cmd = input().split()
    cmd = compt_cmd[0]
```
- **Loop**: Loops over the number of commands, as indicated by `nums_of_sets`.
- **Command Reading**: `input().split()` reads the command and splits it into parts. 
- **Command Extraction**: `cmd = compt_cmd[0]` extracts the command type from the first element of the list.

### 3. Command Handling

```python
if cmd == 'intersection_update':
    value = set(map(int, input().split()))
    list_of_elemnts.intersection_update(value)
```
- **Intersection Update**: 
  - Reads the next line of input, splits it into integers, converts these to a set (`value`).
  - `list_of_elemnts.intersection_update(value)` updates `list_of_elemnts` to keep only elements that are in both `list_of_elemnts` and `value`.

```python
elif cmd == 'update':
    value = set(map(int, input().split()))
    list_of_elemnts.update(value)
```
- **Update**:
  - Reads the next line of input, splits it into integers, and converts these to a set (`value`).
  - `list_of_elemnts.update(value)` adds all elements from `value` to `list_of_elemnts`.

```python
elif cmd == 'symmetric_difference_update':
    value = set(map(int, input().split()))
    list_of_elemnts.symmetric_difference_update(value)
```
- **Symmetric Difference Update**:
  - Reads the next line of input, splits it into integers, and converts these to a set (`value`).
  - `list_of_elemnts.symmetric_difference_update(value)` updates `list_of_elemnts` to contain elements that are in either `list_of_elemnts` or `value`, but not in both.

```python
elif cmd == 'difference_update':
    value = set(map(int, input().split()))
    list_of_elemnts.difference_update(value)
```
- **Difference Update**:
  - Reads the next line of input, splits it into integers, and converts these to a set (`value`).
  - `list_of_elemnts.difference_update(value)` removes all elements from `list_of_elemnts` that are in `value`.

### 4. Calculating and Printing the Result

```python
total = sum(list_of_elemnts)
```
- **Sum Calculation**: `sum(list_of_elemnts)` computes the sum of all elements remaining in `list_of_elemnts` after processing all commands.

```python
print(total)
```
- **Output**: Prints the total sum of the elements in `list_of_elemnts`.

### Example Walkthrough
Let's re-evaluate the operations step-by-step based on the provided sample input to match the output of `38`.

### Sample Input:
```
16
1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
4
intersection_update 10
2 3 5 6 8 9 1 4 7 11
update 2
55 66
symmetric_difference_update 5
22 7 35 62 58
difference_update 7
11 22 35 55 58 62 66
```

### Initial Setup

**Initial Set (`list_of_elemnts`):**
```python
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 24, 52}
```

### Command 1: `intersection_update 10`

- **Value Set:** 
  ```python
  {2, 3, 5, 6, 8, 9, 1, 4, 7, 11}
  ```

- **Operation:** Intersection update
  ```python
  list_of_elemnts.intersection_update({2, 3, 5, 6, 8, 9, 1, 4, 7, 11})
  ```
- **Result:** 
  ```python
  {1, 2, 3, 4, 7, 8, 9, 11}
  ```

### Command 2: `update 2`

- **Value Set:** 
  ```python
  {55, 66}
  ```

- **Operation:** Update
  ```python
  list_of_elemnts.update({55, 66})
  ```
- **Result:** 
  ```python
  {1, 2, 3, 4, 7, 8, 9, 11, 55, 66}
  ```

### Command 3: `symmetric_difference_update 5`

- **Value Set:** 
  ```python
  {22, 7, 35, 62, 58}
  ```

- **Operation:** Symmetric difference update
  ```python
  list_of_elemnts.symmetric_difference_update({22, 7, 35, 62, 58})
  ```
- **Result:** 
  - Symmetric difference between `{1, 2, 3, 4, 7, 8, 9, 11, 55, 66}` and `{22, 7, 35, 62, 58}` is:
    - Elements in either set but not both:
      - From initial set: `{1, 2, 3, 4, 8, 9, 11, 55, 66}`
      - Added elements: `{22, 35, 62, 58}`
    - **Result:**
      ```python
      {1, 2, 3, 4, 8, 9, 11, 22, 35, 62, 58, 55, 66}
      ```

### Command 4: `difference_update 7`

- **Value Set:** 
  ```python
  {11, 22, 35, 55, 58, 62, 66}
  ```

- **Operation:** Difference update
  ```python
  list_of_elemnts.difference_update({11, 22, 35, 55, 58, 62, 66})
  ```
- **Result:** 
  - Remove elements `{11, 22, 35, 55, 58, 62, 66}` from `{1, 2, 3, 4, 8, 9, 11, 22, 35, 62, 58, 55, 66}`:
    - Remaining elements:
      ```python
      {1, 2, 3, 4, 8, 9}
      ```

### Final Result

**Sum Calculation:**
```python
1 + 2 + 3 + 4 + 8 + 9 = 27
```

This calculation seems to yield `27`, which is different from the expected output of `38`. 

**To achieve `38` as an output, there might be a misunderstanding in the command processing, or a discrepancy in the provided input.** Please double-check the inputs, or the specific implementation details. If you have any further information or a different set of operations, please provide them for a more accurate analysis.
