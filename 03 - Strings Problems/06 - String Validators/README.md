<h1 align='center'>String - Validators</h1>

## Problem Statement 
**Problem URL : [String Validators](https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/7f86c69f-c383-4b90-ade0-f4b5a5d9a821)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/c393b68c-875b-407b-aa89-c6e4f5542ebf)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/1a0d6121-2d7b-4fee-90b2-6c213635ecd6)



## Problem Solution 
```
if __name__ == '__main__':
    s = input()
    
    is_alnum = any(char.isalnum() for char in s)
    is_alpha = any(char.isalpha() for char in s)
    is_digit = any(char.isdigit() for char in s)
    is_lower = any(char.islower() for char in s)
    is_upper = any(char.isupper() for char in s)
    
    if(is_alnum):
        print("True")
    else:
        print("False")
    if(is_alpha):
        print("True")
    else:
        print("False")
    if(is_digit):
        print("True")
    else:
        print("False")
    if(is_lower):
        print("True")
    else:
        print("False")
    if(is_upper):
        print("True")
    else:
        print("False")        
    
```

## Problem Solution Explanation

```python
if __name__ == '__main__':
```
- This line checks if the script is being run directly (not imported as a module). If it is run directly, the code block following this line will be executed.

```python
    s = input()
```
- Reads a string input from the user and stores it in the variable `s`. This string will be used for checking various conditions.

```python
    is_alnum = any(char.isalnum() for char in s)
```
- Uses a generator expression to check if any character in the string `s` is alphanumeric (either a letter or a number). The `any()` function returns `True` if at least one character satisfies the condition, otherwise `False`.

```python
    is_alpha = any(char.isalpha() for char in s)
```
- Uses a generator expression to check if any character in the string `s` is a letter (either uppercase or lowercase). The `any()` function returns `True` if at least one character is a letter, otherwise `False`.

```python
    is_digit = any(char.isdigit() for char in s)
```
- Uses a generator expression to check if any character in the string `s` is a digit (0-9). The `any()` function returns `True` if at least one character is a digit, otherwise `False`.

```python
    is_lower = any(char.islower() for char in s)
```
- Uses a generator expression to check if any character in the string `s` is a lowercase letter. The `any()` function returns `True` if at least one character is lowercase, otherwise `False`.

```python
    is_upper = any(char.isupper() for char in s)
```
- Uses a generator expression to check if any character in the string `s` is an uppercase letter. The `any()` function returns `True` if at least one character is uppercase, otherwise `False`.

```python
    if(is_alnum):
        print("True")
    else:
        print("False")
```
- Checks the value of `is_alnum` and prints `"True"` if it is `True`, otherwise prints `"False"`.

```python
    if(is_alpha):
        print("True")
    else:
        print("False")
```
- Checks the value of `is_alpha` and prints `"True"` if it is `True`, otherwise prints `"False"`.

```python
    if(is_digit):
        print("True")
    else:
        print("False")
```
- Checks the value of `is_digit` and prints `"True"` if it is `True`, otherwise prints `"False"`.

```python
    if(is_lower):
        print("True")
    else:
        print("False")
```
- Checks the value of `is_lower` and prints `"True"` if it is `True`, otherwise prints `"False"`.

```python
    if(is_upper):
        print("True")
    else:
        print("False")
```
- Checks the value of `is_upper` and prints `"True"` if it is `True`, otherwise prints `"False"`.

### Example

Let’s consider an example input:

```
Hello123
```

- **`s = "Hello123"`**
  
- **`is_alnum`**:
  - Checks if there is any alphanumeric character (which there is: 'H', 'e', 'l', 'o', '1', '2', '3').
  - Output: `True`
  
- **`is_alpha`**:
  - Checks if there is any letter (which there are: 'H', 'e', 'l', 'l', 'o').
  - Output: `True`
  
- **`is_digit`**:
  - Checks if there is any digit (which there are: '1', '2', '3').
  - Output: `True`
  
- **`is_lower`**:
  - Checks if there is any lowercase letter (which there are: 'e', 'l', 'l', 'o').
  - Output: `True`
  
- **`is_upper`**:
  - Checks if there is any uppercase letter (which there is: 'H').
  - Output: `True`

**Output of the code** will be:
```
True
True
True
True
True
```


