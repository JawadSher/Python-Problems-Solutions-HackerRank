import re

n = int(input())

for _ in range (n):
    css_code = input()
    hex_code = re.search(r'^#[A-Fa-f0-9]*', css_code)
    
    if not hex_code:
        hex_code1 = re.findall(r'#[A-Fa-f0-9]{6}|#[A-Fa-f0-9]{3}', css_code)
        
        if hex_code1:
            for i in hex_code1:
                print(i)
