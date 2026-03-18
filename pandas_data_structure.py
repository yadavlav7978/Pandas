# Pandas has two main data structures
# 🔹 1. Series (1D Data Structure)
# 🔹 2. DataFrame (2D Data Structure)

# 📌 What is Series?
# A Series is a one-dimensional labeled array that can hold any data type integer,float,string,boolean,etc
# 👉 Think of it like: A single column in Excel Or a list with labels (index)

# 📌 What is DataFrame?
# A DataFrame is a two-dimensional labeled data structure similar to table in database
# It has rows and columns
# 👉 Think of it like: An entire Excel sheet,A SQL table or A dictionary of Series

import pandas as pd

# Creating a Series
s=pd.Series([1,2,3,4,5])
print(s)

# Creating a DataFrame
data={
    "name":["Lav","Rahul"],
    "age":[20,21],
    "marks":[45,49]
}

df=pd.DataFrame(data)
print(df)


# Creating a DataFrame
df=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=["A","B","C"])
print(df)

# Creating a DataFrame from a dictionary
df=pd.DataFrame({"A":[1,2,3],"B":[4,5,6],"C":[7,8,9]})
print(df)