# Problem Statement 
**URL : [sWAP cASE](https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/dd042e28-995f-4e28-9599-fc198ce3d327)


# Problem Solution 
```
def swap_case(s):
    txt = ""
    for c in s:
        if c.islower():
            txt += c.upper()
        else:
            txt += c.lower()
    return txt

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
```

## Code Explanation
The function `swap_case` takes a string `s` as input and returns a new string where each lowercase letter in `s` is converted to uppercase, and each uppercase letter is converted to lowercase.

#### Implementation

```
def swap_case(s):
    txt = ""
    for c in s:
        if c.islower():
            txt += c.upper()
        else:
            txt += c.lower()
    return txt
``` 

1.  **Initialization**:
  
    `txt = ""` 
    
    -   This initializes an empty string `txt` which will be used to build the final result.
2.  **Loop through each character in the string `s`**:
    
    
    `for c in s:` 
    
    -   This for loop iterates over each character `c` in the input string `s`.
3.  **Check if the character is lowercase**:
   
    
    ```
    if c.islower():
        txt += c.upper()
    ``` 
    
    -   The `islower()` method checks if the character `c` is a lowercase letter.
    -   If it is, `c.upper()` converts the character to uppercase, and it is appended to `txt`.
4.  **Otherwise, convert to lowercase**:
    
    
    ```
    else:
        txt += c.lower()
    ``` 
    
    -   If the character is not lowercase (i.e., it's either uppercase or non-alphabetic), `c.lower()` converts the character to lowercase, and it is appended to `txt`.
5.  **Return the result**:
    
    
    `return txt` 
    
    -   After the loop finishes, the function returns the new string `txt` which has all the cases swapped.

### Main Section


```
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
   ``` 

1.  **Check if the script is run directly**:
    
    
    `if __name__ == '__main__':` 
    
    -   This condition checks if the script is being run as the main program. If so, it executes the following block of code.
2.  **Read input from the user**:
    
    
    `s = input()` 
    
    -   The `input()` function reads a line of input from the user and stores it in the variable `s`.
3.  **Call the `swap_case` function**:
    
    
    `result = swap_case(s)` 
    
    -   The `swap_case` function is called with `s` as the argument, and the result is stored in the variable `result`.
4.  **Print the result**:
    
    
    `print(result)` 
    
    -   Finally, the result is printed to the console.

### Example

If the user inputs the string `Hello World!`, the function would process it as follows:

-   `H` is uppercase -> converted to `h`
-   `e` is lowercase -> converted to `E`
-   `l` is lowercase -> converted to `L`
-   `l` is lowercase -> converted to `L`
-   `o` is lowercase -> converted to `O`
-   (space) is non-alphabetic -> remains unchanged
-   `W` is uppercase -> converted to `w`
-   `o` is lowercase -> converted to `O`
-   `r` is lowercase -> converted to `R`
-   `l` is lowercase -> converted to `L`
-   `d` is lowercase -> converted to `D`
-   `!` is non-alphabetic -> remains unchanged

The output would be: `hELLO wORLD!`.

