<h1 align='center'>HTML Parser - Part 1</h1>

## Problem Statement

**Problem URL :** [HTML Parser - Part 1](https://www.hackerrank.com/challenges/html-parser-part-1/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/d7850aa6-c836-4593-95c2-8c8e770d1e2d)
![image](https://github.com/user-attachments/assets/35ae6d60-9d1d-4434-a0fa-f08592102100)
![image](https://github.com/user-attachments/assets/7086ab71-9e4e-453b-81a5-3189a0ca4b64)
![image](https://github.com/user-attachments/assets/362dc83b-77ee-49c5-9438-7a67243b77ad)


## Problem Solution
```py
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        self.handle_attrs(attrs = attrs)
        
    def handle_endtag(self, tag):
        print("End   :", tag)
        
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        self.handle_attrs(attrs = attrs)
        
    def handle_attrs(self, attrs):
        [print(f"-> {i[0]} > {i[1]}") for i in attrs]


parser = MyHTMLParser()

n = int(input())
for _ in range(n):
    code = input()
    parser.feed(code)
```

## Problem Solution Explanation
let's go through the code line by line to explain how it works with detailed examples.


```python
from html.parser import HTMLParser
```
- **Purpose**: Imports the `HTMLParser` class from Python's built-in `html.parser` module.
- **Explanation**: `HTMLParser` provides methods to parse and handle HTML or XML data.

```python
class MyHTMLParser(HTMLParser):
```
- **Purpose**: Defines a new class `MyHTMLParser` that inherits from `HTMLParser`.
- **Explanation**: By inheriting from `HTMLParser`, `MyHTMLParser` can override methods to handle specific HTML parsing events.

```python
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        self.handle_attrs(attrs = attrs)
```
- **Purpose**: Defines a method to handle the start of an HTML tag.
- **Explanation**:
  - `tag` is the name of the tag (e.g., `a`, `div`).
  - `attrs` is a list of tuples containing attribute names and values.
  - `print("Start :", tag)` prints the start of the tag.
  - `self.handle_attrs(attrs = attrs)` calls another method to print the attributes of the tag.

```python
    def handle_endtag(self, tag):
        print("End   :", tag)
```
- **Purpose**: Defines a method to handle the end of an HTML tag.
- **Explanation**:
  - `tag` is the name of the tag that is closing.
  - `print("End   :", tag)` prints the end of the tag.

```python
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        self.handle_attrs(attrs = attrs)
```
- **Purpose**: Defines a method to handle self-closing (empty) HTML tags.
- **Explanation**:
  - `tag` is the name of the tag.
  - `attrs` is a list of attributes for the tag.
  - `print("Empty :", tag)` prints the tag's name with an "Empty" label.
  - `self.handle_attrs(attrs = attrs)` calls the method to print the tag's attributes.

```python
    def handle_attrs(self, attrs):
        [print(f"-> {i[0]} > {i[1]}") for i in attrs]
```
- **Purpose**: Defines a method to print the attributes of an HTML tag.
- **Explanation**:
  - `attrs` is a list of tuples, where each tuple contains an attribute name and value.
  - The list comprehension `[print(f"-> {i[0]} > {i[1]}") for i in attrs]` iterates over each attribute tuple and prints it in the format `-> attribute_name > attribute_value`.

```python
parser = MyHTMLParser()
```
- **Purpose**: Creates an instance of `MyHTMLParser`.
- **Explanation**: `parser` will be used to process HTML input and invoke the appropriate methods defined in `MyHTMLParser`.

```python
n = int(input())
```
- **Purpose**: Reads an integer input from the user.
- **Explanation**: This integer represents the number of HTML inputs that the user will provide.

```python
for _ in range(n):
    code = input()
    parser.feed(code)
```
- **Purpose**: Loops through `n` times to read and process multiple HTML inputs.
- **Explanation**:
  - `code = input()` reads a single line of HTML code from the user.
  - `parser.feed(code)` feeds the HTML code to the `MyHTMLParser` instance, which processes the input and prints the parsed information using the overridden methods.

### Example

Let's consider an example with the following HTML input:

```html
<a href="https://example.com">Example</a>
```

If the user provides this HTML input, the parser will:

1. **Process Start Tag**:
   - `handle_starttag('a', [('href', 'https://example.com')])`
   - Output:
     ```
     Start : a
     -> href > https://example.com
     ```

2. **Process End Tag**:
   - `handle_endtag('a')`
   - Output:
     ```
     End   : a
     ```

Since there are no empty tags in this example, the `handle_startendtag` method will not be called.

In summary, this script is designed to parse and print the structure of HTML input, including the start and end tags and their attributes.
