<h1 align='center'>Mean - Var - and - Std</h1>

## Problem Statement

**Problem URL :** [Mean, Var and Std](https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/a6dee4d7-6d32-4e35-9419-5e706945ad68)
![image](https://github.com/user-attachments/assets/e1701a3a-fd7c-4a72-b8e9-5c2f004c71ca)
![image](https://github.com/user-attachments/assets/3653265e-bcc5-4500-aa84-95e0a8201870)

## Problem Solution
```py
import numpy as np

N, M = map(int, input().split())

np_array = np.array([[*map(int, input().split())] for i in range(N)])

mean_values = np.mean(np_array, axis=1)
var_values = np.var(np_array, axis=0)
std_value = np.std(np_array, axis=None)

print(mean_values)
print(var_values)
print(round(std_value, 11))
```

## Problem Solution Explanation
Let's break down the code and explain the process step-by-step, using an example.


1. **Importing Libraries:**
   ```python
   import numpy as np
   ```
   - `numpy` is imported to handle array operations efficiently.

2. **Reading Input:**
   ```python
   N, M = map(int, input().split())
   ```
   - This reads two integers from the input: `N` (number of rows) and `M` (number of columns).

3. **Creating the NumPy Array:**
   ```python
   np_array = np.array([[*map(int, input().split())] for i in range(N)])
   ```
   - This creates a 2D NumPy array.
   - For each row (`N` rows in total), it reads a line of space-separated integers, converts them to integers, and forms a list.
   - These lists are then combined into a 2D NumPy array.

4. **Calculating Mean Values:**
   ```python
   mean_values = np.mean(np_array, axis=1)
   ```
   - Computes the mean of each row (across columns).
   - `axis=1` specifies that the mean should be calculated along the columns for each row.

5. **Calculating Variance Values:**
   ```python
   var_values = np.var(np_array, axis=0)
   ```
   - Computes the variance for each column.
   - `axis=0` specifies that the variance should be calculated along the rows for each column.

6. **Calculating Standard Deviation:**
   ```python
   std_value = np.std(np_array, axis=None)
   ```
   - Computes the standard deviation of all elements in the array.
   - `axis=None` specifies that the standard deviation is calculated over the entire array.

7. **Printing Results:**
   ```python
   print(mean_values)
   print(var_values)
   print(round(std_value, 11))
   ```
   - Prints the mean values (one value per line for each row).
   - Prints the variance values (one value per line for each column).
   - Prints the standard deviation rounded to 11 decimal places.

### Example

Let's use the example input:

```
2 2
1 2
3 4
```

- `N = 2`, `M = 2`
- The 2D NumPy array will be:
  ```
  [[1, 2],
   [3, 4]]
  ```

**Calculations:**

1. **Mean Values (per row):**
   - For the first row `[1, 2]`, mean = `(1 + 2) / 2 = 1.5`
   - For the second row `[3, 4]`, mean = `(3 + 4) / 2 = 3.5`
   - Result: `[1.5, 3.5]`

2. **Variance Values (per column):**
   - For the first column `[1, 3]`, variance = `[(1-2)^2 + (3-2)^2] / 2 = [1 + 1] / 2 = 1.0`
   - For the second column `[2, 4]`, variance = `[(2-3)^2 + (4-3)^2] / 2 = [1 + 1] / 2 = 1.0`
   - Result: `[1.0, 1.0]`

3. **Standard Deviation:**
   - All elements combined: `[1, 2, 3, 4]`
   - Mean of all elements = `(1 + 2 + 3 + 4) / 4 = 2.5`
   - Variance = `[(1-2.5)^2 + (2-2.5)^2 + (3-2.5)^2 + (4-2.5)^2] / 4`
     = `[2.25 + 0.25 + 0.25 + 2.25] / 4`
     = `5 / 4 = 1.25`
   - Standard deviation = `sqrt(1.25) ≈ 1.118033988749895`
   - Result: `1.11803398875` (rounded to 11 decimal places)

### Output

Given the example input, the code will produce:

```
[1.5 3.5]
[1. 1.]
1.11803398875
```

This output matches the expected results for mean values, variance values, and standard deviation, respectively.
