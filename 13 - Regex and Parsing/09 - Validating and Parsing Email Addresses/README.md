<h1 align='center'>Validating and Parsing Email Addresses</h1>

## Problem Statement

**Problem URL :** [Validating and Parsing Email Addresses](https://www.hackerrank.com/challenges/validating-named-email-addresses/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/ba8e1c1a-cbf6-47fc-b391-d2c3392532f6)
![image](https://github.com/user-attachments/assets/52cda696-c3a4-42c6-b0b6-0e89c3bac9d8)

## Problem Solution
```py
import re
import email.utils

n = int(input())

for _ in range(n):
    pattern = r'^[a-zA-Z][\w._-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
    
    inpt = email.utils.parseaddr(input())
    s = inpt[1]
    result = re.match(pattern, s)
    
    if result:
        print(email.utils.formataddr(inpt))
```

## Problem Solution Explanation
let's break down the code line by line to understand how it works:

```python
import re
import email.utils
```
- **`import re`**: This imports Python’s `re` module, which provides support for regular expressions.
- **`import email.utils`**: This imports the `utils` module from the `email` package, which provides utilities for handling email addresses and headers.

```python
n = int(input())
```
- **`n = int(input())`**: This reads an integer from the user input, which represents the number of email addresses to process. The `input()` function reads the input as a string, and `int()` converts it to an integer.

```python
for _ in range(n):
```
- **`for _ in range(n):`**: This sets up a loop that will iterate `n` times, once for each email address provided.

```python
    pattern = r'^[a-zA-Z][\w._-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
```
- **`pattern = r'^[a-zA-Z][\w._-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$'`**: This defines a regular expression pattern for matching email addresses. Here’s a breakdown:
  - **`^`**: Asserts the start of the string.
  - **`[a-zA-Z]`**: Ensures that the email starts with an alphabetical character.
  - **`[\w._-]+`**: Matches one or more word characters (`\w`), periods (`.`), underscores (`_`), or hyphens (`-`) in the local part of the email (before `@`).
  - **`@`**: Matches the literal `@` symbol.
  - **`[a-zA-Z]+`**: Matches one or more alphabetical characters in the domain part of the email (after `@` and before the period).
  - **`\.`**: Matches the literal period (`.`).
  - **`[a-zA-Z]{1,3}`**: Matches the top-level domain (TLD) which consists of 1 to 3 alphabetical characters.
  - **`$`**: Asserts the end of the string.

```python
    inpt = email.utils.parseaddr(input())
```
- **`inpt = email.utils.parseaddr(input())`**: This reads a string from user input and parses it into a tuple containing the email address and the name (if provided). `parseaddr()` is used to handle the email address and name more robustly.

```python
    s = inpt[1]
```
- **`s = inpt[1]`**: Extracts the email address part from the tuple returned by `parseaddr()`. `inpt[1]` contains the email address.

```python
    result = re.match(pattern, s)
```
- **`result = re.match(pattern, s)`**: Applies the regex pattern to the email address (`s`). `re.match()` checks if the beginning of the string matches the pattern.

```python
    if result:
        print(email.utils.formataddr(inpt))
```
- **`if result:`**: Checks if the regex pattern matched the email address (`result` will be non-`None` if there is a match).
- **`print(email.utils.formataddr(inpt))`**: If there is a match, it prints the formatted email address using `formataddr()`. This function ensures that the email address is correctly formatted as a string.

```python
    else:
        print("Invalid email")
```
- **`else: print("Invalid email")`**: If the regex pattern does not match the email address, it prints `"Invalid email"` indicating that the email address did not meet the pattern requirements.

### Summary

1. **Import Libraries**: Import necessary libraries for regex and email handling.
2. **Read Input**: Get the number of email addresses to process.
3. **Loop through Emails**: For each email address:
   - Define the regex pattern.
   - Parse and extract the email address.
   - Check if the email address matches the pattern.
   - Print the formatted email address if it matches, otherwise print `"Invalid email"`.
