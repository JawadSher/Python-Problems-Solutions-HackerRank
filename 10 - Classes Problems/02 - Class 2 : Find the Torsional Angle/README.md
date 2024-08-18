<h1 align='center'>Find - The - Torsional - Angle</h1>

## Problem Statement

**Problem URL :** [Find The Torsional Angle](https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/9112c7f7-83e2-496d-8607-8b5992d83e7f)


## Problem Explanation

You need to compute the dihedral angle between two planes defined by four points in 3D space. The dihedral angle is the angle between the planes that intersect along a common line.

**How to Find the Dihedral Angle:**
1. **Define Two Planes:**
   - You have four points: \( A, B, C, \) and \( D \).
   - The first plane is defined by the points \( A, B, \) and \( C \).
   - The second plane is defined by the points \( B, C, \) and \( D \).

2. **Find the Normals to the Planes:**
   - The normal vector to a plane is perpendicular to the plane. For each plane, you need to find its normal vector.

3. **Compute the Angle Between the Normals:**
   - The angle between the two normals gives the dihedral angle between the planes.

## Problem Solution
```py
import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z

    def cross(self, no):
        return Points(
            self.y * no.z - self.z * no.y,
            self.z * no.x - self.x * no.z,
            self.x * no.y - self.y * no.x
        )
        
    def absolute(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
```

## Problem Solution Explanation

let's break down the code line by line with explanations and examples to make it easy to understand.

```python
import math
```

- **Explanation:** Import the `math` module to use mathematical functions like square root and trigonometric functions.

```python
class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
```

- **Explanation:** Define a class `Points` to represent a point in 3D space. The `__init__` method initializes the point with \(x\), \(y\), and \(z\) coordinates.

**Example:**
```python
p = Points(1, 2, 3)
```
- This creates a point at coordinates (1, 2, 3).

```python
    def __sub__(self, no):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)
```

- **Explanation:** Define the `__sub__` method to subtract one point from another, resulting in a vector. This vector represents the direction and magnitude from one point to another.

**Example:**
```python
p1 = Points(1, 2, 3)
p2 = Points(4, 5, 6)
v = p2 - p1
```
- **`v`** will be a vector with coordinates (3, 3, 3).

```python
    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z
```

- **Explanation:** Define the `dot` method to compute the dot product of two vectors. The dot product helps in finding the angle between vectors.

**Example:**
```python
v1 = Points(1, 2, 3)
v2 = Points(4, 5, 6)
dp = v1.dot(v2)
```
- **`dp`** will be 1*4 + 2*5 + 3*6 = 32.

```python
    def cross(self, no):
        return Points(
            self.y * no.z - self.z * no.y,
            self.z * no.x - self.x * no.z,
            self.x * no.y - self.y * no.x
        )
```

- **Explanation:** Define the `cross` method to compute the cross product of two vectors. The cross product gives a vector that is perpendicular to both original vectors.

**Example:**
```python
v1 = Points(1, 2, 3)
v2 = Points(4, 5, 6)
cp = v1.cross(v2)
```
- **`cp`** will be a vector (-3, 6, -3).

```python
    def absolute(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
```

- **Explanation:** Define the `absolute` method to compute the magnitude (length) of the vector.

**Example:**
```python
v = Points(3, 4, 0)
mag = v.absolute()
```
- **`mag`** will be √(3² + 4²) = 5.

```python
if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)
```

- **Explanation:** In the main block of the code, read input for four points. Each point is a list of three floating-point numbers representing coordinates. This loop reads four lines of input.

**Example Input:**
```
1 2 3
4 5 6
7 8 9
10 11 12
```
- **`points`** will be a list of four lists: `[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]`.

```python
    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
```

- **Explanation:** Create `Points` objects for each of the four points from the input data.

**Example:**
```python
a = Points(1, 2, 3)
b = Points(4, 5, 6)
c = Points(7, 8, 9)
d = Points(10, 11, 12)
```

```python
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
```

- **Explanation:** Calculate the normal vectors to the planes defined by the points:
  - **Plane 1 (ABC):** Compute the cross product of vectors \( \overrightarrow{AB} \) and \( \overrightarrow{BC} \).
  - **Plane 2 (BCD):** Compute the cross product of vectors \( \overrightarrow{BC} \) and \( \overrightarrow{CD} \).

**Example:**
- Vector \( \overrightarrow{AB} \) = (3, 3, 3)
- Vector \( \overrightarrow{BC} \) = (3, 3, 3)
- Cross product \( x \) = (0, 0, 0) (which means no plane is defined properly here as the points are collinear in this example).

```python
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))
```

- **Explanation:** Compute the angle between the two normal vectors using the dot product and magnitudes. The formula used is:
  \[
  \text{angle} = \cos^{-1}\left(\frac{\text{dot product of } x \text{ and } y}{\text{magnitude of } x \times \text{magnitude of } y}\right)
  \]

**Example:**
- Assuming `x` and `y` are vectors representing the planes' normals.

```python
    print("%.2f" % math.degrees(angle))
```

- **Explanation:** Convert the angle from radians to degrees and print it, formatted to two decimal places.

**Example Output:**
- **`angle`** might be, for example, 90.00 if the planes are perpendicular.

### Summary

This code computes the dihedral angle between two planes in 3D space defined by four points. It involves vector operations (subtraction, dot product, cross product) to determine the normal vectors of the planes and then calculates the angle between these normal vectors.


