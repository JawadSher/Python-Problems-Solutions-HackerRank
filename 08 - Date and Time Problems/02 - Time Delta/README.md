<h1 align='center'>Time - Delta</h1>

## Problem Statement

**Problem URL :** [Time Delta](https://www.hackerrank.com/challenges/python-time-delta/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/11c1ce27-07cd-4c39-bf03-748789fb21e4)
![image](https://github.com/user-attachments/assets/eeb8f11b-7d46-45ea-8a28-146b3d3ca656)

## Problem Solution

```py
import os
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):

    date_format = "%a %d %b %Y %H:%M:%S %z"

    time1 = datetime.strptime(t1, date_format)
    time2 = datetime.strptime(t2, date_format)

    time_difference = int(abs((time1 - time2).total_seconds()))
    return time_difference

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(f"{delta}\n")

    fptr.close()
```

## Problem Solution Explanation

Let's break down the code step by step, so you can understand how it works. This script is designed to solve a problem where you need to calculate the absolute difference between two timestamps in seconds. The timestamps are provided in a specific format, and the difference is calculated for multiple pairs of timestamps.

### 1. Importing Modules

```python
import os
from datetime import datetime
```

- **os**: This module is used for interacting with the operating system. In this script, it's used to open a file for writing output.
- **datetime**: This module provides classes for manipulating dates and times. We use it here to parse the input timestamps and calculate the time difference.

### 2. Defining the `time_delta` Function

```python
def time_delta(t1, t2):
    date_format = "%a %d %b %Y %H:%M:%S %z"
    time1 = datetime.strptime(t1, date_format)
    time2 = datetime.strptime(t2, date_format)
    time_difference = int(abs((time1 - time2).total_seconds()))
    return time_difference
```

- **Parameters**: The function takes two strings, `t1` and `t2`, which represent the two timestamps.
  
- **date_format**: This variable defines the format in which the timestamps are provided. The format string `"%a %d %b %Y %H:%M:%S %z"` is interpreted as:
  - `%a`: Abbreviated weekday name (e.g., "Sun", "Mon").
  - `%d`: Day of the month as a zero-padded decimal number (e.g., "02").
  - `%b`: Abbreviated month name (e.g., "May").
  - `%Y`: Year with century (e.g., "2015").
  - `%H:%M:%S`: Time in 24-hour format (e.g., "19:54:36").
  - `%z`: UTC offset in the form +HHMM or -HHMM.

- **datetime.strptime(t1, date_format)**: This function parses the timestamp string `t1` into a `datetime` object using the `date_format`. The same is done for `t2`.
  
- **time1 - time2**: Subtracting two `datetime` objects gives a `timedelta` object, representing the difference between the two times.
  
- **abs(...)**: The `abs()` function ensures that the difference is positive (absolute value), as we only care about the magnitude of the difference, not the direction.
  
- **.total_seconds()**: This method converts the `timedelta` to the total number of seconds.
  
- **int(...)**: The result is converted to an integer because the problem likely expects an integer number of seconds.

- **return time_difference**: The function returns the calculated time difference in seconds.

### 3. Main Execution Block

```python
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
```

- **if __name__ == '__main__'**: This line checks if the script is being run as the main program. If it is, the code inside this block will execute. This is a common Python idiom that prevents certain code from running when the module is imported elsewhere.
  
- **os.environ['OUTPUT_PATH']**: This accesses the environment variable `OUTPUT_PATH`, which typically points to a file where the output should be written. This is commonly used in coding competitions like HackerRank.
  
- **fptr = open(...)**: This opens the file specified by `OUTPUT_PATH` in write mode (`'w'`). The file object `fptr` is used to write the output.

### 4. Reading Input and Writing Output

```python
    t = int(input())
```

- **t = int(input())**: This reads an integer `t` from input, representing the number of test cases (i.e., the number of pairs of timestamps for which you need to calculate the time difference).

```python
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(f"{delta}\n")
```

- **for t_itr in range(t)**: This loop iterates `t` times, once for each pair of timestamps.
  
- **t1 = input()**: Reads the first timestamp for the current test case.
  
- **t2 = input()**: Reads the second timestamp for the current test case.
  
- **delta = time_delta(t1, t2)**: Calls the `time_delta` function with `t1` and `t2` as arguments, and stores the resulting time difference in `delta`.
  
- **fptr.write(f"{delta}\n")**: Writes the time difference (delta) to the output file, followed by a newline.

### 5. Closing the File

```python
    fptr.close()
```

- **fptr.close()**: Closes the file after all the results have been written. It's important to close files to free up system resources and ensure that all data is properly saved.

### Example

**Input:**
```
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 +0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
```

**Output:**
```
25200
88200
```

**Explanation:**
- For the first pair of timestamps, the difference is 25200 seconds.
- For the second pair of timestamps, the difference is 88200 seconds.

### Summary

- The script reads pairs of timestamps, parses them into `datetime` objects, calculates the difference in seconds, and writes the result to a file.
- The `datetime` module is key in handling and manipulating dates and times.
- Environment variables and file handling are used to manage input and output, a common practice in competitive programming.
