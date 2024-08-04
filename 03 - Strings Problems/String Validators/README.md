# Problem Statement 
**URL : [String Validators](https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/7f86c69f-c383-4b90-ade0-f4b5a5d9a821)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/c393b68c-875b-407b-aa89-c6e4f5542ebf)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/1a0d6121-2d7b-4fee-90b2-6c213635ecd6)



# Problem Solution 
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

## Code Explanation

1.  **Read Input:**
    
    
    ```
    if __name__ == '__main__':
        s = input()
	``` 
    
    -   This block reads a string input from the user and stores it in the variable `s`.
2.  **Check for Alphanumeric Characters:**
    
    
    `is_alnum = any(char.isalnum() for char in s)` 
    
    -   `char.isalnum()` returns `True` if the character `char` is alphanumeric (a letter or a digit), and `False` otherwise.
    -   `any(char.isalnum() for char in s)` checks if there is at least one alphanumeric character in the string `s`. It returns `True` if any character in `s` is alphanumeric, otherwise `False`.
3.  **Check for Alphabetic Characters:**
    
    
    `is_alpha = any(char.isalpha() for char in s)` 
    
    -   `char.isalpha()` returns `True` if the character `char` is a letter, and `False` otherwise.
    -   `any(char.isalpha() for char in s)` checks if there is at least one alphabetic character in the string `s`. It returns `True` if any character in `s` is a letter, otherwise `False`.
4.  **Check for Digits:**
    
    
    `is_digit = any(char.isdigit() for char in s)` 
    
    -   `char.isdigit()` returns `True` if the character `char` is a digit, and `False` otherwise.
    -   `any(char.isdigit() for char in s)` checks if there is at least one digit in the string `s`. It returns `True` if any character in `s` is a digit, otherwise `False`.
5.  **Check for Lowercase Characters:**
    
    
    `is_lower = any(char.islower() for char in s)` 
    
    -   `char.islower()` returns `True` if the character `char` is a lowercase letter, and `False` otherwise.
    -   `any(char.islower() for char in s)` checks if there is at least one lowercase character in the string `s`. It returns `True` if any character in `s` is a lowercase letter, otherwise `False`.
6.  **Check for Uppercase Characters:**
    
    
    `is_upper = any(char.isupper() for char in s)` 
    
    -   `char.isupper()` returns `True` if the character `char` is an uppercase letter, and `False` otherwise.
    -   `any(char.isupper() for char in s)` checks if there is at least one uppercase character in the string `s`. It returns `True` if any character in `s` is an uppercase letter, otherwise `False`.
7.  **Print Results:**
    
    -   For each of the properties checked, print `True` if the property is found in the string `s`, otherwise print `False`.
   
    
    ```
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
    

### Example Walkthrough

Let's go through an example to see how the code works:

**Input:**


`Hello123` 

**Checks:**

1.  `is_alnum = any(char.isalnum() for char in s)`:
    
    -   "H", "e", "l", "l", "o", "1", "2", and "3" are alphanumeric.
    -   `is_alnum` is `True`.
2.  `is_alpha = any(char.isalpha() for char in s)`:
    
    -   "H", "e", "l", "l", and "o" are alphabetic.
    -   `is_alpha` is `True`.
3.  `is_digit = any(char.isdigit() for char in s)`:
    
    -   "1", "2", and "3" are digits.
    -   `is_digit` is `True`.
4.  `is_lower = any(char.islower() for char in s)`:
    
    -   "e", "l", "l", and "o" are lowercase.
    -   `is_lower` is `True`.
5.  `is_upper = any(char.isupper() for char in s)`:
    
    -   "H" is uppercase.
    -   `is_upper` is `True`.

## Example Output:


```
True
True
True
True
True
``` 

Each of the properties (`alnum`, `alpha`, `digit`, `lower`, `upper`) is present in the input string "Hello123", hence the output for each check is `True`.

