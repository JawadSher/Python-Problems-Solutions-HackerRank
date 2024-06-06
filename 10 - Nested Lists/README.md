# Problem Statement
**URL : [Nested Lists](https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/0bb4e2fe-788a-418d-9498-7664fb130c10)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/b1cb4d2c-c9c5-49e5-9b2a-b89ade9238bb)

# Problem Explanation

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

# Problem Solution 
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

## Code Explanation 
- **Initialization**
  
  ```students = []``` : An empty list is initialized to store the names and scores of students.

- **Input Reading**
  
  ```for _ in range(int(input())):``` : A loop runs for the number of students entered by the user.
  
  ```name = input():``` : Reads the student's name.
  
  ```score = float(input()):``` : Reads the student's score and converts it to a float.
  
  ```students.append((name, score)):``` : Appends a tuple of the student's name and score to the students list.
  
- **Sorting**
  
  ```students_sorted = sorted(students, key=lambda x: (x[1], x[0])):``` : Sorts the students list first by score (x[1]) and then by name (x[0]) in ascending order.
  
- **Finding the Lowest and Second Lowest Scores**
  
  ```lowestGrade = students_sorted[0][1]:``` : Assigns the lowest score from the sorted list.
  
  ```secLowestGrade = None``` : Initializes secLowestGrade to None.
  
  ```for student in students_sorted:``` : Iterates through the sorted student list to find the second lowest score.
  
  ```if student[1] > lowestGrade:``` : Checks if the current student's score is greater than the lowest score.
  
  ```secLowestGrade = student[1]``` : If true, assigns this score to secLowestGrade.
  
  ```break``` : Exits the loop once the second lowest score is found.
  
- **Collecting Student Names with Second Lowest Score**
  
  ```studentNames = [student[0] for student in students_sorted if secLowestGrade == student[1]]``` : Creates a list of student names who have the second lowest score.
  
- **Sorting and Printing Names**
  
  ```studentNames.sort()``` : Sorts the names alphabetically.
  
  ```for names in studentNames:``` : Iterates through the sorted names list.
  
  ```print(names)``` : Prints each name on a new line.


