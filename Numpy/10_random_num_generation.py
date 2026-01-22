import numpy as np

# Random number generation examples
rng = np.random.default_rng()  # You can set a seed getting the same random numbers every time
print(rng.integers(1, 10))   # Random integer between 1 and 10 (Last number is exclusive, so its actually between 1 and 9)

# Random number with size
print(rng.integers(1, 10, size=5))  # 1D Array of 5 random integers between 1 and 9

# We can set the array shape using a tuple
print(rng.integers(1, 10, size=(3, 4)))  # 2D Array of shape (3,4) with random integers between 1 and 9

# Generate a random float between 0 and 1
print(rng.random())  # Random float between 0 and 1

# Shuffling an array
arr = np.array([1, 2, 3, 4, 5])
rng.shuffle(arr)
print(arr)  # Shuffled array

# Random choice from an array
choices = rng.choice(arr, size=3, replace=False)  # Choose 3 unique
"""If you want a single random element, you can remove the size and replace parameters
    And if you want to allow duplicates, set replace=True
    If you want to set weights for each element, you can use the p parameter
    Weights mean the probability of each element being chosen
    """
print(choices)  # Randomly chosen elements from arr

# These are just a few examples of random number generation using NumPy. There are many more functions and options available in the numpy.random module.
# These are basic examples to get you started with random number generation in NumPy.