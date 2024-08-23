<h1 align='center'>Detect - HTML - Tags - Attributes - and - Attribute Values</h1>

## Problem Statement

**Problem URL :** [Detect HTML Tags, Attributes and Attribute Values](https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/3fcc0c30-64d0-4c08-836b-eb20c0fee5d3)
![image](https://github.com/user-attachments/assets/8279fa5e-cd5d-450e-b811-f9c177691d34)
![image](https://github.com/user-attachments/assets/38dd7a16-7643-4107-bb4c-2ce274632152)

## Problem Solution
```py
from html.parser import HTMLParser

class My_HTML_Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        self.handle_attrs(attrs = attrs)
    
    def handle_attrs(self, attrs):
        [print(f"-> {x[0]} > {x[1]}") for x in attrs]
    
n = int(input())
parser = My_HTML_Parser()

for _ in range(n):
    code = input()
    parser.feed(code)
```

## Problem Solution Explanation
Let’s dive into each part of the code and explain it in detail, including examples.

```python
from html.parser import HTMLParser
```
- **Purpose**: Imports the `HTMLParser` class from the `html.parser` module.
- **Explanation**: This class provides methods to parse HTML and XML documents. It allows you to define custom behavior for handling different parts of an HTML document.

```python
class My_HTML_Parser(HTMLParser):
```
- **Purpose**: Defines a custom class `My_HTML_Parser` that extends the `HTMLParser` class.
- **Explanation**: By inheriting from `HTMLParser`, you can customize how HTML is processed by overriding methods that handle specific HTML elements and attributes.

```python
    def handle_starttag(self, tag, attrs):
        print(tag)
        self.handle_attrs(attrs = attrs)
```
- **Purpose**: Handles the start of an HTML tag.
- **Explanation**:
  - `tag` is the name of the HTML tag (e.g., `div`, `a`).
  - `attrs` is a list of tuples where each tuple represents an attribute and its value (e.g., `[('href', 'https://example.com')]`).
  - `print(tag)` prints the tag name to the console.
  - `self.handle_attrs(attrs = attrs)` calls the `handle_attrs` method to process and print the tag's attributes.

```python
    def handle_attrs(self, attrs):
        [print(f"-> {x[0]} > {x[1]}") for x in attrs]
```
- **Purpose**: Handles and prints the attributes of an HTML tag.
- **Explanation**:
  - `attrs` is a list of tuples, where each tuple contains an attribute name and its corresponding value.
  - `[print(f"-> {x[0]} > {x[1]}") for x in attrs]` is a list comprehension that iterates over each tuple in `attrs` and prints each attribute in the format `-> attribute > value`.

```python
n = int(input())
```
- **Purpose**: Reads the number of HTML lines to process.
- **Explanation**:
  - `input()` reads a line of input from the user, which is the number of lines of HTML code.
  - `int(input())` converts this input into an integer, which specifies how many lines of HTML will follow.

```python
parser = My_HTML_Parser()
```
- **Purpose**: Creates an instance of the `My_HTML_Parser` class.
- **Explanation**:
  - `My_HTML_Parser()` initializes the custom parser object that will be used to process HTML input.

```python
for _ in range(n):
    code = input()
    parser.feed(code)
```
- **Purpose**: Reads each line of HTML input and feeds it to the parser.
- **Explanation**:
  - `for _ in range(n):` loops `n` times to handle `n` lines of HTML code.
  - `code = input()` reads a line of HTML input.
  - `parser.feed(code)` processes the HTML line with the `My_HTML_Parser` instance. The `feed` method triggers the `handle_starttag` method (and other methods as needed) for each HTML line.

### Example

Let's go through an example input and the resulting output.

**Example Input:**
```
3
<a href="https://example.com" class="link">Link</a>
<div id="container" style="color: red">Content</div>
<p class="text">Hello, World!</p>
```

**Explanation:**

1. **Processing `<a href="https://example.com" class="link">Link</a>`:**
   - **`handle_starttag`**:
     - `tag` will be `a`.
     - `attrs` will be `[('href', 'https://example.com'), ('class', 'link')]`.
     - Output:
       ```
       a
       -> href > https://example.com
       -> class > link
       ```

2. **Processing `<div id="container" style="color: red">Content</div>`:**
   - **`handle_starttag`**:
     - `tag` will be `div`.
     - `attrs` will be `[('id', 'container'), ('style', 'color: red')]`.
     - Output:
       ```
       div
       -> id > container
       -> style > color: red
       ```

3. **Processing `<p class="text">Hello, World!</p>`:**
   - **`handle_starttag`**:
     - `tag` will be `p`.
     - `attrs` will be `[('class', 'text')]`.
     - Output:
       ```
       p
       -> class > text
       ```

### Summary

This code defines a custom HTML parser that processes and prints the tag names and their attributes for each HTML line input. It uses the `handle_starttag` method to print the tag name and then calls `handle_attrs` to print each attribute of the tag in a specific format. The code reads a number of HTML lines from the user, processes each line, and prints the tag details to the console.
