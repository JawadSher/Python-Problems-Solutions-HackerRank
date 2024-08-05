<h1 align='center'>Itertools - Permutations()</h1>

## Problem Statement

**Problem URL :** [itertools permutations()](https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/ba954d8e-b329-4461-aaa4-1e4d37c973e4)
![image](https://github.com/user-attachments/assets/e49f8b2f-8a4d-49d8-a42d-d743808672b2)


## Problem Solution

```
from itertools import permutations

s = input()

chars = s.split()[0]
n = int(s.split()[1])
possible_per = permutations(sorted(chars, key=str.upper), n)
for per in possible_per:
    print(''.join(per))
```

## Problem Solution Explanation

1.  **Import the `permutations` Function:**
    
    
    ```
    from itertools import permutations
    ``` 
    
    This imports the `permutations` function from the `itertools` module, which is used to generate permutations of input iterables.
    
2.  **Read Input String:**
    
    
    ```
    s = input()
    ``` 
    
    This line reads a line of input from the user. For example, the input might be:
    
    `HACK 2` 
    
3.  **Extract Characters and Length:**

    ```
    chars = s.split()[0]
    n = int(s.split()[1])
    ``` 
    
    -   `s.split()` splits the input string into a list of substrings based on whitespace. For the input "HACK 2", `s.split()` results in `['HACK', '2']`.
    -   `s.split()[0]` takes the first element of the split list, which is the string `"HACK"`, and assigns it to `chars`.
    -   `s.split()[1]` takes the second element of the split list, which is the string `"2"`, converts it to an integer, and assigns it to `n`.
4.  **Sort Characters (Case Insensitive) and Generate Permutations:**
    
    
    ```
    possible_per = permutations(sorted(chars, key=str.upper), n)
    ``` 
    
    -   `sorted(chars, key=str.upper)` sorts the characters in `chars` in a case-insensitive manner. The `key=str.upper` argument ensures that the sorting is case-insensitive by converting each character to its uppercase equivalent for comparison purposes. For example, if `chars` were "HACK", sorting would result in the list `['A', 'C', 'H', 'K']`.
    -   `permutations(sorted(chars, key=str.upper), n)` generates all possible permutations of length `n` from the sorted characters.
5.  **Iterate Over Permutations and Print Them:**
    
 
    
    ```
    for per in possible_per:
        print(''.join(per))
       ``` 
    
    -   `for per in possible_per` iterates over each permutation tuple in `possible_per`.
    -   `''.join(per)` joins the characters in each permutation tuple to form a string.
    -   `print(''.join(per))` prints each permutation string.

### Example Execution

For the input `"HACK 2"`, let's go through the execution flow:

1.  **Input String:**
    
    ```
    s = "HACK 2"
    ``` 
    
2.  **Split Input String:**
    

    
    ```
    s.split() -> ['HACK', '2']
    chars = s.split()[0] -> "HACK"
    n = int(s.split()[1]) -> 2
    ``` 
    
3.  **Sort Characters:**

    
    ```
    sorted("HACK", key=str.upper) -> ['A', 'C', 'H', 'K']
    ``` 
    
4.  **Generate Permutations:**
    

    
    ```
    permutations(['A', 'C', 'H', 'K'], 2) -> 
    ('A', 'C'), ('A', 'H'), ('A', 'K'), 
    ('C', 'A'), ('C', 'H'), ('C', 'K'), 
    ('H', 'A'), ('H', 'C'), ('H', 'K'), 
    ('K', 'A'), ('K', 'C'), ('K', 'H')
    ``` 
    
5.  **Print Permutations:**
    
    
    ```
    AC
    AH
    AK
    CA
    CH
    CK
    HA
    HC
    HK
    KA
    KC
    KH
    ``` 
    

This step-by-step process ensures that the permutations of the input characters are correctly generated and printed in the desired format, considering the specified length and case-insensitive sorting.
