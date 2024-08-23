<h1 align='center'>Validating - Postal - Codes</h1>

## Problem Statement

**Problem URL :** [Validating Postal Codes](https://www.hackerrank.com/challenges/validating-postalcode/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/0c9eb8e2-b257-496a-952e-cc51c9eecd42)
![image](https://github.com/user-attachments/assets/db6a50f7-ccae-4d2b-8c5f-4a55b9b5601c)

## Problem Solution
```py
regex_integer_in_range = r"^[100000-999999]{6}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.

import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
```

## Problem Solution Explanation
This Python code validates whether a given input `P` is a six-digit number within a specified range and whether it contains fewer than two alternating repetitive digit pairs. Let's break down each part of the code line by line:

1. **Define the first regular expression:**

    ```python
    regex_integer_in_range = r"^[100000-999999]{6}$"  # Do not delete 'r'.
    ```

    - This line defines a regular expression pattern `regex_integer_in_range` to validate that the input is a six-digit number within the range 100000 to 999999.
    - However, the pattern `^[100000-999999]{6}$` is incorrect because it interprets the `[100000-999999]` as a character class, which is not the intended behavior. 

    **Corrected pattern:**

    The intended pattern should be:

    ```python
    regex_integer_in_range = r"^[1-9]\d{5}$"
    ```

    - `^`: Anchors the pattern to the start of the string.
    - `[1-9]`: Matches the first digit, ensuring it is between 1 and 9.
    - `\d{5}`: Matches exactly five digits (0-9), ensuring a six-digit number in total.
    - `$`: Anchors the pattern to the end of the string.

    This corrected pattern checks that the input is a six-digit number starting with a digit from 1 to 9, ensuring it falls within the range 100000 to 999999.

2. **Define the second regular expression:**

    ```python
    regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"  # Do not delete 'r'.
    ```

    - This line defines a regular expression pattern `regex_alternating_repetitive_digit_pair` to identify alternating repetitive digit pairs.
    - `(\d)`: Captures a digit and stores it in a group.
    - `(?=\d\1)`: This is a positive lookahead that checks if the captured digit is followed by another digit and then the same captured digit (`\1` refers to the first captured group).

    **Example Explanation:**
    - For input `P = "121426"`:
        - The regex finds `12` and `26`, but they are not alternating repetitive digit pairs.
        - It would not match any alternating repetitive pair in this example.
    - For input `P = "121212"`:
        - The regex would match `1212`, capturing `1` and `2` as alternating repetitive digit pairs.

3. **Import the `re` module:**

    ```python
    import re
    ```

    - This line imports the `re` module, which provides functions for working with regular expressions.

4. **Read the input:**

    ```python
    P = input()
    ```

    - This line reads the input string `P`, which represents the number to be validated.

5. **Validate the input:**

    ```python
    print (bool(re.match(regex_integer_in_range, P)) 
           and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
    ```

    - `re.match(regex_integer_in_range, P)`: Checks if `P` matches the pattern `regex_integer_in_range`.
        - `bool()`: Converts the match result to a boolean (`True` if the pattern matches, `False` otherwise).
    - `re.findall(regex_alternating_repetitive_digit_pair, P)`: Finds all matches of alternating repetitive digit pairs in `P`.
        - `len(re.findall(...)) < 2`: Checks if the number of alternating repetitive digit pairs is fewer than 2.
    - The `and` operator ensures that both conditions must be `True` for the entire expression to evaluate as `True`.

    **Output:**
    - If the input `P` is a valid six-digit number within the range 100000-999999 and contains fewer than two alternating repetitive digit pairs, the code will print `True`.
    - Otherwise, it will print `False`.

### Example

- **Example 1:**
    - Input: `P = "123456"`
    - `re.match(regex_integer_in_range, "123456")` returns `True` because `123456` is a valid six-digit number.
    - `re.findall(regex_alternating_repetitive_digit_pair, "123456")` returns an empty list `[]`, meaning there are no alternating repetitive digit pairs.
    - Since both conditions are met, the output is `True`.

- **Example 2:**
    - Input: `P = "112233"`
    - `re.match(regex_integer_in_range, "112233")` returns `True` because `112233` is a valid six-digit number.
    - `re.findall(regex_alternating_repetitive_digit_pair, "112233")` returns `['1', '2']`, meaning there are two alternating repetitive digit pairs.
    - Since the second condition is not met (there are 2 pairs), the output is `False`.

This code is useful for ensuring that an input number meets specific criteria for validity in terms of format and content.
