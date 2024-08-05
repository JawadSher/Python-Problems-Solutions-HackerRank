def minion_game(string):
    vowels = "AEIOU"
    Kevin_score = 0
    Stuart_score = 0
    
    s_length = len(string)
    
    for i in range(s_length):
        if string[i] in vowels:
            Kevin_score += s_length - i
        else:
            Stuart_score += s_length - i
    
    if Kevin_score > Stuart_score:
        print("Kevin", Kevin_score)
    elif Kevin_score < Stuart_score:
        print("Stuart", Stuart_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
