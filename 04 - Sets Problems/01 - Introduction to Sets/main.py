def average(array):
    nums = set(array)
    n = len(nums)
   
    total_sum = 0
   
    for i in nums:
       total_sum += i
    
    average = total_sum/n
    return round(average, 3)    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
