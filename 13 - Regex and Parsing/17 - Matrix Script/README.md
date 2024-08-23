<h1 align='center'>Matrix - Script</h1>

## Problem Statement

**Problem URL :** [Matrix Script](https://www.hackerrank.com/challenges/matrix-script/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/56e0fdfe-9c21-4758-9f1c-7d423b0933d2)
![image](https://github.com/user-attachments/assets/2064757d-74bc-4a76-ac10-bd5ecbc8472a)
![image](https://github.com/user-attachments/assets/047da8c5-78f5-4f75-834b-a06deb0b631b)

## Problem Solution
```py
import re

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix.append(input())

decoded_string = ""

for col in range(m):
    for row in range(n):
        decoded_string += matrix[row][col]
        
decoded_string = re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', decoded_string)

print(decoded_string)
```

## Problem Solution Explanation

1. **Input Reading and Initialization:**
    ```python
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    ```
    - `first_multiple_input` reads the first line of input, which contains two integers: `n` (number of rows) and `m` (number of columns).
    - The `rstrip().split()` method is used to remove any trailing spaces and split the input into a list of strings.
    - `n` and `m` are then converted to integers and stored.

    **Example:**
    - Input: `7 3`
    - `n = 7`, `m = 3`

2. **Matrix Input:**
    ```python
    matrix = []

    for _ in range(n):
        matrix.append(input())
    ```
    - An empty list `matrix` is initialized to store the rows of the matrix.
    - A loop runs `n` times, and in each iteration, it reads a row of the matrix and appends it to the `matrix` list.

    **Example:**
    - Suppose the following input is provided:
      ```
      Tsi
      h%x
      i #
      sM 
      $a 
      #t%
      ir!
      ```
    - The `matrix` list will store these rows as:
      ```python
      matrix = ['Tsi', 'h%x', 'i #', 'sM ', '$a ', '#t%', 'ir!']
      ```

3. **Column-wise Decoding:**
    ```python
    decoded_string = ""

    for col in range(m):
        for row in range(n):
            decoded_string += matrix[row][col]
    ```
    - An empty string `decoded_string` is initialized to build the decoded output.
    - The outer loop iterates over each column index (from `0` to `m-1`).
    - The inner loop iterates over each row index (from `0` to `n-1`).
    - Characters are concatenated to `decoded_string` by reading the matrix column by column.

    **Example:**
    - For `col = 0`:
      - Characters appended: `'T'` (matrix[0][0]), `'h'` (matrix[1][0]), `'i'` (matrix[2][0]), `'s'` (matrix[3][0]), `'$'` (matrix[4][0]), `'#'` (matrix[5][0]), `'i'` (matrix[6][0])
      - `decoded_string = "This#i"`
    - For `col = 1`:
      - Characters appended: `'s'` (matrix[0][1]), `'%'` (matrix[1][1]), `' '` (matrix[2][1]), `'M'` (matrix[3][1]), `'a'` (matrix[4][1]), `'t'` (matrix[5][1]), `'r'` (matrix[6][1])
      - `decoded_string = "This#is% Matr"`
    - For `col = 2`:
      - Characters appended: `'i'` (matrix[0][2]), `'x'` (matrix[1][2]), `'#'` (matrix[2][2]), `' '` (matrix[3][2]), `' '` (matrix[4][2]), `'%'` (matrix[5][2]), `'!'` (matrix[6][2])
      - `decoded_string = "This#is%Matrix#  %!"`

4. **Regular Expression Substitution:**
    ```python
    decoded_string = re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', decoded_string)
    ```
    - The `re.sub()` function is used to search for patterns in `decoded_string` and replace them.
    - The pattern `r'(?<=\w)([^\w\d]+)(?=\w)'` works as follows:
      - `(?<=\w)`: Positive lookbehind assertion ensuring the preceding character is a word character (alphanumeric).
      - `([^\w\d]+)`: Matches one or more characters that are not word characters (`\w`) or digits (`\d`), i.e., non-alphanumeric characters like symbols or spaces.
      - `(?=\w)`: Positive lookahead assertion ensuring the following character is a word character.
    - Any sequence of non-alphanumeric characters between two alphanumeric characters is replaced with a single space.

    **Example:**
    - In `"This#is%Matrix#  %!"`, the sequences `#`, `%`, and `#  %` are found between alphanumeric characters.
    - After substitution: `"This is Matrix#  %!"`

5. **Final Output:**
    ```python
    print(decoded_string)
    ```
    - The decoded and cleaned-up string is printed.

    **Example Output:**
    - The final output will be:
      ```
      This is Matrix#  %!
      ```

### Summary

This code reads a matrix of characters, extracts them in a column-wise manner to form a string, and then uses a regular expression to replace any sequences of non-alphanumeric characters between alphanumeric characters with a single space. The final result is a readable string with symbols and spaces cleaned up as required.
