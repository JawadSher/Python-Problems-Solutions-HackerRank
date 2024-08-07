<h1 align='center'>Set - .Add()</h1>

## Problem Statement

**Problem URL :** [Set .add()](https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/d001c776-1f80-481d-b621-2ba693f5d4aa)
![image](https://github.com/user-attachments/assets/f7d25ac2-5374-43e9-ab72-f831ffae6230)

## Problem Solution 

```python
N = int(input().strip())

unique_countries = set()
for i in range(N):
    country = str(input().strip())
    unique_countries.add(country)

unique_count = len(unique_countries)
print(unique_count)
    
```

## Problem Explanation

Here’s a line-by-line explanation of the code:

```python
N = int(input().strip())
```
- `input()` reads a line of input from the user.
- `.strip()` removes any extra spaces or newline characters from the input.
- `int()` converts the cleaned input into an integer.
- `N` stores this integer, which represents the number of countries the user will input.

```python
unique_countries = set()
```
- `set()` creates an empty set named `unique_countries`.
- A set is a collection that automatically removes duplicate values, so it will only store unique countries.

```python
for i in range(N):
```
- `range(N)` generates a sequence of numbers from 0 up to (but not including) `N`.
- `for i in range(N)` starts a loop that will iterate `N` times.

```python
    country = str(input().strip())
```
- `input()` reads a line of input from the user, which is expected to be a country name.
- `.strip()` removes any extra spaces or newline characters from the input.
- `str()` ensures the input is treated as a string (this is usually not necessary here, but it's good practice).
- `country` stores this cleaned string value, representing the name of a country.

```python
    unique_countries.add(country)
```
- `unique_countries.add(country)` adds the `country` to the set `unique_countries`.
- Since `unique_countries` is a set, it will automatically handle duplicates, so each country is stored only once.

```python
unique_count = len(unique_countries)
```
- `len(unique_countries)` calculates the number of unique countries stored in the set.
- `unique_count` stores this number.

```python
print(unique_count)
```
- `print(unique_count)` outputs the number of unique countries to the screen.

### Summary:
The code reads `N` country names from the user, adds them to a set to ensure uniqueness, and then prints the total number of unique countries.
