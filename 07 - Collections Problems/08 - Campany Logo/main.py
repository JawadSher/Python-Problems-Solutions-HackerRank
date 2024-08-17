from collections import Counter

def print_top_three_characters(s):
    frequency = Counter(s)
    
    sorted_characters = sorted(frequency.items(), key=lambda item : (-item[1], item[0]))
    
    for i in range(min(3, len(sorted_characters))):
        char, count = sorted_characters[i]
        print(f'{char} {count}')

if __name__ == '__main__':
    s = input().strip() 
    print_top_three_characters(s)
