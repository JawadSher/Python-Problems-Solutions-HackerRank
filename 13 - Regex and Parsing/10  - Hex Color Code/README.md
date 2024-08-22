<h1 align='center'></h1>

## Problem Statement

**Problem URL :** [Hex Color Code](https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/7543d210-86ea-45e3-9d88-db17c73c3fb8)
![image](https://github.com/user-attachments/assets/353efe6f-961d-4707-b5e0-9c5eea87c43d)
![image](https://github.com/user-attachments/assets/3d9ebe71-3d6a-4928-a57d-bf37b6f90288)

## Problem Solution
```py
import re

n = int(input())

for _ in range (n):
    css_code = input()
    hex_code = re.search(r'^#[A-Fa-f0-9]*', css_code)
    
    if not hex_code:
        hex_code1 = re.findall(r'#[A-Fa-f0-9]{6}|#[A-Fa-f0-9]{3}', css_code)
        
        if hex_code1:
            for i in hex_code1:
                print(i)
```

## Problem Solution Explanation
Let’s break down the code step by step, explaining each part and providing examples to illustrate how it works:

#### 1. **Import the `re` Module**
```python
import re
```
- Imports the `re` module, which is used for regular expressions in Python.

#### 2. **Read Number of Test Cases**
```python
n = int(input())
```
- Reads an integer input which represents the number of test cases.

#### 3. **Iterate Over Each Test Case**
```python
for _ in range(n):
    css_code = input()
```
- Loops through each test case and reads a line of input containing a CSS code (or text that may contain CSS color codes).

#### 4. **Search for Hexadecimal Color Code Pattern**
```python
hex_code = re.search(r'^#[A-Fa-f0-9]*', css_code)
```
- Uses `re.search` to find a match for the pattern `r'^#[A-Fa-f0-9]*'` in `css_code`. This pattern looks for a string starting with `#` followed by zero or more hexadecimal characters (`A-F`, `a-f`, or `0-9`).
- The `^` asserts the position at the start of the string. However, this pattern only matches if the entire string starts with `#` followed by any number of hexadecimal characters.

#### 5. **If No Match is Found**
```python
if not hex_code:
    hex_code1 = re.findall(r'#[A-Fa-f0-9]{6}|#[A-Fa-f0-9]{3}', css_code)
```
- If `re.search` doesn’t find a match (`if not hex_code`), then `re.findall` is used to find all occurrences of the pattern `#[A-Fa-f0-9]{6}|#[A-Fa-f0-9]{3}` in `css_code`. This pattern matches either:
  - `#[A-Fa-f0-9]{6}`: A `#` followed by exactly six hexadecimal digits.
  - `#[A-Fa-f0-9]{3}`: A `#` followed by exactly three hexadecimal digits.

#### 6. **Print Valid Hex Color Codes**
```python
if hex_code1:
    for i in hex_code1:
        print(i)
```
- If any valid hex color codes are found, iterate through each match (`hex_code1`) and print it.

### Examples

**Example 1:**
- **Input:**
  ```
  2
  #FfFdF8
  #aef
  ```
- **Output:**
  ```
  #FfFdF8
  #aef
  ```
  Explanation: Both `#FfFdF8` (6 hexadecimal digits) and `#aef` (3 hexadecimal digits) are valid color codes.

**Example 2:**
- **Input:**
  ```
  2
  #12345
  #XYZ
  ```
- **Output:**
  ```
  #123
  ```
  Explanation: `#12345` is not valid since it has 5 digits, but `#123` is valid as it has exactly 3 digits. `#XYZ` is not valid as it does not consist of hexadecimal digits.

**Example 3:**
- **Input:**
  ```
  1
  #abcd12 #def123
  ```
- **Output:**
  ```
  #abcd12
  #def123
  ```
  Explanation: Both `#abcd12` and `#def123` are valid 6-digit hexadecimal color codes.

### Summary

- The code reads multiple lines of input.
- It first checks if the entire string starts with a valid hex code pattern.
- If not, it looks for all valid hex codes in the string.
- It then prints each valid hex code it finds.

This approach ensures you can find and validate hexadecimal color codes in strings while handling various cases where the color codes might appear.
