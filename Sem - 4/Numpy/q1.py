import numpy as np

#Create a NumPy array of integers from 1 to 20.
array = np.arange(1, 21)

#Find the shape, size, and data type of the array.
shape = array.shape
size = array.size
dtype = array.dtype

print("Shape:", shape)
print("Size:", size)
print("Data Type:", dtype)

#Convert the array into float type.
float_array = array.astype(float)

print("Float Array:", float_array)

#Find the sum and mean of the array.
array_sum = float_array.sum()
array_mean = float_array.mean()
print("Sum:", array_sum)
print("Mean:", array_mean)