## What is a DataFrame?
"""A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns."""

import pandas as pd

# Example
# Creating a simple DataFrame from a dictionary
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df)

## Locate Row
"""As you can see from the result above, the DataFrame is like a table with rows and columns.
Pandas use the loc attribute to return one or more specified row(s)"""

# Example
print(df.loc[0])  # Accessing the first row

## Locate Multiple Rows
"""To return multiple rows, you can use a list of indexes."""

# Example
print(df.loc[[0, 1]])  # Accessing the first and second rows

## Set a Custom Index
"""With the index argument, you can name your own indexes."""

# Example
df2 = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df2)

print(df2.loc["day2"])  # Accessing the row with custom index "day2"


### LOADING FILES INTO A DATAFRAME
## Load CSV File (Comma Separated Values File)
"""Pandas can read files of different formats, like CSV, JSON, HTML etc.
The most common format is CSV files."""

# # Example
df = pd.read_csv(r'E:\DATA_SCIENCE\Pandas\data.csv')  # Make sure 'data.csv' is in the same directory
print(df)