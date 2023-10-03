import numpy as np

# Create a 2D array
a = np.array([[1, 2], [3, 4], [5, 6]])

# Create an ellipsis
ellipsis = ...

# Select the elements in the first and second rows, and all columns
b = a[[0, 1], ellipsis]

# Print the result
print(b)
