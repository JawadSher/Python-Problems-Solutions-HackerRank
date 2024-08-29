<h1 align='center'>Array - Mathematics</h1>

## Problem Statement

**Problem URL :** [Array - Mathematics](https://www.hackerrank.com/challenges/np-array-mathematics/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/41140fa5-9362-499b-af37-b200c8c9e067)
![image](https://github.com/user-attachments/assets/0995fc3f-44e1-4abf-a0ad-1a49df6d933a)

## Problem Solution
```py
import numpy as np

N, M = map(int, input().split())

np_array_A = np.array([[*map(int, input().split())] for _ in range(N)])
np_array_B = np.array([[*map(int, input().split())] for _ in range(N)])

print(np.add(np_array_A, np_array_B))
print(np.subtract(np_array_A, np_array_B))
print(np.multiply(np_array_A, np_array_B))
print(np.floor_divide(np_array_A, np_array_B))
print(np.mod(np_array_A, np_array_B))
print(np.power(np_array_A, np_array_B))
```

## Problem Solution Explanation
Let's go through the code line by line, explaining each part in detail with an example.

```python
import numpy as np
```
- **Importing NumPy**: This line imports the NumPy library, which is a powerful tool for numerical computations in Python, especially for working with arrays and matrices.


```python
N, M = map(int, input().split())
```
- **Input Dimensions**: 
  - This line takes a single input line from the user, splits it into two parts, and converts them to integers using `map(int, input().split())`.
  - `N` represents the number of rows, and `M` represents the number of columns for the arrays.

**Example:**
- Input: `2 3`
- Output: `N = 2`, `M = 3`


```python
np_array_A = np.array([[*map(int, input().split())] for _ in range(N)])
np_array_B = np.array([[*map(int, input().split())] for _ in range(N)])
```
- **Creating the Arrays**:
  - These two lines create the arrays `np_array_A` and `np_array_B` using list comprehensions.
  - For each row (from `0` to `N-1`), the code takes a line of input, splits it into integers, and stores it as a list. This process is repeated `N` times to create a 2D list (list of lists), which is then converted into a NumPy array using `np.array()`.

**Example:**
- Let's say the input is as follows:
  ```
  1 2 3
  4 5 6
  ```
  - This will generate:
    ```python
    np_array_A = np.array([[1, 2, 3], [4, 5, 6]])
    ```
  - If the next input is:
    ```
    7 8 9
    10 11 12
    ```
    - This will generate:
      ```python
      np_array_B = np.array([[7, 8, 9], [10, 11, 12]])
      ```


```python
print(np.add(np_array_A, np_array_B))
```
- **Element-wise Addition**:
  - `np.add(np_array_A, np_array_B)` performs element-wise addition of the two arrays.

**Example:**
- If `np_array_A = [[1, 2, 3], [4, 5, 6]]` and `np_array_B = [[7, 8, 9], [10, 11, 12]]`,
  - The result will be:
    ```python
    [[ 8 10 12]
     [14 16 18]]
    ```


```python
print(np.subtract(np_array_A, np_array_B))
```
- **Element-wise Subtraction**:
  - `np.subtract(np_array_A, np_array_B)` performs element-wise subtraction of the two arrays.

**Example:**
- Using the same arrays as above:
  - The result will be:
    ```python
    [[-6 -6 -6]
     [-6 -6 -6]]
    ```


```python
print(np.multiply(np_array_A, np_array_B))
```
- **Element-wise Multiplication**:
  - `np.multiply(np_array_A, np_array_B)` performs element-wise multiplication of the two arrays.

**Example:**
- Using the same arrays as above:
  - The result will be:
    ```python
    [[ 7 16 27]
     [40 55 72]]
    ```


```python
print(np.floor_divide(np_array_A, np_array_B))
```
- **Element-wise Floor Division**:
  - `np.floor_divide(np_array_A, np_array_B)` performs element-wise integer (floor) division of the two arrays. This division rounds down to the nearest integer.

**Example:**
- Using the same arrays:
  - The result will be:
    ```python
    [[0 0 0]
     [0 0 0]]
    ```


```python
print(np.mod(np_array_A, np_array_B))
```
- **Element-wise Modulus**:
  - `np.mod(np_array_A, np_array_B)` calculates the modulus (remainder) of element-wise division.

**Example:**
- Using the same arrays:
  - The result will be:
    ```python
    [[1 2 3]
     [4 5 6]]
    ```

```python
print(np.power(np_array_A, np_array_B))
```
- **Element-wise Exponentiation**:
  - `np.power(np_array_A, np_array_B)` raises each element in `np_array_A` to the power of the corresponding element in `np_array_B`.

**Example:**
- Using the same arrays:
  - The result will be:
    ```python
    [[      1     256  19683]
     [1048576  48828125 2176782336]]
    ```

### Summary
- **Array Operations**: The code performs a variety of element-wise operations on two NumPy arrays, including addition, subtraction, multiplication, floor division, modulus, and exponentiation.
- **Handling Edge Cases**: The floor division and modulus operations may require special attention if `np_array_B` contains zeros, as dividing by zero will raise an error.
