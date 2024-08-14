<h1>Collections - .OrderedDict()</h1>


## Problem Statement

**Problem URL :** [Collections OrderedDict()](https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true)

![image](https://github.com/user-attachments/assets/a42819b7-f7ba-4e6e-9892-ef8f00cbc2dc)
![image](https://github.com/user-attachments/assets/ffa8fc6d-eb0c-43a0-af70-93903fd0be6e)
![image](https://github.com/user-attachments/assets/82d6c22e-1f76-4a4e-85b6-357fbc142a46)


## Problem Solution
```py
from collections import OrderedDict

product_info = OrderedDict()
nums_items = int(input().strip())

for _ in range(nums_items):
    data = input().rsplit(' ', 1)
    product_name = data[0]
    product_price = int(data[1])
    
    if product_name in product_info:
        product_info[product_name] += product_price
    else:
        product_info[product_name] = product_price

for name, price  in product_info.items():
    print(f'{name} {price}')
```

## Problem Solution Explanation

Let's break down the code step by step to understand how it works.


```python
from collections import OrderedDict
```
- **Import `OrderedDict`**: This line imports the `OrderedDict` class from the `collections` module. `OrderedDict` is a dictionary subclass that maintains the order of keys as they are inserted, which is useful when you want to preserve the order of items.

```python
product_info = OrderedDict()
```
- **Initialize an Empty `OrderedDict`**: 
  - **`OrderedDict()`**: Creates an empty `OrderedDict` named `product_info`. This dictionary will store product names as keys and their corresponding prices as values, while maintaining the order in which products are added.

```python
nums_items = int(input().strip())
```
- **Read the Number of Items**:
  - **`input()`**: Reads a line of input from the user. This should be the number of product records that will follow.
  - **`.strip()`**: Removes any leading or trailing whitespace from the input string.
  - **`int()`**: Converts the input string into an integer.
  - **`nums_items`**: Stores the number of items (products) to be processed.

```python
for _ in range(nums_items):
    data = input().rsplit(' ', 1)
    product_name = data[0]
    product_price = int(data[1])
    
    if product_name in product_info:
        product_info[product_name] += product_price
    else:
        product_info[product_name] = product_price
```
- **Processing Each Product Record**:
  - **`for _ in range(nums_items):`**: This loop iterates `nums_items` times, once for each product record.
  - **`input().rsplit(' ', 1)`**: Reads a line of input for each product. The `rsplit(' ', 1)` method splits the string into two parts from the right. It splits the string into the product name and the product price. For example, if the input line is "Apple 10", `rsplit(' ', 1)` will return `['Apple', '10']`.
  - **`product_name = data[0]`**: Extracts the product name from the split data. For the example above, `product_name` will be `'Apple'`.
  - **`product_price = int(data[1])`**: Extracts the product price from the split data and converts it to an integer. For the example above, `product_price` will be `10`.
  - **`if product_name in product_info:`**: Checks if the product name is already in the `product_info` dictionary.
    - **`product_info[product_name] += product_price`**: If the product is already in the dictionary, add the new price to the existing total price for that product.
    - **`else:`**: If the product is not in the dictionary, add it.
      - **`product_info[product_name] = product_price`**: Adds the product name and price to the dictionary.

```python
for name, price in product_info.items():
    print(f'{name} {price}')
```
- **Print Each Product and Its Total Price**:
  - **`for name, price in product_info.items():`**: This loop iterates over each item in the `product_info` dictionary. `name` is the product name, and `price` is the total price of that product.
  - **`print(f'{name} {price}')`**: Prints each product name followed by its total price. The `f'{name} {price}'` uses an f-string to format the output.

### Summary

1. **Initialize** an `OrderedDict` to keep track of product names and their prices while maintaining the order of insertion.
2. **Read** the number of products.
3. **Process** each product input:
   - **Split** the input line into product name and price.
   - **Update** the dictionary with the product's price, summing prices for duplicate product names.
4. **Print** the product names and their total prices, preserving the order they were first encountered.

This code efficiently handles the addition of product prices while keeping the order of products as they were entered, and ensures that if the same product appears multiple times, its prices are aggregated correctly.
