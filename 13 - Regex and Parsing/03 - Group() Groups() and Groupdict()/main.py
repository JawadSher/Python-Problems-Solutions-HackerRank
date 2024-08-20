import re

S = input().strip()

pattern = re.compile(r'([0-9a-zA-Z]{1})\1+')

match = re.search(pattern, S)

if match:
    print(match.group(0)[0])
else:
    print(-1)
