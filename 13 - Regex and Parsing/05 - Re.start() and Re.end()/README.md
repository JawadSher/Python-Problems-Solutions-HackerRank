<h1 align='center'></h1>

## Problem Statement

**Problem URL :** [Re.start() & Re.end()](https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/f6ac74f8-876c-4f8f-adb4-2484be2ab9d5)
![image](https://github.com/user-attachments/assets/041c638a-3e13-49a8-863c-58e4d48424a6)


## Problem Solution
```py
import re

string = input()
k_string = input()

pattern = f'(?=({k_string}))'
matches = list(re.finditer(pattern, string))

if matches:
    for m in matches:
        print(f"({m.start(1)}, {m.end(1) - 1})")
else:
   print("(-1, -1)")
```

## Problem Solution Explanation
 Let's break down your code line by line and explain each part, including how it works with an example.

```python
import re
```
- **What it does**: This line imports the `re` module, which provides support for regular expressions in Python. Regular expressions are a powerful tool for matching patterns in strings.


```python
string = input()
k_string = input()
```
- **What it does**: These two lines take input from the user.
  - `string`: The main string in which you want to search for a pattern.
  - `k_string`: The substring or pattern that you want to search for within the `string`.

**Example**:
- Let's say the user inputs the following:
  - `string = "aaadaa"`
  - `k_string = "aa"`


```python
pattern = f'(?=({k_string}))'
```
- **What it does**: This line defines the regular expression pattern that will be used to find all occurrences of `k_string` in `string`.
  - `f'...'`: This is an f-string, which allows you to include variables inside a string by placing them in curly braces `{}`.
  - `(?=({k_string}))`: This is a regular expression pattern.
    - `(?=...)`: This is a lookahead assertion. It checks for the presence of a pattern without consuming characters in the string, meaning it allows for overlapping matches.
    - `({k_string})`: This captures the substring you want to match and allows you to refer to this match later.

**Example**:
- With `k_string = "aa"`, the pattern becomes `(?=(aa))`. This pattern looks for occurrences of `"aa"` within `string`, even if they overlap.


```python
matches = list(re.finditer(pattern, string))
```
- **What it does**: This line uses the `re.finditer()` function to find all occurrences of the pattern in `string`. 
  - `re.finditer(pattern, string)`: This function returns an iterator yielding match objects for all non-overlapping matches of the regular expression `pattern` in `string`.
  - `list(...)`: Converts the iterator returned by `re.finditer()` into a list of match objects.

**Example**:
- For `string = "aaadaa"` and `pattern = "(?=(aa))"`, the `matches` list will contain match objects for each occurrence of `"aa"`.


```python
if matches:
```
- **What it does**: This checks if the `matches` list is not empty, meaning at least one match was found.
  - If `matches` contains any match objects, it evaluates as `True`.
  - If `matches` is empty, it evaluates as `False`.


```python
    for m in matches:
```
- **What it does**: This starts a loop that iterates over each match object in the `matches` list.


```python
        print(f"({m.start(1)}, {m.end(1) - 1})")
```
- **What it does**: Inside the loop, this line prints the start and end positions of each match.
  - `m.start(1)`: Returns the starting index of the match for the first capture group (which is the `k_string`).
  - `m.end(1) - 1`: Returns the ending index of the match for the first capture group, minus 1 (since `end()` returns the position just after the last character of the match).

**Example**:
- For `string = "aaadaa"` and `k_string = "aa"`, the output will be:
  - `(0, 1)` for the first occurrence of `"aa"`.
  - `(1, 2)` for the overlapping occurrence of `"aa"`.
  - `(4, 5)` for the third occurrence of `"aa"`.


```python
else:
   print("(-1, -1)")
```
- **What it does**: If the `matches` list is empty (meaning no matches were found), this line prints `(-1, -1)` to indicate that the substring was not found in the string.


### Full Example

Let’s go through a full example step by step:

1. **Input**:
   - `string = "aaadaa"`
   - `k_string = "aa"`

2. **Execution**:
   - `pattern` becomes `(?=(aa))`.
   - `matches` will contain three match objects:
     1. First match at index `(0, 1)`.
     2. Overlapping match at index `(1, 2)`.
     3. Match at index `(4, 5)`.

3. **Output**:
   - `(0, 1)`
   - `(1, 2)`
   - `(4, 5)`

If there were no matches, the code would output `(-1, -1)`.

This code efficiently handles overlapping matches and correctly identifies all positions where the substring occurs in the main string.
