<h1 align='center'>Zeros - and - Ones</h1>

## Problem Statement

**Problem URL :** [Zeros and Ones](https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/d7850120-e7c2-47f0-a707-91d7f879a14f)
![image](https://github.com/user-attachments/assets/e95ac3fa-f88c-43ff-8696-31a14d9269a1)

## Problem Solution
```py
import numpy as np

input_nums = list(map(int, input().split()))
zeros_arr = np.zeros(input_nums, dtype=np.int)
ones_arr = np.ones(input_nums, dtype=np.int)

print(zeros_arr)
print(ones_arr)
```

## Problem Solution Explanation
Let's go through the code line by line, explaining each part in detail with examples:

### 1. **Importing the NumPy Library:**
   ```python
   import numpy as np
   ```
   - **`import numpy as np`**: This imports the NumPy library and gives it the alias `np`. NumPy is widely used for numerical computations and handling arrays in Python.

### 2. **Reading Input and Converting to a List of Integers:**
   ```python
   input_nums = list(map(int, input().split()))
   ```
   - **`input()`**: Reads a line of input from the user as a string. For example, if the input is `"3 4"`, it reads `"3 4"`.
   - **`.split()`**: Splits the input string into a list of substrings based on whitespace. For example, `"3 4"` becomes `['3', '4']`.
   - **`map(int, ...)`**: Converts each substring in the list to an integer. The result is `map(int, ['3', '4'])`, which yields `[3, 4]`.
   - **`list(...)`**: Converts the map object to a list. Thus, `input_nums` becomes `[3, 4]`.

### 3. **Creating a NumPy Array of Zeros:**
   ```python
   zeros_arr = np.zeros(input_nums, dtype=np.int)
   ```
   - **`np.zeros(...)`**: Creates a NumPy array filled with zeros.
     - **`input_nums`**: Specifies the shape of the array. If `input_nums` is `[3, 4]`, this means a 2D array with 3 rows and 4 columns.
     - **`dtype=np.int`**: Specifies the data type of the array elements. `np.int` is an alias for integers, but using `np.int` directly is deprecated; `np.int32` or `np.int64` is preferred.
   - **Example**: If `input_nums` is `[3, 4]`, `zeros_arr` will be:
     ```
     array([[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]])
     ```

### 4. **Creating a NumPy Array of Ones:**
   ```python
   ones_arr = np.ones(input_nums, dtype=np.int)
   ```
   - **`np.ones(...)`**: Creates a NumPy array filled with ones.
     - **`input_nums`**: Specifies the shape of the array. For `input_nums = [3, 4]`, this results in a 2D array with 3 rows and 4 columns.
     - **`dtype=np.int`**: Specifies the data type of the array elements. As with `np.zeros`, `np.int32` or `np.int64` is preferred.
   - **Example**: If `input_nums` is `[3, 4]`, `ones_arr` will be:
     ```
     array([[1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]])
     ```

### 5. **Printing the Arrays:**
   ```python
   print(zeros_arr)
   print(ones_arr)
   ```
   - **`print(zeros_arr)`**: Prints the array of zeros.
   - **`print(ones_arr)`**: Prints the array of ones.

### Example Walkthrough:

1. **Example Input:**
   ```
   3 4
   ```
   - **Conversion to List**: `input_nums` becomes `[3, 4]`.

2. **Creating `zeros_arr`:**
   - **Array Creation**: `np.zeros([3, 4], dtype=np.int)` creates:
     ```
     array([[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]])
     ```

3. **Creating `ones_arr`:**
   - **Array Creation**: `np.ones([3, 4], dtype=np.int)` creates:
     ```
     array([[1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]])
     ```

4. **Output:**
   ```
   [[0 0 0 0]
    [0 0 0 0]
    [0 0 0 0]]
   [[1 1 1 1]
    [1 1 1 1]
    [1 1 1 1]]
   ```

### Summary:
- The code reads dimensions from input, creates two NumPy arrays: one filled with zeros and one filled with ones, both having the specified shape, and prints these arrays. Adjustments include using more specific data types like `np.int32` or `np.int64` instead of the deprecated `np.int`.
