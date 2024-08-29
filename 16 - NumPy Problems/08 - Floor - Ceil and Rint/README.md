<h1 align='center'>Floor - Ceil - and - Rint</h1>

## Problem Statement

**Problem URL :** [Floor - Ceil and Rint](https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/e803ad2b-588d-4c0c-8bee-aeb1d38cb50a)
![image](https://github.com/user-attachments/assets/8ea26e43-805e-436b-a37f-df9dab11b7b2)

## Problem Solution
```py
import numpy as np
np.set_printoptions(legacy='1.13')

np_array = np.array(input().split(), float)

print(np.floor(np_array), np.ceil(np_array), np.rint(np_array), sep="\n")
```

## Problem Solution Explanation
Let's go through the code line by line, explaining each part in detail with examples.


```python
import numpy as np
```
- **Importing NumPy**: This line imports the NumPy library, which is used for numerical computations in Python, particularly for working with arrays and performing mathematical operations efficiently.



```python
np.set_printoptions(legacy='1.13')
```
- **Setting Print Options**: 
  - This line configures how NumPy arrays will be printed.
  - The `legacy='1.13'` option ensures that the array elements are displayed in the same format as they would be in NumPy version 1.13. This typically means that the formatting will be more compact and may include less precision in the printed output.



```python
np_array = np.array(input().split(), float)
```
- **Creating a NumPy Array**:
  - `input().split()` reads a line of input, splits it into a list of strings based on spaces.
  - `np.array(..., float)` converts this list of strings into a NumPy array of floats.
  
**Example:**
- Input: `3.7 1.2 5.9`
- Output: 
  - `np_array` will be `array([3.7, 1.2, 5.9])` as a NumPy array of floats.



```python
print(np.floor(np_array), np.ceil(np_array), np.rint(np_array), sep="\n")
```
- **Performing Operations and Printing**:
  - This line performs three different operations on the array `np_array` and prints the results, each on a new line (`sep="\n"`).

### Detailed Explanation of Operations:

1. **`np.floor(np_array)`**:
   - **Operation**: Computes the floor of each element in the array. The floor of a number is the largest integer less than or equal to that number.
   - **Example**:
     - For `np_array = [3.7, 1.2, 5.9]`, the result will be `[3.0, 1.0, 5.0]`.

2. **`np.ceil(np_array)`**:
   - **Operation**: Computes the ceiling of each element in the array. The ceiling of a number is the smallest integer greater than or equal to that number.
   - **Example**:
     - For `np_array = [3.7, 1.2, 5.9]`, the result will be `[4.0, 2.0, 6.0]`.

3. **`np.rint(np_array)`**:
   - **Operation**: Rounds each element in the array to the nearest integer. If the fractional part of the number is exactly 0.5, it rounds to the nearest even integer.
   - **Example**:
     - For `np_array = [3.7, 1.2, 5.9]`, the result will be `[4.0, 1.0, 6.0]`.

**Final Output**:
- If the input was `3.7 1.2 5.9`, the printed output would be:
  ```
  [ 3.  1.  5.]
  [ 4.  2.  6.]
  [ 4.  1.  6.]
  ```

### Summary
- **Floor**: Rounds each element down to the nearest integer.
- **Ceil**: Rounds each element up to the nearest integer.
- **Rint**: Rounds each element to the nearest integer, with ties going to the nearest even integer.
