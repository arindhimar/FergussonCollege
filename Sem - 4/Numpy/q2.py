import numpy as np

# Create an array of 15 random integers between 10 and 50
random_array = np.random.randint(10, 51, size=15)
print("Original Array:", random_array)

# Extract first 5 elements
first_five = random_array[:5]
print("First 5 elements:", first_five)

# Extract last 5 elements
last_five = random_array[-5:]
print("Last 5 elements:", last_five)

# Replace all values greater than 30 with 0
random_array[random_array > 30] = 0

print("Array after replacing values greater than 30 with 0:", random_array)

# Print elements at even indices
even_indices_elements = random_array[::2]
print("Elements at even indices:", even_indices_elements)