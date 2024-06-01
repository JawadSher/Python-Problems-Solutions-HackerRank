# Problem Statement 
**URL : [Python If-Else](https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/f0695e5c-fefa-46c3-af46-4fa07126fdb6)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/44792e82-39cb-48af-a84a-8543898058c1)

# Problem Solution 
```
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    
    if(n%2==1):
        print("Weird")
    elif(n%2==0 and n >= 2 and n < 5):
        print("Not Weird")
    elif(n%2==0 and n >= 6 and n < 20):
        print("Weird")
    elif(n%2==0 and n >= 20):
        print("Not Weird")

```

## Code Explanation
The provided Python script reads an integer input n and prints a message based on the value of n following specific conditions.
1. **Shebang Line :**
   ```#!/bin/python3```
   - This line is used in Unix-based systems to indicate that the script should be run using Python 3.

2. **Imports**
    ```
    import math
    import os
    import random
    import re
    import sys
    ```
    - These lines import various standard libraries, though they are not used in the current script. They can be useful if the script is expanded later.
3. **Main Funtionality**
   
   ```if __name__ == '__main__'::```
   - Ensures that the code inside this block runs only if the script is executed directly, not when imported as a module.
     
   ```n = int(input().strip()):```
   - Reads an integer input from the user, strips any leading/trailing whitespace, and converts it to an integer.
     
   ****Conditional statements:****
     
    ``if(n%2==1):``: Checks if ```n``` is odd ```(n % 2 == 1)```. If true, ```prints "Weird"```.
   
    ```elif(n%2==0 and n >= 2 and n < 5):```: Checks if n is even and in the range [2, 5). If true, ```prints "Not Weird"```.
   
    ```elif(n%2==0 and n >= 6 and n < 20):```: Checks if n is even and in the range [6, 20). If true, ```prints "Weird"```.
   
    ```elif(n%2==0 and n >= 20):```: Checks if n is even and 20 or more. If true, ```prints "Not Weird"```.

4. **Expected Output**
   
   The output depends on the value of n provided by the user:

    If n is odd, it ```prints "Weird"```.
    
    If n is even and in the range [2, 5), it ```prints "Not Weird"```.
    
    If n is even and in the range [6, 20), it ```prints "Weird"```.
    
    If n is even and 20 or more, it ```prints "Not Weird"```.
