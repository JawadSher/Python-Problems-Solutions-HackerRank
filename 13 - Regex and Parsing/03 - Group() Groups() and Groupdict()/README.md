<h1 align='center'>Group() - Groups() - Groupdict()</h1>

## Problem Statement

**Problem URL :** [Group(), Groups() & Groupdict()](https://www.hackerrank.com/challenges/re-group-groups/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/f9d03f71-92ce-4c3d-a3e3-2fb2dadeaad8)
![image](https://github.com/user-attachments/assets/c6ca35fa-9bae-4821-9517-d74d491e7a8b)
![image](https://github.com/user-attachments/assets/167b8549-f39b-4c10-b620-dea42dace7eb)


## Problem Solution
```py
import re

S = input().strip()
pattern = re.compile(r'([0-9a-zA-Z]{1})\1+')
match = re.search(pattern, S)

if match:
    print(match.group(0)[0])
else:
    print(-1)
```

## Problem Solution Explanation
Let’s break down the code and explain how it works, along with some examples.

1. **`import re`**:
   - Imports the `re` module, which provides support for working with regular expressions in Python.

2. **`S = input().strip()`**:
   - Reads a line of input from the user and removes any leading or trailing whitespace using `strip()`. This input is stored in the variable `S`.

3. **`pattern = re.compile(r'([0-9a-zA-Z]{1})\1+')`**:
   - **`re.compile()`**: Compiles the regular expression pattern into a regex object, which can be used for matching.
   - **`([0-9a-zA-Z]{1})`**: This part of the pattern matches any single alphanumeric character (both digits 0-9 and letters a-z, A-Z). The parentheses `()` create a capturing group for this character.
   - **`\1+`**: The `\1` refers to the first capturing group, which is the single alphanumeric character matched by `([0-9a-zA-Z]{1})`. The `+` means one or more repetitions of this character. Together, `\1+` matches one or more occurrences of the same character that was captured by `([0-9a-zA-Z]{1})`.

4. **`match = re.search(pattern, S)`**:
   - **`re.search()`**: Searches the string `S` for the first location where the regex pattern matches. It returns a match object if found, otherwise `None`.

5. **`if match:`**:
   - Checks if a match object was found (i.e., the pattern matched part of the string).

6. **`print(match.group(0)[0])`**:
   - **`match.group(0)`**: Returns the entire matched string.
   - **`[0]`**: Retrieves the first character of this matched string. Since the pattern matches repeating characters, this will be the repeating character.

7. **`else: print(-1)`**:
   - If no match was found, it prints `-1`.

### Examples

Let's see how this code works with some example inputs.

#### Example 1

**Input**:
```
aaabbcc
```

**Processing**:
- **Pattern `([0-9a-zA-Z]{1})\1+`**: Looks for repeating characters.
- Matches `aaa` (because `a` is repeated).
- **`match.group(0)`**: Returns `aaa`.
- **`match.group(0)[0]`**: The first character of `aaa`, which is `a`.

**Output**:
```
a
```

#### Example 2

**Input**:
```
abcde
```

**Processing**:
- **Pattern `([0-9a-zA-Z]{1})\1+`**: Looks for repeating characters.
- No repeating characters found in the string.
- **`match`**: `None`.

**Output**:
```
-1
```

#### Example 3

**Input**:
```
111223344555
```

**Processing**:
- **Pattern `([0-9a-zA-Z]{1})\1+`**: Looks for repeating characters.
- Matches `111` (because `1` is repeated).
- **`match.group(0)`**: Returns `111`.
- **`match.group(0)[0]`**: The first character of `111`, which is `1`.

**Output**:
```
1
```

### Summary

- The code uses a regex pattern to find the first occurrence of any alphanumeric character that repeats.
- It prints the first repeating character if found, otherwise it prints `-1`.
- The pattern `([0-9a-zA-Z]{1})\1+` ensures that we detect repeating characters and handle alphanumeric inputs.
