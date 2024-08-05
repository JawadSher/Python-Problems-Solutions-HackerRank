<h1 align='center'>Itertools Combinations()</h1>

## Problem Statement

**Problem URL :** [itertools.Combination()](https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/49194b53-4079-4b8d-853a-cfd0991b80f6)
![image](https://github.com/user-attachments/assets/1a179eb0-7a90-40e1-b481-45224fa082b5)

## Problem Solution

```
from itertools import combinations

s = "HACK 2"

chars = s.split()[0]
n = int(s.split()[1])

sorted_chars = sorted(chars)

possible_combinations = combinations(sorted_chars, n)

for i in range(1, n+1):
    possible_combinations = combinations(sorted_chars, i)
    for comb in possible_combinations:
        print(''.join(comb))
```

## Problem Solution Explanation

1.  **Import the `combinations` Function:**
    
    ```
    from itertools import combinations
    ``` 
    
    This imports the `combinations` function from the `itertools` module, which is used to generate combinations of input iterables.
    
2.  **Set the Input String:**
    

    
    ```
    s = "HACK 2"
    ``` 
    
    This sets the input string `s`. For this example, the input is `"HACK 2"`.
    
3.  **Extract Characters and the Integer `n`:**
    

    
    ```
    chars = s.split()[0]
    n = int(s.split()[1])
    ``` 
    
    -   `s.split()` splits the input string into a list of substrings based on whitespace. For the input `"HACK 2"`, `s.split()` results in `['HACK', '2']`.
    -   `s.split()[0]` takes the first element of the split list, which is the string `"HACK"`, and assigns it to `chars`.
    -   `s.split()[1]` takes the second element of the split list, which is the string `"2"`, converts it to an integer, and assigns it to `n`.
4.  **Sort Characters in Lexicographic Order:**
    

    
    ```
    sorted_chars = sorted(chars)
    ``` 
    
    This sorts the characters in `chars` in lexicographic order. For the input `"HACK"`, sorting results in the list `['A', 'C', 'H', 'K']`.
    
5.  **Generate and Print All Combinations from Length 1 to `n`:**
    

    
    ```
    for i in range(1, n + 1):
        possible_combinations = combinations(sorted_chars, i)
        for comb in possible_combinations:
            print(''.join(comb))
       ``` 
    
    -   `for i in range(1, n + 1)` iterates over the lengths from 1 to `n`.
    -   `combinations(sorted_chars, i)` generates all combinations of the sorted characters with length `i`.
    -   `for comb in possible_combinations` iterates over each combination tuple in `possible_combinations`.
    -   `''.join(comb)` joins the characters in each combination tuple to form a string.
    -   `print(''.join(comb))` prints each combination string.

### Detailed Example Execution

Let's go through the execution step-by-step for the input `"HACK 2"`:

1.  **Input String:**
    

    
    ```
    s = "HACK 2"
    ``` 
    
2.  **Split Input String:**
    
 
    
    `s.split() -> ['HACK', '2']`
    `chars = s.split()[0] -> "HACK"`
    `n = int(s.split()[1]) -> 2` 
    
3.  **Sort Characters:**
    

    
    `sorted("HACK") -> ['A', 'C', 'H', 'K']` 
    
4.  **Generate and Print All Combinations from Length 1 to `n`:**
    
    -   **For `i = 1`:**
        

        
        `possible_combinations = combinations(['A', 'C', 'H', 'K'], 1)` 
        
        This generates all combinations of length 1:
        

        
        `('A'), ('C'), ('H'), ('K')` 
        
        Printing these combinations:

        
        ```
        A
        C
        H
        K
        ``` 
        
    -   **For `i = 2`:**

        
        `possible_combinations = combinations(['A', 'C', 'H', 'K'], 2)` 
        
        This generates all combinations of length 2:

        
        `('A', 'C'), ('A', 'H'), ('A', 'K'), ('C', 'H'), ('C', 'K'), ('H', 'K')` 
        
        Printing these combinations:

        
        ```
        AC
        AH
        AK
        CH
        CK
        HK
        ``` 
        

### Complete Output

Combining all the printed outputs for `i` ranging from 1 to `n` (2 in this case), we get:


```
A
C
H
K
AC
AH
AK
CH
CK
HK
``` 

This code ensures that all combinations of the input characters are correctly generated and printed in lexicographic order for all lengths from 1 to `n`.
