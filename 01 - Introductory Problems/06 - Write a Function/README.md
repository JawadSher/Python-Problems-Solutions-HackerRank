<h1 align='center'>Write - A - Function</h1>

## Problem Statement 
**Problem URL : [Write a Function](https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/948fe625-a954-4995-99d8-0e04ad2860c7)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/d3ff1629-f71a-43e2-9a6b-974a2e9cd11b)


## Problem Solution 
```
def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    return leap
```

## Problem Solution Explanation
The given Python function is_leap determines whether a given year is a leap year or not.

```leap = False``` : This initializes a boolean variable leap to False. This variable will be used to store whether the year is a leap year (True) or not (False).

```if year % 4 == 0:``` : A year must be divisible by 4 to be a leap year. If the year is not divisible by 4, it cannot be a leap year.

```if year % 100 == 0:``` : If the year is divisible by 4, the next check is to see if it is divisible by 100. If it is not divisible by 100, it is a leap year.

```if year % 400 == 0:``` : If the year is divisible by 100, the next check is to see if it is also divisible by 400. If it is divisible by 400, it is a leap year; otherwise, it is not.

```return leap``` : The function returns the value of leap, indicating whether the given year is a leap year (True) or not (False).

## Leap Year Rules
  A year is a leap year if it is divisible by 4. However, if the year is divisible by 100, it must also be divisible by 400 to be considered a leap year.
  - **Examples** :
    
      *is_leap(2000)*: Returns True because 2000 is divisible by 400.
    
      *is_leap(1900)*: Returns False because 1900 is divisible by 100 but not by 400.
    
      *is_leap(2012)*: Returns True because 2012 is divisible by 4 but not by 100.
    
      *is_leap(2019)*: Returns False because 2019 is not divisible by 4.

