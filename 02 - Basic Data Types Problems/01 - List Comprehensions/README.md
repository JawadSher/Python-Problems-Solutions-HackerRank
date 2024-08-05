<h1 align='center'>List - Comprehensions</h1>

## Problem Statement 
**Problem URL : [List Comprehensions](https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/4832db89-cca3-4d22-947c-dafbb4c4d257)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/05f5488c-5261-45b8-9f11-1e56287f8972)

## Problem Solution 
```
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    cuboid_list = [[i, j, k] for i in range(x+1) for j in range(y+1)
                    for k in range(z+1) if(i + j + k) != n]
    print(cuboid_list)
```

## Problem Solution Explanation

Certainly! Here’s a line-by-line explanation of the code:

```python
if __name__ == '__main__':
```
- This line checks if the script is being run directly (as opposed to being imported as a module in another script). If the script is run directly, the code block following this line will be executed.

```python
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
```
- These lines prompt the user to enter four integers, which are then stored in the variables `x`, `y`, `z`, and `n`. The `input()` function reads a line from the user input, and `int()` converts that input to an integer.

```python
    cuboid_list = [[i, j, k] for i in range(x+1) for j in range(y+1)
                    for k in range(z+1) if (i + j + k) != n]
```
- This line creates a list comprehension to generate a list called `cuboid_list`. Let’s break it down:
  - `[[i, j, k] ...]` creates a list of lists where each sublist contains three integers: `i`, `j`, and `k`.
  - `for i in range(x+1)` iterates over all integers from 0 to `x` inclusive.
  - `for j in range(y+1)` iterates over all integers from 0 to `y` inclusive for each value of `i`.
  - `for k in range(z+1)` iterates over all integers from 0 to `z` inclusive for each combination of `i` and `j`.
  - `if (i + j + k) != n` filters out the lists where the sum of `i`, `j`, and `k` is equal to `n`. Only those lists where this sum is not equal to `n` are included in `cuboid_list`.

```python
    print(cuboid_list)
```
- This line prints the `cuboid_list` to the console. It will display the list of lists that meet the criteria specified in the list comprehension.

### Example
If `x = 1`, `y = 1`, `z = 1`, and `n = 2`, the code will generate:
- Possible values for `i`, `j`, and `k` are `[0, 0, 0]`, `[0, 0, 1]`, `[0, 1, 0]`, `[0, 1, 1]`, `[1, 0, 0]`, `[1, 0, 1]`, `[1, 1, 0]`, and `[1, 1, 1]`.
- Excluding lists where `i + j + k` equals `2`, the result will be:
  ```python
  [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
  ```
