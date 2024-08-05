<h1 align='center'>Loops</h1>

## Problem Statement 
**Problem URL : [Loops](https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/a132a73f-23c0-4955-b960-765549ae1062)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/d6fa356e-597f-48be-990c-b6f109747af4)


# Problem Solution 
```
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)
```

## Problem Solution Explanation
The given Python script takes an integer input n and prints the square of each integer from 0 to n-1.

```if __name__ == '__main__':``` : This line checks if the script is being run directly as the main program.

```n = int(input())``` : This line prompts the user to input a value, converts it to an integer, and assigns it to the variable n.

```for i in range(n):``` : This line initiates a for loop that iterates over the range of integers from 0 to n-1.

```print(i**2)``` : This line prints the square of the current integer i in the loop.
