def split_and_join(line):
    line_list = line.split(" ")
    line_list = "-".join(line_list)
    return line_list

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    
