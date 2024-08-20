cube = lambda x: x*x*x

def fibonacci(n):
    fibnoacci_nums = [0, 1]
    for _ in range(2, n):
        fibnoacci_nums.append(fibnoacci_nums[-1] + fibnoacci_nums[-2])
    return fibnoacci_nums[:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
