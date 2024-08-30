<h1 align='center'>Polynomials</h1>

## Problem Statement

**Problem URL :** [Polynomials](https://www.hackerrank.com/challenges/np-polynomials/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/76523700-87f1-4683-a612-3321c5d29e2a)
![image](https://github.com/user-attachments/assets/1d23010e-9416-4b91-b11a-a94c9be560e5)

## Problem Solution
```py
import numpy as np

P = list(map(float, input().split()))
X = int(input())

print(np.polyval(P, X))
```

## Problem Solution Explanation
Sure! Let's break down the code step by step and explain it in detail with examples.

#### 1. `import numpy as np`
This line imports the NumPy library, which is a powerful library in Python for numerical computing. By importing it as `np`, you can access its functions using the shorter `np` prefix.

#### 2. `P = list(map(float, input().split()))`
This line does the following:

- **`input()`**: This function reads a line of input from the user as a string.
  
- **`.split()`**: After reading the input, this method splits the string into a list of substrings based on whitespace. For example, if the input is `"1.0 2.5 3.6"`, `split()` will convert it into the list `['1.0', '2.5', '3.6']`.

- **`map(float, ...)`**: The `map()` function applies the `float` function to each element in the list of strings. This converts the list of strings into a list of floating-point numbers. Continuing with the example, `['1.0', '2.5', '3.6']` will be converted to `[1.0, 2.5, 3.6]`.

- **`list(...)`**: Finally, the `map` object is converted into a list. So, `P` will be a list of floats.

**Example**:  
If the user input is `"1.0 -2.5 3.6"`, then:
- `input()` reads `"1.0 -2.5 3.6"`.
- `split()` converts it to `['1.0', '-2.5', '3.6']`.
- `map(float, ...)` converts it to `[1.0, -2.5, 3.6]`.
- `list(...)` makes it a list, so `P = [1.0, -2.5, 3.6]`.

#### 3. `X = int(input())`
This line does the following:

- **`input()`**: Reads another line of input from the user, which is expected to be a single integer.

- **`int(...)`**: Converts the string input into an integer.

**Example**:  
If the user input is `"2"`, then:
- `input()` reads `"2"`.
- `int(...)` converts it to `2`, so `X = 2`.

#### 4. `print(np.polyval(P, X))`
This line evaluates the polynomial described by the coefficients in `P` at the value `X`, and then prints the result.

- **`np.polyval(P, X)`**: The `np.polyval` function evaluates a polynomial at specific values. Here, `P` is the list of coefficients of the polynomial, and `X` is the value at which the polynomial is to be evaluated.

The coefficients in `P` represent the polynomial starting from the highest degree down to the constant term. For example, if `P = [1.0, -2.5, 3.6]`, it represents the polynomial:

\[ P(x) = 1.0 \cdot x^2 - 2.5 \cdot x + 3.6 \]

The `np.polyval(P, X)` function then substitutes `X` into this polynomial.

**Example**:  
Continuing with `P = [1.0, -2.5, 3.6]` and `X = 2`, the polynomial is:

\[ P(x) = 1.0 \cdot x^2 - 2.5 \cdot x + 3.6 \]

Substituting `X = 2`:

\[ P(2) = 1.0 \cdot (2)^2 - 2.5 \cdot 2 + 3.6 = 1.0 \cdot 4 - 5.0 + 3.6 = 4 - 5 + 3.6 = 2.6 \]

So, `np.polyval(P, 2)` returns `2.6`, and this value is printed.

### Final Output:
For the inputs `"1.0 -2.5 3.6"` for `P` and `"2"` for `X`, the output will be:
```
2.6
```

This result corresponds to evaluating the polynomial \( 1.0 \cdot x^2 - 2.5 \cdot x + 3.6 \) at \( x = 2 \).
