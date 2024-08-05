<h1 align='center'>String - Split - And - Join</h1>

## Problem Statement 
**Problem URL : [String Split and Join](https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/56d0319b-6469-45ef-9607-01041b370cc0)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/dfef50ab-ac85-42fb-bc91-994ef669d081)


## Problem Solution 
```
def split_and_join(line):
    line_list = line.split(" ")
    line_list = "-".join(line_list)
    return line_list

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    
```

## Problem Solution Explanation
The function `split_and_join` takes a string `line` as input, splits the string into words based on spaces, and then joins these words back together using hyphens. The result is a single string where the words are separated by hyphens instead of spaces.

#### Implementation


```
def split_and_join(line):
    line_list = line.split(" ")
    line_list = "-".join(line_list)
    return line_list
``` 

1.  **Split the input string into a list of words**:
    

    
    `line_list = line.split(" ")` 
    
    -   The `split(" ")` method splits the string `line` into a list of words based on spaces. Each space in the original string marks the boundary between words.
    
    For example, if `line` is `"Hello world"`, `line.split(" ")` would result in the list `["Hello", "world"]`.
    
2.  **Join the list of words into a single string with hyphens**:
 
    
    `line_list = "-".join(line_list)` 
    
    -   The `"-".join(line_list)` method joins the elements of the list `line_list` into a single string, with each element separated by a hyphen.
    
    Continuing the example, `["Hello", "world"]` becomes `"Hello-world"`.
    
3.  **Return the resulting string**:

    
    `return line_list` 
    
    -   The function returns the new string where the words are separated by hyphens.

### Main Section



```
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
``` 

1.  **Check if the script is run directly**:
    

    
    `if __name__ == '__main__':` 
    
    -   This condition checks if the script is being run as the main program. If so, it executes the following block of code.
2.  **Read input from the user**:
    
    
    `line = input()` 
    
    -   The `input()` function reads a line of input from the user and stores it in the variable `line`.
3.  **Call the `split_and_join` function**:
    
    
    `result = split_and_join(line)` 
    
    -   The `split_and_join` function is called with `line` as the argument, and the result is stored in the variable `result`.
4.  **Print the result**:
    
    
    `print(result)` 
    
    -   Finally, the result is printed to the console.

### Example

If the user inputs the string `Hello world program`, the function would process it as follows:

-   The input string is `"Hello world program"`.
-   The `split(" ")` method splits it into the list `["Hello", "world", "program"]`.
-   The `"-".join(line_list)` method joins the list into the string `"Hello-world-program"`.

The output would be: `Hello-world-program`.


