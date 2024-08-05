def count_substring(string, sub_string):
    n = len(string)
    m = len(sub_string)
    k = n - m + 1
    
    count = 0
    for i in range(k):
        if string[i:i + m] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
