import numpy as np

# Scalar arithmetic operations using numpy

array = np.array([10, 20, 30, 40, 50])

# Scalar addition
added_array = array + 5
print("After adding 5 to each element:", added_array)

# Scalar subtraction
subtracted_array = array - 3
print("After subtracting 3 from each element:", subtracted_array)

# Scalar multiplication
multiplied_array = array * 2
print("After multiplying each element by 2:", multiplied_array)

# Scalar division
divided_array = array / 4
print("After dividing each element by 4:", divided_array)

# Scalar exponentiation
exponentiated_array = array ** 2
print("After raising each element to the power of 2:", exponentiated_array)

# Scalar modulus
modulus_array = array % 6
print("After taking modulus 6 of each element:", modulus_array)

# Scalar floor division
floor_divided_array = array // 7
print("After floor dividing each element by 7:", floor_divided_array)

# There are also various numpy functions that perform element-wise operations with scalars