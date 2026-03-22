import numpy as np

# 10) Mini Data Analysis

# Set seed for reproducible dataset.
np.random.seed(21)

# 1. Generate a dataset of 50 students with marks in 5 subjects.
# Marks are generated between 35 and 100.
marks = np.random.randint(35, 101, size=(50, 5))

# 2. Calculate total marks and average marks.
total_marks = np.sum(marks, axis=1)
average_marks = np.mean(marks, axis=1)

# 3. Find topper student index and number of students scoring above 75%.
# For 5 subjects, percentage is total/5.
percentages = total_marks / 5

topper_student_index = np.argmax(total_marks)
count_above_75 = np.sum(percentages > 75)

# 4. Normalize the dataset subject-wise using min-max normalization.
min_subject = marks.min(axis=0)
max_subject = marks.max(axis=0)
normalized_marks = (marks - min_subject) / (max_subject - min_subject)

print("Dataset (first 5 students):\n", marks[:5])
print("\nTotal Marks (first 10):", total_marks[:10])
print("Average Marks (first 10):", average_marks[:10])

print("\nTopper Student Index:", topper_student_index)
print("Number of students scoring above 75%:", count_above_75)

print("\nNormalized Dataset (first 5 students):\n", normalized_marks[:5])
