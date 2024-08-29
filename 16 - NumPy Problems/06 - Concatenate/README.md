<h1 align='center'>Concatenate</h1>

## Problem Statement

**Problem URL :** [Concatenate](https://www.hackerrank.com/challenges/np-concatenate/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/bbd615c7-18c4-44b8-9f40-03a05f813544)
![image](https://github.com/user-attachments/assets/4cf3d714-3b1d-4ca6-87f1-ef440560f3d3)

## Problem Solution
```py
import numpy as np

N, M, P = map(int, input().split())

arr1 = []
arr2 = []
while(N > 0):
    arr1.append(list(map(int, input().split())))
    N -= 1
while(M > 0):
    arr2.append(list(map(int, input().split())))
    M -= 1


np_array1 = np.array(arr1)
np_array2 = np.array(arr2)

print(np.concatenate((np_array1, np_array2), axis=(M+N)*P))
```

## Problem Solution Explanation
Let's break down the code and explain each part in detail, focusing on the logic and the potential issue with the `axis` parameter in the `np.concatenate` function.

### 1. **Importing NumPy Library:**
   ```python
   import numpy as np
   ```
   - **`import numpy as np`**: This imports the NumPy library and assigns it the alias `np`. NumPy is a powerful library in Python for numerical operations, particularly useful for handling arrays and matrices.

### 2. **Reading Input for Dimensions:**
   ```python
   N, M, P = map(int, input().split())
   ```
   - **`N, M, P`**: These are three integers representing:
     - **`N`**: The number of rows in the first array (`arr1`).
     - **`M`**: The number of rows in the second array (`arr2`).
     - **`P`**: A factor that is intended to influence the axis on which the arrays are concatenated.

   - **`input().split()`**: Reads a single line of input, splits it into three parts (by default on whitespace), and converts them to integers using `map(int, ...)`.

### 3. **Creating the Two Arrays:**
   ```python
   arr1 = []
   arr2 = []
   while N > 0:
       arr1.append(list(map(int, input().split())))
       N -= 1
   while M > 0:
       arr2.append(list(map(int, input().split())))
       M -= 1
   ```
   - **Creating `arr1`**: 
     - An empty list `arr1` is created.
     - A `while` loop runs `N` times, each time appending a list of integers (read from input) to `arr1`.
     - Each `input().split()` reads a line of input, splits it into parts, converts them to integers, and creates a list that is added to `arr1`.
     - The loop continues until `N` becomes 0.
   - **Creating `arr2`**: 
     - Similar to `arr1`, `arr2` is created with `M` rows.

### 4. **Converting Lists to NumPy Arrays:**
   ```python
   np_array1 = np.array(arr1)
   np_array2 = np.array(arr2)
   ```
   - **`np.array(arr1)`**: Converts the list `arr1` into a NumPy array `np_array1`.
   - **`np.array(arr2)`**: Converts the list `arr2` into a NumPy array `np_array2`.

### 5. **Concatenating the Arrays:**
   ```python
   print(np.concatenate((np_array1, np_array2), axis=(M+N)*P))
   ```
   - **`np.concatenate((np_array1, np_array2), axis=(M+N)*P)`**: Attempts to concatenate `np_array1` and `np_array2` along the axis specified by the expression `(M + N) * P`.
     - **`M + N`**: This is the sum of the number of rows in both arrays.
     - **`(M + N) * P`**: Multiplies the sum of the rows by `P`, intending to calculate the axis for concatenation.

### 6. **Potential Issues:**
   - **Axis Value**: 
     - The value of `axis` in NumPy's `np.concatenate` must be `0` (for row-wise concatenation) or `1` (for column-wise concatenation) when dealing with 2D arrays.
     - The expression `(M + N) * P` is problematic because it could produce an invalid axis value. For example, if `M = 2`, `N = 3`, and `P = 1`, the axis would be `(2 + 3) * 1 = 5`, which is out of bounds for a 2D array (which only has axes 0 and 1).
     - This could lead to a runtime error: `AxisError: axis 5 is out of bounds for array of dimension 2`.

### 7. **Correct Usage:**
   - The axis should be explicitly defined as `0` or `1`, depending on the desired concatenation:
     - **`axis=0`**: Vertically stack the arrays (row-wise concatenation).
     - **`axis=1`**: Horizontally stack the arrays (column-wise concatenation).

   - A correct version of the concatenation could be:
     ```python
     print(np.concatenate((np_array1, np_array2), axis=P))
     ```
     Assuming `P` is valid for the dimensions of the arrays.

### Example:

Let’s consider an example with proper values:

**Input:**
```
2 3 0
1 2
3 4
5 6
7 8
9 10
```
- **`N` = 2**: `arr1` will have 2 rows.
- **`M` = 3**: `arr2` will have 3 rows.
- **`P` = 0**: Concatenate along rows.

**Arrays:**
- `arr1`:
  ```
  [[1, 2],
   [3, 4]]
  ```
- `arr2`:
  ```
  [[5, 6],
   [7, 8],
   [9, 10]]
  ```

**Correct Concatenation:**
```python
print(np.concatenate((np_array1, np_array2), axis=0))
```
**Output:**
```
[[ 1  2]
 [ 3  4]
 [ 5  6]
 [ 7  8]
 [ 9 10]]
```

### Conclusion:
- The main issue is the use of `(M + N) * P` for the `axis` parameter in `np.concatenate`. This could result in invalid axis values.
- Ensure the `axis` is correctly set to either `0` or `1` depending on the desired concatenation.
