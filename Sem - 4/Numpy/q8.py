import numpy as np

# 8) Sorting & Searching

# Set seed for reproducible random values.
np.random.seed(7)

# 1. Create an array of 10 random integers.
arr = np.random.randint(1, 101, size=10)

# 2. Sort the array in ascending and descending order.
ascending_order = np.sort(arr)
descending_order = np.sort(arr)[::-1]

# 3. Find maximum and minimum values.
max_value = np.max(arr)
min_value = np.min(arr)

# 4. Find index of the maximum value.
index_of_max = np.argmax(arr)

print("Original Array:", arr)
print("Ascending Order:", ascending_order)
print("Descending Order:", descending_order)
print("Maximum Value:", max_value)
print("Minimum Value:", min_value)
print("Index of Maximum Value:", index_of_max)
