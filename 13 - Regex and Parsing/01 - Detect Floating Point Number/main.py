import re

N = int(input().strip())

for _ in range(N):
    input_value = input()
    pattern = re.compile(r'^(?!\..*\.)[+\.-]{0,1}\d*\.\d*$')
    print(bool(re.match(pattern, input_value)))
