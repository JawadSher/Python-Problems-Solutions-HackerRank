<h1 align='center'>The - Captain's - Room</h1>

## Problem Statement

**Problem URL :** [The Captain's Room](https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/a4b38364-ad9f-4d22-b14c-45cf9d6cc58e)
![image](https://github.com/user-attachments/assets/3b8f1328-8e76-45df-9206-f341c9f95a2e)


## Problem Explanation
The problem you're addressing involves processing a list of room numbers to find one specific number with a particular characteristic. Here's a detailed explanation of the problem statement:

**Objective**: Given a list of room numbers where every room number appears an even number of times except for one room number, which appears exactly once, identify and print the room number that appears only once.

### Detailed Problem Breakdown

1. **Input**:
   - An integer `K` representing the number of room numbers in the list.
   - A list of `K` integers where each integer represents a room number. All room numbers except one appear an even number of times (at least twice).

2. **Output**:
   - Print the room number that appears exactly once in the list.

### Example

**Input**:
```
7
1 1 2 2 3 3 4
```

**Explanation**:
- The list contains room numbers: `[1, 1, 2, 2, 3, 3, 4]`.
- In this list:
  - Room number `1` appears twice.
  - Room number `2` appears twice.
  - Room number `3` appears twice.
  - Room number `4` appears only once.
- The unique room number that appears only once is `4`.

**Output**:
```
4
```

### Constraints and Assumptions

1. **Room Numbers**: The list of room numbers is provided and should be processed to determine the unique room number.
2. **Uniqueness**: The problem guarantees that there is exactly one room number that appears exactly once. All other numbers appear an even number of times.
3. **Edge Cases**: Ensure the program handles cases where the room numbers list has only a few entries, and the unique room number is the only one not repeated.

### Approach

The approach involves:
1. Reading the input list of room numbers.
2. Using a `Counter` from the `collections` module to count the occurrences of each room number.
3. Identifying the room number with a count of `1` (which appears only once).
4. Printing that room number.

This problem leverages counting techniques to find the unique element efficiently, using the `Counter` class to handle the counting and then processing the results to find the unique value.


## Problem Solution
```py
from collections import Counter

K = int(input())
rooms = map(int, input().split())
rooms_counting = Counter(rooms)
captain_room = -1

for i in rooms_counting:
    if rooms_counting[i] == 1:
        captain_room  = i

print(captain_room)
```

## Problem Solution Explanation
Let's break down and explain the provided code in detail. The code is designed to find a specific room number from a list of room numbers where each room number appears multiple times except for one, which appears exactly once. This unique room number is referred to as the "captain's room."

#### 1. Import the `Counter` Class
```python
from collections import Counter
```
- **Purpose**: Imports the `Counter` class from the `collections` module. `Counter` is a specialized dictionary used for counting hashable objects. It will help us count how many times each room number appears.

#### 2. Read Input
```python
K = int(input())
```
- **Purpose**: Reads an integer from the input. This integer (`K`) represents the number of room numbers that will follow. Although `K` is not used further in the code, it is typically read to match the expected format of the input data.

```python
rooms = map(int, input().split())
```
- **Purpose**: Reads a line of input, splits it into individual strings, converts each string to an integer, and creates an iterator of integers (`rooms`). This represents the room numbers.

#### 3. Count Occurrences
```python
rooms_counting = Counter(rooms)
```
- **Purpose**: Uses the `Counter` class to count the occurrences of each room number in the `rooms` iterator. The `rooms_counting` variable is now a `Counter` object that behaves like a dictionary where the keys are room numbers, and the values are their counts. For example, if the input room numbers were `[1, 2, 2, 3]`, `rooms_counting` would be `Counter({2: 2, 1: 1, 3: 1})`.

#### 4. Initialize the Captain’s Room
```python
captain_room = -1
```
- **Purpose**: Initializes the variable `captain_room` to `-1`. This variable will eventually store the room number that appears exactly once. If no room number appears exactly once, `captain_room` will remain `-1`.

#### 5. Find the Captain’s Room
```python
for i in rooms_counting:
    if rooms_counting[i] == 1:
        captain_room  = i
```
- **Purpose**: Iterates over each room number in `rooms_counting`:
  - **Condition**: Checks if the count of the room number `i` is `1` using `rooms_counting[i] == 1`.
  - **Action**: If the count is `1`, it means this room number appears exactly once in the list, so it assigns this room number to `captain_room`. If there are multiple room numbers that appear only once, `captain_room` will be updated to the last one found.

#### 6. Print the Captain’s Room
```python
print(captain_room)
```
- **Purpose**: Prints the room number stored in `captain_room`. If a unique room number was found, it prints that number. If no room number appeared exactly once, it prints `-1`.

### Example

**Input**:
```
7
1 1 2 2 3 3 4
```

**Output**:
```
4
```

**Explanation**:
- The input consists of room numbers where each number except `4` appears twice.
- `4` appears exactly once.
- Therefore, `captain_room` will be `4`, and `print(captain_room)` outputs `4`.

### Summary

The code reads a list of room numbers, counts the occurrences of each number using `Counter`, and identifies the number that appears exactly once. If such a number exists, it prints that number; otherwise, it prints `-1`.
