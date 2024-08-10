<h1 align='center'>No - Idea!</h1>

## Problem Statement

**Problem URL :** [No Idea!](https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/f53372fa-39e6-4ea8-8189-d7143d8f6df0)
![image](https://github.com/user-attachments/assets/957e215a-b1f7-4c34-8d58-fa60af74da81)

## Problem Solution
```py
n, m = map(int, input().split())

elements_set = list(map(int, input().split()))

positive_set = set(map(int, input().split()))
negative_set = set(map(int, input().split()))

happiness = 0

for i in elements_set:
    if i in positive_set:
        happiness += 1
    elif i in negative_set:
        happiness -= 1
    
print(happiness)
```

## Problem Solution Explanation

Let's break down the provided code step-by-step and understand its functionality with examples.

1. **Reading Input Values**

   ```python
   n, m = map(int, input().split())
   ```

   - **`n`**: Number of elements in `elements_set`.
   - **`m`**: Number of elements in both `positive_set` and `negative_set`.

   This line reads two integers from the input, separated by a space, and assigns them to `n` and `m`.

2. **Reading `elements_set`**

   ```python
   elements_set = list(map(int, input().split()))
   ```

   - Reads a line of input consisting of `n` integers.
   - Converts the input string into a list of integers using `map(int, ...)` and `list(...)`.

   **Example:**

   If the input is `1 2 3 4`, then `elements_set` will be `[1, 2, 3, 4]`.

3. **Reading `positive_set`**

   ```python
   positive_set = set(map(int, input().split()))
   ```

   - Reads a line of input consisting of `m` integers.
   - Converts the input string into a set of integers.

   **Example:**

   If the input is `1 3 5`, then `positive_set` will be `{1, 3, 5}`.

4. **Reading `negative_set`**

   ```python
   negative_set = set(map(int, input().split()))
   ```

   - Reads a line of input consisting of `m` integers.
   - Converts the input string into a set of integers.

   **Example:**

   If the input is `2 4 6`, then `negative_set` will be `{2, 4, 6}`.

5. **Calculating Happiness**

   ```python
   happiness = 0

   for i in elements_set:
       if i in positive_set:
           happiness += 1
       elif i in negative_set:
           happiness -= 1
   ```

   - **`happiness`**: Initialized to `0`.
   - Iterates through each element `i` in `elements_set`.
   - **If `i` is in `positive_set`**: Increases `happiness` by `1`.
   - **If `i` is in `negative_set`**: Decreases `happiness` by `1`.

   This loop effectively adjusts the `happiness` score based on whether the element is in the positive or negative set.

6. **Printing the Result**

   ```python
   print(happiness)
   ```

   - Outputs the final value of `happiness`.

### Example

Consider the following input:

```
5 3
1 2 3 4 5
1 3 5
2 4 6
```

- **Input Breakdown**:
  - `n = 5` (number of elements in `elements_set`)
  - `m = 3` (number of elements in `positive_set` and `negative_set`)
  - `elements_set = [1, 2, 3, 4, 5]`
  - `positive_set = {1, 3, 5}`
  - `negative_set = {2, 4, 6}`

- **Processing**:
  - `1` (in `positive_set`): `happiness` becomes `1`.
  - `2` (in `negative_set`): `happiness` becomes `0`.
  - `3` (in `positive_set`): `happiness` becomes `1`.
  - `4` (in `negative_set`): `happiness` becomes `0`.
  - `5` (in `positive_set`): `happiness` becomes `1`.

- **Output**:
  ```
  1
  ```

This code calculates a happiness score based on the presence of elements from `elements_set` in `positive_set` and `negative_set`. Positive elements increase the score, while negative elements decrease it.
