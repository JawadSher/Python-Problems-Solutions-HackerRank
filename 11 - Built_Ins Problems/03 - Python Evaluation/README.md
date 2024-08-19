<h1 align='center'>Python - Evaluation</h1>

## Problem Statement

**Problem URL :** [Python Evaluation](https://www.hackerrank.com/challenges/python-eval/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/163af834-08a8-40b2-881a-c051d9de9317)
![image](https://github.com/user-attachments/assets/589b74dd-0b98-4fc0-993a-d64da94ef844)


## Problem Solution
```py
string = input()
result = eval(string)
```

## Problem Solution Explanation
This Python code takes a string input from the user, evaluates it as a Python expression using the `eval()` function, and stores the result in the variable `result`. Let's break it down step by step and explain it in detail with examples.

1. **Reading Input:**
   ```python
   string = input()
   ```
   - **`input()`**: This function reads a line of input from the user as a string. Whatever the user types is stored in the variable `string`.

   **Example 1:**  
   If the user inputs `2 + 3`, then `string` will be `"2 + 3"`.

   **Example 2:**  
   If the user inputs `4 * (5 + 6)`, then `string` will be `"4 * (5 + 6)"`.

2. **Evaluating the String as an Expression:**
   ```python
   result = eval(string)
   ```
   - **`eval(string)`**: The `eval()` function takes the string `string` and evaluates it as a Python expression. This means that `eval()` interprets the string as if it were actual Python code.
   - **`result = eval(string)`**: The result of this evaluation is stored in the variable `result`.

   **Example 1:**  
   With `string = "2 + 3"`, the `eval()` function interprets it as the expression `2 + 3`.  
   The evaluation returns `5`, so `result = 5`.

   **Example 2:**  
   With `string = "4 * (5 + 6)"`, the `eval()` function interprets it as `4 * (5 + 6)`.  
   The evaluation returns `4 * 11 = 44`, so `result = 44`.

### Examples in Detail:

1. **Simple Arithmetic:**
   - **Input:** `"7 - 2"`
   - **Evaluation:** `7 - 2 = 5`
   - **Result:** `result = 5`

2. **Complex Arithmetic:**
   - **Input:** `"3 ** 2 + 4 * 2"`
   - **Evaluation:** `3 ** 2 + 4 * 2 = 9 + 8 = 17`
   - **Result:** `result = 17`
   
3. **Using Variables:**
   ```python
   x = 10
   string = "x + 5"
   result = eval(string)
   ```
   - **Explanation:** If `x` is already defined in the code (e.g., `x = 10`), the input `"x + 5"` will evaluate to `10 + 5`.
   - **Evaluation:** `10 + 5 = 15`
   - **Result:** `result = 15`

### Important Notes for Beginners:
- **Security Warning:** The `eval()` function can execute arbitrary code, which means it can be dangerous if used with untrusted input. For example, if someone inputs a harmful command like `"__import__('os').system('rm -rf /')"`, it could cause significant damage by executing that command. So, use `eval()` with caution and only with trusted input.
- **Use Cases:** `eval()` is useful when you need to evaluate simple mathematical expressions or execute dynamically generated code. However, it's generally recommended to use safer alternatives for complex tasks.

### Conclusion:
The code provided is a simple way to evaluate any string as a Python expression and store the result. The `eval()` function is powerful but should be used carefully due to potential security risks. The examples show how different inputs lead to different results, demonstrating the flexibility of `eval()` in handling various Python expressions.
