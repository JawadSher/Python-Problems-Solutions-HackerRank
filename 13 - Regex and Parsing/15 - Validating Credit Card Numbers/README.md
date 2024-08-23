<h1 align='center'>Validating - Credit - Card - Numbers</h1>

## Problem Statement

**Problem URL :** [Validating Credit Card Numbers](https://www.hackerrank.com/challenges/validating-credit-card-number/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/cc4da6d3-e64a-4c00-bb79-4f0ad5ea5f6a)
![image](https://github.com/user-attachments/assets/97198e74-8a38-46d0-9786-bbeb8eea257c)


## Problem Solution
```py
import re

n = int(input())
pattern = '^(?=[456])(?!.*(.)-?\\1-?\\1-?\\1)(\\d{4}-?){3}\\d{4}$'
for _ in range(n):
    card_num = input()
    
    if re.match(pattern, card_num):
        print("Valid")
    else:
        print("Invalid")
```

## Problem Solution Explanation
This Python code uses regular expressions to validate credit card numbers based on specific rules. Let's break it down line by line:

1. **Import the `re` module:**

    ```python
    import re
    ```

    - This line imports Python's `re` module, which provides support for working with regular expressions.

2. **Read the number of credit card numbers to validate:**

    ```python
    n = int(input())
    ```

    - This line reads an integer `n` from the input, which represents the number of credit card numbers to validate.

3. **Define the regular expression pattern:**

    ```python
    pattern = '^(?=[456])(?!.*(.)-?\\1-?\\1-?\\1)(\\d{4}-?){3}\\d{4}$'
    ```

    - This is the regular expression pattern used to validate the credit card numbers. Let's break down the pattern:

      - `^` and `$`: These anchors specify the start and end of the string, ensuring that the entire string must match the pattern.

      - `(?=[456])`: This is a positive lookahead assertion that checks if the first character of the string is either '4', '5', or '6'. This ensures that the card number starts with one of these digits.

      - `(?!.*(.)-?\\1-?\\1-?\\1)`: This is a negative lookahead assertion that prevents four or more consecutive repeated digits (with or without dashes). Let's break it down further:
        - `.` matches any character (but `.` is limited by what is specified next in `()`).
        - `(.)` captures any single character (a digit in this case) and stores it in a group.
        - `-?` matches an optional dash `-`.
        - `\\1` refers back to the captured digit from the first group, so `\\1-?\\1-?\\1` matches the captured digit three more times, optionally separated by dashes.
        - `.*` ensures that the negative lookahead checks the entire string.

      - `(\\d{4}-?){3}`: This part matches three groups of exactly four digits each (`\\d{4}`), optionally followed by a dash (`-?`). The `{3}` means this pattern must be repeated three times.

      - `\\d{4}`: This matches the final group of exactly four digits.

    - In summary, this pattern matches a credit card number with:
      1. Exactly 16 digits.
      2. Optionally grouped in blocks of four digits separated by dashes.
      3. Starting with a '4', '5', or '6'.
      4. No group of four identical digits, even if separated by dashes.

4. **Loop through each credit card number:**

    ```python
    for _ in range(n):
    ```

    - This loop will iterate `n` times, once for each credit card number that needs to be validated.

5. **Read the credit card number:**

    ```python
    card_num = input()
    ```

    - Reads the credit card number as a string for the current iteration.

6. **Check if the credit card number matches the pattern:**

    ```python
    if re.match(pattern, card_num):
        print("Valid")
    else:
        print("Invalid")
    ```

    - Uses `re.match()` to check if the `card_num` matches the `pattern`.
    - If it matches, it prints `"Valid"`. Otherwise, it prints `"Invalid"`.

### Example

Let's walk through some examples to see how the pattern works:

#### Example 1: `4253-5678-9012-3456`
- **Step-by-Step Validation:**
  - **Starting Digit Check:** The number starts with '4', so it passes the `(?=[456])` check.
  - **No Repeated Digits:** There are no four consecutive identical digits, so it passes the `(?!.*(.)-?\\1-?\\1-?\\1)` check.
  - **Correct Format:** The number has four groups of four digits separated by dashes, matching `(\\d{4}-?){3}\\d{4}`, so it is valid.

Result: `"Valid"`
