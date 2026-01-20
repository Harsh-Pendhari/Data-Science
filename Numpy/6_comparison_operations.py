import numpy as np

# Comparison operations using numpy

array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([15, 18, 30, 35, 60])

# Element-wise equality
equality = np.equal(array1, array2)
print("Element-wise equality:", equality) # returns results of comparison in boolean array

# Element-wise inequality
inequality = np.not_equal(array1, array2)
print("Element-wise inequality:", inequality)

# Element-wise greater than
greater_than = np.greater(array1, array2)
print("Element-wise greater than:", greater_than)

# Element-wise less than
less_than = np.less(array1, array2)
print("Element-wise less than:", less_than)

# Element-wise greater than or equal to
greater_equal = np.greater_equal(array1, array2)
print("Element-wise greater than or equal to:", greater_equal)

# Element-wise less than or equal to
less_equal = np.less_equal(array1, array2)
print("Element-wise less than or equal to:", less_equal)

# Demonstrating the use of comparison operators directly
eq_operator = (array1 == array2)
print("Element-wise equality using '==':", eq_operator)

neq_operator = (array1 != array2)
print("Element-wise inequality using '!=':", neq_operator)

arr1 = (array1 > 20)
print(arr1)

# Many such comparison operations are possible using numpy functions and operators
# Implementing conditional statements with comparison operators is also used extensively in numpy for filtering and selecting data from arrays.