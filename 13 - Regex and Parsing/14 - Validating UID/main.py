import re

Id_pattern = r"^(?=([a-z\d]*[A-Z]){2})(?=([a-zA-Z]*[\d]){3})(([a-zA-Z0-9])(?!.*\4)){10}$"

t = int(input())

for _ in range(t):
    ID = input()
    
    if re.match(Id_pattern, ID):
        print("Valid")
    else:
        print("Invalid")
