<h1 align='center'>HTML Parser - Part 2</h1>

## Problem Statement

**Problem URL :** [HTML Parser - Part 2](https://www.hackerrank.com/challenges/html-parser-part-2/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/c2be0718-9501-4c82-a4f8-c383e02721da)
![image](https://github.com/user-attachments/assets/1b26edb0-1849-4be1-aabb-2d28f02feb4b)
![image](https://github.com/user-attachments/assets/f10d1b07-b890-48e6-8a1b-360412a1a286)


## Problem Solution
```py
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, comment):
        if "\n" in comment: 
            print(f">>> Multi-line Comment\n{comment}")
            
        if "\n" not in comment:
            print(f">>> Single-line Comment\n{comment}")

    def handle_data(self, data):
        if data.strip():  
            print(f">>> Data")
            print(data)

html = ""
for _ in range(int(input())):
    html += input().rstrip() + '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()
```

## Problem Solution Explanation

let's break down your updated code line by line and explain how it works, including examples for clarity.

```python
from html.parser import HTMLParser
```
- **Purpose**: Imports the `HTMLParser` class from the `html.parser` module.
- **Explanation**: This class provides methods for parsing HTML and XML documents.

```python
class MyHTMLParser(HTMLParser):
```
- **Purpose**: Defines a new class `MyHTMLParser` that inherits from `HTMLParser`.
- **Explanation**: By inheriting from `HTMLParser`, you can customize the behavior for parsing HTML by overriding its methods.

```python
    def handle_comment(self, comment):
        if "\n" in comment: 
            print(f">>> Multi-line Comment\n{comment}")
            
        if "\n" not in comment:
            print(f">>> Single-line Comment\n{comment}")
```
- **Purpose**: Handles HTML comments found during parsing.
- **Explanation**:
  - `comment` is a string containing the comment text.
  - `if "\n" in comment:` checks if the comment contains newline characters, which suggests it's a multi-line comment.
  - `print(f">>> Multi-line Comment\n{comment}")` prints multi-line comments with a specific format.
  - `if "\n" not in comment:` checks if the comment does not contain newlines, suggesting it's a single-line comment.
  - `print(f">>> Single-line Comment\n{comment}")` prints single-line comments with a different format.

```python
    def handle_data(self, data):
        if data.strip():  
            print(f">>> Data")
            print(data)
```
- **Purpose**: Handles text data within HTML tags.
- **Explanation**:
  - `data` is a string containing text data between HTML tags.
  - `if data.strip():` checks if `data` is not just whitespace (i.e., it contains meaningful text).
  - `print(f">>> Data")` prints a label indicating that data is being printed.
  - `print(data)` prints the actual data.

```python
html = ""
for _ in range(int(input())):
    html += input().rstrip() + '\n'
```
- **Purpose**: Collects multiple lines of HTML input.
- **Explanation**:
  - `int(input())` reads the number of lines of HTML input from the user.
  - The `for` loop iterates over the number of lines.
  - `input().rstrip()` reads each line of HTML input and removes any trailing whitespace.
  - `html += input().rstrip() + '\n'` appends each line to the `html` string, ensuring lines are separated by newlines.

```python
parser = MyHTMLParser()
```
- **Purpose**: Creates an instance of `MyHTMLParser`.
- **Explanation**: This instance will be used to parse the collected HTML input.

```python
parser.feed(html)
```
- **Purpose**: Feeds the HTML string to the parser.
- **Explanation**: The `feed` method processes the HTML input and invokes the appropriate methods (`handle_comment`, `handle_data`, etc.) based on the content.

```python
parser.close()
```
- **Purpose**: Cleans up the parser after processing.
- **Explanation**: The `close` method is called to finish parsing and release any resources.

### Example

**Input:**
```
4
<!-- Single-line comment -->
<div> Welcome to HackerRank </div>
<!--[if IE 9]>IE9-specific content<![endif]-->
<p>Some more text here</p>
```

**Explanation:**
1. `<!-- Single-line comment -->`:
   - `handle_comment` will identify this as a single-line comment and output:
     ```
     >>> Single-line Comment
     <!-- Single-line comment -->
     ```

2. `<div> Welcome to HackerRank </div>`:
   - `handle_data` will identify the text within `<div>` tags and output:
     ```
     >>> Data
     Welcome to HackerRank
     ```

3. `<!--[if IE 9]>IE9-specific content<![endif]-->`:
   - This is a multi-line comment. `handle_comment` will identify this and output:
     ```
     >>> Multi-line Comment
     <![if IE 9]>IE9-specific content<![endif]-->
     ```

4. `<p>Some more text here</p>`:
   - `handle_data` will identify the text within `<p>` tags and output:
     ```
     >>> Data
     Some more text here
     ```

### Summary

This code snippet parses HTML input to distinguish between single-line and multi-line comments, and also prints textual data within HTML tags. The comments and data are printed with specific labels to make it clear what type of content is being handled.
