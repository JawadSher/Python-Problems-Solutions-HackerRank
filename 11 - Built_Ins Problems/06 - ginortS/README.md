<h1 align='center'>ginortS</h1>

## Problem Statement

**Problem URL :** [ginortS](https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/240091fa-309a-458b-9cca-bc1e39ef255e)
![image](https://github.com/user-attachments/assets/b4f95524-ba9a-456b-b66c-b1ce7bcf8bde)


## Problem Solution
```py
input_string = sorted(input())

lower = []
upper = []
odd = []
even = []

for char in input_string:
    if char.islower():
        lower.append(char)
    elif char.isupper():
        upper.append(char)
    elif char.isdigit():
        if int(char)%2 != 0:
            odd.append(char)
        else:
            even.append(char)

sorted_string = ''.join(lower + upper + odd + even)
print(sorted_string)
```

## Problem Solution Explanation
Let's break down the code step by step and explain each part with examples to help beginners understand it clearly.

### Problem Overview
The task is to take an input string and sort it such that:
1. All lowercase letters appear first.
2. Followed by all uppercase letters.
3. Followed by all odd digits (1, 3, 5, 7, 9).
4. Finally, followed by all even digits (0, 2, 4, 6, 8).

#### 1. **Reading and Sorting the Input String**
```python
input_string = sorted(input())
```
- `input()` reads a line of input from the user as a string. For example, if the user enters `"Sorting1234"`, `input()` will store the string `"Sorting1234"`.
- `sorted(input())` sorts the characters of the string in ascending order (alphabetically for letters and numerically for digits).
- The sorted characters are stored in the list `input_string`. For example, `"Sorting1234"` would be sorted as `['1', '2', '3', '4', 'g', 'i', 'n', 'o', 'r', 'S', 't']`.

#### 2. **Initializing Lists for Different Categories**
```python
lower = []
upper = []
odd = []
even = []
```
- These lists are initialized to store different categories of characters:
  - `lower` will store all lowercase letters.
  - `upper` will store all uppercase letters.
  - `odd` will store all odd digits.
  - `even` will store all even digits.

#### 3. **Iterating Over Each Character in the Sorted Input String**
```python
for char in input_string:
```
- This `for` loop goes through each character in the sorted list `input_string`.

#### 4. **Categorizing Characters**
```python
    if char.islower():
        lower.append(char)
    elif char.isupper():
        upper.append(char)
    elif char.isdigit():
        if int(char) % 2 != 0:
            odd.append(char)
        else:
            even.append(char)
```
- **If the character is a lowercase letter (`islower()`):**
  - It gets added to the `lower` list. For example, if `char = 'g'`, it gets added to `lower`.
  
- **If the character is an uppercase letter (`isupper()`):**
  - It gets added to the `upper` list. For example, if `char = 'S'`, it gets added to `upper`.
  
- **If the character is a digit (`isdigit()`):**
  - The code checks if the digit is odd or even:
    - `int(char) % 2 != 0`: Converts the character to an integer and checks if it’s odd by checking if the remainder when divided by 2 is not zero. If `char = '1'`, it gets added to `odd`.
    - Otherwise, it gets added to the `even` list. If `char = '4'`, it gets added to `even`.

#### 5. **Combining All Lists and Printing the Result**
```python
sorted_string = ''.join(lower + upper + odd + even)
print(sorted_string)
```
- The `+` operator combines the lists in the order: `lower`, `upper`, `odd`, `even`.
- `''.join(...)` combines all the characters in the list into a single string.
- Finally, `print(sorted_string)` outputs the result.

### Example Walkthrough

#### Example 1:
**Input:**
```
Sorting1234
```

**Step-by-Step Execution:**

1. **Sorting the Input:**
   - The input `"Sorting1234"` is sorted into `['1', '2', '3', '4', 'g', 'i', 'n', 'o', 'r', 'S', 't']`.
  
2. **Categorizing Characters:**
   - `lower` collects: `['g', 'i', 'n', 'o', 'r', 't']`
   - `upper` collects: `['S']`
   - `odd` collects: `['1', '3']`
   - `even` collects: `['2', '4']`

3. **Combining and Printing:**
   - The combined list is `['g', 'i', 'n', 'o', 'r', 't', 'S', '1', '3', '2', '4']`.
   - The final string is `"ginortS1324"`.

**Output:**
```
ginortS1324
```

#### Example 2:
**Input:**
```
aZ3bY2cX1
```

**Step-by-Step Execution:**

1. **Sorting the Input:**
   - The input `"aZ3bY2cX1"` is sorted into `['1', '2', '3', 'X', 'Y', 'Z', 'a', 'b', 'c']`.
  
2. **Categorizing Characters:**
   - `lower` collects: `['a', 'b', 'c']`
   - `upper` collects: `['X', 'Y', 'Z']`
   - `odd` collects: `['1', '3']`
   - `even` collects: `['2']`

3. **Combining and Printing:**
   - The combined list is `['a', 'b', 'c', 'X', 'Y', 'Z', '1', '3', '2']`.
   - The final string is `"abcXYZ132"`.

**Output:**
```
abcXYZ132
```

### Summary

- The code takes a string, sorts it, and then categorizes its characters into lowercase letters, uppercase letters, odd digits, and even digits.
- It then combines these categories in the required order and prints the result.
- The approach ensures that the output is structured and meets the specified sorting rules.

This breakdown should help beginners understand how each part of the code works and how the final result is generated.
