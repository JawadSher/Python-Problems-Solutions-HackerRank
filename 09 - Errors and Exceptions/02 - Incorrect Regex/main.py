import re

num_tests = int(input().strip())

for _ in range(num_tests):
    expression = input().strip()
    invalid = False
    
    for sign in ["+", "*", "?"]:
        if sign + "+" in expression:
            invalid = True
            break
    if invalid:
        print("False")
    else:
        try:
            re.compile(expression)
            print("True")
        except re.error:
            print("False")
