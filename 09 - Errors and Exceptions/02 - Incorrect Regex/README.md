<h1 align='center'>Incorrect - Regex</h1>

## Problem Statement

**Problem URL :** [Incorrect Regex](https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/e49de0af-1a1e-4086-ba81-39897e20e48c)

## Problem Solution
```py
import re

num_tests = int(input().strip())

for _ in range(num_tests):
    expression = input().strip()
    invalid = False
    
    for sign in ["+", "*", "?"]:
        if sign + "+" in expression:
            invalid = True
            break
    if invalid:
        print("False")
    else:
        try:
            re.compile(expression)
            print("True")
        except re.error:
            print("False")
```

## Problem Solution Explanation

Let's break down the code step by step to help beginners understand how it works.

#### 1. Importing the `re` Module
```python
import re
```
- **Purpose**: The `re` module provides support for working with regular expressions in Python. We use it to compile and validate regex patterns.

#### 2. Reading the Number of Test Cases
```python
num_tests = int(input().strip())
```
- **Purpose**: This line reads the number of test cases (i.e., how many regex patterns we want to check). 
- **Explanation**:
  - `input()` reads a line of input from the user.
  - `.strip()` removes any leading or trailing whitespace.
  - `int()` converts the input from a string to an integer.

#### 3. Looping Through Each Test Case
```python
for _ in range(num_tests):
```
- **Purpose**: This loop runs once for each test case. If `num_tests` is 3, the loop will run 3 times.
- **Explanation**:
  - `_` is a common variable name used in loops when the variable itself is not needed.

#### 4. Reading the Regular Expression
```python
expression = input().strip()
```
- **Purpose**: This line reads the regular expression pattern from the user.
- **Explanation**:
  - `input()` reads the user input.
  - `.strip()` removes any leading or trailing whitespace.

#### 5. Checking for Invalid Sequences
```python
invalid = False
    
for sign in ["+", "*", "?"]:
    if sign + "+" in expression:
        invalid = True
        break
```
- **Purpose**: This block of code checks if the regex pattern contains any invalid sequences like `*+`, `++`, or `?+`.
- **Explanation**:
  - `invalid = False`: We start by assuming the pattern is valid (`invalid` is `False`).
  - `for sign in ["+", "*", "?"]:`: This loop iterates over a list of operators (`+`, `*`, `?`) that are commonly used in regex.
  - `if sign + "+" in expression:`: For each operator, the code checks if the pattern contains an invalid sequence like `++`, `*+`, or `?+`. 
  - `invalid = True`: If any invalid sequence is found, the `invalid` flag is set to `True`.
  - `break`: Exits the loop early if an invalid sequence is found.

#### 6. Handling Invalid Patterns
```python
if invalid:
    print("False")
```
- **Purpose**: If an invalid sequence was found in the previous step, the pattern is deemed invalid.
- **Explanation**:
  - `print("False")`: Outputs `False` indicating that the pattern is invalid.

#### 7. Attempting to Compile the Regular Expression
```python
else:
    try:
        re.compile(expression)
        print("True")
    except re.error:
        print("False")
```
- **Purpose**: If no invalid sequences were found, the code tries to compile the regex pattern using the `re.compile()` function.
- **Explanation**:
  - **`else:`**: This block runs if `invalid` is still `False`.
  - **`try:`**: The code attempts to compile the regex pattern.
    - `re.compile(expression)`: This function tries to compile the given pattern. If the pattern is valid, it succeeds silently.
    - `print("True")`: If the pattern is successfully compiled, it prints `True`, indicating the pattern is valid.
  - **`except re.error:`**: If there is an error (i.e., the pattern is not valid), the code catches the error.
    - `print("False")`: If an error occurs during compilation, it prints `False`, indicating the pattern is invalid.

### Summary
- The script first checks for specific invalid sequences in the regex pattern.
- If the pattern contains an invalid sequence, it immediately prints `False`.
- If no invalid sequences are found, the script tries to compile the pattern.
  - If successful, it prints `True`.
  - If an error occurs during compilation, it prints `False`. 

This process ensures that the script only prints `True` for valid regular expression patterns and `False` otherwise.
