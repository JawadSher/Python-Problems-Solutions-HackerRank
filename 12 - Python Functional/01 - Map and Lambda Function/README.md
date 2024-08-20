<h1 align='center'>Map - And - Lambda - Function</h1>

## Problem Statement

**Problem URL :** [Map and Lambda Function](https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/294cc228-21c4-411f-a33e-0ab64cac0487)
![image](https://github.com/user-attachments/assets/2440f71f-ee4f-4523-a15f-0e1b16ee9c7a)


## Problem Solution
```py
cube = lambda x: x*x*x

def fibonacci(n):
    fibnoacci_nums = [0, 1]
    for _ in range(2, n):
        fibnoacci_nums.append(fibnoacci_nums[-1] + fibnoacci_nums[-2])
    return fibnoacci_nums[:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
```

## Problem Solution Explanation
Let's break down this code step by step and explain each part with examples.

#### 1. **Lambda Function:**
   ```python
   cube = lambda x: x*x*x
   ```
   - **Explanation:** 
     - This line defines a lambda function named `cube` that takes an argument `x` and returns `x` raised to the power of 3 (i.e., `x^3`). 
     - **Example:**
       - If `x = 2`, then `cube(2)` would return `2 * 2 * 2 = 8`.
       - If `x = 3`, then `cube(3)` would return `3 * 3 * 3 = 27`.

#### 2. **Fibonacci Function:**
   ```python
   def fibonacci(n):
       fibonacci_nums = [0, 1]
       for _ in range(2, n):
           fibonacci_nums.append(fibonacci_nums[-1] + fibonacci_nums[-2])
       return fibonacci_nums[:n]
   ```
   - **Explanation:**
     - This is a function named `fibonacci` that generates the first `n` Fibonacci numbers.
     - **Line by Line:**
       1. `fibonacci_nums = [0, 1]`: 
          - Initializes a list called `fibonacci_nums` with the first two Fibonacci numbers: 0 and 1.
       2. `for _ in range(2, n):`:
          - This loop runs from 2 up to `n-1` (i.e., it runs `n-2` times) to generate the rest of the Fibonacci numbers.
          - **Example:**
            - If `n = 5`, the loop will run 3 times (for `2, 3, 4`).
       3. `fibonacci_nums.append(fibonacci_nums[-1] + fibonacci_nums[-2])`:
          - This line adds the next Fibonacci number to the list by summing the last two numbers in the list (`fibonacci_nums[-1]` and `fibonacci_nums[-2]`).
          - **Example:**
            - If the current list is `[0, 1, 1]`, it adds `1 + 1 = 2` to the list, making it `[0, 1, 1, 2]`.
       4. `return fibonacci_nums[:n]`:
          - This line returns the first `n` numbers from the `fibonacci_nums` list.
          - **Example:**
            - If `n = 5`, it returns `[0, 1, 1, 2, 3]`.

#### 3. **Main Execution Block:**
   ```python
   if __name__ == '__main__':
       n = int(input())
       print(list(map(cube, fibonacci(n))))
   ```
   - **Explanation:**
     - This block of code runs when the script is executed directly.
     - **Line by Line:**
       1. `n = int(input())`:
          - It prompts the user to enter a number `n` and converts the input to an integer.
          - **Example:**
            - If the user inputs `4`, then `n = 4`.
       2. `print(list(map(cube, fibonacci(n))))`:
          - This line does two main tasks:
            1. `fibonacci(n)` is called to generate the first `n` Fibonacci numbers.
            2. `map(cube, fibonacci(n))` applies the `cube` function to each of the Fibonacci numbers generated.
            3. `list(map(cube, fibonacci(n)))` converts the result into a list and prints it.
          - **Example:**
            - If `n = 4`, the first 4 Fibonacci numbers are `[0, 1, 1, 2]`.
            - Applying `cube` to each: `[cube(0), cube(1), cube(1), cube(2)]` results in `[0, 1, 1, 8]`.
            - The output will be `[0, 1, 1, 8]`.

### Complete Example:
- **Input:** Suppose the user inputs `5`.
- **Execution Flow:**
  - `fibonacci(5)` returns `[0, 1, 1, 2, 3]`.
  - `cube` is applied to each: `cube(0) = 0`, `cube(1) = 1`, `cube(2) = 8`, `cube(3) = 27`.
  - The final output is `[0, 1, 1, 8, 27]`.
- **Output:**
  ```python
  [0, 1, 1, 8, 27]
  ```

This code calculates the first `n` Fibonacci numbers, cubes each of them, and then outputs the list of these cubed numbers.
