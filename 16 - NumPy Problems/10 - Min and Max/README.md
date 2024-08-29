<h1 align='center'>Min - and - Max</h1>

## Problem Statement

**Problem URL :** [Min and Max](https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/795216df-c7cd-41c2-88c5-c9e213e55907)
![image](https://github.com/user-attachments/assets/aa09d6a0-a44e-45e2-aebe-7459a6a2bdb0)

## Problem Solution
```py
import numpy as np

N, M = map(int, input().split())
np_array = np.array([[*map(int, input().split())] for _ in range(N)])

min_num = np.min(np_array, axis=1)
max_num = np.max(min_num)
print(max_num)
```

## Problem Solution Explanation
Let's break down the code step by step, explaining each part in detail with examples.

```python
import numpy as np
```
- **Importing NumPy**: This line imports the NumPy library, which is used for working with arrays and performing mathematical operations.

---

```python
N, M = map(int, input().split())
```
- **Reading Input Values**:
  - `input().split()` reads a line of input, splits it into a list of strings based on spaces.
  - `map(int, ...)` converts each of these strings into an integer.
  - `N` will be the number of rows, and `M` will be the number of columns in the 2D array.

**Example:**
- Input: `3 3`
  - `N` = 3 (rows)
  - `M` = 3 (columns)

---

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
  1 2 3
  4 5 6
  7 8 9
  ```
- `np_array` will be:
  ```python
  array([[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]])
  ```

---

```python
min_num = np.min(np_array, axis=1)
```
- **Finding the Minimum Value in Each Row**:
  - `np.min(np_array, axis=1)` calculates the minimum value for each row of the 2D array.
  - The `axis=1` argument specifies that the operation should be performed along the columns, resulting in a 1D array where each element is the minimum value from the corresponding row.

**Example:**
- For `np_array`:
  ```python
  array([[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]])
  ```
- `min_num` will be:
  ```python
  array([1, 4, 7])
  ```
  - These values represent the minimum of each row: `[min(1, 2, 3), min(4, 5, 6), min(7, 8, 9)]` = `[1, 4, 7]`.

---

```python
max_num = np.max(min_num)
```
- **Finding the Maximum Value Among the Row Minimums**:
  - `np.max(min_num)` calculates the maximum value from the `min_num` array.
  - Since `min_num` is a 1D array containing the minimum value from each row, `np.max(min_num)` finds the largest of these minimum values.

**Example:**
- For `min_num = array([1, 4, 7])`:
  - `max_num` will be `7`, which is the maximum value among `[1, 4, 7]`.

---

```python
print(max_num)
```
- **Printing the Final Result**:
  - This line prints the value of `max_num`.

**Example:**
- For the input:
  ```
  3 3
  1 2 3
  4 5 6
  7 8 9
  ```
- The output will be:
  ```
  7
  ```

### Summary:
- **Input**: You input `N` (rows) and `M` (columns), followed by `N` lines of `M` integers each.
- **2D Array Creation**: A 2D NumPy array is created from the input.
- **Row Minimums**: The minimum value in each row is found.
- **Maximum of Row Minimums**: The maximum value among these row minimums is calculated and printed.

This process can be particularly useful when solving problems where you need to find the "least worst" option or the "maximum of the minimums."
