import numpy as np

# Create a 2D array
a = np.array([[1, 2], [3, 4], [5, 6]])

# Select the elements where the first and second axes are different
b = a[a[:, 0] != a[:, 1]]

# Print the result
print(b)
