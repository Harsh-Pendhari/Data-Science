"""A simple way to store big data sets is to use CSV files (comma separated files).
CSV files contains plain text and is a well know format that can be read by everyone including Pandas.
In our examples we will be using a CSV file called 'data.csv'."""

import pandas as pd

df = pd.read_csv(r'E:\DATA_SCIENCE\Pandas\data.csv')  # Make sure 'data.csv' is in the specified directory
print(df.to_string()) # Display the entire DataFrame. to_string() is used to avoid truncation of the output i.e it shows all rows and columns
print()

# If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:

df = pd.read_csv(r'E:\DATA_SCIENCE\Pandas\data.csv')
print(df) 
print()

## max_rows
"""The number of rows returned is defined in Pandas option settings.
You can check your system's maximum rows with the pd.options.display.max_rows statement."""

# Example
print(pd.options.display.max_rows)
print()

"""In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.
   You can change the maximum rows number with the same statement."""

# Example
"""Increase the maximum number of rows to display the entire DataFrame:"""
pd.options.display.max_rows = 9999
df = pd.read_csv(r'E:\DATA_SCIENCE\Pandas\data.csv')
print(df)
print()
