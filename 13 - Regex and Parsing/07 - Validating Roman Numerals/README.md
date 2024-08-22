<h1 align='center'>Validating Roman Numerals</h1>

## Problem Statement

**Problem URL :** [Validating Roman Numerals](https://www.hackerrank.com/challenges/validate-a-roman-number/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/45c4a94f-9e57-4601-b0e2-bbab68949170)

## Problem Solution
```py
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.
# No One beat Chat-GPT

import re
print(str(bool(re.match(regex_pattern, input()))))
```

## Problem Solution Explanation
Let’s break down this code step by step to explain how it works:

```python
import re
```
- **What it does**: Imports the `re` module, which provides support for working with regular expressions in Python.

```python
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
```
- **What it does**: Defines a regular expression pattern for matching Roman numerals. The `r` before the string indicates a raw string, which tells Python to treat backslashes as literal characters and not escape sequences.

### Explanation of the Regex Pattern
- **`^`**: Asserts that the match must start at the beginning of the string.
- **`M{0,3}`**: Matches 0 to 3 occurrences of the letter `M`. This covers the thousands place (e.g., 1000, 2000, 3000).
- **`(CM|CD|D?C{0,3})`**: Matches the hundreds place:
  - **`CM`**: Matches 900.
  - **`CD`**: Matches 400.
  - **`D?`**: Matches 0 or 1 occurrence of `D` (500). The question mark `?` means "0 or 1" occurrence.
  - **`C{0,3}`**: Matches 0 to 3 occurrences of `C`. This covers 100, 200, and 300.
- **`(XC|XL|L?X{0,3})`**: Matches the tens place:
  - **`XC`**: Matches 90.
  - **`XL`**: Matches 40.
  - **`L?`**: Matches 0 or 1 occurrence of `L` (50).
  - **`X{0,3}`**: Matches 0 to 3 occurrences of `X`. This covers 10, 20, and 30.
- **`(IX|IV|V?I{0,3})`**: Matches the ones place:
  - **`IX`**: Matches 9.
  - **`IV`**: Matches 4.
  - **`V?`**: Matches 0 or 1 occurrence of `V` (5).
  - **`I{0,3}`**: Matches 0 to 3 occurrences of `I`. This covers 1, 2, and 3.
- **`$`**: Asserts that the match must end at the end of the string.

### Full Code Explanation

```python
import re
```
- Imports the `re` module for regular expressions.

```python
print(str(bool(re.match(regex_pattern, input()))))
```
- **`input()`**: Reads a line of input from the user as a string.
- **`re.match(regex_pattern, input())`**: Uses the `re.match()` function to check if the input string matches the regex pattern defined in `regex_pattern`. `re.match()` checks for a match only at the beginning of the string.
- **`bool(...)`**: Converts the result of `re.match()` to a boolean value. If `re.match()` returns a match object (meaning the input matches the pattern), `bool(...)` will be `True`. If it returns `None` (meaning no match), `bool(...)` will be `False`.
- **`str(...)`**: Converts the boolean value to a string. This is done so that `True` or `False` is printed as a string.
- **`print(...)`**: Prints the result to the console.

### Example

**Input**:
```
MMXXI
```

**Process**:
- The regex pattern will check if `MMXXI` is a valid Roman numeral. In this case, it is, so `re.match()` returns a match object.

**Output**:
```
True
```

**Explanation**:
- `MMXXI` is a valid Roman numeral, so `re.match()` returns a match object. `bool(re.match(...))` is `True`, and `str(True)` results in the output `True`.

If the input were `MMXVI`, which is also a valid Roman numeral, the output would be `True`. If the input were `MMMM`, which is not valid (since 4000 is not represented in standard Roman numerals), the output would be `False`.
