import numpy as np

# Create a 2D array
a = np.array([[1, 2], [3, 4], [5, 6]])

# Create a tuple of slices
slices = (1, 2)

# Select the elements at the specified slices
b = a[slices]

# Print the result
print(b)
