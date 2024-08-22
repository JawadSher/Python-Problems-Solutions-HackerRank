<h1 align='center'>Validating phone numbers</h1>

## Problem Statement

**Problem URL :** [Validating phone numbers](https://www.hackerrank.com/challenges/validating-the-phone-number/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/e790e0d5-fa82-4acd-af1a-1b2f73c3a1d8)


## Problem Solution
```py
import re

n = int(input().strip())
pattern = r'^(\+1\s?)?([7 8 9]\d{2})([\s\-]?)\d{3}([\s\-]?)\d{4}$'

for _ in range(n):
    phone_num = input().strip()
    if re.match(pattern, phone_num) and len(phone_num) == 10:
        print("YES")
    else:
        print("NO")

```

## Problem Solution Explanation
Let's break down the code line by line, explaining each part and how it works:

```python
import re
```
- **`import re`**: This imports Python's `re` module, which provides support for regular expressions.

```python
n = int(input().strip())
```
- **`n = int(input().strip())`**: This line reads an integer input from the user (the number of phone numbers to process). The `strip()` function removes any leading or trailing whitespace from the input before converting it to an integer with `int()`.

```python
pattern = r'^(\+1\s?)?([7 8 9]\d{2})([\s\-]?)\d{3}([\s\-]?)\d{4}$'
```
- **`pattern = r'^(\+1\s?)?([7 8 9]\d{2})([\s\-]?)\d{3}([\s\-]?)\d{4}$'`**: This defines a regular expression pattern to match phone numbers. Here’s what each part means:
  - **`^`**: Asserts the position at the start of the string.
  - **`(\+1\s?)?`**: Optionally matches the country code `+1` followed by an optional space. The whole group is optional due to the `?` after the parentheses.
  - **`([7 8 9]\d{2})`**: Matches the area code, which is expected to start with `7`, `8`, or `9` followed by exactly two digits. **Note**: The pattern `[7 8 9]` is incorrect; it should be `[789]` to match digits `7`, `8`, or `9`.
  - **`([\s\-]?)`**: Optionally matches a space or hyphen.
  - **`\d{3}`**: Matches exactly 3 digits (the exchange code).
  - **`([\s\-]?)`**: Optionally matches a space or hyphen.
  - **`\d{4}`**: Matches exactly 4 digits (the subscriber number).
  - **`$`**: Asserts the position at the end of the string.

```python
for _ in range(n):
```
- **`for _ in range(n):`**: This initiates a loop that will iterate `n` times, once for each phone number.

```python
    phone_num = input().strip()
```
- **`phone_num = input().strip()`**: Reads a phone number from the user, removes any leading or trailing whitespace with `strip()`, and stores it in the variable `phone_num`.

```python
    if re.match(pattern, phone_num) and len(phone_num) == 10:
```
- **`if re.match(pattern, phone_num) and len(phone_num) == 10:`**: This checks two conditions:
  - **`re.match(pattern, phone_num)`**: Tests if the `phone_num` matches the `pattern` defined earlier.
  - **`len(phone_num) == 10`**: Ensures that the phone number has exactly 10 characters in length.

```python
        print("YES")
```
- **`print("YES")`**: If both conditions are met, it prints `"YES"` indicating that the phone number is valid.

```python
    else:
        print("NO")
```
- **`else: print("NO")`**: If either of the conditions is not met, it prints `"NO"` indicating that the phone number is not valid.
