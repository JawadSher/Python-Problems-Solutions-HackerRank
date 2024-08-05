if __name__ == '__main__':
    s = input()
    
    is_alnum = any(char.isalnum() for char in s)
    is_alpha = any(char.isalpha() for char in s)
    is_digit = any(char.isdigit() for char in s)
    is_lower = any(char.islower() for char in s)
    is_upper = any(char.isupper() for char in s)
    
    if(is_alnum):
        print("True")
    else:
        print("False")
    if(is_alpha):
        print("True")
    else:
        print("False")
    if(is_digit):
        print("True")
    else:
        print("False")
    if(is_lower):
        print("True")
    else:
        print("False")
    if(is_upper):
        print("True")
    else:
        print("False")        
    
