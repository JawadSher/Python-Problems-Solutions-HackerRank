<h1 align='center'>Alphabet - Rangoli</h1>

## Problem Statement 
**Problem URL : [Alphabet Rangoli](https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/ff6032d1-dc2a-4031-932c-73b83952bc7c)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/8bd52d81-6032-4092-b016-c72414bef3bd)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/9a4aa10a-4748-43c4-aeb7-21451c44917e)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/07da7c93-90d0-4ce7-a2b7-c55ece4dd3cd)




## Problem Solution 
```
def print_rangoli(size):
    import string 
    alphabet = string.ascii_lowercase
    
    lines = []
    
    for i in range(size):
        s = '-'.join(alphabet[i : size])
        lines.append((s[::-1] + s[1:]).center(4 * size - 3, '-'))
        
    
    print('\n'.join(lines[::-1] + lines[1:]))
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
```

## Problem Solution Explanation 

1.  **Importing the Alphabet:**

    
    ```
    import string
    alphabet = string.ascii_lowercase
    ``` 
    
    -   `string.ascii_lowercase` contains all the lowercase letters of the English alphabet ('a' to 'z').
2.  **Initializing a List for Lines:**
    

    
    `lines = []` 
    
    -   This list will hold each line of the rangoli pattern.
3.  **Generating the Lines of the Rangoli:**
  
    
    ```
    for i in range(size):
        s = '-'.join(alphabet[i : size])
        lines.append((s[::-1] + s[1:]).center(4 * size - 3, '-'))
     ``` 
    
    -   **Loop Through the Range:**
        
        -   `for i in range(size):` iterates from 0 to `size-1`.
    -   **Creating the String `s`:**
        
        -   `alphabet[i : size]` slices the `alphabet` string from the `i`th index to the `size`th index.
        -   `'-'.join(alphabet[i : size])` joins these characters with hyphens to form a string like 'a-b-c-d-e'.
    -   **Forming the Symmetrical Line:**
        
        -   `s[::-1]` reverses the string `s`.
        -   `s[1:]` takes all characters of `s` starting from the second character (to avoid repeating the first character in the middle).
        -   `(s[::-1] + s[1:])` combines the reversed string with the second part of the original string to form a symmetrical pattern.
    -   **Centering the Line:**
        
        -   `.center(4 * size - 3, '-')` centers the line within a width of `4 * size - 3` characters, padding with hyphens (`'-'`).
    -   **Appending to Lines:**
        
        -   `lines.append(...)` adds the centered, symmetrical line to the `lines` list.
4.  **Printing the Rangoli Pattern:**

    
    `print('\n'.join(lines[::-1] + lines[1:]))` 
    
    -   `lines[::-1]` reverses the list of lines.
    -   `lines[1:]` takes all lines except the first one.
    -   `lines[::-1] + lines[1:]` combines the reversed list with the second part of the original list to form the full pattern.
    -   `'\n'.join(...)` joins the lines with newline characters to form the final string, which is then printed.

##  Example Output

For `n = 3`, the function would create and print the following pattern:


```
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
``` 


### Summary

-   The function generates a rangoli pattern using letters from the alphabet, joined with hyphens.
-   Each line is symmetrical and centered with hyphens.
-   The final pattern includes the reversed lines and the original lines (excluding the first one) to complete the rangoli shape.

