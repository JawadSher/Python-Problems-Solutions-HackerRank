def print_formatted(number):
    spaces = len(bin(number)) - 2
    for numbers in range(1, number+1):
        octo = oct(numbers)[2:]
        bino = bin(numbers)[2:]
        hexo = hex(numbers)[2:].upper()
        print(f'{numbers:>{spaces}} {octo:>{spaces}} {hexo:>{spaces}} {bino:>{spaces}}')
        


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
