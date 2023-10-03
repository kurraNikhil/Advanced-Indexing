import numpy as np

# Create a 2D array
a = np.array([[1, 2], [3, 4], [5, 6]])

# Select the elements where the first and second axes are both greater than 1
b = a[a[:, 0] > 1, a[:, 1] > 1]

# Print the result
print(b)
