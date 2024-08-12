<h1 align='center'>Iterables - and - Iterators</h1>

## Problem Statement

**Problem URL :** [Iterables and Iterators](https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/04e58ca1-51e0-4b6c-acee-41ffde50edbe)
![image](https://github.com/user-attachments/assets/ce88befc-cfd8-4a95-be17-a9fe3bbcb080)

## Problem Solution
```py
from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

combine = list(combinations(letters, k))
count = 0

for i in combine:
    if 'a' in i :
        count += 1

print(count/len(combine))
```

## Problem Solution Explanation

Let's break down the code step-by-step with explanations and examples for beginners.

1. **Importing `combinations`**

   ```python
   from itertools import combinations
   ```

   - **`combinations`**: This function generates all possible combinations of a given length from an iterable (like a list).

2. **Reading Input**

   ```python
   n = int(input())
   letters = input().split()
   k = int(input())
   ```

   - **`n`**: The number of elements in the list `letters`. (Although `n` is read, it's not used directly in the code.)
   - **`letters`**: A list of characters input by the user. For example, if the input is `a b c`, `letters` will be `['a', 'b', 'c']`.
   - **`k`**: The length of each combination to be generated. For example, if `k` is `2`, combinations of length 2 will be generated.

3. **Generating Combinations**

   ```python
   combine = list(combinations(letters, k))
   ```

   - **`combinations(letters, k)`**: Generates all possible combinations of length `k` from the list `letters`.
   - **`list(...)`**: Converts the combinations generator into a list of tuples. For instance, with `letters = ['a', 'b', 'c']` and `k = 2`, `combine` will be `[('a', 'b'), ('a', 'c'), ('b', 'c')]`.

4. **Counting Combinations with 'a'**

   ```python
   count = 0

   for i in combine:
       if 'a' in i:
           count += 1
   ```

   - **`count`**: A counter to keep track of how many combinations contain the letter 'a'.
   - **`for i in combine`**: Iterates over each combination in `combine`.
   - **`if 'a' in i`**: Checks if 'a' is present in the current combination `i`.
   - **`count += 1`**: Increments the counter if 'a' is found in the combination.

5. **Calculating and Printing the Result**

   ```python
   print(count / len(combine))
   ```

   - **`len(combine)`**: The total number of combinations.
   - **`count / len(combine)`**: Computes the proportion of combinations that contain the letter 'a'.
   - **`print(...)`**: Displays the result.

### Example

#### Input

```
3
a b c
2
```

#### Output

```
0.6666666666666666
```

#### How It Works

1. **Generate Combinations**:
   - With `letters = ['a', 'b', 'c']` and `k = 2`, the combinations are:
     - `('a', 'b')`
     - `('a', 'c')`
     - `('b', 'c')`

2. **Count Combinations Containing 'a'**:
   - `('a', 'b')` contains 'a'.
   - `('a', 'c')` contains 'a'.
   - `('b', 'c')` does not contain 'a'.

   So, 2 out of 3 combinations contain 'a'.

3. **Calculate Proportion**:
   - Proportion of combinations containing 'a' is `2 / 3 ≈ 0.6667`.

   The code outputs `0.6666666666666666`, which represents the proportion of combinations containing the letter 'a'.
