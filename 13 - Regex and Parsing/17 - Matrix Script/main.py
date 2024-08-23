import re

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix.append(input())

decoded_string = ""

for col in range(m):
    for row in range(n):
        decoded_string += matrix[row][col]
        
decoded_string = re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', decoded_string)

print(decoded_string)
