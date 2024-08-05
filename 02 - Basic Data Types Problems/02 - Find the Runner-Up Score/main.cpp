if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    maxNumber = float('-inf')
    secMaxNumber = float('-inf')
        
    for num in arr:
        if num > maxNumber:
            secMaxNumber = maxNumber
            maxNumber = num
        elif num > secMaxNumber and num != maxNumber:
            secMaxNumber = num
    
    print(secMaxNumber)
