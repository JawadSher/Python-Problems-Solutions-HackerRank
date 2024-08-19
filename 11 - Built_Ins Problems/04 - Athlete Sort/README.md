<h1 align='center'>Athlete - Sort</h1>

## Problem Statement

**Problem URL :** [Athlete Sort](https://www.hackerrank.com/challenges/python-sort-sort/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/73ba514a-4952-4b08-8a26-a68db5f52a38)
![image](https://github.com/user-attachments/assets/1c0e56da-6025-4d67-a19d-20e8631b0e06)


## Problem Solution

```py
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    result = sorted(arr, key=lambda x : x[k])
    for i in result:
        print(*i)
```

## Problem Solution Explanation
Let's break down this Python code step by step to understand how it works. The code reads a matrix (a list of lists), sorts it based on one of its columns, and then prints the sorted matrix. This kind of problem is common in coding competitions or practice platforms.

1. **Importing Required Modules:**
   ```python
   import math
   import os
   import random
   import re
   import sys
   ```
   - These modules are imported for potential use in the program, but in this specific code, they are not actively used.

2. **Reading Input:**
   ```python
   nm = input().split()
   n = int(nm[0])
   m = int(nm[1])
   ```
   - **`input()`**: Reads a line of input from the user.
   - **`.split()`**: Splits the input string into a list of strings based on spaces.
   - **`nm = input().split()`**: This line reads two numbers `n` and `m`, which represent the number of rows and columns in the matrix, and splits them into a list `nm`.
   - **`n = int(nm[0])` and `m = int(nm[1])`**: These lines convert the first and second elements of the `nm` list into integers, representing the number of rows (`n`) and columns (`m`).

   **Example:**  
   If the input is `3 4`, then `n = 3` (rows) and `m = 4` (columns).

3. **Reading the Matrix:**
   ```python
   arr = []
   for _ in range(n):
       arr.append(list(map(int, input().rstrip().split())))
   ```
   - **`arr = []`**: Initializes an empty list to store the matrix.
   - **`for _ in range(n):`**: Loops `n` times to read each row of the matrix.
   - **`input().rstrip().split()`**: Reads a line of input, removes any trailing whitespace, and splits it into a list of strings.
   - **`map(int, input().rstrip().split())`**: Converts the list of strings into a list of integers.
   - **`list(map(int, ...))`**: The result is converted to a list.
   - **`arr.append(list(...))`**: Each row (list of integers) is appended to the `arr` list, building up the matrix.

   **Example:**  
   If the input is:
   ```
   10 2 5 1
   7 1 0 2
   9 9 9 9
   ```
   The matrix `arr` will be:
   ```python
   arr = [
       [10, 2, 5, 1],
       [7, 1, 0, 2],
       [9, 9, 9, 9]
   ]
   ```

4. **Reading the Column Index `k`:**
   ```python
   k = int(input())
   ```
   - **`k = int(input())`**: Reads the index `k` (the column to sort by) as an integer.
   
   **Example:**  
   If the input is `2`, then `k = 2`.

5. **Sorting the Matrix:**
   ```python
   result = sorted(arr, key=lambda x: x[k])
   ```
   - **`sorted(arr, key=lambda x: x[k])`**: This line sorts the matrix `arr` based on the `k`-th column.
   - **`key=lambda x: x[k]`**: The `lambda` function specifies that the sorting key for each row `x` is the element at index `k` in that row.
   - The `sorted()` function returns a new list (`result`) with the rows sorted based on the `k`-th column.

   **Example:**  
   With `k = 2`, the matrix will be sorted based on the 3rd element of each row:
   ```python
   result = [
       [7, 1, 0, 2],  # 0 in the 2nd index
       [10, 2, 5, 1], # 5 in the 2nd index
       [9, 9, 9, 9]   # 9 in the 2nd index
   ]
   ```

6. **Printing the Sorted Matrix:**
   ```python
   for i in result:
       print(*i)
   ```
   - **`for i in result:`**: Iterates over each row in the sorted matrix `result`.
   - **`print(*i)`**: The `*i` syntax unpacks the list `i` so that each element is printed separately, without brackets or commas, resulting in a clean output.

   **Example Output:**
   ```
   7 1 0 2
   10 2 5 1
   9 9 9 9
   ```

### Complete Example:

**Input:**
```
3 4
10 2 5 1
7 1 0 2
9 9 9 9
2
```

**Explanation:**
- `n = 3` (rows), `m = 4` (columns)
- Matrix `arr`:
  ```
  10 2 5 1
  7 1 0 2
  9 9 9 9
  ```
- `k = 2` (sort by the 3rd column)
- After sorting by the 3rd column, the matrix becomes:
  ```
  7 1 0 2
  10 2 5 1
  9 9 9 9
  ```

**Output:**
```
7 1 0 2
10 2 5 1
9 9 9 9
```

### Conclusion:
This code allows you to input a matrix, specify a column, and then sort the entire matrix based on the values in that column. It’s a common operation in data processing where sorting data based on certain criteria is required. This explanation, along with the example, should make it easier for beginners to understand how the code works and what each part does.

