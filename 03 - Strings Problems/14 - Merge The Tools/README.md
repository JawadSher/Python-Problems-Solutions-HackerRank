<h1 align='center'>Merge - The - Tools</h1>

## Problem Statement

**Problem URL** : [Merge The Tools](https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/00fab7ea-253d-432c-b731-75fd0e154325)
![image](https://github.com/user-attachments/assets/a126614a-544e-409c-b1e2-47e73a534cb8)


## Problem Explanation

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
## Problem Solution Explanation
Certainly! Here's a detailed line-by-line explanation of the code with an example:

```python
def merge_the_tools(string, k):
```
- Defines a function named `merge_the_tools` that takes two arguments:
  - `string`: the input string to be processed.
  - `k`: the length of each segment to be processed from the input string.

```python
  n = len(string)
```
- Calculates the length of the input string `string` and stores it in the variable `n`.

```python
  for i in range(0, n, k):
```
- Iterates over the indices of the string in steps of `k`. This creates segments of length `k` from the string.
  - `i` starts at `0` and increases by `k` each time, up to `n` (the length of the string).

```python
    result = ""
```
- Initializes an empty string `result` to build the unique characters of the current segment.

```python
    segment = string[i : i+k]
```
- Extracts a substring from `string` starting at index `i` and ending at index `i + k` (not inclusive). This substring is a segment of length `k`.

```python
    for char in segment:
```
- Iterates over each character `char` in the current `segment`.

```python
      if char not in result:
```
- Checks if the current character `char` is not already present in `result`.

```python
        result += char
```
- If `char` is not in `result`, it is appended to `result`. This ensures that each character in the segment appears only once in the `result` string.

```python
    print(result)
```
- Prints the `result` string, which contains unique characters of the current segment.

```python
if __name__ == '__main__':
```
- Checks if the script is being run directly (not imported as a module). If so, the code block following this line will be executed.

```python
    string, k = input(), int(input())
```
- Reads two inputs from the user:
  - The first input is the string `string`.
  - The second input is converted to an integer and assigned to `k`.

```python
    merge_the_tools(string, k)
```
- Calls the `merge_the_tools` function with `string` and `k` as arguments to process the string and print the results.

### Example

Consider the following input:

```
string: "AABCAAADA"
k: 3
```

Here’s how the code works step by step:

1. **Initial Inputs:**
   - `string = "AABCAAADA"`
   - `k = 3`

2. **Processing:**
   - **First Segment (`i = 0`):**
     - `segment = "AAB"`
     - Unique characters: "AB"
     - `result = "AB"`
     - Output: `AB`

   - **Second Segment (`i = 3`):**
     - `segment = "CAA"`
     - Unique characters: "CA"
     - `result = "CA"`
     - Output: `CA`

   - **Third Segment (`i = 6`):**
     - `segment = "ADA"`
     - Unique characters: "AD"
     - `result = "AD"`
     - Output: `AD`

3. **Final Output:**
   - The function prints:
     ```
     AB
     CA
     AD
     ```

Each segment of length `k` is processed to remove duplicate characters, and the unique characters of each segment are printed on separate lines.
