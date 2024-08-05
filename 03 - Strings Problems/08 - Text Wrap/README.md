<h1 align='center'>Text - Wrap</h1>

## Problem Statement 
**Problem URL : [Text Wrap](https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true)**

![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/51a55dff-4414-4014-beae-f2e498d7b385)
![image](https://github.com/JawadSher/Python_Problems-HackerRank/assets/158135119/2a6fdf8c-270a-46d1-8e6c-d70579274d90)


## Problem Solution 
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

## Problem Solution Explanation

```python
import textwrap
```
- Imports the `textwrap` module, which provides functionality for wrapping and formatting text. 

```python
def wrap(string, max_width):
```
- Defines a function named `wrap` that takes two arguments:
  - `string`: the text to be wrapped.
  - `max_width`: the maximum width of each line after wrapping.

```python
    wrapped_words = textwrap.wrap(string, width=max_width)
```
- Uses the `textwrap.wrap` function to wrap the input `string` into lines, where each line has a maximum width of `max_width` characters. This function returns a list of lines, each of which is a string with a length up to `max_width`.

```python
    words = "";
```
- Initializes an empty string `words` that will be used to accumulate the wrapped lines.

```python
    for line in wrapped_words:
```
- Iterates over each line in the `wrapped_words` list.

```python
        words += f"{line}\n"
```
- Appends the current `line` to the `words` string, followed by a newline character `\n`. This effectively joins all the lines into a single string, with each line separated by a newline.

```python
    return words
```
- Returns the accumulated `words` string, which contains the wrapped text with each line ending with a newline character.

```python
if __name__ == '__main__':
```
- This line checks if the script is being run directly (not imported as a module). If it is run directly, the code block following this line will be executed.

```python
    string, max_width = input(), int(input())
```
- Reads two inputs from the user:
  - The first input is assigned to `string`.
  - The second input is converted to an integer and assigned to `max_width`.

```python
    result = wrap(string, max_width)
```
- Calls the `wrap` function with `string` and `max_width` as arguments, and stores the result (the wrapped text) in the variable `result`.

```python
    print(result)
```
- Prints the wrapped text stored in `result`.

### Example

Consider the following inputs:
```
string: "Hello, this is a test of the textwrap module."
max_width: 10
```

Here’s how the code works step by step:

1. **Initial Input:**
   - `string = "Hello, this is a test of the textwrap module."`
   - `max_width = 10`

2. **Function Call:**
   - `wrapped_words = textwrap.wrap("Hello, this is a test of the textwrap module.", width=10)`
   - This results in:
     ```
     ['Hello, this', 'is a test', 'of the', 'textwrap', 'module.']
     ```

3. **Loop Through Lines:**
   - `words = "Hello, this\nis a test\nof the\ntextwrap\nmodule.\n"`

4. **Output:**
   - The wrapped text is:
     ```
     Hello, this
     is a test
     of the
     textwrap
     module.
     ```

Thus, the final output printed will be:
```
Hello, this
is a test
of the
textwrap
module.
```


