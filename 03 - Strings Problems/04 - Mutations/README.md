# Problem Statement 
**URL : [Mutations](https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/d10beb10-0dd2-466c-b4fb-2d28dba30d58)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/f7050677-ac26-4b07-9eba-1c8278dfcf2d)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/acfcfc06-5676-4753-ae0d-9e1cb1d7a625)


# Problem Solution 
```
def mutate_string(string, position, character):
    new_string = string[:position]+character+string[position+1:]
    return new_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
```

## Code Explanation
Let's break down the code and its functionality step by step.
#### Function Definition


```
def mutate_string(string, position, character):
    new_string = string[:position] + character + string[position+1:]
    return new_string
``` 

-   **Function Name:** `mutate_string`
-   **Parameters:**
    -   `string`: The original string that you want to modify.
    -   `position`: The index in the string where you want to replace a character.
    -   `character`: The new character that will replace the old character at the specified position.
-   **Function Body:**
    -   `new_string = string[:position] + character + string[position+1:]`
        -   `string[:position]`: This slice operation takes all characters from the beginning of the string up to, but not including, the specified position.
        -   `character`: The new character that will replace the old character at the specified position.
        -   `string[position+1:]`: This slice operation takes all characters from the position immediately after the specified position to the end of the string.
    -   `return new_string`: The function returns the newly constructed string.

#### 2. Main Block


```
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
``` 

-   **Conditional Statement:** `if __name__ == '__main__':`
    -   This line checks if the script is being run as the main program. If the script is executed directly, `__name__` is set to `'__main__'`.
-   **Input Collection:**
    -   `s = input()`: This line reads a string from the user input and assigns it to the variable `s`.
    -   `i, c = input().split()`: This line reads a single input line, splits it into two parts, and assigns them to `i` and `c`. The `split()` method splits the input string by whitespace by default.
        -   `i`: Expected to be the position (index) in the string where a character will be replaced.
        -   `c`: The new character that will replace the old character at the specified position.
-   **Function Call:** `s_new = mutate_string(s, int(i), c)`
    -   This line calls the `mutate_string` function with the original string `s`, the position `i` (converted to an integer), and the new character `c`.
-   **Output:** `print(s_new)`
    -   This line prints the modified string returned by the `mutate_string` function.

### How It Works

1.  When the script runs, the user is prompted to enter a string `s`.
2.  The user is then prompted to enter a position (index) and a new character, separated by a space.
3.  The script splits the input into the position and the character, converts the position to an integer, and calls the `mutate_string` function with these values.
4.  The `mutate_string` function constructs a new string by replacing the character at the specified position with the new character.
5.  The modified string is printed.

### Example

Assume the user inputs the following:

-   First input (the original string): `"hello"`
-   Second input (position and new character): `"1 a"`

The operations would be as follows:

-   The original string `s` is `"hello"`.
-   The position `i` is `1` (converted to an integer).
-   The new character `c` is `"a"`.

Inside the `mutate_string` function:

-   `string[:position]` is `"h"` (substring from start to position 1).
-   `character` is `"a"`.
-   `string[position+1:]` is `"llo"` (substring from position 2 to the end).

So, `new_string` becomes `"h" + "a" + "llo"`, resulting in `"hallo"`.

The output will be:
`hallo`

