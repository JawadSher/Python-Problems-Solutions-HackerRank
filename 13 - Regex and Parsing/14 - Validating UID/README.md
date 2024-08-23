<h1 align='center'>Validating - UID</h1>

## Problem Statement

**Problem URL :** [Validating UID](https://www.hackerrank.com/challenges/validating-uid/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/6ef20d70-7e23-4a02-aa64-724a831a3fc3)

## Problem Solution
```py
import re

Id_pattern = r"^(?=([a-z\d]*[A-Z]){2})(?=([a-zA-Z]*[\d]){3})(([a-zA-Z0-9])(?!.*\4)){10}$"

t = int(input())

for _ in range(t):
    ID = input()
    
    if re.match(Id_pattern, ID):
        print("Valid")
    else:
        print("Invalid")
```

## Problem Solution Explanation
This Python code uses regular expressions to validate IDs based on a specific pattern. Let's break it down line by line:

1. **Import the `re` module:**

    ```python
    import re
    ```

    - This line imports Python's `re` module, which provides support for regular expressions.

2. **Define the regular expression pattern:**

    ```python
    Id_pattern = r"^(?=([a-z\d]*[A-Z]){2})(?=([a-zA-Z]*[\d]){3})(([a-zA-Z0-9])(?!.*\4)){10}$"
    ```

    - This is the regular expression pattern used to validate the ID. Let's break down the pattern:

      - `^` and `$`: These anchors specify the start and end of the string, ensuring that the entire string must match the pattern.

      - `(?=([a-z\d]*[A-Z]){2})`: This is a positive lookahead assertion. It checks if there are at least two uppercase letters in the string, but it does not consume characters. `[a-z\d]*` matches any combination of lowercase letters and digits before the uppercase letter `[A-Z]`. `{2}` ensures that this pattern appears at least twice.

      - `(?=([a-zA-Z]*[\d]){3})`: Another positive lookahead assertion. It checks if there are at least three digits in the string, but it does not consume characters. `[a-zA-Z]*` matches any combination of letters before the digit `[\d]`. `{3}` ensures that this pattern appears at least three times.

      - `(([a-zA-Z0-9])(?!.*\4)){10}`: This part matches exactly 10 characters where each character is alphanumeric (`[a-zA-Z0-9]`). The `(?!.*\4)` is a negative lookahead assertion that ensures no character is repeated.

3. **Read the number of test cases:**

    ```python
    t = int(input())
    ```

    - This line reads an integer from the input, which represents the number of test cases.

4. **Loop through each test case:**

    ```python
    for _ in range(t):
    ```

    - This loop will iterate `t` times, processing each test case.

5. **Read the ID and validate it:**

    ```python
    ID = input()
    ```

    - Reads the ID string for the current test case.

6. **Check if the ID matches the pattern:**

    ```python
    if re.match(Id_pattern, ID):
        print("Valid")
    else:
        print("Invalid")
    ```

    - Uses `re.match()` to check if the ID matches the `Id_pattern`.
    - If it matches, it prints `"Valid"`. Otherwise, it prints `"Invalid"`.

### Example

Let's walk through an example to illustrate how the pattern works:

- Suppose the pattern is `^(?=([a-z\d]*[A-Z]){2})(?=([a-zA-Z]*[\d]){3})(([a-zA-Z0-9])(?!.*\4)){10}$` and we are validating the ID `aA1bB2cC3dD4`.

  - **Step-by-Step Validation:**
    - **Positive Lookahead for Uppercase Letters:** `(?=([a-z\d]*[A-Z]){2})`
      - `aA1bB2cC3dD4` contains three uppercase letters (`A`, `B`, `C`), so this part is satisfied.
    - **Positive Lookahead for Digits:** `(?=([a-zA-Z]*[\d]){3})`
      - `aA1bB2cC3dD4` contains four digits (`1`, `2`, `3`, `4`), so this part is satisfied.
    - **Exact 10 Characters with No Repeated Characters:** `(([a-zA-Z0-9])(?!.*\4)){10}`
      - `aA1bB2cC3dD4` has exactly 10 characters with no repeating characters.

Since all conditions are met, the ID `aA1bB2cC3dD4` would be considered `"Valid"`.

**Note:** The given regular expression might be complex and could have limitations or be incorrect for certain edge cases. Make sure to test thoroughly or simplify if needed.
