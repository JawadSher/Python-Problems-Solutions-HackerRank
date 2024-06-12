# Problem Statement 
**URL : [Finding the Percentage](https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/ae00c9f1-ae16-4c24-8e70-23ab48e4cea3)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/1bd01b3a-aada-4d46-b925-ae27b1472348)

# Problem Solution
```
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    if query_name in student_marks:
        marks = student_marks[query_name]
        average = sum(marks) / len(marks)
        print("{:.2f}".format(average))
```

## Code Explanation
The provided source code is a Python script that calculates the average marks of a student based on the input provided.

1. **Reading Input :**
   - It first reads an integer n from input, representing the number of students.
   - Then it initializes an empty dictionary student_marks to store the marks of each student.
   - It iterates n times to read the input for each student. For each student:
       - It reads the name of the student followed by their marks separated by spaces.
       - It converts the marks from strings to floats and stores them in a list.
       - It stores the name of the student as a key and their marks as a list in the student_marks dictionary.

2. **Calculating Average :**
   - After reading all the input, it reads the name of the student for which the average marks need to be calculated.
   - If the student's name exists in the student_marks dictionary:
       - It retrieves the list of marks for the student.
       - It calculates the average of the marks by summing them up and dividing by the total number of marks.
       - It prints the average marks with two decimal places.
    
- ```if __name__ == '__main__':``` :
    - This line checks if the script is being run directly as the main program.
    - If it is, the code block below it will be executed.

- ```n = int(input())``` :
   - Reads an integer from the standard input (usually the keyboard) and assigns it to the variable `n`.
   - This integer represents the number of students.

-   `student_marks = {}` :
    -   Initializes an empty dictionary named `student_marks` to store the marks of each student.
   
-  `for _ in range(n):` :
	- Iterates `n` times to read the input for each student.
	- The underscore `_` is used as a placeholder variable because the loop doesn't need to use the loop variable.

-   `name, *line = input().split()` :
    -   Reads a line of input, splits it into words, and assigns the first word to the variable `name`.
    -   The remaining words are collected into a list called `line`.
    -   This line effectively separates the student's name from their marks in the input.
    
-   `scores = list(map(float, line))` :
    -   Converts each mark (which is initially a string) in the list `line` to a float and creates a list of floats called `scores`.
    -   `map(float, line)` applies the `float` function to each element of `line`.
    -   `list(...)` converts the result of `map` into a list.
    
-   `student_marks[name] = scores` :
    -   Assigns the list of marks `scores` to the dictionary `student_marks` with the student's name `name` as the key.
    -   This effectively stores the marks of each student in the dictionary.
-   `query_name = input()`
    -   Reads a line of input, which is assumed to be the name of the student for which the average marks need to be calculated.
    
-   `if query_name in student_marks:` :
    -   Checks if the entered `query_name` exists in the `student_marks` dictionary.
    -   If it does, it means marks are available for the specified student, so the script proceeds to calculate the average.

-   `marks = student_marks[query_name]` :
    -   Retrieves the list of marks for the student specified by `query_name` from the `student_marks` dictionary.
    
-   `average = sum(marks) / len(marks)` :
    -   Calculates the average of the marks by summing them up and dividing by the total number of marks.
    
-   `print("{:.2f}".format(average))` :
    -   Prints the average marks with two decimal places. The `{:.2f}` format specifier ensures that the floating-point number is displayed with two decimal places.
