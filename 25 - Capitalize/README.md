# Problem Statement
**URL** : [Capitalize](https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/855c80dd-07d7-41ee-84ff-e255c8ba0fc7)

# Problem Solution
```
#!/bin/python3
def solve(s):
    result = ""
    capitalization = True
    
    for char in s:
        if char == ' ':
            result += char
            capitalization = True
        elif capitalization:
            result += char.upper()
            capitalization = False
        else:
            result += char
    
    return result

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()

```

## Source Code Explanation
-   **Function Definition:**
    
    -   `def solve(s):` defines a function named `solve` that takes a string `s` as input.
    -   The docstring (triple-quoted string) at the beginning provides a clear description of the function's purpose, arguments, and return value. This is especially helpful for code maintainability and understanding.
-   **Initializing Variables:**
    
    -   `result = ""`: Creates an empty string to store the output with the corrected capitalization.
    -   `capitalization = True`: Initializes a flag `capitalization` to `True` to indicate that the next character should be capitalized (assuming the first character could be the start of a word).
-   **Iterating Through the Input String:**
    
    -   `for char in s:` loops through each character in the input string `s`.
-   **Handling Whitespace:**
    
    -   `if char == ' ':`: Checks if the current character is a space.
        -   If so,  `result += char` appends the space to the output string.
        -   `capitalization = True` resets the `capitalization` flag to `True` in preparation for the next word (potentially starting with the next character).
-   **Capitalizing the First Letter of Each Word:**
    
    -   `elif capitalization:` Checks if the `capitalization` flag is still `True` (meaning the previous character was either a space or the beginning of the string).
        -   If so,  `result += char.upper()` converts the current character to uppercase (capitalizes it) and appends it to the output string.
        -   `capitalization = False` sets the `capitalization` flag to `False` to indicate that subsequent letters in the same word should be lowercase.
-   **Handling Other Characters:**
    
    -   `else:` This block executes if the current character is neither a space nor the first letter of a word (based on the `capitalization` flag).
        -   `result += char` Simply appends the character (which is assumed to be lowercase already) to the output string.
-   **Returning the Result:**
    
    -   `return result` returns the final `result` string, which contains the input string with the corrected capitalization.
