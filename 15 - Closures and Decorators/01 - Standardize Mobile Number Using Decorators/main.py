from re import sub

def wrapper(f):
    pattern = r"^(?:\+?91|0)??(\d{5})(\d{5})$"
    code_pattern = r"+91 \1 \2"
    
    def fun(l):
        return f([sub(pattern, code_pattern, i) for i in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
