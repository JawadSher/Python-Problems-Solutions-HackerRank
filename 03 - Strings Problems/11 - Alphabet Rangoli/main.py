def print_rangoli(size):
    import string 
    alphabet = string.ascii_lowercase
    
    lines = []
    
    for i in range(size):
        s = '-'.join(alphabet[i : size])
        lines.append((s[::-1] + s[1:]).center(4 * size - 3, '-'))
        
    
    print('\n'.join(lines[::-1] + lines[1:]))
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
