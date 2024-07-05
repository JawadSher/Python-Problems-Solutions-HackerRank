# Problem Statement 
**URL : [Designer Door Mat](https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/de5b8da2-6bc4-40b1-b4a2-156891514472)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/0420088b-244e-4c1a-81a6-df17dee1e261)




# Problem Solution 
```
N, M = map(int, input().split())

for i in range(1, N, 2):
    print(('.|.' * i).center(M, '-'))

for i in range(1, 2):
    print(('WELCOME' * i).center(M, '-'))

for i in range(N-2, -1, -2):
    print(('.|.' * i).center(M, '-'))
    
```

## Source Code Explanation

1.  **`N, M = map(int, input().split())`**:
    
    -   This line takes two integer inputs from the user.
    -   `N` represents the number of rows in the pattern.
    -   `M` represents the width of each row in the pattern.
    -   `map(int, input().split())` splits the input string into two parts, converts them to integers, and assigns them to `N` and `M`.
2.  **Upper Part**:

    
    ```
    for i in range(1, N, 2):
        print(('.|.' * i).center(M, '-'))
	``` 
    
    -   This loop generates the upper part of the pattern.
    -   `range(1, N, 2)` generates odd numbers starting from 1 up to (but not including) `N`.
    -   `'.|.' * i` repeats the string `'.|.'` `i` times.
    -   `.center(M, '-')` centers the resulting string within a field of width `M`, filling the empty spaces with `'-'`.
    -   The `print` statement outputs the centered string.
3.  **Middle Part**:
    

    
    ```
    for i in range(1, 2):
        print(('WELCOME' * i).center(M, '-'))
	``` 
    
    -   This loop generates the middle part of the pattern, which is a single line with the word "WELCOME".
    -   Since the loop runs only once with `i = 1`, it effectively prints `'WELCOME'.center(M, '-')`.
    -   The string `'WELCOME'` is centered within a field of width `M`, with `'-'` as the fill character.
4.  **Lower Part**:
    

    
    ```
    for i in range(N-2, -1, -2):
        print(('.|.' * i).center(M, '-'))
	``` 
    
    -   This loop generates the lower part of the pattern.
    -   `range(N-2, -1, -2)` generates numbers starting from `N-2` down to (and including) 1, decrementing by 2 each time.
    -   `'.|.' * i` repeats the string `'.|.'` `i` times.
    -   `.center(M, '-')` centers the resulting string within a field of width `M`, filling the empty spaces with `'-'`.
    -   The `print` statement outputs the centered string.

### Example:

Let's say the user inputs `7 21`.

#### Input:

`7 21` 

## Example Output:


```
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
.|..|..|..|..|..|..|.
-------WELCOME-------
.|..|..|..|..|..|..|.
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
``` 

### Breakdown of the Example:

1.  **Upper Part**:
    
    -   `i = 1`: `'.|.'` centered in width `21`:
        
 
        
        `---------.|.---------` 
        
    -   `i = 3`: `'.|..|..|.'` centered in width `21`:
        
        
        `------.|..|..|.------` 
        
    -   `i = 5`: `'.|..|..|..|..|.'` centered in width `21`:

        
        `---.|..|..|..|..|.---` 
        
    -   `i = 7`: `'.|..|..|..|..|..|..|.'` centered in width `21`:
        
        
        `.|..|..|..|..|..|..|.` 
        
2.  **Middle Part**:
    
    -   `'WELCOME'` centered in width `21`:
        

        
        `-------WELCOME-------` 
        
3.  **Lower Part**:
    
    -   `i = 5`: `'.|..|..|..|..|.'` centered in width `21`:

        
        `.|..|..|..|..|..|..|.` 
        
    -   `i = 3`: `'.|..|..|.'` centered in width `21`:
        
   
        
        `---.|..|..|..|..|.---` 
        
    -   `i = 1`: `'.|.'` centered in width `21`:
        
  
        
        `---------.|.---------` 
        

This way, the pattern is symmetric with the "WELCOME" message in the center.

