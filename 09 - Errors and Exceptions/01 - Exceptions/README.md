<h1 align='center'>Exceptions</h1>

## Problem Statement

**Problem URL :** [Exceptions](https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/c1a59e40-1e19-4473-94b6-9598c7548f54)
![image](https://github.com/user-attachments/assets/970cc971-e0b3-494f-ae83-14a5e5fa6e2c)
![image](https://github.com/user-attachments/assets/d4581e04-fad9-4fc3-88af-0d2314ea2e2c)

## Problem Solution
```py
test_cases = int(input().strip())

for _ in range(test_cases):
    input_values = input().split()
    result = 0
    try:
        n1 = input_values[0]
        n2 = input_values[1]
        result = (int(n1) // int(n2))
        print(result)
    except (ZeroDivisionError, ValueError) as e:
        print(f"Error Code: {e}")
```

## Problem Solution Explanation

Let's break down the code step by step to help beginners understand how it works. This code is designed to handle multiple test cases, each involving the division of two numbers. It also handles specific errors that might occur during the process.

### 1. Reading the Number of Test Cases
```python
test_cases = int(input().strip())
```
- **Explanation**: 
  - The `input()` function reads a line of input from the user.
  - The `strip()` method removes any leading and trailing spaces from the input string.
  - The `int()` function converts the cleaned input string into an integer. This integer represents the number of test cases the program will handle.

### 2. Looping Through Each Test Case
```python
for _ in range(test_cases):
```
- **Explanation**: 
  - This is a `for` loop that iterates `test_cases` number of times.
  - The `_` is used as a loop variable. It’s a common convention to use `_` when the variable’s value is not needed within the loop.

### 3. Reading Input Values
```python
    input_values = input().split()
```
- **Explanation**:
  - The `input()` function reads a line of input from the user. This line is expected to contain two numbers separated by a space.
  - The `split()` method splits the input string into a list of substrings based on spaces. For example, if the input is `"10 2"`, `input_values` will become `['10', '2']`.

### 4. Initializing the Result
```python
    result = 0
```
- **Explanation**:
  - A variable `result` is initialized to `0`. This variable will store the result of the division.

### 5. Performing the Division and Handling Errors
```python
    try:
        n1 = input_values[0]
        n2 = input_values[1]
        result = (int(n1) // int(n2))
        print(result)
```
- **Explanation**:
  - **Try Block**: The code within the `try` block is where the main operation is performed. If an error occurs, the code execution will jump to the `except` block.
  - `n1 = input_values[0]`: The first value from `input_values` (e.g., `'10'`) is stored in the variable `n1`.
  - `n2 = input_values[1]`: The second value from `input_values` (e.g., `'2'`) is stored in the variable `n2`.
  - `result = (int(n1) // int(n2))`: The program converts `n1` and `n2` from strings to integers using `int()`. It then performs integer division using the `//` operator and stores the result in `result`.
  - `print(result)`: The result of the division is printed to the console.

### 6. Handling Errors
```python
    except (ZeroDivisionError, ValueError) as e:
        print(f"Error Code: {e}")
```
- **Explanation**:
  - **Except Block**: If an error occurs during the execution of the `try` block, the program jumps to the `except` block.
  - The `except` block here is designed to catch two types of errors:
    1. **ZeroDivisionError**: This error occurs if `n2` is `0`, because division by zero is undefined in mathematics and illegal in most programming languages.
    2. **ValueError**: This error occurs if the input cannot be converted to an integer, such as if the input was `'a'` instead of a number.
  - `as e`: This part captures the error message and stores it in the variable `e`.
  - `print(f"Error Code: {e}")`: The program prints a message that includes the type of error that occurred. For example, if the user tried to divide by zero, it might print something like `Error Code: division by zero`.

### Summary
This code is designed to handle multiple division operations, printing the result of each or an appropriate error message if something goes wrong. It ensures that the program does not crash when encountering common issues like dividing by zero or non-numeric input. This makes the code more robust and user-friendly.
