import numpy as np

# Creating a 0-dimensional array (scalar)
scalar = np.array(42)
print("0-dimensional array (scalar):", scalar)
print(scalar.ndim)  # Print number of dimensions of the array

# Creating a 1-dimensional array (vector)
vector = np.array([1, 2, 3, 4, 5])  # 1D array is just a row of elements
print("\n1-dimensional array (vector):", vector)
print(vector.ndim)

# Creating a 2-dimensional array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array is a list of lists or a matrix (rows and columns)
print("\n2-dimensional array (matrix):\n", matrix)
print(matrix.ndim)

# Creating a 3-dimensional array (tensor)
tensor = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # 3D array is a list of matrices (depth, rows, columns)
print("\n3-dimensional array (tensor):\n", tensor)
print(tensor.ndim)

## Note that the numpy arrays should have consistent dimensions in each level, i.e all rows in a matrix should have the same number of columns

# Creating a 4-dimensional array
array_4d = np.array([[[[1], [2]], [[3], [4]]], [[[5], [6]], [[7], [8]]]])  # 4D array (batches, depth, rows, columns) 
print("\n4-dimensional array:\n", array_4d)
print(array_4d.ndim)

## Note that higher-dimensional arrays (3D and above) are less common in basic applications but are used in advanced fields like deep learning and scientific computing.

# Numpy arrays shape demonstration
print("\nShape of scalar (0D array):", scalar.shape)
print("Shape of vector (1D array):", vector.shape)
print("Shape of matrix (2D array):", matrix.shape)
print("Shape of tensor (3D array):", tensor.shape)
print("Shape of 4D array:", array_4d.shape)

# shape attribute gives the dimensions of the array as a tuple eg. (rows, columns) for 2D arrays, (depth, rows, columns) for 3D arrays etc.