# Problem Statement

**Problem URL :** [Polar Coordinates](https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/dcf20df5-4491-44ac-bcd7-4f34378a7ffa)
![image](https://github.com/user-attachments/assets/e7c26aff-0bf7-4fdb-a288-cfcc32d4e52c)
![image](https://github.com/user-attachments/assets/2e7d03c1-e7bf-492f-8bb7-1a05d5244918)

### Problem Explanation

Given a complex number in the form of a string, your task is to:
1. Convert the complex number from its rectangular form (a + bi) into its polar form.
2. Output the magnitude (radius) and the phase (angle) of the complex number.

### Steps to Solve

1. **Input Handling**: 
   - Read the complex number input as a string.
   - Convert this string into a complex number using Python's `complex()` function.

2. **Conversion to Polar Coordinates**:
   - Compute the magnitude using `cmath.polar()`, which returns a tuple of the magnitude and phase.
   - The magnitude is the distance from the origin, and the phase is the angle with the positive real axis.

3. **Output**:
   - Print the magnitude and phase separately.

### Example

#### Input
```
1+2j
```

#### Output
```
2.23606797749979
1.1071487177940904
```

### Explanation

1. **Convert to Complex Number**:
   - `1+2j` is converted to the complex number `1 + 2i`.

2. **Compute Polar Coordinates**:
   - **Magnitude**: \( \sqrt{1^2 + 2^2} \approx 2.236 \)
   - **Phase**: The angle \( \arctan(\frac{2}{1}) \approx 1.107 \) radians

3. **Print Results**:
   - Print the magnitude and phase.
     

## Problem Solution 

```python
import cmath

# Read the input complex number as a string
z = input().strip()

# Convert the string to a complex number
c = complex(z)

# Compute the magnitude and phase using cmath.polar
magnitude, phase = cmath.polar(c)

# Print the results
print(magnitude)
print(phase)
```

## Problem Solution Explanation
### 1. Importing the `cmath` Module

```python
import cmath
```
- **Purpose**: Imports the `cmath` module, which provides mathematical functions for complex numbers. Functions in this module are used for operations such as computing magnitudes, phases, and other complex number-related computations.

### 2. Reading Input

```python
z = input().strip()
```
- **Purpose**: Reads a line of input from the user and removes any leading or trailing whitespace using `.strip()`. This input should be a complex number in string format (e.g., `"1+2j"`).

### 3. Converting to a Complex Number

```python
c = complex(z)
```
- **Purpose**: Converts the input string `z` into a complex number object. For instance, if the input string is `"1+2j"`, the `complex()` function converts it into a complex number `1 + 2j`. 

### 4. Computing Magnitude and Phase

```python
magnitude, phase = cmath.polar(c)
```
- **Purpose**: Converts the complex number `c` from its rectangular form (a + bi) to its polar coordinates.
- **`cmath.polar(c)`**: This function returns a tuple containing two values:
  - **Magnitude**: The distance from the origin to the point in the complex plane.
  - **Phase**: The angle between the positive real axis and the line connecting the origin to the point, measured in radians.

### 5. Printing Results

```python
print(magnitude)
print(phase)
```
- **Purpose**: Prints the magnitude and phase of the complex number. The `magnitude` is printed first, followed by the `phase`.

### Example Walkthrough

**Input**: `"1+2j"`

1. **Conversion**:
   - `c = complex("1+2j")` results in `c` being the complex number `1 + 2j`.

2. **Polar Coordinates**:
   - **Magnitude**: Computed as \(\sqrt{1^2 + 2^2} \approx 2.236\).
   - **Phase**: Computed as \(\arctan\left(\frac{2}{1}\right) \approx 1.107\) radians.

3. **Output**:
   - The code prints:
     ```
     2.23606797749979
     1.1071487177940904
     ```
   - The first line is the magnitude, and the second line is the phase.

This code effectively converts a complex number from its standard form to its polar form and prints the two polar coordinates.
