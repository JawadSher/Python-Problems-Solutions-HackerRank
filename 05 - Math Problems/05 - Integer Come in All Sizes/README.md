<h1 align='center'>Integer - Come - In - All - Sizes</h1>

## Problem Statement

**Problem URL :** [Integer Come In All Sizes](https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/960377b0-5354-4ae3-bd7a-1b4de400fc22)


## Problem Explanation

In this HackerRank problem, you're given four integers `a`, `b`, `c`, and `d`. The task is to calculate and output the result of the expression:

result = a^b + c^d

where `^` denotes the power operation (i.e., raising a number to the power of another number).

Python's `int` type can handle arbitrarily large integers, so you don't have to worry about integer overflow issues. Your job is to read the integers from input, compute the result of the expression, and print it.



## Problem Solution
```
a = int(input().strip())
b = int(input().strip())
c = int(input().strip())
d = int(input().strip())

print((a**b) + (c**d))

```

## Problem Solution Explanation

1. **`a = int(input().strip())`**:
   - `input()`: Reads a line of input from the user.
   - `.strip()`: Removes any leading or trailing whitespace characters from the input string.
   - `int()`: Converts the cleaned string to an integer.
   - `a`: Stores the integer value read from the input.

2. **`b = int(input().strip())`**:
   - Similar to the first line, this reads the next integer input from the user, removes whitespace, converts it to an integer, and stores it in `b`.

3. **`c = int(input().strip())`**:
   - Reads the third integer input, cleans it, converts it to an integer, and stores it in `c`.

4. **`d = int(input().strip())`**:
   - Reads the fourth integer input, cleans it, converts it to an integer, and stores it in `d`.

```python
print((a**b) + (c**d))
```

5. **`(a**b) + (c**d)`**:
   - `a**b`: Computes `a` raised to the power of `b`.
   - `c**d`: Computes `c` raised to the power of `d`.
   - The `+` operator adds the two results together.

6. **`print()`**:
   - Outputs the result of the expression to the standard output.

In summary, the code reads four integers from the input, computes the sum of two power operations, and prints the result.
