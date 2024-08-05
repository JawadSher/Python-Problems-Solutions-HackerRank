<h1 align='center'>Finding - The - Percentage</h1>

## Problem Statement 
**Problem URL : [Finding the Percentage](https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/ae00c9f1-ae16-4c24-8e70-23ab48e4cea3)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/1bd01b3a-aada-4d46-b925-ae27b1472348)

## Problem Solution
```
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    if query_name in student_marks:
        marks = student_marks[query_name]
        average = sum(marks) / len(marks)
        print("{:.2f}".format(average))
```

## Problem Solution Explanation

```python
if __name__ == '__main__':
```
- This line checks if the script is being run directly (not imported as a module). If it is run directly, the code block following this line will be executed.

```python
    n = int(input())
```
- Reads an integer input from the user, converts it to an integer using `int()`, and stores it in the variable `n`. This value represents the number of students and their scores to be processed.

```python
    student_marks = {}
```
- Initializes an empty dictionary `student_marks` to store student names as keys and their respective scores as values.

```python
    for _ in range(n):
```
- Starts a `for` loop that will iterate `n` times, once for each student.

```python
        name, *line = input().split()
```
- Reads a line of input, splits it into individual strings, and assigns the first part to `name` and the remaining parts to `line` using the unpacking feature `name, *line`.
  - `name` will be a string representing the student’s name.
  - `line` will be a list of strings representing the student's scores.

```python
        scores = list(map(float, line))
```
- Converts each score in `line` from a string to a floating-point number using `map(float, line)`, then converts the map object to a list and stores it in the variable `scores`.

```python
        student_marks[name] = scores
```
- Adds an entry to the `student_marks` dictionary where `name` is the key and `scores` is the value.

```python
    query_name = input()
```
- Reads a string input from the user, which is the name of the student whose average score will be queried. The input is stored in the variable `query_name`.

```python
    if query_name in student_marks:
```
- Checks if `query_name` exists in the `student_marks` dictionary.

```python
        marks = student_marks[query_name]
```
- Retrieves the list of scores for the student `query_name` from the dictionary and stores it in the variable `marks`.

```python
        average = sum(marks) / len(marks)
```
- Calculates the average score by summing all scores in `marks` with `sum(marks)` and dividing by the number of scores with `len(marks)`.

```python
        print("{:.2f}".format(average))
```
- Prints the average score formatted to two decimal places. The `"{:.2f}".format(average)` formats the `average` to two decimal places as a string.

### Example
Consider the following input:
```
3
Alice 85.5 90.0 88.0
Bob 78.0 82.5 80.0
Charlie 90.0 95.0 92.0
Bob
```
- `n` will be `3`, indicating there are three students.
- `student_marks` will be `{'Alice': [85.5, 90.0, 88.0], 'Bob': [78.0, 82.5, 80.0], 'Charlie': [90.0, 95.0, 92.0]}`.
- `query_name` will be `'Bob'`.
- The average score for Bob will be `(78.0 + 82.5 + 80.0) / 3 = 80.83`.

The output will be `80.83`.
