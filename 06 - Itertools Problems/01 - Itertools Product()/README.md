<h1 align='center'>Itertools - Product()</h1>

## Problem Statement

**Problem URL :** [itertool.product()](https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/dff7be58-ef2a-4f32-a62b-234617d30270)
![image](https://github.com/user-attachments/assets/4180a766-9202-4d51-8246-f14c078a5a9f)

## Problem Solution 
```
from itertools import product
A = input().strip().split()
B = input().strip().split()

certesian = product(A, B)

print(" ".join(f"({a}, {b})" for a, b, in certesian))

```

## Problem Solution Explanation

1.  **Import the `product` Function:**
    
    
    ```
    from itertools import product
    ``` 
    
    This imports the `product` function from the `itertools` module, which is used to compute the Cartesian product of input iterables.
    
3.  **Read and Split Input Strings:**
    
    
    ```
    A = input().strip().split()
    B = input().strip().split()
    ``` 
    
    -   `input()` reads a line of input from the user.
    -   `.strip()` removes any leading and trailing whitespace from the input string.
    -   `.split()` splits the input string into a list of substrings based on whitespace.
    
    Example:

    
    ```
    Input: '1 2'
    A becomes: ['1', '2']
    Input: '3 4'
    B becomes: ['3', '4']
    ``` 
    
4.  **Compute the Cartesian Product:**
    

    
    ```
    cartesian = product(A, B)`
    ``` 
    
    -   `product(A, B)` computes the Cartesian product of the lists `A` and `B`.
    -   The result is an iterator that produces tuples, where each tuple is a pair of elements, one from `A` and one from `B`.
    
    Example:

    
    ```
    Cartesian product of ['1', '2'] and ['3', '4'] is:
    ('1', '3'), ('1', '4'), ('2', '3'), ('2', '4')
    ``` 
    
5.  **Format and Print the Output:**
    

    
    ```
    print(" ".join(f"({a}, {b})" for a, b in cartesian))
    ``` 
    
    -   `for a, b in cartesian` iterates over each tuple in the Cartesian product.
    -   `f"({a}, {b})"` creates a formatted string for each tuple, representing the pair in the format `(a, b)`.
    -   `" ".join(...)` joins all the formatted strings with a space separator, creating a single output string.
    -   `print(...)` prints the final formatted string.
    
    Example:
    
    ```
    Iterating over the Cartesian product gives:
    ('1', '3') -> "(1, 3)"
    ('1', '4') -> "(1, 4)"
    ('2', '3') -> "(2, 3)"
    ('2', '4') -> "(2, 4)"
    
    Joining these with spaces results in:
    "(1, 3) (1, 4) (2, 3) (2, 4)"
    ``` 
    

### Complete Example with Input and Output

Given the inputs:



```
A: '1 2'
B: '3 4'
``` 

The code execution flow is as follows:

1.  `A = input().strip().split()` -> `A = ['1', '2']`
2.  `B = input().strip().split()` -> `B = ['3', '4']`
3.  `cartesian = product(A, B)` produces an iterator with tuples:
    -   ('1', '3')
    -   ('1', '4')
    -   ('2', '3')
    -   ('2', '4')
4.  `" ".join(f"({a}, {b})" for a, b in cartesian)` generates the string:
    -   "(1, 3) (1, 4) (2, 3) (2, 4)"
5.  `print(...)` outputs the final string:

    
    `(1, 3) (1, 4) (2, 3) (2, 4)` 
    

This process ensures that the Cartesian product of the input lists is correctly formatted and printed as specified.
