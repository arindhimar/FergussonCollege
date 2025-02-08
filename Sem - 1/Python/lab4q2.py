import math

def maxGrade(tempDict):
    max_grade = max(tempDict.values())
    max_grade_key = [key for key, value in tempDict.items() if value == max_grade]
    return max_grade, max_grade_key

student_grades = {'ram': 85, 'Sham': 92, 'Ojas': 88, 'Anay': 79}

max_grade, max_grade_key = maxGrade(student_grades)
print("Maximum grade:", max_grade)
print("Student(s) with maximum grade:", max_grade_key)


student_grades['Eve'] = 95


print(sorted(student_grades.keys()))