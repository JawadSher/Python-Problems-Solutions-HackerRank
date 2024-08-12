<h1 align='center'>Compress - The - String!</h1>

## Problem Statement

**Problem URL :** [Compress the String!](https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/698c75ee-b08b-49d3-b677-ac583a3faef5)


## Problem Solution
```py
from itertools import groupby

s = input()

for k, g in groupby(s):
    print((len(list(g)), int(k)), end=" ")
```

## Problem Solution Explanation
Let's break down the code step by step with explanations and examples:

1. **Importing `groupby`**

   ```python
   from itertools import groupby
   ```

   - **`groupby`**: This function is part of the `itertools` module and is used to group consecutive identical elements in an iterable (like a string or list).

2. **Reading Input**

   ```python
   s = input()
   ```

   - **`input()`**: Reads a line of input from the user. For example, if the input is `11233221`, `s` will be `'11233221'`.

3. **Grouping Consecutive Characters**

   ```python
   for k, g in groupby(s):
   ```

   - **`groupby(s)`**: Groups consecutive identical characters in the string `s`. Here, `groupby` produces tuples where:
     - **`k`**: The key, which is the character being grouped.
     - **`g`**: An iterator over the group of consecutive identical characters.

   For example, with `s = '11233221'`, the `groupby` function produces:
   - `('1', <group of '1's>)`
   - `('2', <group of '2's>)`
   - `('3', <group of '3's>)`
   - `('2', <group of '2's>)`
   - `('1', <group of '1's>)`

4. **Printing the Results**

   ```python
   print((len(list(g)), int(k)), end=" ")
   ```

   - **`list(g)`**: Converts the group iterator `g` to a list so that you can count its length.
   - **`len(list(g))`**: The number of times the character `k` appears consecutively.
   - **`int(k)`**: Converts the character `k` to an integer (since `k` is a character).
   - **`end=" "`**: Ensures that the results are printed on the same line with a space in between, rather than each on a new line.

### Example

#### Input

```
11233221
```

#### Output

```
(2, 1) (2, 2) (2, 3) (2, 2) (2, 1) 
```

#### How It Works

- **`groupby(s)`**:
  - Groups `('1', <group of '1's>)`: `('1', ['1', '1'])`
  - Groups `('2', <group of '2's>)`: `('2', ['2', '2'])`
  - Groups `('3', <group of '3's>)`: `('3', ['3', '3'])`
  - Groups `('2', <group of '2's>)`: `('2', ['2', '2'])`
  - Groups `('1', <group of '1's>)`: `('1', ['1', '1'])`

- **Print Statements**:
  - `(2, 1)`: Two consecutive '1's.
  - `(2, 2)`: Two consecutive '2's.
  - `(2, 3)`: Two consecutive '3's.
  - `(2, 2)`: Two consecutive '2's.
  - `(2, 1)`: Two consecutive '1's.

The code effectively counts and prints the number of consecutive occurrences of each character in the input string.
