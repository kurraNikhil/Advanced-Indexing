import numpy as np

# Create a 2D array
a = np.array([[1, 2], [3, 4], [5, 6]])

# Create a new axis
newaxis = np.newaxis

# Select the elements in the first row and the second column, and insert a new axis
b = a[0, newaxis, 1]

# Print the result
print(b)
