<h1 align='center'>Introduction - To - Sets</h1>

## Problem Statemeent

**Problem URL :** [Introduction to Sets](https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/b5d64fd3-43e6-4e0f-b289-21fb4c5d7df9)
![image](https://github.com/user-attachments/assets/15aa432d-3f90-4239-8776-fa61ac9aa53d)
![image](https://github.com/user-attachments/assets/42827f92-03b6-4fdf-9da7-6515be06073f)

## Problem Solution 
```python
def average(array):
    nums = set(array)
    n = len(nums)
   
    total_sum = 0
   
    for i in nums:
       total_sum += i
    
    average = total_sum/n
    return round(average, 3)    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
```

## Problem Solution Explanation
Here’s a line-by-line explanation of the code:

### Function Definition: `average(array)`
1. **`def average(array):`**  
   Defines a function named `average` that takes one argument `array`.

2. **`nums = set(array)`**  
   Converts `array` into a set called `nums`. This removes any duplicate values from `array` because sets do not allow duplicate elements.

3. **`n = len(nums)`**  
   Calculates the number of unique elements in `nums` and stores it in the variable `n`.

4. **`total_sum = 0`**  
   Initializes a variable `total_sum` to 0. This variable will be used to accumulate the sum of the unique elements.

5. **`for i in nums:`**  
   Starts a loop that iterates over each element `i` in the set `nums`.

6. **`total_sum += i`**  
   Adds the current element `i` to `total_sum`.

7. **`average = total_sum / n`**  
   Calculates the average of the unique elements by dividing `total_sum` by `n`.

8. **`return round(average, 3)`**  
   Returns the average rounded to 3 decimal places using the `round` function.

### Main Execution Block
9. **`if __name__ == '__main__':`**  
   This line checks if the script is being run directly (not imported as a module). If it is, the code inside this block will execute.

10. **`n = int(input())`**  
    Reads an integer from user input and assigns it to `n`. This integer represents the number of elements in the array.

11. **`arr = list(map(int, input().split()))`**  
    Reads a line of input, splits it into individual strings, converts each string to an integer, and then creates a list of these integers. This list is assigned to `arr`.

12. **`result = average(arr)`**  
    Calls the `average` function with `arr` as the argument and stores the returned result in the variable `result`.

13. **`print(result)`**  
    Prints the result of the `average` function, which is the average of the unique elements in the array rounded to 3 decimal places.

### Summary
- The code defines a function `average` to compute the average of unique elements in a list.
- It reads input values, processes them to compute the average, and prints the result rounded to three decimal places.
