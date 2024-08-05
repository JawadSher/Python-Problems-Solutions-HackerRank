<h1 align='center'>Triangle - Quest</h1>

## Problem Statement

**Problem URL :** [Triangle Quest](https://www.hackerrank.com/challenges/python-quest-1/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/cad4dd88-4631-4603-9879-f4721773d0b0)


## Problem Explanation

In the "Triangle Quest" problem, you need to generate a number pattern in the form of a triangle. Each row `i` of the pattern should contain the digit `i` repeated `i` times.

#### Example

For an input of `5`, the output should be:
```
1
22
333
4444
55555
```

### Approach to Solve the Problem

1. **Understand the Pattern**:
   - Each row `i` contains the digit `i` repeated `i` times. 
   - For `i = 1`, the pattern is `1`.
   - For `i = 2`, the pattern is `22`.
   - For `i = 3`, the pattern is `333`, and so on.

2. **Avoid String Manipulation**:
   - Since string manipulation is not allowed, use arithmetic operations to generate the pattern.

3. **Arithmetic Approach**:
   - Use the formula `(10**i - 1) // 9` to generate a number with `i` repeated `1`s.
   - Multiply this result by `i` to repeat the digit `i`, not just `1`.

## Problem Solution
```python
for i in range(1, int(input())):
    print((10**i - 1) // 9 * i)
```

## Problem Solution Explanation

1. **`for i in range(1, int(input())):`**

   - **`int(input())`**: This part takes an input from the user, converts it to an integer, and specifies the end value for the `range` function. The `input()` function reads a line from the user, and `int()` converts it into an integer. For example, if the user inputs `4`, then `int(input())` evaluates to `4`.
   - **`range(1, int(input()))`**: This generates a sequence of integers starting from `1` up to, but not including, the value provided by `int(input())`. For example, if `int(input())` is `4`, `range(1, 4)` generates the sequence `1, 2, 3`.

2. **`print((10**i - 1) // 9 * i)`**

   - **`10**i`**: This calculates `10` raised to the power of `i`. For example, if `i` is `2`, `10**2` equals `100`.
   - **`10**i - 1`**: Subtracting `1` from `10**i` results in a number consisting of `i` nines. For example, if `i` is `2`, `10**2 - 1` equals `99`.
   - **`(10**i - 1) // 9`**: This performs integer division of the previous result by `9`. Since `10**i - 1` is a number consisting of `i` nines, dividing by `9` converts it into a number consisting of `i` ones. For example, `99 // 9` equals `11`.
   - **`(10**i - 1) // 9 * i`**: Finally, this result is multiplied by `i`. For example, if `i` is `2`, the result of `(10**2 - 1) // 9` is `11`, so `11 * 2` equals `22`.

### Example

Let's illustrate this with an example where the user inputs `4`:

- For `i = 1`: 
  - `10**1 - 1` is `9`
  - `9 // 9` is `1`
  - `1 * 1` is `1`
  - The output will be `1`.

- For `i = 2`:
  - `10**2 - 1` is `99`
  - `99 // 9` is `11`
  - `11 * 2` is `22`
  - The output will be `22`.

- For `i = 3`:
  - `10**3 - 1` is `999`
  - `999 // 9` is `111`
  - `111 * 3` is `333`
  - The output will be `333`.

The code prints a sequence of numbers where each number corresponds to the pattern described above, based on the value of `i`.
