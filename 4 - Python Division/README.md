# Problem Statement 
**URL : [Python Division](https://www.hackerrank.com/challenges/python-division/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/d071e79e-d8a4-4764-9ecc-7d7c4f56c528)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/d65d7d83-57ec-4024-8a1a-0f7f49924ddf)


# Problem Solution 
```
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(f'{a//b}\n{a/b}')
```

## Code Explanation
The given Python script performs integer division and float division on two numbers inputted by the user.

```if __name__ == '__main__':``` : This line checks if the script is being run directly as the main program.

```a = int(input())``` : This line prompts the user to input a value, converts it to an integer, and assigns it to the variable a.

```b = int(input())``` : This line prompts the user to input another value, converts it to an integer, and assigns it to the variable b.


```print(f'{a//b}\n{a/b}')``` : This line performs two types of division on the inputted numbers :

- ```a // b``` : This performs integer (floor) division, which returns the largest integer less than or equal to the division result.
  
- ```a / b``` : This performs float (true) division, which returns a floating-point result.
Both results are printed, separated by newline characters.


