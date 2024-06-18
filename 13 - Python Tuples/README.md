# Problem Statement 
**URL : [Python Tuples](https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/cffa0cf8-7ffb-4e46-a070-4a019a59fc2f)

# Problem Solution 
```
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    my_tuple = tuple(integer_list)
    hash_value = hash(my_tuple)
    
    print(hash_value)
```

## Code Explanation

-   **Entry Point Check**:
  
    `if __name__ == '__main__':` 
   
    This line ensures that the code inside the block only runs if the script is executed directly. It won't run if the 	
    script is imported as a module in another script.
    
-   **Reading the Number of Elements**:
  
    `n = int(input())` 
    
    -   `input()` reads a line of input from the user.
    -   `int(input())` converts the input to an integer. This integer `n` represents the number of elements in the tuple.
-   **Reading the Space-Separated Integers**:

    `integer_list = map(int, input().split())` 
    
    -   `input().split()` reads a line of input from the user and splits it into a list of strings using spaces as the delimiter.
    -   `map(int, input().split())` applies the `int` function to each element of the list, converting each string to an integer. This results in a map object of integers.
-   **Creating the Tuple**:
    
    `my_tuple = tuple(integer_list)` 
    
    -   `tuple(integer_list)` converts the map object into a tuple. The tuple `my_tuple` now contains the integers provided by the user.
    
-   **Calculating the Hash Value**:

    `hash_value = hash(my_tuple)` 
    
    -   `hash(my_tuple)` computes the hash value of the tuple. The `hash` function returns an integer which is the hash value of the object passed to it.
    
-   **Printing the Hash Value**:
    
    `print(hash_value)` 
    
    -   `print(hash_value)` outputs the computed hash value to the console.
