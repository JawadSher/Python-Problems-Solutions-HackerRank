import re
import email.utils

n = int(input())

for _ in range(n):
    pattern = r'^[a-zA-Z][\w._-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
    
    inpt = email.utils.parseaddr(input())
    s = inpt[1]
    result = re.match(pattern, s)
    
    if result:
        print(email.utils.formataddr(inpt))
