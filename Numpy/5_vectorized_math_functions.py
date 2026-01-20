import numpy as np

# Vectorized math functions using numpy

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])

# Demonstrating element-wise addition
added_array = np.add(array1, array2)
print("Element-wise addition of two numpy arrays:", added_array)

# Demonstrating element-wise subtraction
subtracted_array = np.subtract(array2, array1)
print("Element-wise subtraction of two numpy arrays:", subtracted_array)

# Demonstrating element-wise multiplication
multiplied_array = np.multiply(array1, array2)
print("Element-wise multiplication of two numpy arrays:", multiplied_array)

# Demonstrating element-wise division
divided_array = np.divide(array2, array1)
print("Element-wise division of two numpy arrays:", divided_array)

# Demonstrating element-wise power
powered_array = np.power(array1, array2)
print("Element-wise power of two numpy arrays:", powered_array)

