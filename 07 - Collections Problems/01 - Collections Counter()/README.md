<h1 align='center'>Collections - Counter()</h1>

## Problem Statement

**Problem URL :** [Collections.Counter()](https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true) 

![image](https://github.com/user-attachments/assets/067a2bcc-ed37-4a85-804f-34695510b173)
![image](https://github.com/user-attachments/assets/0f994556-1cbc-4b05-9c51-41456fc850b7)
![image](https://github.com/user-attachments/assets/d51843a8-7237-4906-8a0d-3b40c00cd817)

## Problem Explanation

The `collections.Counter` class in Python is a very useful tool for counting hashable objects. It belongs to the `collections` module and is specifically designed to count occurrences of items in an iterable.

### Key Features:

1. **Initialization:**
   - You can initialize a `Counter` with an iterable (like a list or a string), or with a mapping (like a dictionary), or even with keyword arguments.
   ```python
   from collections import Counter

   # From an iterable
   c = Counter(['a', 'b', 'c', 'a', 'b', 'a'])
   # From a mapping
   c = Counter({'a': 3, 'b': 2, 'c': 1})
   # With keyword arguments
   c = Counter(a=3, b=2, c=1)
   ```

2. **Accessing Counts:**
   - The `Counter` object works like a dictionary where the keys are the elements and the values are their counts.
   ```python
   print(c['a'])  # Output: 3
   print(c['b'])  # Output: 2
   print(c['d'])  # Output: 0 (default value for missing keys)
   ```

3. **Common Operations:**
   - **Most Common Elements:** You can retrieve the most common elements in the `Counter` object.
   ```python
   print(c.most_common(2))  # Output: [('a', 3), ('b', 2)]
   ```
   - **Subtracting Counts:** You can perform operations like subtraction and addition on `Counter` objects.
   ```python
   c1 = Counter(a=3, b=2)
   c2 = Counter(a=1, b=3)
   print(c1 - c2)  # Output: Counter({'a': 2})
   ```

4. **Updating Counts:**
   - You can update the counts of an existing `Counter` with another iterable or mapping.
   ```python
   c.update(['a', 'b', 'b', 'd'])
   print(c)  # Output: Counter({'a': 4, 'b': 4, 'c': 1, 'd': 1})
   ```

5. **Arithmetic Operations:**
   - You can use arithmetic operators to combine `Counter` objects.
   ```python
   c1 = Counter(a=2, b=3)
   c2 = Counter(a=1, b=1)
   print(c1 + c2)  # Output: Counter({'a': 3, 'b': 4})
   print(c1 - c2)  # Output: Counter({'a': 1, 'b': 2})
   ```

6. **Cleaning Up:**
   - Negative or zero counts are removed by default.
   ```python
   c = Counter(a=3, b=-1)
   print(c)  # Output: Counter({'a': 3})
   ```

### Example Use Case:

Suppose you want to count the frequency of characters in a string and find the most common ones:

```python
from collections import Counter

text = "hello world"
counter = Counter(text)
print(counter)  # Output: Counter({'l': 3, 'o': 2, ' ': 1, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1})
print(counter.most_common(2))  # Output: [('l', 3), ('o', 2)]
```

In this example:
- `Counter(text)` counts each character in the string.
- `counter.most_common(2)` returns the two most common characters.

`collections.Counter` is highly efficient for frequency counting and provides a convenient way to handle such tasks with minimal code.

To solve this problem, we'll use the `collections.Counter` class to efficiently count the available shoe sizes in the shop and then determine how much money we can earn based on customer demands. Here’s a step-by-step breakdown of the task:

### Problem Breakdown

1. **Input Reading:**
   - **Number of Shoes (`n`):** The total number of shoes in the shop.
   - **List of Shoe Sizes:** A space-separated list of integers where each integer represents the size of a shoe in the shop.
   - **Number of Customers (`m`):** The total number of customers.
   - **Customer Demands:** For each customer, a line of input contains two integers:
     - **Size (`size`):** The desired size of the shoe.
     - **Price (`price`):** The amount the customer is willing to pay for that size.

2. **Objective:**
   - Determine how much money is earned by matching the shoes in the shop with the customers' desired sizes.

### Solution Approach

1. **Count Available Shoes:**
   - Use `Counter` from the `collections` module to count occurrences of each shoe size in the shop.

2. **Process Customer Requests:**
   - For each customer, check if the desired shoe size is available.
   - If available, add the price to the total earnings and reduce the count of that shoe size in the `Counter`.

3. **Print the Total Earnings:**
   - Output the total amount of money earned by the shop.


## Problem Solution 

```python
from collections import Counter

number_of_shoes = int(input().strip())
shoe_sizes = list(map(int, input().strip().split()))
number_of_customers = int(input().strip())

shoe_counter = Counter(shoe_sizes)
total_earnings = 0

for _ in range(number_of_customers):
    size, price = map(int, input().strip().split())
    
    if shoe_counter[size] > 0:
        total_earnings += price
        shoe_counter[size] -= 1
        
print(total_earnings)
```

## Problem Solution Explanation

```python
from collections import Counter
```
- **Importing `Counter`:** This imports the `Counter` class from the `collections` module. `Counter` is a dictionary subclass specifically designed to count hashable objects.

```python
number_of_shoes = int(input().strip())
```
- **Read Number of Shoes:** 
  - `input().strip()` reads a line of input from the user and removes any leading or trailing whitespace.
  - `int()` converts the input string to an integer.
  - `number_of_shoes` now holds the total count of different shoes available in the shop.

```python
shoe_sizes = list(map(int, input().strip().split()))
```
- **Read Shoe Sizes:**
  - `input().strip()` reads a line of input, which is expected to be space-separated shoe sizes.
  - `split()` splits the input string into a list of substrings based on spaces.
  - `map(int, ...)` converts each substring into an integer.
  - `list(...)` converts the result into a list of integers.
  - `shoe_sizes` now holds the sizes of all the shoes available in the shop.

```python
number_of_customers = int(input().strip())
```
- **Read Number of Customers:**
  - Similar to the first input line, this reads the total number of customers from user input and converts it to an integer.

```python
shoe_counter = Counter(shoe_sizes)
```
- **Count Shoe Sizes:**
  - `Counter(shoe_sizes)` creates a `Counter` object that counts the occurrences of each shoe size in the `shoe_sizes` list.
  - `shoe_counter` now holds a dictionary-like object where keys are shoe sizes and values are their respective counts.

```python
total_earnings = 0
```
- **Initialize Earnings:**
  - `total_earnings` is initialized to zero. This variable will keep track of the total money earned from selling shoes.

```python
for _ in range(number_of_customers):
```
- **Loop Over Customers:**
  - A loop is started to iterate over the number of customers. The loop will execute `number_of_customers` times.

```python
    size, price = map(int, input().strip().split())
```
- **Read Customer Request:**
  - `input().strip()` reads a line of input for each customer, which contains two space-separated values.
  - `split()` splits the input into two parts.
  - `map(int, ...)` converts these parts into integers: `size` (the desired shoe size) and `price` (the amount the customer is willing to pay).

```python
    if shoe_counter[size] > 0:
```
- **Check Shoe Availability:**
  - This condition checks if the requested shoe size is available (`shoe_counter[size] > 0`).
  - If the size is available (i.e., count is greater than zero), the following block executes.

```python
        total_earnings += price
```
- **Update Earnings:**
  - Adds the `price` to `total_earnings`, increasing the total money earned by the shop.

```python
        shoe_counter[size] -= 1
```
- **Decrease Shoe Count:**
  - Decreases the count of the available shoe size by 1 in `shoe_counter`, reflecting that one shoe of that size has been sold.

```python
print(total_earnings)
```
- **Output Total Earnings:**
  - Finally, the total earnings are printed, which represents the total amount of money earned from the sales.

### Summary

1. **Read Input:**
   - The code reads the number of shoes, the list of shoe sizes, the number of customers, and each customer’s request.

2. **Count Shoes:**
   - It counts the available sizes using `Counter`.

3. **Process Requests:**
   - For each customer, it checks if the requested shoe size is available.
   - If available, it updates the earnings and reduces the count of that shoe size.

4. **Print Result:**
   - Outputs the total amount of money earned from selling the shoes. 

This approach ensures efficient handling of shoe inventory and customer requests, leveraging the `Counter` class for quick lookups and updates.


