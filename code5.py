import numpy as np

# Create a 2D array
a = np.array([[1, 2], [3, 4], [5, 6]])

# Create a boolean mask
mask = np.array([True, False, True])

# Select the elements where the mask is True
b = a[mask]

# Print the result
print(b)
