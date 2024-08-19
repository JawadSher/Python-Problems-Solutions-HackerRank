<h1 align='center'>Input()</h1>

## Problem Statement

**Problem URL :** [Input()](https://www.hackerrank.com/challenges/input/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/23d2150b-0341-4dfd-adb3-31c95622e8d5)
![image](https://github.com/user-attachments/assets/70d12c6d-dcc9-46f5-85cc-788c2bbf9cce)


## Problem Solution
```py
x, k = map(int, input().split())
P = input()
result = eval(P)
print("False" if result != k else "True")
```

## Problem Solution Explanation

Let's break down this Python code step by step, explaining it in detail for beginners. We'll walk through each part of the code and provide an example to help clarify how it works.

1. **Input Parsing:**
   ```python
   x, k = map(int, input().split())
   ```
   - **`input()`**: This function reads a line of input from the user as a string.
   - **`split()`**: This method splits the input string by spaces and returns a list of substrings.
   - **`map(int, input().split())`**: The `map()` function applies the `int()` function to each element in the list returned by `split()`, converting them to integers. Here, the input provides two numbers:
     - `x`: A variable that might be used in the mathematical expression.
     - `k`: The value we expect the expression to evaluate to.

   **Example:**  
   If the input is `2 5`, then `x = 2` and `k = 5`.

2. **Reading the Mathematical Expression:**
   ```python
   P = input()
   ```
   - **`P = input()`**: This line reads another line of input, which is expected to be a mathematical expression involving the variable `x`. The expression is stored as a string in the variable `P`.

   **Example:**  
   If the input for `P` is `"x**2 + 3*x + 1"`, then `P = "x**2 + 3*x + 1"`.

3. **Evaluating the Expression:**
   ```python
   result = eval(P)
   ```
   - **`eval(P)`**: The `eval()` function takes a string as input and evaluates it as a Python expression. In this case, it substitutes the value of `x` into the expression `P` and computes the result.
   - **`result = eval(P)`**: The result of the evaluation is stored in the variable `result`.

   **Example:**  
   Suppose `x = 2` and `P = "x**2 + 3*x + 1"`.  
   The expression `"x**2 + 3*x + 1"` becomes `2**2 + 3*2 + 1`, which evaluates to `4 + 6 + 1 = 11`.  
   So, `result = 11`.

4. **Checking the Result:**
   ```python
   print("False" if result != k else "True")
   ```
   - **`if result != k`**: This condition checks if the result of the evaluation (`result`) is not equal to the expected value (`k`).
   - **`"False" if result != k else "True"`**: This is a conditional expression that prints `"False"` if `result` is not equal to `k`, and `"True"` if they are equal.
   - **`print(...)`**: Finally, the program prints the result.

   **Example:**  
   If `result = 11` and `k = 5`, the condition `result != k` is `True`, so it prints `"False"`.  
   If `k` were `11`, it would print `"True"`.

### Example Walkthrough:
Let's go through an example with input and output:

**Input:**
```
2 11
x**2 + 3*x + 1
```

- `x = 2`
- `k = 11`
- `P = "x**2 + 3*x + 1"`

**Evaluation:**
- The expression `P` is evaluated as `2**2 + 3*2 + 1`, which simplifies to `11`.

**Output:**
- Since `result = 11` and `k = 11`, the program prints `"True"`.

### Conclusion:
This code is a simple way to check if a mathematical expression involving a variable evaluates to a specific value. It uses the `eval()` function to compute the expression and a conditional statement to compare the result with the expected value. If they match, it prints `"True"`; otherwise, it prints `"False"`. This can be useful for verifying algebraic expressions or other mathematical calculations programmatically.
