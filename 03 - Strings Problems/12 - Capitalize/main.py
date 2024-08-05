#!/bin/python3
def solve(s):
    result = ""
    capitalization = True
    
    for char in s:
        if char == ' ':
            result += char
            capitalization = True
        elif capitalization:
            result += char.upper()
            capitalization = False
        else:
            result += char
    
    return result

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
