student_grades = {'Ram': 85, 'Sham': 92, 'Ojas': 88, 'Anay': 79}
student_grades['Eve'] = 95

for temp in sorted(student_grades):
    print(temp,student_grades[temp])

print(sorted(student_grades.items(), key=lambda x: x[1],reverse=True))
