<h1 align='center'></h1>

## Problem Statement

**Problem URL :** [Validating Email Addresses with a Filter](https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/2b3e87a5-eaca-414c-b3b2-687329378bd3)
![image](https://github.com/user-attachments/assets/38f7ab0a-57b7-47a8-9602-7a574ddf4f00)

## Problem Solution
```py
import re

email_pattern = re.compile(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$')

def fun(s):
    return email_pattern.match(s)
    
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
```

## Problem Solution Explanation
Let's go through the code step by step and explain each part, including examples to make it easy to understand for beginners.

#### 1. **Importing the `re` Module:**
   ```python
   import re
   ```
   - **Explanation:** 
     - The `re` module in Python provides support for working with regular expressions (regex). Regular expressions are patterns used to match character combinations in strings.

#### 2. **Defining the Email Pattern Regex:**
   ```python
   email_pattern = re.compile(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$')
   ```
   - **Explanation:**
     - `re.compile()` compiles a regular expression pattern into a regex object, which can be used for matching later.
     - The regex pattern `r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'` is designed to match email addresses that follow a specific format:
       - `^` asserts the start of the string.
       - `[a-zA-Z0-9_-]+` matches one or more characters that can be lowercase or uppercase letters (`a-zA-Z`), digits (`0-9`), underscores (`_`), or hyphens (`-`).
       - `@` matches the literal `@` symbol.
       - `[a-zA-Z0-9]+` matches one or more characters that can be letters or digits.
       - `\.` matches the literal `.` (dot).
       - `[a-zA-Z]{1,3}` matches between 1 and 3 letters (the domain extension).
       - `$` asserts the end of the string.
     - **Examples:**
       - Valid: `example@example.com`, `user_name123@domain.org`
       - Invalid: `example@com`, `@example.com`, `user@domain`, `user@domain.toolong`

#### 3. **Defining the `fun()` Function:**
   ```python
   def fun(s):
       return email_pattern.match(s)
   ```
   - **Explanation:**
     - This function takes a string `s` as input.
     - `email_pattern.match(s)` checks if the entire string `s` matches the compiled regex pattern.
     - If the string matches the pattern, it returns a match object (which evaluates to `True`), otherwise, it returns `None` (which evaluates to `False`).
     - **Examples:**
       - `fun('example@example.com')` returns a match object (valid email).
       - `fun('example@com')` returns `None` (invalid email).

#### 4. **Defining the `filter_mail()` Function:**
   ```python
   def filter_mail(emails):
       return list(filter(fun, emails))
   ```
   - **Explanation:**
     - This function takes a list of email addresses (`emails`) as input.
     - `filter(fun, emails)` applies the `fun()` function to each email in the list and filters out only the valid emails (i.e., those for which `fun()` returns `True`).
     - `list(filter(...))` converts the filtered results back into a list.
     - **Examples:**
       - If `emails = ['example@example.com', 'example@com', 'user@domain.org']`, then `filter_mail(emails)` will return `['example@example.com', 'user@domain.org']`.

#### 5. **Main Execution Block:**
   ```python
   if __name__ == '__main__':
       n = int(input())
       emails = []
       for _ in range(n):
           emails.append(input())

   filtered_emails = filter_mail(emails)
   filtered_emails.sort()
   print(filtered_emails)
   ```
   - **Explanation:**
     - `if __name__ == '__main__':` is a standard Python idiom to ensure that the following code block runs only if the script is executed directly (not when imported as a module).
     - `n = int(input())`: 
       - Prompts the user to input an integer `n`, which specifies how many email addresses they will enter.
     - `emails = []` initializes an empty list to store the email addresses.
     - The `for _ in range(n):` loop runs `n` times, appending each input email address to the `emails` list.
     - `filtered_emails = filter_mail(emails)` filters the valid email addresses using the `filter_mail()` function.
     - `filtered_emails.sort()` sorts the filtered list of email addresses in alphabetical order.
     - `print(filtered_emails)` prints the sorted list of valid email addresses.

### Complete Example:

- **Input Example:**
  ```plaintext
  3
  user1@example.com
  invalidemail@
  user2@domain.org
  ```
  - Here, `n = 3`, so the user will input 3 email addresses.

- **Execution:**
  - The list `emails` will be `['user1@example.com', 'invalidemail@', 'user2@domain.org']`.
  - After filtering, only `['user1@example.com', 'user2@domain.org']` will remain, as `invalidemail@` does not match the pattern.
  - The valid emails will be sorted alphabetically, resulting in `['user1@example.com', 'user2@domain.org']`.

- **Output:**
  ```python
  ['user1@example.com', 'user2@domain.org']
  ```

This code is designed to take a list of email addresses from the user, filter out the invalid ones, sort the valid ones, and then print them.

