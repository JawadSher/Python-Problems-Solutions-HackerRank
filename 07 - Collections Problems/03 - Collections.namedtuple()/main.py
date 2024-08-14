from collections import namedtuple

nums_records = int(input())
Student = namedtuple('Student', input().split())
stdnt_records = [Student(*input().split()) for _ in range(nums_records)]
stdnt_marks = [student.MARKS for student in stdnt_records]
total_marks = sum(map(int, stdnt_marks))
avg_marks = total_marks / nums_records
print(f'{avg_marks:.2f}')

