# Install numpy library using command: pip install numpy if not already installed
import numpy as np

list1 = [1, 2, 3, 4, 5] # Ordinary Python list
print("Original list:", list1)

list1 = list1 * 2 # Replicating the list instead of vectorized operation
print("After replicating the list:", list1)

list2 = np.array([1, 2, 3, 4, 5]) # Creating a numpy array
print("numpy array:", list2)

list2 = list2 * 2 # Vectorized operation
print("After multiplying numpy array by 2:", list2)


# Demonstrating element-wise addition
list3 = np.array([10, 20, 30, 40, 50])
print("Another numpy array:", list3)

list4 = list2 + list3 # Element-wise addition
print("Element-wise addition of two numpy arrays:", list4)

# Demonstrating element-wise division
list5 = np.array([2, 4, 5, 10, 25])
list6 = list3 / list5 # Element-wise division
print("Element-wise division of two numpy arrays:", list6)

# Demonstrating element-wise square root
list7 = np.array([4, 9, 16, 25, 36])
list8 = np.sqrt(list7) # Element-wise square root
print("Element-wise square root of numpy array:", list8)

# Demonstrating element-wise exponentiation
list9 = np.array([1, 2, 3, 4, 5])
list10 = np.exp(list9) # Element-wise exponentiation
print("Element-wise exponentiation of numpy array:", list10)

# Demonstrating element-wise sine function
list11 = np.array([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
list12 = np.sin(list11) # Element-wise sine function    
print("Element-wise sine of numpy array:", list12)

# Demonstrating element-wise logarithm
list13 = np.array([1, np.e, np.e**2, np.e**3, np.e**4])
list14 = np.log(list13) # Element-wise logarithm
print("Element-wise logarithm of numpy array:", list14)

# Demonstrating element-wise maximum
list15 = np.array([5, 10, 15, 20, 25])
list16 = np.array([3, 12, 8, 25, 20])
list17 = np.maximum(list15, list16) # Element-wise maximum  
print("Element-wise maximum of two numpy arrays:", list17)

# Demonstrating element-wise minimum
list18 = np.minimum(list15, list16) # Element-wise minimum
print("Element-wise minimum of two numpy arrays:", list18)

# Demonstrating element-wise power
list19 = np.array([2, 3, 4, 5, 6])
list20 = np.power(list19, 3) # Element-wise power  
print("Element-wise power of numpy array:", list20)

# Demonstrating element-wise absolute value
list21 = np.array([-1, -2, -3, -4, -5])
list22 = np.abs(list21) # Element-wise absolute value
print("Element-wise absolute value of numpy array:", list22)

# Demonstrating element-wise floor
list23 = np.array([1.7, 2.3, 3.9, 4.1, 5.6])    
list24 = np.floor(list23) # Element-wise floor
print("Element-wise floor of numpy array:", list24)

# Demonstrating element-wise ceiling
list25 = np.ceil(list23) # Element-wise ceiling
print("Element-wise ceiling of numpy array:", list25)

# Demonstrating element-wise rounding
list26 = np.round(list23) # Element-wise rounding
print("Element-wise rounding of numpy array:", list26)

# Demonstrating element-wise modulo operation
list27 = np.array([10, 20, 30, 40, 50])
list28 = np.array([3, 7, 4, 6, 9])
list29 = np.mod(list27, list28) # Element-wise modulo operation
print("Element-wise modulo of two numpy arrays:", list29)

# THERE ARE MANY MORE ELEMENT-WISE OPERATIONS AVAILABLE IN NUMPY. REFER TO THE NUMPY DOCUMENTATION FOR A COMPLETE LIST.
# This code demonstrates various element-wise operations using numpy arrays.
# Each operation is performed on corresponding elements of the arrays, showcasing the power of numpy for numerical computations.
