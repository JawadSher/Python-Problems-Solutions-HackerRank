<h1 align='center'>Inner - and - Outer</h1>

## Problem Statement

**Problem URL :** [Inner and Outer](https://www.hackerrank.com/challenges/np-inner-and-outer/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/3d1748eb-687d-4913-a971-a45fe25b0529)
![image](https://github.com/user-attachments/assets/d06e0c5f-26a8-4d10-b493-52ecd0e80c46)

## Problem Solution
```py
import numpy as np

arr_A = np.array(input().split(), int)
arr_B = np.array(input().split(), int)

print(np.inner(arr_A, arr_B))
print(np.outer(arr_A, arr_B))
```

## Problem Solution Explanation

Let’s go through the code line by line, and then I’ll provide a detailed example to illustrate how it works.

```python
import numpy as np
```
- **`import numpy as np`**: Imports the NumPy library and assigns it the alias `np`.

```python
arr_A = np.array(input().split(), int)
```
- **`input().split()`**: Reads a line of input and splits it into a list of strings based on whitespace.
- **`np.array(..., int)`**: Converts this list of strings to a NumPy array of integers. The `int` argument specifies that the array should be of integer type.

```python
arr_B = np.array(input().split(), int)
```
- This line does the same as the previous one but for the second array `arr_B`.

```python
print(np.inner(arr_A, arr_B))
```
- **`np.inner(arr_A, arr_B)`**: Computes the inner product (dot product) of the two arrays `arr_A` and `arr_B`. For 1-D arrays, this is the sum of the products of the corresponding elements.

```python
print(np.outer(arr_A, arr_B))
```
- **`np.outer(arr_A, arr_B)`**: Computes the outer product of the two arrays. For 1-D arrays, this is a matrix where each element is the product of the elements from `arr_A` and `arr_B`.

### Example

Let’s use an example to illustrate how the code works. Assume the input is:

```
1 2 3
4 5 6
```

**1. Reading the Arrays:**

```python
arr_A = np.array(input().split(), int)
arr_B = np.array(input().split(), int)
```

- **Input for `arr_A`:** `1 2 3`
  - **`arr_A`** will be:
    ```python
    np.array([1, 2, 3])
    ```

- **Input for `arr_B`:** `4 5 6`
  - **`arr_B`** will be:
    ```python
    np.array([4, 5, 6])
    ```

**2. Calculating the Inner Product:**

```python
print(np.inner(arr_A, arr_B))
```

- **`np.inner(arr_A, arr_B)`** computes the dot product of `arr_A` and `arr_B`:
  - Formula: `1*4 + 2*5 + 3*6`
  - Calculation: `4 + 10 + 18 = 32`
  - **Output:**
    ```python
    32
    ```

**3. Calculating the Outer Product:**

```python
print(np.outer(arr_A, arr_B))
```

- **`np.outer(arr_A, arr_B)`** computes the outer product of `arr_A` and `arr_B`:
  - It creates a 2D matrix where each element `(i, j)` is the product of `arr_A[i]` and `arr_B[j]`.
  - Matrix Calculation:
    - For `i=0` (first row of `arr_A`): `[1*4, 1*5, 1*6]` -> `[4, 5, 6]`
    - For `i=1` (second row of `arr_A`): `[2*4, 2*5, 2*6]` -> `[8, 10, 12]`
    - For `i=2` (third row of `arr_A`): `[3*4, 3*5, 3*6]` -> `[12, 15, 18]`
  - **Output:**
    ```python
    [[ 4  5  6]
     [ 8 10 12]
     [12 15 18]]
    ```

### Summary

Given the inputs:

```
1 2 3
4 5 6
```

The code produces:

- **Inner Product:**
  ```
  32
  ```

- **Outer Product:**
  ```
  [[ 4  5  6]
   [ 8 10 12]
   [12 15 18]]
  ```

The inner product is a single number representing the sum of the products of corresponding elements, while the outer product is a matrix where each element is the product of every pair of elements from the two input arrays.
