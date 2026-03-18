import pandas as pd

# Read CSV file

# CSV files are plain text files,A CSV file stores data as raw text
# Text can be encoded in different formats like:
# UTF-8 (default in many systems) -> Latin-1 or UTF-16, etc.
# So when you read a CSV, Pandas must decode the text correctly

df=pd.read_csv("sales_data_sample.csv",encoding="latin1")
print(df)


# Read excel file
df=pd.read_excel("SampleSuperstore.xlsx")
print(df)


# Read json file

df=pd.read_json("sample_Data.json")
print(df)
