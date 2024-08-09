<h1>Set - .Symmetric_difference() - Operation</h1>

## Problem Statement

**Problem URL :** [Set .Symmetric-difference() Operation](https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/90766f66-1ca6-41a0-a9d4-8131c43510ce)
![image](https://github.com/user-attachments/assets/8dd0e6ed-7239-4aa9-aeee-b12b18464a4b)
![image](https://github.com/user-attachments/assets/4562f8fe-740d-47a4-b3c9-241ff6634ccb)


## Problem Solution
```py
student_english = int(input())
roll_nums1 = list(map(int, input().split()))
eng_std_rollnums = set(roll_nums1[::-1])

student_french = int(input())
roll_nums2 = list(map(int, input().split()))
fr_std_rollnums = set(roll_nums2[::-1])

total_subscriptions = eng_std_rollnums ^ fr_std_rollnums
subscriptions_length = len(total_subscriptions)
print(subscriptions_length)
```

## Problem Solution Explanation
Here’s a detailed line-by-line explanation of the provided code:

```python
student_english = int(input())
```
- **Input Reading**: Reads a single line of input from the user, which should be an integer representing the number of students taking English.
- **Conversion**: Converts the input from a string to an integer using `int()`.
- **Assignment**: Stores this integer in the variable `student_english`.

```python
roll_nums1 = list(map(int, input().split()))
```
- **Input Reading**: Reads a line of input from the user, which should contain space-separated roll numbers of students taking English.
- **Splitting**: Uses `split()` to break this input string into individual substrings (each representing a roll number).
- **Conversion**: Uses `map(int, ...)` to convert each substring to an integer.
- **List Creation**: Converts the mapped integers into a list using `list()`, resulting in `roll_nums1`, a list of integers representing the roll numbers of students taking English.

```python
eng_std_rollnums = set(roll_nums1[::-1])
```
- **Reversing**: Uses slicing (`[::-1]`) to reverse the order of `roll_nums1`. This means the last element of the list becomes the first, and so on.
- **Conversion to Set**: Converts the reversed list to a set using `set()`. This removes any duplicate roll numbers and ensures only unique roll numbers are stored in `eng_std_rollnums`.

```python
student_french = int(input())
```
- **Input Reading**: Reads a single line of input from the user, which should be an integer representing the number of students taking French.
- **Conversion**: Converts the input from a string to an integer using `int()`.
- **Assignment**: Stores this integer in the variable `student_french`.

```python
roll_nums2 = list(map(int, input().split()))
```
- **Input Reading**: Reads a line of input from the user, which should contain space-separated roll numbers of students taking French.
- **Splitting**: Uses `split()` to break this input string into individual substrings (each representing a roll number).
- **Conversion**: Uses `map(int, ...)` to convert each substring to an integer.
- **List Creation**: Converts the mapped integers into a list using `list()`, resulting in `roll_nums2`, a list of integers representing the roll numbers of students taking French.

```python
fr_std_rollnums = set(roll_nums2[::-1])
```
- **Reversing**: Uses slicing (`[::-1]`) to reverse the order of `roll_nums2`.
- **Conversion to Set**: Converts the reversed list to a set using `set()`. This removes any duplicate roll numbers and ensures only unique roll numbers are stored in `fr_std_rollnums`.

```python
total_subscriptions = eng_std_rollnums ^ fr_std_rollnums
```
- **Set Symmetric Difference**: Uses the `^` operator to find the symmetric difference between `eng_std_rollnums` and `fr_std_rollnums`. The symmetric difference results in a new set, `total_subscriptions`, containing elements that are in either `eng_std_rollnums` or `fr_std_rollnums` but not in both. In other words, it contains roll numbers that are either in English or French but not in both.

```python
subscriptions_length = len(total_subscriptions)
```
- **Length Calculation**: Uses `len()` to find the number of elements in `total_subscriptions`, which gives the count of unique roll numbers that are in either English or French, but not in both.
- **Assignment**: Stores this count in the variable `subscriptions_length`.

```python
print(subscriptions_length)
```
- **Output**: Prints the value of `subscriptions_length`, representing the number of students enrolled in only one of the two subjects (English or French, but not both).

### Summary
The code calculates and prints the number of students who are enrolled in either English or French, but not in both, by computing the symmetric difference of the two sets of roll numbers.
