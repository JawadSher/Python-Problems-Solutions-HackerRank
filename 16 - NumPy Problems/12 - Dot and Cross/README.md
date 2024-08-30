<h1 align='center'>Dot - and - Cross</h1>

## Problem Statement

**Problem URL :** [Dot and Cross](https://www.hackerrank.com/challenges/np-dot-and-cross/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/38bd9a7f-0a7a-43a6-b222-9eb524f1c05e)
![image](https://github.com/user-attachments/assets/a1fd0c9e-6e90-4437-a0a0-6f5a4e4ca6ae)

## Problem Solution
```py
import numpy as np
from numpy import matmul

N = int(input().strip())

np_arrA = np.array([[*map(int, input().split())] for _ in range(N)])
np_arrB = np.array([[*map(int, input().split())] for _ in range(N)])

result = matmul(np_arrA, np_arrB)
print(result)
```

## Problem Solution Explanation

Let's break down the code for matrix multiplication using NumPy, line by line, and explain it with an example.

```python
import numpy as np
from numpy import matmul

N = int(input().strip())
```

1. **Importing Libraries:**
   ```python
   import numpy as np
   from numpy import matmul
   ```
   - `numpy` is imported as `np` to handle numerical operations.
   - `matmul` function is imported from `numpy` to perform matrix multiplication.

2. **Reading the Size of the Matrices:**
   ```python
   N = int(input().strip())
   ```
   - Reads an integer `N` from the input which represents the size of the NxN matrices.
   - `.strip()` removes any extra whitespace from the input.

```python
np_arrA = np.array([[*map(int, input().split())] for _ in range(N)])
```

3. **Creating the First Matrix (`np_arrA`):**
   ```python
   np_arrA = np.array([[*map(int, input().split())] for _ in range(N)])
   ```
   - This line reads `N` lines of input, each containing `N` integers.
   - `input().split()` splits the input line into a list of strings.
   - `map(int, ...)` converts these strings to integers.
   - `[... for _ in range(N)]` creates a list of lists, where each inner list is a row of the matrix.
   - `np.array(...)` converts this list of lists into a NumPy array representing matrix `A`.

```python
np_arrB = np.array([[*map(int, input().split())] for _ in range(N)])
```

4. **Creating the Second Matrix (`np_arrB`):**
   - This line is similar to the previous one but for the second matrix.
   - It reads `N` lines of input, each containing `N` integers for matrix `B`.
   - Constructs the NumPy array `np_arrB` in the same way as `np_arrA`.

```python
result = matmul(np_arrA, np_arrB)
```

5. **Performing Matrix Multiplication:**
   ```python
   result = matmul(np_arrA, np_arrB)
   ```
   - `matmul(np_arrA, np_arrB)` computes the matrix product of `np_arrA` and `np_arrB`.
   - `matmul` is a function for matrix multiplication that follows the rules of linear algebra: for matrices `A` and `B`, the element at position `(i, j)` in the resulting matrix is computed as the dot product of the `i`-th row of `A` and the `j`-th column of `B`.

```python
print(result)
```

6. **Printing the Result:**
   ```python
   print(result)
   ```
   - Prints the resulting matrix from the multiplication.

### Example

Consider the following input:

```
2
1 2
3 4
5 6
7 8
```

- `N = 2`
- Matrix `A` (np_arrA):
  ```
  1 2
  3 4
  ```
- Matrix `B` (np_arrB):
  ```
  5 6
  7 8
  ```

**Matrix Multiplication:**

To compute the product of matrices `A` and `B`, we perform the following calculations:

- **Element (0,0):**
  \[
  (1 \times 5) + (2 \times 7) = 5 + 14 = 19
  \]
- **Element (0,1):**
  \[
  (1 \times 6) + (2 \times 8) = 6 + 16 = 22
  \]
- **Element (1,0):**
  \[
  (3 \times 5) + (4 \times 7) = 15 + 28 = 43
  \]
- **Element (1,1):**
  \[
  (3 \times 6) + (4 \times 8) = 18 + 32 = 50
  \]

The resulting matrix from multiplying `A` and `B` is:

```
[[19 22]
 [43 50]]
```

### Complete Example Output

For the input:

```
2
1 2
3 4
5 6
7 8
```

The output will be:

```
[[19 22]
 [43 50]]
```
