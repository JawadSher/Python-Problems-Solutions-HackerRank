N, X = map(int, input().split())

actual_marks = []
avg_marks = []

for _ in range(X):
    marks = map(float, input().split())
    actual_marks.append(marks)
    
stdnt_marks = zip(*actual_marks)

for marks in stdnt_marks:
    avg_marks.append(sum(marks)/X)
    
for i in avg_marks:
    print(i)
