# Problem Statement 
**URL : [Python Lists](https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/6ad41091-99a5-4c0d-a9d3-4286b5bca0af)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/503fe67f-a259-4485-926e-5d4fdcd3c160)

# Problem Solution 
```
if __name__ == '__main__':
    n = int(input())
    my_list = []
    
    for i in range(n):
        HR_input = input().split()
        functions = HR_input[0]
        numbers = list(map(int, HR_input[1:]))
        
        if functions == 'insert':
            my_list.insert(int(numbers[0]), int(numbers[1]))
        elif functions == 'print':
            print(my_list)
        elif functions == 'remove':
            my_list.remove(int(numbers[0]))
        elif functions == 'append':
            my_list.append(int(numbers[0]))
        elif functions == 'sort':
            my_list.sort()
        elif functions == 'pop':
            my_list.pop()
        elif functions == 'reverse':
            my_list.reverse()
```

## Code Explanation
This source code is designed to handle various list operations based on user input. Let's break down what each part does:

-   **`if __name__ == '__main__':`**
    
    -   This line checks if the script is being run directly (as opposed to being imported as a module).
-   **`n = int(input())`**
    
    -   Reads an integer `n` from the user input. This specifies the number of operations that will follow.
-   **`my_list = []`**
    
    -   Initializes an empty list `my_list` which will be manipulated based on the subsequent input operations.
-   **`for i in range(n):`**
    
    -   Loops `n` times to process `n` operations.
-   **`HR_input = input().split()`**
    
    -   Reads a line of input and splits it into a list of strings based on whitespace.
-   **`functions = HR_input[0]`**
    
    -   Retrieves the first element from `HR_input`, which indicates the operation to be performed on `my_list`.
-   **`numbers = list(map(int, HR_input[1:]))`**
    
    -   Converts the remaining elements of `HR_input` into integers and stores them in `numbers`. These are the arguments for the operation specified by `functions`.
-   **Operation Handling:**
    
    -   The script uses conditional statements `if`, `elif` to determine which list operation to perform based on the value of `functions`:
        -   **`insert`**: Inserts an element into `my_list` at a specified position.
        -   **`print`**: Prints the current contents of `my_list`.
        -   **`remove`**: Removes the first occurrence of a specified value from `my_list`.
        -   **`append`**: Appends a value to the end of `my_list`.
        -   **`sort`**: Sorts `my_list` in ascending order.
        -   **`pop`**: Removes and returns the last element from `my_list`.
        -   **`reverse`**: Reverses the order of elements in `my_list`.



