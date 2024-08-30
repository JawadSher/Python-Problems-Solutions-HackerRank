<h1 align='center'>Default - Arguments</h1>

## Problem Statement

**Problem URL :** [Default Arguments](https://www.hackerrank.com/challenges/default-arguments/problem?isFullScreen=true)


![image](https://github.com/user-attachments/assets/a70036c4-f907-4cd6-b471-923b04a1fa3d)
![image](https://github.com/user-attachments/assets/2f8a8c32-427d-4778-82f3-9c6af915ddc5)
![image](https://github.com/user-attachments/assets/2fac635c-0d7b-4e0f-88f6-1b1655d40388)

## Problem Solution
```py
class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream();
    for _ in range(n):
        print(stream.get_next())


queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())

```

## Problem Solution Explanation
Let's go through the code step by step with detailed explanations for each part:

### 1. Defining the `EvenStream` Class
```python
class EvenStream(object):
    def __init__(self):
        self.current = 0
```
- **`class EvenStream(object):`**  
  This line defines a new class named `EvenStream`. In Python, `object` is the base class from which all classes inherit.

- **`def __init__(self):`**  
  This is the constructor method that is automatically called when an instance of `EvenStream` is created. The method initializes the state of the object.

- **`self.current = 0`**  
  Here, `self.current` is an instance variable that keeps track of the current even number. It's initialized to `0`, meaning the sequence will start from 0.

### 2. `get_next` Method in `EvenStream`
```python
    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return
```
- **`def get_next(self):`**  
  This method is responsible for generating the next even number in the sequence.

- **`to_return = self.current`**  
  The current even number is stored in the variable `to_return`.

- **`self.current += 2`**  
  The `current` variable is then incremented by 2, so that the next time `get_next()` is called, the next even number is ready.

- **`return to_return`**  
  Finally, the current even number is returned.

### 3. Defining the `OddStream` Class
```python
class OddStream(object):
    def __init__(self):
        self.current = 1
```
- **`class OddStream(object):`**  
  This line defines a new class named `OddStream`. Just like `EvenStream`, it inherits from `object`.

- **`def __init__(self):`**  
  The constructor method initializes the state of the `OddStream` object.

- **`self.current = 1`**  
  Here, `self.current` is initialized to `1`, so the sequence of odd numbers will start from 1.

### 4. `get_next` Method in `OddStream`
```python
    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return
```
- The `get_next` method in `OddStream` works the same way as in `EvenStream`, but it generates odd numbers by starting from 1 and incrementing by 2 each time.

### 5. `print_from_stream` Function
```python
def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())
```
- **`def print_from_stream(n, stream=None):`**  
  This function takes two arguments: `n`, the number of values to print, and `stream`, which can be an instance of either `EvenStream` or `OddStream`. If `stream` is not provided (i.e., it's `None`), it defaults to an `EvenStream`.

- **`if stream is None:`**  
  This checks if `stream` is `None`.

- **`stream = EvenStream()`**  
  If `stream` is `None`, it assigns an instance of `EvenStream` to `stream`, meaning the function will print even numbers by default.

- **`for _ in range(n):`**  
  This loop runs `n` times, where `n` is the number of values to be printed.

- **`print(stream.get_next())`**  
  For each iteration, it calls the `get_next()` method of the `stream` (either `EvenStream` or `OddStream`) to get the next number in the sequence and prints it.

### 6. Reading Input and Processing Queries
```python
queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())
```
- **`queries = int(input())`**  
  This reads an integer input that indicates the number of queries to process.

- **`for _ in range(queries):`**  
  This loop will run once for each query.

- **`stream_name, n = input().split()`**  
  For each query, it reads a line of input, splits it into two parts: `stream_name` (which will be either "even" or "odd") and `n` (the number of values to print).

- **`n = int(n)`**  
  Converts `n` from a string to an integer.

- **`if stream_name == "even":`**  
  This checks if the `stream_name` is "even".

- **`print_from_stream(n)`**  
  If `stream_name` is "even", it calls `print_from_stream(n)` with the default `EvenStream`.

- **`else:`**  
  If `stream_name` is "odd", it executes the code inside the else block.

- **`print_from_stream(n, OddStream())`**  
  This calls `print_from_stream(n, OddStream())`, using an instance of `OddStream` to print odd numbers.

### Summary
- This code allows you to print either even or odd numbers, depending on the input, for a specified number of times (`n`). The choice between even and odd is controlled by the `stream_name` input, and the numbers are printed in sequence based on the stream chosen.
