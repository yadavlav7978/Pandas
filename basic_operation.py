import pandas as pd

# df.head() -> Returns the first 5 rows of the DataFrame
# Use cases:
# - Quickly preview data
# - Check if the file loaded correctly
# - Understand column structure


# df.tail() -> Returns the last 5 rows of the DataFrame
# Use case:
# - Useful for large datasets (to see latest or ending entries)


# df.info() -> Returns a summary of the DataFrame
# Includes:
# - Number of rows
# - Column names
# - Non-null values (helps detect missing data)
# - Data types (int, float, object, etc.)
# - Memory usage


# df.describe() -> Returns statistical summary of numerical columns
# Includes:
# - Count
# - Mean
# - Standard deviation (std)
# - Minimum and Maximum values
# - Quartiles (25%, 50%, 75%)

df=pd.read_csv("Data/sales_data_sample.csv",encoding="latin1")

print(df.head())
print(df.tail())
print(df.info())
print(df.describe())