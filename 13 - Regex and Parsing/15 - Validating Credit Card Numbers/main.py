import re

n = int(input())
pattern = '^(?=[456])(?!.*(.)-?\\1-?\\1-?\\1)(\\d{4}-?){3}\\d{4}$'
for _ in range(n):
    card_num = input()
    
    if re.match(pattern, card_num):
        print("Valid")
    else:
        print("Invalid")
