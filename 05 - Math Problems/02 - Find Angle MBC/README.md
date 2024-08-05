<h1 align='center'>Find - Angle - MBC</h1>

## Problem Statement

**Problem URL :** [Find Angle MBC](https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/e6e2c212-7aad-4f13-b79b-c62a915a0e7b)
![image](https://github.com/user-attachments/assets/2e76bc78-104e-429b-b5e4-563f58a9ecdd)
![image](https://github.com/user-attachments/assets/4ed677c3-856f-48c9-9db5-a5f4438ed34b)

## Problem Explanation

Sure! Let’s break down the problem statement and the solution step-by-step.

### Problem Statement: "Find angle MBC"

**Objective:**
Given a right-angled triangle where the lengths of the two perpendicular sides (AB and BC) are provided, find the measure of angle MBC (the angle between the side BC and the hypotenuse AC) in degrees.

### How to Find the Angle

1. **Identify the Triangle:**
   - We have a right-angled triangle ABC with:
     - AB and BC as the perpendicular sides.
     - AC as the hypotenuse.

2. **Calculate the Hypotenuse (AC):**
   - Use the Pythagorean theorem to find the hypotenuse:
     \[
     AC = \sqrt{AB^2 + BC^2}
     \]

3. **Find the Angle MBC:**
   - We need to find the angle MBC which is opposite the side BC and adjacent to the hypotenuse AC.
   - The angle can be found using trigonometric functions. Specifically, you can use the inverse cosine function (arccos) since you know the adjacent side (BC) and hypotenuse (AC).

   The formula for the angle MBC in radians is:
   \[
   \text{angle} = \arccos\left(\frac{BC}{AC}\right)
   \]
   - Convert the angle from radians to degrees using:
     \[
     \text{angle (degrees)} = \text{math.degrees}(\text{angle (radians)})
     \]

## Problem Solution
```
import math

AB = int(input().strip())
BC = int(input().strip())

AC = math.sqrt(AB**2 + BC**2)
BM = AC / 2
angle = math.acos(BC / (2 * BM))
angle = math.degrees(angle)
print(round(angle), chr(176), sep='')

```

## Problem Solution Explanation

```python
import math
```
- **Imports the math module**, which provides access to mathematical functions and constants. This is necessary for functions like `sqrt`, `acos`, and `degrees`.

```python
AB = int(input().strip())
BC = int(input().strip())
```
- **Reads two integer inputs** from the user. The `input().strip()` part removes any leading or trailing whitespace from the input string. `int()` converts the cleaned input string into an integer.
  - `AB` is the length of one perpendicular side of the right-angled triangle.
  - `BC` is the length of the other perpendicular side.

```python
AC = math.sqrt(AB**2 + BC**2)
```
- **Calculates the hypotenuse (AC)** of the right-angled triangle using the Pythagorean theorem. `AB**2` and `BC**2` are squared values of the sides, and their sum is then square-rooted to find the hypotenuse.

```python
BM = AC / 2
```
- **Calculates the midpoint (BM)** of the hypotenuse AC. However, this step is unnecessary for finding the angle MBC and might be incorrect or misplaced in the context of this problem.

```python
angle = math.acos(BC / (2 * BM))
```
- **Calculates the angle MBC in radians** using the `acos` function, which computes the arccosine of a value. The argument `BC / (2 * BM)` seems incorrect for calculating the angle. The correct argument should be `BC / AC` for finding the angle between BC and the hypotenuse AC.

```python
angle = math.degrees(angle)
```
- **Converts the angle from radians to degrees** using `math.degrees()`. This is necessary because trigonometric functions in Python typically return angles in radians, and we need the angle in degrees for the output.

```python
print(round(angle), chr(176), sep='')
```
- **Prints the angle** rounded to the nearest integer with the degree symbol (°) appended. `chr(176)` is used to insert the degree symbol, but if non-ASCII characters are not allowed, this might need to be replaced or omitted. The `sep=''` parameter ensures there is no space between the rounded angle and the degree symbol.

### Summary
The code reads the lengths of two sides of a right-angled triangle, calculates the hypotenuse, attempts to compute the angle (although incorrectly), converts the angle to degrees, and prints it with a degree symbol.

