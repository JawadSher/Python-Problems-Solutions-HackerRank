<h1 align='center'></h1>

## Problem Statement

**Problem URL :** [Regex Substitution](https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/d3373264-4cd7-4954-b8e8-e7390df9c549)
![image](https://github.com/user-attachments/assets/b766cc44-ff6c-42c0-b1eb-5b2cc2801fa4)
![image](https://github.com/user-attachments/assets/e2a8065f-37d5-4d6c-998d-ee160f2ee6d2)
![image](https://github.com/user-attachments/assets/25a3096e-33b9-48e1-a11a-17bd1de0a34a)

## Problem Solution
```py
import re

n = int(input())

for _ in range(n):
    line = input()
    
    line = re.sub(r'(?<= )&&(?= )', 'and', line)
    line = re.sub(r'(?<= )\|\|(?= )', 'or', line)
    
    print(line)
```

## Problem Solution Explanation
Let's break down the code and explain each part in detail:

```python
import re
```
- **What it does**: Imports the `re` module, which provides support for regular expressions in Python.

```python
n = int(input())
```
- **What it does**: Reads an integer from user input, which represents the number of lines to process. `input()` reads the input as a string, and `int()` converts it to an integer.

```python
for _ in range(n):
    line = input()
```
- **What it does**: Loops `n` times to process each line of input. For each iteration, `input()` reads a line of text from the user and stores it in the variable `line`.

```python
    line = re.sub(r'(?<= )&&(?= )', 'and', line)
```
- **What it does**: Uses the `re.sub()` function to replace occurrences of `&&` with `and` in the `line`.
  - `r'(?<= )&&(?= )'` is a regex pattern used here:
    - `(?<= )` is a **positive lookbehind assertion** that ensures there is a space before `&&`. This means `&&` must be preceded by a space.
    - `&&` is the literal string we're searching for.
    - `(?= )` is a **positive lookahead assertion** that ensures there is a space after `&&`. This means `&&` must be followed by a space.
  - This regex pattern ensures that `&&` is replaced only if it is surrounded by spaces, which helps avoid replacing `&&` in other contexts.

```python
    line = re.sub(r'(?<= )\|\|(?= )', 'or', line)
```
- **What it does**: Similarly, this line replaces occurrences of `||` with `or` in the `line`.
  - `r'(?<= )\|\|(?= )'` is the regex pattern used here:
    - `(?<= )` is a positive lookbehind assertion that ensures there is a space before `||`.
    - `\|\|` is the literal string for `||`. The `\` is used to escape the `|` character because `|` has a special meaning in regex (it represents "or").
    - `(?= )` is a positive lookahead assertion that ensures there is a space after `||`.

```python
    print(line)
```
- **What it does**: Prints the modified line after performing the substitutions.

### Example Walkthrough

**Input**:
```
3
x && y
a || b
this is a test && for regex || substitution
```

**Processing**:
1. For the first line, `x && y`:
   - `&&` is surrounded by spaces, so it gets replaced by `and`, resulting in `x and y`.

2. For the second line, `a || b`:
   - `||` is surrounded by spaces, so it gets replaced by `or`, resulting in `a or b`.

3. For the third line, `this is a test && for regex || substitution`:
   - `&&` is surrounded by spaces, so it gets replaced by `and`.
   - `||` is surrounded by spaces, so it gets replaced by `or`.
   - The resulting line is `this is a test and for regex or substitution`.

**Output**:
```
x and y
a or b
this is a test and for regex or substitution
```

### Summary

- The code reads a number of lines of input.
- For each line, it performs two substitutions:
  1. Replaces `&&` with `and` if it is surrounded by spaces.
  2. Replaces `||` with `or` if it is surrounded by spaces.
- Finally, it prints the modified line for each input.

This approach is useful for simple text processing where you need to replace specific patterns in a controlled way.
