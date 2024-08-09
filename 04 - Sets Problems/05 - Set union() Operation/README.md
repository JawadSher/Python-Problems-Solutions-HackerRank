<h1 align='center'>Set - .Union() - Operation</h1>

## Problem Statement

**Problem URL :** [Set .Union() Operation](https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/fa18745c-5c8a-4e11-a354-bf40383a2426)
![image](https://github.com/user-attachments/assets/0b0d459e-28fc-4f74-8472-a3bd82a502b9)
![image](https://github.com/user-attachments/assets/aa80ec32-b399-408a-b51f-b1d6405e944f)

## Problem Solution
```py
student_english = int(input())
roll_nums1 = list(map(int, input().split()))
eng_std_rollnums = set(roll_nums1[::-1])

student_french = int(input())
roll_nums2 = list(map(int, input().split()))
fr_std_rollnums = set(roll_nums2[::-1])

total_subscriptions = eng_std_rollnums | fr_std_rollnums
subscriptions_length = len(total_subscriptions)
print(subscriptions_length)
```

## Problem Solution Explanation
Here's a detailed explanation of each line of the code:

```python
student_english = int(input())
```
- **Input Reading**: Reads a single line of input from the user. This line is expected to be an integer value representing the number of students taking English.
- **Conversion**: Converts the input (which is a string by default) to an integer using `int()`.
- **Assignment**: Stores this integer in the variable `student_english`.

```python
roll_nums1 = list(map(int, input().split()))
```
- **Input Reading**: Reads a line of input from the user, which is expected to contain space-separated roll numbers of students taking English.
- **Splitting**: Uses `split()` to break this input string into individual substrings (roll numbers).
- **Conversion**: Applies `map(int, ...)` to convert each substring to an integer.
- **List Creation**: Converts the result of `map()` to a list using `list()`, resulting in a list of integers stored in `roll_nums1`.

```python
eng_std_rollnums = set(roll_nums1[::-1])
```
- **Reversing**: Uses slicing (`[::-1]`) to reverse the `roll_nums1` list. This means the last roll number will come first, and so on.
- **Conversion to Set**: Converts the reversed list to a set using `set()`. This removes any duplicate roll numbers and ensures that the roll numbers are stored as unique values in `eng_std_rollnums`.

```python
student_french = int(input())
```
- **Input Reading**: Reads a single line of input from the user, which is expected to be an integer representing the number of students taking French.
- **Conversion**: Converts this input (which is a string) to an integer using `int()`.
- **Assignment**: Stores this integer in the variable `student_french`.

```python
roll_nums2 = list(map(int, input().split()))
```
- **Input Reading**: Reads a line of input from the user, which is expected to contain space-separated roll numbers of students taking French.
- **Splitting**: Uses `split()` to break this input string into individual substrings (roll numbers).
- **Conversion**: Applies `map(int, ...)` to convert each substring to an integer.
- **List Creation**: Converts the result of `map()` to a list using `list()`, resulting in a list of integers stored in `roll_nums2`.

```python
fr_std_rollnums = set(roll_nums2[::-1])
```
- **Reversing**: Uses slicing (`[::-1]`) to reverse the `roll_nums2` list.
- **Conversion to Set**: Converts the reversed list to a set using `set()`. This removes any duplicate roll numbers and ensures that the roll numbers are stored as unique values in `fr_std_rollnums`.

```python
total_subscriptions = eng_std_rollnums | fr_std_rollnums
```
- **Set Union**: Uses the `|` operator to perform a union operation between `eng_std_rollnums` and `fr_std_rollnums`. This combines all unique roll numbers from both sets into a new set, `total_subscriptions`.

```python
subscriptions_length = len(total_subscriptions)
```
- **Length Calculation**: Uses `len()` to calculate the number of elements in the `total_subscriptions` set. This gives the count of unique students who are subscribed to either English or French (or both).
- **Assignment**: Stores this count in the variable `subscriptions_length`.

```python
print(subscriptions_length)
```
- **Output**: Prints the value of `subscriptions_length`, which represents the total number of unique students across both English and French subscriptions.

Overall, the code calculates and prints the total number of unique students taking either English or French by processing and combining roll numbers from two sets of students.
