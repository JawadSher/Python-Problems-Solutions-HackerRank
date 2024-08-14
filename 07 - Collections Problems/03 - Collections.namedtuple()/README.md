<h1 align='center'>Collections - .NamedTuple()</h1>

## Problem Statement

**Problem URL :** [Collections .nameTuple()](https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/baa260a5-ed5a-43a8-b7cc-c172c6ca22d1)
![image](https://github.com/user-attachments/assets/e57de4cf-107b-47e6-b364-7657544974c1)
![image](https://github.com/user-attachments/assets/06653567-6451-41da-9801-455244bdea14)

## Problem Solution
```py
nums_records = int(input().strip())
header = input().split()

header_index = header.index("MARKS")
marks = [int(input().split()[header_index]) for _ in range(nums_records)]
avg_marks = sum(marks) / nums_records
print(f'{avg_marks:.2f}')
```

## Problem Solution Explanation

Let's break down this code step by step. This code is used to calculate the average of the "MARKS" column from a set of student records.

```python
nums_records = int(input().strip())
```
- **`input().strip()`**: Reads a line of input from the user and removes any leading or trailing whitespace (like spaces or newlines). This ensures clean input.
- **`int()`**: Converts the cleaned input (a string) into an integer.
- **`nums_records`**: Stores the number of student records (or rows) you will process.

```python
header = input().split()
```
- **`input()`**: Reads the next line of input, which contains the column headers.
- **`split()`**: Splits this line into individual strings based on whitespace (spaces). This creates a list where each element corresponds to a column name.
- **`header`**: Stores this list of column names.

```python
header_index = header.index("MARKS")
```
- **`header.index("MARKS")`**: Finds the position (index) of the column name "MARKS" in the `header` list. This tells you where the "MARKS" column is located in the subsequent data lines.
- **`header_index`**: Stores this index value.

```python
marks = [int(input().split()[header_index]) for _ in range(nums_records)]
```
- **`[int(input().split()[header_index]) for _ in range(nums_records)]`**: This is a list comprehension, which creates a list by iterating over a range of `nums_records` times.
    - **`for _ in range(nums_records)`**: Repeats the process `nums_records` times (once for each record).
    - **`input()`**: Reads a line of input for each record.
    - **`split()`**: Splits the input line into a list of values (columns).
    - **`[header_index]`**: Accesses the value at the position of the "MARKS" column in this list.
    - **`int()`**: Converts this value to an integer.
- **`marks`**: Stores a list of integers, where each integer is the mark for one record.

```python
avg_marks = sum(marks) / nums_records
```
- **`sum(marks)`**: Calculates the total sum of all the marks in the `marks` list.
- **`/ nums_records`**: Divides this total by the number of records to compute the average.
- **`avg_marks`**: Stores the calculated average of the marks.

```python
print(f'{avg_marks:.2f}')
```
- **`f'{avg_marks:.2f}'`**: This is an f-string that formats `avg_marks` to two decimal places. The `:.2f` specifies that the number should be formatted as a floating-point number with two decimal places.
- **`print()`**: Outputs the formatted average to the console.

### Summary

1. **Read the number of records**: The first input tells you how many records (or lines) you will process.
2. **Read and process the header**: The second input line contains column names, from which you find the index of the "MARKS" column.
3. **Extract marks**: For each record, you read the line, extract the mark based on the index, and convert it to an integer.
4. **Calculate the average**: Sum all the marks and divide by the number of records to find the average.
5. **Print the average**: Display the average, formatted to two decimal places.

This approach ensures that you accurately compute and display the average of the marks from the provided data. If you have further questions or need more details, just let me know!
