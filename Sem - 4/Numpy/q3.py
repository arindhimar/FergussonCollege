import numpy as np

# Create a 3×3 matrix with values from 1 to 9
matrix = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

# Find the transpose of the matrix
transpose_matrix = matrix.T

# Calculate row-wise sum
row_sum = matrix.sum(axis=1)

# Calculate column-wise sum
column_sum = matrix.sum(axis=0)

# Find the determinant of the matrix
determinant = np.linalg.det(matrix)
print("Original Matrix:\n", matrix)

print("Transpose of the Matrix:\n", transpose_matrix)

print("Row-wise Sum:", row_sum)

print("Column-wise Sum:", column_sum)

print("Determinant of the Matrix:", determinant)

