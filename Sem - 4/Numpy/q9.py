import numpy as np

# 9) Linear Algebra

# 1. Create two 3x3 matrices.
A = np.array([
    [2, 1, 3],
    [1, 0, 2],
    [4, 1, 8]
])

B = np.array([
    [1, 2, 0],
    [3, 1, 4],
    [2, 5, 1]
])

# 2. Perform matrix multiplication and element-wise multiplication.
matrix_multiplication = np.matmul(A, B)
elementwise_multiplication = A * B

# 3. Find inverse of a matrix and eigenvalues.
# A is chosen to be invertible.
inverse_A = np.linalg.inv(A)
eigenvalues_A = np.linalg.eigvals(A)

print("Matrix A:\n", A)
print("\nMatrix B:\n", B)

print("\nMatrix Multiplication (A @ B):\n", matrix_multiplication)
print("\nElement-wise Multiplication (A * B):\n", elementwise_multiplication)

print("\nInverse of A:\n", inverse_A)
print("\nEigenvalues of A:\n", eigenvalues_A)
