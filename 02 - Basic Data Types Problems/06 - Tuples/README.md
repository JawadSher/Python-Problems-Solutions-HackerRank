<h1 align='center'>Tuples</h1>

## Problem Statement 
**Problem URL : [Python Tuples](https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/cffa0cf8-7ffb-4e46-a070-4a019a59fc2f)

## Problem Solution 
```
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    my_tuple = tuple(integer_list)
    hash_value = hash(my_tuple)
    
    print(hash_value)
```

## Problem Solution Explanation

```python
if __name__ == '__main__':
```
- This line checks if the script is being run directly (not imported as a module). If it is run directly, the code block following this line will be executed.

```python
    n = int(input())
```
- This line reads an integer from the user input, converts it to an integer using `int()`, and stores it in the variable `n`. This value represents the number of elements that the user will input next.

```python
    integer_list = map(int, input().split())
```
- This line reads a line of input from the user, splits it into individual string elements using `split()`, converts each string element to an integer using `map(int, ...)`, and stores the result as an iterable `integer_list`. This iterable contains the integers input by the user.

```python
    my_tuple = tuple(integer_list)
```
- This line converts the `integer_list` iterable into a tuple, which is an immutable sequence type in Python. The resulting `my_tuple` will contain the integers provided by the user.

```python
    hash_value = hash(my_tuple)
```
- This line calculates the hash value of `my_tuple` using the `hash()` function. The `hash()` function returns a unique integer for the contents of the tuple, which is useful for operations like using the tuple as a key in a dictionary.

```python
    print(hash_value)
```
- Finally, this line prints the computed hash value to the console.

### Example
Consider the following input:
```
4
1 2 3 4
```
- `n` will be `4`, indicating the number of integers expected.
- `integer_list` will be an iterable of integers `[1, 2, 3, 4]`.
- `my_tuple` will be `(1, 2, 3, 4)`.
- The `hash()` function will compute a hash value for this tuple.

The output will be the hash value of the tuple `(1, 2, 3, 4)`. The exact hash value may vary between different runs of the program or different Python versions.
