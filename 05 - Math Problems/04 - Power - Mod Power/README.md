<h1 align='center'>Power - Mod Power</h1>

## Problem Statement

**Problem URL :** [Power - Mod Power](https://www.hackerrank.com/challenges/python-power-mod-power/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/54ca1ec5-8115-4134-b182-175a2e00a8f7)
![image](https://github.com/user-attachments/assets/5ac6cb41-6c12-4bd7-9e5a-007a80f31c20)


## Problem Explanation

The problem requires you to compute the result of raising a number \( a \) to the power of \( b \) and then taking the result modulo \( m \). Specifically, you need to compute:

result = ((a^b) % m)

Where:
- \( a \) is the base.
- \( b \) is the exponent.
- \( m \) is the modulus.

## Problem Solution

```python
from math import pow

a = int(input().strip())
b = int(input().strip())
m = int(input().strip())

print(int(pow(a,b)))
print(int(pow(a,b) % m))
```


## Problem Solution Explanation

1. **Import `pow` Function:**
   ```python
   from math import pow
   ```
   This imports the `pow` function from the `math` module. The `pow` function in Python can be used to compute \( a^b \) (base raised to the power of exponent) but does not directly support modular arithmetic.

2. **Read Input Values:**
   ```python
   a = int(input().strip())
   b = int(input().strip())
   m = int(input().strip())
   ```
   These lines read three integer inputs from the user. `strip()` is used to remove any leading or trailing whitespace from the input strings before converting them to integers.

   - `a`: The base.
   - `b`: The exponent.
   - `m`: The modulus.

3. **Compute \( a^b \):**
   ```python
   print(int(pow(a,b)))
   ```
   This line calculates \( a^b \) using the `pow` function and prints the result. Note that the `pow` function here does not handle the modulus; it only computes the power. The result of \( a^b \) can be a very large number depending on the values of `a` and `b`.

4. **Compute \( (a^b) \mod m \):**
   ```python
   print(int(pow(a,b) % m))
   ```
   This line first calculates \( a^b \) using the `pow` function, then takes the result modulo `m` to compute \( (a^b) \mod m \). The final result is then printed. 

### Summary

- **Efficiency:** The code uses the `pow` function to compute \( a^b \). However, for large values of \( b \), this can be inefficient due to the large intermediate results.
- **Modular Arithmetic:** The code computes the modulus after calculating the power, which is less efficient than directly computing \( (a^b) \mod m \) using modular exponentiation techniques.

The provided code works correctly but is not optimized for very large values of \( a \) and \( b \) due to the potential size of the intermediate result. For large numbers, the modular exponentiation method is preferred for efficiency.
