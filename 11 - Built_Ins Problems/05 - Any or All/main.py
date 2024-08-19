N = int(input().strip())
nums = list(map(int, input().split()))
print(all(i > 0 for i in nums ) and any(str(n) == str(n)[::-1] for n in nums ))
