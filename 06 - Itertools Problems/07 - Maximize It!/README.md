<h1 align='center'>Maximize - It!</h1>

## Problem Statement

**Problem URL :** [Maximize It!](https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/9b7055d4-4c41-4848-8f04-233b6e401804)
![image](https://github.com/user-attachments/assets/15e29978-e873-4c0c-99ae-7027144febdb)

## Problem Solution
```py
from itertools import product

def calculateMax(m, k, lst):
    result = 0
    
    for combo in product(*lst):
        sums = sum(x**2 for x in combo)
        result = max(sums % k, result)
        
    return result
    
m, k = map(int, input().split())
lists = [list(map(int, input().split()[1:])) for _ in range(m)]

s = calculateMax(m, k, lists)
print(s)
```

## Problem Solution Explanation

Let's break down the code step by step and explain each part in detail.

#### 1. **Imports**

```python
from itertools import product
```

- **`product`**: This function from the `itertools` module generates the Cartesian product of input iterables. It’s used here to generate all possible combinations where each element is chosen from a different list.

#### 2. **Function Definition: `calculateMax`**

```python
def calculateMax(m, k, lst):
    result = 0
    
    for combo in product(*lst):
        sums = sum(x**2 for x in combo)
        result = max(sums % k, result)
        
    return result
```

- **Parameters**:
  - `m`: Number of lists.
  - `k`: The modulo value.
  - `lst`: A list of lists where each sub-list contains integers.

- **Logic**:
  1. **Initialization**: `result` is initialized to `0`. This variable will store the maximum value of the expression found.
  
  2. **Generate Combinations**:
     - `product(*lst)` generates all possible combinations where each combination includes one element from each list. For example, if you have two lists `[1, 2]` and `[3, 4]`, `product` will generate combinations like `(1, 3)`, `(1, 4)`, `(2, 3)`, and `(2, 4)`.

  3. **Compute the Expression**:
     - For each combination, compute the sum of squares of its elements: `sums = sum(x**2 for x in combo)`.
     - Compute `sums % k` to get the result modulo `k`.
     - Update `result` to the maximum value between the current `result` and the computed modulo.

  4. **Return the Maximum Result**:
     - After checking all combinations, return the maximum result found.

#### 3. **Read Input and Call Function**

```python
m, k = map(int, input().split())
lists = [list(map(int, input().split()[1:])) for _ in range(m)]
```

- **Read `m` and `k`**:
  - `m` is the number of lists.
  - `k` is the modulo value.

- **Read Lists**:
  - For each of the `m` lists, read the line of integers, skip the first integer (which represents the number of elements in that list), and convert the rest to a list of integers.

#### 4. **Compute and Print Result**

```python
s = calculateMax(m, k, lists)
print(s)
```

- **Call `calculateMax`** with the input lists and modulo value.
- **Print** the result obtained from `calculateMax`.

### Example

#### Input

```
3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10
```

#### Explanation

1. **Lists**:
   - `[2, 5, 4]`
   - `[3, 7, 8, 9]`
   - `[5, 5, 7, 8, 9, 10]`

2. **Combinations**:
   - All possible combinations of one number from each list, e.g., `(2, 3, 5)`, `(2, 3, 10)`, etc.

3. **Sum of Squares and Modulo Calculation**:
   - For each combination, calculate the sum of squares, e.g., `(2, 3, 5)` gives `4 + 9 + 25 = 38`, and `38 % 1000 = 38`.
   - Update the result with the maximum modulo value found.

4. **Output**:
   - Print the maximum value obtained from the modulo operations.

### Summary

This code finds the maximum value of the sum of squares of elements selected from each list, modulo `k`. It uses Cartesian product to generate all possible combinations and evaluates each to find the maximum result.
