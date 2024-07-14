# Problem Statement

**URL** : [Merge The Tools](https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/00fab7ea-253d-432c-b731-75fd0e154325)
![image](https://github.com/user-attachments/assets/a126614a-544e-409c-b1e2-47e73a534cb8)


## Problem Explanation: "Merge the Tools"

The "Merge the Tools" problem on HackerRank is a string manipulation problem that involves breaking a given string into several substrings and removing duplicate characters from each substring.

Here are the key steps of the problem:

1.  **Input**:
    
    -   A string `S` of length `N`.
    -   An integer `K`, which divides the length `N` of the string such that `N` is a multiple of `K`.
2.  **Output**:
    
    -   For each segment of the string (each of length `K`), create a new string by removing any duplicate characters while preserving the order of the first occurrence of each character.

### Example

Let's consider an example to clarify the problem.

-   Given string `S = "AABCAAADA"` and `K = 3`.
-   The string `S` can be split into 3 segments of length 3:
    -   Segment 1: `"AAB"`
    -   Segment 2: `"CAA"`
    -   Segment 3: `"ADA"`

After removing duplicates from each segment, we get:

-   Segment 1: `"AAB"` → `"AB"`
-   Segment 2: `"CAA"` → `"CA"`
-   Segment 3: `"ADA"` → `"AD"`

Thus, the output should be:

```
AB
CA
AD
``` 

### Approach to Solve the Problem

1.  **Divide the String into Segments**:
    
    -   Split the string `S` into `N/K` segments, each of length `K`.
2.  **Process Each Segment**:
    
    -   For each segment, iterate through the characters and keep track of the characters that have already been encountered using a set.
    -   Construct a new string by adding each character only if it hasn't been seen before in that segment.
3.  **Output the Results**:
    
    -   Print or return each processed segment as the result.

### Step-by-Step Approach

1.  **Loop Through the String**:
    
    -   Use a loop to create segments of length `K` from the string `S`.
2.  **Remove Duplicates**:
    
    -   For each segment, create an empty set to keep track of seen characters.
    -   Create a new string for the segment by appending characters that are not in the set.
    -   Add each character to the set once it has been appended to the new string.
3.  **Store/Print the Processed Segments**:
    
    -   Collect all processed segments.
    -   Print or return each segment.
## Problem Solution 

```
  def merge_the_tools(string, k):
  n = len(string)
  
  for i in range(0, n, k):
    result = ""
    segment = string[i : i+k]
    for char in segment:
      if char not in result:
        result += char
    print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
```
## Source Code Explanation
1.  **Function Definition: `merge_the_tools(string, k)`**
    
    -   This function takes two parameters:
        -   `string`: The input string that needs to be divided into segments.
        -   `k`: The segment length into which the string should be divided.
2.  **Initialization:**
    
    -   `n = len(string)`: Calculates the length of the input string `string`.
3.  **Segmentation and Processing:**
    
    -   `for i in range(0, n, k):`
        -   This loop iterates through the string in steps of `k`. It starts at index `0` and ends at `n` with a step of `k`, ensuring that each iteration processes a segment of length `k`.
4.  **Creating the Segment:**
    
    -   `segment = string[i : i+k]`: Slices the input string `string` to extract the current segment of length `k` starting from index `i`.
5.  **Removing Duplicates:**
    
    -   `result = ""`: Initializes an empty string `result` to store the processed segment without duplicates.
    -   `for char in segment:`
        -   Iterates through each character `char` in the current segment `segment`.
        -   `if char not in result:`
            -   Checks if the character `char` is not already present in the `result` string.
            -   `result += char`: If `char` is not in `result`, adds `char` to `result`.
6.  **Printing the Result:**
    
    -   `print(result)`: Prints the processed segment `result` after removing duplicates.
7.  **Main Program Execution:**
    
    -   `if __name__ == '__main__':`
        -   This block ensures that the following code is executed only when the script is run directly, not when it is imported as a module.
    -   `string, k = input(), int(input())`
        -   Takes user input where:
            -   `string`: The input string to be segmented and processed.
            -   `k`: The segment length provided as an integer input.
    -   `merge_the_tools(string, k)`: Calls the `merge_the_tools` function with `string` and `k` as arguments to perform the segmentation and printing of processed segments.

### Explanation of Functionality

-   **Segmentation**: The input string `string` is divided into segments of length `k` using slicing (`string[i : i+k]`).
-   **Duplicate Removal**: Within each segment, duplicates are removed by iterating through each character and appending it to `result` only if it's not already present (`if char not in result`).
-   **Output**: Each processed segment (`result`) is printed immediately after processing.

### Example

If the input is:

-   `string = "AABCAAADA"`
-   `k = 3`

The output will be:

```
AB
CA
AD
``` 

This solution effectively divides the input string into segments, removes duplicate characters from each segment while maintaining their order, and prints each processed segment.
