import re

string = input()
k_string = input()

pattern = f'(?=({k_string}))'
matches = list(re.finditer(pattern, string))

if matches:
    for m in matches:
        print(f"({m.start(1)}, {m.end(1) - 1})")
else:
   print("(-1, -1)")
