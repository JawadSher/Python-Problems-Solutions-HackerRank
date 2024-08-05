if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append((name, score))

    students_sorted = sorted(students, key=lambda x: (x[1], x[0]))      
    
    lowestGrade = students_sorted[0][1]
    secLowestGrade = None
    
    for student in students_sorted:
        if student[1] > lowestGrade:
            secLowestGrade = student[1]
            break
    
    studentNames = [student[0] for student in students_sorted if secLowestGrade == student[1]]
    studentNames.sort()
    for names in studentNames:
        print(names)
