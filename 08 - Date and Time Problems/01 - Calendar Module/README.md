<h1 align='center'>Calendar - Module</h1>

## Problem Statement

**Problem URL :** [Calendar Module](https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-date-time)

![image](https://github.com/user-attachments/assets/42a02d97-72a9-4327-9814-6cd217250a61)
![image](https://github.com/user-attachments/assets/c65e9d42-a766-40b9-a513-f9130f3b9633)
![image](https://github.com/user-attachments/assets/dcb6c3f0-3d28-4945-87ca-28d8232b2d64)

## Problem Solution
```py
import calendar

n = list(map(int, input().split()))

week_day = calendar.weekday(n[2], n[0], n[1])
dayName = calendar.day_name[week_day]
print(dayName.upper())
```

## Problem Solution Explanation

Let's break down the code step by step for beginners.

```python
import calendar
```

- **Importing the `calendar` module**: 
  - The `calendar` module in Python provides useful functions related to the calendar, including functions to find out the day of the week for a given date.

```python
n = list(map(int, input().split()))
```

- **Getting the Input**:
  - `input()` reads a line of text input from the user.
  - `split()` splits this line into a list of strings wherever there are spaces.
  - `map(int, ...)` converts each of these strings into integers.
  - `list(...)` creates a list of these integers.
  - If the user inputs "08 05 2015", after this line, `n` will be `[8, 5, 2015]`, where `8` is the day, `5` is the month, and `2015` is the year.

```python
week_day = calendar.weekday(n[2], n[0], n[1])
```

- **Determining the Day of the Week**:
  - `n[2]` refers to the year (`2015`).
  - `n[0]` refers to the month (`8`).
  - `n[1]` refers to the day (`5`).
  - `calendar.weekday(year, month, day)` returns an integer representing the day of the week:
    - `0` = Monday
    - `1` = Tuesday
    - `2` = Wednesday
    - `3` = Thursday
    - `4` = Friday
    - `5` = Saturday
    - `6` = Sunday
  - So, `calendar.weekday(2015, 8, 5)` returns `2`, meaning the day is Wednesday.

```python
dayName = calendar.day_name[week_day]
```

- **Getting the Name of the Day**:
  - `calendar.day_name` is an array-like object where:
    - `calendar.day_name[0]` is "Monday",
    - `calendar.day_name[1]` is "Tuesday", and so on.
  - So, `calendar.day_name[2]` will be "Wednesday".
  - This line stores "Wednesday" in the variable `dayName`.

```python
print(dayName.upper())
```

- **Printing the Day in Uppercase**:
  - `.upper()` is a string method that converts all characters in the string to uppercase.
  - `"Wednesday".upper()` results in `"WEDNESDAY"`.
  - `print(dayName.upper())` will print `WEDNESDAY` to the screen.

### Example

Let's walk through an example:

- **Input**: Suppose the user inputs "08 05 2015".
  - `n` will be `[8, 5, 2015]` after processing.
  - `calendar.weekday(2015, 8, 5)` will return `2`.
  - `calendar.day_name[2]` will be "Wednesday".
  - `.upper()` will convert it to "WEDNESDAY".
  - The output will be `WEDNESDAY`.

### Key Points for Beginners

1. **Modules**: Modules like `calendar` provide pre-written functions that simplify complex tasks like finding the day of the week for a specific date.
  
2. **Input Handling**: The `input().split()` method allows you to easily separate the day, month, and year from a single line of input.

3. **List Indexing**: Lists in Python are zero-indexed, meaning the first element is accessed with `n[0]`, the second with `n[1]`, and so on.

4. **String Manipulation**: `.upper()` is one of many string methods that can be used to modify text output.

This code is a simple and effective way to determine the day of the week for any given date, while also demonstrating some basic Python concepts like list manipulation, module usage, and string methods.
