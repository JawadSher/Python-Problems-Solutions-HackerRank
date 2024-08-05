<h1 align='center'>Find - The - Runner-Up - Score</h1>

## Problem Statement
**Problem URL : [Find the Runner-Up Score!](https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/a3b2845a-5b04-4643-a190-8ce4bb0f9631)

## Problem Solution 
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

## Problem Solution Explanation

```python
if __name__ == '__main__':
```
- This line checks if the script is being run directly (not imported as a module in another script). If it is run directly, the code block following this line will be executed.

```python
    n = int(input())
```
- This line prompts the user to enter an integer, which is read from the input, converted to an integer using `int()`, and stored in the variable `n`. This value typically represents the number of elements in the array, although it’s not directly used in the subsequent code.

```python
    arr = map(int, input().split())
```
- This line reads a line of input from the user, splits it into individual string elements using `split()`, converts each string element to an integer using `map(int, ...)`, and stores the result as an iterable `arr`.

```python
    maxNumber = float('-inf')
    secMaxNumber = float('-inf')
```
- These lines initialize two variables, `maxNumber` and `secMaxNumber`, to negative infinity (`float('-inf')`). This is done to ensure that any number in the array will be greater than these initial values.

```python
    for num in arr:
```
- This line starts a `for` loop that iterates over each number in the iterable `arr`.

```python
        if num > maxNumber:
```
- Inside the loop, this line checks if the current number `num` is greater than `maxNumber`. 

```python
            secMaxNumber = maxNumber
            maxNumber = num
```
- If `num` is greater than `maxNumber`, then the current `maxNumber` is assigned to `secMaxNumber` (making it the second largest number so far), and `num` becomes the new `maxNumber`.

```python
        elif num > secMaxNumber and num != maxNumber:
```
- If `num` is not greater than `maxNumber` but is greater than `secMaxNumber` and not equal to `maxNumber`, this condition is true. This means `num` is the second largest number found so far.

```python
            secMaxNumber = num
```
- Here, `num` is assigned to `secMaxNumber`, making it the new second largest number.

```python
    print(secMaxNumber)
```
- Finally, the code prints the value of `secMaxNumber`, which is the second largest number in the array.

### Example
Consider the following input:
```
5
1 5 2 3 5
```
- `n` is set to 5, though it's not used in the computation.
- `arr` becomes an iterable of `[1, 5, 2, 3, 5]`.
- After processing:
  - `maxNumber` will be `5`.
  - `secMaxNumber` will be `3` (the largest number other than `5`).

Thus, the output will be `3`, which is the second largest number in the array.
