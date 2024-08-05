<h1 align='center'>Nested - Lists</h1>

## Problem Statement
**Problem URL : [Nested Lists](https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/0bb4e2fe-788a-418d-9498-7664fb130c10)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/b1cb4d2c-c9c5-49e5-9b2a-b89ade9238bb)

## Problem Explanation

Given the names and grades for each student in a class of `N` students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
**Input Format**:
- The first line contains an integer, `N`, the number of students.
- The `2N` subsequent lines describe each student over `2` lines:
  - The first line contains a student's name.
  - The second line contains their grade.

**Output Format**:
- Print the name(s) of any student(s) having the second lowest grade.
- If there are multiple students, order their names alphabetically and print each one on a new line.

## Example

**Input** :
  5
  Harry
  37.21
  Berry
  37.21
  Tina
  37.2
  Akriti
  41
  Harsh
  39

**Output** : Berry Harry

## Problem Solution 
```
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append((name, score))

    students_sorted = sorted(students, key=lambda x: (x[1], x[0]))      
    
    lowestGrade = students_sorted[0][1]
    secLowestGrade = None
    
    for student in students_sorted:
        if student[1] > lowestGrade:
            secLowestGrade = student[1]
            break
    
    studentNames = [student[0] for student in students_sorted if secLowestGrade == student[1]]
    studentNames.sort()
    for names in studentNames:
        print(names)
```

## Problem Solution Explanation 

```python
if __name__ == '__main__':
```
- This line checks if the script is being run directly (as opposed to being imported as a module). If it is run directly, the code block following this line will be executed.

```python
    students = []
```
- Initializes an empty list `students` to store tuples of student names and their scores.

```python
    for _ in range(int(input())):
```
- This line starts a `for` loop that will iterate a number of times equal to the integer input provided by the user. Each iteration processes one student’s data.

```python
        name = input()
```
- Reads a string input from the user representing the student's name and stores it in the variable `name`.

```python
        score = float(input())
```
- Reads a numeric input from the user, converts it to a floating-point number using `float()`, and stores it in the variable `score`.

```python
        students.append((name, score))
```
- Appends a tuple `(name, score)` to the `students` list, storing the student's name and score together.

```python
    students_sorted = sorted(students, key=lambda x: (x[1], x[0]))
```
- Sorts the `students` list. The `sorted()` function is used with a `lambda` function as the `key` parameter:
  - `lambda x: (x[1], x[0])` means that sorting is first done by the second element of the tuple (the score) in ascending order. If scores are equal, sorting is then done by the first element (the name) in ascending order.
- The sorted list is stored in `students_sorted`.

```python
    lowestGrade = students_sorted[0][1]
```
- Sets `lowestGrade` to the score of the first student in the sorted list. Since the list is sorted by score, this will be the lowest score.

```python
    secLowestGrade = None
```
- Initializes `secLowestGrade` to `None`. This variable will later hold the second lowest score.

```python
    for student in students_sorted:
```
- Starts a `for` loop to iterate over each student in the sorted list.

```python
        if student[1] > lowestGrade:
```
- Checks if the student's score is greater than `lowestGrade`. This helps in identifying the second lowest score.

```python
            secLowestGrade = student[1]
            break
```
- If the condition is met, assigns the student's score to `secLowestGrade` and breaks out of the loop. This is because the first score greater than the lowest score is the second lowest score.

```python
    studentNames = [student[0] for student in students_sorted if secLowestGrade == student[1]]
```
- Creates a list of names of students whose score matches `secLowestGrade`. This is done using a list comprehension that filters the students based on their score.

```python
    studentNames.sort()
```
- Sorts the list of student names in alphabetical order.

```python
    for names in studentNames:
        print(names)
```
- Iterates over the sorted list of student names and prints each name.

### Summary
This script processes student data, identifies the second lowest score, and prints the names of students who have that second lowest score in alphabetical order.


