# Aggregate means to summarize or combine multiple values into a single value.
# Numpy provides several aggregate functions to perform operations on arrays.

import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])

# Sum of all elements
total_sum = np.sum(array)
print("Sum of all elements:", total_sum)

# Mean of all elements
mean_value = np.mean(array)
print("Mean of all elements:", mean_value)

# Standard deviation of all elements
std_deviation = np.std(array)
print("Standard deviation of all elements:", std_deviation)

# Minimum value in the array
min_value = np.min(array)
print("Minimum value in the array:", min_value)

# Maximum value in the array
max_value = np.max(array)
print("Maximum value in the array:", max_value)

# Cumulative sum along the rows (axis=0)
cumsum_rows = np.cumsum(array, axis=0)
print("Cumulative sum along rows:\n", cumsum_rows)

# Cumulative sum along the columns (axis=1)
cumsum_columns = np.cumsum(array, axis=1)
print("Cumulative sum along columns:\n", cumsum_columns)

# Product of all elements
product_all = np.prod(array)
print("Product of all elements:", product_all)

# Variance of all elements
variance_value = np.var(array)
print("Variance of all elements:", variance_value)

# Median of all elements
median_value = np.median(array)
print("Median of all elements:", median_value)

# Count of non-zero elements
non_zero_count = np.count_nonzero(array)
print("Count of non-zero elements:", non_zero_count)

# These aggregate functions can also be applied along specific axes of the array.
# For example, sum along columns (axis=0)
sum_columns = np.sum(array, axis=0)
print("Sum along columns:", sum_columns)

# Sum along rows (axis=1)
sum_rows = np.sum(array, axis=1)
print("Sum along rows:", sum_rows)

# Similarly, other aggregate functions can be applied along specific axes as needed.
# These aggregate functions are essential for data analysis and statistical computations using numpy.
# They help in summarizing large datasets efficiently.
# Numpy's aggregate functions are optimized for performance and can handle large arrays effectively.
# There are many more aggregate functions available in numpy for various statistical and mathematical operations.