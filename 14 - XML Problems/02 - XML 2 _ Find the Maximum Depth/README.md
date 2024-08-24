<h1 align='center'>XML2 - Find - the - Maximum - Depth</h1>

## Problem Statement

**Problem URL :** [XML2 - Find the Maximum Depth](https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/9634e2bd-9cfc-47d3-8b6a-2e4fc3135489)

## Problem Solution
```py
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, nesting_level):
    global maxdepth
    
    nesting_level = nesting_level + 1
    
    for i in elem:
        depth(i, nesting_level)
        
    if(nesting_level > maxdepth):
        maxdepth = nesting_level

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
```

## Problem Solution Explanation

Let's go through the code step by step, explaining each part with examples.

```python
import xml.etree.ElementTree as etree
```
1. **Importing Modules**: The code imports the `xml.etree.ElementTree` module, aliased as `etree`. This module is used for parsing and creating XML data.

```python
maxdepth = 0
```
2. **Global Variable**: The variable `maxdepth` is initialized to `0`. This variable will be used to track the maximum depth of the XML tree as the script recursively explores the tree.

```python
def depth(elem, nesting_level):
    global maxdepth
    
    nesting_level = nesting_level + 1
    
    for i in elem:
        depth(i, nesting_level)
        
    if(nesting_level > maxdepth):
        maxdepth = nesting_level
```
3. **Defining the `depth` Function**: This function calculates the depth of the XML tree recursively.
   - **Parameters**:
     - `elem`: The current XML element being processed.
     - `nesting_level`: The current depth level in the tree.
   - **Global Variable**: The function declares `maxdepth` as a global variable so it can modify it.
   - `nesting_level = nesting_level + 1`: Each time the function is called, it increases the `nesting_level` by `1` to reflect moving one level deeper in the tree.
   - `for i in elem`: This loop iterates over each child element of the current element (`elem`).
     - `depth(i, nesting_level)`: For each child element, the `depth` function is called recursively with the updated `nesting_level`.
   - `if(nesting_level > maxdepth)`: After processing all children, the function checks if the current `nesting_level` is greater than `maxdepth`.
     - `maxdepth = nesting_level`: If it is, `maxdepth` is updated to the current `nesting_level`, ensuring that the maximum depth is recorded.

Example:
Imagine the XML structure:
```xml
<a>
    <b>
        <c></c>
    </b>
</a>
```
- The depth of element `a` is `0`.
- The depth of element `b` is `1`.
- The depth of element `c` is `2`.

This function will calculate and store `2` as the maximum depth.

```python
if __name__ == '__main__':
    n = int(input())
```
4. **Main Execution Block**: This part is executed when the script is run as a standalone program.
   - `n = int(input())`: The program reads an integer `n` from the user, which represents the number of lines of XML input to follow.

```python
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
```
5. **Reading the XML Input**:
   - `xml = ""`: Initializes an empty string `xml`.
   - `for i in range(n)`: A loop that runs `n` times.
     - `xml =  xml + input() + "\n"`: Each iteration reads a line of XML input from the user and appends it to the `xml` string, followed by a newline character (`\n`). This constructs the entire XML document as a single string.

Example:
If `n = 3` and the input is:
```
<a>
  <b>
    <c/>
  </b>
</a>
```
The variable `xml` would store:
```xml
<a>
  <b>
    <c/>
  </b>
</a>
```

```python
    tree = etree.ElementTree(etree.fromstring(xml))
```
6. **Parsing the XML**:
   - `tree = etree.ElementTree(etree.fromstring(xml))`: This line parses the XML string stored in `xml` and constructs an `ElementTree` object. `etree.fromstring(xml)` converts the string into an XML element, which `ElementTree` then uses to create a tree structure.

```python
    depth(tree.getroot(), -1)
```
7. **Calculating Maximum Depth**:
   - `depth(tree.getroot(), -1)`: This calls the `depth` function, starting from the root element of the XML tree with an initial `nesting_level` of `-1`. Starting with `-1` ensures that when we move to the root element, the depth begins at `0`.

```python
    print(maxdepth)
```
8. **Printing the Result**:
   - `print(maxdepth)`: After the depth calculation is complete, the program prints the maximum depth (`maxdepth`) of the XML tree.

### Summary with Example

Given the following XML input:
```xml
<a>
  <b>
    <c/>
  </b>
</a>
```
- The depth of the XML tree is `2` (since the deepest element `<c/>` is nested two levels inside the root `<a>`).
- The program will output `2`.

In summary, this code reads an XML structure from the user, parses it, and calculates the maximum depth of the tree, printing the result.
