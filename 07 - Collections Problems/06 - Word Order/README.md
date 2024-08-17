<h1 align='center'>Word - Order</h1>

## Problem Statement

**Problem URL :** [Word Order](https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/4fcf16cf-c26d-40c9-b844-c05dd6285121)
![image](https://github.com/user-attachments/assets/acade75e-24c6-4e05-a82e-65c1eb5637c6)

## Problem Solution
```py
from collections import Counter

n = int(input().strip())

x = [input() for _ in range(n)]
print(len(Counter(x)))
print(*Counter(x).values())
```

## Problem Solution Explanation

Let's break down the provided Python code step by step to understand what each line does, including examples to illustrate the process.

```python
from collections import Counter
```
- **Importing the `Counter` class:** This line imports the `Counter` class from Python's `collections` module. `Counter` is a specialized dictionary that counts the occurrences of elements in an iterable (like a list).

```python
n = int(input().strip())
```
- **Reading the number of elements:** This line reads an integer input from the user, removes any leading or trailing whitespace with `strip()`, and converts the input into an integer. The result is stored in the variable `n`.
- Example: If the user inputs `5`, then `n` will hold the value `5`.

```python
x = [input() for _ in range(n)]
```
- **Creating a list of inputs:** This line creates a list `x` by reading `n` inputs from the user. A list comprehension is used to collect the inputs. Each input is read as a string.
- Example: If the user enters the following strings one by one:
  ```
  apple
  banana
  apple
  orange
  banana
  ```
  Then, `x` will be the list `['apple', 'banana', 'apple', 'orange', 'banana']`.

```python
print(len(Counter(x)))
```
- **Counting unique elements:** This line first creates a `Counter` object from the list `x`. The `Counter` will count the occurrences of each element in the list. The `len()` function then returns the number of unique elements in the list (i.e., the number of keys in the `Counter` dictionary).
- Example: For the list `['apple', 'banana', 'apple', 'orange', 'banana']`, the `Counter` object will be `Counter({'apple': 2, 'banana': 2, 'orange': 1})`. The length of this `Counter` is `3` because there are three unique elements: `'apple'`, `'banana'`, and `'orange'`.

```python
print(*Counter(x).values())
```
- **Printing the counts of each unique element:** The `Counter(x).values()` method returns a view object that displays the counts of each element in the `Counter`. The `*` operator is used to unpack these counts so they can be printed as separate arguments.
- Example: Continuing with the previous example, `Counter(x).values()` would give `dict_values([2, 2, 1])`. The `*` operator unpacks this to `2 2 1`, so the output will be `2 2 1`.

### Example Walkthrough

Let’s go through a full example step by step:

1. **User Input:**
    ```
    5
    apple
    banana
    apple
    orange
    banana
    ```

2. **Step-by-Step Execution:**

    - **`n = int(input().strip())`:** 
      - The user inputs `5`, so `n` becomes `5`.

    - **`x = [input() for _ in range(n)]`:**
      - The list comprehension reads 5 strings from the user: `['apple', 'banana', 'apple', 'orange', 'banana']`.

    - **`print(len(Counter(x)))`:**
      - `Counter(x)` becomes `Counter({'apple': 2, 'banana': 2, 'orange': 1})`.
      - `len(Counter(x))` is `3` because there are 3 unique elements.
      - The output is `3`.

    - **`print(*Counter(x).values())`:**
      - `Counter(x).values()` returns `dict_values([2, 2, 1])`.
      - `*Counter(x).values()` unpacks these values to `2 2 1`.
      - The output is `2 2 1`.

3. **Final Output:**
    ```
    3
    2 2 1
    ```

### Summary

- **Unique Elements:** The first print statement outputs the number of unique strings in the list.
- **Element Counts:** The second print statement outputs the count of each unique string in the list, in the order they first appear as unique in the `Counter`. 

This code efficiently counts and displays the number of unique items and their frequencies in the list.
