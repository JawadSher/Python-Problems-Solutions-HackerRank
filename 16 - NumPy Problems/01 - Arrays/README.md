<h1 align='center'>Arrays</h1>

## Problem Statement

**Problem URL :** [Arrays](https://www.hackerrank.com/challenges/np-arrays/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/a4e7307f-d85b-4219-a7b2-8c1587dbbbca)
![image](https://github.com/user-attachments/assets/fa16ff73-4c7b-4294-bad4-df1849878a08)

## Problem Solution
```py
import numpy

def arrays(arr):
    return numpy.array(arr, float)[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
```

## Problem Solution Explanation
Let's break down the code line by line:

### 1. **Importing the `numpy` module:**
   ```python
   import numpy
   ```
   - The `import numpy` statement imports the NumPy library, which is a powerful library for numerical computations in Python. It provides support for arrays, matrices, and many mathematical functions.

### 2. **Defining the `arrays` function:**
   ```python
   def arrays(arr):
       return numpy.array(arr, float)[::-1]
   ```
   - **`def arrays(arr):`**: This defines a function named `arrays` that takes one argument `arr`.
   - **`numpy.array(arr, float)`**: This converts the input list `arr` into a NumPy array of type `float`. 
     - The `float` argument ensures that all elements in the array are treated as floating-point numbers (decimals).
   - **`[::-1]`**: This is a slicing operation that reverses the array. The `[::-1]` syntax means "start from the end towards the first element, with a step of -1," effectively reversing the order of elements in the array.
   - **`return`**: The function returns the reversed NumPy array.

### 3. **Reading input:**
   ```python
   arr = input().strip().split(' ')
   ```
   - **`input()`**: This reads a line of input from the user as a string.
   - **`.strip()`**: This removes any leading or trailing whitespace (spaces, tabs, newlines) from the input string.
   - **`.split(' ')`**: This splits the string into a list of substrings wherever there is a space `' '`. For example, the input `'1 2 3'` will be split into the list `['1', '2', '3']`.

### 4. **Calling the `arrays` function:**
   ```python
   result = arrays(arr)
   ```
   - The `arrays(arr)` function is called with the list `arr` as the argument. 
   - The result of this function (which is the reversed NumPy array of floats) is stored in the variable `result`.

### 5. **Printing the result:**
   ```python
   print(result)
   ```
   - This prints the `result` (the reversed NumPy array) to the console.

### Example Input and Output:
- **Input**: `1 2 3 4 5`
  - After splitting: `['1', '2', '3', '4', '5']`
  - After converting to float array: `[1.0, 2.0, 3.0, 4.0, 5.0]`
  - After reversing: `[5.0, 4.0, 3.0, 2.0, 1.0]`
  - **Output**: `[5. 4. 3. 2. 1.]`

So, this code reads a space-separated string of numbers, converts them to a NumPy array of floats, reverses the array, and prints the result.
