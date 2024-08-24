<h1 align='center'>Standardize - Mobile - Number - Using - Decorators</h1>

## Problem Statement

**Problem URL :** [Standardize Mobile Number Using Decorators](https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/2c6ec74e-a83c-4c51-b5ae-e55e941b04de)

## Problem Solution
```py
from re import sub

def wrapper(f):
    pattern = r"^(?:\+?91|0)??(\d{5})(\d{5})$"
    code_pattern = r"+91 \1 \2"
    
    def fun(l):
        return f([sub(pattern, code_pattern, i) for i in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
```

## Problem Solution Explanation
Let's break down the code line by line, explaining its purpose and functionality:

### Imports
```python
from re import sub
```
- This imports the `sub` function from the `re` (regular expression) module in Python. `sub` is used to replace occurrences of a pattern in a string.

### Wrapper Function Definition
```python
def wrapper(f):
    pattern = r"^(?:\+?91|0)??(\d{5})(\d{5})$"
    code_pattern = r"+91 \1 \2"
```
- The `wrapper` function takes another function `f` as an argument.
- Inside `wrapper`, two regular expression patterns are defined:
  - `pattern`: This pattern matches Indian phone numbers in different formats. It supports numbers starting with `+91`, `91`, `0`, or no prefix, followed by ten digits. The number is split into two groups of five digits.
  - `code_pattern`: This is the replacement pattern used with `sub`. It formats the phone number as `+91 XXXXX XXXXX`, where `\1` and `\2` represent the two groups of five digits captured by the `pattern`.

### Inner Function Definition
```python
    def fun(l):
        return f([sub(pattern, code_pattern, i) for i in l])
```
- `fun` is an inner function that takes a list `l` of phone numbers.
- It processes each phone number `i` in the list using `sub`, which replaces the matched pattern in `i` with the formatted pattern `code_pattern`.
- The list of formatted phone numbers is then passed to the original function `f` (which will be `sort_phone`).

### Applying the Wrapper
```python
    return fun
```
- The `wrapper` function returns the `fun` function, effectively replacing the original function `f` with `fun`. This allows `fun` to preprocess the phone numbers before passing them to `f`.

### Decorating the `sort_phone` Function
```python
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')
```
- The `@wrapper` decorator is applied to the `sort_phone` function. This means that when `sort_phone` is called, it is first passed through `wrapper`, so the `fun` function runs instead.
- `sort_phone` itself sorts the list `l` of phone numbers and prints each one on a new line using the `sep='\n'` argument.

### Main Execution Block
```python
if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
```
- This block handles user input:
  - It first reads an integer `n`, which represents the number of phone numbers to input.
  - It then reads `n` phone numbers from the user and stores them in the list `l`.
  - Finally, it calls `sort_phone(l)`, which is decorated and will print the sorted and formatted phone numbers.

### Example Execution
Let's walk through an example:

1. **Input:**
    ```plaintext
    3
    07895462130
    919875641230
    9195969878
    ```

2. **Processing:**
    - `07895462130` matches the pattern, and the replacement is `+91 78954 62130`.
    - `919875641230` matches the pattern, and the replacement is `+91 98756 41230`.
    - `9195969878` is first padded to `09195969878` (as the pattern expects 10 digits) and then replaced with `+91 19596 9878`.

3. **Output:**
    The numbers are sorted and printed:
    ```plaintext
    +91 19596 9878
    +91 78954 62130
    +91 98756 41230
    ```

In summary, this code takes a list of phone numbers in various formats, normalizes them to a standard format (`+91 XXXXX XXXXX`), and then prints them in sorted order.
