import numpy as np

# Create a 3D array
a = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# Select all elements along the second axis where the first axis is equal to 1
b = a[1, :, :]

# Print the result
print(b)
