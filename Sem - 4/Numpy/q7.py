import numpy as np

# 7) Reshaping & Stacking

# 1. Create a 1D array of size 12.
arr_1d = np.arange(1, 13)

# 2. Reshape it into 3x4 and 2x6.
arr_3x4 = arr_1d.reshape(3, 4)
arr_2x6 = arr_1d.reshape(2, 6)

# 3. Stack two arrays vertically and horizontally.
# Use two compatible 2x6 arrays for both stacking operations.
arr_a = arr_2x6
arr_b = arr_2x6 + 100

vertical_stack = np.vstack((arr_a, arr_b))
horizontal_stack = np.hstack((arr_a, arr_b))

# 4. Flatten the final array.
# Here, we flatten the horizontally stacked array.
flattened_final = horizontal_stack.flatten()

print("Original 1D Array:\n", arr_1d)
print("\nReshaped to 3x4:\n", arr_3x4)
print("\nReshaped to 2x6:\n", arr_2x6)

print("\nVertical Stack:\n", vertical_stack)
print("\nHorizontal Stack:\n", horizontal_stack)

print("\nFlattened Final Array:\n", flattened_final)
