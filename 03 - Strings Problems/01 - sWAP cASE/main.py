def swap_case(s):
    txt = ""
    for c in s:
        if c.islower():
            txt += c.upper()
        else:
            txt += c.lower()
    return txt

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
