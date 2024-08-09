student_english = int(input())
roll_nums1 = list(map(int, input().split()))
eng_std_rollnums = set(roll_nums1[::-1])

student_french = int(input())
roll_nums2 = list(map(int, input().split()))
fr_std_rollnums = set(roll_nums2[::-1])

total_subscriptions = eng_std_rollnums | fr_std_rollnums
subscriptions_length = len(total_subscriptions)
print(subscriptions_length)
