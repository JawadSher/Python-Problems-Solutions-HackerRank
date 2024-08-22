import re

string = input().strip()
pattern = r"(?<=[^aeiou])([aeiou|AEIOU]{2,})(?=[^aeiou])"
matches = list(map(lambda x : x.group(), re.finditer(pattern, string)))

if matches:
    for i in matches:
        print(i)
else:
    print(-1)
