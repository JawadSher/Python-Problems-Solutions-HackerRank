N, M = map(int, input().split())

for i in range(1, N, 2):
    print(('.|.' * i).center(M, '-'))

for i in range(1, 2):
    print(('WELCOME' * i).center(M, '-'))

for i in range(N-2, -1, -2):
    print(('.|.' * i).center(M, '-'))
    
