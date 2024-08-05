<h1 align='center'>Capitalize</h1>

## Problem Statement
**Problem URL** : [Capitalize](https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/855c80dd-07d7-41ee-84ff-e255c8ba0fc7)

## Problem Solution
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

## Problem Solution Explanation

```python
#!/bin/python3
```
- This line is a shebang that indicates the script should be run using the Python interpreter located at `/bin/python3`. It’s used in Unix-like systems to specify the interpreter for executing the script.

```python
def solve(s):
```
- Defines a function named `solve` that takes one argument, `s`, which is a string that will be processed.

```python
    result = ""
```
- Initializes an empty string `result` which will be used to build the final output string.

```python
    capitalization = True
```
- Initializes a boolean variable `capitalization` to `True`. This variable tracks whether the next non-space character should be capitalized.

```python
    for char in s:
```
- Iterates over each character in the string `s`.

```python
        if char == ' ':
```
- Checks if the current character `char` is a space.

```python
            result += char
            capitalization = True
```
- If the character is a space, it is appended to the `result` string. The `capitalization` variable is set to `True`, indicating that the next non-space character should be capitalized.

```python
        elif capitalization:
```
- Checks if `capitalization` is `True`. This means the current character should be capitalized.

```python
            result += char.upper()
            capitalization = False
```
- Converts the current character to uppercase and appends it to the `result` string. Sets `capitalization` to `False` to ensure subsequent characters are not capitalized until the next space is encountered.

```python
        else:
            result += char
```
- If `capitalization` is `False`, appends the current character as is to the `result` string.

```python
    return result
```
- Returns the `result` string, which now contains the processed text with proper capitalization.

```python
if __name__ == '__main__':
```
- Checks if the script is being run directly (not imported as a module). If so, the code block following this line will be executed.

```python
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
```
- Opens a file for writing using the file path specified by the environment variable `OUTPUT_PATH`. This line assumes that the environment variable `OUTPUT_PATH` is set and contains the path to the output file.

```python
    s = input()
```
- Reads a string input from the user and assigns it to the variable `s`.

```python
    result = solve(s)
```
- Calls the `solve` function with `s` as the argument and stores the returned value in `result`.

```python
    fptr.write(result + '\n')
```
- Writes the `result` string to the file, followed by a newline character.

```python
    fptr.close()
```
- Closes the file after writing.

### Example

Consider the input string:
```
this is a test
```

1. **Initial Input:**
   - `s = "this is a test"`

2. **Processing:**
   - `capitalization = True` initially.
   - Iterating through the string:
     - `t` (capitalized): `Result = "T"`, `capitalization = False`
     - `h`: `Result = "Th"`, `capitalization = False`
     - `i`: `Result = "Thi"`, `capitalization = False`
     - `s`: `Result = "This"`, `capitalization = False`
     - Space: `Result = "This "`, `capitalization = True`
     - `i` (capitalized): `Result = "This I"`, `capitalization = False`
     - `s`: `Result = "This Is"`, `capitalization = False`
     - Space: `Result = "This Is "`, `capitalization = True`
     - `a` (capitalized): `Result = "This Is A"`, `capitalization = False`
     - Space: `Result = "This Is A "`, `capitalization = True`
     - `t` (capitalized): `Result = "This Is A T"`, `capitalization = False`
     - `e`: `Result = "This Is A Te"`, `capitalization = False`
     - `s`: `Result = "This Is A Tes"`, `capitalization = False`
     - `t`: `Result = "This Is A Test"`, `capitalization = False`

3. **Output:**
   - The final output is:
     ```
     This Is A Test
     ```

The `solve` function capitalizes the first letter of each word in the string and leaves the rest of the letters as they are.


