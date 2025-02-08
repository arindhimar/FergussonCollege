student_grades = {'Ram': 85, 'Sham': 92, 'Ojas’': 88, 'Anay': 79}

print(sorted(student_grades.items(),key = lambda x:x[1],reverse=True)[0])

student_grades['Eve'] = 95

print(student_grades)

print(sorted(student_grades.keys()))
