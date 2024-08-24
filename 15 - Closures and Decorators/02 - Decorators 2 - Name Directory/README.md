<h1 align='center'>Decorators 2 - Name - Directory</h1>

## Problem Statement

**Problem URL :** [Decorators 2 - Name Directory](https://www.hackerrank.com/challenges/decorators-2-name-directory/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/ab0841c8-7ec3-423e-a695-6f16a94b9dbf)
![image](https://github.com/user-attachments/assets/35976a1d-2ab8-4408-8ca8-7f485084c706)

## Problem Solution
```py
import operator

def person_lister(f):
    def inner(people):
        sorted_info = sorted(people, key=lambda x : int(x[2]))
        return [f(i) for i in sorted_info]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
```

## Problem Solution Explanation
This code defines a decorator `person_lister` and a function `name_format` to format and sort a list of people based on their age. Let's go through the code line by line.

### Import Statement
```python
import operator
```
- Although `operator` is imported, it is not used in this code, so this line is unnecessary.

### Decorator Definition: `person_lister`
```python
def person_lister(f):
    def inner(people):
        sorted_info = sorted(people, key=lambda x : int(x[2]))
        return [f(i) for i in sorted_info]
    return inner
```
- `person_lister` is a decorator function that takes another function `f` as an argument.
- **Inner Function (`inner`)**:
  - `inner` is a nested function inside `person_lister` that takes `people` (a list of people) as an argument.
  - `sorted_info` is a list of people sorted by their age. The lambda function `lambda x: int(x[2])` converts the age (which is a string at index 2 of each person's list) to an integer and uses it as the sorting key.
  - The function `f` (which will be `name_format`) is then applied to each person in `sorted_info`, and the results are returned as a list.
- Finally, `inner` is returned from `person_lister`, effectively replacing the original function `f` with `inner`.

### Function Definition: `name_format`
```python
@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]
```
- `name_format` is a function that formats a person's name based on their gender.
- The function checks if the person is male (`person[3] == "M"`) or female, and prefixes the name with "Mr." or "Ms." accordingly.
- The full name is then constructed using the first name (`person[0]`) and the last name (`person[1]`).
- The `@person_lister` decorator is applied to `name_format`, so when `name_format` is called, it first sorts the list of people by age using `person_lister`.

### Main Execution Block
```python
if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
```
- This block handles the input and output:
  - It first reads an integer `n`, which indicates the number of people to input.
  - It then reads `n` lines of input, where each line contains a person's information: first name, last name, age, and gender.
  - `input().split()` splits each line into a list of strings, and all these lists are stored in `people`.
  - `name_format(people)` is called to format and sort the list of people. The result is printed line by line using `print(*..., sep='\n')`.

### Example Execution

1. **Input:**
    ```plaintext
    3
    John Doe 25 M
    Jane Smith 30 F
    Alice Brown 22 F
    ```

2. **Processing:**
    - The input is split into the following list of lists:
      ```python
      people = [["John", "Doe", "25", "M"], ["Jane", "Smith", "30", "F"], ["Alice", "Brown", "22", "F"]]
      ```
    - The `person_lister` decorator sorts this list by age:
      ```python
      sorted_info = [["Alice", "Brown", "22", "F"], ["John", "Doe", "25", "M"], ["Jane", "Smith", "30", "F"]]
      ```
    - `name_format` is then applied to each sorted person:
      - For Alice Brown: `"Ms. Alice Brown"`
      - For John Doe: `"Mr. John Doe"`
      - For Jane Smith: `"Ms. Jane Smith"`

3. **Output:**
    The formatted names are printed in the following order:
    ```plaintext
    Ms. Alice Brown
    Mr. John Doe
    Ms. Jane Smith
    ```

### Summary
- The code sorts a list of people by age and formats their names based on gender.
- The decorator `person_lister` is used to sort the list before formatting it.
- The final output is a list of names, each prefixed with "Mr." or "Ms." and printed in ascending order of age.
