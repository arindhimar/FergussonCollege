student_grades = {'Ram': 85, 'Sham': 92, 'Ojas’': 88, 'Anay': 79}

print(student_grades)
print(sorted(student_grades.items(), key=lambda x: x[1]))
# print(student_grades)


# Define the initial dictionary of student grades
student_grades = {'Ram': 85, 'Sham': 92, 'Ojas': 88, 'Anay': 79}

def find_highest_grade(grades):
    """Return the student with the highest grade."""
    highest_student = max(grades, key=grades.get)
    return highest_student, grades[highest_student]

# Find the student with the highest grade
highest_student, highest_grade = find_highest_grade(student_grades)
print(f"The student with the highest grade is {highest_student} with a grade of {highest_grade}.")

# Add a new student 'Eve' with a grade of 95
student_grades['Eve'] = 95

# Print all student names and their grades in alphabetical order
print("All students and their grades in alphabetical order:")
for student in sorted(student_grades.keys()):
    print(f"{student}: {student_grades[student]}")