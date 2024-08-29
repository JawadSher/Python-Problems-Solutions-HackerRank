<h1 align='center'>Shape and Reshape</h1>

## Problem Statement

**Problem URL :** [Shape and Reshape](https://www.hackerrank.com/challenges/np-shape-reshape/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/6e0e30c3-eff3-4e8f-9911-2d4263526b92)
![image](https://github.com/user-attachments/assets/77f39f62-08ce-45a1-bbb4-ccb9039daab8)

## Problem Solution
```py
import numpy as np

arr_elemnts = input().split()
x = np.array(arr_elemnts, int)
updated_arr = np.reshape(x, (3, 3))
print(updated_arr)
```

## Problem Solution Explanation
Let's go through the code step by step, explaining each line in detail:

### 1. **Importing the NumPy Library:**
   ```python
   import numpy as np
   ```
   - **`import numpy as np`**: This imports the NumPy library, a powerful library for numerical computations in Python, and assigns it the alias `np` to make it easier to call its functions. NumPy provides support for large multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.

### 2. **Reading Input and Splitting it into a List:**
   ```python
   arr_elemnts = input().split()
   ```
   - **`input()`**: This function reads a line of input from the user as a string. The input is typically given in a single line.
   - **`.split()`**: This method splits the input string into a list of substrings based on whitespace (spaces, tabs, etc.). By default, `.split()` splits on any whitespace and removes any extra spaces.
     - **Example**: If the input is `"1 2 3 4 5 6 7 8 9"`, then `arr_elemnts` will be `['1', '2', '3', '4', '5', '6', '7', '8', '9']`.

### 3. **Converting the List of Strings to a NumPy Array of Integers:**
   ```python
   x = np.array(arr_elemnts, int)
   ```
   - **`np.array(arr_elemnts, int)`**: This converts the list `arr_elemnts` into a NumPy array of integers.
     - The first argument is the list `arr_elemnts`.
     - The second argument `int` specifies that the elements should be converted to integers.
   - **Example**: If `arr_elemnts` is `['1', '2', '3', '4', '5', '6', '7', '8', '9']`, then `x` will be a NumPy array: `array([1, 2, 3, 4, 5, 6, 7, 8, 9])`.

### 4. **Reshaping the Array into a 3x3 Matrix:**
   ```python
   updated_arr = np.reshape(x, (3, 3))
   ```
   - **`np.reshape(x, (3, 3))`**: This reshapes the 1D NumPy array `x` into a 3x3 2D array (or matrix).
     - The first argument is the array `x`.
     - The second argument is a tuple `(3, 3)` that specifies the desired shape of the output array. Here, `(3, 3)` means 3 rows and 3 columns.
   - **Important Note**: The total number of elements must match the product of the new shape dimensions. In this case, `3 * 3 = 9`, which matches the number of elements in `x`.
   - **Example**: If `x` is `array([1, 2, 3, 4, 5, 6, 7, 8, 9])`, then `updated_arr` will be:
     ```
     array([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])
     ```

### 5. **Printing the Reshaped Array:**
   ```python
   print(updated_arr)
   ```
   - **`print(updated_arr)`**: This prints the reshaped 2D NumPy array to the console.
   - **Example Output**:
     ```
     [[1 2 3]
      [4 5 6]
      [7 8 9]]
     ```

### Summary of an Example Input/Output:
- **Input**: `1 2 3 4 5 6 7 8 9`
- **Steps**:
  1. The input string is split into a list of strings: `['1', '2', '3', '4', '5', '6', '7', '8', '9']`.
  2. The list is converted to a NumPy array of integers: `array([1, 2, 3, 4, 5, 6, 7, 8, 9])`.
  3. The 1D array is reshaped into a 3x3 2D array:
     ```
     [[1 2 3]
      [4 5 6]
      [7 8 9]]
     ```
  4. The reshaped array is printed.

This process transforms a list of integers into a 2D matrix, which can be particularly useful in various numerical and data processing tasks.
