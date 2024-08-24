<h1 align='center'>XML 1 - Find - the - Score</h1>

## Problem Statement

**Problem URL :** [XML 1 - Find the Score](https://www.hackerrank.com/challenges/xml-1-find-the-score/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/55979315-643b-4268-9a31-b3caf2c3846e)
![image](https://github.com/user-attachments/assets/4acc3127-e985-486a-a1f9-b8e213811217)

## Problem Solution
```py
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    count = 0
    for child in node.iter():
        count += int(len(child.attrib))
    
    return count

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
```

## Problem Solution Explanation
Let's go through the code step by step to understand how it works.

```python
import sys
import xml.etree.ElementTree as etree
```
1. **Imports**: The code imports two modules:
   - `sys`: This module provides access to some variables used or maintained by the Python interpreter and functions that interact with the interpreter.
   - `xml.etree.ElementTree as etree`: This is a module in Python that provides methods for parsing and creating XML data. It's commonly used for working with XML files. The `as etree` part is just giving the `ElementTree` module an alias (`etree`), making it easier to refer to in the code.

```python
def get_attr_number(node):
    count = 0
    for child in node.iter():
        count += int(len(child.attrib))
    
    return count
```
2. **Defining a Function**: A function named `get_attr_number` is defined that takes a single argument, `node`.
   - `count = 0`: Initializes a counter `count` to zero. This counter will keep track of the total number of attributes in the XML tree.
   - `for child in node.iter()`: This loop iterates over all elements (nodes) in the XML tree starting from `node` (which is usually the root). The `iter()` method is used to traverse all elements in the XML tree.
   - `count += int(len(child.attrib))`: For each element (`child`) in the XML tree, the code increments the `count` by the number of attributes that the element has. `child.attrib` is a dictionary containing all the attributes of the element, and `len(child.attrib)` gives the number of attributes.
   - `return count`: Finally, the function returns the total number of attributes counted.

```python
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
```
3. **Main Execution Block**: This block is executed when the script is run as a standalone program.
   - `sys.stdin.readline()`: This line reads a single line of input from standard input (usually provided by the user or a file). However, in this code, it reads the first line and discards it. This is often used when the first line is not needed (e.g., in a coding challenge where the first line might contain the number of elements).
   - `xml = sys.stdin.read()`: This reads the entire input XML data from standard input (ignoring the first line) and stores it in the variable `xml`.
   - `tree = etree.ElementTree(etree.fromstring(xml))`: This line parses the XML string stored in `xml` and constructs an `ElementTree` object. The `etree.fromstring(xml)` function converts the XML string into an XML element, which `ElementTree` can then work with.
   - `root = tree.getroot()`: This retrieves the root element of the XML tree (i.e., the top-level node) and stores it in the variable `root`.
   - `print(get_attr_number(root))`: This calls the `get_attr_number` function with the root of the XML tree and prints the total number of attributes in the entire XML tree.

### Summary
This script reads an XML structure from standard input, parses it, and counts the total number of attributes present in all the elements of the XML tree. The `get_attr_number` function performs the counting by iterating through every element in the XML and summing up their attributes. The result is then printed to the console.
