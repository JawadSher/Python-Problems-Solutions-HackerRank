import textwrap

def wrap(string, max_width):
    wrapped_words = textwrap.wrap(string, width=max_width)
    words = "";
    for line in wrapped_words:
        words += f"{line}\n"
        
    return words

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)       
    
