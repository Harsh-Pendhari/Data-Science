## What is a Series?
"""A Pandas Series is like a column in a table.
It is a one-dimensional array holding data of any type."""

import pandas as pd

# Example
# Creating a Pandas Series from a list

lst = [10, 20, 30, 40, 50]
pdseries = pd.Series(lst)

# Displaying the Series
print(pdseries)

## Labels
"""If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.
This label can be used to access a specified value."""

# Example
print(pdseries[2])  # Accessing the value with index 2

## Creating Custom Labels
"""With the index argument, you can name your own labels."""

# Example
pdseries2 = pd.Series(lst, index=["a", "b", "c", "d", "e"])
print(pdseries2)
print(pdseries2["c"])  # Accessing the value with custom label "c"

## Key/Value Objects as Series
"""You can also create a Series by using a key/value object, like a dictionary."""

# Example
calories = {"day1": 420, "day2": 380, "day3": 390}
pdseries3 = pd.Series(calories)
print(pdseries3)
print(pdseries3["day2"])  # Accessing the value with key "day2"

## Series as Columns in a DataFrame
"""A Pandas Series can be used as a column in a DataFrame."""

# Example
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df)