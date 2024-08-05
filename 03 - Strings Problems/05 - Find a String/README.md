<h1 align='center'>Find - A - String</h1>

## Problem Statement 
**Problem URL : [Find a String](https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/897353ad-4367-44d8-ab02-1122bea3ee41)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/f95f7b63-58de-4bf6-9b03-2398a3170f8c)


## Problem Solution 
```
def count_substring(string, sub_string):
    n = len(string)
    m = len(sub_string)
    k = n - m + 1
    
    count = 0
    for i in range(k):
        if string[i:i + m] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
```

## Problem Solution Explanation

The code defines a function `count_substring` that takes two strings as input:

1.  **`string`**: The main string to search within.
2.  **`sub_string`**: The substring to find occurrences of.

**Steps:**

1.  **Calculate Lengths:**
    
    -   `n`: Length of the main string (`string`).
    -   `m`: Length of the substring (`sub_string`).
    -   `k`: Number of possible starting positions for `sub_string` within `string` (calculated as `n - m + 1`).
2.  **Initialize Counter:**
    
    -   `count`: Variable to store the number of substring occurrences (initialized to 0).
3.  **Loop through String:**
    
    -   The loop iterates through all possible starting positions for `sub_string` within `string` (using the `k` value).
4.  **Check Substring Match:**
    
    -   Inside the loop, it checks if the substring starting at position `i` in `string` matches `sub_string` using string slicing (`string[i:i + m]`).
    -   If there's a match, `count` is incremented.
5.  **Return the Count:**
    
    -   The function returns the final `count` representing the number of substring occurrences.
6.  **Main Execution Block:**
    
    -   This block is executed only when the script is run directly (not imported as a module).
    -   It prompts the user to enter the main string and substring.
    -   Calls the `count_substring` function with the user inputs.
    -   Prints the final count of substring occurrences.

### Example Walkthrough

Let's consider `string = "ABCDCDC"` and `sub_string = "CDC"`:

1.  **Input:**
    
    -   `string = "ABCDCDC"`
    -   `sub_string = "CDC"`
2.  **Calculate Lengths:**
    
    -   `n = 7`
    -   `m = 3`
    -   `k = 7 - 3 + 1 = 5` (possible starting positions)
3.  **Loop and Check Matches:**
    
    -   `i = 0`: No match ("ABC")
    -   `i = 1`: No match ("BCD")
    -   `i = 2`: **Match** ("CDC"), `count` becomes 1
    -   `i = 3`: No match ("DCD")
    -   `i = 4`: **Match** ("CDC"), `count` becomes 2
4.  **Return and Print:**
    
    -   Final `count` is 2.
    -   Output: `2`

### Key Points

-   The loop range (`k`) ensures all potential starting positions are checked.
-   String slicing (`string[i:i + m]`) extracts the substring for comparison.

This approach correctly counts overlapping occurrences, providing the desired result.
