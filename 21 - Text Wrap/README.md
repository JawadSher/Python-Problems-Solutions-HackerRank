# Problem Statement 
**URL : [Text Wrap](https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/51a55dff-4414-4014-beae-f2e498d7b385)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/2a6fdf8c-270a-46d1-8e6c-d70579274d90)


# Problem Solution 
```
import textwrap

def wrap(string, max_width):
    wrapped_words = textwrap.wrap(string, width=max_width)
    words = "";
    for line in wrapped_words:
        words += f"{line}\n"
        
    return words

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)       
    
```

## Source Code Explanation

1.  **Import the `textwrap` Module**:
    -   We start by importing the `textwrap` module from the Python standard library. This module provides convenient functions for wrapping text to a certain width.

	`import textwrap` 

	```
	def wrap(string, max_width):
	    wrapped_words = textwrap.wrap(string, width=max_width)
	    words = ""
	    for line in wrapped_words:
	        words += f"{line}\n"
	    return words
	``` 

2.  **Define the `wrap` Function**:
    
    -   The `wrap` function takes two arguments: `string` (the text to be wrapped) and `max_width` (the maximum number of characters per line).
3.  **Wrap the String**:
    
    -   `wrapped_words = textwrap.wrap(string, width=max_width)`: This line uses the `textwrap.wrap` function to break the input string into a list of lines. Each line will have at most `max_width` characters.
    -   For example, if `string` is "ABCDEFGHIJKLIMNOQRSTUVWXYZ" and `max_width` is 4, `wrapped_words` will be `['ABCD', 'EFGH', 'IJKL', 'IMNO', 'QRST', 'UVWX', 'YZ']`.
4.  **Concatenate Lines with New Lines**:
    
    -   `words = ""`: Initialize an empty string to store the final result.
    -   `for line in wrapped_words: words += f"{line}\n"`: Iterate over each line in `wrapped_words` and add it to the `words` string followed by a newline character (`\n`). This ensures that each line is separated by a newline in the final result.
5.  **Return the Result**:
    
    -   `return words`: Return the final concatenated string with new lines.



  ```
  if __name__ == '__main__':
      string, max_width = input(), int(input())
      result = wrap(string, max_width)
      print(result)
  
  ``` 

6.  **Main Program**:
    -   `if __name__ == '__main__':`: This checks if the script is being run directly (not imported as a module).
    -   `string, max_width = input(), int(input())`: Read input from the user. The first input is the `string` to be wrapped, and the second input is `max_width` (converted to an integer).
    -   `result = wrap(string, max_width)`: Call the `wrap` function with the user inputs and store the result in `result`.
    -   `print(result)`: Print the wrapped string.

##  Example Output 

Let's see an example to make it clear:

-   If the input string is: `"ABCDEFGHIJKLIMNOQRSTUVWXYZ"`
-   And the max width is: `4`

The `wrap` function will process the input and produce the following output:


```
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
``` 

This output is printed line by line with each line containing at most 4 characters. This way, the text is wrapped to fit within the specified width.

