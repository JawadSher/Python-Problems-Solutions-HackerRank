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
