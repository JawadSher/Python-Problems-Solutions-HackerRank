<h1 align='center'>Collections - .NamedTuple()</h1>

## Problem Statement

**Problem URL :** [Collections .nameTuple()](https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/baa260a5-ed5a-43a8-b7cc-c172c6ca22d1)
![image](https://github.com/user-attachments/assets/e57de4cf-107b-47e6-b364-7657544974c1)
![image](https://github.com/user-attachments/assets/06653567-6451-41da-9801-455244bdea14)

## Problem Solution
```py
from collections import namedtuple

nums_records = int(input())
Student = namedtuple('Student', input().split())
stdnt_records = [Student(*input().split()) for _ in range(nums_records)]
stdnt_marks = [student.MARKS for student in stdnt_records]
total_marks = sum(map(int, stdnt_marks))
avg_marks = total_marks / nums_records
print(f'{avg_marks:.2f}')
```

## Problem Solution Explanation

Let's break down this code line by line to understand how it works and how it uses `namedtuple` to process student records and compute the average of their marks.

```python
from collections import namedtuple
```
- **Importing `namedtuple`**: This line imports the `namedtuple` function from the `collections` module. `namedtuple` is used to create tuple subclasses with named fields, making it easier to access and manage structured data.

```python
nums_records = int(input())
```
- **Reading the Number of Records**: 
  - **`input()`**: Reads a line of input from the user. This should be a single integer value indicating how many student records will follow.
  - **`int()`**: Converts the input string into an integer.
  - **`nums_records`**: Stores the number of student records to be processed.

```python
Student = namedtuple('Student', input().split())
```
- **Defining the `Student` Namedtuple**:
  - **`input().split()`**: Reads a line of input which should be the column headers, then splits this line into a list of strings based on whitespace. For example, if the input is "MARKS CLASS NAME ID", `input().split()` will return `['MARKS', 'CLASS', 'NAME', 'ID']`.
  - **`namedtuple('Student', ...)`**: Creates a new namedtuple class called `Student` with fields named according to the list of column headers. This allows you to access data using field names like `student.MARKS`, `student.CLASS`, etc.
  - **`Student`**: This is now a class that can be used to create instances representing student records.

```python
stdnt_records = [Student(*input().split()) for _ in range(nums_records)]
```
- **Creating Instances of `Student`**:
  - **`for _ in range(nums_records)`**: This creates a loop that iterates `nums_records` times, once for each student record.
  - **`input().split()`**: Reads a line of input for each student record and splits it into individual components based on whitespace. For example, if the input line is "92 2 Calum 1", `input().split()` will return `['92', '2', 'Calum', '1']`.
  - **`Student(*input().split())`**: Unpacks this list of values and creates a `Student` instance with these values. The `*` operator is used to unpack the list into separate arguments.
  - **`[ ... for _ in range(nums_records)]`**: Collects all the `Student` instances into a list called `stdnt_records`.

```python
stdnt_marks = [student.MARKS for student in stdnt_records]
```
- **Extracting Marks**:
  - **`[student.MARKS for student in stdnt_records]`**: This is a list comprehension that iterates over each `Student` instance in `stdnt_records` and extracts the `MARKS` field from each.
  - **`stdnt_marks`**: This list contains all the marks extracted from the student records.

```python
total_marks = sum(map(int, stdnt_marks))
```
- **Calculating Total Marks**:
  - **`map(int, stdnt_marks)`**: Converts each mark in `stdnt_marks` from a string to an integer.
  - **`sum(...)`**: Sums up all the integer values to get the total marks.
  - **`total_marks`**: Stores the sum of all marks.

```python
avg_marks = total_marks / nums_records
```
- **Calculating the Average Marks**:
  - **`total_marks / nums_records`**: Divides the total marks by the number of records to compute the average.
  - **`avg_marks`**: Stores the calculated average marks.

```python
print(f'{avg_marks:.2f}')
```
- **Printing the Result**:
  - **`f'{avg_marks:.2f}'`**: Formats `avg_marks` to two decimal places. The `:.2f` specifies that the number should be displayed with two decimal places.
  - **`print()`**: Outputs the formatted average marks to the console.

### Summary

- **Define** a namedtuple with fields from the input.
- **Create** instances of this namedtuple using data from the input.
- **Extract** the marks from these instances.
- **Compute** the average of these marks.
- **Print** the average rounded to two decimal places.

This code leverages `namedtuple` to simplify handling structured data and makes the code more readable by using named fields instead of relying on index positions. If you have any more questions or need further clarification, feel free to ask!
