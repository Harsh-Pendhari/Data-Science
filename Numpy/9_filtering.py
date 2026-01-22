import numpy as np

ages = np.array([22, 25, 30, 35, 40, 45, 50, 55, 60])

# Filter ages greater than 30
filtered_ages = ages[ages > 30]
print("Ages greater than 30:", filtered_ages)

# Filter even ages
even_ages = ages[ages % 2 == 0]
print("Even ages:", even_ages)

# Filter ages between 30 and 50
between_30_and_50 = ages[(ages >= 30) & (ages <= 50)]
print("Ages between 30 and 50:", between_30_and_50)

# Filter ages that are either less than 25 or greater than 55
less_than_25_or_greater_than_55 = ages[(ages < 25) | (ages > 55)]
print("Ages less than 25 or greater than 55:", less_than_25_or_greater_than_55)

# Filter using np.where to get indices of ages greater than 40
indices_greater_than_40 = np.where(ages > 40, ages, 0) # Return ages if condition is true, otherwise 0. 0 at the end is just a placeholder/ fill value
"""This is used when if you want to keep the original array shape but mark non-matching elements with a specific value.
Else you can directly use the formula: indices_greater_than_40 = np.where(ages > 40)"""

print("Indices of ages greater than 40:", indices_greater_than_40)
print("Ages greater than 40 using np.where:", ages[indices_greater_than_40])

# Filter using np.isin to find ages that are in a specific list
specific_ages = [25, 35, 45]
ages_in_specific_list = ages[np.isin(ages, specific_ages)]
print("Ages in the specific list [25, 35, 45]:", ages_in_specific_list)

# Negation filter: ages not equal to 30
not_equal_30 = ages[ages != 30]
print("Ages not equal to 30:", not_equal_30)

# Complex filter: ages that are even and greater than 40
even_and_greater_than_40 = ages[(ages % 2 == 0) & (ages > 40)]
print("Ages that are even and greater than 40:", even_and_greater_than_40)
