![image](https://github.com/user-attachments/assets/c0d8db47-883e-4255-b17a-54baf2697bf7)<h1 align='center'>Transpose - And - Flatten</h1>

## Problem Statement

**Problem URL :** [Transpose and Flatten](https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/67889cfe-fa13-49b8-8004-c01a49277490)
![image](https://github.com/user-attachments/assets/fe11f09c-e91a-4948-98b4-8181160fd513)


## Problem Solution
```py
import numpy as np

N, M = map(int, input().split())
arr = []

while N > 0:
    arr.append(list(map(int, input().split())))
    N -= 1

np_array = np.array(arr, int)

print(np.transpose(np_array))
print(np_array.flatten())

```

## Problem Solution Explanation
Let’s break down the code step-by-step, explaining each line in detail with examples.

### 1. **Importing the NumPy Library:**
   ```python
   import numpy as np
   ```
   - **`import numpy as np`**: This imports the NumPy library and gives it the alias `np`. NumPy is a library for numerical operations in Python and is commonly used for handling arrays and matrices.

### 2. **Reading Input for Dimensions:**
   ```python
   N, M = map(int, input().split())
   ```
   - **`input()`**: Reads a line of input from the user as a string.
   - **`.split()`**: Splits the input string into a list of substrings based on whitespace. For example, if the input is `"2 3"`, this results in `['2', '3']`.
   - **`map(int, ...)`**: Applies the `int` function to each substring in the list to convert them to integers. This results in `map(int, ['2', '3'])`, which is equivalent to `[2, 3]`.
   - **`N, M = ...`**: Unpacks the list `[2, 3]` into two variables, `N` and `M`. Here, `N` is assigned `2` (number of rows), and `M` is assigned `3` (number of columns).

### 3. **Initializing an Empty List for the Array:**
   ```python
   arr = []
   ```
   - **`arr = []`**: Initializes an empty list `arr` that will be used to store the rows of the matrix as lists of integers.

### 4. **Reading Matrix Rows:**
   ```python
   while N > 0:
       arr.append(list(map(int, input().split())))
       N -= 1
   ```
   - **`while N > 0:`**: This loop continues to execute as long as `N` is greater than `0`. It reads `N` rows of input.
   - **`input().split()`**: Reads a line of input, splits it into a list of strings.
   - **`map(int, ...)`**: Converts each string in the list to an integer.
   - **`list(map(int, ...))`**: Converts the mapped object into a list of integers representing a row of the matrix.
   - **`arr.append(...)`**: Adds the list of integers as a new row in the matrix `arr`.
   - **`N -= 1`**: Decrements `N` by 1 after each row is read. This ensures that the loop runs exactly `N` times.

### 5. **Creating a NumPy Array:**
   ```python
   np_array = np.array(arr, int)
   ```
   - **`np.array(arr, int)`**: Converts the list `arr` into a NumPy array of type `int`. The `arr` list, which contains the rows of the matrix, becomes a 2D NumPy array.

### 6. **Printing the Transposed Array:**
   ```python
   print(np.transpose(np_array))
   ```
   - **`np.transpose(np_array)`**: Transposes the NumPy array `np_array`. Transposing switches rows with columns. For example, a 2x3 array becomes a 3x2 array.
   - **`print(...)`**: Prints the transposed array.

### 7. **Printing the Flattened Array:**
   ```python
   print(np_array.flatten())
   ```
   - **`np_array.flatten()`**: Flattens the 2D NumPy array `np_array` into a 1D array. This collapses all dimensions into a single dimension.
   - **`print(...)`**: Prints the flattened array.

### Example Input and Output:

**Example Input:**
```
2 3
1 2 3
4 5 6
```
- **`N = 2`** (number of rows)
- **`M = 3`** (number of columns)

**Execution of Code:**

1. **Reading Dimensions:**
   - `N` is `2` and `M` is `3`.

2. **Reading Rows:**
   - The first line `1 2 3` is converted to `[1, 2, 3]` and added as the first row.
   - The second line `4 5 6` is converted to `[4, 5, 6]` and added as the second row.
   - The list `arr` becomes `[[1, 2, 3], [4, 5, 6]]`.

3. **Creating the NumPy Array:**
   - `np_array` becomes:
     ```
     array([[1, 2, 3],
            [4, 5, 6]])
     ```

4. **Printing the Transposed Array:**
   - Transposed array:
     ```
     array([[1, 4],
            [2, 5],
            [3, 6]])
     ```
   - The first row `[1, 2, 3]` becomes the first column, and the second row `[4, 5, 6]` becomes the second column.

5. **Printing the Flattened Array:**
   - Flattened array:
     ```
     array([1, 2, 3, 4, 5, 6])
     ```
   - The 2D array is converted into a single list of values.

With these explanations, the code is designed to handle matrix input, process it using NumPy, and output both the transposed and flattened forms of the matrix.
