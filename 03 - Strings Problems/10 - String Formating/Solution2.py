def octal_number(number):
    if number == 0:
        return "0"
        
    octal_num = ""
    
    while number:
        digit = number % 8
        octal_num = str(digit) + octal_num
        number //= 8
    
    return octal_num
    
def hexa_decimal(number):
    if number == 0:
        return "0"
        
    hex_chars = "0123456789ABCDEF"
    hex_decimal = ""
    
    while number:
        hex_digit = number % 16
        hex_decimal = hex_chars[hex_digit] + hex_decimal
        number //= 16
    
    return hex_decimal
    
def to_binary(number):
    if number == 0:
        return "0"
        
    binary_num = ""
    
    while number:
        bit = number & 1
        binary_num = str(bit) + binary_num
        number = number >> 1
    
    return binary_num

def print_formatted(n):
    max_width = len(bin(n)[2:])
    
    for i in range(1, n + 1):
        octal_str = octal_number(i).rjust(max_width)
        hex_str = hexa_decimal(i).rjust(max_width)
        binary_str = to_binary(i).rjust(max_width)
        print(f'{i:2d} {octal_str} {hex_str} {binary_str}')

        
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
