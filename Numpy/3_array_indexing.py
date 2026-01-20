import numpy as np

# Demonstrating indexing in numpy arrays
array = np.array([[10, 20, 30, 40, 50],
                  [60, 70, 80, 90, 100],
                  [110, 120, 130, 140, 150]])

print("Original array:\n", array)
# Accessing a single element (row 1, column 2)
element = array[1][2]
print("\nElement at row 1, column 2:", element)

# This method is called 'chained indexing' and is generally discouraged due to potential performance issues and unexpected behavior in some cases.
# unexpected behavior includes the possibility of returning a copy instead of a view, leading to modifications not affecting the original array.

# Recommended way is using multi-dimensional indexing method

## ARRAY SLICING #array[start:end:step]

# Accessing a single element (row 1, column 2) using multi-dimensional indexing
element_multi = array[1, 2]
print("Element at row 1, column 2 using multi-dimensional indexing:", element_multi)

# Accessing a full row (row 0)
row = array[0]
print("\nFull row 0:", row)

# Accessing a full column (column 3)
column = array[:, 3] # Using ':' to select all rows for column 3
print("Full column 3:", column)

# Accessing a sub-array (rows 0 to 1 and columns 1 to 3)
sub_array = array[0:2, 1:4] # Slicing rows and columns
print("\nSub-array (rows 0 to 1 and columns 1 to 3):\n", sub_array) 

# Accessing elements with a step (every second element in row 2)
step_elements = array[2, ::2] # Slicing with step  
print("Elements in row 2 with a step of 2:", step_elements)

# Accessing elements using negative indexing (last row, last column)
neg_index_element = array[-1, -1]
print("Element at last row, last column using negative indexing:", neg_index_element)

# Accessing a sub-array using negative indexing (last two rows and last three columns)
neg_sub_array = array[-2:, -3:]
print("\nSub-array (last two rows and last three columns) using negative indexing:\n", neg_sub_array)

# Accessing elements using a list of indices (rows 0 and 2, columns 1 and 3)
list_indexed_elements = array[[0, 2], :][:, [1, 3]]
print("Elements at rows 0 and 2, columns 1 and 3 using list of indices:\n", list_indexed_elements)

# Boolean indexing (elements greater than 100)
bool_indexed_elements = array[array > 100]
print("Elements greater than 100 using boolean indexing:", bool_indexed_elements)

# Modifying elements using indexing (setting element at row 0, column 0 to 999)
mod_arr = array[0,0] = 999
print("\nArray after modifying element at row 0, column 0 to 999:\n", array)
