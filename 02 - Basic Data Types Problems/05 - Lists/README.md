<h1 align='center'>Lists</h1>

## Problem Statement 
**Problem URL : [Python Lists](https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/6ad41091-99a5-4c0d-a9d3-4286b5bca0af)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/503fe67f-a259-4485-926e-5d4fdcd3c160)

## Problem Solution 
```
if __name__ == '__main__':
    n = int(input())
    my_list = []
    
    for i in range(n):
        HR_input = input().split()
        functions = HR_input[0]
        numbers = list(map(int, HR_input[1:]))
        
        if functions == 'insert':
            my_list.insert(int(numbers[0]), int(numbers[1]))
        elif functions == 'print':
            print(my_list)
        elif functions == 'remove':
            my_list.remove(int(numbers[0]))
        elif functions == 'append':
            my_list.append(int(numbers[0]))
        elif functions == 'sort':
            my_list.sort()
        elif functions == 'pop':
            my_list.pop()
        elif functions == 'reverse':
            my_list.reverse()
```

## Problem Solution Explanation

```python
if __name__ == '__main__':
```
- This line checks if the script is being run directly (as opposed to being imported as a module). If it is run directly, the code block following this line will be executed.

```python
    n = int(input())
```
- Reads an integer input from the user, converts it to an integer using `int()`, and stores it in the variable `n`. This value represents the number of commands that will be processed.

```python
    my_list = []
```
- Initializes an empty list `my_list` which will be used to perform various operations based on the input commands.

```python
    for i in range(n):
```
- Starts a `for` loop that will iterate `n` times, once for each command to be processed.

```python
        HR_input = input().split()
```
- Reads a line of input from the user, splits it into a list of strings using `split()`, and stores it in `HR_input`.

```python
        functions = HR_input[0]
```
- Assigns the first element of `HR_input` (which specifies the function to be performed) to the variable `functions`.

```python
        numbers = list(map(int, HR_input[1:]))
```
- Converts the remaining elements of `HR_input` (which are supposed to be numbers) from strings to integers using `map(int, HR_input[1:])`, and stores the result as a list in the variable `numbers`.

```python
        if functions == 'insert':
```
- Checks if the function specified in `functions` is `'insert'`.

```python
            my_list.insert(int(numbers[0]), int(numbers[1]))
```
- If the function is `'insert'`, this line inserts the integer value `numbers[1]` at the index specified by `numbers[0]` in `my_list`.

```python
        elif functions == 'print':
```
- Checks if the function specified in `functions` is `'print'`.

```python
            print(my_list)
```
- If the function is `'print'`, this line prints the current state of `my_list`.

```python
        elif functions == 'remove':
```
- Checks if the function specified in `functions` is `'remove'`.

```python
            my_list.remove(int(numbers[0]))
```
- If the function is `'remove'`, this line removes the first occurrence of the integer value `numbers[0]` from `my_list`.

```python
        elif functions == 'append':
```
- Checks if the function specified in `functions` is `'append'`.

```python
            my_list.append(int(numbers[0]))
```
- If the function is `'append'`, this line appends the integer value `numbers[0]` to the end of `my_list`.

```python
        elif functions == 'sort':
```
- Checks if the function specified in `functions` is `'sort'`.

```python
            my_list.sort()
```
- If the function is `'sort'`, this line sorts `my_list` in ascending order.

```python
        elif functions == 'pop':
```
- Checks if the function specified in `functions` is `'pop'`.

```python
            my_list.pop()
```
- If the function is `'pop'`, this line removes and returns the last element from `my_list`.

```python
        elif functions == 'reverse':
```
- Checks if the function specified in `functions` is `'reverse'`.

```python
            my_list.reverse()
```
- If the function is `'reverse'`, this line reverses the order of elements in `my_list`.

### Summary
This script reads a series of commands to manipulate a list. Depending on the command, it performs various operations such as inserting, appending, removing elements, or modifying the list in other ways.


