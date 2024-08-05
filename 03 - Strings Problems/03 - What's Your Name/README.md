<h1 align='center'>What's - Your - Name</h1>

## Problem Statement 
**Problem URL : [What's Your Name](https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/6292609f-fb6d-43ca-b6d6-4e3dc0de8881)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/ebd4f2be-c0cd-44a5-8573-ef1bd3fe3fe4)

## Problem Solution 
```
def print_full_name(first, last):
    print(f'Hello {first} {last}! You just delved into python.')

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
```

## Problem Solution Explanation
Let's break down the code and its functionality step by step.
#### Function Definition

```
def print_full_name(first, last):
	print(f'Hello {first} {last}! You just delved into python.')
``` 

-   **Function Name:** `print_full_name`
-   **Parameters:** The function takes two parameters, `first` and `last`, which are expected to be strings representing a person's first name and last name.
-   **Function Body:** The function prints a formatted string that incorporates the values of `first` and `last`. The formatted string uses an f-string (formatted string literal) which allows embedding expressions inside string literals using curly braces `{}`.

#### 2. Main Block
```
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
``` 

-   **Conditional Statement:** `if __name__ == '__main__':`
    -   This line checks if the script is being run as the main program. In Python, the `__name__` variable is set to `'__main__'` when the script is executed directly. If the script is imported as a module in another script, `__name__` will be set to the module's name instead.
-   **Input Collection:**
    -   `first_name = input()`: This line reads a string from the user input and assigns it to the variable `first_name`.
    -   `last_name = input()`: This line reads another string from the user input and assigns it to the variable `last_name`.
-   **Function Call:** `print_full_name(first_name, last_name)`
    -   This line calls the `print_full_name` function, passing `first_name` and `last_name` as arguments.

### How It Works

1.  When the script is run, the `if __name__ == '__main__':` block ensures that the subsequent code only runs if the script is executed directly, not when it's imported as a module.
2.  The script prompts the user to enter their first and last names using the `input()` function. The entered names are stored in the `first_name` and `last_name` variables.
3.  The `print_full_name` function is called with the provided `first_name` and `last_name` as arguments.
4.  Inside the `print_full_name` function, the formatted string `f'Hello {first} {last}! You just delved into python.'` is printed, where `{first}` and `{last}` are replaced with the actual values of the `first_name` and `last_name` variables.

### Example

If a user inputs "John" for the first name and "Doe" for the last name, the output will be:

`Hello John Doe! You just delved into python.` 

This code is a simple demonstration of defining and using a function, collecting user input, and using f-strings for formatted output in Python.

