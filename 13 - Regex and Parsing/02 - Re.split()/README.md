<h1 align='center'>Re.Split()</h1>

## Problem Statement

**Problem URL :** [Re.split()](https://www.hackerrank.com/challenges/re-split/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/3be94c77-5b5b-4ee4-95c3-567b3c16b8b6)

## Problem Solution
```py

regex_pattern = r"[,.]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))
```


## Problem Solution Explanation
 Let’s break down the provided code and explain how it works with examples.

1. **`regex_pattern = r"[,.]"`**:
   - **`r"[,.]"`**: This is a raw string literal in Python. The `r` before the string makes it a raw string, meaning backslashes are treated literally and not as escape characters. This regex pattern matches either a comma `,` or a period `.`.
   - **`[,.]`**: This is a character class in regex. It matches any single character that is either a comma or a period.

2. **`import re`**:
   - Imports the `re` module, which provides functions for working with regular expressions in Python.

3. **`input()`**:
   - Reads a line of input from the user. The `input()` function captures everything typed by the user until they press Enter.

4. **`re.split(regex_pattern, input())`**:
   - **`re.split(pattern, string)`**: This function splits the `string` at each occurrence of the pattern specified by `regex_pattern`. The `regex_pattern` `[,.]` means that the string will be split wherever a comma or a period is found.
   - The `input()` function provides the string to be split based on the pattern.

5. **`"\n".join(...)`**:
   - **`"\n"`**: This is the newline character. When used with `.join()`, it joins the elements of a list with a newline character between them.
   - **`"\n".join(re.split(regex_pattern, input()))`**: This joins the list of strings returned by `re.split` with a newline between each element, effectively printing each part on a new line.

### Examples

Let’s go through some examples to understand how this code works.

#### Example 1

**Input**:
```
Hello, World. How are you?
```

**Processing**:
- **`regex_pattern = r"[,.]"`**: The pattern will split the input at every comma `,` and period `.`.
- **`re.split(r"[,.]", "Hello, World. How are you?")`**:
  - Splits at `,` resulting in: `["Hello", " World. How are you?"]`
  - Splits at `.` resulting in: `["Hello", " World", " How are you?"]`

**Output**:
```
Hello
 World
 How are you?
```

#### Example 2

**Input**:
```
One. Two, Three. Four
```

**Processing**:
- **`regex_pattern = r"[,.]"`**: The pattern will split the input at every comma `,` and period `.`.
- **`re.split(r"[,.]", "One. Two, Three. Four")`**:
  - Splits at `.` resulting in: `["One", " Two", " Two, Three", " Four"]`
  - Splits at `,` resulting in: `["One", " Two", " Three", " Four"]`

**Output**:
```
One
 Two
 Three
 Four
```

### Summary

- **`re.split(regex_pattern, input())`**: Splits the input string at every occurrence of `,` or `.`.
- **`"\n".join(...)`**: Joins the resulting list of strings with newline characters, so each substring appears on a new line when printed.

The code effectively separates the input string by commas and periods, then prints each separated part on a new line.
