<h1 align='center'>Zipped!</h1>

## Problem Statement

**Problem URL :** [Zipped!](https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/76959829-32d5-478d-b95d-1e77eda69684)
![image](https://github.com/user-attachments/assets/74a2fdc8-4a83-4408-b89e-e775ffda61d8)
![image](https://github.com/user-attachments/assets/39131802-05cb-4910-998e-c1e23b6dc49a)
![image](https://github.com/user-attachments/assets/4fe71cfb-978b-4eb2-982e-b25b0f5c19f9)

## Problem Solution
```py
N, X = map(int, input().split())

actual_marks = []
avg_marks = []

for _ in range(X):
    marks = map(float, input().split())
    actual_marks.append(marks)
    
stdnt_marks = zip(*actual_marks)

for marks in stdnt_marks:
    avg_marks.append(sum(marks)/X)
    
for i in avg_marks:
    print(i)
```

## Problem Solution Explanation
Let's break down this Python code step by step, explaining it in detail for beginners. We'll use an example to illustrate how the code works.

1. **Input Parsing:**
   ```python
   N, X = map(int, input().split())
   ```
   - **`input()`**: This function takes a single line of input from the user.
   - **`split()`**: This method splits the input string by spaces and returns a list of substrings.
   - **`map(int, input().split())`**: The `map()` function applies the `int()` function to each element in the list returned by `split()`, converting the input to integers. In this case, the input provides two numbers:
     - `N`: The number of students.
     - `X`: The number of subjects.

   **Example:**  
   If the input is `3 2`, then `N = 3` (3 students) and `X = 2` (2 subjects).

2. **Initializing Lists:**
   ```python
   actual_marks = []
   avg_marks = []
   ```
   - **`actual_marks`**: An empty list that will store the marks of all students across subjects.
   - **`avg_marks`**: An empty list that will store the average marks for each student.

3. **Reading Marks:**
   ```python
   for _ in range(X):
       marks = map(float, input().split())
       actual_marks.append(marks)
   ```
   - **`for _ in range(X)`**: A loop that runs `X` times (once for each subject).
   - **`map(float, input().split())`**: This reads the marks for a subject, converts them to floating-point numbers, and stores them in a list.
   - **`actual_marks.append(marks)`**: Appends the list of marks for that subject to the `actual_marks` list.

   **Example:**  
   If the input for two subjects is:
   ```
   89.5 78.0 92.0
   75.0 88.5 82.0
   ```
   The `actual_marks` list would look like:
   ```python
   actual_marks = [
       [89.5, 78.0, 92.0],  # Marks for subject 1
       [75.0, 88.5, 82.0]   # Marks for subject 2
   ]
   ```

4. **Transposing the Marks:**
   ```python
   stdnt_marks = zip(*actual_marks)
   ```
   - **`zip(*actual_marks)`**: This is a clever trick to transpose the list of marks. It rearranges the list so that each tuple contains all the marks for a single student across all subjects.

   **Example:**  
   After transposing, `stdnt_marks` would look like:
   ```python
   stdnt_marks = [
       (89.5, 75.0),  # Marks for student 1
       (78.0, 88.5),  # Marks for student 2
       (92.0, 82.0)   # Marks for student 3
   ]
   ```

5. **Calculating Averages:**
   ```python
   for marks in stdnt_marks:
       avg_marks.append(sum(marks)/X)
   ```
   - **`for marks in stdnt_marks`**: Loops through each tuple of marks for the students.
   - **`sum(marks)/X`**: Calculates the average of the marks for each student.
   - **`avg_marks.append(...)`**: Stores the average marks in the `avg_marks` list.

   **Example:**  
   The averages for the students would be:
   ```python
   avg_marks = [
       (89.5 + 75.0) / 2,  # Average for student 1 = 82.25
       (78.0 + 88.5) / 2,  # Average for student 2 = 83.25
       (92.0 + 82.0) / 2   # Average for student 3 = 87.00
   ]
   ```

6. **Printing Averages:**
   ```python
   for i in avg_marks:
       print(i)
   ```
   - This loop simply prints the average marks for each student.

   **Example Output:**
   ```
   82.25
   83.25
   87.0
   ```

### Example Walkthrough:
Let's say the input is:
```
3 2
89.5 78.0 92.0
75.0 88.5 82.0
```

**Output:**
```
82.25
83.25
87.0
```

This output corresponds to the average marks for each of the three students across two subjects. 

### Conclusion:
This code effectively calculates and prints the average marks for each student based on the marks entered for multiple subjects. By using techniques like list transposition (`zip(*...)`) and floating-point arithmetic, it handles the input and output in a streamlined way.
