<h1 align='center'>Set - .Difference() - Operation</h1>

## Problem Statement

**Problem URL :** [Set .Difference() Operation](https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/8856c6bc-d31d-4f4f-a393-5c607ef17890)
![image](https://github.com/user-attachments/assets/e611136b-04ed-4908-bb24-ffedbb979146)
![image](https://github.com/user-attachments/assets/45f1aaec-05bb-46ff-8519-5758b2345c3d)


## Problem Solution
```py
student_english = int(input())
roll_nums1 = list(map(int, input().split()))
eng_std_rollnums = set(roll_nums1[::-1])

student_french = int(input())
roll_nums2 = list(map(int, input().split()))
fr_std_rollnums = set(roll_nums2[::-1])

total_subscriptions = eng_std_rollnums - fr_std_rollnums
subscriptions_length = len(total_subscriptions)
print(subscriptions_length)
```

## Problem Solution Explanation

Here’s a detailed line-by-line explanation of the code:

```python
student_english = int(input())
```
- **Input Reading**: Reads a single line of input from the user, which is expected to be an integer representing the number of students taking English.
- **Conversion**: Converts the input (which is a string by default) to an integer using `int()`.
- **Assignment**: Stores this integer value in the variable `student_english`.

```python
roll_nums1 = list(map(int, input().split()))
```
- **Input Reading**: Reads a line of input from the user. This line should contain space-separated roll numbers of students taking English.
- **Splitting**: Uses `split()` to break the input string into individual substrings (representing roll numbers).
- **Conversion**: Uses `map(int, ...)` to convert each substring to an integer.
- **List Creation**: Converts the result of `map()` to a list using `list()`, resulting in a list of integers that represents the roll numbers of students taking English. This list is stored in `roll_nums1`.

```python
eng_std_rollnums = set(roll_nums1[::-1])
```
- **Reversing**: Reverses the `roll_nums1` list using slicing (`[::-1]`). This changes the order of the roll numbers in the list.
- **Conversion to Set**: Converts the reversed list to a set using `set()`. This removes any duplicate roll numbers and ensures that only unique roll numbers are included in `eng_std_rollnums`.

```python
student_french = int(input())
```
- **Input Reading**: Reads a single line of input from the user, which is expected to be an integer representing the number of students taking French.
- **Conversion**: Converts the input string to an integer using `int()`.
- **Assignment**: Stores this integer value in the variable `student_french`.

```python
roll_nums2 = list(map(int, input().split()))
```
- **Input Reading**: Reads a line of input from the user. This line should contain space-separated roll numbers of students taking French.
- **Splitting**: Uses `split()` to break the input string into individual substrings (representing roll numbers).
- **Conversion**: Uses `map(int, ...)` to convert each substring to an integer.
- **List Creation**: Converts the result of `map()` to a list using `list()`, resulting in a list of integers that represents the roll numbers of students taking French. This list is stored in `roll_nums2`.

```python
fr_std_rollnums = set(roll_nums2[::-1])
```
- **Reversing**: Reverses the `roll_nums2` list using slicing (`[::-1]`). This changes the order of the roll numbers in the list.
- **Conversion to Set**: Converts the reversed list to a set using `set()`. This removes any duplicate roll numbers and ensures that only unique roll numbers are included in `fr_std_rollnums`.

```python
total_subscriptions = eng_std_rollnums - fr_std_rollnums
```
- **Set Difference**: Uses the `-` operator to find the difference between the two sets, `eng_std_rollnums` and `fr_std_rollnums`. This operation results in a new set, `total_subscriptions`, containing only the roll numbers that are in `eng_std_rollnums` but not in `fr_std_rollnums`. In other words, it finds the roll numbers of students who are only taking English but not French.

```python
subscriptions_length = len(total_subscriptions)
```
- **Length Calculation**: Uses `len()` to determine the number of elements in the `total_subscriptions` set. This gives the count of unique roll numbers of students who are taking English but not French.
- **Assignment**: Stores this count in the variable `subscriptions_length`.

```python
print(subscriptions_length)
```
- **Output**: Prints the value of `subscriptions_length`, which represents the number of students who are enrolled in English but not in French.

### Summary
The code reads the roll numbers of students taking English and French, computes the number of students who are enrolled only in English (and not in French), and prints this count.
