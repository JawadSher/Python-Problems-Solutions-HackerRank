import re

n = int(input().strip())
pattern = r'^(\+1\s?)?([7 8 9]\d{2})([\s\-]?)\d{3}([\s\-]?)\d{4}$'

for _ in range(n):
    phone_num = input().strip()
    if re.match(pattern, phone_num) and len(phone_num) == 10:
        print("YES")
    else:
        print("NO")
