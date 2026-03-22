import numpy as np

# 1. Generate 100 random numbers between 0 and 1.
random_numbers = np.random.rand(100)

# 2. Find:
mean = random_numbers.mean()
median = np.median(random_numbers)
std_dev = random_numbers.std()

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)

# 3. Count how many values are greater than 0.5.
count_greater_than_half = np.sum(random_numbers > 0.5)
print("Count of values greater than 0.5:", count_greater_than_half)

# 4. Normalize the data between 0 and 1.
normalized_data = (random_numbers - random_numbers.min()) / (random_numbers.max() - random_numbers.min())
print("Normalized Data:", normalized_data)
