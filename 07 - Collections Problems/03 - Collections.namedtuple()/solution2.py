nums_records = int(input().strip())
header = input().split()

header_index = header.index("MARKS")
marks = [int(input().split()[header_index]) for _ in range(nums_records)]
avg_marks = sum(marks) / nums_records
print(f'{avg_marks:.2f}')
