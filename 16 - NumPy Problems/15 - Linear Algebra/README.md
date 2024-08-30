<h1 align='center'>Linear - Algebra</h1>

## Problem Statement

**Problem URL :** [Linear Algebra](https://www.hackerrank.com/challenges/np-linear-algebra/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/de93d101-172b-46e2-9312-b75b825f2aa0)
![image](https://github.com/user-attachments/assets/b7d4d5cd-9c4e-4ddc-ac37-d72bd2cc155f)

## Problem Solution
```py
import numpy as np

N = int(input().strip())
arr_A = [list(map(float, input().split())) for _ in range(N)]

print(round(np.linalg.det(arr_A), 3))
```

## Problem Solution Explanation
Let's go through the code step by step, explaining each part in detail with examples.

#### 1. `import numpy as np`
This line imports the NumPy library, which is widely used in Python for numerical computations, especially for operations involving arrays and matrices. By importing it as `np`, we can use a shorter alias to access its functions.

#### 2. `N = int(input().strip())`
This line does the following:

- **`input()`**: Reads a line of input from the user as a string.
  
- **`.strip()`**: Removes any leading or trailing whitespace from the input string. This ensures that if the user accidentally adds spaces before or after the number, they are removed before processing.

- **`int(...)`**: Converts the stripped string input into an integer.

This integer `N` represents the size of a square matrix, i.e., the number of rows (and columns) in the matrix.

**Example**:  
If the user input is `"3"`, then:
- `input()` reads `"3"`.
- `.strip()` removes any whitespace, so the string remains `"3"`.
- `int(...)` converts it to `3`, so `N = 3`.

This means we are going to work with a 3x3 matrix.

#### 3. `arr_A = [list(map(float, input().split())) for _ in range(N)]`
This line constructs a 2D list `arr_A`, which represents a square matrix of size `N x N`. Here's what happens:

- **`input().split()`**: For each row of the matrix, this part reads a line of input as a string and splits it into a list of substrings (based on whitespace). For example, if the input is `"1.0 2.0 3.0"`, `split()` converts it to `['1.0', '2.0', '3.0']`.

- **`map(float, ...)`**: The `map()` function applies the `float` function to each element of the list of strings. This converts the list of strings into a list of floating-point numbers. For example, `['1.0', '2.0', '3.0']` becomes `[1.0, 2.0, 3.0]`.

- **`list(...)`**: Converts the map object into a list.

- **`for _ in range(N)`**: This is a list comprehension that repeats the above steps `N` times to read `N` rows from the user and convert them into a 2D list (a list of lists). Each inner list represents a row of the matrix.

**Example**:  
If `N = 3`, and the user inputs:
```
1.0 2.0 3.0
4.0 5.0 6.0
7.0 8.0 9.0
```
Then:
- The first iteration reads `"1.0 2.0 3.0"` and converts it to `[1.0, 2.0, 3.0]`.
- The second iteration reads `"4.0 5.0 6.0"` and converts it to `[4.0, 5.0, 6.0]`.
- The third iteration reads `"7.0 8.0 9.0"` and converts it to `[7.0, 8.0, 9.0]`.

So, `arr_A` will be:
```python
arr_A = [
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0]
]
```

#### 4. `print(round(np.linalg.det(arr_A), 3))`
This line computes the determinant of the matrix `arr_A` and prints it rounded to three decimal places.

- **`np.linalg.det(arr_A)`**: The `np.linalg.det` function from the NumPy library calculates the determinant of a square matrix `arr_A`.

- **`round(..., 3)`**: The `round` function rounds the determinant value to three decimal places.

- **`print(...)`**: Finally, the rounded determinant value is printed.

**Example**:  
For the matrix:
```python
arr_A = [
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0]
]
```
The determinant is computed as:
```
det(arr_A) = 1.0*(5.0*9.0 - 6.0*8.0) - 2.0*(4.0*9.0 - 6.0*7.0) + 3.0*(4.0*8.0 - 5.0*7.0)
           = 1.0*(45.0 - 48.0) - 2.0*(36.0 - 42.0) + 3.0*(32.0 - 35.0)
           = 1.0*(-3.0) - 2.0*(-6.0) + 3.0*(-3.0)
           = -3.0 + 12.0 - 9.0
           = 0.0
```
So, the determinant is `0.0`.

**Final Output**:  
Since the determinant is `0.0`, rounding it to three decimal places will still give `0.0`, and the output will be:
```
0.0
```

This means the matrix is singular (non-invertible), as it has a determinant of zero.
