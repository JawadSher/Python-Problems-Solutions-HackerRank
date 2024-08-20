<h1 align='center'>Detect - Floating - Point - Number</h1>

## Problem Statement

**Problem URL :** [Deletect Floating Point Number](https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/263c959f-bd22-4031-ba36-def8a945cedd)
![image](https://github.com/user-attachments/assets/b457938c-a9ce-45b1-a8d1-1afca4c68e8e)

## Problem Solution
```py
import re

N = int(input().strip())

for _ in range(N):
    input_value = input()
    pattern = re.compile(r'^(?!\..*\.)[+\.-]{0,1}\d*\.\d*$')
    print(bool(re.match(pattern, input_value)))
```

## Problem Solution Explanation
Let’s dive into the provided code and explain each part in detail, including how the regular expression works with examples.


1. **`import re`**:
   - Imports the `re` module, which provides support for working with regular expressions in Python.

2. **`N = int(input().strip())`**:
   - Reads an integer input from the user, which represents the number of test cases. `strip()` removes any leading or trailing whitespace from the input.

3. **`for _ in range(N):`**:
   - Loops through each of the `N` test cases. The loop variable `_` is unused.

4. **`input_value = input()`**:
   - Reads a line of input from the user, which is expected to be a string representing a potential floating-point number.

5. **`pattern = re.compile(r'^(?!\..*\.)[+\.-]{0,1}\d*\.\d*$')`**:
   - Compiles a regular expression pattern into a regex object for matching against the input string. The pattern is designed to match floating-point numbers with specific rules.

6. **`print(bool(re.match(pattern, input_value)))`**:
   - Uses `re.match` to check if the `input_value` matches the compiled regex pattern. `re.match` returns a match object if the pattern matches the start of the string, or `None` if it doesn't. `bool()` converts the result to `True` if there is a match or `False` otherwise. The result is then printed.

### Regular Expression Pattern Breakdown

**Pattern: `r'^(?!\..*\.)[+\.-]{0,1}\d*\.\d*$'`**

1. **`^`**:
   - Anchors the pattern to the start of the string.

2. **`(?!\..*\.)`**:
   - This is a negative lookahead assertion. It ensures that there is no more than one decimal point in the string. If there is more than one decimal point, the match fails. This prevents formats like `1.2.3`.

3. **`[+\.-]{0,1}`**:
   - Matches an optional leading sign (`+`, `-`, or `.`). The `{0,1}` quantifier means that one or zero of these characters is allowed. This allows numbers to optionally start with a `+` or `-` sign.

4. **`\d*\.\d*`**:
   - **`\d*`**: Matches zero or more digits before the decimal point.
   - **`\.`**: Matches the decimal point itself.
   - **`\d*`**: Matches zero or more digits after the decimal point. 

5. **`$`**:
   - Anchors the pattern to the end of the string. Ensures that the entire string matches the pattern.

### Examples

Let's see how this pattern works with different input values:

1. **`123.456`**
   - Matches because it has digits before and after the decimal point.
   - Result: `True`

2. **`+123.456`**
   - Matches because it starts with a `+` sign and has digits before and after the decimal point.
   - Result: `True`

3. **`-123.456`**
   - Matches because it starts with a `-` sign and has digits before and after the decimal point.
   - Result: `True`

4. **`123.`**
   - Matches because it has digits before the decimal point and a decimal point, even though there are no digits after the decimal point.
   - Result: `True`

5. **`.456`**
   - Matches because it has digits after the decimal point and no digits before it. The negative lookahead ensures only one decimal point.
   - Result: `True`

6. **`123.456.789`**
   - Does not match because there is more than one decimal point.
   - Result: `False`

7. **`abc`**
   - Does not match because it contains non-numeric characters and no decimal point.
   - Result: `False`

8. **`1.2.3`**
   - Does not match because there is more than one decimal point.
   - Result: `False`

### Summary

The provided regex pattern effectively checks for valid floating-point numbers while ensuring:
- There is at most one decimal point.
- Optionally starts with a `+` or `-` sign.
- Contains digits, optionally before and/or after the decimal point.

It does not handle scientific notation or cases where numbers have no digits after the decimal point but still is effective for a majority of common floating-point number formats.

