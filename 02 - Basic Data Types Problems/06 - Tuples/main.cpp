if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    my_tuple = tuple(integer_list)
    hash_value = hash(my_tuple)
    
    print(hash_value)
