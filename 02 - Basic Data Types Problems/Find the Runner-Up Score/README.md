# Problem Statement
**URL : [Find the Runner-Up Score!](https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/a3b2845a-5b04-4643-a190-8ce4bb0f9631)

# Problem Solution 
```
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    maxNumber = float('-inf')
    secMaxNumber = float('-inf')
        
    for num in arr:
        if num > maxNumber:
            secMaxNumber = maxNumber
            maxNumber = num
        elif num > secMaxNumber and num != maxNumber:
            secMaxNumber = num
    
    print(secMaxNumber)
```

## Code Explanation
```if __name__ == '__main__':``` : This line checks if the script is being run directly (as the main program) and not imported as a module in another script. If it is being run directly, the following code will execute.

```n = int(input()):``` : This reads an integer input from the user, which is expected to be the number of elements in the array. However, in this code, n is not used directly after this line.

```arr = map(int, input().split())``` : This reads a line of input, splits it by spaces into a list of strings, and maps each string to an integer, resulting in a map object that can be iterated over to get the integers.

```maxNumber = float('-inf')``` :  Initialized to negative infinity to ensure that any number from the input will be larger.

```secMaxNumber``` : Initialized to negative infinity to ensure that any number from the input will be larger.

```if num > maxNumber``` : If the current number is greater than ```maxNumber```, it means we have found a new maximum. We update ```secMaxNumber``` to the old ```maxNumber``` value, then update ```maxNumber``` to the current number.

```elif num > secMaxNumber and num != maxNumber``` : If the current number is not the maximum but greater than ```secMaxNumber```, it means we have found a new second maximum. We update ```secMaxNumber``` to this number.

