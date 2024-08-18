<h1 align='center'>Dealing - With - Complex - Numbers</h1>


## Problem Statement

**Problem URL :** [Dealing with Complex Numbers](https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/28f2afd3-ced1-45d7-b698-6f693f572f28)
![image](https://github.com/user-attachments/assets/74e733ad-0b38-4daa-a91d-d4a9befaa4ce)

## Problem Solution
```py
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)
        
    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)
        
    def __mul__(self, no):
        n1 = complex(self.real, self.imaginary)
        n2 = complex(no.real, no.imaginary)
        result = n1 * n2
        return Complex(result.real, result.imag)

    def __truediv__(self, no):
        n1 = complex(self.real, self.imaginary)
        n2 = complex(no.real, no.imaginary)
        result = n1 / n2
        return Complex(result.real, result.imag)

    def mod(self):
        return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
```

## Problem Solution Explanation

let's go through the code step by step to understand how it works:

### 1. **Class Definition and Initialization**

```python
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
```

- **Imports**: `math` module is imported for mathematical functions, such as square root.
- **`Complex` Class**: Defines a class `Complex` to handle complex numbers.
- **`__init__` Method**: This is the constructor that initializes the `real` and `imaginary` attributes of the complex number.

### 2. **Addition**

```python
def __add__(self, no):
    return Complex(self.real + no.real, self.imaginary + no.imaginary)
```

- **`__add__` Method**: Defines how to add two complex numbers. It creates and returns a new `Complex` object where:
  - The real part is the sum of the real parts of both complex numbers.
  - The imaginary part is the sum of the imaginary parts of both complex numbers.

### 3. **Subtraction**

```python
def __sub__(self, no):
    return Complex(self.real - no.real, self.imaginary - no.imaginary)
```

- **`__sub__` Method**: Defines how to subtract one complex number from another. It creates and returns a new `Complex` object where:
  - The real part is the difference of the real parts.
  - The imaginary part is the difference of the imaginary parts.

### 4. **Multiplication**

```python
def __mul__(self, no):
    n1 = complex(self.real, self.imaginary)
    n2 = complex(no.real, no.imaginary)
    result = n1 * n2
    return Complex(result.real, result.imag)
```

- **`__mul__` Method**: Defines how to multiply two complex numbers using Python's built-in `complex` type.
  - Convert the `Complex` objects to Python’s built-in `complex` type.
  - Perform multiplication.
  - Extract the real and imaginary parts from the result and return a new `Complex` object.

### 5. **Division**

```python
def __truediv__(self, no):
    n1 = complex(self.real, self.imaginary)
    n2 = complex(no.real, no.imaginary)
    result = n1 / n2
    return Complex(result.real, result.imag)
```

- **`__truediv__` Method**: Defines how to divide one complex number by another.
  - Convert the `Complex` objects to Python’s built-in `complex` type.
  - Perform division.
  - Extract the real and imaginary parts from the result and return a new `Complex` object.

### 6. **Modulus**

```python
def mod(self):
    return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)
```

- **`mod` Method**: Computes the modulus (or magnitude) of the complex number.
  - The modulus is calculated using the formula \(\sqrt{a^2 + b^2}\), where `a` is the real part and `b` is the imaginary part.
  - It returns a new `Complex` object with the modulus as the real part and 0 as the imaginary part.

### 7. **String Representation**

```python
def __str__(self):
    if self.imaginary == 0:
        result = "%.2f+0.00i" % (self.real)
    elif self.real == 0:
        if self.imaginary >= 0:
            result = "0.00+%.2fi" % (self.imaginary)
        else:
            result = "0.00-%.2fi" % (abs(self.imaginary))
    elif self.imaginary > 0:
        result = "%.2f+%.2fi" % (self.real, self.imaginary)
    else:
        result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
    return result
```

- **`__str__` Method**: Defines how to convert the complex number to a string.
  - Formats the string representation to show the real and imaginary parts in a specific format.
  - Handles cases where the imaginary part is zero, positive, or negative, ensuring the output is in the required format.

### 8. **Main Program Execution**

```python
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
```

- **Main Block**: This part of the code runs when the script is executed.
  - **Input Handling**: Reads two lines of input, each containing two floating-point numbers, and maps them to `float`.
  - **Creating Complex Numbers**: Initializes two `Complex` objects, `x` and `y`, using the input values.
  - **Printing Results**: Computes the sum, difference, product, and quotient of `x` and `y`, as well as their moduli. Converts the results to strings and prints them, each on a new line.

This code provides a comprehensive implementation of complex number operations, allowing you to work with complex numbers in a structured way.
