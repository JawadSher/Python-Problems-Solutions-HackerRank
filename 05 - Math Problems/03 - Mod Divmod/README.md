<h1 align='center'>Mod - Divmod</h1>

## Problem Statement

**Problem URL :** [Mod Divmod](https://www.hackerrank.com/challenges/python-mod-divmod/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/553bee6a-dc13-46b1-9e80-1b38309b589a)

## Problem Solution

```
a = int(input().strip())
b = int(input().strip())

print(a//b)
print(a%b)
print(divmod(a, b))
```

## Problem Solution Explanation

Here's a line-by-line explanation of the given code:

```python
a = int(input().strip())
b = int(input().strip())
```
- `input().strip()`: Reads a line of input from the user, and `strip()` removes any leading or trailing whitespace (like spaces or newline characters).
- `int(...)`: Converts the input string to an integer.
- `a = int(input().strip())`: Reads the first line of input, removes any extra spaces, converts it to an integer, and assigns it to variable `a`.
- `b = int(input().strip())`: Reads the second line of input, removes any extra spaces, converts it to an integer, and assigns it to variable `b`.

```python
print(a//b)
```
- `a // b`: Performs integer (floor) division of `a` by `b`. This means it divides `a` by `b` and rounds down to the nearest integer.
- `print(...)`: Outputs the result of the integer division.

```python
print(a%b)
```
- `a % b`: Computes the remainder when `a` is divided by `b`. This is known as the modulus operation.
- `print(...)`: Outputs the remainder.

```python
print(divmod(a, b))
```
- `divmod(a, b)`: Returns a tuple `(q, r)`, where `q` is the quotient (result of integer division) and `r` is the remainder.
- `print(...)`: Outputs the tuple containing the quotient and remainder.

In summary, this code reads two integers from the user, performs integer division and modulus operations, and then uses the `divmod` function to display both results together.
