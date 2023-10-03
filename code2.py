import numpy as np

# Create a 2D array
a = np.array([[1, 2], [3, 4], [5, 6]])

# Select the first and third rows, and the second and third columns
b = a[[0, 2], [1, 2]]

# Print the result
print(b)
