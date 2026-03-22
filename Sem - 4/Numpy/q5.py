import numpy as np

# 5) Mathematical Operations

# 1. Create two arrays of size 10.
arr1 = np.arange(1, 11)              # [1, 2, ..., 10]
arr2 = np.arange(11, 21)             # [11, 12, ..., 20]

# 2. Perform addition, subtraction, multiplication, and division.
addition = arr1 + arr2
subtraction = arr2 - arr1
multiplication = arr1 * arr2
division = arr2 / arr1

# 3. Find square root, square, and exponential of elements.
square_root_arr1 = np.sqrt(arr1)
square_arr1 = np.square(arr1)
exponential_arr1 = np.exp(arr1)

print("Array 1:", arr1)
print("Array 2:", arr2)

print("\nAddition:", addition)
print("Subtraction (arr2 - arr1):", subtraction)
print("Multiplication:", multiplication)
print("Division (arr2 / arr1):", division)

print("\nSquare root of arr1:", square_root_arr1)
print("Square of arr1:", square_arr1)
print("Exponential of arr1:", exponential_arr1)
