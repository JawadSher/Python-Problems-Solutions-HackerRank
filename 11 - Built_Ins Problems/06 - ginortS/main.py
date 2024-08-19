input_string = sorted(input())

lower = []
upper = []
odd = []
even = []

for char in input_string:
    if char.islower():
        lower.append(char)
    elif char.isupper():
        upper.append(char)
    elif char.isdigit():
        if int(char)%2 != 0:
            odd.append(char)
        else:
            even.append(char)

sorted_string = ''.join(lower + upper + odd + even)
print(sorted_string)
