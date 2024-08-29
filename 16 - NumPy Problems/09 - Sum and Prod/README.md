<h1 align='center'>Sum - and - Prod</h1>

## Problem Statement

**Problem URL :** [Sum and Prod](https://www.hackerrank.com/challenges/np-sum-and-prod/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/5c9bb952-729b-4315-bb02-68b4a2c86b28)
![image](https://github.com/user-attachments/assets/68222b40-b01b-409f-9e66-1963aab57b77)

## Problem Solution
```py
import numpy as np

N, M = map(int, input().split())

np_array = np.array([[*map(int, input().split())] for _ in range(N)])

sum_array = np.sum(np_array, axis=0)
prod_array = np.prod(sum_array, axis=0)
print(prod_array)
```

## Problem Solution Explanation
Let's go through the code step by step, explaining each part in detail with examples.

```python
import numpy as np
```
- **Importing NumPy**: This line imports the NumPy library, which provides support for arrays, matrices, and many mathematical functions.



```python
N, M = map(int, input().split())
```
- **Reading Input Values**:
  - `input().split()` reads a line of input, splits it into a list of strings based on spaces.
  - `map(int, ...)` converts each of these strings into an integer.
  - `N` will be the number of rows, and `M` will be the number of columns in the 2D array.

**Example:**
- Input: `3 2`
  - `N` = 3 (rows)
  - `M` = 2 (columns)



```python
np_array = np.array([[*map(int, input().split())] for _ in range(N)])
```
- **Creating a 2D NumPy Array**:
  - `input().split()` inside the list comprehension reads a line of input, splits it into a list of strings.
  - `map(int, ...)` converts these strings into integers.
  - `[*map(int, ...)]` creates a list of these integers (i.e., a row in the 2D array).
  - The list comprehension `for _ in range(N)` repeats this process `N` times, resulting in a list of `N` rows, each containing `M` integers.
  - `np.array(...)` converts this list of lists into a NumPy 2D array.

**Example:**
- Input:
  ```
  1 2
  3 4
  5 6
  ```
- `np_array` will be:
  ```
  array([[1, 2],
         [3, 4],
         [5, 6]])
  ```



```python
sum_array = np.sum(np_array, axis=0)
```
- **Calculating the Sum Along Columns**:
  - `np.sum(np_array, axis=0)` calculates the sum of elements along the specified axis. Here, `axis=0` means summing across the rows for each column.
  - The result is a 1D array containing the sum of each column.

**Example:**
- For `np_array`:
  ```
  array([[1, 2],
         [3, 4],
         [5, 6]])
  ```
- `sum_array` will be:
  ```
  array([9, 12])
  ```
  - Column sums: `[1+3+5, 2+4+6]` = `[9, 12]`


```python
prod_array = np.prod(sum_array, axis=0)
```
- **Calculating the Product of the Sum Array**:
  - `np.prod(sum_array, axis=0)` calculates the product of all elements in `sum_array`. Since `sum_array` is 1D, the product is calculated over the entire array.
  - The result is a single integer value, which is the product of the sums of each column.

**Example:**
- For `sum_array = array([9, 12])`:
  - `prod_array` will be `9 * 12 = 108`.



```python
print(prod_array)
```
- **Printing the Final Result**:
  - This line prints the value of `prod_array`.

**Example**:
- For the input:
  ```
  3 2
  1 2
  3 4
  5 6
  ```
- The output will be:
  ```
  108
  ```

### Summary:
- **Input**: You input `N` (rows) and `M` (columns), followed by `N` lines of `M` integers each.
- **2D Array Creation**: A 2D NumPy array is created from the input.
- **Column Sum**: The sum of elements in each column is calculated.
- **Product of Sums**: The product of these column sums is computed and printed.
