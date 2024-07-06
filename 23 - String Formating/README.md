# Problem Statement 
**URL : [String Formating](https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/59cc09e3-c4d8-4e79-9bc9-256e05a75177)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/d03cf3e8-0a94-4a8b-b45b-f73a87bf6963)



# Problem Solution 1
```
def print_formatted(number):
    spaces = len(bin(number)) - 2
    for numbers in range(1, number+1):
        octo = oct(numbers)[2:]
        bino = bin(numbers)[2:]
        hexo = hex(numbers)[2:].upper()
        print(f'{numbers:>{spaces}} {octo:>{spaces}} {hexo:>{spaces}} {bino:>{spaces}}')
        


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
```

# Problem Solution 2
```
def octal_number(number):
    if number == 0:
        return "0"
        
    octal_num = ""
    
    while number:
        digit = number % 8
        octal_num = str(digit) + octal_num
        number //= 8
    
    return octal_num
    
def hexa_decimal(number):
    if number == 0:
        return "0"
        
    hex_chars = "0123456789ABCDEF"
    hex_decimal = ""
    
    while number:
        hex_digit = number % 16
        hex_decimal = hex_chars[hex_digit] + hex_decimal
        number //= 16
    
    return hex_decimal
    
def to_binary(number):
    if number == 0:
        return "0"
        
    binary_num = ""
    
    while number:
        bit = number & 1
        binary_num = str(bit) + binary_num
        number = number >> 1
    
    return binary_num

def print_formatted(n):
    max_width = len(bin(n)[2:])
    
    for i in range(1, n + 1):
        octal_str = octal_number(i).rjust(max_width)
        hex_str = hexa_decimal(i).rjust(max_width)
        binary_str = to_binary(i).rjust(max_width)
        print(f'{i:2d} {octal_str} {hex_str} {binary_str}')

        
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
```

## Source Code Explanation 


**Function Definition:**



```
def print_formatted(number):

```



-   This line defines a function named `print_formatted` that takes a single argument `number`. This function will be used to print formatted representations of numbers from 1 to `number`.

**Calculating Number of Spaces:**


```
    spaces = len(bin(number)) - 2

```



-   This line calculates the number of spaces needed for alignment when printing the different number representations.
    -   `len(bin(number))` counts the total characters in the binary representation of `number` (including the `0b` prefix).
    -   Subtracting 2 removes the `0b` prefix, leaving the length needed for alignment.

**Looping through Numbers:**



```
    for numbers in range(1, number + 1):

```




-   This line starts a `for` loop that iterates through numbers from 1 (inclusive) to `number` (inclusive).
    -   The variable `numbers` will hold the current number in each iteration.

**Converting Numbers:**



```
        octo = oct(numbers)[2:]
        bino = bin(numbers)[2:]
        hexo = hex(numbers)[2:].upper()

```



-   Inside the loop, these lines convert the current number (`numbers`) into different representations:
    -   `oct(numbers)[2:]` converts to octal (base 8), removes the `0o` prefix with `[2:]`, and stores the result in `octo`.
    -   `bin(numbers)[2:]` converts to binary (base 2), removes the `0b` prefix with `[2:]`, and stores the result in `bino`.
    -   `hex(numbers)[2:].upper()` converts to hexadecimal (base 16), removes the `0x` prefix with `[2:]`, converts to uppercase with `.upper()`, and stores the result in `hexo`.

**Formatted Printing:**


```
        print(f'{numbers:>{spaces}}  {octo:>{spaces}}  {hexo:>{spaces}}  {bino:>{spaces}}')

```



-   This line prints the current number (`numbers`) along with its octal, hexadecimal, and binary representations in a formatted way.
    -   `f-string`: This uses an f-string for formatted string output.
    -   `{numbers:>{spaces}}`: Formats the number (`numbers`) with right alignment (`>`) and a minimum width of `spaces`.
    -   (spaces): Adds three spaces for better readability between columns.
    -   The same formatting is applied for `octo`,  `hexo`, and `bino`, using their respective variables.

**Main Block:**


```
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

```

-   This block checks if the script is being run directly (not imported as a module).
    -   `int(input())`: Prompts the user for input, converts it to an integer (`int`), and stores it in `n`.
    -   `print_formatted(n)`: Calls the `print_formatted` function with the user-provided `n` to print the formatted number representations.

## Example Output 

If the user enters `10`, the output would be (assuming an 8-character minimum width for alignment):

```
      1     1     1     01
      2     2     2     10
      3     3     3     11
      4     4     4    100
      5     5     5    101
      6     6     6    110
      7     7     7    111
      8     10    8   1000
      9     11    9   1001
     10     12    A   1010
```

