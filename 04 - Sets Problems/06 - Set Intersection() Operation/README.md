<h1 align='center'>Set - .Intersection() - Operation</h1>

## Problem Statement

**Problem URL :** [Set .Intersection() Operation](https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/87e27d90-de5b-4992-b600-7e5bd4cea79a)
![image](https://github.com/user-attachments/assets/9fd08325-d770-4172-b835-36de712e6d33)
![image](https://github.com/user-attachments/assets/150aabb4-a014-4306-b6e8-1dd53932d084)


## Problem Solution
```py
student_english = int(input())
roll_nums1 = list(map(int, input().split()))
eng_std_rollnums = set(roll_nums1[::-1])

student_french = int(input())
roll_nums2 = list(map(int, input().split()))
fr_std_rollnums = set(roll_nums2[::-1])

total_subscriptions = eng_std_rollnums & fr_std_rollnums
subscriptions_length = len(total_subscriptions)
print(subscriptions_length)
```

## Problem Solution Explanation
Let’s break down this code line by line:

```python
student_english = int(input())
```
- **Input Reading**: Reads a single line of input from the user, which should be an integer representing the number of students taking English.
- **Conversion**: Converts the input string to an integer using `int()`.
- **Assignment**: Stores this integer in the variable `student_english`.

```python
roll_nums1 = list(map(int, input().split()))
```
- **Input Reading**: Reads a line of input from the user, which is expected to contain space-separated roll numbers of students taking English.
- **Splitting**: Uses `split()` to split this input string into individual substrings (roll numbers).
- **Conversion**: Uses `map(int, ...)` to convert each substring to an integer.
- **List Creation**: Converts the result from `map()` to a list using `list()`, which results in a list of integers stored in `roll_nums1`.

```python
eng_std_rollnums = set(roll_nums1[::-1])
```
- **Reversing**: Uses slicing (`[::-1]`) to reverse the `roll_nums1` list. This means the last roll number in the original list will be the first one in the reversed list, and so on.
- **Conversion to Set**: Converts the reversed list to a set using `set()`. This removes any duplicate roll numbers and ensures that only unique roll numbers are stored in `eng_std_rollnums`.

```python
student_french = int(input())
```
- **Input Reading**: Reads a single line of input from the user, which should be an integer representing the number of students taking French.
- **Conversion**: Converts this input string to an integer using `int()`.
- **Assignment**: Stores this integer in the variable `student_french`.

```python
roll_nums2 = list(map(int, input().split()))
```
- **Input Reading**: Reads a line of input from the user, which is expected to contain space-separated roll numbers of students taking French.
- **Splitting**: Uses `split()` to divide this input string into individual substrings (roll numbers).
- **Conversion**: Uses `map(int, ...)` to convert each substring to an integer.
- **List Creation**: Converts the result from `map()` to a list using `list()`, resulting in a list of integers stored in `roll_nums2`.

```python
fr_std_rollnums = set(roll_nums2[::-1])
```
- **Reversing**: Uses slicing (`[::-1]`) to reverse the `roll_nums2` list. This reverses the order of roll numbers in the list.
- **Conversion to Set**: Converts the reversed list to a set using `set()`. This removes any duplicate roll numbers and ensures that only unique roll numbers are stored in `fr_std_rollnums`.

```python
total_subscriptions = eng_std_rollnums & fr_std_rollnums
```
- **Set Intersection**: Uses the `&` operator to find the intersection between the two sets, `eng_std_rollnums` and `fr_std_rollnums`. This results in a new set, `total_subscriptions`, containing only the roll numbers that are present in both the English and French sets.

```python
subscriptions_length = len(total_subscriptions)
```
- **Length Calculation**: Uses `len()` to calculate the number of elements in the `total_subscriptions` set. This gives the count of unique roll numbers that are common to both English and French subscriptions.
- **Assignment**: Stores this count in the variable `subscriptions_length`.

```python
print(subscriptions_length)
```
- **Output**: Prints the value of `subscriptions_length`, which represents the number of students enrolled in both English and French.

### Summary
The code calculates the number of students who are enrolled in both English and French classes by finding the intersection of their roll numbers and prints the count of these common roll numbers.
