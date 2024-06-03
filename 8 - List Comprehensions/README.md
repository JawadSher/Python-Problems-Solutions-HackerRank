# Problem Statement 
**URL : [List Comprehensions](https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/4832db89-cca3-4d22-947c-dafbb4c4d257)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/05f5488c-5261-45b8-9f11-1e56287f8972)

# Problem Solution 
```
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    cuboid_list = [[i, j, k] for i in range(x+1) for j in range(y+1)
                    for k in range(z+1) if(i + j + k) != n]
    print(cuboid_list)
```

## Code Explanation
This source code is a Python script that generates a list of all possible coordinates within a cuboid (a 3D rectangular solid) with dimensions x, y, and z, where the sum of the coordinates (i, j, k) does not equal n. Here's a breakdown of the code:

```if __name__ == '__main__':``` :
This line ensures that the following code block will only run if the script is executed directly, not if it's imported as a module into another script.

```x = int(input()), y = int(input()), z = int(input()), n = int(input()):``` :
These lines prompt the user to input four integers (x, y, z, and n) representing the dimensions of the cuboid (x, y, z) and the target sum (n). int(input()) is used to convert the input strings to integers.

```cuboid_list = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if(i + j + k) != n]:``` :
This is a list comprehension that generates a list of coordinates (i, j, k) within the cuboid.
It iterates over all possible combinations of i ranging from 0 to x, j ranging from 0 to y, and k ranging from 0 to z.
For each combination, it checks if the sum of i, j, and k is not equal to n.
If the condition is met, the coordinates [i, j, k] are added to the cuboid_list.

```print(cuboid_list):``` :
Finally, the script prints the cuboid_list, which contains all valid coordinates within the cuboid where the sum of coordinates is not equal to n.

