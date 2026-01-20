import numpy as np

# Broadcasting arrays using numpy
# Broadcasting allows numpy to perform operations on arrays of different shapes
# without the need for explicit replication of data.
# rules of broadcasting:
# 1. If the arrays do not have the same number of dimensions,
#    prepend the shape of the smaller-dimensional array with ones until both shapes have the same length
# 2. The sizes of the dimensions are compared element-wise from the trailing dimensions.
# 3. Two dimensions are compatible when:
#    - they are equal, or
#    - one of them is 1
# 4. If the sizes of the dimensions are not compatible, a broadcasting error is raised.

array1 = np.array([[1,2,3,4]])  # shape (1, 4)
array2 = np.array([[5],[6],[7],[8]])  # shape (4, 1)

# Broadcasting addition
result_add = array1 + array2  # shape (4, 4)
print("Broadcasting addition result:\n", result_add)

# Broadcasting multiplication
result_mul = array1 * array2  # shape (4, 4)
print("\nBroadcasting multiplication result:\n", result_mul)

# Broadcasting with different shapes
array3 = np.array([1, 2, 3])  # shape (3,)
array4 = np.array([[10],[20],[30],[40]])  # shape (4, 1)
result_sub = array4 - array3  # shape (4, 3)
print("\nBroadcasting subtraction result:\n", result_sub)

# Broadcasting with higher dimensions
array5 = np.array([[[1]], [[2]], [[3]]])  # shape (3, 1, 1)
array6 = np.array([[10, 20, 30]])  # shape (1, 3)
result_div = array5 / array6  # shape (3, 3)
print("\nBroadcasting division result:\n", result_div)

# Many more complex broadcasting scenarios can be created by combining arrays of various shapes and dimensions.
# Broadcasting is a powerful feature in numpy that simplifies code and improves performance.