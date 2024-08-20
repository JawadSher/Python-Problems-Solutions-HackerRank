<h1 align='center'>Reduce - Function</h1>

## Problem Statement

**Problem URL :** [Reduce Function](https://www.hackerrank.com/challenges/reduce-function/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/f5d54fc4-9ef9-4788-aa80-ff47ce40a398)
![image](https://github.com/user-attachments/assets/f2347401-b5ab-40ba-98bc-f6647007885b)

## Problem Solution
```py
from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y : x * y, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
```

## Problem Solution Explanation

Let's break down this code step by step to explain how it works, including examples to make it easy for beginners to understand.

#### 1. **Importing Modules:**
   ```python
   from fractions import Fraction
   from functools import reduce
   ```
   - **Explanation:**
     - `Fraction`: This is imported from the `fractions` module. The `Fraction` class allows you to create and manipulate fractions in Python.
     - `reduce`: This function is imported from the `functools` module. It applies a function cumulatively to the items of an iterable (e.g., a list), reducing the iterable to a single value.

#### 2. **Defining the `product()` Function:**
   ```python
   def product(fracs):
       t = reduce(lambda x, y : x * y, fracs)
       return t.numerator, t.denominator
   ```
   - **Explanation:**
     - This function takes a list of fractions `fracs` as input and returns the product of these fractions as a tuple containing the numerator and denominator.
     - **Line by Line:**
       1. `t = reduce(lambda x, y: x * y, fracs)`:
          - `reduce(lambda x, y: x * y, fracs)` multiplies all the fractions in the list `fracs` together. 
          - `lambda x, y: x * y` is a small anonymous function that takes two arguments `x` and `y` and returns their product.
          - **Example:**
            - If `fracs = [1/2, 3/4, 5/6]`, the reduce function will calculate `(1/2) * (3/4) * (5/6)`.
       2. `return t.numerator, t.denominator`:
          - After multiplying all the fractions, `t` is the resulting fraction.
          - `t.numerator` gives the numerator of the resulting fraction.
          - `t.denominator` gives the denominator of the resulting fraction.
          - **Example:**
            - If `t = 5/16`, the function returns `(5, 16)`.

#### 3. **Main Execution Block:**
   ```python
   if __name__ == '__main__':
       fracs = []
       for _ in range(int(input())):
           fracs.append(Fraction(*map(int, input().split())))
       result = product(fracs)
       print(*result)
   ```
   - **Explanation:**
     - This block of code is executed when the script runs directly.
     - **Line by Line:**
       1. `fracs = []`:
          - Initializes an empty list `fracs` to store the fractions.
       2. `for _ in range(int(input())):`:
          - This loop runs for the number of times specified by the user.
          - The `int(input())` part asks the user to input an integer, which specifies how many fractions they will input.
       3. `fracs.append(Fraction(*map(int, input().split())))`:
          - Inside the loop, this line reads a fraction from user input, splits it into two parts (numerator and denominator), converts them to integers, and creates a `Fraction` object.
          - The `Fraction` object is then added to the `fracs` list.
          - **Example:**
            - If the user inputs `1 2`, it means `1/2`. This is converted into `Fraction(1, 2)` and added to `fracs`.
       4. `result = product(fracs)`:
          - Calls the `product()` function with the list of fractions and stores the result (numerator and denominator) in `result`.
       5. `print(*result)`:
          - Prints the numerator and denominator of the product of all fractions.
          - The `*` operator unpacks the tuple `result` so that both the numerator and denominator are printed separately.

### Complete Example:

- **Input Example:**
  ```plaintext
  3
  1 2
  3 4
  10 6
  ```
  - Here, the user inputs `3`, meaning they will enter 3 fractions.
  - The fractions input are `1/2`, `3/4`, and `10/6`.

- **Execution Flow:**
  - The list `fracs` will be `[Fraction(1, 2), Fraction(3, 4), Fraction(10, 6)]`.
  - The `product(fracs)` function calculates the product of these fractions:
    - First, `1/2 * 3/4 = 3/8`
    - Then, `3/8 * 10/6 = 30/48`
    - The fraction `30/48` simplifies to `5/8`.
  - The `product()` function returns `(5, 8)`.

- **Output:**
  ```python
  5 8
  ```

This code calculates the product of a series of fractions entered by the user and prints the result as a simplified fraction (numerator and denominator).
