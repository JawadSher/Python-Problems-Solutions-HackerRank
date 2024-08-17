<h1 align='center'>Campany - Logo</h1>

## Problem Statement

**Problem URL :** [Campany Logo](https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/4c7d1971-11bf-4b6c-9184-5395ca6804b8)
![image](https://github.com/user-attachments/assets/247dc778-854f-4bda-a117-3e7417a875a8)

## Problem Solution
```py
from collections import Counter

def print_top_three_characters(s):
    frequency = Counter(s)
    
    sorted_characters = sorted(frequency.items(), key=lambda item : (-item[1], item[0]))
    
    for i in range(min(3, len(sorted_characters))):
        char, count = sorted_characters[i]
        print(f'{char} {count}')

if __name__ == '__main__':
    s = input().strip() 
    print_top_three_characters(s)
```

## Problem Solution Explanation

Let's break down the code you've provided, which prints the top three most frequent characters in a string, sorted by frequency and then alphabetically if the frequencies are the same.

#### 1. **Importing `Counter` from `collections`**:
   ```python
   from collections import Counter
   ```
   - `Counter` is a specialized dictionary subclass from the `collections` module that helps count the occurrences of each element in a collection. Here, it's used to count the frequency of characters in the string.

#### 2. **Defining the Function `print_top_three_characters`**:
   ```python
   def print_top_three_characters(s):
       frequency = Counter(s)
   ```
   - The function `print_top_three_characters(s)` takes a string `s` as input.
   - `frequency = Counter(s)` creates a `Counter` object that counts the occurrences of each character in the string `s`.

   **Example**:
   - If `s = "aabbbcc"`, `frequency` would be `Counter({'b': 3, 'a': 2, 'c': 2})`.

#### 3. **Sorting the Characters by Frequency and Alphabetically**:
   ```python
   sorted_characters = sorted(frequency.items(), key=lambda item: (-item[1], item[0]))
   ```
   - `frequency.items()` returns a list of tuples where each tuple contains a character and its frequency, e.g., `[('a', 2), ('b', 3), ('c', 2)]`.
   - The `sorted()` function sorts these tuples based on a custom key provided by the `lambda` function.
     - `-item[1]` sorts the characters by frequency in descending order (because of the negative sign).
     - `item[0]` sorts the characters alphabetically in ascending order if frequencies are the same.

   **Example**:
   - For the string `s = "aabbbcc"`, the sorted result will be `[('b', 3), ('a', 2), ('c', 2)]`.

#### 4. **Printing the Top Three Characters**:
   ```python
   for i in range(min(3, len(sorted_characters))):
       char, count = sorted_characters[i]
       print(f'{char} {count}')
   ```
   - This loop iterates through the first three elements of `sorted_characters` (or fewer if there are less than three characters).
   - `char, count = sorted_characters[i]` unpacks each tuple into the character (`char`) and its frequency (`count`).
   - `print(f'{char} {count}')` prints the character and its frequency.

   **Example**:
   - Continuing with the example `s = "aabbbcc"`, the output will be:
     ```
     b 3
     a 2
     c 2
     ```

#### 5. **Main Execution Block**:
   ```python
   if __name__ == '__main__':
       s = input().strip() 
       print_top_three_characters(s)
   ```
   - This block ensures the script runs only when executed directly (not when imported as a module).
   - `s = input().strip()` takes input from the user and removes any leading or trailing whitespace.
   - `print_top_three_characters(s)` is then called to print the top three most frequent characters in the string.

### Full Example Walkthrough

Let's go through an example to see how this works step by step.

#### Example Input:
```python
s = "aabbbccccdddde"
```

1. **Counting Frequencies**:
   - `Counter(s)` would yield:
     ```
     {'c': 4, 'd': 4, 'b': 3, 'a': 2, 'e': 1}
     ```

2. **Sorting**:
   - Sorted by frequency (descending) and alphabetically (ascending) for ties:
     ```
     [('c', 4), ('d', 4), ('b', 3), ('a', 2), ('e', 1)]
     ```

3. **Printing the Top Three**:
   - The top three characters are `'c'`, `'d'`, and `'b'`.
   - Output:
     ```
     c 4
     d 4
     b 3
     ```

This code efficiently identifies the most frequent characters in a string and displays the top three, prioritizing higher frequencies and resolving ties alphabetically.
