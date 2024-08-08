<h1 align='center'>Set - .discard() - .remove() - .pop()</h1>

## Problem Statement

**Problem URL :** [Set .discard() .remove() .pop()](https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/99592ba2-8a91-40b4-9876-edb859359fa0)
![image](https://github.com/user-attachments/assets/07364ef0-e2d9-487e-a100-05b357161276)
![image](https://github.com/user-attachments/assets/c1f803ac-db4c-4e2c-a421-de8e5555b380)
![image](https://github.com/user-attachments/assets/a18cf331-392c-46ac-a0fc-654bc631bddd)




## Problem Solution
```python
n = int(input().strip())
nums_list = list(map(int, input().split()))
nums = set(nums_list[::-1])
cmds = int(input())

for _ in range(cmds):
    cmd = input().strip().split()
    
    prompt = cmd[0]
    
    if prompt == 'remove':
        elemnt = int(cmd[1])
        if elemnt in nums:
            nums.remove(elemnt)
    elif prompt == 'discard':
        elemnt = int(cmd[1])
        nums.discard(elemnt)
    elif prompt == 'pop':
        if nums:
            nums.pop()

print(sum(nums))

```

## Problem Solution Explanation

let’s break down the code line by line to explain it in a way that's beginner-friendly.

```python
n = int(input().strip())
```
- **Explanation:** This line reads an integer from the input, which represents the number of elements in the list. `input().strip()` reads the input and removes any extra whitespace around it. `int()` converts the cleaned input into an integer.

```python
nums_list = list(map(int, input().split()))
```
- **Explanation:** This line reads a line of input, splits it into separate strings based on spaces, converts each string to an integer, and stores these integers in a list called `nums_list`. `map(int, input().split())` applies the `int` function to each element of the split input, and `list()` converts the result into a list.

```python
nums = set(nums_list[::-1])
```
- **Explanation:** This line reverses the `nums_list` using slicing `[::-1]` and then converts it into a set called `nums`. A set is a collection of unique elements, so any duplicate values in `nums_list` will be removed.

```python
cmds = int(input())
```
- **Explanation:** This line reads an integer from the input, which represents the number of commands that will be processed.

```python
for _ in range(cmds):
```
- **Explanation:** This starts a loop that will run `cmds` times. Each iteration of the loop will handle one command.

```python
    cmd = input().strip().split()
```
- **Explanation:** Inside the loop, this line reads a line of input for the command, removes any extra whitespace, and splits it into a list of strings based on spaces. For example, if the input is `"remove 3"`, `cmd` will be `['remove', '3']`.

```python
    prompt = cmd[0]
```
- **Explanation:** This line extracts the first element of the `cmd` list, which indicates the type of command (`'remove'`, `'discard'`, or `'pop'`), and stores it in the variable `prompt`.

```python
    if prompt == 'remove':
```
- **Explanation:** This checks if the `prompt` is `'remove'`. If true, it will execute the following block of code to handle the removal of an element.

```python
        elemnt = int(cmd[1])
```
- **Explanation:** If the command is `'remove'`, this line extracts the second element of `cmd` (which is the element to remove), converts it to an integer, and stores it in the variable `elemnt`.

```python
        if elemnt in nums:
            nums.remove(elemnt)
```
- **Explanation:** This checks if `elemnt` is in the `nums` set. If true, it removes `elemnt` from `nums`.

```python
    elif prompt == 'discard':
```
- **Explanation:** This checks if the `prompt` is `'discard'`. If true, it will execute the following block of code to handle discarding an element.

```python
        elemnt = int(cmd[1])
```
- **Explanation:** If the command is `'discard'`, this line extracts and converts the second element of `cmd` (the element to discard) to an integer and stores it in `elemnt`.

```python
        nums.discard(elemnt)
```
- **Explanation:** This removes `elemnt` from the `nums` set if it is present. If `elemnt` is not in the set, `discard()` does nothing, so there’s no error.

```python
    elif prompt == 'pop':
```
- **Explanation:** This checks if the `prompt` is `'pop'`. If true, it will execute the following block of code to handle popping an element.

```python
        if nums:
            nums.pop()
```
- **Explanation:** This checks if the `nums` set is not empty. If true, it removes and returns an arbitrary element from the set using `pop()`. If the set is empty, `pop()` would raise an error, but this check prevents that.

```python
print(sum(nums))
```
- **Explanation:** After processing all commands, this line calculates the sum of all elements remaining in the `nums` set and prints the result.

### Summary
- The code reads a set of integers and a series of commands.
- It performs operations on the set based on the commands: removing specific elements, discarding elements (if present), or popping an arbitrary element.
- Finally, it prints the sum of the remaining elements in the set.
