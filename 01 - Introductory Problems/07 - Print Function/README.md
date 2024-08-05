<h1 align='center'>Print - Function</h1>

## Problem Statement 
**Problem URL : [Print Function](https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/142ea07a-3641-4370-86e7-a602184a6ca3)


## Problem Solution 
```
if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        print(i, end="")
```

## Problem Solution Explanation
The given Python script takes an integer input n and prints the numbers from 1 to n consecutively without any spaces or newlines in between.

```if __name__ == '__main__':``` : This line ensures that the code block inside it runs only if the script is executed as the main program.

```n = int(input())``` : This line prompts the user to input an integer value, converts it to an integer, and assigns it to the variable n.

```for i in range(1, n+1):``` : This line initiates a for loop that iterates over the range of integers from 1 to n inclusive. The range(1, n+1) generates numbers starting from 1 up to and including n.

```print(i, end="")``` : This line prints the current integer i in each iteration. The end="" parameter in the print function ensures that the printed output is not followed by a newline character but by an empty string, resulting in consecutive numbers being printed on the same line without spaces.


