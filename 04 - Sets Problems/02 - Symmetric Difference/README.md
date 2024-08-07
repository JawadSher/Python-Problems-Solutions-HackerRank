<h1 align='center'>Symmetric - Difference</h1>

**Problem URL :** [Symmetric Difference](https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true)

## Problem Statement

![image](https://github.com/user-attachments/assets/213a18d2-47f2-48f6-b0d0-3836b7105ac7)
![image](https://github.com/user-attachments/assets/958dfbc1-f0b2-4fd5-abf8-bdb12da21fd7)
![image](https://github.com/user-attachments/assets/533d0aba-fe13-4307-bb9f-50b3b3feb724)
![image](https://github.com/user-attachments/assets/9574c045-d0fe-4067-ba88-537e84f21a70)



## Problem Solution
```python
M = int(input().strip())
A = set(map(int, input().split()))
N = int(input().strip())
B = set(map(int, input().split()))

new_list = []
new_list.extend(A.difference(B))
new_list.extend(B.difference(A))
new_list.sort()

for i in new_list:
    print(i)
```

## Problem Solution Explanation
Let's break down the code line by line:

```python
M = int(input().strip())
```
- `input().strip()` reads a line of input from the user and removes any leading or trailing whitespace (like spaces or newlines). 
- `int()` converts the input string to an integer.
- `M` stores this integer value, which represents the number of elements in set \( A \).

```python
A = set(map(int, input().split()))
```
- `input().split()` reads a line of input from the user and splits it into a list of strings based on spaces.
- `map(int, ...)` converts each string in this list to an integer.
- `set(...)` converts this list of integers into a set, which automatically removes any duplicate values.
- `A` stores this set of integers, which represents the elements of set \( A \).

```python
N = int(input().strip())
```
- Similar to the first line, this reads another integer input from the user and stores it in `N`, which represents the number of elements in set \( B \).

```python
B = set(map(int, input().split()))
```
- This line performs the same operations as the one for set \( A \), but it reads input for set \( B \). It converts the space-separated numbers into a set of integers.

```python
new_list = []
```
- `new_list` is initialized as an empty list. This will be used to store the elements that are unique to each set.

```python
new_list.extend(A.difference(B))
```
- `A.difference(B)` calculates the elements that are in set \( A \) but not in set \( B \).
- `new_list.extend(...)` adds these elements to `new_list`. The `extend` method adds each element of the provided iterable to the list.

```python
new_list.extend(B.difference(A))
```
- `B.difference(A)` calculates the elements that are in set \( B \) but not in set \( A \).
- `new_list.extend(...)` adds these elements to `new_list`.

```python
new_list.sort()
```
- `new_list.sort()` sorts the list `new_list` in ascending order. This is useful for printing the elements in a sorted manner.

```python
for i in new_list:
    print(i)
```
- This loop iterates over each element `i` in `new_list`.
- `print(i)` prints each element on a new line.

### Summary:
The code reads two sets of integers from the user, calculates the unique elements in each set, combines these unique elements into a list, sorts the list, and prints each element in the sorted list.
