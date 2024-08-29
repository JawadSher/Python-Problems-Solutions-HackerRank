<h1 align='center'>Eye - and - Identity</h1>

## Problem Statement

**Problem URL :** [Eye and Identity](https://www.hackerrank.com/challenges/np-eye-and-identity/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/67d8ef41-d2bf-44a1-8dc6-932ac48df26b)
![image](https://github.com/user-attachments/assets/0200ff76-1507-4a66-a1f7-aa3d05929e62)

## Problem Solution
```py
import numpy as np
np.set_printoptions(legacy='1.13')

N, M = map(int, input().split())

print(np.eye(N, M, k=0))
```

## Problem Solution Explanation
Let's break down the code step-by-step, explaining each line in detail with examples:

### 1. **Importing the NumPy Library:**
   ```python
   import numpy as np
   ```
   - **`import numpy as np`**: This imports the NumPy library and assigns it the alias `np`. NumPy is a popular library in Python for numerical computations, particularly useful for handling arrays and matrices.

### 2. **Setting Print Options:**
   ```python
   np.set_printoptions(legacy='1.13')
   ```
   - **`np.set_printoptions(...)`**: Configures how NumPy arrays are displayed when printed.
   - **`legacy='1.13'`**: Sets the printing options to be compatible with the display style of NumPy version 1.13. This might affect formatting, precision, and overall display of arrays when printed. This setting ensures that the output format is consistent with older versions of NumPy.

### 3. **Reading Input for Dimensions:**
   ```python
   N, M = map(int, input().split())
   ```
   - **`input()`**: Reads a line of input from the user as a string.
   - **`.split()`**: Splits the input string into a list of substrings based on whitespace. For example, if the input is `"3 4"`, it becomes `['3', '4']`.
   - **`map(int, ...)`**: Applies the `int` function to each substring to convert them into integers. This results in `map(int, ['3', '4'])`, which is equivalent to `[3, 4]`.
   - **`N, M = ...`**: Unpacks the list `[3, 4]` into two variables: `N` is assigned `3` (number of rows), and `M` is assigned `4` (number of columns).

### 4. **Creating and Printing the Identity Matrix:**
   ```python
   print(np.eye(N, M, k=0))
   ```
   - **`np.eye(N, M, k=0)`**: Creates a 2D identity matrix of shape `(N, M)` with the main diagonal at `k=0`.
     - **`N`**: Number of rows in the matrix.
     - **`M`**: Number of columns in the matrix.
     - **`k=0`**: Specifies the diagonal to place ones. The `k=0` option means the main diagonal (from top-left to bottom-right).
   - **`print(...)`**: Prints the created identity matrix.

### Examples:

**Example 1:**

1. **Input:**
   ```
   3 4
   ```
   - **`N`** = `3` (number of rows)
   - **`M`** = `4` (number of columns)

2. **Creating the Identity Matrix:**
   - **`np.eye(3, 4, k=0)`** creates a 3x4 matrix with ones on the main diagonal and zeros elsewhere:
     ```
     array([[1., 0., 0., 0.],
            [0., 1., 0., 0.],
            [0., 0., 1., 0.]])
     ```
   - Here, the matrix has 3 rows and 4 columns, with ones along the main diagonal.

**Example 2:**

1. **Input:**
   ```
   2 5
   ```
   - **`N`** = `2` (number of rows)
   - **`M`** = `5` (number of columns)

2. **Creating the Identity Matrix:**
   - **`np.eye(2, 5, k=0)`** creates a 2x5 matrix with ones on the main diagonal:
     ```
     array([[1., 0., 0., 0., 0.],
            [0., 1., 0., 0., 0.]])
     ```
   - This matrix has 2 rows and 5 columns, with ones placed along the main diagonal.

### Summary:
- The code reads dimensions for the identity matrix from user input, creates an identity matrix with those dimensions using NumPy's `np.eye` function, and prints the matrix. The `np.set_printoptions(legacy='1.13')` ensures the output format is consistent with older versions of NumPy.
