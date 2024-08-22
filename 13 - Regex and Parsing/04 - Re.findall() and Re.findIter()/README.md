<h1 align='center'>Re.findall() - and - Re.finditer()</h1>

## Problem Statement

**Problem URL :** [Re.findall() and Re.finditer()](https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/82f0ec24-402d-4390-aa3c-5f2cbc8da726)
![image](https://github.com/user-attachments/assets/9b42835d-b172-4e20-95d2-a2a9b7c1fd9c)


## Problem Solution
```py
import re

string = input().strip()
pattern = r"(?<=[^aeiou])([aeiou|AEIOU]{2,})(?=[^aeiou])"
matches = list(map(lambda x : x.group(), re.finditer(pattern, string)))

if matches:
    for i in matches:
        print(i)
else:
    print(-1)

```

## Problem Solution Explanation
let's break down the code line by line and explain each part with examples:

### 1. `import re`
```python
import re
```
- **Purpose**: This line imports the `re` module, which is Python's library for working with regular expressions. 

### 2. `string = input().strip()`
```python
string = input().strip()
```
- **Purpose**: This line reads a line of input from the user and removes any leading or trailing whitespace from it.
- **Example**: If the user inputs `"  rabcdeefgyYhFjkIoomnpOeorteeeeet  "`, after `strip()`, the `string` will be `"rabcdeefgyYhFjkIoomnpOeorteeeeet"`.

### 3. `pattern = r"(?<=[^aeiou])([aeiou|AEIOU]{2,})(?=[^aeiou])"`
```python
pattern = r"(?<=[^aeiou])([aeiou|AEIOU]{2,})(?=[^aeiou])"
```
- **Purpose**: This line defines a regular expression pattern to match sequences of two or more vowels surrounded by non-vowel characters.
- **Explanation**:
  - `(?<=[^aeiou])`: Positive lookbehind for a non-vowel character.
  - `([aeiou|AEIOU]{2,})`: Captures sequences of two or more vowels (both lowercase and uppercase).
  - `(?=[^aeiou])`: Positive lookahead for a non-vowel character.
- **Example**: In the string `"rabcdeefgyYhFjkIoomnpOeorteeeeet"`, this pattern will match `"ee"`, `"Ioo"`, `"Oeo"`, and `"eeeee"`.

### 4. `matches = list(map(lambda x : x.group(), re.finditer(pattern, string)))`
```python
matches = list(map(lambda x : x.group(), re.finditer(pattern, string)))
```
- **Purpose**: This line finds all matches of the pattern in the string and converts them to a list of matched strings.
- **Explanation**:
  - `re.finditer(pattern, string)`: Finds all matches of the pattern in the string and returns an iterator of match objects.
  - `map(lambda x : x.group(), ...)`: Applies a function to each match object to extract the matched substring.
  - `list(...)`: Converts the map object to a list.
- **Example**: For the string `"rabcdeefgyYhFjkIoomnpOeorteeeeet"`, `matches` will be `['ee', 'Ioo', 'Oeo', 'eeeee']`.

### 5. `if matches:`
```python
if matches:
```
- **Purpose**: Checks if there are any matches found.
- **Example**: If `matches` is `['ee', 'Ioo', 'Oeo', 'eeeee']`, this condition will be `True`.

### 6. `for i in matches:`
```python
for i in matches:
```
- **Purpose**: Iterates over each matched sequence in the `matches` list.
- **Example**: Iterates over `['ee', 'Ioo', 'Oeo', 'eeeee']`, so `i` will take on the values `'ee'`, `'Ioo'`, `'Oeo'`, and `'eeeee'` in turn.

### 7. `print(i)`
```python
print(i)
```
- **Purpose**: Prints each matched sequence.
- **Example**: Will print:
  ```
  ee
  Ioo
  Oeo
  eeeee
  ```

### 8. `else:`
```python
else:
```
- **Purpose**: Executes if the `if matches` condition is `False`, meaning no matches were found.

### 9. `print(-1)`
```python
print(-1)
```
- **Purpose**: Prints `-1` if no matches were found.
- **Example**: If `matches` is an empty list `[]`, this line will execute, printing `-1`.

### Full Example
Suppose the user inputs `"rabcdeefgyYhFjkIoomnpOeorteeeeet"`. 

- **Pattern Matching**: 
  - The regular expression finds the following vowel sequences surrounded by non-vowel characters: `'ee'`, `'Ioo'`, `'Oeo'`, `'eeeee'`.
- **Output**:
  ```
  ee
  Ioo
  Oeo
  eeeee
  ```

If the input string did not contain any matching sequences, such as `"abcd"`, the output would be `-1`.
