if __name__ == '__main__':
    n = int(input())
    my_list = []
    
    for i in range(n):
        HR_input = input().split()
        functions = HR_input[0]
        numbers = list(map(int, HR_input[1:]))
        
        if functions == 'insert':
            my_list.insert(int(numbers[0]), int(numbers[1]))
        elif functions == 'print':
            print(my_list)
        elif functions == 'remove':
            my_list.remove(int(numbers[0]))
        elif functions == 'append':
            my_list.append(int(numbers[0]))
        elif functions == 'sort':
            my_list.sort()
        elif functions == 'pop':
            my_list.pop()
        elif functions == 'reverse':
            my_list.reverse()
