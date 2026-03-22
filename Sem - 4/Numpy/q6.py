import numpy as np

# 6) Conditional Operations

# Set seed for reproducible random values.
np.random.seed(42)

# 1. Create an array of 20 random integers between 1 and 100.
arr = np.random.randint(1, 101, size=20)

# 2. Extract all even numbers.
even_numbers = arr[arr % 2 == 0]

# 3. Replace odd numbers with -1.
replaced_array = arr.copy()
replaced_array[replaced_array % 2 != 0] = -1

# 4. Count numbers divisible by 5.
count_div_by_5 = np.sum(arr % 5 == 0)

print("Original Array:", arr)
print("Even Numbers:", even_numbers)
print("Array after replacing odd numbers with -1:", replaced_array)
print("Count of numbers divisible by 5:", count_div_by_5)
